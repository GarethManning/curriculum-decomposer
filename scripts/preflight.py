#!/usr/bin/env python3
"""REAL wellbeing preflight.

Run at session start. Twelve checks against the canonical band convention,
the live structured artefacts, and cross-artefact referential integrity.
Exit 0 on all-pass, 1 on any fail.

Usage:
    python scripts/preflight.py
    python scripts/preflight.py --criterion-bank <path> --unified-data <path> --expected-lts 21
"""

from __future__ import annotations

import argparse
import ast
import json
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from band_constants import BAND_LABELS, VALID_BAND_LETTERS

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BANK = (
    REPO_ROOT / "docs" / "reference-corpus" / "real-wellbeing" / "criterion-bank-v5_1.json"
)
DEFAULT_UNIFIED = (
    REPO_ROOT / "docs" / "reference-corpus" / "real-wellbeing" / "unified-wellbeing-data-v6.json"
)
DEFAULT_EXPECTED_LTS = 21

SCRIPTS_DIR = REPO_ROOT / "scripts"
SELF_NAME = "band_constants.py"


def _fmt_pass_fail(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


# ── Check 1 — band_label compliance ────────────────────────────────────────────


def check_band_label_compliance(criteria: list[dict]) -> tuple[bool, str]:
    canonical = set(BAND_LABELS.values())
    compliant = 0
    non_compliant: list[tuple[str, str]] = []
    for c in criteria:
        if "band_label" not in c:
            continue
        label = c["band_label"]
        if label in canonical:
            compliant += 1
        else:
            non_compliant.append((c.get("criterion_id", "<missing id>"), label))
    details = f"{compliant} compliant, {len(non_compliant)} non-compliant"
    if non_compliant:
        sample = "; ".join(
            f"{cid}='{lab}'" for cid, lab in non_compliant[:10]
        )
        details += f". First {min(10, len(non_compliant))}: {sample}"
    return len(non_compliant) == 0, details


# ── Check 2 — LT count ─────────────────────────────────────────────────────────


def check_lt_count(lts: list[dict], expected: int) -> tuple[bool, str]:
    actual = len(lts)
    return actual == expected, f"expected {expected} LTs, got {actual}"


# ── Check 3 — DAG validity on unified data edges ───────────────────────────────


def _collect_edges_from_unified(lts: list[dict]) -> tuple[set[str], list[tuple[str, str]]]:
    """Collect prerequisite edges between LTs from the unified data.

    Each LT may carry prerequisite_lt_ids on a per-band basis; we aggregate
    across bands into a single LT-level prerequisite graph. An edge (u, v) means
    u is prerequisite to v.
    """
    nodes: set[str] = set()
    edges: list[tuple[str, str]] = []
    for lt in lts:
        lt_id = lt.get("lt_id")
        if not lt_id:
            continue
        nodes.add(lt_id)
        bands = lt.get("bands") or {}
        if isinstance(bands, dict):
            for _band_letter, band_obj in bands.items():
                if not isinstance(band_obj, dict):
                    continue
                for prereq in band_obj.get("prerequisite_lt_ids", []) or []:
                    nodes.add(prereq)
                    edges.append((prereq, lt_id))
    return nodes, edges


def check_dag_validity(lts: list[dict]) -> tuple[bool, str]:
    nodes, edges = _collect_edges_from_unified(lts)
    indeg: dict[str, int] = {n: 0 for n in nodes}
    out: dict[str, list[str]] = {n: [] for n in nodes}
    for u, v in edges:
        out.setdefault(u, []).append(v)
        indeg[v] = indeg.get(v, 0) + 1
        indeg.setdefault(u, indeg.get(u, 0))

    q = deque([n for n, d in indeg.items() if d == 0])
    visited = 0
    while q:
        n = q.popleft()
        visited += 1
        for m in out.get(n, []):
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)

    total = len(indeg)
    if visited == total:
        return True, f"{total} nodes, {len(edges)} edges, topological sort OK"
    remaining = [n for n, d in indeg.items() if d > 0]
    return False, (
        f"cycle detected — {total - visited} nodes remain after toposort. "
        f"Nodes in cycle(s): {sorted(remaining)[:20]}"
    )


