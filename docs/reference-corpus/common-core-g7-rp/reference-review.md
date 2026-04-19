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
- Criterion rubrics (Type 1/2): **7** (gate pass=6; halted=1)
  - stability: {'rubric_unstable': 3, 'stable': 4}
- Supporting components (Type 1/2): **4** (halted=2)
- Halted at any stage: 13
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

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated independently at the LT's level of demand, with no hedging language or framing of incompleteness.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to test ratios or analyze graphs. |
| emerging | With support, tests some ratios or describes graph features but reaches inaccurate conclusions. |
| developing | Independently tests equivalent ratios or analyzes graphs but inconsistently determines proportionality. |
| competent | Independently identifies proportional relationships by testing equivalent ratios or analyzing graphs accurately. |
| extending | Identifies proportional relationships and explains why non-proportional relationships fail the test. |

_Prerequisite edges:_
- `cluster_01_lt_01` [ontological_prerequisite/high] — Computing unit rates is essential to testing equivalent ratios, the primary method for recognizing proportionality.
- `cluster_01_lt_02` [pedagogical_sequencing/medium] — Understanding unit rate concepts supports reasoning about proportional relationships but is not strictly required to test ratios.

**Supporting components** — stability `stable`.

_Co-construction plan:_
- stage: Show students a simple ratio table and ask them to predict what makes a relationship proportional.
- stage: Guide students to test whether ratios are equivalent by calculating unit rates or cross-multiplying.
- stage: Have students examine a graph and identify what they notice about points that show proportional versus non-proportional relationships.
- stage: Ask students to articulate the difference between testing ratios and analyzing graphs as two valid methods.
- stage: Collaboratively build the rubric levels by sorting student work samples from weakest to strongest.
- prompt: What do you notice about the ratios when a relationship is proportional?
- prompt: How can you check if two ratios are equivalent without a calculator?
- prompt: What does a proportional relationship look like on a graph compared to one that is not proportional?
- prompt: When you test ratios or look at a graph, what tells you that a relationship is NOT proportional?
- anchor-examples guidance: Select work samples that show clear differences: one where a student tests ratios correctly and concludes proportionality accurately, one where a student attempts to test ratios but makes a calculation error, and one where a student correctly analyzes a graph. Avoid examples with multiple errors or ambiguous reasoning.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to test ratios or analyze a graph to determine if a relationship is proportional. |
| emerging | I can test some ratios or describe features of a graph with help, but I do not always reach the correct conclusion about whether a relationship is proportional. |
| developing | I can independently test equivalent ratios or analyze a graph, but I am not consistent in determining whether a relationship is proportional. |
| competent | I can independently identify whether two quantities are in a proportional relationship by accurately testing equivalent ratios or analyzing a graph. |
| extending | I can identify proportional relationships and explain why a relationship fails the proportionality test. |

- self-check: Did I test the ratios by finding unit rates or cross-multiplying, or did I analyze the graph to check if it passes through the origin and is a straight line?
- self-check: Is my conclusion about proportionality correct based on my method, and can I explain why the relationship is or is not proportional?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to pick one ratio pair from the table and show you how to check if they are equivalent.
  - Point to a graph and ask: does this line go through the origin, and does every point fit the same pattern?
- **emerging**
  - Review the calculation step-by-step and ask the student to check their arithmetic or unit rate.
  - Ask: if this ratio works, does the next ratio also work the same way, or is something different?
- **developing**
  - Have the student test one more ratio pair or analyze a different part of the graph to build consistency.
  - Ask the student to state their conclusion in a complete sentence and then verify it matches their test results.
- **competent**
  - Ask the student to explain what would happen to the graph or ratios if the relationship were NOT proportional.
  - Invite the student to test a relationship that is close to proportional but not quite, and explain the difference.

##### Representing Proportional Relationships — `cluster_02_lt_02`

**Definition.** I can represent proportional relationships using multiple mathematical forms including tables, graphs, equations, and other representations.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**Prerequisites:** `Recognizing Proportional Relationships`

