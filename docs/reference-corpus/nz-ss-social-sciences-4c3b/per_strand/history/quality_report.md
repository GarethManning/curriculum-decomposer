# KUD quality report — strand-history

**Overall:** PASSED

## Summary

- **source_domain:** horizontal
- **inventory_blocks_total:** 150
- **inventory_non_heading_blocks:** 143
- **kud_items_total:** 109
- **halted_blocks_total:** 68
- **halted_severe:** 67
- **halted_unreliable:** 1
- **knowledge_type_distribution:** Type 1=80, Type 2=29
- **kud_column_distribution:** do_skill=19, know=65, understand=25
- **stability_distribution:** classification_unstable=27, stable=82
- **underspecification_distribution:** mild=5, moderate=2, null=102

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — PASS

KUD items / expected-yield blocks = 109/76 = 1.434 (denominator excludes 67 severely-underspecified blocks) within horizontal-domain target [0.8, 1.5]

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

- clusters: **9**
- overall stability flag: `cluster_unstable`
- diagnostics:
  - cluster_count_differs: counts across runs = [9, 9, 7]
  - cluster_missing_in_run3: canonical clusters [6, 7] have no Jaccard>=0.30 match
  - dominant_type_drift_run3: canonical cluster 2 (Type 1) → run3 cluster 2 (Type 2)
- per-cluster stability:
  - `cluster_01` (Treaty of Waitangi and Colonial Foundations): stable — 11 items, dkt=Type 1
  - `cluster_02` (Natural Events and Historical Impact): stable — 8 items, dkt=Type 2
  - `cluster_03` (Early European Contact and Cultural Exchange): cluster_unstable — 16 items, dkt=Type 1
  - `cluster_04` (Ancient Greek Civilization): stable — 15 items, dkt=Type 1
  - `cluster_05` (Ancient Chinese Civilization): stable — 12 items, dkt=Type 1
  - `cluster_06` (Elizabethan England): stable — 16 items, dkt=Type 1
  - `cluster_07` (Victorian England): cluster_unstable — 11 items, dkt=Type 1
  - `cluster_08` (Historical Comparison and Analysis): cluster_unstable — 4 items, dkt=Type 2
  - `cluster_09` (Roman Civilization): stable — 16 items, dkt=Type 1

## Stage: LT generation

- LTs: **23** (halted clusters: 0)
- knowledge-type split: Type 1=13, Type 2=10, Type 3=0
- LT stability: {'lt_set_unstable': 8, 'stable': 15}

## Stage: Type 1/2 band statements

- band sets: **19** (halted LTs: 4)
- stability: {'band_statements_unstable': 9, 'stable': 10}
- halted:
  - `cluster_01_lt_03`: band_statements_gate_failed — 3 format/quality failures
  - `cluster_03_lt_01`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'long'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'long'), ('Level 5', 'medium'), ('Level 6', 'long'), ('Level 7', 'medium'), ('Level 8', 'long')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium'))]
  - `cluster_04_lt_01`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Level 1', 'short'), ('Level 2', 'short'), ('Level 3', 'short'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'short'), ('Level 2', 'short'), ('Level 3', 'short'), ('Level 4', 'short'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium'))]
  - `cluster_08_lt_02`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Level 1', 'short'), ('Level 2', 'short'), ('Level 3', 'short'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'short'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'short'), ('Level 2', 'short'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium'))]

## Stage: Type 3 observation indicators

- indicator sets: **0** (halted LTs: 0)
- stability: {}

## Stage: Type 1/2 criterion rubrics

- rubrics: **23** (halted LTs: 0)
- stability: {'stable': 4, 'rubric_unstable': 2, 'rubric_unreliable': 17}
- rubrics with gate failures: 18
- competent-framing judge: 0 fail
- propositional_lt_rubric_thin_flag: 0

### Criterion gate details

**Overall:** HALTED
**Halted by:** `criterion_gates`

## Summary

- **rubrics_total:** 23
- **rubrics_halted_lts:** 0
- **rubrics_with_gate_failures:** 18
- **rubrics_competent_judge_fail:** 0
- **rubrics_propositional_thin_flag:** 0
- **stability_distribution:** rubric_unreliable=17, rubric_unstable=2, stable=4

## Per-LT gate results

### `cluster_01_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict unavailable (error) — retry recommended
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_01_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict unavailable (error) — retry recommended
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_01_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['emerging', 'developing']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict unavailable (error) — retry recommended
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_02_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict unavailable (error) — retry recommended
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_02_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict unavailable (error) — retry recommended
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_03_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict unavailable (error) — retry recommended
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