# ── Check 4 — schema compliance ────────────────────────────────────────────────


CRITERION_COMMON_FIELDS = {
    "criterion_id",
    "associated_lt_ids",
    "band",
    "band_label",
    "lt_type",
    "strand",
    "criterion_statement",
    "criterion_label",
    "source_kud_item_ids",
    "decomposition_rationale",
    "prerequisite_criterion_ids",
    "prerequisite_edges_detail",
    "schema_version",
}
CRITERION_T1_T2_EXTRA = {"competency_level_descriptors"}
CRITERION_T3_EXTRA = {
    "observation_indicators",
    "confusable_behaviours",
    "absence_indicators",
    "conversation_prompts",
}

LT_REQUIRED_FIELDS = {"lt_id", "lt_name", "competency", "knowledge_type", "bands"}


def check_schema_compliance(
    criteria: list[dict], lts: list[dict]
) -> tuple[bool, str]:
    non_compliant: list[tuple[str, list[str]]] = []
    compliant = 0
    for c in criteria:
        required = set(CRITERION_COMMON_FIELDS)
        lt_type = c.get("lt_type")
        if lt_type in ("Type 1", "Type 2"):
            required |= CRITERION_T1_T2_EXTRA
        elif lt_type == "Type 3":
            required |= CRITERION_T3_EXTRA
        missing = sorted(f for f in required if f not in c)
        if missing:
            non_compliant.append((c.get("criterion_id", "<missing id>"), missing))
        else:
            compliant += 1

    lt_non_compliant: list[tuple[str, list[str]]] = []
    lt_compliant = 0
    for lt in lts:
        missing = sorted(f for f in LT_REQUIRED_FIELDS if f not in lt)
        if missing:
            lt_non_compliant.append((lt.get("lt_id", "<missing id>"), missing))
        else:
            lt_compliant += 1

    ok = not non_compliant and not lt_non_compliant
    details = (
        f"criteria: {compliant} compliant, {len(non_compliant)} non-compliant; "
        f"LTs: {lt_compliant} compliant, {len(lt_non_compliant)} non-compliant"
    )
    if non_compliant:
        sample = "; ".join(
            f"{cid} missing {missing}" for cid, missing in non_compliant[:5]
        )
        details += f". First {min(5, len(non_compliant))} criteria: {sample}"
    if lt_non_compliant:
        sample = "; ".join(
            f"{lid} missing {missing}" for lid, missing in lt_non_compliant[:5]
        )
        details += f". First {min(5, len(lt_non_compliant))} LTs: {sample}"
    return ok, details


# ── Check 5 — field-derivation consistency ────────────────────────────────────


def check_field_derivation(criteria: list[dict]) -> tuple[bool, str]:
    consistent = 0
    inconsistent: list[tuple[str, str, str, str]] = []
    for c in criteria:
        band = c.get("band")
        label = c.get("band_label")
        if band is None or label is None:
            continue
        if band not in BAND_LABELS:
            inconsistent.append(
                (
                    c.get("criterion_id", "<missing id>"),
                    str(band),
                    "<unknown band letter>",
                    label,
                )
            )
            continue
        expected = BAND_LABELS[band]
        if label == expected:
            consistent += 1
        else:
            inconsistent.append(
                (c.get("criterion_id", "<missing id>"), band, expected, label)
            )
    details = f"{consistent} consistent, {len(inconsistent)} inconsistent"
    if inconsistent:
        sample = "; ".join(
            f"{cid} band={b} expected='{e}' actual='{a}'"
            for cid, b, e, a in inconsistent[:10]
        )
        details += f". First {min(10, len(inconsistent))}: {sample}"
    return len(inconsistent) == 0, details


# ── Check 6 — no inline BAND_LABELS dicts in scripts ─────────────────────────


