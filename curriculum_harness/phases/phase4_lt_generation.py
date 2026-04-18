"""Phase 4 — learning targets via MCP learning-target-authoring-guide (per KUD item)."""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import Any

from curriculum_harness._anthropic import (
    AnthropicCallTimeout,
    beta_messages_create,
    get_async_client,
    mcp_servers_param,
    mcp_toolset_single_tool,
    response_debug_dump,
    response_text_content,
)
from curriculum_harness.phases.phase3_kud import is_recall_only_know_content
from curriculum_harness.source_faithfulness import (
    SOURCE_FAITHFULNESS_FAIL_FLAG,
    compute_parent_provenance,
    compute_source_provenance,
)
from curriculum_harness.state import DecomposerState
from curriculum_harness.types import (
    HE_DISPOSITION_INFERRED,
    HumanReviewItem,
    KUD,
    KUDItem,
    LearningTarget,
    SONNET_MODEL,
    extract_json_array,
    extract_json_object,
    resolve_lt_statement_format,
)

TOOL_NAME = "learning-target-authoring-guide"

TYPE_FRAMEWORK_FOR_LT = """Learning target types (wording must match the assigned type number for this KUD item):

Type 1 — Hierarchical knowledge. Assessed via criterion-referenced rubric. Criteria describe what was specifically and correctly demonstrated. Standards are relatively well-defined.

Type 2 — Horizontal or perspectival knowledge. Assessed via criterion-referenced rubric. Criteria describe quality of knowledge and reasoning together on a continuum — these cannot be separated in horizontal subjects. Multiple valid interpretations exist; quality is judged on depth and sophistication.

Type 3 — Dispositional knowledge. Assessed primarily via multi-informant observation protocol. A single-point rubric (competent descriptor only) may be appropriate for student self-assessment contexts. Do not generate five-level rubric language for Type 3 LTs.

All three types use criterion-referenced assessment. A compound LT that requires both horizontal knowledge (Type 2) and dispositional enactment (Type 3) should be flagged COMPOUND_TYPE, not silently assigned one type.

This framework is designed for schools generally — not for any specific school. The type system should work whether a school uses grade levels, multi-grade bands, key stages, or any other leveling structure."""

LT_ACTION_RULES_ICAN = """Additional generation rules:
Rule 1 — No "demonstrate understanding" language:
- "Demonstrate understanding" and "show understanding" are not observable.
- Replace with observable actions: constructs, orders, analyses, evaluates, explains, applies, identifies, interprets.
- Never use "understanding" as the primary verb or as the object of "demonstrate".

Rule 2 — No rote recall as a component of a substantive LT:
- If a KUD item contains both a recall element (dates, names, definitions) AND a substantive task, write the LT for the substantive task ONLY.
- If a KUD item is purely recall with no substantive task, skip it entirely — do not generate an LT.
- Treat rote recall as scaffolding, not the target itself.
- Example: recall dates + construct sequences → "I can construct chronological sequences that show cause-effect relationships."

Rule 3 — The statement must lead with a specific observable action verb after the required prefix.
- Vague verbs (understand, know, appreciate) are acceptable only for Type 3 with explicit observational framing.
"""

LT_ACTION_RULES_NEUTRAL = """Additional generation rules:
Rule 1 — No "demonstrate understanding" language; use observable actions (analyses, evaluates, explains, applies, identifies, interprets, describes, compares).
Rule 2 — Same recall vs substantive rule as for I-can mode: write the substantive task only; skip pure recall items.
Rule 3 — Lead with strong observable language appropriate to the output format (see hard rules below).
"""

GCSE_AQA_EXAM_BLOCK = """
GCSE / AQA assessment awareness (this document is an exam specification):
- Prefer command words that match typical AQA History assessments: describe, explain, analyse, evaluate, assess, compare — choose the level that fits the KUD (do not use "evaluate" for a purely descriptive KUD).
- Align demand with how papers reward responses: shorter AO1-style recall/description vs extended AO2/AO3 analysis — match the KUD's assessment_route and knowledge depth.
- Use wording that could plausibly appear in level-marked schemes: specific, evidential, discriminating — avoid vague "understand the topic" phrasing.
- Do not invent mark totals or tariff numbers unless the KUD text cites them.
"""

