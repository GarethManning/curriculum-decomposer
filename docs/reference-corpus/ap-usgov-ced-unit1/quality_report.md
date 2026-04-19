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

- clusters: **14**
- overall stability flag: `stable`
- per-cluster stability:
  - `cluster_01` (Democratic Ideals and Constitutional Foundations): stable — 7 items, dkt=Type 1
  - `cluster_02` (Models of Representative Democracy): stable — 3 items, dkt=Type 1
  - `cluster_03` (Federalist and Anti-Federalist Perspectives): stable — 1 items, dkt=Type 1
  - `cluster_04` (Weaknesses of the Articles of Confederation): stable — 3 items, dkt=Type 1
  - `cluster_05` (Constitutional Compromises and Ratification): stable — 6 items, dkt=Type 1
  - `cluster_06` (Separation of Powers and Checks and Balances): stable — 10 items, dkt=Type 1
  - `cluster_07` (Federalism and the Distribution of Power): stable — 15 items, dkt=Type 1
  - `cluster_08` (Constitutional Interpretation and Supreme Court Doctrine): stable — 1 items, dkt=Type 1
  - `cluster_09` (Contemporary Constitutional Debates): stable — 2 items, dkt=Type 1
  - `cluster_10` (Describing Political Principles and Institutions in Context): stable — 5 items, dkt=Type 2
  - `cluster_11` (Explaining Political Arguments and Perspectives): stable — 4 items, dkt=Type 2
  - `cluster_12` (Applying Political Principles to Scenarios): stable — 3 items, dkt=Type 2
  - `cluster_13` (Constructing and Supporting Arguments): stable — 6 items, dkt=Type 2
  - `cluster_14` (Understanding Governmental Terminology): stable — 1 items, dkt=Type 1

## Stage: LT generation

- LTs: **26** (halted clusters: 2)
- knowledge-type split: Type 1=16, Type 2=10, Type 3=0
- LT stability: {'stable': 23, 'lt_set_unstable': 3}
- halted clusters:
  - `cluster_01`: lt_set_unreliable — only 1/3 runs produced parseable output
  - `cluster_03`: lt_set_unreliable — only 0/3 runs produced parseable output

## Stage: Type 1/2 band statements

- band sets: **25** (halted LTs: 1)
- stability: {'stable': 24, 'band_statements_unstable': 1}
- halted:
  - `cluster_13_lt_01`: band_statements_gate_failed — 1 format/quality failures

## Stage: Type 3 observation indicators

- indicator sets: **0** (halted LTs: 0)
- stability: {}

## Stage: Type 1/2 criterion rubrics

- rubrics: **26** (halted LTs: 0)
- stability: {'rubric_unstable': 9, 'stable': 10, 'rubric_unreliable': 7}
- rubrics with gate failures: 16
- competent-framing judge: 0 fail
- propositional_lt_rubric_thin_flag: 2

### Criterion gate details

**Overall:** HALTED
**Halted by:** `criterion_gates`

## Summary

- **rubrics_total:** 26
- **rubrics_halted_lts:** 0
- **rubrics_with_gate_failures:** 16
- **rubrics_competent_judge_fail:** 0
- **rubrics_propositional_thin_flag:** 2
- **stability_distribution:** rubric_unreliable=7, rubric_unstable=9, stable=10

## Per-LT gate results

