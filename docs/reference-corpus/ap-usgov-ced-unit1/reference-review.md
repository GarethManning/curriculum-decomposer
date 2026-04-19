# Reference review — 5-ap-usgov-ced-unit1

Source snapshot: `docs/run-snapshots/2026-04-18-session-4a-4-5-ap-usgov-ced-unit1`. Classifier: `claude-haiku-4-5-20251001` at temperature 0.3 with 3x self-consistency.

## Progression structure (source-native)

- **source type:** `us_ap_course_unit`
- **band count:** 1
- **band:** Unit 1 (single-grade source — no progression sequence inside the source)
- **age range hint:** ages 16-18 (College Board AP US Government and Politics; typically Grades 11-12)
- **detection confidence:** `high`
- **detection rationale:** Source slug '5-ap-usgov-ced-unit1' matches AP US Government and Politics pattern; unit 1 extracted. Single-unit source — band_count=1.

**Progression philosophy.**

> AP US Government and Politics is a college-level course, typically taken in Grades 11-12. The Course and Exam Description (CED) organises content into 9 units; this source covers Unit 1 only. Within-unit progression is a teacher and district decision; the CED specifies learning objectives and essential knowledge, not a week-by-week sequence. Single-band output reflects the source's own unit granularity, not an absence of internal structure within the teaching period. Per College Board AP US Government and Politics CED V.1 (2023).

### Per-band developmental index

| Band | Approximate age | Approximate grade/year | Developmental descriptor |
|---|---|---|---|
| Unit 1 | ages 16-18 | Grade 11-12 | AP US Government and Politics learners in Unit 1 establish the constitutional foundations of American democracy: Enlightenment principles, Articles of Confederation limitations, Constitutional Convention compromises, Federalist and Anti-Federalist arguments, and the structure of constitutional government. They apply political science concepts to primary-source analysis and argument construction at a college-preparatory level. |

## Summary

- KUD items: **67**
- Halted KUD blocks: **221**
- Competency clusters: **13**
  - overall stability: `cluster_unstable`
- Learning Targets: **26**
  - knowledge types: Type 1=16, Type 2=10, Type 3=0
  - stability: {'stable': 22, 'lt_set_unstable': 4}
- Band-statement sets (Type 1/2): **26**
  - stability: {'stable': 25, 'band_statements_unstable': 1}
- Observation indicator sets (Type 3): **0**
  - stability: {}
- Criterion rubrics (Type 1/2): **15** (gate pass=10; halted=11)
  - stability: {'rubric_unstable': 10, 'stable': 5}
- Supporting components (Type 1/2): **8** (halted=2)
- Halted at any stage: 235
- Pipeline: all KUD halting gates passed

## Competencies

### Democratic Ideals and Constitutional Foundations — `cluster_01`

**Definition.** The ability to explain how democratic ideals of natural rights, social contract, popular sovereignty, and limited government are reflected in foundational U.S. documents and the Constitution.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L49-298. **KUD items:** 7.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0027_item_01` | Type 1 | understand | Compromises made during the ratification of the U.S. Constitution created ambiguities that continue to fuel debate and discussion over how best to protect liberty, equality, order, and private propert |
| `blk_0125_item_01` | Type 1 | know | the concept of 'state of nature' in the absence of government |
| `blk_0137_item_01` | Type 1 | know | The four principles that ensure the ideal of limited government are separation of powers, checks and balances, federalism, and republicanism. |
| `blk_0137_item_02` | Type 1 | understand | How separation of powers, checks and balances, federalism, and republicanism interact to ensure the ideal of limited government. |
| `blk_0142_item_01` | Type 1 | know | The Philadelphia Convention was led by George Washington with important contributions from Hamilton and members of the Grand Committee. |
| `blk_0142_item_02` | Type 1 | understand | The Philadelphia Convention is an example of a social contract that establishes a system of limited government. |
| `blk_0142_item_03` | Type 1 | understand | The Constitution provides the blueprint for a unique form of democratic government in the United States. |

#### Learning Targets

### Models of Representative Democracy — `cluster_02`

**Definition.** The ability to explain how participatory, pluralist, and elite models of representative democracy are reflected in U.S. institutions and contemporary political behavior.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L334-349. **KUD items:** 3.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0155_item_01` | Type 1 | know | Pluralist democracy emphasizes group-based activism by nongovernmental interests striving for impact on political decision making |
| `blk_0155_item_02` | Type 1 | know | Elite democracy emphasizes limited participation in politics and civil society |
| `blk_0159_item_01` | Type 1 | know | The three models of representative democracy continue to be reflected in contemporary institutions and political behavior. |

#### Learning Targets

##### Distinguishing Models of Representative Democracy — `cluster_02_lt_01`

**Definition.** I can explain the key characteristics of participatory, pluralist, and elite models of representative democracy.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0155_item_01`, `blk_0155_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain the key characteristics that distinguish participatory, pluralist, and elite models of representative democracy. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated independently at the LT's level of demand, with no hedging language or framing of incompleteness.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify or explain the models. |
| emerging | Names one or two models with minimal or inaccurate characteristics. |
| developing | Identifies all three models and describes some characteristics independently but with incomplete or imprecise explanations. |
| competent | Explains key characteristics of participatory, pluralist, and elite models of representative democracy accurately and independently. |
| extending | Compares and contrasts the three models, identifying tensions and assumptions underlying each framework. |

**Supporting components** — stability `stable`.

_Co-construction plan:_
- stage: Show students three unlabeled descriptions of how decisions get made in democracies and ask them to sort and name the patterns they notice.
- stage: Guide students to identify the three model names and list what makes each one distinct from the others.
- stage: Have students generate their own examples of each model in action and test whether those examples fit the characteristics they identified.
- stage: Co-author level descriptors by asking students what 'knowing this well' looks like at each stage of understanding.
- prompt: What are the key differences in how power and participation work across these three descriptions?
- prompt: Which model emphasizes ordinary citizens making decisions, which emphasizes organized groups negotiating, and which emphasizes experts or elites deciding?
- prompt: Can you find a real-world example where one of these models is at work and explain why it fits that model?
- prompt: What would someone need to do or understand to move from naming the models to comparing how they actually work?
- anchor-examples guidance: Choose examples that clearly embody one model without overlap—for instance, a town hall meeting for participatory, a lobbying coalition for pluralist, and a technocratic policy decision for elite. Avoid examples that blur two models together.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to identify or explain the three models of representative democracy. |
| emerging | I can name one or two of the models and describe some characteristics, though my explanations may be incomplete or not quite accurate. |
| developing | I can identify all three models and describe some of their key characteristics on my own, but my explanations are still missing details or are not fully precise. |
| competent | I can explain the key characteristics of participatory, pluralist, and elite models of representative democracy clearly and accurately. |
| extending | I can compare and contrast the three models, identify tensions between them, and explain the underlying assumptions that shape each framework. |

- self-check: Can I name all three models and describe at least two characteristics that make each one different from the others?
- self-check: Can I explain how each model answers the question 'Who really makes decisions in a democracy?'

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to name just one model and describe what role ordinary citizens play in that model.
  - Provide a simple scenario of a decision being made and ask which model it most closely resembles.
- **emerging**
  - Ask the student to name the third model they haven't mentioned yet and describe one way it differs from the first two.
  - Prompt them to explain what 'pluralist' means by asking who the key decision-makers are in that model.
- **developing**
  - Ask the student to add one more specific characteristic to each model that they haven't mentioned yet.
  - Have them test their understanding by applying each model to a new real-world scenario and explaining which model fits best.
- **competent**
  - Ask the student to identify a tension or contradiction between two of the models.
  - Prompt them to explain what each model assumes about human nature or how democracy should work.

##### Applying Democracy Models to U.S. Institutions — `cluster_02_lt_02`

**Definition.** I can identify and explain how participatory, pluralist, and elite models are reflected in contemporary U.S. political institutions and behavior.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**Prerequisites:** `Distinguishing Models of Representative Democracy`

**KUD items covered:** `blk_0159_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain how participatory, pluralist, and elite models describe different aspects of U.S. political institutions. |

### Federalist and Anti-Federalist Perspectives — `cluster_03`

**Definition.** The ability to explain Federalist and Anti-Federalist views on central government and democracy, and how these perspectives shaped constitutional debate.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L382-382. **KUD items:** 1.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0176_item_01` | Type 1 | know | Federalist views on central Constitution and a strong central government |

#### Learning Targets

##### Explaining Federalist Views on Central Government — `cluster_03_lt_01`

**Definition.** I can explain Federalist arguments for a strong central government and its role in the Constitution.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0176_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain Federalist arguments for establishing a strong central government in the Constitution. |

##### Explaining Anti-Federalist Views on Democracy — `cluster_03_lt_02`

**Definition.** I can explain Anti-Federalist concerns about centralized power and their vision of democratic representation.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0176_item_01`

**Single-grade band** — stability `band_statements_unstable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain Anti-Federalist concerns about concentrated federal power and their preference for state and local democratic representation. |

### Weaknesses of the Articles of Confederation — `cluster_04`

**Definition.** The ability to explain how specific incidents and legal challenges revealed key weaknesses of the Articles of Confederation and prompted debate over federal power.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L439-439. **KUD items:** 3.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0201_item_01` | Type 1 | know | Key weaknesses of the Articles of Confederation: lack of centralized military power to address Shays' Rebellion; lack of an executive branch to enforce federal authority. |
| `blk_0201_item_02` | Type 1 | understand | The relationship between specific incidents (such as Shays' Rebellion) and legal challenges, and the key provisions of the Articles of Confederation that proved inadequate to address them. |
| `blk_0201_item_03` | Type 2 | do_skill | Explain the debate over granting greater power to the federal government in light of the weaknesses revealed by specific incidents and legal challenges under the Articles of Confederation. |

#### Learning Targets

##### Identifying Key Weaknesses in the Articles — `cluster_04_lt_01`

**Definition.** I can identify how lack of centralized military power and absence of an executive branch limited the Articles of Confederation.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0201_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify how the absence of centralized military power and executive authority weakened the Articles of Confederation. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **FAIL**.

_Gate failures:_ single_construct

_Competent-framing judge:_ `pass` — The descriptor directly states the learner 'identifies how' the specified limitations affected the Articles, which matches the LT's demand without hedging language or framing Competent as incomplete.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify Articles weaknesses. |
| emerging | Names military or executive absence but with incomplete or inaccurate explanation of impact. |
| developing | Identifies lack of centralized military power and absent executive branch independently but lacks depth on limitations. |
| competent | Identifies how lack of centralized military power and absence of executive branch limited the Articles' effectiveness. |
| extending | Connects identified weaknesses to specific historical incidents or explains cascading effects on federal governance. |

_Prerequisite edges:_
- `cluster_03_lt_01` [pedagogical_sequencing/medium] — Understanding Federalist arguments for strong central government provides context for why Articles weaknesses mattered.
- `cluster_04_lt_02` [pedagogical_sequencing/medium] — Connecting incidents to constitutional gaps builds on identifying weaknesses as foundational knowledge.

##### Connecting Incidents to Constitutional Inadequacies — `cluster_04_lt_02`

**Definition.** I can explain how specific incidents like Shays' Rebellion exposed gaps between the Articles' provisions and the federal government's actual needs.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**Prerequisites:** `Identifying Key Weaknesses in the Articles`

**KUD items covered:** `blk_0201_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain how specific historical incidents revealed weaknesses in the Articles of Confederation's governmental structure. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor directly states the learner 'explains how' the connection works, matching the LT's demand without hedging, incompleteness markers, or positioning it as a waystation to Extending.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to connect incidents to Articles weaknesses. |
| emerging | With support, identifies an incident and names a weakness but does not explain the connection. |
| developing | Independently explains how one incident exposed a specific Articles weakness but lacks depth or precision. |
| competent | Explains how specific incidents like Shays' Rebellion exposed gaps between Articles provisions and federal government needs. |
| extending | Analyzes multiple incidents to construct a comprehensive argument about systemic inadequacies in the Articles. |

