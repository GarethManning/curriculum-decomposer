# Curriculum Harness run report

**Run ID:** ontario_session3c_e2e
**Output directory:** `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3c-e2e`

## Output-shape discipline (Session 3c)

- **Output mode:** `curriculum`
- KUD / map artefact kind: `kud`
- KUD / map artefact path: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3c-e2e/ontario_session3c_e2e_kud_v1.json`
- Curriculum mode: full KUD emitted (know, understand, do_skills, do_dispositions).

## Source language (Session 3c)

- Detected language: `en`
- Signal: {'status': 'measured', 'total_tokens': 10427, 'en_stopword_hits': 4493, 'en_stopword_ratio': 0.4309, 'threshold': 0.05}
- Phase 4 regeneration loop retries all FAIL_SET flags normally.

## Source bullets

- Count: 937
- Artefact: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3c-e2e/ontario_session3c_e2e_source_bullets_v1.json`

## Curriculum profile

- document_family: national_framework
- level_model: multi_level_progression
- scoping_strategy: grade_subject_filter
- lt_statement_format (profile output_conventions): i_can
- lt_statement_format (resolved for pipeline): i_can
- recommended_adjacent_radius (product default ±1): 1
- confidence: high
- Profile JSON: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3c-e2e/ontario_session3c_e2e_curriculum_profile_v1.json`

_Classification notes:_ Ontario Curriculum Grades 1–8 (2023) is a provincial framework spanning multiple grade levels. Document targets Grade 7 History but encompasses K–8 progression. Contains learning expectations, achievement levels, and assessment guidance but no exam specifications or mark schemes.


## Curriculum coverage (content themes)

_These strands describe topic or period coverage. They are **not** used for learning-target assignment in Phase 5._

- **Indigenous Perspectives and Reconciliation** (`indigenous-perspectives-reconciliation`): This represents specific content coverage integrated throughout the curriculum rather than a skills-based learning target category.
- **New France and Early Settlement** (`new-france-early-settlement`): Specific historical period content that provides context for skill development but is not itself a learning target type.
- **Canadian Confederation and Development** (`canadian-confederation-development`): Specific historical content area that serves as context for applying historical thinking skills.

## Learning targets

- Count by type: 1=4, 2=9, 3=5
- Word count stats: min=12, max=17, mean=14.5
- Items with any validation flag: 18
- Total flags across items: 19
- HE disposition inferred (Phase 4 supplement): 0

## Phase 3 profile-conditional branch (Session 3b)

- Branch selected: **strand_aggregated**
- Input source bullets: 937
- Output KUD items: 18
- Merge events (per_bullet only): 0

## Phase 3 recall filter

- recall_filtered_count: 1

## Source faithfulness flagging (Session 3a)

- Phase 3 KUD items flagged SOURCE_FAITHFULNESS_FAIL: 16
- Phase 4 LTs flagged SOURCE_FAITHFULNESS_FAIL: 17

## Regeneration loop (Session 3c)

- Total LTs that entered regeneration: 18
- LTs that exhausted the retry budget: 17
- Regeneration artefact: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3c-e2e/ontario_session3c_e2e_regeneration_events_v1.json`
  - outcome `exhausted_retries`: 17
  - outcome `success@retry_1`: 1

_Human-review entries (budget exhausted):_
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- `(no sb_ids)` → flags: [SOURCE_FAITHFULNESS_FAIL]; outcome: exhausted_retries
- _…and 5 more_

## Flags (unique)

- Learning target flags: ['COMPOUND_TYPE', 'POSSIBLE_COMPOUND', 'SOURCE_FAITHFULNESS_FAIL']
- Structured LT (Phase 5) flags: ['COMPOUND_TYPE', 'POSSIBLE_COMPOUND', 'SOURCE_FAITHFULNESS_FAIL']

## Comparison note

_Reserved for manual comparison against the validation experiment._

## Phase 5 structured output

- Competency groups: 7
- Group LT counts: {'Historical Chronological Knowledge': 2, 'Historical Inquiry and Analysis': 6, 'Civic Engagement and Understanding': 3, 'Global Citizenship Mindset': 3, 'Geographical Foundational Concepts': 2, 'Critical Thinking Disposition': 1, 'Collaborative Inquiry Capacity': 1}
- Level columns generated: ['Grade 7']
- COMPETENCY_MAPPING_UNCERTAIN count: 0
- Structured JSON path: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3c-e2e/ontario_session3c_e2e_structured_lts_v1.json`
- Structured CSV path: `/Users/garethmanning/Github/curriculum-harness/outputs/ontario-2026-04-18-session-3c-e2e/ontario_session3c_e2e_structured_lts_v1.csv`

## Phase errors

- phase1: scoped extraction returned empty or unfound — using profile-aware fallback slice