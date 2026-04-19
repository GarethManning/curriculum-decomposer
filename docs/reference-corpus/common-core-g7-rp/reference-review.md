# Reference review — 2a-regression-common-core-7rp

Source snapshot: `docs/run-snapshots/2026-04-18-session-4a-2a-regression-common-core-7rp`. Classifier: `claude-haiku-4-5-20251001` at temperature 0.3 with 3x self-consistency.

## Progression structure (source-native)

- **source type:** `us_common_core_grade`
- **band count:** 1
- **band:** Grade 7 (single-grade source — no progression sequence inside the source)
- **age range hint:** ages 12-13 (Common Core State Standards Initiative; CCSSO grade alignment)
- **detection confidence:** `high`
- **detection rationale:** Common Core source detected (host=thecorestandards.org, slug=2a-regression-common-core-7rp); grade 7 extracted. Single-grade source — band_count=1.

**Progression philosophy.**

> Grade-level standards published at grade-level granularity only. Each standard is expected to be mastered by the end of the named grade. Sub-grade progression (quarterly, monthly) is a pedagogical decision made by districts and schools, not by the standards themselves. The presence of a single band in this reference output reflects the source's own granularity, not an absence of internal structure within the teaching year.

### Per-band developmental index

| Band | Approximate age | Approximate grade/year | Developmental descriptor |
|---|---|---|---|
| Grade 7 | ages 12-13 | Grade 7 | Grade 7 learners extend proportional reasoning from Grades 5-6 to analyse proportional relationships using equations, tables, and graphs, and apply them to multi-step ratio and percent problems. This domain is foundational for linear algebra and functional thinking in Grade 8. |

## Summary

- KUD items: **22**
- Halted KUD blocks: **8**
- Competency clusters: **4**
  - overall stability: `cluster_unstable`
- Learning Targets: **8**
  - knowledge types: Type 1=6, Type 2=2, Type 3=0
  - stability: {'stable': 4, 'lt_set_unstable': 4}
- Band-statement sets (Type 1/2): **6**
  - stability: {'stable': 5, 'band_statements_unstable': 1}
- Observation indicator sets (Type 3): **0**
  - stability: {}
- Halted at any stage: 10
- Pipeline: all KUD halting gates passed

## Competencies

### Computing Unit Rates — `cluster_01`

**Definition.** The ability to compute unit rates from ratios of quantities, including fractions and different units.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L7-8. **KUD items:** 4.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0004_item_01` | Type 1 | know | Unit rates associated with ratios of fractions |
| `blk_0004_item_02` | Type 1 | do_skill | Compute unit rates associated with ratios of fractions, including ratios of lengths, areas and other quantities measured in like or different units |
| `blk_0005_item_01` | Type 1 | know | A unit rate is computed by dividing a quantity by a time interval, expressed as a complex fraction and simplified to a single-unit denominator. |
| `blk_0005_item_02` | Type 1 | do_skill | Compute a unit rate by expressing a quantity and time interval as a complex fraction and simplifying to a rate per single unit of time. |

#### Learning Targets

##### Computing Unit Rates from Ratios — `cluster_01_lt_01`

**Definition.** I can compute unit rates from ratios of quantities, including fractions and different units.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0004_item_02`, `blk_0005_item_02`

_No band statements produced._

##### Understanding Unit Rate Concepts — `cluster_01_lt_02`

**Definition.** I can explain what a unit rate is and how it relates to ratios of quantities.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0004_item_01`, `blk_0005_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Grade 7 | I can explain how a unit rate describes the relationship between two quantities in a ratio. |

### Recognizing and Representing Proportional Relationships — `cluster_02`

**Definition.** The ability to recognize, represent, and analyze proportional relationships between quantities using multiple representations.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L5-17. **KUD items:** 8.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0002_item_01` | Type 1 | understand | Proportional relationships and their properties. |
| `blk_0002_item_02` | Type 1 | do_skill | Analyze proportional relationships to identify their characteristics and structure. |
| `blk_0007_item_01` | Type 1 | understand | Proportional relationships between quantities and how they are structured. |
| `blk_0007_item_02` | Type 1 | do_skill | Recognize proportional relationships between quantities in given contexts or data. |
| `blk_0007_item_03` | Type 1 | do_skill | Represent proportional relationships between quantities using tables, graphs, equations, or other mathematical forms. |
| `blk_0009_item_01` | Type 1 | understand | Proportional relationships: two quantities are in a proportional relationship when their ratios are equivalent. |
| `blk_0009_item_02` | Type 1 | do_skill | Test for equivalent ratios in a table to decide whether two quantities are in a proportional relationship. |
| `blk_0009_item_03` | Type 1 | do_skill | Graph two quantities on a coordinate plane and observe whether the graph is a straight line through the origin to decide whether they are in a proportional relationship. |

#### Learning Targets

##### Recognizing Proportional Relationships — `cluster_02_lt_01`

**Definition.** I can identify whether two quantities are in a proportional relationship by testing equivalent ratios or analyzing graphical representations.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0002_item_01`, `blk_0007_item_01`, `blk_0007_item_02`, `blk_0009_item_01`, `blk_0009_item_02`, `blk_0009_item_03`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Grade 7 | I can identify proportional relationships by testing equivalent ratios or analyzing graphs. |

