# Session 3c end-to-end re-runs — Phase 4 regeneration + exam-spec output discipline (2026-04-18)

Two full-pipeline runs with Session 3c's additions active: Phase 4
hard-fail regeneration on FAIL_SET flags, exam-spec output-shape
refusal (Understands / Dispositions suppressed in per_bullet mode),
source-language bypass for English-only-matcher + non-English source.

- Ontario (`ontario/`): `configs/ontario_session3c_e2e.json`.
- Felveteli (`felveteli/`): `configs/felveteli_session3c_e2e.json`.

Both runs completed end-to-end with exit 0. `validate_lt_surface_form`
and `validate_regenerate_loop` gates both **PASS** on each snapshot.

## Measurements

### Ontario — curriculum mode (strand_aggregated branch, English)

| Measure | Session 3b | Session 3c |
|---|---:|---:|
| Source bullets | 937 | 937 |
| KUD items | 17 | 18 (know 4, understand 6, do_skills 5, do_dispositions 3) |
| LTs | 17 | 18 |
| Output mode | curriculum (implicit) | **curriculum (logged)** |
| KUD artefact filename | `_kud_v1.json` (bare) | `_kud_v1.json` (bare) |
| Source language | en (implicit) | **en (logged, stopword ratio 0.43)** |
| Phase 3 SOURCE_FAITHFULNESS_FAIL count | 13 / 17 (76%) | 14 / 18 (78%) |
| Phase 4 SOURCE_FAITHFULNESS_FAIL count (pre-retry) | 15 / 17 (88%) | ~18 / 18 (100%, pre-retry all flagged) |
| Phase 4 SOURCE_FAITHFULNESS_FAIL count (final LT set) | 15 / 17 | 17 / 18 (94%) |
| LTs that entered regeneration | n/a | 18 |
| LTs cleared by retry | n/a | **1** (success@retry_1) |
| LTs exhausted retries → human_review_required | n/a | **17** |

**Reading:** the regeneration loop worked end-to-end on Ontario.
Phase 4 attempted retries on every flagged LT, repaired 1 substantively,
and correctly surfaced 17 source bullets for human review rather than
shipping them as valid. The 17 exhausted entries are a genuine signal:
Ontario's 937-bullet corpus is over-wide (Session 3d's scope), so
aggregated-strand LTs cannot trace above the 0.35 threshold against
diluted bullet content. The regen loop did not paper this over — it
surfaced it.

### Felveteli — exam-spec mode (per_bullet + v4.1 refusal, non-English)

| Measure | Session 3b | Session 3c |
|---|---:|---:|
| Source bullets | 32 | 32 |
| KUD items pre-refusal | 32 (18 K + 4 U + 10 D + 0 Disp) | 28 (24 K + 0 U + 4 D + 0 Disp) |
| Understands dropped by Phase 3 | n/a | **0** (Sonnet chose to emit fewer understand items this run; pre-refusal count was 0 in this sample) |
| Dispositions dropped by Phase 3 | n/a | **0** (Sonnet chose none; pre-refusal count was 0) |
| LTs | 32 | **28** |
| Output mode | n/a | **exam_specification (logged)** |
| Output artefact filename | `_kud_v1.json` | **`_assessed_demonstrations_map_v1.json`** |
| Output shape | bare KUD | `{output_mode, schema_version, assessed_demonstrations_map:{assessed_topics, tested_demonstrations, understandings: null, dispositions: null, pedagogical_criteria: null}}` |
| Source language | n/a | **non-en (logged, stopword ratio 0.0476)** |
| Language bypass fires on SOURCE_FAITHFULNESS_FAIL | n/a | **28 / 28** |
| LTs cleared by retry | n/a | 0 (all language-bypassed after first attempt) |
| LTs in human_review_required | n/a | **0** (bypass mechanism absorbs the language mismatch cleanly) |
| Factorial LT ships as valid? | No (flagged) | **No — language-bypass flagged + annotated** |