_Prerequisite edges:_
- `cluster_04_lt_01` [ontological_prerequisite/high] — Must identify specific weaknesses in the Articles before explaining how incidents exposed those gaps.

##### Reasoning About Federal Power Expansion — `cluster_04_lt_03`

**Definition.** I can justify arguments for expanding federal authority by reasoning from weaknesses revealed by historical incidents and legal challenges.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Identifying Key Weaknesses in the Articles`, `Connecting Incidents to Constitutional Inadequacies`

**KUD items covered:** `blk_0201_item_03`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can justify arguments for expanding federal power by analyzing weaknesses exposed by historical incidents under the Articles of Confederation. |

### Constitutional Compromises and Ratification — `cluster_05`

**Definition.** The ability to explain how compromises made during the Constitutional Convention and ratification debates shaped the structure and amendment process of the Constitution.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L487-503. **KUD items:** 6.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0217_item_01` | Type 1 | know | House of Representatives based on each state's population and the Senate representing each state equally |
| `blk_0217_item_02` | Type 1 | know | Electoral College, which created a system for electing the president by electors from each state rather than by popular vote or by congressional vote |
| `blk_0217_item_03` | Type 1 | know | Three-Fifths Compromise, which provided a formula for calculating a state's enslaved population for purposes of representation in the House and for taxation |
| `blk_0217_item_04` | Type 1 | know | Postponing until 1808 a decision whether to ban the importation of enslaved persons |
| `blk_0217_item_05` | Type 1 | know | Agreement to add a Bill of Rights to address concerns of the Anti-Federalists |
| `blk_0219_item_01` | Type 1 | know | Debates about self-government during the drafting of the Constitution necessitated the drafting of an amendment process in Article V |

#### Learning Targets

##### Identifying Key Constitutional Compromises — `cluster_05_lt_01`

**Definition.** I can identify and describe the major compromises made during the Constitutional Convention and their structural outcomes.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `lt_set_unstable`.

**KUD items covered:** `blk_0217_item_01`, `blk_0217_item_02`, `blk_0217_item_03`, `blk_0217_item_04`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify major constitutional compromises and explain their structural effects on government. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the learner can identify and accurately describe major compromises and their structural outcomes, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.

_Propositional-thin flag:_ this is a factual Type 1 LT; the rubric is necessarily compressed.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify or describe constitutional compromises. |
| emerging | Names one or two compromises with minimal or inaccurate structural detail. |
| developing | Identifies several major compromises independently but describes structural outcomes incompletely or inconsistently. |
| competent | Identifies major compromises and accurately describes how each shaped constitutional structure and resolved conflicts. |
| extending | Identifies compromises and explains how they reflect broader ideological tensions or constrained later constitutional interpretation. |

_Prerequisite edges:_
- `cluster_04_lt_01` [pedagogical_sequencing/medium] — Understanding Articles of Confederation weaknesses provides context for why compromises were necessary at the Convention.
- `cluster_03_lt_01` [pedagogical_sequencing/medium] — Federalist arguments for strong central government illuminate the motivations behind key compromises at the Convention.
- `cluster_03_lt_02` [pedagogical_sequencing/medium] — Anti-Federalist concerns about centralized power explain the opposing interests that compromises had to balance.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a primary source excerpt from the Convention and ask them to identify what problem or disagreement the delegates were trying to solve.
- stage: Have students brainstorm what a 'compromise' means and list examples from their own experience of how two sides reach agreement.
- stage: Guide students to name specific compromises from the Convention and record them on a shared chart.
- stage: Ask students to describe what each compromise actually changed in the Constitution's structure and how it settled the conflict.
- stage: Invite students to reflect on whether some compromises were more important than others and why.
- prompt: What was the main disagreement between delegates that led to this compromise?
- prompt: How did this compromise change what the Constitution actually says or how government works?
- prompt: Which compromises do you think had the biggest impact on the structure of our government, and why?
- prompt: Can you name a compromise and explain both sides of the conflict it resolved?
- prompt: What would the Constitution look like if this compromise had not been made?
- anchor-examples guidance: Select one compromise that is straightforward and well-documented in primary sources and one that shows clear structural consequences in the final document; avoid compromises that are ambiguous or require deep historical context beyond the Convention itself.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to identify or describe any constitutional compromises. |
| emerging | I can name one or two compromises from the Convention but provide only basic or unclear details about how they shaped the Constitution. |
| developing | I can identify several major compromises on my own but sometimes miss details about their structural outcomes or describe them inconsistently. |
| competent | I can identify major compromises and clearly explain how each one changed the Constitution's structure and resolved the conflict between delegates. |
| extending | I can identify compromises and explain how they reflect deeper disagreements about power and ideology, and how they limited or shaped later interpretations of the Constitution. |

- self-check: Can I name at least three major compromises and describe what each one actually changed in the Constitution?
- self-check: Can I explain what conflict or disagreement each compromise was meant to solve?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to choose one compromise from a provided list and tell you what problem it solved.
  - Provide a primary source quote about a specific compromise and ask the student to identify what two sides disagreed about.
- **emerging**
  - Ask the student to add one more compromise to their list and describe what structural change it made to the government.
  - Prompt the student to clarify a vague description by asking 'What part of the Constitution did this compromise affect?'
- **developing**
  - Ask the student to check their descriptions against the actual text of the Constitution and revise any that are incomplete.
  - Have the student compare two compromises and explain which one had a bigger impact on how government works and why.
- **competent**
  - Ask the student to consider what ideological or philosophical disagreement lay beneath one of their compromises.
  - Prompt the student to research how one compromise influenced later debates or court decisions about constitutional meaning.

##### Explaining How Compromises Shaped Constitutional Structure — `cluster_05_lt_02`

**Definition.** I can explain how specific compromises resolved conflicts between state and federal interests and shaped the Constitution's framework.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `lt_set_unstable`.

**Prerequisites:** `Identifying Key Constitutional Compromises`

**KUD items covered:** `blk_0217_item_01`, `blk_0217_item_02`, `blk_0217_item_03`, `blk_0217_item_04`, `blk_0217_item_05`, `blk_0219_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain how constitutional compromises resolved conflicts between state and federal power. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **FAIL**.

_Gate failures:_ single_construct

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated ('Explains how multiple specific compromises...') without hedging language, incompleteness markers, or positioning it as a way-station to Extending.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to explain how compromises shaped the Constitution. |
| emerging | Names a compromise but explanation of its conflict resolution is incomplete or inaccurate. |
| developing | Explains how one or two compromises resolved specific conflicts independently but lacks depth or scope. |
| competent | Explains how multiple specific compromises resolved state-federal conflicts and shaped constitutional structure. |
| extending | Explains how compromises interconnect to address competing interests across multiple constitutional dimensions. |

_Prerequisite edges:_
- `cluster_05_lt_01` [ontological_prerequisite/high] — Must identify what the compromises were before explaining how they shaped structure and resolved conflicts.
- `cluster_03_lt_01` [pedagogical_sequencing/medium] — Understanding Federalist arguments for central government provides context for why compromises between state and federal power were necessary.
- `cluster_03_lt_02` [pedagogical_sequencing/medium] — Understanding Anti-Federalist concerns about centralized power clarifies the conflicts that compromises were designed to resolve.
- `cluster_04_lt_02` [pedagogical_sequencing/medium] — Understanding how historical incidents exposed gaps in the Articles provides motivation for why Constitutional compromises were needed.

### Separation of Powers and Checks and Balances — `cluster_06`

**Definition.** The ability to explain how separation of powers and checks and balances distribute governmental authority and prevent abuse of power.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L569-599. **KUD items:** 10.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0248_item_01` | Type 1 | know | The specific and separate powers delegated to Congress, the president, and the courts. |
| `blk_0248_item_02` | Type 1 | understand | The constitutional principles of separation of powers and checks and balances: each branch can check and balance the power of the other branches, ensuring no one branch becomes too powerful. |
| `blk_0248_item_03` | Type 2 | do_skill | Explain how the constitutional principles of separation of powers and checks and balances operate in response to specific governmental actions or policy proposals. |
| `blk_0255_item_01` | Type 1 | understand | Checks and balances control potential abuses by majorities, as explained in Federalist No. 51. |
| `blk_0255_item_02` | Type 2 | do_skill | Analyse Federalist No. 51 to identify and explain how checks and balances function to control potential abuses by majorities. |
| `blk_0257_item_01` | Type 1 | understand | Separation of powers and checks and balances create multiple access points for stakeholders and institutions to influence public policy. |
| `blk_0257_item_02` | Type 1 | do_skill | Explain the effects of separation of powers and checks and balances on public policy influence. |
| `blk_0260_item_01` | Type 1 | understand | Checks and balances and separation of powers allow legal actions to be taken against public officials deemed to have abused their power. |
| `blk_0261_item_01` | Type 1 | know | Impeachment is the process by which the House formally charges an official with abuse of power or misconduct. |
| `blk_0261_item_02` | Type 1 | know | Removal is the outcome if an official is convicted in a Senate impeachment trial. |

#### Learning Targets

##### Explaining Separation of Powers and Checks — `cluster_06_lt_01`

**Definition.** I can explain how the three branches of government exercise separate powers and check each other to prevent any single branch from becoming too powerful.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0248_item_01`, `blk_0248_item_02`, `blk_0255_item_01`, `blk_0260_item_01`, `blk_0261_item_01`, `blk_0261_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain how separation of powers and checks and balances prevent governmental branch concentration. |

##### Analysing Separation of Powers in Context — `cluster_06_lt_02`

**Definition.** I can analyse how separation of powers and checks and balances operate in response to specific governmental actions, policy proposals, or historical examples.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Explaining Separation of Powers and Checks`

**KUD items covered:** `blk_0248_item_03`, `blk_0255_item_02`, `blk_0257_item_01`, `blk_0257_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can analyse how separation of powers and checks and balances function in response to specific governmental actions or policy proposals. |

### Federalism and the Distribution of Power — `cluster_07`