##### Representing Proportional Relationships — `cluster_02_lt_02`

**Definition.** I can represent proportional relationships using multiple mathematical forms including tables, graphs, equations, and other representations.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**Prerequisites:** `Recognizing Proportional Relationships`

**KUD items covered:** `blk_0002_item_02`, `blk_0007_item_03`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Grade 7 | I can represent proportional relationships using tables, graphs, and equations. |

### Identifying and Using the Constant of Proportionality — `cluster_03`

**Definition.** The ability to identify the constant of proportionality across representations and use it to express proportional relationships.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L19-25. **KUD items:** 7.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0011_item_01` | Type 1 | know | The constant of proportionality (unit rate) is the constant ratio between two proportional quantities. |
| `blk_0011_item_02` | Type 1 | do_skill | Identify the constant of proportionality (unit rate) in tables, graphs, equations, diagrams, and verbal descriptions of proportional relationships. |
| `blk_0013_item_01` | Type 1 | do_skill | Represent proportional relationships by equations. |
| `blk_0014_item_01` | Type 1 | know | The relationship between total cost, number of items, and constant price can be expressed as t = pn, where t is total cost, p is the constant price per item, and n is the number of items purchased. |
| `blk_0016_item_01` | Type 1 | understand | What a point (x, y) on the graph of a proportional relationship means in terms of the situation |
| `blk_0016_item_02` | Type 1 | understand | The meaning of the point (0, 0) on the graph of a proportional relationship in terms of the situation |
| `blk_0016_item_03` | Type 1 | understand | The meaning of the point (1, r) where r is the unit rate on the graph of a proportional relationship in terms of the situation |

#### Learning Targets

##### Identifying the Constant of Proportionality — `cluster_03_lt_01`

**Definition.** I can identify the constant of proportionality across tables, graphs, equations, diagrams, and verbal descriptions.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `lt_set_unstable`.

**KUD items covered:** `blk_0011_item_01`, `blk_0011_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Grade 7 | I can identify the constant of proportionality from tables, graphs, equations, and verbal descriptions. |

##### Using the Constant in Proportional Equations — `cluster_03_lt_02`

**Definition.** I can use the constant of proportionality to write and interpret equations and ordered pairs in proportional relationships.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `lt_set_unstable`.

**Prerequisites:** `Identifying the Constant of Proportionality`

**KUD items covered:** `blk_0013_item_01`, `blk_0014_item_01`, `blk_0016_item_01`, `blk_0016_item_02`, `blk_0016_item_03`

**Single-grade band** — stability `band_statements_unstable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Grade 7 | I can use the constant of proportionality to write equations representing proportional relationships. |

### Solving Real-World Proportional Relationship Problems — `cluster_04`

**Definition.** The ability to apply proportional relationships to solve multistep ratio and percent problems in real-world contexts.

**Dominant knowledge type:** Type 2. **Stability:** `cluster_unstable`. **Source lines:** L5-33. **KUD items:** 3.

_Stability diagnostics:_
- dominant_type_drift_run2: Type 2→Type 1
- dominant_type_drift_run3: Type 2→Type 1

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0002_item_03` | Type 2 | do_skill | Use proportional relationships to solve real-world and mathematical problems. |
| `blk_0018_item_01` | Type 1 | understand | Proportional relationships and their use in solving multistep ratio and percent problems |
| `blk_0018_item_02` | Type 1 | do_skill | Solve multistep ratio and percent problems including simple interest, tax, markups and markdowns, gratuities and commissions, fees, percent increase and decrease, and percent error |

#### Learning Targets

##### Solving Multistep Ratio and Percent Problems — `cluster_04_lt_01`

**Definition.** I can solve multistep ratio and percent problems including simple interest, tax, markups, markdowns, gratuities, commissions, fees, percent increase and decrease, and percent error.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `lt_set_unstable`.

**KUD items covered:** `blk_0018_item_02`, `blk_0002_item_03`

_No band statements produced._

##### Applying Proportional Relationships to Real-World Contexts — `cluster_04_lt_02`

**Definition.** I can apply proportional relationships to solve real-world and mathematical problems involving multiple steps and reasoning.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `lt_set_unstable`.

**KUD items covered:** `blk_0002_item_03`, `blk_0018_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Grade 7 | I can solve multi-step real-world problems by applying proportional relationships and reasoning about the results. |

## Halted items

### KUD halted blocks

- `blk_0001` — severe_underspecification: meta_or_nonteachable
- `blk_0003` — severe_underspecification: meta_or_nonteachable
- `blk_0006` — severe_underspecification: meta_or_nonteachable
- `blk_0008` — severe_underspecification: meta_or_nonteachable
- `blk_0010` — severe_underspecification: meta_or_nonteachable
- `blk_0012` — severe_underspecification: meta_or_nonteachable
- `blk_0015` — severe_underspecification: meta_or_nonteachable
- `blk_0017` — severe_underspecification: meta_or_nonteachable

### Band-statement stage halted LTs

- `cluster_01_lt_01` (Computing Unit Rates from Ratios) — band_statements_gate_failed: 1 format/quality failures
  - failures: ['Grade 7:no_observable_verb']
- `cluster_04_lt_01` (Solving Multistep Ratio and Percent Problems) — band_statements_gate_failed: 1 format/quality failures
  - failures: ['Grade 7:no_observable_verb']