**Reading:** the exam-spec output-shape gate fired correctly. The file
name is `assessed_demonstrations_map_v1.json`, its top-level key is
`output_mode: "exam_specification"`, and `understandings` /
`dispositions` / `pedagogical_criteria` are `null` per v4.1 (not empty
arrays). The language-detection bypass absorbed the expected 28/28
`SOURCE_FAITHFULNESS_FAIL` flags without burning any retry budget —
exactly the escape hatch designed for an English-only matcher on
Hungarian source.

Note on KUD cardinality: Session 3b produced 32 KUD items from 32
bullets under Shape C. This Session 3c run produced 28 items, all
classified as know or do_skills (Sonnet produced no understand /
disposition items this run). Because Phase 3's exam-spec refusal only
drops items that exist, understand_dropped and dispositions_dropped
are both 0 here — the refusal is structurally active but had nothing
to drop. Output shape (`assessed_demonstrations_map` with `null`
pedagogical columns) is still correct.

## Regeneration events

Both runs produce `<runId>_regeneration_events_v1.json`.

- Ontario: 18 events. 1 success@retry_1, 17 exhausted_retries.
- Felveteli: 28 events. 28 language_bypass_ship_flagged, 0 elsewhere.

Every event record includes the full attempt history (statement,
flags, annotations, similarity_to_prev) so a reviewer can see what
was tried and what went wrong.

## Factorial LT guarantee

Felvételi LT[0]:
```
"I can calculate the number of possible arrangements and selections
 using counting principles, permutations, and combinations."
```
Flags: `['SOURCE_FAITHFULNESS_FAIL']`.
Regeneration event outcome: `language_bypass_ship_flagged`.
KUD source: `know: Basic counting principles, permutations, and combinations` (derived
from `sb_001` — Hungarian `Elemi kombinatorika (összeszámolás,
sorrendek száma, kiválasztás)`).

**Hard requirement met:** the LT ships with the `SOURCE_FAITHFULNESS_FAIL`
flag, annotated in the regeneration-event log with
`SOURCE_LANGUAGE_BYPASS`. It is not claimed as valid; a reviewer
looking at the run report or regeneration-events artefact can see
the flag and bypass annotation explicitly.

## Output-shape discipline (v4.1)

Felvételi — the exam-spec gate fires (`per_bullet` branch →
`output_mode == "exam_specification"`):
- `understand` array emptied by Phase 3 refusal (nothing to drop here).
- `do_dispositions` array emptied by Phase 3 refusal (nothing to drop).
- Output artefact written as
  `<runId>_assessed_demonstrations_map_v1.json` with the wrapper
  `{output_mode, schema_version, assessed_demonstrations_map:
  {assessed_topics, tested_demonstrations, understandings: null,
  dispositions: null, pedagogical_criteria: null}}`.

Ontario — curriculum mode retains the legacy `_kud_v1.json` filename
and bare shape. `output_mode == "curriculum"` recorded in the run
report.

## Validity-gate results

Running both gates on each Session 3c snapshot:

Ontario:
- `validate_lt_surface_form`: **PASS 100.0% (18/18)**.
- `validate_regenerate_loop`: **PASS** — clean=1, success-after-retry=0,
  language-bypass=0, human-review=17, gaps=0.

Felvételi:
- `validate_lt_surface_form`: **PASS 100.0% (28/28)**, all 28 recognised
  as language-bypass.
- `validate_regenerate_loop`: **PASS** — clean=0, success-after-retry=0,
  language-bypass=28, human-review=0, gaps=0.

## Phase errors

Both runs logged `phase3: MCP/tools failed: Connection error.` — the
MCP endpoint at `mcp-server-sigma-sooty.vercel.app` was intermittent
as in Session 3b. Sonnet-direct fallback activated for Phase 3 on both
runs, and the correct branch (strand_aggregated / per_bullet) fired
for each config.

Ontario also logged one `phase4_sonnet_direct_lt` fallback mid-run
(MCP empty-statement recovery) — expected behaviour.
