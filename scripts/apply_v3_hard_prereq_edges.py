#!/usr/bin/env python3
"""Add LT 6.1 Band C → LT 7.1 Band D hard_prerequisite edges to criterion-bank-v3.json.

This is a one-shot apply script for the QA Step 6 panel recommendation implemented
in the 23 April 2026 KUD v3 session. No existing cross-LT edges between LT 6.1 and
LT 7.1 were present in criterion-bank-v3.json at session start, so this script
adds new edges rather than retyping existing ones.

New edges (all edge_type=hard_prerequisite):
    crit_0080 (LT 6.1 Band C, stress-response mechanism) → each LT 7.1 Band D criterion
    crit_0082 (LT 6.1 Band C, habit-loop mechanism)        → each LT 7.1 Band D criterion

Rationale: LT 7.1 Band D requires the student to distinguish the origin of a
personal pattern from its sustaining conditions. This analytical move is
parasitic on the neuroscience knowledge that LT 6.1 Band C provides — specifically
the stress-response mechanism (crit_0080) and the habit-loop mechanism (crit_0082).
The neuroplasticity Band C criterion (crit_0081) is not added here; it is not
directly load-bearing on the origin-vs-sustaining distinction.

DAG validation: runs after the edit and prints PASS/FAIL.
"""
from __future__ import annotations

import json
from pathlib import Path

BANK_PATH = Path(
    "docs/reference-corpus/real-wellbeing/criterion-bank-v3.json"
)
SCHEMA_PATH = Path(
    "docs/reference-corpus/real-wellbeing/criterion-bank-schema.json"
)
LOG_PATH = Path(
    "docs/reference-corpus/real-wellbeing/v3-edge-addition-log-lt-6-1-to-7-1-20260423.md"
)

PREFIX = "real-wellbeing-2026-04_"
SOURCES = [f"{PREFIX}crit_0080", f"{PREFIX}crit_0082"]
TARGETS = [
    f"{PREFIX}crit_0101",
    f"{PREFIX}crit_0102",
    f"{PREFIX}crit_0180",
    f"{PREFIX}crit_0181",
]


def detect_cycles(criteria: list[dict]) -> list[list[str]]:
    graph: dict[str, list[str]] = {c["criterion_id"]: [] for c in criteria}
    for c in criteria:
        for prereq in c.get("prerequisite_criterion_ids", []):
            if prereq in graph:
                graph[prereq].append(c["criterion_id"])

    visited: set[str] = set()
    rec_stack: set[str] = set()
    cycles: list[list[str]] = []

    def dfs(node: str, path: list[str]) -> None:
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, path + [neighbor])
            elif neighbor in rec_stack:
                start = path.index(neighbor) if neighbor in path else 0
                cycles.append(path[start:] + [neighbor])
        rec_stack.discard(node)

    for node in list(graph.keys()):
        if node not in visited:
            dfs(node, [node])
    return cycles


def detect_self_loops(criteria: list[dict]) -> list[str]:
    return [
        c["criterion_id"]
        for c in criteria
        if c["criterion_id"] in c.get("prerequisite_criterion_ids", [])
    ]


def detect_unresolved(criteria: list[dict]) -> list[dict]:
    valid = {c["criterion_id"] for c in criteria}
    out: list[dict] = []
    for c in criteria:
        for p in c.get("prerequisite_criterion_ids", []):
            if p not in valid:
                out.append({"criterion_id": c["criterion_id"], "missing": p})
    return out


