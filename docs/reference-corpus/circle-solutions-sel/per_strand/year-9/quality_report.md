# KUD quality report — strand-year-9

**Overall:** PASSED

## Summary

- **source_domain:** dispositional
- **inventory_blocks_total:** 41
- **inventory_non_heading_blocks:** 28
- **kud_items_total:** 32
- **halted_blocks_total:** 0
- **halted_severe:** 0
- **halted_unreliable:** 0
- **knowledge_type_distribution:** Type 1=8, Type 2=17, Type 3=7
- **kud_column_distribution:** do_disposition=7, do_skill=20, know=5
- **stability_distribution:** classification_unstable=1, stable=31
- **underspecification_distribution:** null=32

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — PASS

KUD items / expected-yield blocks = 32/28 = 1.143 (denominator excludes 0 severely-underspecified blocks) within dispositional-domain target [0.8, 2.2] (dispositional ceiling is PROVISIONAL per 4b-2; next dispositional source may re-trigger review)

### `type3_distribution` — PASS

Type 3 items = 7/32 = 21.9% (≥20% expected for dispositional domain)

### `no_compound_unsplit` — PASS

every KUD item carries a single knowledge type with consistent column and route

## Stage: source-native progression structure

- source type: `circle_solutions_sel`
- band count: **4**
- band labels: Year 2, Year 6, Year 9, Year 12
- age range hint: ages 7-18 (Cowie & Myers 2016; Year 2 through Year 12; sparse 4-checkpoint structure — Years 3-5, 7-8, 10-11 not explicitly covered)
- detection confidence: `high`
- detection rationale: Source slug 'strand-year-9' / reference 'cowie-myers-2016-circle-solutions-student-wellbeing' matches Circle Solutions SEL pattern (Cowie & Myers, 2016). 4-checkpoint structure: Year 2, 6, 9, 12.

## Stage: competency clustering

- clusters: **12**
- overall stability flag: `cluster_unstable`
- diagnostics:
  - dominant_type_drift_run2: canonical cluster 6 (Type 2) → run2 cluster 6 (Type 3)
- per-cluster stability:
  - `cluster_01` (Self-Awareness and Identity Development): stable — 4 items, dkt=Type 2
  - `cluster_02` (Emotional Knowledge and Understanding): stable — 5 items, dkt=Type 1
  - `cluster_03` (Emotional Regulation and Resilience): stable — 3 items, dkt=Type 2
  - `cluster_04` (Shared Humanity and Social Justice): stable — 2 items, dkt=Type 2
  - `cluster_05` (Interpersonal Communication Skills): stable — 3 items, dkt=Type 2
  - `cluster_06` (Empathy and Social Awareness): stable — 2 items, dkt=Type 3
  - `cluster_07` (Leadership and Goal Achievement): cluster_unstable — 3 items, dkt=Type 2
  - `cluster_08` (Positive Mindset and Solution Focus): stable — 2 items, dkt=Type 3
  - `cluster_09` (Conflict Resolution and Assertiveness): stable — 2 items, dkt=Type 3
  - `cluster_10` (Repair and Restoration): stable — 2 items, dkt=Type 3
  - `cluster_11` (Ethics and Civic Engagement): stable — 2 items, dkt=Type 3
  - `cluster_12` (Meaning and Purpose Exploration): stable — 2 items, dkt=Type 2

## Stage: LT generation

- LTs: **27** (halted clusters: 0)
- knowledge-type split: Type 1=5, Type 2=15, Type 3=7
- LT stability: {'stable': 21, 'lt_set_unstable': 6}

## Stage: Type 1/2 band statements

- band sets: **9** (halted LTs: 11)
- stability: {'stable': 7, 'band_statements_unstable': 2}
- halted:
  - `cluster_01_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_04_lt_02`: band_statements_gate_failed — 2 format/quality failures
  - `cluster_05_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_05_lt_02`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium'))]
  - `cluster_05_lt_03`: band_statements_gate_failed — 3 format/quality failures
  - `cluster_07_lt_01`: band_statements_gate_failed — 3 format/quality failures
  - `cluster_08_lt_01`: band_statements_gate_failed — 2 format/quality failures
  - `cluster_09_lt_01`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'long'), ('Year 12', 'long'))]
  - `cluster_10_lt_01`: band_statements_gate_failed — 2 format/quality failures
  - `cluster_12_lt_01`: band_statements_gate_failed — 4 format/quality failures
  - `cluster_12_lt_02`: band_statements_gate_failed — 2 format/quality failures

## Stage: Type 3 observation indicators

- indicator sets: **7** (halted LTs: 0)
- stability: {'stable': 7}


## Flags
Total flags: **21**


### `competency_clusters` — `cluster_unstable (dominant_type_drift_run2: canonical cluster 6 (Type 2) → run2 cluster 6 (Type 3))` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

### `cluster_07` — `cluster_unstable` — **MEDIUM**

**Stage:** competency clustering

**Technical:** The cluster_unstable flag means the clustering model's output varied across runs — cluster count or member assignment differed across 3 self-consistency runs. The canonical cluster set was retained using the majority-vote result, but alternative groupings exist.

**Pedagogical:** Cluster instability means the competency groupings may not be the only reasonable arrangement. A teacher reviewing these LTs should check whether each LT genuinely represents one distinct capability, or whether some LTs could reasonably be grouped differently.

### `cluster_03_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_03_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_03_lt_03` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_07_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_07_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_07_lt_03` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_01_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_04_lt_02` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_05_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_05_lt_02` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_05_lt_03` — `band_statements_unreliable — 3 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_07_lt_01` — `band_statements_unreliable — 3 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_08_lt_01` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_09_lt_01` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'long'), ('Year 12', 'long'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_10_lt_01` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_12_lt_01` — `band_statements_unreliable — 4 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_12_lt_02` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_07_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_11_lt_01` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

