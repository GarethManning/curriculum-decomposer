# KUD quality report — 2a-secondary-rshe-2025

**Overall:** PASSED

## Summary

- **source_domain:** dispositional
- **inventory_blocks_total:** 249
- **inventory_non_heading_blocks:** 132
- **kud_items_total:** 149
- **halted_blocks_total:** 37
- **halted_severe:** 36
- **halted_unreliable:** 1
- **knowledge_type_distribution:** Type 1=115, Type 2=29, Type 3=5
- **kud_column_distribution:** do_disposition=5, do_skill=29, know=69, understand=46
- **stability_distribution:** classification_unstable=28, stable=121
- **underspecification_distribution:** mild=1, moderate=3, null=145

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — PASS

KUD items / expected-yield blocks = 149/96 = 1.552 (denominator excludes 36 severely-underspecified blocks) within dispositional-domain target [0.8, 2.2] (dispositional ceiling is PROVISIONAL per 4b-2; next dispositional source may re-trigger review)

### `type3_distribution` — FLAG

dispositional_content_underrepresented: Type 3 items = 5/149 = 3.4% < expected ≥20% for dispositional domain (informational only)

### `no_compound_unsplit` — PASS

every KUD item carries a single knowledge type with consistent column and route

## Stage: source-native progression structure

- source type: `england_rshe_secondary`
- band count: **1**
- band labels: End of Secondary
- age range hint: ages 11-16 (DfE RSHE statutory guidance; secondary phase = Years 7-11, KS3 + KS4; outcomes framed as 'by the end of secondary school')
- detection confidence: `high`
- detection rationale: DfE RSHE statutory guidance detected (host=assets.publishing.service.gov.uk, path contains 'relationships'). Single-band End-of-Secondary structure (ages 11-16).

## Stage: competency clustering

- clusters: **27**
- overall stability flag: `cluster_unstable`
- diagnostics:
  - cluster_count_differs: counts across runs = [27, 41, 34]
  - membership_drift_run2: 22.15% of items reassigned vs run1 (threshold 20%)
  - dominant_type_drift_run2: canonical cluster 8 (Type 2) → run2 cluster 13 (Type 1)
  - dominant_type_drift_run3: canonical cluster 3 (Type 1) → run3 cluster 3 (Type 2)
  - dominant_type_drift_run3: canonical cluster 8 (Type 2) → run3 cluster 11 (Type 1)
- per-cluster stability:
  - `cluster_01` (Family Structures and Legal Relationships): stable — 5 items, dkt=Type 1
  - `cluster_02` (Healthy Romantic Relationships): stable — 4 items, dkt=Type 1
  - `cluster_03` (Respectful Treatment of Self and Others): stable — 6 items, dkt=Type 1
  - `cluster_04` (Addressing Bullying and Relationship Endings): cluster_unstable — 5 items, dkt=Type 1
  - `cluster_05` (Recognising Stereotypes and Power Dynamics): stable — 5 items, dkt=Type 1
  - `cluster_06` (Online Safety and Digital Citizenship): stable — 6 items, dkt=Type 1
  - `cluster_07` (Managing Digital Content and Image Sharing): stable — 8 items, dkt=Type 1
  - `cluster_08` (Identifying Digital Manipulation and Harmful Content): stable — 7 items, dkt=Type 1
  - `cluster_09` (Recognising Online Abuse and Exploitation): cluster_unstable — 2 items, dkt=Type 2
  - `cluster_10` (Online Privacy, Scams and Emerging Technology Risks): stable — 7 items, dkt=Type 1
  - `cluster_11` (Consent and Boundaries in Relationships): stable — 4 items, dkt=Type 2
  - `cluster_12` (Assessing Trustworthiness and Personal Safety): stable — 7 items, dkt=Type 2
  - `cluster_13` (Understanding Sexual Harassment and Violence): stable — 3 items, dkt=Type 1
  - `cluster_14` (Recognising Domestic Abuse and Exploitation): stable — 4 items, dkt=Type 1
  - `cluster_15` (Understanding Harmful Practices and Physical Harms): stable — 5 items, dkt=Type 1
  - `cluster_16` (Healthy Sexual Relationships and Decision-Making): stable — 6 items, dkt=Type 1
  - `cluster_17` (Contraception, Pregnancy and Sexual Health): stable — 10 items, dkt=Type 1
  - `cluster_18` (Emotional Wellbeing and Mental Health Literacy): stable — 8 items, dkt=Type 1
  - `cluster_19` (Substance Use and Mental Health): stable — 3 items, dkt=Type 1
  - `cluster_20` (Digital Wellbeing and Online Harms): stable — 13 items, dkt=Type 1
  - `cluster_21` (Nutrition and Diet-Related Health): stable — 2 items, dkt=Type 1
  - `cluster_22` (Drugs, Alcohol and Tobacco): stable — 6 items, dkt=Type 1
  - `cluster_23` (Health Maintenance and Prevention): stable — 9 items, dkt=Type 1
  - `cluster_24` (Accessing Healthcare Services): stable — 3 items, dkt=Type 1
  - `cluster_25` (Managing Personal Safety and Risk): stable — 4 items, dkt=Type 2
  - `cluster_26` (Weapons, Exploitation and Seeking Help): stable — 3 items, dkt=Type 1
  - `cluster_27` (Reproductive Health and First Aid Knowledge): stable — 4 items, dkt=Type 1