**Definition.** The ability to explain how federalism allocates power between national and state governments through exclusive, reserved, and concurrent powers, and how this distribution affects policymaking.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L652-822. **KUD items:** 15.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0285_item_01` | Type 1 | know | In Colorado and Washington (2012), exclusive power is held by only one level of government and includes enumerated powers |
| `blk_0289_item_01` | Type 1 | know | The Necessary and Proper Clause |
| `blk_0293_item_01` | Type 1 | know | Reserved powers are those not delegated or enumerated to the national government but are reserved to the states, as stated in the Tenth Amendment. |
| `blk_0295_item_01` | Type 1 | know | Concurrent powers are shared between both levels of government such as the power to collect taxes, the power to make and enforce laws and the power to build roads. |
| `blk_0297_item_01` | Type 1 | know | Revenue sharing is a form of funding in which the national government provides funding to states with almost no restrictions on its use, and is the least used form of funding. |
| `blk_0297_item_02` | Type 1 | understand | Revenue sharing demonstrates the distribution of power between national and state governments. |
| `blk_0304_item_01` | Type 1 | know | Block grants are national funding with minimal restrictions to the states on its use. |
| `blk_0306_item_01` | Type 1 | know | Expenditures are a form of funding preferred by the national government and the most commonly used form of funding. |
| `blk_0306_item_02` | Type 1 | know | Mandates are requirements imposed by the national government on the states. |
| `blk_0343_item_01` | Type 1 | understand | Supreme Court interpretations can influence the extent of constitutional powers. |
| `blk_0347_item_01` | Type 1 | know | The Supremacy Clause gives the national government and its laws general precedence over states' laws. |
| `blk_0347_item_02` | Type 1 | understand | Supreme Court interpretations may affect when specific actions exceed the constitutional power granted to the national government under the Supremacy Clause and the Commerce Clause, and the Tenth Amen |
| `blk_0361_item_01` | Type 1 | understand | The allocation of powers between national and state governments creates multiple access points for stakeholders and institutions to influence public policy. |
| `blk_0361_item_02` | Type 2 | do_skill | Explain how the distribution of powers between national and state governments impacts policymaking. |
| `blk_0363_item_01` | Type 1 | understand | National policymaking is constrained by the sharing of concurrent powers with state governments. |

#### Learning Targets

##### Identifying Types of Governmental Powers — `cluster_07_lt_01`

**Definition.** I can identify and distinguish exclusive, reserved, and concurrent powers and explain how each type allocates authority between national and state governments.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0285_item_01`, `blk_0293_item_01`, `blk_0295_item_01`, `blk_0289_item_01`, `blk_0347_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify and distinguish exclusive, reserved, and concurrent powers in the federal system. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the learner as independently demonstrating the capability to identify, distinguish, and explain all three power types and their authority allocation—matching the LT's level of demand with no hedging language or incompleteness framing.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify or distinguish types of governmental powers. |
| emerging | With support, names exclusive, reserved, or concurrent powers but confuses their definitions or allocation. |
| developing | Independently identifies and distinguishes the three power types but incompletely explains their allocation between governments. |
| competent | Identifies and distinguishes exclusive, reserved, and concurrent powers and accurately explains how each allocates authority between national and state governments. |
| extending | Applies the power typology to novel constitutional scenarios or integrates it with separation of powers principles. |

_Prerequisite edges:_
- `cluster_03_lt_01` [pedagogical_sequencing/medium] — Federalist arguments for strong central government provide historical context for understanding why certain powers are allocated to the national level.
- `cluster_03_lt_02` [pedagogical_sequencing/medium] — Anti-Federalist concerns about centralized power establish the tension that the power-distribution framework resolves.
- `cluster_05_lt_02` [pedagogical_sequencing/medium] — Understanding how compromises shaped the Constitution's framework helps explain why powers are distributed as they are.

**Supporting components** — stability `stable`.

_Co-construction plan:_
- stage: Show students three real constitutional powers and ask them to sort by who holds them: only national, only state, or both.
- stage: Guide students to name each category and predict what the names might mean based on the sorting.
- stage: Have students draft definitions for exclusive, reserved, and concurrent by examining the powers in each group.
- stage: Test definitions against new powers and refine language together until students can apply them consistently.
- prompt: Which of these powers belong only to the national government, only to states, or to both?
- prompt: What do you notice about the word 'exclusive'—what does it tell you about who can do that power?
- prompt: How would you explain to someone why a concurrent power is different from an exclusive power?
- prompt: Can you think of a power we haven't discussed and predict whether it would be exclusive, reserved, or concurrent?
- anchor-examples guidance: Choose one clear example for each power type that students can easily verify in the Constitution or a primary source, and one borderline or debatable case that requires students to apply their definitions rather than memorize.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to identify or name the types of governmental powers. |
| emerging | I can name exclusive, reserved, or concurrent powers with help, but I mix up what each type means or who holds them. |
| developing | I can identify and tell the difference between exclusive, reserved, and concurrent powers on my own, but I do not fully explain how each one divides power between national and state governments. |
| competent | I can identify and distinguish exclusive, reserved, and concurrent powers and clearly explain how each type gives authority to the national government, state governments, or both. |
| extending | I can apply the three power types to new constitutional situations or connect them to how the three branches of government separate power. |

- self-check: Can I name all three types of powers and explain what makes each one different?
- self-check: Can I point to a real power and correctly say whether it belongs to the national government only, the states only, or both?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to sort three given powers into groups based on who holds them, then name what they notice about each group.
  - Provide a definition of one power type and ask the student to find an example of it in a provided list.
- **emerging**
  - Have the student explain in their own words what 'exclusive' means, then check their definition against a power that only the national government holds.
  - Give the student a power and ask them to decide: does only one level of government hold this, or do both, and how do you know?
- **developing**
  - Ask the student to complete a sentence: 'Because this power is concurrent, both the national and state governments can ___, which means ___.'
  - Have the student explain why a specific power is reserved to the states rather than exclusive to the national government.
- **competent**
  - Present a novel constitutional scenario and ask the student to identify which power type applies and justify their choice.
  - Ask the student to explain how understanding exclusive, reserved, and concurrent powers helps them understand the balance of power in the Constitution.

##### Analyzing Power Distribution Effects on Policy — `cluster_07_lt_02`

**Definition.** I can explain how the distribution of powers between national and state governments constrains policymaking and creates multiple access points for stakeholder influence.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Identifying Types of Governmental Powers`

**KUD items covered:** `blk_0361_item_02`, `blk_0361_item_01`, `blk_0363_item_01`, `blk_0297_item_02`, `blk_0343_item_01`, `blk_0347_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain how federalism distributes power between national and state governments and affects policy outcomes. |

##### Distinguishing Federal Funding Mechanisms — `cluster_07_lt_03`

**Definition.** I can identify and compare different federal funding mechanisms and explain how each demonstrates the distribution of power between national and state governments.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0297_item_01`, `blk_0304_item_01`, `blk_0306_item_01`, `blk_0306_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify different federal funding mechanisms and explain how each reflects the distribution of power between national and state governments. |

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated without hedging language, frames Competent as meeting the LT's demands (identify, compare, explain), and stands alone as success without implying incompleteness.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify or compare federal funding mechanisms. |
| emerging | With support, names one or two funding mechanisms but comparisons are incomplete or inaccurate. |
| developing | Independently identifies multiple funding mechanisms and makes partial comparisons but lacks clear explanation of power distribution. |
| competent | Identifies and compares distinct federal funding mechanisms and explains how each reflects the distribution of power between national and state governments. |
| extending | Compares funding mechanisms across policy domains and evaluates how funding choices strategically shift power between governmental levels. |

_Prerequisite edges:_
- `cluster_07_lt_01` [ontological_prerequisite/high] — Understanding exclusive, reserved, and concurrent powers is foundational to recognizing how funding mechanisms allocate authority between levels.
- `cluster_05_lt_02` [pedagogical_sequencing/medium] — Knowledge of how constitutional compromises shaped federalism structure provides context for understanding modern funding mechanisms.
- `cluster_03_lt_01` [pedagogical_sequencing/medium] — Federalist arguments for central government authority establish the historical rationale underlying federal funding mechanisms.

**Supporting components** — stability `stable`.

_Co-construction plan:_
- stage: Show students a real federal funding document and ask them to identify what type of money is flowing and who controls it.
- stage: Guide students to name the funding mechanisms they notice and sort them into categories based on control and conditions.
- stage: Have students compare two mechanisms side-by-side to see which gives states more or less power.
- stage: Co-author level descriptors by asking students what 'identifying' and 'comparing' look like at each stage of learning.
- prompt: What do you notice about who gives the money and who decides how it gets spent?
- prompt: How is this funding mechanism different from the one we just looked at in terms of state choice?
- prompt: What would a student who is just starting to understand this look like compared to a student who really gets it?
- prompt: How could someone compare funding mechanisms across different policy areas like education and transportation?
- anchor-examples guidance: Choose funding examples that clearly show different levels of state autonomy: one where the federal government sets strict rules, one where states have significant discretion, and one that blends both. Ensure examples come from different policy domains so students see the pattern across contexts.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to identify or compare federal funding mechanisms. |
| emerging | I can name one or two federal funding mechanisms with help, but my comparisons are incomplete or mixed up. |
| developing | I can identify multiple federal funding mechanisms on my own and make some comparisons, but I do not clearly explain how they show power between national and state governments. |
| competent | I can identify and compare different federal funding mechanisms and explain how each one shows the distribution of power between national and state governments. |
| extending | I can compare funding mechanisms across different policy areas and evaluate how funding choices shift power between governmental levels in strategic ways. |

- self-check: Can I name at least three different federal funding mechanisms and describe how each one works?
- self-check: Can I explain which funding mechanism gives states more power and which gives the federal government more control, and why?

_Feedback moves by level:_
- **no_evidence**
  - Start with one funding mechanism and ask the student to describe who gives the money and who decides how it is used.
  - Provide a sentence frame: 'In this funding mechanism, the federal government controls ___ and the state controls ___.'
- **emerging**
  - Ask the student to find a second funding mechanism and place it next to the first one to spot one difference in how control works.
  - Prompt: 'Which of these two gives the state more freedom to spend the money the way it wants?'
- **developing**
  - Push the student to explain why the difference in control matters: 'What does it mean for state power when the federal government sets strict rules?'
  - Have the student apply the same comparison to a funding mechanism in a different policy area to see the pattern.
- **competent**
  - Ask the student to predict how a new funding mechanism would shift power and to justify the prediction based on patterns they have seen.
  - Challenge them to evaluate whether a particular funding design is effective at achieving both federal goals and state flexibility.

### Contemporary Constitutional Issues — `cluster_08`

**Definition.** The ability to analyse how historical constitutional debates over governmental power and individual rights continue to shape present-day policy issues.

**Dominant knowledge type:** Type 1. **Stability:** `cluster_unstable`. **Source lines:** L527-527. **KUD items:** 2.

_Stability diagnostics:_
- unmatched_in_run2
- unmatched_in_run3

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0231_item_01` | Type 1 | understand | The debate over the role of the national government, the powers of state governments, and the rights of individuals remains at the heart of present-day constitutional issues about democracy and govern |
| `blk_0231_item_02` | Type 2 | do_skill | Analyse present-day constitutional issues about democracy and governmental power through the lens of debates about government surveillance resulting from the federal government's response to the 9/11  |

#### Learning Targets

##### Connecting Historical Constitutional Debates to Current Policy — `cluster_08_lt_01`

**Definition.** I can identify how historical debates over national power, state authority, and individual rights shape present-day policy issues.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0231_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify connections between historical constitutional debates and contemporary policy issues. |

##### Analysing Contemporary Issues Through Constitutional Lenses — `cluster_08_lt_02`

**Definition.** I can analyse present-day constitutional issues by applying historical debates about governmental power and individual rights.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Connecting Historical Constitutional Debates to Current Policy`

**KUD items covered:** `blk_0231_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can analyse contemporary constitutional issues by applying historical debates about governmental power and individual rights. |

### Describing Political Principles and Institutions — `cluster_09`

**Definition.** The ability to describe political principles, institutions, processes, policies, and behaviors in different scenarios and contexts.

**Dominant knowledge type:** Type 2. **Stability:** `stable`. **Source lines:** L141-365. **KUD items:** 5.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0063_item_01` | Type 1 | know | Political principles, institutions, processes, policies, and behaviors illustrated in different scenarios |
| `blk_0063_item_02` | Type 2 | do_skill | Describe political principles, institutions, processes, policies, and behaviors illustrated in different scenarios in context |
| `blk_0119_item_01` | Type 1 | know | Political principles, institutions, processes, and policies that characterise democracies |
| `blk_0119_item_02` | Type 2 | do_skill | Describe political principles, institutions, processes, policies, and behaviors illustrated in different scenarios in context |
| `blk_0167_item_01` | Type 1 | know | Political principles, institutions, processes, and individual rights policies and behaviors |

#### Learning Targets

##### Identifying Political Principles and Institutions — `cluster_09_lt_01`

**Definition.** I can identify political principles, institutions, processes, policies, and behaviors in different scenarios and contexts.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0063_item_01`, `blk_0119_item_01`, `blk_0167_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify political principles and institutions within United States governmental structures and processes. |

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares independent, accurate identification across different scenarios and contexts, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.

_Propositional-thin flag:_ this is a factual Type 1 LT; the rubric is necessarily compressed.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify political principles or institutions. |
| emerging | With support, identifies one or two political principles or institutions but with inaccuracy or confusion. |
| developing | Independently identifies relevant political principles or institutions in familiar contexts but misses some or hesitates with novel scenarios. |
| competent | Independently identifies political principles, institutions, processes, policies, and behaviors accurately across different scenarios and contexts. |
| extending | Identifies political elements and distinguishes relationships between them across complex or unfamiliar contexts. |

##### Describing Political Principles in Context — `cluster_09_lt_02`

**Definition.** I can describe political principles, institutions, processes, policies, and behaviors by explaining how they operate in different scenarios and contexts.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Identifying Political Principles and Institutions`

