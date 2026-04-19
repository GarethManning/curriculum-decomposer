# KUD quality report — 5-ap-usgov-ced-unit1

**Overall:** PASSED

## Summary

- **source_domain:** horizontal
- **inventory_blocks_total:** 365
- **inventory_non_heading_blocks:** 264
- **kud_items_total:** 67
- **halted_blocks_total:** 221
- **halted_severe:** 215
- **halted_unreliable:** 6
- **knowledge_type_distribution:** Type 1=48, Type 2=19
- **kud_column_distribution:** do_skill=20, know=32, understand=15
- **stability_distribution:** classification_unstable=15, stable=52
- **underspecification_distribution:** mild=38, moderate=3, null=26

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — PASS

KUD items / expected-yield blocks = 67/49 = 1.367 (denominator excludes 215 severely-underspecified blocks) within horizontal-domain target [0.8, 1.5]

### `type3_distribution` — PASS

type3_distribution gate skipped — source is not marked as dispositional-domain

### `no_compound_unsplit` — PASS

every KUD item carries a single knowledge type with consistent column and route

## Stage: source-native progression structure

- source type: `us_ap_course_unit`
- band count: **1**
- band labels: Unit 1
- age range hint: ages 16-18 (College Board AP US Government and Politics; typically Grades 11-12)
- detection confidence: `high`
- detection rationale: Source slug '5-ap-usgov-ced-unit1' matches AP US Government and Politics pattern; unit 1 extracted. Single-unit source — band_count=1.

## Stage: competency clustering

- clusters: **13**
- overall stability flag: `cluster_unstable`
- diagnostics:
  - cluster_count_differs: counts across runs = [13, 12, 13]
  - cluster_missing_in_run2: canonical clusters [7] have no Jaccard>=0.30 match
  - cluster_missing_in_run3: canonical clusters [7] have no Jaccard>=0.30 match
- per-cluster stability:
  - `cluster_01` (Democratic Ideals and Constitutional Foundations): stable — 7 items, dkt=Type 1
  - `cluster_02` (Models of Representative Democracy): stable — 3 items, dkt=Type 1
  - `cluster_03` (Federalist and Anti-Federalist Perspectives): stable — 1 items, dkt=Type 1
  - `cluster_04` (Weaknesses of the Articles of Confederation): stable — 3 items, dkt=Type 1
  - `cluster_05` (Constitutional Compromises and Ratification): stable — 6 items, dkt=Type 1
  - `cluster_06` (Separation of Powers and Checks and Balances): stable — 10 items, dkt=Type 1
  - `cluster_07` (Federalism and the Distribution of Power): stable — 15 items, dkt=Type 1
  - `cluster_08` (Contemporary Constitutional Issues): cluster_unstable — 2 items, dkt=Type 1
  - `cluster_09` (Describing Political Principles and Institutions): stable — 5 items, dkt=Type 2
  - `cluster_10` (Analysing Arguments and Sources): stable — 4 items, dkt=Type 2
  - `cluster_11` (Applying Concepts to Scenarios): stable — 3 items, dkt=Type 2
  - `cluster_12` (Constructing and Supporting Arguments): stable — 6 items, dkt=Type 2
  - `cluster_13` (Understanding Governmental Terminology): stable — 2 items, dkt=Type 1

## Stage: LT generation

- LTs: **26** (halted clusters: 1)
- knowledge-type split: Type 1=16, Type 2=10, Type 3=0
- LT stability: {'stable': 22, 'lt_set_unstable': 4}
- halted clusters:
  - `cluster_01`: lt_set_unreliable — only 0/3 runs produced parseable output

## Stage: Type 1/2 band statements

- band sets: **26** (halted LTs: 0)
- stability: {'stable': 25, 'band_statements_unstable': 1}

## Stage: Type 3 observation indicators

- indicator sets: **0** (halted LTs: 0)
- stability: {}

## Stage: Type 1/2 criterion rubrics

