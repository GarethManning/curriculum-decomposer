# LT 6.1 Band C → LT 7.1 Band D hard_prerequisite edge addition log
## 23 April 2026 (KUD v3 / QA Step 6 panel recommendation)

## Summary

At session start, `criterion-bank-v3.json` contained **zero** cross-LT edges between LT 6.1 and LT 7.1 in either direction. The chart prose at KUD v2 line 691 named LT 6.1 Bands C–D as a *conceptual accelerator* for LT 7.1 Band C onward, but the coupling was not materialised in the edge set. The brief's instruction to "retype soft-enabler edges as hard_prerequisite" therefore resolves to **edge addition, not retyping** — the edges did not exist to retype.

The schema (`criterion-bank-schema.json`) previously allowed only two edge_type values: `within_lt_band` and `cross_lt_source_stated`. The `hard_prerequisite` value was added to the schema enum in this session to honour the brief's explicit naming and the QA Step 6 panel rationale.

## Schema change

- `criterion-bank-schema.json` edge_types enum extended: ['within_lt_band', 'cross_lt_source_stated', 'hard_prerequisite']

## Edges added (all edge_type = hard_prerequisite)

| # | from | from LT/band | to | to LT/band | edge_type (old) | edge_type (new) |
|---|---|---|---|---|---|---|
| 1 | real-wellbeing-2026-04_crit_0080 | LT 6.1 Band C | real-wellbeing-2026-04_crit_0101 | LT 7.1 Band D | (no prior edge) | hard_prerequisite |
| 2 | real-wellbeing-2026-04_crit_0082 | LT 6.1 Band C | real-wellbeing-2026-04_crit_0101 | LT 7.1 Band D | (no prior edge) | hard_prerequisite |
| 3 | real-wellbeing-2026-04_crit_0080 | LT 6.1 Band C | real-wellbeing-2026-04_crit_0102 | LT 7.1 Band D | (no prior edge) | hard_prerequisite |
| 4 | real-wellbeing-2026-04_crit_0082 | LT 6.1 Band C | real-wellbeing-2026-04_crit_0102 | LT 7.1 Band D | (no prior edge) | hard_prerequisite |
| 5 | real-wellbeing-2026-04_crit_0080 | LT 6.1 Band C | real-wellbeing-2026-04_crit_0180 | LT 7.1 Band D | (no prior edge) | hard_prerequisite |
| 6 | real-wellbeing-2026-04_crit_0082 | LT 6.1 Band C | real-wellbeing-2026-04_crit_0180 | LT 7.1 Band D | (no prior edge) | hard_prerequisite |
| 7 | real-wellbeing-2026-04_crit_0080 | LT 6.1 Band C | real-wellbeing-2026-04_crit_0181 | LT 7.1 Band D | (no prior edge) | hard_prerequisite |
| 8 | real-wellbeing-2026-04_crit_0082 | LT 6.1 Band C | real-wellbeing-2026-04_crit_0181 | LT 7.1 Band D | (no prior edge) | hard_prerequisite |

## Rationale

LT 7.1 Band D requires the student to distinguish the origin of a personal pattern from its sustaining conditions. This analytical move cannot be executed without the stress-response mechanism knowledge that LT 6.1 Band C provides (amygdala / prefrontal-cortex interaction under stress; habit-loop mechanism). Two of the three LT 6.1 Band C criteria are load-bearing on this analytical move:

- `crit_0080` — amygdala / prefrontal-cortex interaction under stress
- `crit_0082` — habit-loop mechanism (cue → routine → reward)

The neuroplasticity criterion (`crit_0081`) was judged not directly load-bearing on the origin-vs-sustaining distinction and was therefore not linked.

## DAG validation

- Criteria:       238
- Total edges:    499
- Edge-type counts: {'cross_lt_source_stated': 173, 'within_lt_band': 318, 'hard_prerequisite': 8}
- Cycles:         0
- Self-loops:     0
- Unresolved IDs: 0
- DAG status:     **PASS**

## Companion changes

- `REAL_Wellbeing_KUD_v3_20260423.md` — LT 7.1 prerequisite line rewritten to name the hard-prerequisite pair; authoring notes updated to record the retyping and the Claxton dissent verbatim.
- `criterion-bank-schema.json` — `hard_prerequisite` added to `edge_types`.