**KUD items covered:** `blk_0002_item_02`, `blk_0007_item_03`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Grade 7 | I can represent proportional relationships using tables, graphs, and equations. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated independently at the LT's level of demand, using no hedging language and standing alone as a verdict that the LT is met.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to represent proportional relationships. |
| emerging | With support, represents proportional relationships in one form with errors or gaps. |
| developing | Independently represents proportional relationships in two forms but inconsistencies appear across representations. |
| competent | Independently represents proportional relationships accurately using tables, graphs, equations, and other forms. |
| extending | Translates fluidly between multiple representations and justifies equivalence across different forms. |

_Prerequisite edges:_
- `cluster_02_lt_01` [ontological_prerequisite/high] — Cannot represent a proportional relationship without first identifying whether one exists.
- `cluster_03_lt_01` [pedagogical_sequencing/medium] — Identifying the constant of proportionality supports accurate representation in equations and graphs.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a simple proportional relationship and ask them to name all the different ways they could show it.
- stage: Guide students to sort their ideas into categories: numbers in a table, a picture or graph, a rule or equation, and other ways.
- stage: Work together to describe what makes each representation correct or incomplete, building criteria for each form.
- stage: Agree on what it means to show the same relationship in multiple ways and what mistakes might happen.
- prompt: If I tell you that every 2 apples costs 3 dollars, how many different ways can you write or draw this?
- prompt: Which of these representations shows the same relationship, and which ones have mistakes?
- prompt: What would someone need to see in a table, graph, and equation to know they are all showing the same proportional relationship?
- prompt: When you move from a table to a graph to an equation, what stays the same and what changes?
- anchor-examples guidance: Choose examples that show a proportional relationship represented correctly in at least two forms and one example with an error in one representation so students can identify what breaks the connection between forms. Include a simple ratio like 2:3 or 1:4 that students can verify across all representations.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to show a proportional relationship in any form. |
| emerging | I can show a proportional relationship in one form with help, but my work has mistakes or missing parts. |
| developing | I can show a proportional relationship in two different forms on my own, but the forms do not match perfectly. |
| competent | I can accurately show a proportional relationship using tables, graphs, equations, and other forms that all match. |
| extending | I can move smoothly between different representations and explain why they show the same proportional relationship. |

- self-check: Can I show this relationship in at least two different ways, and do they tell the same story?
- self-check: If I check one point from my table in my graph and equation, do all three agree?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to pick one form they feel most comfortable with and start there.
  - Provide a partially completed table or graph and ask the student to finish it and describe what they see.
- **emerging**
  - Have the student check one point from their representation against the original relationship to find where the error is.
  - Guide them to create a second representation by asking what the same relationship would look like in a different form.
- **developing**
  - Ask the student to pick a point and trace it through both representations to find where they do not match.
  - Encourage them to create a third representation and check if all three forms agree on the same points.
- **competent**
  - Ask the student to explain how they know their table, graph, and equation are all showing the same relationship.
  - Challenge them to create a fourth representation or to predict what would happen if the constant of proportionality changed.

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

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated independently and accurately across all required contexts, standing alone as evidence the LT is met without hedging or incompleteness language.

_Propositional-thin flag:_ this is a factual Type 1 LT; the rubric is necessarily compressed.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify the constant of proportionality. |
| emerging | With support, identifies the constant in one representation but inconsistently or with errors. |
| developing | Independently identifies the constant in familiar representations but struggles across multiple forms. |
| competent | Identifies the constant of proportionality accurately across tables, graphs, equations, diagrams, and verbal descriptions. |
| extending | Identifies the constant and explains how it remains invariant across different representations of the same relationship. |