## Stage: LT generation

- LTs: **66** (halted clusters: 0)
- knowledge-type split: Type 1=43, Type 2=19, Type 3=4
- LT stability: {'stable': 58, 'lt_set_unstable': 8}

## Stage: Type 1/2 band statements

- band sets: **61** (halted LTs: 1)
- stability: {'stable': 60, 'band_statements_unstable': 1}
- halted:
  - `cluster_17_lt_03`: band_statements_gate_failed — 1 format/quality failures

## Stage: Type 3 observation indicators

- indicator sets: **4** (halted LTs: 0)
- stability: {'stable': 4}

## Stage: Type 1/2 criterion rubrics

- rubrics: **62** (halted LTs: 0)
- stability: {'stable': 17, 'rubric_unstable': 39, 'rubric_unreliable': 6}
- rubrics with gate failures: 26
- competent-framing judge: 0 fail
- propositional_lt_rubric_thin_flag: 4

### Criterion gate details

**Overall:** HALTED
**Halted by:** `criterion_gates`

## Summary

- **rubrics_total:** 62
- **rubrics_halted_lts:** 0
- **rubrics_with_gate_failures:** 26
- **rubrics_competent_judge_fail:** 0
- **rubrics_propositional_thin_flag:** 4
- **stability_distribution:** rubric_unreliable=6, rubric_unstable=39, stable=17

## Per-LT gate results