## Stage: supporting components

- components: **0** (halted LTs: 23)
- stability: {}
- halted:
  - `cluster_01_lt_01`: supporting_unreliable — only 0/3 runs produced parseable output
  - `cluster_01_lt_02`: supporting_unreliable — only 0/3 runs produced parseable output
  - `cluster_02_lt_01`: supporting_unreliable — only 0/3 runs produced parseable output
  - `cluster_02_lt_02`: supporting_unreliable — only 0/3 runs produced parseable output
  - `cluster_03_lt_01`: supporting_unreliable — only 0/3 runs produced parseable output
  - `cluster_01_lt_03`: supporting_skipped_gate_fail — rubric has gate failures ['observable_verb']; not a stable anchor for supporting materials
  - `cluster_03_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_03_lt_02; no content to build from
  - `cluster_04_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_04_lt_01; no content to build from
  - `cluster_04_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_04_lt_02; no content to build from
  - `cluster_05_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_05_lt_01; no content to build from
  - `cluster_05_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_05_lt_02; no content to build from
  - `cluster_05_lt_03`: supporting_skipped_gen_fail — rubric generation failed for cluster_05_lt_03; no content to build from
  - `cluster_06_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_06_lt_01; no content to build from
  - `cluster_06_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_06_lt_02; no content to build from
  - `cluster_06_lt_03`: supporting_skipped_gen_fail — rubric generation failed for cluster_06_lt_03; no content to build from
  - `cluster_07_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_07_lt_01; no content to build from
  - `cluster_07_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_07_lt_02; no content to build from
  - `cluster_07_lt_03`: supporting_skipped_gen_fail — rubric generation failed for cluster_07_lt_03; no content to build from
  - `cluster_08_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_08_lt_01; no content to build from
  - `cluster_08_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_08_lt_02; no content to build from
  - `cluster_09_lt_01`: supporting_skipped_gen_fail — rubric generation failed for cluster_09_lt_01; no content to build from
  - `cluster_09_lt_02`: supporting_skipped_gen_fail — rubric generation failed for cluster_09_lt_02; no content to build from
  - `cluster_09_lt_03`: supporting_skipped_gen_fail — rubric generation failed for cluster_09_lt_03; no content to build from


## Flags
Total flags: **68**


### `blk_0117` — `classification_unreliable` — **MEDIUM**

**Stage:** KUD classification

**Technical:** The KUD classifier ran 3 times on this source block; fewer than 2/3 runs agreed on the knowledge type (Type 1 / 2 / 3). The block was halted rather than forced into an uncertain classification.

**Pedagogical:** If the classifier can't agree on whether this is declarative knowledge, a skill, or a disposition, the LT derived from it may not accurately reflect the source intent. A teacher should check the original source block and decide the classification manually before using this LT.

**Horizontal-domain note:** In horizontal domains, a single source block may legitimately describe both a cognitive skill (Type 2) and a dispositional orientation (Type 3). The classification disagreement may reflect genuine domain complexity rather than an error.

### `competency_clusters` — `cluster_unstable (cluster_count_differs: counts across runs = [9, 9, 7]; cluster_missing_in_run3: canonical clusters [6, 7] have no Jaccard>=0.30 match; dominant_type_drift_run3: canonical cluster 2 (Type 1) → run3 cluster 2 (Type 2))` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

**Horizontal-domain note:** Horizontal-domain knowledge tends to form denser semantic networks where competency boundaries are legitimately less distinct than in hierarchical domains. This flag may reflect genuine domain complexity rather than a clustering error.

### `cluster_03` — `cluster_unstable` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

**Horizontal-domain note:** Horizontal-domain knowledge tends to form denser semantic networks where competency boundaries are legitimately less distinct than in hierarchical domains. This flag may reflect genuine domain complexity rather than a clustering error.

### `cluster_07` — `cluster_unstable` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

**Horizontal-domain note:** Horizontal-domain knowledge tends to form denser semantic networks where competency boundaries are legitimately less distinct than in hierarchical domains. This flag may reflect genuine domain complexity rather than a clustering error.

### `cluster_08` — `cluster_unstable` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

**Horizontal-domain note:** Horizontal-domain knowledge tends to form denser semantic networks where competency boundaries are legitimately less distinct than in hierarchical domains. This flag may reflect genuine domain complexity rather than a clustering error.

### `cluster_01_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_01_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_01_lt_03` — `lt_set_unstable` — **MEDIUM**

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

### `cluster_05_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_05_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_05_lt_03` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

**Horizontal-domain note:** LT instability is more common in horizontal domains where conceptual overlap between adjacent LTs is normal. The instability may reflect legitimate conceptual continuity rather than a generation error.

### `cluster_01_lt_03` — `band_statements_unreliable — 3 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_03_lt_01` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'long'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'long'), ('Level 5', 'medium'), ('Level 6', 'long'), ('Level 7', 'medium'), ('Level 8', 'long')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_04_lt_01` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Level 1', 'short'), ('Level 2', 'short'), ('Level 3', 'short'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'short'), ('Level 2', 'short'), ('Level 3', 'short'), ('Level 4', 'short'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'medium'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_08_lt_02` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Level 1', 'short'), ('Level 2', 'short'), ('Level 3', 'short'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'short'), ('Level 2', 'medium'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium')), (('Level 1', 'short'), ('Level 2', 'short'), ('Level 3', 'medium'), ('Level 4', 'medium'), ('Level 5', 'medium'), ('Level 6', 'medium'), ('Level 7', 'medium'), ('Level 8', 'medium'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_01_lt_01` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_01_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_03_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_04_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_06_lt_01` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_07_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_07_lt_03` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_09_lt_01` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_09_lt_03` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_01_lt_03` — `observable_verb` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The observable_verb gate checks that each applied level descriptor contains at least one verb from the observable-action-verb list (identify, describe, compare, explain, analyse, evaluate, apply, etc.). No observable verb means the level cannot be reliably assessed.

**Pedagogical:** A rubric level with no observable action verb describes a state of being rather than a demonstrable performance. Teachers need observable verbs to assess whether a learner has met each level — without them, the assessment criteria become subjective.

**Horizontal-domain note:** Horizontal-domain content sometimes uses relational or orientational language rather than action verbs. A flag here may indicate that the rubric is using legitimately different (but observable) language that the gate's verb list does not include.

### `cluster_02_lt_02` — `gate_unknown` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_03_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_04_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_05_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_05_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_05_lt_03` — `rubric_generation_failed` — **MEDIUM**

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

### `cluster_06_lt_03` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_07_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_07_lt_02` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_07_lt_03` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_08_lt_01` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_08_lt_02` — `rubric_generation_failed` — **MEDIUM**

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

### `cluster_09_lt_03` — `rubric_generation_failed` — **MEDIUM**

**Stage:** criterion rubrics

**Technical:** The rubric generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent level-signature. No rubric was produced for this LT. This entry is a placeholder flag — no descriptor text is available.

**Pedagogical:** Without a rubric, this LT cannot be used for criterion-referenced assessment. The LT exists in the output and represents a real competency from the source; a teacher can author a rubric manually using the LT name and definition as the starting point.

**Horizontal-domain note:** Rubric instability is more common in horizontal-domain sources where political, social, or contested vocabulary is used. The generator may be producing legitimately different-but-valid rubric formulations across runs rather than disagreeing about the construct.

### `cluster_01_lt_01` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_01_lt_02` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_02_lt_01` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_02_lt_02` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_03_lt_01` — `supporting_unreliable` — **MEDIUM**

**Stage:** supporting components

**Technical:** The supporting components generator (co-construction plan, student rubric, feedback guide) ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature.

**Pedagogical:** The supporting materials help teachers introduce the rubric to students and give actionable feedback. Without stable supporting components, teachers will need to author these materials manually.

### `cluster_01_lt_03` — `supporting_skipped_gate_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric failed one or more semantic quality gates. A rubric with gate failures is not a stable anchor for co-construction materials.

**Pedagogical:** The rubric for this LT has known quality issues (listed under the rubric's gate failures). Generating student-facing materials from a flawed rubric risks amplifying those issues. Resolve the rubric quality flags before generating supporting components.

### `cluster_03_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_04_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_04_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_05_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_05_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_05_lt_03` — `supporting_skipped_gen_fail` — **MEDIUM**

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

### `cluster_06_lt_03` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_07_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_07_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_07_lt_03` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_08_lt_01` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

### `cluster_08_lt_02` — `supporting_skipped_gen_fail` — **MEDIUM**

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

### `cluster_09_lt_03` — `supporting_skipped_gen_fail` — **MEDIUM**

**Stage:** supporting components

**Technical:** Supporting components were not generated for this LT because the rubric generator itself failed (rubric_generation_failed). There is no rubric content to base co-construction materials on.

**Pedagogical:** No rubric was produced for this LT, so supporting materials cannot be generated. A teacher would need to author a rubric manually first.