HE_SUPPLEMENT_MAX = 3
HE_RAW_EXCERPT_CHARS = 60_000
HE_COSINE_DEDUP_THRESHOLD = 0.92

RUBRIC_TERMS = (
    "rubric",
    "criteria",
    "proficient",
    "emerging",
    "level 1",
    "level 2",
    "level 3",
    "level 4",
    "achievement chart",
    "scoring guide",
)

VERB_HINTS = (
    " analyze ",
    " explain ",
    " describe ",
    " compare ",
    " evaluate ",
    " demonstrate ",
    " identify ",
    " interpret ",
    " apply ",
    " create ",
    " solve ",
    " use ",
    " understand ",
    " assess ",
    " revise ",
)

ICAN_PREFIX = "I can "


def _tokenize_for_cosine(s: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", (s or "").lower())


def cosine_similarity_text(a: str, b: str) -> float:
    """Token-frequency cosine similarity in [0, 1]; stdlib only."""
    ta = _tokenize_for_cosine(a)
    tb = _tokenize_for_cosine(b)
    if not ta or not tb:
        return 0.0
    ca = Counter(ta)
    cb = Counter(tb)
    vocab = set(ca) | set(cb)
    dot = sum(ca.get(w, 0) * cb.get(w, 0) for w in vocab)
    na = math.sqrt(sum(c * c for c in ca.values()))
    nb = math.sqrt(sum(c * c for c in cb.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def _max_cosine_to_corpus(stmt: str, corpus: list[str]) -> float:
    if not stmt.strip():
        return 0.0
    return max((cosine_similarity_text(stmt, c) for c in corpus if c.strip()), default=0.0)


def _hard_rules_for_format(fmt: str) -> str:
    if fmt == "i_can":
        return (
            f'Hard rules: the statement must begin exactly with {ICAN_PREFIX!r} (capital I, lowercase can, one space); '
            "max 25 words; single construct; no parenthetical examples."
        )
    if fmt == "outcome_statement":
        return (
            "Hard rules: write ONE plain student-facing outcome statement — **no** 'I can' prefix. "
            "Start with an observable verb or short noun phrase (e.g. 'Describes…', 'Explains…', 'Analyses…'). "
            "Max 25 words; single construct; no parenthetical examples."
        )
    if fmt == "competency_descriptor":
        return (
            "Hard rules: write ONE third-person competency-style clause (e.g. 'Uses evidence to…', 'Applies…', 'Demonstrates…'). "
            "**No** 'I can' and **no** first-person. Max 25 words; single construct; no parenthetical examples."
        )
    return _hard_rules_for_format("i_can")


def _action_rules_for_format(fmt: str) -> str:
    return LT_ACTION_RULES_ICAN if fmt == "i_can" else LT_ACTION_RULES_NEUTRAL


def _system_direct_for_format(fmt: str) -> str:
    rules = _hard_rules_for_format(fmt)
    ar = _action_rules_for_format(fmt)
    return f"""You write ONE measurable learning target per request.

{TYPE_FRAMEWORK_FOR_LT}
{ar}

{rules}

Output ONLY JSON: {{"statement": str}}
"""


def _primary_type_from_assessment_route(route: str) -> int:
    r = (route or "").lower()
    if "observation" in r:
        return 3
    if any(x in r for x in ("reasoning", "interpret", "analytical", "judgment", "essay")):
        return 2
    return 2


def _fallback_type_from_route(route: str) -> int:
    r = (route or "").lower()
    if "observation" in r:
        return 3
    if any(x in r for x in ("reasoning", "interpret", "analytical", "judgment", "essay")):
        return 2
    return 1


def _lt_type_and_compound(item: KUDItem) -> tuple[int, bool]:
    kt = (item.knowledge_type or "").strip().lower()
    route = item.assessment_route or ""
    body = f"{item.content or ''} {item.notes or ''}".lower()

    h_hier = "hierarchical" in kt
    h_horiz = "horizontal" in kt
    h_disp = "dispositional" in kt or "disposition" in kt

    horiz_and_disp_tags = h_horiz and h_disp
    horiz_tag_disp_in_body = h_horiz and (
        "dispositional" in body or "disposition" in body or "dispositions" in body
    )
    disp_tag_horiz_in_body = h_disp and (
        "horizontal" in body or "perspectival" in body or "perspective" in body
    )

    if "mixed" in kt or horiz_and_disp_tags or horiz_tag_disp_in_body or disp_tag_horiz_in_body:
        return _primary_type_from_assessment_route(route), True

    if h_hier and h_horiz and not h_disp:
        return 1, False
    if h_hier and h_disp and not h_horiz:
        return _fallback_type_from_route(route), False
    if h_horiz and h_hier and not h_disp:
        return 1, False

    if h_hier and not h_horiz and not h_disp:
        return 1, False
    if h_horiz and not h_hier and not h_disp:
        return 2, False
    if h_disp and not h_hier and not h_horiz:
        return 3, False

    return _fallback_type_from_route(route), False


def _validate_lt(lt: LearningTarget, *, compound_type: bool, fmt: str) -> list[str]:
    flags = list(lt.flags)
    stmt = (lt.statement or "").strip()
    words = stmt.split()
    wc = len(words)
    lt.word_count = wc

    if not stmt:
        flags.append("MISSING_LT_STATEMENT")
    elif fmt == "i_can":
        if not stmt.startswith(ICAN_PREFIX):
            flags.append("MISSING_I_CAN_FORMAT")
    elif fmt == "outcome_statement":
        if stmt.lower().startswith("i can "):
            flags.append("LT_FORMAT_EXPECTATION_MISMATCH")
    elif fmt == "competency_descriptor":
        low = stmt.lower()
        if low.startswith("i can ") or low.startswith("i "):
            flags.append("LT_FORMAT_EXPECTATION_MISMATCH")

    if compound_type:
        flags.append("COMPOUND_TYPE")
    if wc > 25:
        flags.append("EXCEEDS_WORD_LIMIT")
    lower = stmt.lower()
    if fmt == "i_can" and " and " in lower:
        parts = re.split(r"\s+and\s+", lower, maxsplit=1)
        if len(parts) == 2:
            v0 = any(v in f" {parts[0]} " for v in VERB_HINTS)
            v1 = any(v in f" {parts[1]} " for v in VERB_HINTS)
            if v0 and v1:
                flags.append("POSSIBLE_COMPOUND")
    if re.search(r"\([^)]+\)", stmt):
        flags.append("EMBEDDED_EXAMPLE")
    if lt.type == 3:
        rub = any(t in lower for t in RUBRIC_TERMS)
        if rub:
            flags.append("DISPOSITION_RUBRIC_ERROR")
    return list(dict.fromkeys(flags))


async def _direct_lt(kud_line: str, assigned_type: int, fmt: str) -> LearningTarget:
    client = get_async_client()
    system = _system_direct_for_format(fmt)
    msg = await beta_messages_create(
        client,
        model=SONNET_MODEL,
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": system},
                {
                    "type": "text",
                    "text": (
                        f"KUD element:\n{kud_line}\n"
                        f"Assigned learning target type (from knowledge_type taxonomy): {assigned_type}"
                    ),
                },
            ],
        }],
        label="phase4_sonnet_direct_lt",
    )
    text = response_text_content(msg)
    parsed = extract_json_object(text) or {}
    stmt = str(parsed.get("statement", "")).strip()
    lt = LearningTarget(
        statement=stmt,
        type=assigned_type,
        word_count=len(stmt.split()),
        lt_statement_format=fmt,
    )
    return lt