### `cluster_01_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_01_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently, stating the learner 'explains' and 'identifies' the required content without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_02_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and stands alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_02_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently demonstrates the capability with accuracy, indicating full achievement of the learning target.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_03_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner 'independently explains' and 'describes' the required concepts, demonstrating complete achievement of the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_03_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and effectively, standing alone as clear evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_04_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated with 'independently applies appropriate strategies' and shows complete mastery of the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_05_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently with clear reasoning, standing alone as evidence the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_05_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently demonstrates the full capability described in the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_06_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated with 'independently identifies' and 'explains clearly' without any hedging language or positioning as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_06_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['emerging']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently demonstrates the capability at the target level without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_06_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner can independently demonstrate the exact capability described in the learning target without any hedging language or positioning as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_07_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner 'independently explains' the required content, demonstrating complete achievement of the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_08_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('emerging', 'developing')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and accurately, meeting the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_08_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated with 'independently describes' and 'clearly explains' without any hedging language or positioning as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_08_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner can independently identify appropriate support sources, demonstrating complete achievement of the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_09_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated with 'independently recognises' and 'determines appropriate support responses accurately' without any hedging language or positioning as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_09_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_10_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner explains and identifies the required concepts without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_10_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('emerging', 'developing'), ('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — FAIL (halts): Competent descriptor uses deficit hedge-phrasing: ['\\bemerging\\b']
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner 'independently identifies' and 'determines appropriate responses' which demonstrates full capability without hedging language or positioning as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_11_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated with 'independently' and 'consistently' indicating complete mastery of the learning target.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_11_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated by stating the learner 'explains' the concept fully, without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_12_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['competent', 'extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated independently with appropriate reasoning strategies across various contexts, standing alone as evidence the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_12_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and can stand alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_13_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['emerging']
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('developing', 'competent')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently demonstrates the exact capability defined in the learning target without hedging or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_14_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_14_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently and accurately demonstrates the capability without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_15_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently and accurately identifies the required practices, demonstrating complete mastery of the learning target.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_15_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and can stand alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_15_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('developing', 'competent'), ('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner can describe and identify the required elements without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_16_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and can stand alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_16_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated accurately and independently, standing alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_16_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_17_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_17_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner can independently and accurately perform the target capability without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_17_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['competent']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_18_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('emerging', 'developing'), ('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated with 'independently communicates' and shows complete mastery of the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_18_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner can independently perform the required capabilities without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_19_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_19_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('developing', 'competent'), ('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and stands alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_20_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated with accurate connections and reasoning, standing alone as evidence the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_20_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and can stand alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_21_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently demonstrates the capability at the target level without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_21_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently recognizes the specific health consequences mentioned in the learning target, demonstrating complete achievement without hedging language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_22_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated with 'independently identifies comprehensive health risks and legal consequences...accurately' without any hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_22_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner can explain and describe the required capabilities without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_23_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and accurately, standing alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_23_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and comprehensively, standing alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_24_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently demonstrates the capability and accurately explains access methods, indicating full achievement of the learning target.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_24_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated accurately and independently, standing alone as evidence the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_25_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently and consistently demonstrates the full capability described in the learning target without any hedging language or implications of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_25_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_25_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_26_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner 'independently identifies appropriate help sources' which demonstrates the capability is fully met without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_27_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and accurately, standing alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_27_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated independently and accurately, meeting the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

## Stage: supporting components

- components: **28** (halted LTs: 34)
- stability: {'supporting_unstable': 22, 'stable': 6}
- halted:
  - `cluster_01_lt_02`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_14_lt_02`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_16_lt_01`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 4), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 3), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_21_lt_01`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 4), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_21_lt_02`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 3), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_22_lt_01`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 3), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 3), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_22_lt_02`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 3), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_24_lt_02`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_02_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_03_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_03_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_04_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_06_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_08_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_10_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb', 'single_construct', 'competent_framing_regex']; not a stable anchor for supporting materials
  - `cluster_11_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_12_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_13_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb', 'single_construct']; not a stable anchor for supporting materials
  - `cluster_15_lt_03`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_16_lt_03`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_17_lt_03`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_18_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb', 'single_construct']; not a stable anchor for supporting materials
  - `cluster_19_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_25_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_25_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_25_lt_03`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_27_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_27_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_04_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_04_lt_01; no content to build from
  - `cluster_07_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_07_lt_02; no content to build from
  - `cluster_11_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_11_lt_01; no content to build from
  - `cluster_13_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_13_lt_01; no content to build from
  - `cluster_20_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_20_lt_02; no content to build from
  - `cluster_26_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_26_lt_01; no content to build from


## Flags
Total flags: **97**


### `blk_0176` — `classification_unreliable` — **MEDIUM**

**Stage:** KUD classification

**Technical:** The KUD classifier ran 3 times on this source block; fewer than 2/3 runs agreed on the knowledge type (Type 1 / 2 / 3). The block was halted rather than forced into an uncertain classification.

**Pedagogical:** If the classifier can't agree on whether this is declarative knowledge, a skill, or a disposition, the LT derived from it may not accurately reflect the source intent. A teacher should check the original source block and decide the classification manually before using this LT.

### `competency_clusters` — `cluster_unstable (cluster_count_differs: counts across runs = [27, 41, 34]; membership_drift_run2: 22.15% of items reassigned vs run1 (threshold 20%); dominant_type_drift_run2: canonical cluster 8 (Type 2) → run2 cluster 13 (Type 1); dominant_type_drift_run3: canonical cluster 3 (Type 1) → run3 cluster 3 (Type 2); dominant_type_drift_run3: canonical cluster 8 (Type 2) → run3 cluster 11 (Type 1))` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

### `cluster_04` — `cluster_unstable` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

### `cluster_09` — `cluster_unstable` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

### `cluster_04_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_04_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_04_lt_03` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_09_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_09_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_12_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_12_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_12_lt_03` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_17_lt_03` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_06_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_02_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_02_lt_02` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_03_lt_01` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_03_lt_02` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_04_lt_02` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_05_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_05_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_06_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_06_lt_02` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_06_lt_03` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_08_lt_01` — `single_construct` — **HIGH**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

### `cluster_08_lt_03` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_09_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_09_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_10_lt_02` — `observable_verb, single_construct, competent_framing_regex` — **LOW**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_11_lt_02` — `observable_verb` — **HIGH**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_11_lt_03` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_12_lt_01` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_12_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_13_lt_02` — `observable_verb, single_construct` — **LOW**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_14_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_14_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_15_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_15_lt_03` — `single_construct` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

### `cluster_16_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_16_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_16_lt_03` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_17_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_17_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_17_lt_03` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_18_lt_01` — `observable_verb, single_construct` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_19_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_19_lt_02` — `single_construct` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

### `cluster_20_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_20_lt_03` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_21_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_22_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_24_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_25_lt_01` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_25_lt_02` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_25_lt_03` — `observable_verb` — **HIGH**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_27_lt_01` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_27_lt_02` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

### `cluster_04_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_07_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_11_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_13_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_20_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_26_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

### `cluster_01_lt_02` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_14_lt_02` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_16_lt_01` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_21_lt_01` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_21_lt_02` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_22_lt_01` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_22_lt_02` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_24_lt_02` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_02_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_03_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_03_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_04_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_06_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_08_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_10_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_11_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_12_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_13_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_15_lt_03` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_16_lt_03` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_17_lt_03` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_18_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_19_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_25_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_25_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_25_lt_03` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_27_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_27_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_04_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_07_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_11_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_13_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_20_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_26_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