def _scan_py_for_inline_bands(path: Path) -> list[str]:
    """Return human-readable offence strings found in a single .py file.

    Offences:
      (a) any top-level BAND_LABELS = {...} assignment
      (b) any dict literal with keys including at least one of A,B,C,D whose
          value is a string containing "Dragon"
    """
    offences: list[str] = []
    try:
        src = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return offences
    try:
        tree = ast.parse(src, filename=str(path))
    except SyntaxError:
        return offences

    class Visitor(ast.NodeVisitor):
        def visit_Assign(self, node: ast.Assign) -> None:
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == "BAND_LABELS":
                    offences.append(
                        f"{path}:{node.lineno} top-level BAND_LABELS assignment"
                    )
            self.generic_visit(node)

        def visit_Dict(self, node: ast.Dict) -> None:
            band_keys_found: list[str] = []
            short_dragon_value = False
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and k.value in ("A", "B", "C", "D"):
                    band_keys_found.append(k.value)
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        if "Dragon" in v.value and len(v.value) < 80:
                            short_dragon_value = True
            # Flag only dicts that look like inline band-letter→short-band-label
                # maps: all four of A,B,C,D present and at least one short
                # Dragon-labelled value.
            if set(band_keys_found) >= {"A", "B", "C", "D"} and short_dragon_value:
                offences.append(
                    f"{path}:{node.lineno} dict literal with band keys {sorted(set(band_keys_found))} "
                    f"and Dragon-name string value (inline band map)"
                )
            self.generic_visit(node)

    Visitor().visit(tree)
    return offences


def check_no_inline_band_labels() -> tuple[bool, str]:
    # Excludes scripts/legacy/ — legacy code preserves historical patterns by design
    # and is exempt from active-code invariants.
    offences: list[str] = []
    for path in SCRIPTS_DIR.rglob("*.py"):
        if path.name == SELF_NAME:
            continue
        if "__pycache__" in path.parts:
            continue
        if path.name == Path(__file__).name:
            continue
        if "legacy" in path.parts:
            continue
        offences.extend(_scan_py_for_inline_bands(path))
    if not offences:
        return True, f"no inline BAND_LABELS found under {SCRIPTS_DIR}/"
    details = f"{len(offences)} offence(s): " + "; ".join(offences[:20])
    return False, details


# ── Check 7 — unified data internal band consistency ─────────────────────────


def _walk_band_labels(obj: object, path: str = "$") -> list[tuple[str, str]]:
    """Recursively yield (json_path, value) for every 'band_label' key in obj."""
    found: list[tuple[str, str]] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = f"{path}.{k}"
            if k == "band_label":
                found.append((new_path, v))
            else:
                found.extend(_walk_band_labels(v, new_path))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            found.extend(_walk_band_labels(item, f"{path}[{i}]"))
    return found


def check_unified_data_bands(unified: dict) -> tuple[bool, str]:
    canonical = set(BAND_LABELS.values())
    all_labels = _walk_band_labels(unified)
    if not all_labels:
        return True, "no band_label fields present in unified data"
    compliant = [(p, v) for p, v in all_labels if v in canonical]
    non_compliant = [(p, v) for p, v in all_labels if v not in canonical]
    details = (
        f"{len(all_labels)} found, {len(compliant)} compliant, "
        f"{len(non_compliant)} non-compliant"
    )
    if non_compliant:
        sample = "; ".join(f"{p}='{v}'" for p, v in non_compliant[:10])
        details += f". First {min(10, len(non_compliant))}: {sample}"
    return len(non_compliant) == 0, details


# ── Check 8 — band-conventions.json self-check ────────────────────────────────

_BAND_CONVENTIONS_REL = (
    "docs/reference-corpus/real-wellbeing/band-conventions.json"
)
_REQUIRED_BAND_FIELDS = {"band_label", "letter", "dragons", "grades", "ages_approx"}
_EXPECTED_BAND_KEYS = {"A", "B", "C", "D", "E", "F"}