### `cluster_02_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly mirrors the LT definition without hedging language, frames the capability as demonstrated, and stands alone as evidence the target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_04_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner 'explains how specific incidents exposed gaps,' which demonstrates the capability required by the LT without hedging language, incompleteness markers, or positioning it as a way-station to a higher level.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_05_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to explain how each compromise resolved conflicts, matching the LT's demand without hedging, incompleteness framing, or positioning as a way-station to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_05_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the learner can analyze how compromises and the Bill of Rights shaped ratification debates and the amendment process, which directly matches the LT's demand without hedging or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_07_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to identify and distinguish the three power categories at the level demanded by the LT, with no hedging language or implication of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_07_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('emerging', 'developing')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner 'explains' the core concepts without hedging language, frames the capability as demonstrated, and aligns with the LT's level of demand without implying incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_07_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the learner can describe all four mechanisms and explain their relationship to power distribution, which directly matches the LT's demand without hedging or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_08_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent demonstration of all required capabilities (identify and explain facts, issue, holding, reasoning, decision) at the target level without hedging or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_08_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to explain how all four constitutional doctrines shape federal-state power balance, matching the LT's demand without hedging or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_10_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent, accurate identification across different scenarios and contexts without hedging language, positioning Competent as meeting the Learning Target.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_10_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated and matches the LT's core demand without hedging language, incompleteness markers, or positioning it as a way-station to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_11_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as independently demonstrated at the LT's level of demand, with no hedging language or framing of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_11_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the LT's level of demand, using no hedging language or deficit framing, and can stand alone as evidence the LT is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_12_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to explain application of political principles to different scenarios with accurate reasoning, which directly matches the LT's demand and stands alone as success.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_12_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent, accurate, and complete identification of all required elements without hedging language or framing Competent as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_13_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['emerging', 'developing', 'competent', 'extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated ('Articulates') at the target level ('defensible claim or thesis that moves beyond facts and takes a reasoned position') and can stand alone as evidence the LT is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_13_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['emerging']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated without hedging language, frames it as meeting the LT's demand, and stands alone as success.
- **level_progression** — FAIL (halts): level-progression violations: ['developing_missing_hedge_or_gap_marker']
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_14_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as independently demonstrated and directly aligns with the LT's demand to identify and state definitions, with no hedging language or framing of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_14_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as independently demonstrated at the LT's level of demand ('explains accurate differences...using precise, complete definitions') without hedging language or framing it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

## Stage: supporting components