- rubrics: **15** (halted LTs: 11)
- stability: {'rubric_unstable': 10, 'stable': 5}
- rubrics with gate failures: 5
- competent-framing judge: 0 fail
- propositional_lt_rubric_thin_flag: 4
- halted:
  - `cluster_02_lt_02`: rubric_unreliable — only 0/3 runs produced parseable output
  - `cluster_03_lt_01`: rubric_unreliable — no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'analyse'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'scoped'))]
  - `cluster_03_lt_02`: rubric_unreliable — no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'analyse'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'analyse'), ('competent_scope', 'unscoped'))]
  - `cluster_04_lt_03`: rubric_unreliable — no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'evaluate'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'none'), ('competent', 'within_limit', 'evaluate'), ('extending', 'within_limit', 'evaluate'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'evaluate'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'evaluate'), ('competent', 'within_limit', 'evaluate'), ('extending', 'within_limit', 'evaluate'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'evaluate'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'evaluate'), ('competent', 'within_limit', 'evaluate'), ('extending', 'within_limit', 'evaluate'), ('competent_scope', 'unscoped'))]
  - `cluster_06_lt_01`: rubric_unreliable — no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'unscoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'unscoped'))]
  - `cluster_06_lt_02`: rubric_unreliable — only 0/3 runs produced parseable output
  - `cluster_07_lt_02`: rubric_unreliable — no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'apply'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'apply'), ('competent_scope', 'unscoped'))]
  - `cluster_08_lt_01`: rubric_unreliable — only 0/3 runs produced parseable output
  - `cluster_08_lt_02`: rubric_unreliable — only 0/3 runs produced parseable output
  - `cluster_11_lt_02`: rubric_unreliable — no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'apply'), ('emerging', 'within_limit', 'apply'), ('developing', 'within_limit', 'apply'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'apply'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'apply'), ('emerging', 'within_limit', 'apply'), ('developing', 'within_limit', 'apply'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'apply'), ('competent_scope', 'unscoped')), (('no_evidence', 'within_limit', 'apply'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'scoped'))]
  - `cluster_12_lt_02`: rubric_unreliable — no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'none'), ('emerging', 'within_limit', 'none'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'none'), ('competent_scope', 'unscoped')), (('no_evidence', 'within_limit', 'none'), ('emerging', 'within_limit', 'none'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'unscoped'))]

### Criterion gate details

**Overall:** HALTED
**Halted by:** `criterion_gates`

## Summary

- **rubrics_total:** 15
- **rubrics_halted_lts:** 11
- **rubrics_with_gate_failures:** 5
- **rubrics_competent_judge_fail:** 0
- **rubrics_propositional_thin_flag:** 4
- **stability_distribution:** rubric_unstable=10, stable=5

## Per-LT gate results

### `cluster_02_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the LT's level of demand, with no hedging language or framing of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_04_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner 'identifies how' the specified limitations affected the Articles, which matches the LT's demand without hedging language or framing Competent as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_04_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner 'explains how' the connection works, matching the LT's demand without hedging, incompleteness markers, or positioning it as a waystation to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_05_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the learner can identify and accurately describe major compromises and their structural outcomes, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_05_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('emerging', 'developing')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated ('Explains how multiple specific compromises...') without hedging language, incompleteness markers, or positioning it as a way-station to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_07_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the learner as independently demonstrating the capability to identify, distinguish, and explain all three power types and their authority allocation—matching the LT's level of demand with no hedging language or incompleteness framing.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_07_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated without hedging language, frames Competent as meeting the LT's demands (identify, compare, explain), and stands alone as success without implying incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_09_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent, accurate identification across different scenarios and contexts, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_09_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to describe how political elements operate across different scenarios and contexts accurately, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_10_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and at the LT's level of demand ('identifies and extracts...accurately'), with no hedging language or framing of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_10_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['developing']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to explain connections between arguments and political frameworks at the level demanded by the LT, with no hedging language or implication of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_11_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent identification of multiple relevant political concepts without hedging language, incompleteness markers, or framing Competent as a stepping stone to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_12_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['emerging', 'developing', 'competent', 'extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated ('Articulates') at the target level without hedging, incompleteness language, or framing Competent as a stepping stone to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_13_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the LT's level of demand without hedging language, incompleteness markers, or positioning it as a way-station to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_13_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('developing', 'competent'), ('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to identify and distinguish all required components without hedging language, implying the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

## Stage: supporting components

- components: **8** (halted LTs: 2)
- stability: {'stable': 3, 'supporting_unstable': 5}
- halted:
  - `cluster_04_lt_02`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_09_lt_01`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]