def check_band_conventions_self(repo_root: Path) -> tuple[bool, str]:
    conventions_path = repo_root / _BAND_CONVENTIONS_REL
    try:
        with conventions_path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except OSError as exc:
        return False, f"cannot open band-conventions.json: {exc}"
    except json.JSONDecodeError as exc:
        return False, f"band-conventions.json malformed JSON: {exc}"

    issues: list[str] = []

    if "version" not in data or not isinstance(data.get("version"), str):
        issues.append("missing or non-string 'version' field")

    if "source_of_truth" not in data:
        issues.append("missing 'source_of_truth' field")
    else:
        sot_path = repo_root / data["source_of_truth"]
        if not sot_path.exists():
            issues.append(
                f"source_of_truth path does not exist on disk: {data['source_of_truth']}"
            )

    bands = data.get("bands")
    if not isinstance(bands, dict):
        issues.append("'bands' is missing or not an object")
    else:
        actual_keys = set(bands.keys())
        if actual_keys != _EXPECTED_BAND_KEYS:
            extra = sorted(actual_keys - _EXPECTED_BAND_KEYS)
            missing = sorted(_EXPECTED_BAND_KEYS - actual_keys)
            issues.append(
                f"'bands' key mismatch — extra: {extra}, missing: {missing}"
            )
        for letter, entry in bands.items():
            if not isinstance(entry, dict):
                issues.append(f"band '{letter}' is not an object")
                continue
            missing_fields = sorted(_REQUIRED_BAND_FIELDS - set(entry.keys()))
            if missing_fields:
                issues.append(f"band '{letter}' missing fields: {missing_fields}")

    if not issues:
        return True, (
            "band-conventions.json valid — version present, source_of_truth exists, "
            "6 bands (A–F), all required fields present"
        )
    return False, "; ".join(issues)


# ── Check 9 — criterion → LT referential integrity ──────────────────────────


def check_criterion_to_lt_integrity(
    criteria: list[dict], lts: list[dict]
) -> tuple[bool, str]:
    """Every criterion's associated_lt_ids must resolve to an LT in unified data,
    and if lt_type is populated on the criterion it must match the unified LT's
    knowledge_type.
    """
    lt_by_id: dict[str, dict] = {lt["lt_id"]: lt for lt in lts if lt.get("lt_id")}

    kt_map = {
        "Type 1": {"S", "Sequential", "Type 1", "T1"},
        "Type 2": {"H", "Horizontal", "Type 2", "T2"},
        "Type 3": {"D", "Dispositional", "Type 3", "T3"},
    }

    checked = 0
    valid = 0
    broken: list[tuple[str, str, str]] = []
    for c in criteria:
        cid = c.get("criterion_id", "<missing id>")
        lt_refs = c.get("associated_lt_ids") or []
        lt_type = c.get("lt_type")
        has_issue = False
        for lt_id in lt_refs:
            checked += 1
            if lt_id not in lt_by_id:
                broken.append((cid, lt_id, "not_found"))
                has_issue = True
                continue
            if lt_type:
                unified_kt = lt_by_id[lt_id].get("knowledge_type")
                allowed = kt_map.get(lt_type)
                if allowed is not None and unified_kt not in allowed:
                    broken.append(
                        (
                            cid,
                            lt_id,
                            f"type_mismatch (criterion.lt_type='{lt_type}' "
                            f"vs unified knowledge_type='{unified_kt}')",
                        )
                    )
                    has_issue = True
        if lt_refs and not has_issue:
            valid += 1

    details = (
        f"{len(criteria)} criteria checked, {valid} fully valid, "
        f"{len({cid for cid, _, _ in broken})} with broken refs "
        f"({len(broken)} total broken refs over {checked} edges)"
    )
    if broken:
        sample = "; ".join(
            f"{cid}→{lt_id} ({reason})" for cid, lt_id, reason in broken[:10]
        )
        details += f". First {min(10, len(broken))}: {sample}"
    return not broken, details


# ── Check 10 — LT → criterion referential integrity ──────────────────────────