- components: **9** (halted LTs: 17)
- stability: {'supporting_unstable': 8, 'stable': 1}
- halted:
  - `cluster_08_lt_01`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 3), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_04_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_05_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_07_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_07_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_07_lt_03`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_08_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_13_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_13_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb', 'level_progression']; not a stable anchor for supporting materials
  - `cluster_14_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_02_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_02_lt_01; no content to build from
  - `cluster_04_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_04_lt_01; no content to build from
  - `cluster_04_lt_03`: supporting_skipped_gen_fail — rubric generation failed for cluster_04_lt_03; no content to build from
  - `cluster_06_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_06_lt_01; no content to build from
  - `cluster_06_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_06_lt_02; no content to build from
  - `cluster_09_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_09_lt_01; no content to build from
  - `cluster_09_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_09_lt_02; no content to build from


## Flags
Total flags: **50**


### `blk_0068` — `classification_unreliable` — **MEDIUM**

**Stage:** KUD classification

**Technical:** The KUD classifier ran 3 times on this source block; fewer than 2/3 runs agreed on the knowledge type (Type 1 / 2 / 3). The block was halted rather than forced into an uncertain classification.

**Pedagogical:** If the classifier can't agree on whether this is declarative knowledge, a skill, or a disposition, the LT derived from it may not accurately reflect the source intent. A teacher should check the original source block and decide the classification manually before using this LT.

**Horizontal-domain note:** In horizontal domains, a single source block may legitimately describe both a cognitive skill (Type 2) and a dispositional orientation (Type 3). The classification disagreement may reflect genuine domain complexity rather than an error.

### `blk_0108` — `classification_unreliable` — **MEDIUM**

**Stage:** KUD classification

**Technical:** The KUD classifier ran 3 times on this source block; fewer than 2/3 runs agreed on the knowledge type (Type 1 / 2 / 3). The block was halted rather than forced into an uncertain classification.

**Pedagogical:** If the classifier can't agree on whether this is declarative knowledge, a skill, or a disposition, the LT derived from it may not accurately reflect the source intent. A teacher should check the original source block and decide the classification manually before using this LT.

**Horizontal-domain note:** In horizontal domains, a single source block may legitimately describe both a cognitive skill (Type 2) and a dispositional orientation (Type 3). The classification disagreement may reflect genuine domain complexity rather than an error.

### `blk_0154` — `classification_unreliable` — **MEDIUM**

**Stage:** KUD classification

**Technical:** The KUD classifier ran 3 times on this source block; fewer than 2/3 runs agreed on the knowledge type (Type 1 / 2 / 3). The block was halted rather than forced into an uncertain classification.

**Pedagogical:** If the classifier can't agree on whether this is declarative knowledge, a skill, or a disposition, the LT derived from it may not accurately reflect the source intent. A teacher should check the original source block and decide the classification manually before using this LT.

**Horizontal-domain note:** In horizontal domains, a single source block may legitimately describe both a cognitive skill (Type 2) and a dispositional orientation (Type 3). The classification disagreement may reflect genuine domain complexity rather than an error.

### `blk_0157` — `classification_unreliable` — **MEDIUM**

**Stage:** KUD classification

**Technical:** The KUD classifier ran 3 times on this source block; fewer than 2/3 runs agreed on the knowledge type (Type 1 / 2 / 3). The block was halted rather than forced into an uncertain classification.

**Pedagogical:** If the classifier can't agree on whether this is declarative knowledge, a skill, or a disposition, the LT derived from it may not accurately reflect the source intent. A teacher should check the original source block and decide the classification manually before using this LT.

**Horizontal-domain note:** In horizontal domains, a single source block may legitimately describe both a cognitive skill (Type 2) and a dispositional orientation (Type 3). The classification disagreement may reflect genuine domain complexity rather than an error.

### `blk_0183` — `classification_unreliable` — **MEDIUM**

**Stage:** KUD classification

**Technical:** The KUD classifier ran 3 times on this source block; fewer than 2/3 runs agreed on the knowledge type (Type 1 / 2 / 3). The block was halted rather than forced into an uncertain classification.

**Pedagogical:** If the classifier can't agree on whether this is declarative knowledge, a skill, or a disposition, the LT derived from it may not accurately reflect the source intent. A teacher should check the original source block and decide the classification manually before using this LT.

**Horizontal-domain note:** In horizontal domains, a single source block may legitimately describe both a cognitive skill (Type 2) and a dispositional orientation (Type 3). The classification disagreement may reflect genuine domain complexity rather than an error.

### `blk_0315` — `classification_unreliable` — **MEDIUM**

**Stage:** KUD classification

**Technical:** The KUD classifier ran 3 times on this source block; fewer than 2/3 runs agreed on the knowledge type (Type 1 / 2 / 3). The block was halted rather than forced into an uncertain classification.

**Pedagogical:** If the classifier can't agree on whether this is declarative knowledge, a skill, or a disposition, the LT derived from it may not accurately reflect the source intent. A teacher should check the original source block and decide the classification manually before using this LT.

**Horizontal-domain note:** In horizontal domains, a single source block may legitimately describe both a cognitive skill (Type 2) and a dispositional orientation (Type 3). The classification disagreement may reflect genuine domain complexity rather than an error.

### `cluster_01` — `lt_set_unreliable — only 1/3 runs produced parseable output` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator ran 3 times on this cluster; fewer than 2/3 runs produced parseable LT output with a consistent count and knowledge-type distribution. No LTs were produced for this cluster.

**Pedagogical:** The source content in this competency cluster did not produce stable learning targets. The content may be too loosely specified, or the cluster may contain content from multiple distinct competencies. A teacher should review the cluster's KUD items and consider manual LT authoring.

**Horizontal-domain note:** In horizontal domains, large clusters containing conceptually dense content are more prone to LT generation instability. This may reflect genuine conceptual depth rather than a pipeline error.

### `cluster_03` — `lt_set_unreliable — only 0/3 runs produced parseable output` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator ran 3 times on this cluster; fewer than 2/3 runs produced parseable LT output with a consistent count and knowledge-type distribution. No LTs were produced for this cluster.

**Pedagogical:** The source content in this competency cluster did not produce stable learning targets. The content may be too loosely specified, or the cluster may contain content from multiple distinct competencies. A teacher should review the cluster's KUD items and consider manual LT authoring.

**Horizontal-domain note:** In horizontal domains, large clusters containing conceptually dense content are more prone to LT generation instability. This may reflect genuine conceptual depth rather than a pipeline error.

### `cluster_04_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_04_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_04_lt_03` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_13_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_02_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_02_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_02` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