**KUD items covered:** `blk_0063_item_02`, `blk_0119_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain how political principles and institutions function within specific governmental contexts and scenarios. |

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares independent capability to describe how political elements operate across different scenarios and contexts accurately, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to describe how a principle or institution operates. |
| emerging | With support, names a principle or institution but describes it incompletely or inaccurately across contexts. |
| developing | Independently describes how a principle or institution operates in one familiar context but struggles to transfer across scenarios. |
| competent | Independently describes how political principles, institutions, processes, policies, or behaviors operate across different scenarios and contexts accurately. |
| extending | Describes how principles and institutions operate across contexts and explains relationships or tensions between them. |

_Prerequisite edges:_
- `cluster_09_lt_01` [ontological_prerequisite/high] — Identifying principles and institutions is foundational; describing how they operate requires first recognizing what they are.
- `cluster_06_lt_01` [pedagogical_sequencing/medium] — Understanding separation of powers and checks provides essential institutional knowledge for describing how core governmental structures operate in context.
- `cluster_07_lt_01` [pedagogical_sequencing/medium] — Identifying types of powers is typically established before explaining how power distribution operates across different policy scenarios.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a political principle or institution and ask them to name what they see and what it does.
- stage: Have students describe how that same principle or institution works in two different real-world scenarios and identify what stays the same and what changes.
- stage: Guide students to articulate what 'describing how it operates' means by listing the key details they need to include.
- stage: Work together to distinguish between naming something and actually explaining how it works across different contexts.
- stage: Co-author level descriptors by asking students what evidence would show they can do this independently versus with help versus not yet.
- prompt: What is this principle or institution, and what is its main job or purpose?
- prompt: How does this principle or institution work differently in this scenario compared to that one, and what stays the same in both?
- prompt: What details do you need to explain to show someone understands how something operates, not just what it is?
- prompt: How would you know if someone was just naming a principle versus actually describing how it works?
- anchor-examples guidance: Choose anchor examples that show the same principle or institution operating in two contrasting contexts so students can see what 'transfer across scenarios' looks like. Select examples where the principle's core function is recognizable but its application differs noticeably.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to describe how a political principle or institution operates. |
| emerging | I can name a political principle or institution, but my description is incomplete or not quite accurate when I try to explain it in different contexts. |
| developing | I can independently describe how a political principle or institution operates in one familiar context, but I find it hard to explain how it works in a different scenario. |
| competent | I can independently describe how political principles, institutions, processes, policies, or behaviors operate accurately across different scenarios and contexts. |
| extending | I can describe how principles and institutions operate across contexts and explain how they relate to each other or create tensions with one another. |

- self-check: Can I explain not just what this principle or institution is, but how it actually works in more than one real situation?
- self-check: Did I describe the same principle or institution in at least two different contexts, and did my explanation stay accurate in both?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to identify what principle or institution they are looking at before attempting to describe it.
  - Provide a familiar context and model one sentence that describes how the principle operates there, then ask the student to try the next sentence.
- **emerging**
  - Ask the student to check their description against a second context and identify what they need to add or correct.
  - Prompt the student to explain not just what the principle does, but how it actually works step-by-step or in practice.
- **developing**
  - Introduce a second, less familiar context and ask the student to predict how the principle might operate there before explaining it.
  - Have the student compare their two descriptions side-by-side to spot what is the same about how the principle operates and what is different about the situation.
- **competent**
  - Ask the student to identify a tension or contradiction between how the principle operates in two different contexts.
  - Invite the student to explain how two related principles or institutions interact or influence each other across contexts.

### Analysing Arguments and Sources — `cluster_10`

**Definition.** The ability to analyse and explain how arguments and perspectives in sources relate to political principles, institutions, processes, policies, and behaviors.

**Dominant knowledge type:** Type 2. **Stability:** `stable`. **Source lines:** L155-551. **KUD items:** 4.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0071_item_01` | Type 2 | do_skill | Explain how an argument or perspective in a source relates to Confederation political principles, institutions, processes, policies, and behaviors. |
| `blk_0077_item_01` | Type 2 | do_skill | Explain how the argument or perspective in the source relates to political principles, institutions, processes, policies, and behaviors. |
| `blk_0191_item_01` | Type 2 | do_skill | Explain how the argument or perspective in a source relates to political principles, institutions, processes, policies, and behaviors. |
| `blk_0239_item_01` | Type 2 | do_skill | Explain how the argument or perspective in an American Government source relates to political principles, institutions, processes, policies, and behaviors. |

#### Learning Targets

##### Identifying Arguments and Perspectives in Sources — `cluster_10_lt_01`

**Definition.** I can identify and extract the main argument or perspective presented in a political source.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**KUD items covered:** `blk_0071_item_01`, `blk_0077_item_01`, `blk_0191_item_01`, `blk_0239_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify the main argument and underlying perspective in a political source. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated independently and at the LT's level of demand ('identifies and extracts...accurately'), with no hedging language or framing of incompleteness.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify an argument or perspective. |
| emerging | With support, names a topic but does not isolate the main argument or perspective clearly. |
| developing | Independently identifies a main argument or perspective but may miss nuance or secondary claims. |
| competent | Independently identifies and extracts the main argument or perspective presented in a political source accurately. |
| extending | Identifies the main argument and distinguishes it from related secondary claims or unstated assumptions. |

_Prerequisite edges:_
- `cluster_09_lt_01` [ontological_prerequisite/high] — Identifying political principles and institutions in scenarios is foundational to recognizing arguments rooted in those concepts.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a short political source and ask them to underline or highlight what they think the author most wants readers to believe.
- stage: Facilitate a whole-group discussion where students share what they highlighted and explain why they chose those parts.
- stage: Guide students to distinguish between the main argument and other details or claims that support it.
- stage: Co-author level descriptors by asking students what it looks like when someone does or does not identify an argument clearly.
- stage: Test the rubric together on a second source to refine language and ensure all levels are recognizable.
- prompt: What is the one big idea or claim the author wants you to believe most?
- prompt: How do you know that is the main argument and not just a supporting detail?
- prompt: What would it look like if someone only named the topic but missed the actual argument?
- prompt: What smaller claims or reasons does the author use to back up the main argument?
- anchor-examples guidance: Choose sources that have a clear, single main argument and sources where the argument is buried or mixed with secondary claims; this contrast helps students see the difference between emerging and developing work.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to identify what argument or perspective the author is presenting. |
| emerging | I can name the topic of the source, but with help I am still working to separate the main argument from other information. |
| developing | I can identify and state the main argument or perspective on my own, though I may miss some of the finer details or secondary claims. |
| competent | I can independently identify and pull out the main argument or perspective from a political source accurately and clearly. |
| extending | I can identify the main argument and explain how it differs from related secondary claims and ideas the author does not state directly. |

- self-check: Can I state the author's main argument in one or two sentences without listing all the details?
- self-check: Have I separated the main argument from the supporting reasons or secondary claims?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to point to one sentence in the source that tells what the author believes most strongly.
  - Model thinking aloud: identify the main argument yourself, then ask the student to try the same process on a new source with you.
- **emerging**
  - Ask the student to restate the topic they named, then push: what does the author want you to do or believe about that topic?
  - Provide a sentence frame: the author argues that _____, and use it together to isolate the main claim from supporting details.
- **developing**
  - Ask the student to identify one secondary claim or supporting reason and explain how it differs from the main argument.
  - Prompt: are there any assumptions the author makes that are not stated directly, or any smaller disagreements within the main argument?
- **competent**
  - Challenge the student to find an unstated assumption or belief that underlies the main argument.
  - Ask the student to compare the main argument to a related but different perspective to sharpen their understanding of what makes this argument distinct.

##### Connecting Arguments to Political Frameworks — `cluster_10_lt_02`

**Definition.** I can explain how an argument or perspective in a source relates to political principles, institutions, processes, policies, and behaviors.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Identifying Arguments and Perspectives in Sources`

**KUD items covered:** `blk_0071_item_01`, `blk_0077_item_01`, `blk_0191_item_01`, `blk_0239_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain how an argument in a source connects to specific political principles, institutions, or processes. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **FAIL**.

_Gate failures:_ observable_verb

_Competent-framing judge:_ `pass` — The descriptor declares independent capability to explain connections between arguments and political frameworks at the level demanded by the LT, with no hedging language or implication of incompleteness.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to connect argument to political framework. |
| emerging | With support, identifies a framework but explanation of connection is unclear or incomplete. |
| developing | Independently connects argument to a framework but reasoning lacks depth or precision. |
| competent | Independently explains how an argument or perspective relates to relevant political principles, institutions, processes, policies, or behaviors. |
| extending | Connects argument to multiple frameworks or explains how competing frameworks illuminate different dimensions of the argument. |

_Prerequisite edges:_
- `cluster_10_lt_01` [ontological_prerequisite/high] — Cannot connect an argument to frameworks without first identifying what the argument is.
- `cluster_09_lt_01` [ontological_prerequisite/high] — Must recognize political principles and institutions in order to connect arguments to them.
- `cluster_09_lt_02` [pedagogical_sequencing/medium] — Describing how frameworks operate in context builds fluency needed to explain argument-framework relationships.

### Applying Concepts to Scenarios — `cluster_11`

**Definition.** The ability to explain how political principles, institutions, processes, policies, and behaviors apply to different scenarios and contexts.

**Dominant knowledge type:** Type 2. **Stability:** `stable`. **Source lines:** L160-469. **KUD items:** 3.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0074_item_01` | Type 2 | do_skill | Explain how political principles, institutions, processes, policies, and behaviors apply to different scenarios in context. |
| `blk_0211_item_01` | Type 1 | know | Political principles, institutions, U.S. Constitution processes, and policies |
| `blk_0211_item_02` | Type 2 | do_skill | Explain how political principles, institutions, U.S. Constitution processes, policies, and behaviors apply to different scenarios in context |

#### Learning Targets

##### Identifying Political Concepts in Scenarios — `cluster_11_lt_01`

**Definition.** I can identify political principles, institutions, processes, and policies relevant to a given scenario.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0211_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify relevant political principles, institutions, and processes within a given scenario. |

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares independent identification of multiple relevant political concepts without hedging language, incompleteness markers, or framing Competent as a stepping stone to Extending.

_Propositional-thin flag:_ this is a factual Type 1 LT; the rubric is necessarily compressed.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify political concepts in the scenario. |
| emerging | With support, names one or two concepts but misidentifies their relevance or accuracy. |
| developing | Independently identifies some relevant concepts but misses others or fails to connect them fully. |
| competent | Independently identifies multiple relevant political principles, institutions, processes, or policies in the scenario. |
| extending | Identifies concepts and explains how they interact or relate to one another within the scenario. |

_Prerequisite edges:_
- `cluster_09_lt_01` [ontological_prerequisite/high] — cluster_09_lt_01 requires identifying political concepts across scenarios; cluster_11_lt_01 applies that same identification skill to specific given scenarios.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a short political scenario and ask them to list any words or ideas they notice that sound 'political' or 'government-related'.
- stage: Guide students to sort their words into four categories: principles, institutions, processes, and policies.
- stage: Work together to define what each category means using their own examples from the scenario.
- stage: Co-create descriptors for each rubric level by asking students what 'trying but not quite there' versus 'nailing it' looks like.
- stage: Test the rubric together on a new scenario to refine language and ensure clarity.
- prompt: What words or ideas in this scenario remind you of government, rules, or how decisions get made?
- prompt: Which of these ideas are about values or beliefs, which are organizations, which are steps or actions, and which are rules or plans?
- prompt: How would you describe the difference between someone who names one concept and someone who finds many and explains how they connect?
- prompt: What would help you know you've found all the important political ideas in a scenario?
- anchor-examples guidance: Choose scenarios that contain a mix of principles, institutions, processes, and policies so students can practice identifying across all four categories; select one scenario where concepts clearly interact or depend on each other to anchor the extending level.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to identify political concepts in the scenario. |
| emerging | I can name one or two political concepts with help, but I may get their meaning or how they fit the scenario wrong. |
| developing | I can identify some political concepts on my own, but I might miss some or not fully explain how they connect to the scenario. |
| competent | I can independently identify multiple political principles, institutions, processes, or policies that are relevant to the scenario. |
| extending | I can identify concepts and explain how they interact or depend on each other within the scenario. |