def main() -> None:
    bank = json.loads(BANK_PATH.read_text())
    criteria = bank["criteria"]
    by_id = {c["criterion_id"]: c for c in criteria}

    # Sanity: all source and target IDs must exist.
    for cid in SOURCES + TARGETS:
        assert cid in by_id, f"Missing criterion: {cid}"

    added_edges: list[dict] = []
    for target_id in TARGETS:
        t = by_id[target_id]
        t.setdefault("prerequisite_criterion_ids", [])
        t.setdefault("prerequisite_edges_detail", [])
        for source_id in SOURCES:
            if source_id not in t["prerequisite_criterion_ids"]:
                t["prerequisite_criterion_ids"].append(source_id)
            edge = {
                "from": source_id,
                "to": target_id,
                "edge_type": "hard_prerequisite",
            }
            # Avoid duplicate edge_detail entries on re-runs.
            already = any(
                e.get("from") == source_id
                and e.get("to") == target_id
                and e.get("edge_type") == "hard_prerequisite"
                for e in t["prerequisite_edges_detail"]
            )
            if not already:
                t["prerequisite_edges_detail"].append(edge)
                added_edges.append(edge)

    # Extend schema enum if needed.
    schema = json.loads(SCHEMA_PATH.read_text())
    edge_types = schema.get("edge_types", [])
    if "hard_prerequisite" not in edge_types:
        edge_types.append("hard_prerequisite")
        schema["edge_types"] = edge_types
        SCHEMA_PATH.write_text(json.dumps(schema, indent=2) + "\n")
        schema_updated = True
    else:
        schema_updated = False

    # Persist bank.
    BANK_PATH.write_text(json.dumps(bank, indent=2, ensure_ascii=False) + "\n")

    # DAG validation.
    cycles = detect_cycles(criteria)
    self_loops = detect_self_loops(criteria)
    unresolved = detect_unresolved(criteria)
    dag_pass = not cycles and not self_loops and not unresolved

    total_edges = 0
    type_counts: dict[str, int] = {}
    for c in criteria:
        for e in c.get("prerequisite_edges_detail", []):
            total_edges += 1
            t = e.get("edge_type", "unknown")
            type_counts[t] = type_counts.get(t, 0) + 1

    print(f"Criteria:          {len(criteria)}")
    print(f"Total edges:       {total_edges}")
    print(f"Edge-type counts:  {type_counts}")
    print(f"New edges added:   {len(added_edges)}")
    print(f"Schema updated:    {schema_updated}")
    print(f"DAG cycles:        {len(cycles)}")
    print(f"DAG self-loops:    {len(self_loops)}")
    print(f"DAG unresolved:    {len(unresolved)}")
    print(f"DAG status:        {'PASS' if dag_pass else 'FAIL'}")

    # Write log.
    lines = [
        "# LT 6.1 Band C → LT 7.1 Band D hard_prerequisite edge addition log",
        "## 23 April 2026 (KUD v3 / QA Step 6 panel recommendation)",
        "",
        "## Summary",
        "",
        ("At session start, `criterion-bank-v3.json` contained **zero** cross-LT "
         "edges between LT 6.1 and LT 7.1 in either direction. The chart prose at "
         "KUD v2 line 691 named LT 6.1 Bands C–D as a *conceptual accelerator* for "
         "LT 7.1 Band C onward, but the coupling was not materialised in the edge "
         "set. The brief's instruction to \"retype soft-enabler edges as "
         "hard_prerequisite\" therefore resolves to **edge addition, not retyping** "
         "— the edges did not exist to retype."),
        "",
        ("The schema (`criterion-bank-schema.json`) previously allowed only two "
         "edge_type values: `within_lt_band` and `cross_lt_source_stated`. The "
         "`hard_prerequisite` value was added to the schema enum in this session "
         "to honour the brief's explicit naming and the QA Step 6 panel rationale."),
        "",
        "## Schema change",
        "",
        f"- `criterion-bank-schema.json` edge_types enum extended: {edge_types}",
        "",
        "## Edges added (all edge_type = hard_prerequisite)",
        "",
        "| # | from | from LT/band | to | to LT/band | edge_type (old) | edge_type (new) |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, e in enumerate(added_edges, 1):
        src = by_id[e["from"]]
        tgt = by_id[e["to"]]
        lines.append(
            f"| {i} | {e['from']} | LT {src['associated_lt_ids'][0].split('_',1)[1].replace('_','.')} "
            f"Band {src['band']} | {e['to']} | LT {tgt['associated_lt_ids'][0].split('_',1)[1].replace('_','.')} "
            f"Band {tgt['band']} | (no prior edge) | hard_prerequisite |"
        )
    lines.extend([
        "",
        "## Rationale",
        "",
        ("LT 7.1 Band D requires the student to distinguish the origin of a "
         "personal pattern from its sustaining conditions. This analytical move "
         "cannot be executed without the stress-response mechanism knowledge that "
         "LT 6.1 Band C provides (amygdala / prefrontal-cortex interaction under "
         "stress; habit-loop mechanism). Two of the three LT 6.1 Band C criteria "
         "are load-bearing on this analytical move:"),
        "",
        "- `crit_0080` — amygdala / prefrontal-cortex interaction under stress",
        "- `crit_0082` — habit-loop mechanism (cue → routine → reward)",
        "",
        ("The neuroplasticity criterion (`crit_0081`) was judged not directly "
         "load-bearing on the origin-vs-sustaining distinction and was therefore "
         "not linked."),
        "",
        "## DAG validation",
        "",
        f"- Criteria:       {len(criteria)}",
        f"- Total edges:    {total_edges}",
        f"- Edge-type counts: {type_counts}",
        f"- Cycles:         {len(cycles)}",
        f"- Self-loops:     {len(self_loops)}",
        f"- Unresolved IDs: {len(unresolved)}",
        f"- DAG status:     **{'PASS' if dag_pass else 'FAIL'}**",
        "",
        "## Companion changes",
        "",
        ("- `REAL_Wellbeing_KUD_v3_20260423.md` — LT 7.1 prerequisite line rewritten "
         "to name the hard-prerequisite pair; authoring notes updated to record the "
         "retyping and the Claxton dissent verbatim."),
        "- `criterion-bank-schema.json` — `hard_prerequisite` added to `edge_types`.",
        "",
    ])
    LOG_PATH.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
