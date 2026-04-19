# KUD quality report — strand-economic-activity

**Overall:** PASSED

## Summary

- **source_domain:** horizontal
- **inventory_blocks_total:** 47
- **inventory_non_heading_blocks:** 47
- **kud_items_total:** 40
- **halted_blocks_total:** 13
- **halted_severe:** 13
- **halted_unreliable:** 0
- **knowledge_type_distribution:** Type 1=32, Type 2=8
- **kud_column_distribution:** do_skill=10, know=21, understand=9
- **stability_distribution:** classification_unstable=2, stable=38
- **underspecification_distribution:** null=40

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — PASS

KUD items / expected-yield blocks = 40/34 = 1.176 (denominator excludes 13 severely-underspecified blocks) within horizontal-domain target [0.8, 1.5]

### `type3_distribution` — PASS

type3_distribution gate skipped — source is not marked as dispositional-domain

### `no_compound_unsplit` — PASS

every KUD item carries a single knowledge type with consistent column and route

## Stage: source-native progression structure

- source type: `nz_curriculum`
- band count: **8**
- band labels: Level 1, Level 2, Level 3, Level 4, Level 5, Level 6, Level 7, Level 8
- age range hint: ages 5-18 (Ministry of Education NZ; The New Zealand Curriculum)
- detection confidence: `high`
- detection rationale: New Zealand Curriculum source (host=newzealandcurriculum.tahurangi.education.govt.nz). Levels 1-8.

## Stage: competency clustering

- clusters: **5**
- overall stability flag: `stable`
- per-cluster stability:
  - `cluster_01` (Personal Financial Decision Making): stable — 14 items, dkt=Type 1
  - `cluster_02` (Economic Exchange and Trade Systems): stable — 10 items, dkt=Type 1
  - `cluster_03` (Work and Economic Contribution): stable — 4 items, dkt=Type 1
  - `cluster_04` (Business Operations and Enterprise): stable — 7 items, dkt=Type 1
  - `cluster_05` (Credit, Debt, and Financial Planning): stable — 5 items, dkt=Type 1

## Stage: LT generation

- LTs: **12** (halted clusters: 0)
- knowledge-type split: Type 1=7, Type 2=5, Type 3=0
- LT stability: {'stable': 7, 'lt_set_unstable': 5}

## Stage: Type 1/2 band statements

- band sets: **9** (halted LTs: 3)
- stability: {'stable': 7, 'band_statements_unstable': 2}
- halted:
  - `cluster_01_lt_02`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_03_lt_02`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'long'), ('Level 7', 'long'), ('Level 8', 'long')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'long'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'long'), ('Level 8', 'long'))]
  - `cluster_05_lt_02`: band_statements_gate_failed — 1 format/quality failures

## Stage: Type 3 observation indicators

- indicator sets: **0** (halted LTs: 0)
- stability: {}

## Stage: Type 1/2 criterion rubrics

- rubrics: **12** (halted LTs: 0)
- stability: {'stable': 5, 'rubric_unstable': 5, 'rubric_unreliable': 2}
- rubrics with gate failures: 4
- competent-framing judge: 0 fail
- propositional_lt_rubric_thin_flag: 0

### Criterion gate details

**Overall:** HALTED
**Halted by:** `criterion_gates`

## Summary

- **rubrics_total:** 12
- **rubrics_halted_lts:** 0
- **rubrics_with_gate_failures:** 4
- **rubrics_competent_judge_fail:** 0
- **rubrics_propositional_thin_flag:** 0
- **stability_distribution:** rubric_unreliable=2, rubric_unstable=5, stable=5

## Per-LT gate results

### `cluster_01_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and stands alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_01_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as fully demonstrated with words like 'independently,' 'accurately,' 'correctly,' and 'realistic' without any hedging language or implications of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_01_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_02_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner can explain the required concepts without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_03_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor clearly states the learner independently demonstrates the exact capabilities defined in the learning target without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_03_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_04_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently with accurate understanding, standing alone as evidence the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_04_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['developing']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and systematically, standing alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_05_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and accurately, standing alone as evidence that the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_05_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the learning target's level of demand without hedging language or positioning it as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

## Stage: supporting components

- components: **7** (halted LTs: 5)
- stability: {'supporting_unstable': 6, 'stable': 1}
- halted:
  - `cluster_04_lt_01`: supporting_unreliable — no structural signature reached 2/3 agreement; signatures=[(('stages', 4), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 3), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
  - `cluster_01_lt_01`: supporting_skipped_gate_fail — rubric has gate failures ['single_construct']; not a stable anchor for supporting materials
  - `cluster_04_lt_02`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_02_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_02_lt_02; no content to build from
  - `cluster_04_lt_03`: supporting_skipped_gen_fail — rubric generation failed for cluster_04_lt_03; no content to build from


## Flags
Total flags: **24**


### `cluster_02_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_02_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

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

### `cluster_01_lt_02` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_03_lt_02` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'long'), ('Level 7', 'long'), ('Level 8', 'long')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'long'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'long'), ('Level 8', 'long'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_05_lt_02` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_04_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_04_lt_03` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_01_lt_01` — `single_construct` — **HIGH**

**Stage:** criterion rubrics

**Technical:** The single_construct gate checks that adjacent applied levels (Emerging, Developing, Competent, Extending) share at least one topic-lemma. No topic-lemma overlap between adjacent levels is a signal that the rubric may be describing two different things across the progression.

**Pedagogical:** A rubric where adjacent levels use entirely different vocabulary may be assessing different capabilities at different levels, rather than the same capability at different depths. A teacher reviewing this rubric should check whether the construct is genuinely the same across all levels.

**Horizontal-domain note:** In horizontal domains, legitimate conceptual deepening often introduces new vocabulary as the learner moves to higher levels. A single_construct flag may reflect authentic progression rather than construct drift. A teacher should judge whether the vocabulary shift represents deepening the same construct or introducing a different one.

### `cluster_01_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_02_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_03_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_02` — `observable_verb` — **HIGH**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

**Horizontal-domain note:** Horizontal-domain content sometimes uses relational or orientational language rather than action verbs. A flag here may indicate that the rubric is using legitimately different (but observable) language that the gate's verb list does not include.

### `cluster_05_lt_01` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_02_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_03` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_01` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_01_lt_01` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_04_lt_02` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_02_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_04_lt_03` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