def _format_kud_line(bucket: str, item: KUDItem) -> str:
    return (
        f"[{bucket}] {item.content}\n"
        f"knowledge_type={item.knowledge_type}; assessment_route={item.assessment_route}\n"
        f"notes={item.notes}"
    )


async def _he_dispositional_supplement(
    *,
    raw_curriculum: str,
    subject: str,
    grade: str,
    jurisdiction: str,
    fmt: str,
    existing_statements: list[str],
) -> list[LearningTarget]:
    excerpt = (raw_curriculum or "")[:HE_RAW_EXCERPT_CHARS].strip()
    if len(excerpt) < 400:
        return []

    subj = subject.strip() or "the course"
    gr = grade.strip() or "this level"
    juris = jurisdiction.strip() or "the institution"
    rules = _hard_rules_for_format(fmt)
    system = (
        "You infer implicit graduate-level dispositions from a higher-education syllabus excerpt. "
        "Dispositions include (examples only): critical judgement, independent scholarship, tolerance of ambiguity, "
        "intellectual humility, sustained inquiry. "
        f"Return ONLY a JSON array of at most {HE_SUPPLEMENT_MAX} objects, each "
        '{"statement": "<single disposition phrased as a learning outcome>"}. '
        "Each must be assessable via multi-informant observation (no exam-style source analysis). "
        f"Subject context: {subj} at {gr} ({juris}).\n"
        f"{rules}"
    )
    client = get_async_client()
    msg = await beta_messages_create(
        client,
        model=SONNET_MODEL,
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": system},
                {"type": "text", "text": f"Syllabus excerpt:\n\n{excerpt}"},
            ],
        }],
        label="phase4_he_disposition_supplement",
    )
    text = response_text_content(msg)
    arr = extract_json_array(text) or []
    out: list[LearningTarget] = []
    corpus = list(existing_statements)
    for item in arr:
        if len(out) >= HE_SUPPLEMENT_MAX:
            break
        if not isinstance(item, dict):
            continue
        stmt = str(item.get("statement", "")).strip()
        if not stmt:
            continue
        if _max_cosine_to_corpus(stmt, corpus) >= HE_COSINE_DEDUP_THRESHOLD:
            continue
        lt = LearningTarget(
            statement=stmt,
            type=3,
            knowledge_type="dispositional",
            assessment_route="observation_protocol",
            kud_source="phase4:he_disposition_inference",
            word_count=len(stmt.split()),
            flags=[HE_DISPOSITION_INFERRED],
            lt_statement_format=fmt,
        )
        lt.flags = _validate_lt(lt, compound_type=False, fmt=fmt)
        if HE_DISPOSITION_INFERRED not in lt.flags:
            lt.flags.insert(0, HE_DISPOSITION_INFERRED)
        out.append(lt)
        corpus.append(stmt)
    return out