**Horizontal-domain note:** Horizontal-domain content sometimes uses relational or orientational language rather than action verbs. A flag here may indicate that the rubric is using legitimately different (but observable) language that the gate's verb list does not include.

### `cluster_05_lt_01` — `single_construct` — **HIGH**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

**Horizontal-domain note:** In horizontal domains, legitimate conceptual deepening often introduces new vocabulary as the learner moves to higher levels. A single_construct flag may reflect authentic progression rather than construct drift. A teacher should judge whether the vocabulary shift represents deepening the same construct or introducing a different one.

### `cluster_07_lt_01` — `single_construct` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

**Horizontal-domain note:** In horizontal domains, legitimate conceptual deepening often introduces new vocabulary as the learner moves to higher levels. A single_construct flag may reflect authentic progression rather than construct drift. A teacher should judge whether the vocabulary shift represents deepening the same construct or introducing a different one.

### `cluster_07_lt_02` — `single_construct` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

**Horizontal-domain note:** In horizontal domains, legitimate conceptual deepening often introduces new vocabulary as the learner moves to higher levels. A single_construct flag may reflect authentic progression rather than construct drift. A teacher should judge whether the vocabulary shift represents deepening the same construct or introducing a different one.

### `cluster_07_lt_03` — `single_construct` — **HIGH**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

**Horizontal-domain note:** In horizontal domains, legitimate conceptual deepening often introduces new vocabulary as the learner moves to higher levels. A single_construct flag may reflect authentic progression rather than construct drift. A teacher should judge whether the vocabulary shift represents deepening the same construct or introducing a different one.

### `cluster_08_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_08_lt_02` — `single_construct` — **HIGH**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

**Horizontal-domain note:** In horizontal domains, legitimate conceptual deepening often introduces new vocabulary as the learner moves to higher levels. A single_construct flag may reflect authentic progression rather than construct drift. A teacher should judge whether the vocabulary shift represents deepening the same construct or introducing a different one.

### `cluster_12_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_13_lt_01` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

**Horizontal-domain note:** Horizontal-domain content sometimes uses relational or orientational language rather than action verbs. A flag here may indicate that the rubric is using legitimately different (but observable) language that the gate's verb list does not include.

### `cluster_13_lt_02` — `observable_verb, level_progression` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

**Horizontal-domain note:** Horizontal-domain content sometimes uses relational or orientational language rather than action verbs. A flag here may indicate that the rubric is using legitimately different (but observable) language that the gate's verb list does not include.

### `cluster_14_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_14_lt_02` — `single_construct` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

**Horizontal-domain note:** In horizontal domains, legitimate conceptual deepening often introduces new vocabulary as the learner moves to higher levels. A single_construct flag may reflect authentic progression rather than construct drift. A teacher should judge whether the vocabulary shift represents deepening the same construct or introducing a different one.

### `cluster_02_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_03` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_06_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_06_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_09_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_09_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_08_lt_01` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_04_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_05_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_07_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_07_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_07_lt_03` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_08_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_13_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_13_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_14_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_02_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_04_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_04_lt_03` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_06_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_06_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_09_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_09_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

