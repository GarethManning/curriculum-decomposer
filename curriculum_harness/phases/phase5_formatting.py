"""Phase 5 — structure LTs into competency-grouped, level-aware output."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

from curriculum_harness._anthropic import beta_messages_create, get_async_client, response_text_content
from curriculum_harness.output_naming import next_available_structured_lts_paths
from curriculum_harness.state import DecomposerState
from curriculum_harness.types import (
    SONNET_MODEL,
    ArchitectureDiagnosis,
    ArchitectureStrand,
    StructuredLT,
    extract_json_object,
    resolve_lt_statement_format,
)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

DEMAND_LEVELS = ["concrete", "transitional", "abstract"]


def _effective_levels(output_structure: dict[str, Any]) -> list[dict[str, str]]:
    levels = list(output_structure.get("levels") or [])
    if not output_structure.get("generate_adjacent"):
        return levels
    adjacent_count = int(output_structure.get("adjacent_count") or 0)
    if adjacent_count <= 0:
        return levels

    expanded: list[dict[str, str]] = []
    for level in levels:
        base_demand = str(level.get("cognitive_demand", "transitional")).lower()
        try:
            base_i = DEMAND_LEVELS.index(base_demand)
        except ValueError:
            base_i = 1
        for offset in range(-adjacent_count, adjacent_count + 1):
            i = max(0, min(len(DEMAND_LEVELS) - 1, base_i + offset))
            if offset == 0:
                expanded.append(level)
            else:
                expanded.append(
                    {
                        "id": f"{level.get('id')}_adj_{offset:+d}",
                        "label": f"{level.get('label')} (adj {offset:+d})",
                        "age_range": str(level.get("age_range", "")),
                        "cognitive_demand": DEMAND_LEVELS[i],
                    }
                )
    return expanded


def _competency_name_variants(competency_name: str) -> list[str]:
    raw = competency_name.strip()
    if not raw:
        return []
    head = raw.split("→")[0].split("–")[0].strip()
    out = [raw]
    if head and head.lower() != raw.lower():
        out.append(head)
    return out


def _competency_relevance_score(lt: dict[str, Any], competency_name: str) -> float:
    ks = str(lt.get("kud_source", ""))
    detail = ks.split(":", 1)[1].strip().lower() if ":" in ks else ks.lower()
    blob = f"{ks} {detail} {lt.get('statement', '')}".lower()
    if not blob.strip():
        return 0.0
    best = 0.0
    for variant in _competency_name_variants(competency_name):
        name = variant.lower()
        if name and name in blob:
            return 1.0
        words = [w for w in re.split(r"[^\w]+", name) if len(w) > 2]
        if not words:
            continue
        hits = sum(1 for w in set(words) if w in blob)
        best = max(best, hits / len(set(words)))
    return best


def _lt_type_int(lt: dict[str, Any]) -> int:
    t = int(lt.get("type") or 1)
    return t if t in (1, 2, 3) else 1


def _assignable_strands_for_type(strands: list[ArchitectureStrand], T: int) -> list[ArchitectureStrand]:
    """Type-first: only strands in the correct lane; content_theme never assignable."""
    out: list[ArchitectureStrand] = []
    for s in strands:
        if s.lane == "content_theme":
            continue
        if T == 1 and s.lane == "hierarchical":
            if not s.expected_lt_types or 1 in s.expected_lt_types:
                out.append(s)
        elif T == 2 and s.lane == "horizontal_analytical":
            if not s.expected_lt_types or 2 in s.expected_lt_types:
                out.append(s)
        elif T == 3 and s.lane == "dispositional":
            if not s.expected_lt_types or 3 in s.expected_lt_types:
                out.append(s)
    return out


def _lane_relaxed_strands_for_type(strands: list[ArchitectureStrand], T: int) -> list[ArchitectureStrand]:
    """Same lane as T, ignore expected_lt_types (still never content_theme)."""
    out: list[ArchitectureStrand] = []
    for s in strands:
        if s.lane == "content_theme":
            continue
        if T == 1 and s.lane == "hierarchical":
            out.append(s)
        elif T == 2 and s.lane == "horizontal_analytical":
            out.append(s)
        elif T == 3 and s.lane == "dispositional":
            out.append(s)
    return out


def map_lt_to_strand_label(lt: dict[str, Any], strands: list[ArchitectureStrand]) -> tuple[str, bool]:
    """
    Map one LT to a strand label for Phase 5 grouping. Similarity is tiebreaker only among
    strands that already pass lane + expected_lt_types. Exported for tests.
    """
    if not strands:
        return "", True
    T = _lt_type_int(lt)
    candidates = _assignable_strands_for_type(strands, T)
    kind_relaxed = False
    if not candidates:
        candidates = _lane_relaxed_strands_for_type(strands, T)
        kind_relaxed = bool(candidates)
    if not candidates:
        return "", True

    scored = [(s.label, _competency_relevance_score(lt, s.label)) for s in candidates]
    scored.sort(key=lambda x: -x[1])
    best_name, best_s = scored[0]
    second_s = scored[1][1] if len(scored) > 1 else -1.0

    uncertain = kind_relaxed
    if (
        not uncertain
        and len(scored) > 1
        and best_s >= 0.35
        and second_s >= 0.35
        and (best_s - second_s) < 0.05
    ):
        uncertain = True

    return best_name, uncertain


_HISTORY_CIVIC_DRIFT = re.compile(
    r"\b(school council|classroom rules|playground rules|rules in my community|rules in my school|"
    r"my school community|good citizen|citizenship class|following rules at school|"
    r"basic rules in my community)\b",
    re.I,
)

_T2_ANALYTICAL_IN_T3 = re.compile(
    r"(evaluate|assess|analy[sz]e).{0,40}(reliability|bias|perspective).{0,30}source|"
    r"reliability.{0,20}historical source|"
    r"interpret.{0,30}as evidence|"
    r"compare.{0,40}sources?.{0,20}(to|for) construct|"
    r"perspective of different historical sources",
    re.I | re.DOTALL,
)

_T2_LIKE_FOR_T1 = re.compile(
    r"\bevaluate\s+the\s+reliability\b|\bcompare\s+multiple\s+interpretations\b|"
    r"\bjudge\s+which\s+source\b",
    re.I,
)

_T3_LIKE_FOR_T2 = re.compile(
    r"^\s*i can (be|show|demonstrate) (curiosity|open[- ]mindedness|persistence|empathy)\b",
    re.I,
)


def _statement_domain_drift(subject: str, statement: str) -> bool:
    subj = (subject or "").strip().lower()
    if "history" in subj or subj == "":
        return bool(_HISTORY_CIVIC_DRIFT.search(statement))
    return False


def _statement_type_drift(lt_type: int, statement: str) -> bool:
    if lt_type == 3:
        return bool(_T2_ANALYTICAL_IN_T3.search(statement))
    if lt_type == 1:
        return bool(_T2_LIKE_FOR_T1.search(statement))
    if lt_type == 2:
        return bool(_T3_LIKE_FOR_T2.search(statement))
    return False


def _level_statement_validation_flags(
    subject: str,
    lt_type: int,
    level_statements: dict[str, str],
) -> list[str]:
    """Required v1.2 checks on all generated level columns."""
    domain_hit = False
    type_hit = False
    for stmt in level_statements.values():
        st = (stmt or "").strip()
        if not st:
            continue
        if _statement_domain_drift(subject, st):
            domain_hit = True
        if _statement_type_drift(lt_type, st):
            type_hit = True
    out: list[str] = []
    if domain_hit:
        out.append("LEVEL_STATEMENT_DOMAIN_DRIFT")
    if type_hit:
        out.append("LEVEL_STATEMENT_TYPE_DRIFT")
    return out


def _level_statement_fallback(statement: str, fmt: str, max_words: int = 20) -> str:
    """Anchor column fallback when the model omits a level cell (v1.3: word cap for all formats)."""
    s = (statement or "").strip()
    if not s:
        return ""
    words = s.split()
    return " ".join(words[:max_words])


def _phase5_lt_format_rules_block() -> str:
    return (
        "Each learning target row includes `lt_statement_format`. Apply it to that row only:\n"
        "- i_can: lt_definition must start with 'I can ' and be <=15 words; each level_statement must "
        "start with 'I can ' and be <=20 words.\n"
        "- outcome_statement: no 'I can' prefix; plain student-facing outcomes; lt_definition <=15 words; "
        "each level_statement <=20 words.\n"
        "- competency_descriptor: third-person competency clause (e.g. Uses…, Demonstrates…); no 'I can' "
        "and no first person; lt_definition <=15 words; each level_statement <=20 words.\n"
    )




def _type_label(lt: dict[str, Any]) -> str:
    t = int(lt.get("type") or 1)
    return f"T{t}" if t in (1, 2, 3) else "T1"


async def _format_competency_batch(
    competency: str,
    items: list[dict[str, Any]],
    levels: list[dict[str, str]],
    subject: str,
    grade: str,
    anchor_level_id: str,
    profile_fmt: str,
) -> list[dict[str, Any]]:
    client = get_async_client()
    level_payload = []
    for lvl in levels:
        lid = str(lvl.get("id"))
        level_payload.append(
            {
                "id": lid,
                "label": str(lvl.get("label", lid)),
                "cognitive_demand": str(lvl.get("cognitive_demand", "")),
                "is_anchor": bool(anchor_level_id and lid == anchor_level_id),
            }
        )
    payload = {
        "competency": competency,
        "subject": subject,
        "grade": grade,
        "anchor_level_id": anchor_level_id,
        "levels": level_payload,
        "learning_targets": [
            {
                "idx": i,
                "statement": x["statement"],
                "knowledge_type": x["knowledge_type"],
                "kud_source": x["kud_source"],
                "type": x["type"],
                "lt_statement_format": str(x.get("lt_statement_format") or "").strip() or profile_fmt,
            }
            for i, x in enumerate(items)
        ],
    }
    subj = subject.strip() or "this subject"
    gr = grade.strip() or "this grade"
    anchor = anchor_level_id.strip() or "(see levels marked is_anchor)"
    comp_def_rules = (
        f"For each row, competency_definition must be ONE sentence defining this competency group "
        f"as it applies to {subj} at {gr} level. "
        "Do NOT echo, restate, or lightly paraphrase the group name or internal slug (e.g. snake_case). "
        "Write a genuine description of what students in this competency group are learning to do. "
        "Example format: 'The ability to locate, sequence, and interpret geographical and chronological "
        "information as foundations for historical analysis.' "
        "(Use different wording per row; this is style only.) "
    )
    fmt_rules = _phase5_lt_format_rules_block()
    system = (
        "You convert learning targets into a structured competency table. Return ONLY JSON object with "
        "'rows' list. Each row must have keys: idx, competency_definition, lt_name, lt_definition, "
        "level_statements. "
        f"{comp_def_rules}"
        f"{fmt_rules}"
        "Constraints: lt_name 2-4 words; obey lt_statement_format per row for lt_definition and "
        "level_statements; align each level statement to its cognitive_demand (concrete/transitional/abstract). "
        "level_statements MUST be an object whose keys are EXACTLY the strings in levels[].id from "
        "the input payload (no other keys). "
        f"Domain: all level statements must stay within {subj} — do not drift to unrelated subjects "
        f"(e.g. generic citizenship or school rules when the subject is history). "
        "Type lock: for each row, every entry in level_statements must preserve that row's learning target "
        "type from field 'type' (1=hierarchical knowledge, 2=horizontal/analytical, 3=dispositional). "
        "A T3 disposition must remain a disposition at every level (habits, stance, curiosity, persistence) "
        "— never rewrite it as T2 analytical skills such as evaluating source reliability. "
        "Similarly, do not rewrite T1 or T2 rows into the wrong type. "
        f"The anchor curriculum level id is '{anchor}'; levels with is_anchor true match the original LT; "
        "other level ids may be adjacent cognitive levels — still obey domain and type lock for those too."
    )
    msg = await beta_messages_create(
        client,
        model=SONNET_MODEL,
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": system},
                    {"type": "text", "text": json.dumps(payload, ensure_ascii=True)},
                ],
            }
        ],
        label=f"phase5_format_{competency[:24]}",
    )
    text = response_text_content(msg)
    parsed = extract_json_object(text) or {}
    rows = parsed.get("rows") if isinstance(parsed, dict) else None
    if isinstance(rows, list):
        return [r for r in rows if isinstance(r, dict)]
    return []


def _flag_duplicate_lt_names(structured_lts: list[StructuredLT]) -> None:
    from collections import Counter

    names = [str(row.get("lt_name") or "").strip() for row in structured_lts]
    counts = Counter(names)
    dup = {n for n, c in counts.items() if n and c > 1}
    if not dup:
        return
    for row in structured_lts:
        if str(row.get("lt_name") or "").strip() in dup:
            flags = list(row.get("flags") or [])
            if "DUPLICATE_LT_NAME" not in flags:
                flags.append("DUPLICATE_LT_NAME")
            row["flags"] = list(dict.fromkeys(flags))


def _write_phase5_outputs(
    out_dir: Path,
    run_id: str,
    structured_lts: list[StructuredLT],
    levels: list[dict[str, str]],
) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path, csv_path = next_available_structured_lts_paths(out_dir, run_id)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"structured_lts": structured_lts}, f, indent=2, ensure_ascii=False)

    level_cols = [str(level.get("label", level.get("id", ""))) for level in levels]
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "Competency",
                "Competency Definition",
                "LT Name",
                "LT Definition",
                *level_cols,
                "Knowledge Type",
                "Flags",
            ]
        )
        for row in structured_lts:
            cells = [
                row["competency"],
                row["competency_definition"],
                row["lt_name"],
                row["lt_definition"],
            ]
            for lvl in levels:
                cells.append(str(row["level_statements"].get(str(lvl.get("id")), "")))
            cells.append(row["knowledge_type"])
            cells.append("|".join(row["flags"]))
            writer.writerow(cells)
    return json_path, csv_path


async def phase5_formatting(state: DecomposerState) -> dict[str, Any]:
    output_structure = state.get("output_structure") or (state.get("config") or {}).get("outputStructure")
    if not output_structure:
        return {"current_phase": "phase5:skipped", "structured_lts": []}

    lts = list(state.get("learning_targets") or [])
    arch = state.get("architecture_diagnosis") or {}
    input_level_id = str(output_structure.get("input_level_id") or "")
    run_id = str(state.get("run_id") or "run")
    subject = str(state.get("subject") or "")
    grade = str(state.get("grade") or "")
    review = list(state.get("human_review_queue") or [])
    errs = list(state.get("errors") or [])

    profile_fmt = resolve_lt_statement_format(dict(state.get("curriculum_profile") or {}))

    levels = _effective_levels(output_structure)

    diagnosis = ArchitectureDiagnosis.from_dict(arch)
    if not diagnosis.strands:
        return {
            "current_phase": "phase5:skipped",
            "errors": errs + ["phase5: skipped — architecture_diagnosis has no strands"],
            "human_review_queue": review,
            "structured_lts": [],
            "phase5_summary": {},
        }

    by_comp: dict[str, list[dict[str, Any]]] = {}
    uncertain_count = 0
    skipped_no_strand = 0
    for lt in lts:
        comp, uncertain = map_lt_to_strand_label(lt, diagnosis.strands)
        if not comp:
            skipped_no_strand += 1
            continue
        row = dict(lt)
        row["_uncertain"] = uncertain
        by_comp.setdefault(comp, []).append(row)
        if uncertain:
            uncertain_count += 1
    if skipped_no_strand:
        errs.append(
            f"phase5: {skipped_no_strand} learning targets had no assignable strand "
            "(e.g. missing horizontal_analytical strands for T2 — re-run Phase 2)."
        )

    structured: list[StructuredLT] = []
    group_counts: dict[str, int] = {}
    for comp, comp_lts in by_comp.items():
        rows = await _format_competency_batch(
            comp,
            comp_lts,
            levels,
            subject,
            grade,
            anchor_level_id=input_level_id,
            profile_fmt=profile_fmt,
        )
        rows_by_idx = {int(r.get("idx")): r for r in rows if str(r.get("idx", "")).isdigit()}

        for i, lt in enumerate(comp_lts):
            gen = rows_by_idx.get(i, {})
            flags = list(lt.get("flags") or [])
            if lt.get("_uncertain"):
                flags.append("COMPETENCY_MAPPING_UNCERTAIN")
            row_fmt = str(lt.get("lt_statement_format") or "").strip() or profile_fmt
            level_statements = {}
            for lvl in levels:
                lvl_id = str(lvl.get("id"))
                val = ""
                if isinstance(gen.get("level_statements"), dict):
                    val = str(gen["level_statements"].get(lvl_id, "")).strip()
                if (
                    not val
                    and input_level_id
                    and lvl_id == input_level_id
                ):
                    val = _level_statement_fallback(str(lt.get("statement", "")), row_fmt)
                level_statements[lvl_id] = val

            lt_type_i = _lt_type_int(lt)
            for drift_flag in _level_statement_validation_flags(subject, lt_type_i, level_statements):
                if drift_flag not in flags:
                    flags.append(drift_flag)

            structured.append(
                {
                    "competency": comp,
                    "competency_definition": str(gen.get("competency_definition", "")).strip(),
                    "lt_name": str(gen.get("lt_name", "")).strip(),
                    "lt_definition": str(gen.get("lt_definition", "")).strip(),
                    "level_statements": level_statements,
                    "knowledge_type": _type_label(lt),
                    "flags": list(dict.fromkeys(flags)),
                    "lt_statement_format": row_fmt,
                }
            )
        group_counts[comp] = len(comp_lts)

    _flag_duplicate_lt_names(structured)
    orp = str(state.get("output_path_resolved") or "").strip()
    out_dir_p = Path(orp).resolve() if orp else (REPO_ROOT / "outputs")
    json_path, csv_path = _write_phase5_outputs(out_dir_p, run_id, structured, levels)
    review.append(
        {
            "item_type": "phase5_outputs",
            "summary": "Structured outputs generated.",
            "decision_needed": f"CSV: {csv_path} | JSON: {json_path}",
        }
    )
    return {
        "current_phase": "phase5:complete",
        "errors": errs,
        "human_review_queue": review,
        "structured_lts": structured,
        "phase5_summary": {
            "group_counts": group_counts,
            "level_columns": [str(level.get("label", level.get("id", ""))) for level in levels],
            "mapping_uncertain_count": uncertain_count,
            "json_path": str(json_path),
            "csv_path": str(csv_path),
        },
    }