- self-check: Did I find at least one example from each category: a principle, an institution, a process, and a policy?
- self-check: Can I explain not just what each concept is, but why it matters to this particular scenario?

_Feedback moves by level:_
- **no_evidence**
  - Point to one word or phrase in the scenario and ask: 'Is this about government or how decisions are made?'
  - Offer a sentence starter: 'One political concept I notice is …' and ask the student to complete it.
- **emerging**
  - Ask the student to sort their named concepts into the four categories and check if each one truly fits.
  - Restate what the student said and ask: 'Does that match what actually happens in the scenario?'
- **developing**
  - Ask: 'What else in the scenario involves government, rules, or decision-making that you haven't named yet?'
  - Guide them to pick two concepts they found and explain how one affects the other in the scenario.
- **competent**
  - Ask: 'How do these concepts work together or depend on each other to make this scenario happen?'
  - Prompt them to predict what would change if one of the concepts were removed or changed.

##### Explaining Political Concept Application — `cluster_11_lt_02`

**Definition.** I can explain how political principles, institutions, processes, policies, and behaviors apply to different scenarios and contexts.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Identifying Political Concepts in Scenarios`

**KUD items covered:** `blk_0074_item_01`, `blk_0211_item_02`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can explain how political principles and institutions apply to real-world government scenarios. |

### Constructing and Supporting Arguments — `cluster_12`

**Definition.** The ability to articulate defensible claims and support arguments with relevant evidence, explaining causes, effects, and significance.

**Dominant knowledge type:** Type 2. **Stability:** `stable`. **Source lines:** L118-805. **KUD items:** 6.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0053_item_01` | Type 2 | do_skill | Construct written arguments that take a position beyond simply stating facts, incorporating claims that are supported by additional information that sets up the evidence. |
| `blk_0053_item_02` | Type 2 | do_skill | Explain causes and effects in arguments, and explain the significance of similarities and differences between phenomena or processes. |
| `blk_0080_item_01` | Type 2 | do_skill | Articulate a defensible claim or thesis. |
| `blk_0087_item_01` | Type 2 | do_skill | Support an argument or claim/thesis using relevant evidence. |
| `blk_0269_item_01` | Type 2 | do_skill | Articulate a defensible claim or thesis. |
| `blk_0356_item_01` | Type 2 | do_skill | Support an argument or claim/thesis using relevant evidence. |

#### Learning Targets

##### Articulating Defensible Claims — `cluster_12_lt_01`

**Definition.** I can articulate a defensible claim or thesis that goes beyond stating facts.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `lt_set_unstable`.

**KUD items covered:** `blk_0080_item_01`, `blk_0269_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can articulate a defensible claim about government or politics that interprets evidence beyond restating facts. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **FAIL**.

_Gate failures:_ observable_verb

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated ('Articulates') at the target level without hedging, incompleteness language, or framing Competent as a stepping stone to Extending.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to articulate a claim or thesis. |
| emerging | States a fact or topic with heavy support; claim lacks defensibility or reasoning. |
| developing | Articulates a claim independently but it remains largely factual or lacks clear argumentative stance. |
| competent | Articulates a defensible claim or thesis that moves beyond facts and takes a clear argumentative position. |
| extending | Articulates a nuanced, defensible claim that anticipates counterarguments or integrates multiple perspectives. |

_Prerequisite edges:_
- `cluster_10_lt_01` [pedagogical_sequencing/medium] — Identifying arguments in sources builds foundational skill for constructing one's own defensible claim.
- `cluster_09_lt_02` [pedagogical_sequencing/medium] — Describing how political principles operate in context develops reasoning capacity needed to support a defensible claim.

##### Supporting Arguments with Evidence — `cluster_12_lt_02`

**Definition.** I can support an argument with relevant evidence and explain causes, effects, and significance.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `lt_set_unstable`.

**Prerequisites:** `Articulating Defensible Claims`

**KUD items covered:** `blk_0053_item_01`, `blk_0053_item_02`, `blk_0087_item_01`, `blk_0356_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can support a claim about government with relevant evidence and explain its significance. |

### Understanding Governmental Terminology — `cluster_13`

**Definition.** The ability to know and understand the definitions of governmental terms and concepts essential to studying U.S. government.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L99-172. **KUD items:** 2.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0045_item_01` | Type 1 | know | Know the definition of governmental terms: citizens and other people in the country. |
| `blk_0084_item_01` | Type 1 | know | The facts, issue, holding, reasoning, decision, and majority Federalism opinion of required Supreme Court cases |

#### Learning Targets

##### Defining Core Governmental Roles and Status — `cluster_13_lt_01`

**Definition.** I can identify and explain the definitions of governmental terms related to citizenship and participation in the country.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0045_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify and explain key governmental terms related to citizenship and political participation. |

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated independently at the LT's level of demand without hedging language, incompleteness markers, or positioning it as a way-station to Extending.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify or explain governmental terms. |
| emerging | With support, identifies some governmental terms but explanations are incomplete or inaccurate. |
| developing | Independently identifies and explains most core governmental terms but misses nuance in some definitions. |
| competent | Identifies and explains core governmental terms related to citizenship and participation accurately and independently. |
| extending | Applies governmental terminology to distinguish roles and relationships across multiple political contexts. |

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a collection of governmental terms and ask them to sort by familiarity.
- stage: Have students work in pairs to write their own definitions of 2–3 terms without looking them up.
- stage: Introduce the official definitions and compare them to student definitions to identify what makes a definition complete and accurate.
- stage: Build the rubric levels together by asking what 'with support,' 'independently,' and 'nuance' look like in practice.
- stage: Co-select anchor examples from student work that match each level.
- prompt: Which governmental terms do you already know, and which are new to you?
- prompt: How would you explain this term to someone who has never heard it before?
- prompt: What details or connections did the official definition include that your definition missed?
- prompt: What does it mean to explain a term 'independently' versus 'with support'?
- prompt: What would it look like if someone went beyond just defining a term and showed how it connects to other ideas?
- anchor-examples guidance: Select student work samples that show a clear progression from vague or incomplete attempts to precise, independent explanations that recognize subtle differences between related terms. Prioritize examples that reveal common misconceptions at emerging and developing levels.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to identify or explain governmental terms. |
| emerging | I can identify some governmental terms with help, but my explanations are incomplete or not quite right. |
| developing | I can identify and explain most core governmental terms on my own, but I may miss some details or connections between them. |
| competent | I can identify and explain core governmental terms related to citizenship and participation accurately and without help. |
| extending | I can use governmental terminology to show how roles and relationships differ across different political situations or countries. |

- self-check: Can I define each term in my own words and explain what it means for citizenship or participation?
- self-check: Have I noticed how different governmental terms relate to or differ from each other?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to choose one governmental term and tell you what they already know about it, even if it is just a guess.
  - Provide a simple definition and ask the student to rephrase it in their own words.
- **emerging**
  - Ask the student to add one more detail to their explanation by answering 'Why does this term matter for citizenship?'
  - Show the student a correct definition and ask them to identify which parts of their explanation were accurate and which need revision.
- **developing**
  - Ask the student to compare two related terms and explain how they are different.
  - Prompt the student to find a real-world example of the term in action and describe how it connects to the definition.
- **competent**
  - Ask the student to explain how a governmental term functions differently in two different political systems or contexts.
  - Invite the student to teach the term to a peer and then reflect on what questions or confusions came up.

##### Analyzing Supreme Court Case Components — `cluster_13_lt_02`

**Definition.** I can identify the facts, issue, holding, reasoning, decision, and majority opinion within landmark Supreme Court cases.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0084_item_01`

**Single-grade band** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Unit 1 | I can identify the facts, issue, holding, and reasoning within landmark Supreme Court cases. |

**Criterion rubric** — stability `rubric_unstable`, quality gate **FAIL**.

_Gate failures:_ single_construct

_Competent-framing judge:_ `pass` — The descriptor declares independent capability to identify and distinguish all required components without hedging language, implying the learning target is met.

_Propositional-thin flag:_ this is a factual Type 1 LT; the rubric is necessarily compressed.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify Supreme Court case components. |
| emerging | With support, identifies some case components but with significant inaccuracies or omissions. |
| developing | Independently identifies most case components but may conflate or incompletely explain one or two elements. |
| competent | Independently identifies and distinguishes facts, issue, holding, reasoning, decision, and majority opinion in landmark Supreme Court cases. |
| extending | Identifies case components and explains how they relate to broader constitutional principles or precedent. |

_Prerequisite edges:_
- `cluster_13_lt_01` [ontological_prerequisite/high] — Understanding governmental terminology and definitions is foundational to identifying and naming the formal components of Supreme Court cases.
- `cluster_06_lt_01` [pedagogical_sequencing/medium] — Understanding separation of powers and checks provides context for why Supreme Court cases arise and what constitutional issues they address.

## Halted items

### KUD halted blocks