async def phase4_lt_generation(state: DecomposerState) -> dict[str, Any]:
    errs = list(state.get("errors") or [])
    review_dicts = list(state.get("human_review_queue") or [])

    kud = KUD.from_dict(state.get("kud"))
    arch = state.get("architecture_diagnosis") or {}
    profile = dict(state.get("curriculum_profile") or {})
    fmt = resolve_lt_statement_format(profile)
    doc_fam = str(profile.get("document_family", "")).strip().lower()

    if not kud.all_items():
        errs.append("phase4: skipped — empty KUD")
        return {
            "current_phase": "phase4:skipped",
            "errors": errs,
            "learning_targets": [],
        }

    mcp_url = state.get("mcp_server_url") or ""
    mcp_name = state.get("mcp_server_name") or "claude-education-skills"
    arch_summary = str(arch)[:12000]
    exam_addon = GCSE_AQA_EXAM_BLOCK if doc_fam == "exam_specification" else ""
    hard = _hard_rules_for_format(fmt)
    action_block = _action_rules_for_format(fmt)

    targets: list[dict[str, Any]] = []
    client = get_async_client()

    for bucket, item in kud.all_items():
        if bucket == "know" and is_recall_only_know_content(item.content):
            continue
        assigned_type, compound = _lt_type_and_compound(item)
        kud_line = _format_kud_line(bucket, item)
        instruction = (
            f"Call `{TOOL_NAME}` to author ONE learning target from this KUD element.\n\n"
            f"{TYPE_FRAMEWORK_FOR_LT}\n\n"
            f"{action_block}\n\n"
            f"{hard}\n"
            f"{exam_addon}\n"
            f"This element has **assigned type {assigned_type}** from the KUD `knowledge_type` field — "
            "generate wording consistent with that type only (do not choose a different type from the wording).\n"
            f"Architecture context (summary): {arch_summary[:4000]}\n"
            'Then output ONLY JSON: {"statement": str}'
        )
        messages = [{
            "role": "user",
            "content": [
                {"type": "text", "text": instruction},
                {"type": "text", "text": kud_line},
            ],
        }]
        resp: Any = None
        stmt = ""
        source = f"{bucket}: {item.content[:120]}"

        try:
            resp = await beta_messages_create(
                client,
                model=SONNET_MODEL,
                max_tokens=2048,
                messages=messages,
                label=f"phase4_mcp_lt_{bucket}",
                mcp_servers=mcp_servers_param(mcp_url, mcp_name),
                tools=[mcp_toolset_single_tool(mcp_name, TOOL_NAME)],
            )
            text = response_text_content(resp)
            parsed = extract_json_object(text) or {}
            stmt = str(parsed.get("statement", "")).strip()
        except AnthropicCallTimeout:
            errs.append(f"phase4: timeout for KUD item {source[:80]} (trying direct Sonnet)")
            try:
                fb = await _direct_lt(kud_line, assigned_type, fmt)
                stmt = fb.statement
            except Exception:
                review_dicts.append(
                    HumanReviewItem(
                        item_type="phase4_timeout",
                        summary=source,
                        decision_needed="Re-run or author LT manually.",
                    ).to_dict(),
                )
                continue
        except Exception as exc:
            raw_dump = response_debug_dump(resp) if resp is not None else str(exc)
            review_dicts.append(
                HumanReviewItem(
                    item_type="phase4_mcp",
                    summary=f"{source}: {exc}"[:500],
                    decision_needed="MCP LT failure; attempting direct Sonnet.",
                ).to_dict(),
            )
            review_dicts.append(
                HumanReviewItem(
                    item_type="phase4_mcp_raw",
                    summary="raw (truncated)",
                    decision_needed=raw_dump[:6000],
                ).to_dict(),
            )
            fb = await _direct_lt(kud_line, assigned_type, fmt)
            stmt = fb.statement

        if not stmt:
            fb = await _direct_lt(kud_line, assigned_type, fmt)
            stmt = fb.statement

        s_low = stmt.lower().strip()
        if "skip_rote" in s_low or s_low in ("skip", "skip_rote_recall_only"):
            continue

        lt = LearningTarget(
            statement=stmt,
            type=assigned_type,
            knowledge_type=item.knowledge_type,
            assessment_route=item.assessment_route,
            kud_source=source,
            word_count=len(stmt.split()),
            lt_statement_format=fmt,
        )
        lt.flags = _validate_lt(lt, compound_type=compound, fmt=fmt)
        targets.append(lt.to_dict())

    if doc_fam == "higher_ed_syllabus":
        try:
            existing_st = [str(t.get("statement", "")) for t in targets]
            extras = await _he_dispositional_supplement(
                raw_curriculum=str(state.get("raw_curriculum") or ""),
                subject=str(state.get("subject") or ""),
                grade=str(state.get("grade") or ""),
                jurisdiction=str(state.get("jurisdiction") or ""),
                fmt=fmt,
                existing_statements=existing_st,
            )
            for lt in extras:
                targets.append(lt.to_dict())
        except Exception as exc:
            errs.append(f"phase4: HE disposition supplement failed: {exc}")

    # Source faithfulness threading — Session 3a Step 7.
    # Every LT is matched against (a) the KUD-item corpus for parent
    # provenance, (b) the source_bullets corpus for source provenance.
    # LTs whose best source match falls below the matcher's threshold
    # are flagged SOURCE_FAITHFULNESS_FAIL and ship with the flag. No
    # regeneration — Session 3b adds that. See
    # `curriculum_harness/source_faithfulness.py` for the matcher's
    # adjacent-mechanism declaration (grain, language boundary, etc.).
    source_bullets = list(state.get("source_bullets") or [])
    kud_parents = [
        {"id": f"{bucket}[{idx}]", "content": it.content}
        for idx, (bucket, it) in enumerate(kud.all_items())
    ]
    phase4_flagged = 0
    for t in targets:
        stmt = str(t.get("statement", ""))
        kud_prov, _ = compute_parent_provenance(stmt, kud_parents, top_k=1)
        src_prov, src_passed = compute_source_provenance(stmt, source_bullets)
        t["kud_provenance"] = kud_prov
        t["source_provenance"] = src_prov
        if not src_passed and source_bullets:
            flags = list(t.get("flags") or [])
            if SOURCE_FAITHFULNESS_FAIL_FLAG not in flags:
                flags.append(SOURCE_FAITHFULNESS_FAIL_FLAG)
            t["flags"] = flags
            phase4_flagged += 1
    if not source_bullets:
        errs.append(
            "phase4: no source_bullets corpus available — "
            "SOURCE_FAITHFULNESS_FAIL flags suppressed for this run"
        )

    return {
        "current_phase": "phase4:complete",
        "errors": errs,
        "human_review_queue": review_dicts,
        "learning_targets": targets,
        "phase4_faithfulness_flagged_count": phase4_flagged,
    }
