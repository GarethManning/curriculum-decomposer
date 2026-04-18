# Curriculum Harness run report

**Run ID:** felveteli_session3c_e2e
**Output directory:** `/Users/garethmanning/Github/curriculum-harness/outputs/felveteli-2026-04-18-session-3c-e2e`

## Output-shape discipline (Session 3c)

- **Output mode:** `exam_specification`
- KUD / map artefact kind: `assessed_demonstrations_map`
- KUD / map artefact path: `/Users/garethmanning/Github/curriculum-harness/outputs/felveteli-2026-04-18-session-3c-e2e/felveteli_session3c_e2e_assessed_demonstrations_map_v1.json`
- Exam-spec discipline active: Understands and Dispositions refused per v4.1.
- Understand items dropped by Phase 3: 4
- Disposition items dropped by Phase 3: 2
- Pedagogical criterion bank: NOT produced (not yet emitted by any phase; exam-spec refusal is pre-emptive).
- Demonstration criterion bank: not yet produced (no criterion phase in harness yet — tracked in VALIDITY.md §4).

## Source language (Session 3c)

- Detected language: `non-en`
- Signal: {'status': 'measured', 'total_tokens': 420, 'en_stopword_hits': 20, 'en_stopword_ratio': 0.0476, 'threshold': 0.05}
- Phase 4 regeneration loop skips `SOURCE_FAITHFULNESS_FAIL` retries for non-en sources (English-only matcher).

## Source bullets

- Count: 32
- Artefact: `/Users/garethmanning/Github/curriculum-harness/outputs/felveteli-2026-04-18-session-3c-e2e/felveteli_session3c_e2e_source_bullets_v1.json`

## Curriculum profile

- document_family: exam_specification
- level_model: single_intended_level
- scoping_strategy: full_document
- lt_statement_format (profile output_conventions): i_can
- lt_statement_format (resolved for pipeline): i_can
- recommended_adjacent_radius (product default ±1): 1
- confidence: high
- Profile JSON: `/Users/garethmanning/Github/curriculum-harness/outputs/felveteli-2026-04-18-session-3c-e2e/felveteli_session3c_e2e_curriculum_profile_v1.json`

_Classification notes:_ Hungarian central written entrance exam specification for 8th-graders applying to 9th grade. Canonical topic list spanning grades 1–8 curriculum requirements. No assessment objectives or mark scheme present.


## Curriculum coverage (content themes)

_These strands describe topic or period coverage. They are **not** used for learning-target assignment in Phase 5._

- _(none listed)_

## Learning targets

- Count by type: 1=27, 2=1, 3=0
- Word count stats: min=9, max=20, mean=13.0
- Items with any validation flag: 28
- Total flags across items: 29
- HE disposition inferred (Phase 4 supplement): 0

## Phase 3 profile-conditional branch (Session 3b)

- Branch selected: **per_bullet**
- Input source bullets: 32
- Output KUD items: 28
- Merge events (per_bullet only): 6

_Bullet merges recorded in Phase 3 per_bullet branch:_
- `sb_023, sb_024` → Reflection properties and characteristics
- `sb_028, sb_029` → Polygon angle and diagonal formulas
- `sb_030, sb_031` → Triangle side-angle relationships and special lines
- `sb_016, sb_017` → Construct and interpret coordinate graphs
- `sb_021, sb_023, sb_024` → Apply geometric transformations accurately
- `sb_027, sb_032` → Calculate areas and volumes using appropriate formulas

## Phase 3 recall filter

- recall_filtered_count: 0

## Source faithfulness flagging (Session 3a)

- Phase 3 KUD items flagged SOURCE_FAITHFULNESS_FAIL: 28
- Phase 4 LTs flagged SOURCE_FAITHFULNESS_FAIL: 28

## Regeneration loop (Session 3c)

- Total LTs that entered regeneration: 28
- LTs that exhausted the retry budget: 0
- Regeneration artefact: `/Users/garethmanning/Github/curriculum-harness/outputs/felveteli-2026-04-18-session-3c-e2e/felveteli_session3c_e2e_regeneration_events_v1.json`
  - outcome `language_bypass_ship_flagged`: 28

## Flags (unique)

- Learning target flags: ['POSSIBLE_COMPOUND', 'SOURCE_FAITHFULNESS_FAIL']
- Structured LT (Phase 5) flags: ['COMPETENCY_MAPPING_UNCERTAIN', 'POSSIBLE_COMPOUND', 'SOURCE_FAITHFULNESS_FAIL']

## Comparison note

_Reserved for manual comparison against the validation experiment._

## Phase 5 structured output

- Competency groups: 5
- Group LT counts: {'Number Systems and Operations': 17, 'Algebraic Expressions and Equations': 2, 'Statistics and Probability Concepts': 1, 'Geometric Properties and Transformations': 7, 'Mathematical Problem-Solving Approaches': 1}
- Level columns generated: ['Year 6', 'Year 7', 'Year 8']
- COMPETENCY_MAPPING_UNCERTAIN count: 1
- Structured JSON path: `/Users/garethmanning/Github/curriculum-harness/outputs/felveteli-2026-04-18-session-3c-e2e/felveteli_session3c_e2e_structured_lts_v1.json`
- Structured CSV path: `/Users/garethmanning/Github/curriculum-harness/outputs/felveteli-2026-04-18-session-3c-e2e/felveteli_session3c_e2e_structured_lts_v1.csv`

## Phase errors

- phase1: scoped extraction returned empty or unfound — using profile-aware fallback slice