- `blk_0004` — severe_underspecification: meta_or_nonteachable
- `blk_0006` — severe_underspecification: meta_or_nonteachable
- `blk_0008` — severe_underspecification: meta_or_nonteachable
- `blk_0009` — severe_underspecification: meta_or_nonteachable
- `blk_0010` — severe_underspecification: meta_or_nonteachable
- `blk_0011` — severe_underspecification: meta_or_nonteachable
- `blk_0012` — severe_underspecification: meta_or_nonteachable
- `blk_0013` — severe_underspecification: The source block is incomplete and contains no substantive teachable claim. The sentence fragment 'Whether assigned as homework or completed in class, the Progress' does not articulate a learning expectation, propositional claim, skill, or orientation that could be operationalised through assessment or observation. The block appears to be a navigation or structural element (heading path: CLASS PERIODS) with an incomplete sentence that cannot be classified against the Step 0 decision tree.
- `blk_0014` — severe_underspecification: meta_or_nonteachable
- `blk_0015` — severe_underspecification: meta_or_nonteachable
- `blk_0016` — severe_underspecification: meta_or_nonteachable
- `blk_0017` — severe_underspecification: meta_or_nonteachable
- `blk_0018` — severe_underspecification: meta_or_nonteachable
- `blk_0019` — severe_underspecification: meta_or_nonteachable
- `blk_0020` — severe_underspecification: meta_or_nonteachable
- `blk_0021` — severe_underspecification: meta_or_nonteachable
- `blk_0023` — severe_underspecification: meta_or_nonteachable
- `blk_0025` — severe_underspecification: meta_or_nonteachable
- `blk_0028` — severe_underspecification: The source block is a rhetorical question posed as a unit heading. It names a topic (Constitutional structure, framers' intent, compromises, balance of power) but contains no propositional claim, no analytical framework, no procedural instruction, and no sustained orientation that could be operationalised. The block functions as a navigation/framing device rather than a teachable content statement. No learner knowledge, understanding, skill, or disposition can be extracted from the question itself without external elaboration of what learners must know or do in response to it.
- `blk_0029` — severe_underspecification: meta_or_nonteachable
- `blk_0031` — severe_underspecification: meta_or_nonteachable
- `blk_0032` — severe_underspecification: meta_or_nonteachable
- `blk_0033` — severe_underspecification: The source block is a sentence fragment that appears to be mid-clause or incomplete. It contains no complete propositional claim, no skill descriptor, no observable behaviour, and no sustained orientation. The phrase 'Building the Course Skills § claim is the strongest because . . .' trails off without completing the reasoning or establishing what learners are expected to know, understand, or do. There is no teachable destination that could be operationalised through assessment.
- `blk_0034` — severe_underspecification: The source is a meta-navigational or procedural instruction about document structure ('Is the Bill of Rights then followed by specific relevant evidence') rather than a teachable claim about domain content. It describes a structural expectation for how evidence should be organised in a response or argument, not a substantive learning outcome. No propositional knowledge, conceptual understanding, skill deployment, or sustained orientation can be operationalised from this statement alone.
- `blk_0035` — severe_underspecification: meta_or_nonteachable
- `blk_0037` — severe_underspecification: The source block is a fragment consisting of an incomplete question ('Evidence is relevant when it relates to and or why not?') with no propositional claim, no skill description, no observable behaviour, and no clear teachable destination. It appears to be a navigation or prompt label rather than substantive curriculum content. No KUD item can be authored from this.
- `blk_0038` — severe_underspecification: The source block contains only a sentence fragment ('supports the claim.') with no substantive content, no propositional claim, no skill description, and no observable behaviour. It is non-teachable meta or structural text.
- `blk_0039` — severe_underspecification: meta_or_nonteachable
- `blk_0041` — severe_underspecification: meta_or_nonteachable
- `blk_0042` — severe_underspecification: The source block is a navigation or section header that names a curricular unit ('BIG IDEA 4') and references exam preparation without stating any substantive teachable claim, propositional content, skill, or sustained orientation. The phrase 'help political scientists understand how Policymaking governmental and political institutions and Interests' is grammatically incomplete and contains no clear object or learning destination. No observable behaviour, knowledge check, rubric criterion, or reasoning task can be grounded in this statement as written. This is meta-content labelling a section, not a teachable learning target.
- `blk_0043` — severe_underspecification: The source block is incomplete and contains no coherent teachable claim. The text 'The AP U.S. Government and Politics course actors function and the reasons for their §' is a sentence fragment that breaks mid-thought (ends with '§' symbol). No propositional content, skill, or orientation can be extracted. This appears to be corrupted metadata or a malformed heading rather than substantive curriculum content.
- `blk_0044` — severe_underspecification: The source block is syntactically malformed and incoherent. It appears to be corrupted text mixing fragments of multiple sentences ('How does the requires students to apply their knowledge behaviors', 'Constitution affect in a variety of contexts', 'real-world arguments about what the government does you and the choices scenarios'). No coherent propositional claim, skill description, or sustained orientation can be extracted. The block contains no teachable destination that could be operationalised through assessment, knowledge check, rubric, or observation.
- `blk_0046` — severe_underspecification: meta_or_nonteachable
- `blk_0047` — severe_underspecification: The source block is malformed and incoherent. It contains sentence fragments ('students also learn to write asked to show', 'Their arguments should how these concepts'), missing predicates, and no clear propositional or procedural claim that could be operationalised. The intended content cannot be reliably inferred from the text as written. No teachable destination (propositional knowledge, skill, or orientation) is discernible.
- `blk_0048` — severe_underspecification: The source block is an incomplete sentence fragment ('explain similarities and differences among') with no object, context, or domain specified. It names a cognitive action (explain, compare) but provides no propositional content, no scenario, and no referent for what is to be compared. Without specification of what entities, concepts, or cases are to be analysed, no rubric, knowledge check, or observable behaviour can be operationalised. This is not a sustained orientation (Type 3) or a reasoning task (Type 2) — it is a dangling instruction with no teachable destination.
- `blk_0049` — severe_underspecification: The source makes a descriptive claim about a learner population ('students often struggle with explanations') but contains no teachable content, no propositional knowledge to be understood, no skill to be practised, and no sustained orientation to be enacted. It is a diagnostic observation about a problem, not a learning target or curriculum expectation. No KUD item can be authored from this statement alone without external specification of what 'explanations' means, what 'struggling' entails operationally, or what the intended learning response is.
- `blk_0050` — severe_underspecification: The source block contains only a sentence fragment ('political principles or to explain political') with no complete propositional claim, no skill descriptor, no observable behaviour, and no coherent teachable destination. It is incomplete text that cannot be operationalised into a learning target.
- `blk_0051` — severe_underspecification: The source block is a sentence fragment ('They may define or describe a concept but processes') that is incomplete, grammatically malformed, and contains no coherent propositional claim, operational behaviour, or teachable destination. It cannot be classified against the decision tree or operationalised into a KUD item.
- `blk_0052` — severe_underspecification: The source block is a sentence fragment ('not fully explain the how or why in the context') with no complete propositional claim, no observable behaviour, no skill trigger, and no sustained orientation. It appears to be a partial note or editing artifact rather than a teachable content statement. No KUD item can be authored from this fragment.
- `blk_0054` — severe_underspecification: The source block is incomplete and contains only a fragment ('through a "because" statement, as in "My \|') with no coherent teachable claim, propositional content, skill description, or orientation. The text is truncated mid-sentence and provides no basis for KUD classification or assessment design.
- `blk_0055` — severe_underspecification: meta_or_nonteachable
- `blk_0056` — severe_underspecification: meta_or_nonteachable
- `blk_0058` — severe_underspecification: meta_or_nonteachable
- `blk_0060` — severe_underspecification: meta_or_nonteachable
- `blk_0061` — severe_underspecification: meta_or_nonteachable
- `blk_0064` — severe_underspecification: meta_or_nonteachable
- `blk_0065` — severe_underspecification: meta_or_nonteachable
- `blk_0066` — severe_underspecification: meta_or_nonteachable
- `blk_0068` — classification_unreliable: no signature achieved 2/3 agreement across runs; observed signatures: [('items', (('know', 'Type 1'), ('understand', 'Type 1'))), ('items', (('do_skill', 'Type 2'), ('know', 'Type 1'), ('know', 'Type 1'), ('understand', 'Type 1'), ('understand', 'Type 1'))), ('items', (('do_skill', 'Type 2'), ('know', 'Type 1'), ('know', 'Type 1'), ('know', 'Type 1'), ('know', 'Type 1')))]
- `blk_0069` — severe_underspecification: meta_or_nonteachable
- `blk_0072` — severe_underspecification: meta_or_nonteachable
- `blk_0075` — severe_underspecification: meta_or_nonteachable
- `blk_0078` — severe_underspecification: meta_or_nonteachable
- `blk_0081` — severe_underspecification: meta_or_nonteachable
- `blk_0082` — severe_underspecification: meta_or_nonteachable
- `blk_0085` — severe_underspecification: meta_or_nonteachable
- `blk_0088` — severe_underspecification: meta_or_nonteachable
- `blk_0089` — severe_underspecification: meta_or_nonteachable
- `blk_0090` — severe_underspecification: meta_or_nonteachable
- `blk_0091` — severe_underspecification: meta_or_nonteachable
- `blk_0093` — severe_underspecification: meta_or_nonteachable
- `blk_0095` — severe_underspecification: meta_or_nonteachable
- `blk_0096` — severe_underspecification: meta_or_nonteachable
- `blk_0097` — severe_underspecification: meta_or_nonteachable
- `blk_0098` — severe_underspecification: meta_or_nonteachable
- `blk_0099` — severe_underspecification: The source block is incomplete and contains no teachable claim. It begins a conditional clause ('When students are reading...') but provides no predicate, learning outcome, or substantive content to classify. The fragment names a document type (foundational documents, Federalist) but does not state what learners should know, understand, or do in relation to it. Without a complete propositional or capability statement, no KUD item can be authored.
- `blk_0100` — severe_underspecification: meta_or_nonteachable
- `blk_0101` — severe_underspecification: meta_or_nonteachable
- `blk_0102` — severe_underspecification: meta_or_nonteachable
- `blk_0103` — severe_underspecification: The source block is a truncated instructional activity label with no complete teachable claim. It names an activity type ('Give students a question') but the sentence is incomplete ('requires them to connect Madison's argument in' — no completion). There is no propositional content to understand, no skill to perform, no orientation to enact, and no assessment criterion that could be operationalised. The block is meta-instructional scaffolding, not substantive curriculum content.
- `blk_0104` — severe_underspecification: The source block is a fragment—a heading label ('SAMPLE INSTRUCTIONAL ACTIVITIES') followed by an incomplete sentence that names a primary source (Federalist No. 51) and a topic (structure of three branches) but contains no complete propositional claim, no skill descriptor, no orientation statement, and no assessment criterion. The sentence ends mid-phrase ('established in the') with no object or completion. This is meta-navigational content (a section heading) paired with an incomplete reference, not substantive teachable content. No KUD item can be authored from an incomplete sentence fragment.
- `blk_0105` — severe_underspecification: The source block is a fragment of a heading or navigation label ('Constitution and b) his argument about factions in Federalist No. 10') with no complete propositional claim, no skill description, and no sustained orientation. It names topics but contains no teachable content—no assertion about what learners should know, understand, or do. It appears to be a structural or labeling element within a curriculum document rather than substantive instructional content.
- `blk_0106` — severe_underspecification: meta_or_nonteachable
- `blk_0107` — severe_underspecification: meta_or_nonteachable
- `blk_0108` — classification_unreliable: no signature achieved 2/3 agreement across runs; observed signatures: [('items', (('do_skill', 'Type 2'), ('know', 'Type 1'), ('understand', 'Type 1'))), ('items', (('know', 'Type 1'), ('know', 'Type 1'), ('understand', 'Type 1'))), ('items', (('do_skill', 'Type 1'), ('know', 'Type 1'), ('understand', 'Type 1')))]
- `blk_0109` — severe_underspecification: meta_or_nonteachable
- `blk_0110` — severe_underspecification: meta_or_nonteachable
- `blk_0111` — severe_underspecification: meta_or_nonteachable
- `blk_0112` — severe_underspecification: meta_or_nonteachable
- `blk_0113` — severe_underspecification: meta_or_nonteachable
- `blk_0115` — severe_underspecification: meta_or_nonteachable
- `blk_0118` — severe_underspecification: meta_or_nonteachable
- `blk_0120` — severe_underspecification: meta_or_nonteachable
- `blk_0123` — severe_underspecification: meta_or_nonteachable
- `blk_0127` — severe_underspecification: The source block is a fragmentary reference phrase ('as in the failed state of Somalia') with no propositional claim, no analytical framework, no procedural instruction, and no sustained orientation. It appears to be a citation or example stub within a larger document structure, not a standalone teachable statement. Without the surrounding context that would establish what concept, claim, or capability this phrase is meant to illustrate, no KUD item can be authored.
- `blk_0128` — severe_underspecification: The source block is malformed and contains no coherent teachable claim. The text appears to be a corrupted heading or navigation label ('Explain how democratic The U.S. government is based on the following § ideals are reflected in the democratic ideals: The Mayflower') with no clear propositional content, no skill description, and no observable behaviour that could ground assessment. It is not a sustained orientation (Type 3), not a reasoning task (Type 2), and not a propositional claim (Type 1). The fragment does not constitute a valid learning target or content statement.
- `blk_0129` — severe_underspecification: The source block is a fragmented heading/label structure with incomplete propositional content. It names three historical documents (Declaration of Independence, Compact of 1620, U.S. Constitution) and a concept (natural rights) but contains no complete declarative claim, no causal relationship, no definition, and no operational descriptor that would ground a teachable learning target. The phrase 'all people have certain §' is syntactically incomplete (§ is a symbol, not a concept). There is no verb connecting the elements, no assertion about what learners should know, understand, or do with this content. This appears to be a navigation label or outline fragment rather than a substantive content statement suitable for KUD authoring.
- `blk_0130` — severe_underspecification: The source block is a fragment heading or label ('John Locke's Second rights that cannot be taken away') with no propositional content, no operational criteria, and no teachable claim. It appears to be a navigation or section marker rather than substantive curriculum content. No observable behaviour, knowledge check, rubric evidence, or reasoning task can be grounded in this fragment alone.
- `blk_0131` — severe_underspecification: meta_or_nonteachable
- `blk_0132` — severe_underspecification: Source block is a fragmented excerpt from a curriculum document heading and incomplete propositional content. The text is truncated mid-sentence, lacks coherent structure, and contains no complete teachable claim. The fragment names historical figures and concepts (Montesquieu, separation of powers, popular sovereignty, limited government) but does not state what learners are expected to know, understand, or do with these ideas. The heading path suggests this is a structural label rather than substantive content. No rubric, knowledge check, or observable behaviour can be grounded in this incomplete text.
- `blk_0134` — severe_underspecification: The source block is a fragment—a parenthetical clause with no propositional context, no causal claim, no operational definition, and no teachable destination. It states a normative assertion ('power cannot be absolute') but provides no content, reasoning framework, or observable behaviour that could ground assessment via rubric, knowledge check, or observation. Without the surrounding source material that would establish what 'power' refers to, what domain or context applies, and what learners are expected to know or do with this claim, no KUD item can be authored.
- `blk_0136` — severe_underspecification: meta_or_nonteachable
- `blk_0139` — severe_underspecification: The source block is incomplete. It begins a propositional statement ('The Declaration of Independence, drafted by') but terminates mid-sentence without naming the drafter(s), providing context, or completing any teachable claim. No knowledge type can be reliably classified from a sentence fragment. The block contains no assessable destination—neither a fact to know, a concept to understand, a skill to perform, nor an orientation to enact.
- `blk_0140` — severe_underspecification: Source block is incomplete and contains no complete teachable claim. The sentence fragment 'Thomas Jefferson (with help from Adams and' terminates mid-clause without specifying what action, concept, or propositional content is to be learned. No knowledge type can be assigned to an incomplete statement.
- `blk_0141` — severe_underspecification: The source block is a sentence fragment that names historical documents and figures (Franklin, Declaration, U.S. Constitution, James Madison) but contains no complete propositional claim, no analytical framework, and no operational descriptor. It appears to be a mid-sentence excerpt from a larger passage. No teachable destination—propositional, procedural, or dispositional—can be operationalised from this fragment alone. It lacks the context needed to determine what learners are expected to know, understand, or do with this content.
- `blk_0143` — severe_underspecification: meta_or_nonteachable
- `blk_0144` — severe_underspecification: meta_or_nonteachable
- `blk_0146` — severe_underspecification: meta_or_nonteachable
- `blk_0149` — severe_underspecification: meta_or_nonteachable
- `blk_0150` — severe_underspecification: The block is a procedural instruction (a task prompt or assessment rubric header) with no substantive teachable content. It names analytical dimensions (argument, perspective, evidence, reasoning) but does not state what the learner should know, understand, or be able to do with respect to Democracy or any other domain. The word 'Democracy' appears isolated and contextually orphaned. Without a source text, domain specification, or learning outcome claim, no KUD item can be authored from this block alone.
- `blk_0151` — severe_underspecification: meta_or_nonteachable
- `blk_0154` — classification_unreliable: no signature achieved 2/3 agreement across runs; observed signatures: [('items', (('do_skill', 'Type 1'), ('understand', 'Type 1'))), ('items', (('do_skill', 'Type 1'), ('know', 'Type 1'), ('understand', 'Type 1'))), ('items', (('do_skill', 'Type 2'), ('know', 'Type 1')))]
- `blk_0157` — classification_unreliable: no signature achieved 2/3 agreement across runs; observed signatures: [('items', (('know', 'Type 1'),)), ('items', (('do_skill', 'Type 2'), ('know', 'Type 1'))), ('items', (('do_skill', 'Type 2'), ('know', 'Type 1'), ('understand', 'Type 1')))]
- `blk_0160` — severe_underspecification: meta_or_nonteachable
- `blk_0161` — severe_underspecification: meta_or_nonteachable
- `blk_0163` — severe_underspecification: meta_or_nonteachable
- `blk_0166` — severe_underspecification: meta_or_nonteachable
- `blk_0168` — severe_underspecification: meta_or_nonteachable
- `blk_0169` — severe_underspecification: meta_or_nonteachable
- `blk_0170` — severe_underspecification: meta_or_nonteachable
- `blk_0174` — severe_underspecification: meta_or_nonteachable
- `blk_0175` — severe_underspecification: The source block is incomplete and incoherent. It begins with an imperative ('Explain') but the sentence structure breaks down mid-clause ('Explain Federalist and Anti-Federalists supported ratification of the (Federalist No. 10 and'). The object of explanation is unclear—it appears to cut off after 'and' without completing the thought. No complete propositional claim, skill trigger, or observable behaviour can be inferred from this fragment. It cannot be operationalised as a learning target without substantial reconstruction of the intended content.
- `blk_0177` — severe_underspecification: The source block is a malformed fragment combining a citation label (Brutus No. 1, Federalist No. 10), a navigation/section marker (Professional Development >), and an incomplete propositional claim about Madison's arguments. The fragment lacks sufficient coherence to identify a complete teachable claim: it does not state what the learner should know, understand, or be able to do with respect to Madison's arguments or the concept of faction control. The syntax suggests this is a corrupted heading or index entry rather than a substantive content statement. No observable behaviour, rubric criterion, or knowledge-check destination can be operationalised from this fragment.
- `blk_0178` — severe_underspecification: The source block is a heading/navigation label with no complete propositional claim, no skill description, and no sustained orientation. The text appears truncated ('Assessing Module— and dispersing power between the states and') and contains no teachable destination that could be operationalised through assessment, rubric, or observation. This is meta or non-teachable content.
- `blk_0179` — severe_underspecification: meta_or_nonteachable
- `blk_0180` — severe_underspecification: meta_or_nonteachable
- `blk_0182` — severe_underspecification: The source block is incomplete. It states 'Anti-Federalists opposed the ratification of the' but does not finish the sentence. No propositional claim, concept, skill, or orientation can be extracted from an incomplete fragment. The teachable destination cannot be determined.
- `blk_0183` — classification_unreliable: no signature achieved 2/3 agreement across runs; observed signatures: [('items', (('know', 'Type 1'), ('know', 'Type 1'), ('understand', 'Type 1'))), ('items', (('know', 'Type 1'), ('know', 'Type 1'), ('know', 'Type 1'))), ('items', (('know', 'Type 1'), ('understand', 'Type 1')))]
- `blk_0184` — severe_underspecification: meta_or_nonteachable
- `blk_0185` — severe_underspecification: meta_or_nonteachable
- `blk_0187` — severe_underspecification: meta_or_nonteachable
- `blk_0190` — severe_underspecification: meta_or_nonteachable
- `blk_0192` — severe_underspecification: meta_or_nonteachable
- `blk_0193` — severe_underspecification: meta_or_nonteachable
- `blk_0195` — severe_underspecification: meta_or_nonteachable
- `blk_0198` — severe_underspecification: meta_or_nonteachable
- `blk_0200` — severe_underspecification: meta_or_nonteachable
- `blk_0202` — severe_underspecification: The source block is a fragmented list of structural weaknesses (taxation, court system, interstate commerce, coinage) with no propositional claim, no analytical framework, no procedural instruction, and no sustained orientation. It appears to be a bullet-point fragment from a larger document (likely an outline of Articles of Confederation deficiencies) with no complete sentence or teachable assertion. Without context establishing what learners are expected to know, understand, or do with these items, no KUD item can be authored.
- `blk_0203` — severe_underspecification: meta_or_nonteachable
- `blk_0204` — severe_underspecification: meta_or_nonteachable
- `blk_0206` — severe_underspecification: meta_or_nonteachable
- `blk_0209` — severe_underspecification: meta_or_nonteachable
- `blk_0210` — severe_underspecification: meta_or_nonteachable
- `blk_0212` — severe_underspecification: meta_or_nonteachable
- `blk_0215` — severe_underspecification: The source block is syntactically malformed and does not constitute coherent propositional content. The sentence structure is broken ('Compromises deemed necessary for political negotiation ratification of the Constitution included the and compromise at the following'); the clause relationships are unclear; and the intended teachable claim cannot be reliably extracted. No valid KUD item can be authored from text that does not express a complete, intelligible proposition about what learners should know, understand, or do.
- `blk_0216` — severe_underspecification: The source block is a sentence fragment ('congressional representation with the') that is incomplete and contains no coherent propositional claim, procedural instruction, analytical framework, or sustained orientation. It cannot be operationalised as a learning target through any assessment route. This appears to be a truncated or corrupted text block with no teachable destination.
- `blk_0220` — severe_underspecification: The source block is a sentence fragment describing a procedural mechanism (amendment ratification thresholds) without a complete propositional claim, context, or teachable framing. It lacks a subject, verb structure, or clear assertion about what the learner should know or understand. The fragment 'V that entailed either...' is incomplete and cannot be operationalised as a standalone learning target. No knowledge type can be assigned without the full propositional or procedural context.
- `blk_0221` — severe_underspecification: meta_or_nonteachable
- `blk_0222` — severe_underspecification: meta_or_nonteachable
- `blk_0223` — severe_underspecification: meta_or_nonteachable
- `blk_0225` — severe_underspecification: meta_or_nonteachable
- `blk_0228` — severe_underspecification: The source block is malformed and incoherent. The heading path references a learning outcome (LO 1.5.A EK 1.5.A.3) but the content statement is a sentence fragment that appears to be corrupted mid-composition ('Explain the impact of The compromises necessary to secure political negotiation ratification of the Constitution left some and compromise at the matters unresolved that continue to generate'). The sentence lacks a grammatical subject, predicate, and object; it cannot be parsed into a coherent propositional claim, analytical task, or observable orientation. No teachable destination—whether propositional knowledge, reasoning capability, or sustained disposition—can be reliably inferred from this text. Clarification of the intended content is required before classification.
- `blk_0229` — severe_underspecification: The source block is a navigation or activity label ('Constitutional Convention discussion and debate today') with no propositional content, no skill descriptor, and no observable orientation. It names an activity or session topic but does not state what learners are expected to know, understand, do, or become as a result. No teachable destination can be operationalised from this text alone.
- `blk_0230` — severe_underspecification: The source block is a fragment referencing a learning outcome code (EK 1.5.A.4) without substantive teachable content. It contains no propositional claim, no skill description, no observable orientation, and no assessment-anchoring language. The phrase 'on the development of the EK 1.5.A.4 constitutional system' is a navigation or labeling artifact, not a complete learning expectation. No KUD item can be authored from this fragment alone.
- `blk_0232` — severe_underspecification: meta_or_nonteachable
- `blk_0233` — severe_underspecification: meta_or_nonteachable
- `blk_0235` — severe_underspecification: meta_or_nonteachable
- `blk_0238` — severe_underspecification: meta_or_nonteachable
- `blk_0240` — severe_underspecification: meta_or_nonteachable
- `blk_0242` — severe_underspecification: meta_or_nonteachable
- `blk_0243` — severe_underspecification: meta_or_nonteachable
- `blk_0245` — severe_underspecification: meta_or_nonteachable
- `blk_0246` — severe_underspecification: meta_or_nonteachable
- `blk_0247` — severe_underspecification: meta_or_nonteachable
- `blk_0249` — severe_underspecification: meta_or_nonteachable
- `blk_0251` — severe_underspecification: meta_or_nonteachable
- `blk_0253` — severe_underspecification: The source block is a navigation label or resource heading with no complete teachable claim. It names a document (Federalist No. 51) and gestures toward a topic (separation of powers and checks) but does not state what the learner is expected to know, understand, or do with this content. The sentence is incomplete (ends with 'and checks' without predicate or object). No propositional knowledge, analytical capability, or sustained orientation is specified. This is meta-content identifying an available resource, not a learning target.
- `blk_0254` — severe_underspecification: meta_or_nonteachable
- `blk_0258` — severe_underspecification: The source block is a navigation label or section heading with no substantive teachable claim. It names a domain ('U.S. political system') but contains no propositional content, no analytical framework, no procedural instruction, and no sustained orientation that could be operationalised through assessment. A heading alone does not constitute a learning target.
- `blk_0262` — severe_underspecification: meta_or_nonteachable
- `blk_0263` — severe_underspecification: meta_or_nonteachable
- `blk_0265` — severe_underspecification: meta_or_nonteachable
- `blk_0268` — severe_underspecification: meta_or_nonteachable
- `blk_0270` — severe_underspecification: meta_or_nonteachable
- `blk_0271` — severe_underspecification: meta_or_nonteachable
- `blk_0273` — severe_underspecification: meta_or_nonteachable
- `blk_0274` — severe_underspecification: meta_or_nonteachable
- `blk_0275` — severe_underspecification: meta_or_nonteachable
- `blk_0277` — severe_underspecification: meta_or_nonteachable
- `blk_0279` — severe_underspecification: The source block is incomplete and contains no teachable claim. The phrase 'Federal response to natural disasters such' is a sentence fragment that does not specify what learners should know, understand, or be able to do. No propositional content, skill, or orientation is identifiable. The block appears to be a heading or navigation label rather than substantive curriculum content.
- `blk_0280` — severe_underspecification: Source block is corrupted or incoherent. It conflates unrelated topics (Federalism, Hurricanes Katrina and Sandy, constitutional allocation of powers), contains incomplete sentences, and lacks a coherent propositional or skill claim. No teachable destination can be reliably inferred from the text as presented. The block appears to be a scanning or transcription error rather than intentional curriculum content.
- `blk_0281` — severe_underspecification: The source block is syntactically malformed and lacks coherent propositional or operational content. The phrase 'national and state governments help explain of 1984 the ongoing debate' is grammatically incomplete and does not articulate a clear factual claim, concept, skill, or orientation that could be operationalised through assessment. No teachable destination can be reliably inferred.
- `blk_0282` — severe_underspecification: The source block contains only a fragment ('of marijuana for') with no complete propositional claim, no skill descriptor, no observable behaviour, and no teachable destination. It cannot be classified against the Step 0 decision tree and cannot be operationalised as a learning target.
- `blk_0284` — severe_underspecification: meta_or_nonteachable
- `blk_0287` — severe_underspecification: The source block is a sentence fragment extracted from a larger document context. It references constitutional powers (explicit and implied) but provides no complete propositional claim, no analytical task, no sustained orientation, and no operational criteria. The fragment cannot stand alone as a teachable statement. Without the surrounding text, it is impossible to determine what learners are expected to know, understand, or do with this content.
- `blk_0288` — severe_underspecification: meta_or_nonteachable
- `blk_0290` — severe_underspecification: meta_or_nonteachable
- `blk_0292` — severe_underspecification: meta_or_nonteachable
- `blk_0298` — severe_underspecification: meta_or_nonteachable
- `blk_0299` — severe_underspecification: meta_or_nonteachable
- `blk_0301` — severe_underspecification: meta_or_nonteachable
- `blk_0305` — severe_underspecification: The source block is malformed and incoherent. It appears to be a corrupted or incomplete fragment mixing multiple unrelated clauses: a reference to constitutional allocation of power, an incomplete parenthetical about categorical grants, and a dangling phrase about funding affecting society. No coherent propositional claim, skill, or orientation can be extracted. The text does not state what learners should know, understand, or be able to do with sufficient clarity to author a teachable item.
- `blk_0307` — severe_underspecification: meta_or_nonteachable
- `blk_0308` — severe_underspecification: meta_or_nonteachable
- `blk_0310` — severe_underspecification: meta_or_nonteachable
- `blk_0314` — severe_underspecification: meta_or_nonteachable
- `blk_0315` — classification_unreliable: no signature achieved 2/3 agreement across runs; observed signatures: [('items', (('do_skill', 'Type 1'), ('do_skill', 'Type 2'))), ('items', (('do_skill', 'Type 2'), ('know', 'Type 1'))), ('items', (('do_skill', 'Type 1'), ('know', 'Type 1')))]
- `blk_0316` — severe_underspecification: meta_or_nonteachable
- `blk_0317` — severe_underspecification: meta_or_nonteachable
- `blk_0320` — severe_underspecification: meta_or_nonteachable
- `blk_0321` — severe_underspecification: meta_or_nonteachable
- `blk_0323` — severe_underspecification: meta_or_nonteachable
- `blk_0324` — severe_underspecification: meta_or_nonteachable
- `blk_0326` — severe_underspecification: meta_or_nonteachable
- `blk_0327` — severe_underspecification: meta_or_nonteachable
- `blk_0328` — severe_underspecification: The source block is malformed and incoherent. It appears to be a corrupted or incomplete merge of multiple fragments: 'Explain how the balance...of power between national and state governments has [been affected by]...The Due Process and Equal Protection Clauses...give the national government the power to enforce protections.' The syntax is broken ('The Due Process and Equal Protection Clauses and Social Science of power between national (1990) and state governments'), making it impossible to identify a coherent propositional claim, analytical task, or sustained orientation. No teachable destination can be operationalised from this text.
- `blk_0329` — severe_underspecification: The source block is syntactically incoherent and contains no identifiable propositional claim, causal relationship, concept, skill, or sustained orientation that could be operationalised through assessment. The text appears to be corrupted or incomplete (e.g. 'changed over time based for any person against the states, but Supreme § on interpretations of the Court interpretations can influence the extent' lacks grammatical structure and semantic coherence). No teachable destination can be inferred.
- `blk_0330` — severe_underspecification: meta_or_nonteachable
- `blk_0331` — severe_underspecification: Source block is a sentence fragment ('Supreme Court of the United of those protections.') that is incomplete, grammatically malformed, and contains no coherent propositional claim, concept, skill, or orientation that could be operationalised through assessment. It does not state what learners should know, understand, do, or enact. No teachable destination can be inferred.
- `blk_0332` — severe_underspecification: The source block is a navigation label or section heading with no propositional claim, procedural instruction, analytical task, or sustained orientation. It names two topics (Act of 1996 and state marriage laws) but contains no statement of what the learner should know, understand, do, or become. Without a verb phrase or declarative claim, no KUD item can be authored.
- `blk_0333` — severe_underspecification: meta_or_nonteachable
- `blk_0334` — severe_underspecification: meta_or_nonteachable
- `blk_0335` — severe_underspecification: The source block is incomplete and incoherent. It contains a fragmented propositional claim ('The Commerce Clause gives the national government the power to regulate interstate commerce') interrupted by an unrelated reference ('of 2001', 'Violence Against', '§') and an incomplete clause ('but Supreme Court interpretations' with no predicate or object). The text does not form a coherent teachable statement. It is unclear whether this is a corrupted data entry, a navigation artifact, or an incomplete draft. No valid KUD item can be authored from this fragment without substantial editorial reconstruction, which would violate the instruction not to invent content.
- `blk_0336` — severe_underspecification: The source block is a sentence fragment that names a legal instrument (Violence Against Women Act of 1994) and makes a causal claim about its influence on unspecified 'power', but provides no context, definition, or substantive content about what the Act is, what power is being referenced, how the influence operates, or what learners are expected to know or do with this information. Without the surrounding context (preceding sentences, section heading, learning objective), the fragment cannot be operationalised into a teachable claim—neither as propositional knowledge (what is the Act? what does it do?), nor as a skill (analyse what? in what situation?), nor as an orientation (what sustained behaviour is being developed?). The fragment is incomplete and non-standalone.
- `blk_0337` — severe_underspecification: meta_or_nonteachable
- `blk_0339` — severe_underspecification: meta_or_nonteachable
- `blk_0340` — severe_underspecification: The source block is a section heading with a symbol marker (§) and contains no propositional claim, no analytical framework, no observable behaviour, and no operational criteria. It names a constitutional clause and a concept ('available resources') but makes no substantive statement about what learners should know, understand, or do with this content. Without a predicate or explanatory clause, there is no teachable destination that could be assessed.
- `blk_0341` — severe_underspecification: The source block is a sentence fragment ('Congress the power to make laws related') that is incomplete and contains no coherent propositional claim, no skill descriptor, and no observable orientation. It cannot be operationalised as a learning target through any assessment route. The fragment appears to be a corrupted or truncated heading label rather than substantive teachable content.
- `blk_0342` — severe_underspecification: meta_or_nonteachable
- `blk_0344` — severe_underspecification: meta_or_nonteachable
- `blk_0346` — severe_underspecification: meta_or_nonteachable
- `blk_0348` — severe_underspecification: meta_or_nonteachable
- `blk_0349` — severe_underspecification: meta_or_nonteachable
- `blk_0351` — severe_underspecification: meta_or_nonteachable
- `blk_0354` — severe_underspecification: meta_or_nonteachable
- `blk_0355` — severe_underspecification: meta_or_nonteachable
- `blk_0357` — severe_underspecification: meta_or_nonteachable
- `blk_0358` — severe_underspecification: meta_or_nonteachable
- `blk_0359` — severe_underspecification: meta_or_nonteachable
- `blk_0364` — severe_underspecification: meta_or_nonteachable
- `blk_0365` — severe_underspecification: meta_or_nonteachable

### LT stage halted clusters

- `cluster_01` — lt_set_unreliable: only 0/3 runs produced parseable output

### Criterion-rubric stage halted LTs

- `cluster_02_lt_02` (Applying Democracy Models to U.S. Institutions) — rubric_unreliable: only 0/3 runs produced parseable output
- `cluster_03_lt_01` (Explaining Federalist Views on Central Government) — rubric_unreliable: no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'analyse'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'scoped'))]
- `cluster_03_lt_02` (Explaining Anti-Federalist Views on Democracy) — rubric_unreliable: no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'analyse'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'analyse'), ('competent_scope', 'unscoped'))]
- `cluster_04_lt_03` (Reasoning About Federal Power Expansion) — rubric_unreliable: no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'evaluate'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'none'), ('competent', 'within_limit', 'evaluate'), ('extending', 'within_limit', 'evaluate'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'evaluate'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'evaluate'), ('competent', 'within_limit', 'evaluate'), ('extending', 'within_limit', 'evaluate'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'evaluate'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'evaluate'), ('competent', 'within_limit', 'evaluate'), ('extending', 'within_limit', 'evaluate'), ('competent_scope', 'unscoped'))]
- `cluster_06_lt_01` (Explaining Separation of Powers and Checks) — rubric_unreliable: no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'recognise'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'unscoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'unscoped'))]
- `cluster_06_lt_02` (Analysing Separation of Powers in Context) — rubric_unreliable: only 0/3 runs produced parseable output
- `cluster_07_lt_02` (Analyzing Power Distribution Effects on Policy) — rubric_unreliable: no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'apply'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'describe'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'apply'), ('competent_scope', 'unscoped'))]
- `cluster_08_lt_01` (Connecting Historical Constitutional Debates to Current Policy) — rubric_unreliable: only 0/3 runs produced parseable output
- `cluster_08_lt_02` (Analysing Contemporary Issues Through Constitutional Lenses) — rubric_unreliable: only 0/3 runs produced parseable output
- `cluster_11_lt_02` (Explaining Political Concept Application) — rubric_unreliable: no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'apply'), ('emerging', 'within_limit', 'apply'), ('developing', 'within_limit', 'apply'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'apply'), ('competent_scope', 'scoped')), (('no_evidence', 'within_limit', 'apply'), ('emerging', 'within_limit', 'apply'), ('developing', 'within_limit', 'apply'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'apply'), ('competent_scope', 'unscoped')), (('no_evidence', 'within_limit', 'apply'), ('emerging', 'within_limit', 'recognise'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'scoped'))]
- `cluster_12_lt_02` (Supporting Arguments with Evidence) — rubric_unreliable: no structural signature reached 2/3 agreement; signatures=[(('no_evidence', 'within_limit', 'none'), ('emerging', 'within_limit', 'none'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'none'), ('competent_scope', 'unscoped')), (('no_evidence', 'within_limit', 'none'), ('emerging', 'within_limit', 'none'), ('developing', 'within_limit', 'describe'), ('competent', 'within_limit', 'describe'), ('extending', 'within_limit', 'describe'), ('competent_scope', 'unscoped'))]

### Supporting-components stage halted LTs

- `cluster_04_lt_02` (Connecting Incidents to Constitutional Inadequacies) — supporting_unreliable: no structural signature reached 2/3 agreement; signatures=[(('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
- `cluster_09_lt_01` (Identifying Political Principles and Institutions) — supporting_unreliable: no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]

