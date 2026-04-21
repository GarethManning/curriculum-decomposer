# KUD quality report — strand-year-2

**Overall:** PASSED

## Summary

- **source_domain:** dispositional
- **inventory_blocks_total:** 41
- **inventory_non_heading_blocks:** 28
- **kud_items_total:** 30
- **halted_blocks_total:** 0
- **halted_severe:** 0
- **halted_unreliable:** 0
- **knowledge_type_distribution:** Type 1=8, Type 2=17, Type 3=5
- **kud_column_distribution:** do_disposition=5, do_skill=23, understand=2
- **stability_distribution:** classification_unstable=2, stable=28
- **underspecification_distribution:** null=30

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — PASS

KUD items / expected-yield blocks = 30/28 = 1.071 (denominator excludes 0 severely-underspecified blocks) within dispositional-domain target [0.8, 2.2] (dispositional ceiling is PROVISIONAL per 4b-2; next dispositional source may re-trigger review)

### `type3_distribution` — FLAG

dispositional_content_underrepresented: Type 3 items = 5/30 = 16.7% < expected ≥20% for dispositional domain (informational only)

### `no_compound_unsplit` — PASS

every KUD item carries a single knowledge type with consistent column and route

## Stage: source-native progression structure

- source type: `circle_solutions_sel`
- band count: **4**
- band labels: Year 2, Year 6, Year 9, Year 12
- age range hint: ages 7-18 (Cowie & Myers 2016; Year 2 through Year 12; sparse 4-checkpoint structure — Years 3-5, 7-8, 10-11 not explicitly covered)
- detection confidence: `high`
- detection rationale: Source slug 'strand-year-2' / reference 'cowie-myers-2016-circle-solutions-student-wellbeing' matches Circle Solutions SEL pattern (Cowie & Myers, 2016). 4-checkpoint structure: Year 2, 6, 9, 12.

## Stage: competency clustering

- clusters: **12**
- overall stability flag: `stable`
- per-cluster stability:
  - `cluster_01` (Self-Awareness): stable — 3 items, dkt=Type 1
  - `cluster_02` (Emotional Knowledge): stable — 2 items, dkt=Type 2
  - `cluster_03` (Emotional Regulation and Expression): stable — 3 items, dkt=Type 2
  - `cluster_04` (Shared Humanity and Belonging): stable — 2 items, dkt=Type 2
  - `cluster_05` (Interpersonal Skills): stable — 3 items, dkt=Type 2
  - `cluster_06` (Empathy and Social Awareness): stable — 2 items, dkt=Type 2
  - `cluster_07` (Leadership and Personal Confidence): stable — 3 items, dkt=Type 3
  - `cluster_08` (Promoting Positive Interactions): stable — 2 items, dkt=Type 2
  - `cluster_09` (Conflict Resolution and Assertiveness): stable — 3 items, dkt=Type 2
  - `cluster_10` (Repair and Restoration): stable — 2 items, dkt=Type 2
  - `cluster_11` (Ethics and Human Rights): stable — 2 items, dkt=Type 1
  - `cluster_12` (Meaning and Spirituality): stable — 3 items, dkt=Type 2

## Stage: LT generation

- LTs: **26** (halted clusters: 0)
- knowledge-type split: Type 1=5, Type 2=16, Type 3=5
- LT stability: {'stable': 24, 'lt_set_unstable': 2}

## Stage: Type 1/2 band statements

- band sets: **11** (halted LTs: 10)
- stability: {'stable': 9, 'band_statements_unstable': 2}
- halted:
  - `cluster_01_lt_02`: band_statements_gate_failed — 2 format/quality failures
  - `cluster_02_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_02_lt_02`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_03_lt_02`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_04_lt_02`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_05_lt_01`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium'))]
  - `cluster_09_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_10_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_10_lt_02`: band_statements_gate_failed — 4 format/quality failures
  - `cluster_12_lt_02`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'long'), ('Year 12', 'medium'))]

## Stage: Type 3 observation indicators

- indicator sets: **5** (halted LTs: 0)
- stability: {'observation_indicators_unstable': 3, 'stable': 2}


## Flags
Total flags: **14**


### `cluster_09_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_09_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_01_lt_02` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_02_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_02_lt_02` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_03_lt_02` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_04_lt_02` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_05_lt_01` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_09_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_10_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_10_lt_02` — `band_statements_unreliable — 4 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_12_lt_02` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'long'), ('Year 12', 'medium'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_11_lt_01` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_12_lt_01` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