_Prerequisite edges:_
- `cluster_01_lt_01` [ontological_prerequisite/high] — Computing unit rates is the foundational skill; the constant of proportionality is the unit rate in a proportional relationship.
- `cluster_02_lt_01` [ontological_prerequisite/high] — Recognizing proportional relationships must precede identifying the constant within them; you cannot extract the constant from a non-proportional relationship.
- `cluster_02_lt_02` [pedagogical_sequencing/medium] — Representing proportional relationships across multiple forms provides the contexts in which the constant is identified; familiarity with representations aids extraction.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a simple proportional relationship in one representation and ask them what stays the same no matter how the numbers change.
- stage: Guide students to discover the constant by comparing pairs of values across two or three different representations of the same relationship.
- stage: Have students name what they found and decide what it means to identify the constant correctly versus incorrectly.
- stage: Work together to describe what identifying the constant looks like across all five forms: tables, graphs, equations, diagrams, and words.
- stage: Sort anchor examples by level and discuss why some show the constant clearly while others show confusion or missing work.
- prompt: What number or ratio stays the same when we look at different points in this relationship?
- prompt: How can you find that same constant in a table, a graph, and an equation?
- prompt: What would it look like if someone found the constant in only one representation but not in others?
- prompt: How would you explain to a friend what the constant of proportionality is and why it matters?
- anchor-examples guidance: Choose examples that show the constant of proportionality in at least two different representations so students can see consistency, and include one example where a student confuses the constant with another number in the problem. Select a mix where the constant is a whole number and a fraction to show variety.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to identify the constant of proportionality. |
| emerging | I can identify the constant of proportionality in one representation with help, but I make mistakes or am not sure when I try on my own. |
| developing | I can identify the constant of proportionality on my own in tables and graphs, but I struggle when it is shown as an equation, diagram, or words. |
| competent | I can identify the constant of proportionality correctly in tables, graphs, equations, diagrams, and verbal descriptions. |
| extending | I can identify the constant of proportionality and explain why it stays the same across all different representations of the same relationship. |

- self-check: Can I find the constant in at least three different forms: a table, a graph, and an equation or words?
- self-check: Does the constant I found make sense when I check it with another pair of values in the relationship?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to pick any two related values from a table and find the ratio between them.
  - Model finding the constant in one representation aloud, then ask the student to try the same process with a different table.
- **emerging**
  - Have the student identify the constant in a familiar representation, then guide them to find the same constant in a second representation by asking what should stay the same.
  - Ask the student to check their constant by testing it with a different pair of values to build confidence and reduce errors.
- **developing**
  - Provide the constant and ask the student to verify it appears in an unfamiliar representation like an equation or diagram.
  - Scaffold the student through one example of finding the constant in a new form, then release responsibility for the next example.
- **competent**
  - Ask the student to identify the constant in two representations and explain why both show the same value.
  - Challenge the student to predict what the constant would be in a new representation before finding it, then verify.

##### Using the Constant in Proportional Equations — `cluster_03_lt_02`

**Definition.** I can use the constant of proportionality to write and interpret equations and ordered pairs in proportional relationships.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `lt_set_unstable`.

**Prerequisites:** `Identifying the Constant of Proportionality`

**KUD items covered:** `blk_0013_item_01`, `blk_0014_item_01`, `blk_0016_item_01`, `blk_0016_item_02`, `blk_0016_item_03`