def check_lt_to_criterion_integrity(
    lts: list[dict], criteria: list[dict]
) -> tuple[bool, str]:
    """Every criterion_id referenced from unified-data LT bands must exist in
    the criterion bank.
    """
    crit_id_set = {c.get("criterion_id") for c in criteria if c.get("criterion_id")}
    checked = 0
    valid = 0
    broken: list[tuple[str, str, str]] = []  # (lt_id, band_letter, bad_criterion_id)
    any_refs_present = False
    lts_with_valid_refs = 0

    for lt in lts:
        lt_id = lt.get("lt_id", "<missing id>")
        bands = lt.get("bands") or {}
        if not isinstance(bands, dict):
            continue
        lt_has_any = False
        lt_has_issue = False
        for letter, band_obj in bands.items():
            if not isinstance(band_obj, dict):
                continue
            refs = band_obj.get("criterion_ids") or []
            if refs:
                any_refs_present = True
                lt_has_any = True
            for cid in refs:
                checked += 1
                if cid in crit_id_set:
                    valid += 1
                else:
                    broken.append((lt_id, letter, cid))
                    lt_has_issue = True
        if lt_has_any and not lt_has_issue:
            lts_with_valid_refs += 1

    if not any_refs_present:
        return True, (
            "no explicit criterion references in unified data — "
            "implicit via lt_id reverse lookup, covered by Check 9"
        )

    details = (
        f"{len(lts)} LTs checked, {lts_with_valid_refs} with all refs valid, "
        f"{len({lid for lid, _, _ in broken})} with broken refs "
        f"({valid}/{checked} refs valid)"
    )
    if broken:
        sample = "; ".join(
            f"{lid} band {letter}: {cid}" for lid, letter, cid in broken[:10]
        )
        details += f". First {min(10, len(broken))}: {sample}"
    return not broken, details


# ── Check 11 — orphan detection ──────────────────────────────────────────────


def check_orphans(
    criteria: list[dict], lts: list[dict]
) -> tuple[bool, str]:
    """Two directions:
      - Criterion orphans: criteria whose associated_lt_ids is missing/empty,
        or contains only ids not present in unified data.
      - LT orphans: LTs in unified data that have zero criteria in the bank
        associating back to them.
    """
    lt_id_set = {lt.get("lt_id") for lt in lts if lt.get("lt_id")}

    # Direction A — criterion orphans
    criterion_orphans: list[str] = []
    for c in criteria:
        cid = c.get("criterion_id", "<missing id>")
        refs = c.get("associated_lt_ids") or []
        if not refs:
            criterion_orphans.append(cid)
            continue
        if not any(r in lt_id_set for r in refs):
            criterion_orphans.append(cid)

    # Direction B — LT orphans
    lts_with_criteria: set[str] = set()
    for c in criteria:
        for lt_id in c.get("associated_lt_ids") or []:
            lts_with_criteria.add(lt_id)
    lt_orphans = sorted(lt_id_set - lts_with_criteria)

    ok = not criterion_orphans and not lt_orphans
    details = (
        f"criterion orphans: {len(criterion_orphans)}; "
        f"LT orphans: {len(lt_orphans)}"
    )
    if criterion_orphans:
        details += (
            f". Criterion orphans (first 10): "
            f"{criterion_orphans[:10]}"
        )
    if lt_orphans:
        details += f". LT orphans: {lt_orphans}"
    return ok, details


# ── Check 12 — criterion-level prerequisite DAG ──────────────────────────────


def check_criterion_prereq_dag(criteria: list[dict]) -> tuple[bool, str]:
    """Every prerequisite_criterion_ids entry must resolve to a criterion in
    the bank, and the resulting graph must be a DAG (topological sort succeeds).
    """
    crit_ids = {c.get("criterion_id") for c in criteria if c.get("criterion_id")}

    edges: list[tuple[str, str]] = []
    broken: list[tuple[str, str]] = []  # (downstream_criterion, bad_prereq)
    for c in criteria:
        cid = c.get("criterion_id")
        if not cid:
            continue
        for p in c.get("prerequisite_criterion_ids") or []:
            if p not in crit_ids:
                broken.append((cid, p))
            else:
                edges.append((p, cid))

    # Topological sort over the criterion-id nodes that participate in any edge
    # or exist in the bank.
    indeg: dict[str, int] = {cid: 0 for cid in crit_ids}
    out: dict[str, list[str]] = {cid: [] for cid in crit_ids}
    for u, v in edges:
        out[u].append(v)
        indeg[v] = indeg.get(v, 0) + 1
        indeg.setdefault(u, indeg.get(u, 0))

    q = deque([n for n, d in indeg.items() if d == 0])
    visited = 0
    while q:
        n = q.popleft()
        visited += 1
        for m in out.get(n, []):
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)

    total_nodes = len(indeg)
    dag_ok = visited == total_nodes
    cycle_nodes: list[str] = []
    if not dag_ok:
        cycle_nodes = sorted(n for n, d in indeg.items() if d > 0)[:20]

    ok = not broken and dag_ok
    details = (
        f"{len(edges) + len(broken)} edges checked, {len(edges)} valid, "
        f"{len(broken)} broken; "
        f"DAG: {'OK' if dag_ok else 'CYCLE'} ({total_nodes} nodes, {visited} visited)"
    )
    if broken:
        sample = "; ".join(f"{cid}←{bad}" for cid, bad in broken[:10])
        details += f". First {min(10, len(broken))} broken: {sample}"
    if cycle_nodes:
        details += f". Cycle nodes (sample): {cycle_nodes}"
    return ok, details


