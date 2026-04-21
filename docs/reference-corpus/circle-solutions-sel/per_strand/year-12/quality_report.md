# KUD quality report — strand-year-12

**Overall:** PASSED

## Summary

- **source_domain:** dispositional
- **inventory_blocks_total:** 41
- **inventory_non_heading_blocks:** 28
- **kud_items_total:** 31
- **halted_blocks_total:** 0
- **halted_severe:** 0
- **halted_unreliable:** 0
- **knowledge_type_distribution:** Type 1=6, Type 2=23, Type 3=2
- **kud_column_distribution:** do_disposition=2, do_skill=23, know=5, understand=1
- **stability_distribution:** stable=31
- **underspecification_distribution:** null=31

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — PASS

KUD items / expected-yield blocks = 31/28 = 1.107 (denominator excludes 0 severely-underspecified blocks) within dispositional-domain target [0.8, 2.2] (dispositional ceiling is PROVISIONAL per 4b-2; next dispositional source may re-trigger review)

### `type3_distribution` — FLAG

dispositional_content_underrepresented: Type 3 items = 2/31 = 6.5% < expected ≥20% for dispositional domain (informational only)

### `no_compound_unsplit` — PASS

every KUD item carries a single knowledge type with consistent column and route

## Stage: source-native progression structure

- source type: `circle_solutions_sel`
- band count: **4**
- band labels: Year 2, Year 6, Year 9, Year 12
- age range hint: ages 7-18 (Cowie & Myers 2016; Year 2 through Year 12; sparse 4-checkpoint structure — Years 3-5, 7-8, 10-11 not explicitly covered)
- detection confidence: `high`
- detection rationale: Source slug 'strand-year-12' / reference 'cowie-myers-2016-circle-solutions-student-wellbeing' matches Circle Solutions SEL pattern (Cowie & Myers, 2016). 4-checkpoint structure: Year 2, 6, 9, 12.

## Stage: competency clustering

- clusters: **12**
- overall stability flag: `stable`
- per-cluster stability:
  - `cluster_01` (Self-Awareness and Personal Identity): stable — 4 items, dkt=Type 2
  - `cluster_02` (Emotional Knowledge and Understanding): stable — 3 items, dkt=Type 1
  - `cluster_03` (Emotional Regulation and Resilience Skills): stable — 3 items, dkt=Type 2
  - `cluster_04` (Shared Humanity and Social Awareness): stable — 2 items, dkt=Type 2
  - `cluster_05` (Interpersonal and Collaborative Skills): stable — 4 items, dkt=Type 2
  - `cluster_06` (Empathy and Perspective-Taking): stable — 2 items, dkt=Type 2
  - `cluster_07` (Leadership and Personal Goal Setting): stable — 3 items, dkt=Type 2
  - `cluster_08` (Positive Thinking and Solution Focus): stable — 2 items, dkt=Type 2
  - `cluster_09` (Conflict Resolution and Negotiation): stable — 2 items, dkt=Type 2
  - `cluster_10` (Social Justice and Restoration): stable — 2 items, dkt=Type 2
  - `cluster_11` (Ethics and Human Rights Advocacy): stable — 2 items, dkt=Type 2
  - `cluster_12` (Personal Meaning and Life Purpose): stable — 2 items, dkt=Type 2

## Stage: LT generation

- LTs: **24** (halted clusters: 1)
- knowledge-type split: Type 1=4, Type 2=19, Type 3=1
- LT stability: {'stable': 24}
- halted clusters:
  - `cluster_01`: lt_set_unreliable — no signature reached 2/3 agreement; signatures=[(2, ('Type 2', 'Type 3')), (3, ('Type 2', 'Type 2', 'Type 3')), (3, ('Type 1', 'Type 2', 'Type 3'))]

## Stage: Type 1/2 band statements

- band sets: **11** (halted LTs: 12)
- stability: {'stable': 10, 'band_statements_unstable': 1}
- halted:
  - `cluster_03_lt_01`: band_statements_gate_failed — 2 format/quality failures
  - `cluster_04_lt_02`: band_statements_gate_failed — 2 format/quality failures
  - `cluster_05_lt_02`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_06_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_07_lt_02`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'short'), ('Year 12', 'medium')), (('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'short'), ('Year 6', 'short'), ('Year 9', 'short'), ('Year 12', 'medium'))]
  - `cluster_07_lt_03`: band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'long'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long'))]
  - `cluster_08_lt_02`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_09_lt_02`: band_statements_gate_failed — 4 format/quality failures
  - `cluster_11_lt_01`: band_statements_gate_failed — 2 format/quality failures
  - `cluster_11_lt_02`: band_statements_gate_failed — 2 format/quality failures
  - `cluster_12_lt_01`: band_statements_gate_failed — 1 format/quality failures
  - `cluster_12_lt_02`: band_statements_gate_failed — 2 format/quality failures

## Stage: Type 3 observation indicators

- indicator sets: **1** (halted LTs: 0)
- stability: {'stable': 1}


## Flags
Total flags: **14**


### `cluster_01` — `lt_set_unreliable — no signature reached 2/3 agreement; signatures=[(2, ('Type 2', 'Type 3')), (3, ('Type 2', 'Type 2', 'Type 3')), (3, ('Type 1', 'Type 2', 'Type 3'))]` — **MEDIUM**

**Stage:** LT generation

**Technical:** The LT generator ran 3 times on this cluster; fewer than 2/3 runs produced parseable LT output with a consistent count and knowledge-type distribution. No LTs were produced for this cluster.

**Pedagogical:** The source content in this competency cluster did not produce stable learning targets. The content may be too loosely specified, or the cluster may contain content from multiple distinct competencies. A teacher should review the cluster's KUD items and consider manual LT authoring.

### `cluster_03_lt_01` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_04_lt_02` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_05_lt_02` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_06_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_07_lt_02` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'short'), ('Year 12', 'medium')), (('Year 2', 'short'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'short'), ('Year 6', 'short'), ('Year 9', 'short'), ('Year 12', 'medium'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_07_lt_03` — `band_statements_unreliable — no word-count-class signature reached 2/3 agreement; signatures=[(('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'medium')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'long'), ('Year 12', 'long')), (('Year 2', 'medium'), ('Year 6', 'medium'), ('Year 9', 'medium'), ('Year 12', 'long'))]` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_08_lt_02` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_09_lt_02` — `band_statements_unreliable — 4 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_11_lt_01` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_11_lt_02` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_12_lt_01` — `band_statements_unreliable — 1 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_12_lt_02` — `band_statements_unreliable — 2 format/quality failures` — **MEDIUM**

**Stage:** band statements

**Technical:** The band statement generator ran 3 times; fewer than 2/3 runs produced parseable output with a consistent signature. No band statements were produced for this LT.

**Pedagogical:** Without band statements, teachers cannot use this LT to assess learners across the source's progression bands. The content may need manual authoring of band-level descriptors.

### `cluster_03_lt_02` — `band_statements_unstable` — **MEDIUM**

**Stage:** band statements

**Technical:** Band statement generation reached 2/3 agreement but not 3/3 stability. The majority-vote statements were retained.

**Pedagogical:** The band-level statements may be rephrased differently in alternative valid runs. The substance is stable but specific wording should be reviewed by a teacher before use.