**Single-grade band** — stability `band_statements_unstable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Grade 7 | I can use the constant of proportionality to write equations representing proportional relationships. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares independent capability to use the constant of proportionality to write equations and interpret ordered pairs accurately, which directly matches the LT's demand and stands alone as success.

_Propositional-thin flag:_ this is a factual Type 1 LT; the rubric is necessarily compressed.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to use the constant of proportionality. |
| emerging | With support, uses the constant to write or interpret one equation or ordered pair incompletely. |
| developing | Independently uses the constant to write equations or interpret ordered pairs in familiar proportional relationships. |
| competent | Independently uses the constant of proportionality to write equations and interpret ordered pairs in proportional relationships accurately. |
| extending | Uses the constant to write equations and interpret ordered pairs across multiple representations and unfamiliar contexts. |

_Prerequisite edges:_
- `cluster_03_lt_01` [ontological_prerequisite/high] — Cannot use the constant in equations without first identifying what it is across representations.
- `cluster_02_lt_01` [ontological_prerequisite/high] — Must recognize proportional relationships exist before using their constant in equations.
- `cluster_01_lt_01` [pedagogical_sequencing/high] — Computing unit rates builds the numerical foundation for understanding and applying the constant of proportionality.

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

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares independent application of proportional relationships to multistep problems with accurate reasoning, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to apply proportional relationships to a problem. |
| emerging | With support, identifies a proportional relationship but applies it incompletely or inaccurately. |
| developing | Applies proportional relationships to solve a problem independently but misses a step or reasoning gap. |
| competent | Independently applies proportional relationships to solve multistep real-world problems with accurate reasoning. |
| extending | Applies proportional relationships to novel or complex contexts and justifies solution strategy choices. |

_Prerequisite edges:_
- `cluster_01_lt_01` [ontological_prerequisite/high] — Computing unit rates is foundational to recognizing and applying proportional relationships in real-world contexts.
- `cluster_02_lt_01` [ontological_prerequisite/high] — Identifying proportional relationships is a prerequisite to applying them; cannot apply what is not recognized.
- `cluster_03_lt_02` [ontological_prerequisite/high] — Using the constant of proportionality in equations is essential to solving multistep proportional problems.
- `cluster_04_lt_01` [pedagogical_sequencing/medium] — Solving multistep ratio and percent problems builds reasoning skills that support application to broader proportional contexts.

**Supporting components** — stability `stable`.

_Co-construction plan:_
- stage: Show students a real-world scenario involving proportions and ask them to identify what stays the same and what changes.
- stage: Guide students to distinguish between incomplete attempts and accurate applications by examining sample work together.
- stage: Have students articulate what makes a solution multistep and what reasoning must be shown.
- stage: Discuss how applying proportions to unfamiliar or complex situations differs from routine problems.
- prompt: What quantities in this problem are connected proportionally, and how do you know?
- prompt: What would it look like if someone tried to use a proportion but made a mistake or stopped too early?
- prompt: What steps do you need to take to fully solve a problem with proportions, and why is each step necessary?
- prompt: How would you explain your choice of strategy if the problem were more complex or used a context you'd never seen before?
- anchor-examples guidance: Select anchor examples that show the progression from a single incomplete proportion application to a multistep solution with clear reasoning, and include one example where a student adapts their strategy to an unfamiliar context. Ensure examples reflect realistic student work rather than polished solutions.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to use proportional relationships to solve a problem. |
| emerging | I can identify a proportional relationship with help, but I apply it incompletely or make errors in my solution. |
| developing | I can apply proportional relationships to solve a problem on my own, but I may skip a step or leave out some of my reasoning. |
| competent | I can independently apply proportional relationships to solve multistep real-world problems and show all my reasoning clearly. |
| extending | I can apply proportional relationships to new or complex situations and explain why I chose my solution strategy. |

- self-check: Did I identify which quantities are proportional and set up the relationship correctly?
- self-check: Did I complete all the steps needed to solve the problem and explain my reasoning at each step?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to point out two quantities in the problem that might be related and describe how they change together.
  - Model identifying a proportional relationship aloud, then ask the student to try the same thinking on a similar problem.
- **emerging**
  - Have the student check their proportion setup by testing it with a simple value and asking if the relationship makes sense.
  - Guide the student to complete one more step by asking what information they still need to find to answer the full question.
- **developing**
  - Ask the student to trace through their work and identify which step answers which part of the question.
  - Prompt the student to add a sentence explaining why they chose their strategy or how they knew their answer was reasonable.
- **competent**
  - Present a proportional problem with an unfamiliar context and ask the student to explain how their strategy would change.
  - Challenge the student to solve the same problem using a different method and compare the efficiency of both approaches.

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

### Criterion-rubric stage halted LTs

- `cluster_01_lt_02` (Understanding Unit Rate Concepts) — rubric_unreliable: only 1/3 runs produced parseable output

### Supporting-components stage halted LTs

- `cluster_01_lt_01` (Computing Unit Rates from Ratios) — supporting_unreliable: no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
- `cluster_03_lt_02` (Using the Constant in Proportional Equations) — supporting_unreliable: no structural signature reached 2/3 agreement; signatures=[(('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]