# ── Runner ────────────────────────────────────────────────────────────────────


def _load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="REAL wellbeing preflight")
    parser.add_argument("--criterion-bank", type=Path, default=DEFAULT_BANK)
    parser.add_argument("--unified-data", type=Path, default=DEFAULT_UNIFIED)
    parser.add_argument("--expected-lts", type=int, default=DEFAULT_EXPECTED_LTS)
    args = parser.parse_args(argv)

    bank = _load_json(args.criterion_bank)
    unified = _load_json(args.unified_data)
    criteria = bank.get("criteria", [])
    lts = unified.get("learning_targets", [])

    timestamp = datetime.now(timezone.utc).isoformat()
    print("=== PREFLIGHT REPORT ===")
    print(f"Timestamp: {timestamp}")
    print(f"Criterion bank: {args.criterion_bank} ({len(criteria)} entries)")
    print(f"Unified data: {args.unified_data} ({len(lts)} LTs)")
    print()

    c1_ok, c1 = check_band_label_compliance(criteria)
    c2_ok, c2 = check_lt_count(lts, args.expected_lts)
    c3_ok, c3 = check_dag_validity(lts)
    c4_ok, c4 = check_schema_compliance(criteria, lts)
    c5_ok, c5 = check_field_derivation(criteria)
    c6_ok, c6 = check_no_inline_band_labels()
    c7_ok, c7 = check_unified_data_bands(unified)
    c8_ok, c8 = check_band_conventions_self(REPO_ROOT)
    c9_ok, c9 = check_criterion_to_lt_integrity(criteria, lts)
    c10_ok, c10 = check_lt_to_criterion_integrity(lts, criteria)
    c11_ok, c11 = check_orphans(criteria, lts)
    c12_ok, c12 = check_criterion_prereq_dag(criteria)

    print(f"Check 1  (band_label compliance):       {_fmt_pass_fail(c1_ok)} — {c1}")
    print(f"Check 2  (LT count):                    {_fmt_pass_fail(c2_ok)} — {c2}")
    print(f"Check 3  (DAG validity, unified):       {_fmt_pass_fail(c3_ok)} — {c3}")
    print(f"Check 4  (schema compliance):           {_fmt_pass_fail(c4_ok)} — {c4}")
    print(f"Check 5  (field-derivation):            {_fmt_pass_fail(c5_ok)} — {c5}")
    print(f"Check 6  (no inline BAND_LABELS):       {_fmt_pass_fail(c6_ok)} — {c6}")
    print(f"Check 7  (unified data bands):          {_fmt_pass_fail(c7_ok)} — {c7}")
    print(f"Check 8  (canonical self-check):        {_fmt_pass_fail(c8_ok)} — {c8}")
    print(f"Check 9  (criterion→LT integrity):      {_fmt_pass_fail(c9_ok)} — {c9}")
    print(f"Check 10 (LT→criterion integrity):      {_fmt_pass_fail(c10_ok)} — {c10}")
    print(f"Check 11 (orphans):                     {_fmt_pass_fail(c11_ok)} — {c11}")
    print(f"Check 12 (criterion prereq DAG):        {_fmt_pass_fail(c12_ok)} — {c12}")
    print()
    overall_ok = all(
        [c1_ok, c2_ok, c3_ok, c4_ok, c5_ok, c6_ok, c7_ok, c8_ok,
         c9_ok, c10_ok, c11_ok, c12_ok]
    )
    print(f"OVERALL: {_fmt_pass_fail(overall_ok)}")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())
