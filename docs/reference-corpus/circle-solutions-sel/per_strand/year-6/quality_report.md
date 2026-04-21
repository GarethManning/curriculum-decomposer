# KUD quality report — strand-year-6

**Overall:** PASSED

## Summary

- **source_domain:** dispositional
- **inventory_blocks_total:** 41
- **inventory_non_heading_blocks:** 28
- **kud_items_total:** 31
- **halted_blocks_total:** 0
- **halted_severe:** 0
- **halted_unreliable:** 0
- **knowledge_type_distribution:** Type 1=7, Type 2=16, Type 3=8
- **kud_column_distribution:** do_disposition=8, do_skill=16, know=5, understand=2
- **stability_distribution:** classification_unstable=2, stable=29
- **underspecification_distribution:** null=31

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — PASS

KUD items / expected-yield blocks = 31/28 = 1.107 (denominator excludes 0 severely-underspecified blocks) within dispositional-domain target [0.8, 2.2] (dispositional ceiling is PROVISIONAL per 4b-2; next dispositional source may re-trigger review)

### `type3_distribution` — PASS

Type 3 items = 8/31 = 25.8% (≥20% expected for dispositional domain)

### `no_compound_unsplit` — PASS

every KUD item carries a single knowledge type with consistent column and route

## Stage: source-native progression structure

- source type: `circle_solutions_sel`
- band count: **4**
- band labels: Year 2, Year 6, Year 9, Year 12
- age range hint: ages 7-18 (Cowie & Myers 2016; Year 2 through Year 12; sparse 4-checkpoint structure — Years 3-5, 7-8, 10-11 not explicitly covered)
- detection confidence: `high`
- detection rationale: Source slug 'strand-year-6' / reference 'cowie-myers-2016-circle-solutions-student-wellbeing' matches Circle Solutions SEL pattern (Cowie & Myers, 2016). 4-checkpoint structure: Year 2, 6, 9, 12.

## Stage: competency clustering

- clusters: **12**
- overall stability flag: `stable`
- per-cluster stability:
  - `cluster_01` (Self-Awareness): stable — 3 items, dkt=Type 2
  - `cluster_02` (Emotional Knowledge): stable — 3 items, dkt=Type 2
  - `cluster_03` (Emotional Skills): stable — 3 items, dkt=Type 2
  - `cluster_04` (Shared Humanity): stable — 3 items, dkt=Type 1
  - `cluster_05` (Interpersonal Skills): stable — 3 items, dkt=Type 3
  - `cluster_06` (Empathy and Awareness of Others): stable — 2 items, dkt=Type 2
  - `cluster_07` (Leadership and Personal Growth): stable — 4 items, dkt=Type 3
  - `cluster_08` (Positive Thinking and Gratitude): stable — 2 items, dkt=Type 2
  - `cluster_09` (Conflict Management): stable — 2 items, dkt=Type 2
  - `cluster_10` (Repair and Restoration): stable — 2 items, dkt=Type 1
  - `cluster_11` (Ethics and Human Rights): stable — 2 items, dkt=Type 2
  - `cluster_12` (Meaning and Spirituality): stable — 2 items, dkt=Type 2

## Stage: LT generation

- LTs: **27** (halted clusters: 0)
- knowledge-type split: Type 1=4, Type 2=16, Type 3=7
- LT stability: {'stable': 25, 'lt_set_unstable': 2}

## Stage: Type 1/2 band statements

- band sets: **16** (halted LTs: 4)
- stability: {'stable': 13, 'band_statements_unstable': 3}
- halted:
  - `cluster_01_lt_02`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_04_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_07_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_09_lt_01`: band_statements_gate_failed — 1 format/quality failures

## Stage: Type 3 observation indicators

- indicator sets: **7** (halted LTs: 0)
- stability: {'observation_indicators_unstable': 2, 'stable': 5}


## Flags
Total flags: **9**


### `cluster_02_lt_01` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_02_lt_02` — `lt_set_unstable` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator reached 2/3 agreement on a majority signature, but not 3/3 stability. The LT set was retained using the majority result.

**Pedagogical:** The learning targets in this set are the most consistent description produced, but alternative valid descriptions exist. A teacher reviewing these LTs should be aware that the boundaries between LTs may have shifted in different runs.

### `cluster_01_lt_02` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_04_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_07_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_09_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_01_lt_03` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_03_lt_01` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

### `cluster_04_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

