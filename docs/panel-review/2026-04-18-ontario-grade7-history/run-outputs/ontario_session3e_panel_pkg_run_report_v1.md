# Curriculum Harness run report

**Run ID:** ontario_session3e_panel_pkg
**Output directory:** `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3e-panel-pkg`

## Output-shape discipline (Session 3c)

- **Output mode:** `curriculum`
- KUD / map artefact kind: `kud`
- KUD / map artefact path: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3e-panel-pkg/ontario_session3e_panel_pkg_kud_v1.json`
- Curriculum mode: full KUD emitted (know, understand, do_skills, do_dispositions).

## Source language (Session 3c)

- Detected language: `en`
- Signal: {'status': 'measured', 'total_tokens': 10427, 'en_stopword_hits': 4493, 'en_stopword_ratio': 0.4309, 'threshold': 0.05}
- Phase 4 regeneration loop retries all FAIL_SET flags normally.

## Source bullets

- Count: 937
- Artefact: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3e-panel-pkg/ontario_session3e_panel_pkg_source_bullets_v1.json`

## Curriculum profile

- document_family: national_framework
- level_model: multi_level_progression
- scoping_strategy: grade_subject_filter
- lt_statement_format (profile output_conventions): i_can
- lt_statement_format (resolved for pipeline): i_can
- recommended_adjacent_radius (product default ±1): 1
- confidence: high
- Profile JSON: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3e-panel-pkg/ontario_session3e_panel_pkg_curriculum_profile_v1.json`

_Classification notes:_ Ontario Curriculum Grades 1–8 (2023) is a provincial framework spanning multiple grade levels. Document covers Grades 1–8 with dedicated History section for Grade 7. Multi-level progression model applies. Assessment section describes achievement levels and evaluation approaches.


## Curriculum coverage (content themes)

_These strands describe topic or period coverage. They are **not** used for learning-target assignment in Phase 5._

- _(none listed)_

## Learning targets

- Count by type: 1=7, 2=11, 3=4
- Word count stats: min=11, max=20, mean=15.5
- Items with any validation flag: 22
- Total flags across items: 25
- HE disposition inferred (Phase 4 supplement): 0

## Phase 3 profile-conditional branch (Session 3b)

- Branch selected: **strand_aggregated**
- Input source bullets: 937
- Output KUD items: 22
- Merge events (per_bullet only): 0

## Phase 3 recall filter

- recall_filtered_count: 0

## Source faithfulness flagging (Session 3a)

- Phase 3 KUD items flagged SOURCE_FAITHFULNESS_FAIL: 19
- Phase 4 LTs flagged SOURCE_FAITHFULNESS_FAIL: 22

## Regeneration loop (Session 3c)

- Total LTs that entered regeneration: 22
- LTs that exhausted the retry budget: 22
- Regeneration artefact: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3e-panel-pkg/ontario_session3e_panel_pkg_regeneration_events_v1.json`
  - outcome `exhausted_retries`: 20
  - outcome `near_identical_retry_abort`: 2

_Human-review entries (budget exhausted):_
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: near_identical_retry_abort
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- _…and 10 more_

## Flags (unique)

- Learning target flags: ['COMPOUND_TYPE', 'SOURCE_FAITHFULNESS_FAIL']
- Structured LT (Phase 5) flags: []

## Comparison note

_Reserved for manual comparison against the validation experiment._

## Phase 5 structured output

- Competency groups: 0
- Group LT counts: {}
- Level columns generated: []
- COMPETENCY_MAPPING_UNCERTAIN count: 0
- Structured JSON path: `None`
- Structured CSV path: `None`

## Phase errors

- phase2: API timeout after 240s
- phase5: skipped — architecture_diagnosis has no strands