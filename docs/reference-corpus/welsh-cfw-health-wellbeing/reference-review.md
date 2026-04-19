# Reference review — wales-cfw-health-wellbeing-sow

Source snapshot: `docs/run-snapshots/2026-04-19-session-4a-5-wales-cfw-health-wellbeing-sow`. Classifier: `claude-haiku-4-5-20251001` at temperature 0.3 with 3x self-consistency.

## Progression structure (source-native)

- **source type:** `welsh_cfw_aole`
- **band count:** 5
- **bands (developmental order):** Progression Step 1, Progression Step 2, Progression Step 3, Progression Step 4, Progression Step 5
- **age range hint:** ages 3-16 (Welsh Government Curriculum for Wales overview, statutory under the Curriculum and Assessment (Wales) Act 2021)
- **detection confidence:** `high`
- **detection rationale:** URL host hwb.gov.wales with /curriculum-for-wales path — Welsh Curriculum for Wales uses Progression Steps 1-5 across ages 3-16 per Welsh Government statutory specification.

## Summary

- KUD items: **33**
- Halted KUD blocks: **6**
- Competency clusters: **9**
  - overall stability: `cluster_unstable`
- Learning Targets: **20**
  - knowledge types: Type 1=8, Type 2=6, Type 3=6
  - stability: {'stable': 13, 'lt_set_unstable': 7}
- Band-statement sets (Type 1/2): **11**
  - stability: {'band_statements_unstable': 5, 'stable': 6}
- Observation indicator sets (Type 3): **5**
  - stability: {'observation_indicators_unstable': 3, 'stable': 2}
- Halted at any stage: 10
- Pipeline: all KUD halting gates passed

## Competencies

### Physical Health and Well-being — `cluster_01`

**Definition.** The ability to understand factors supporting physical health and develop confidence, motivation, and competence to lead healthy and active lifestyles.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L9-12. **KUD items:** 4.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0007_item_01` | Type 1 | understand | Developing physical health and well-being has lifelong benefits. |
| `blk_0010_item_01` | Type 1 | know | Knowledge and understanding of factors that support physical health and well-being, including the relationship between physical activity, nutrition, sleep, and overall health outcomes. |
| `blk_0010_item_02` | Type 1 | do_skill | Physical competence in movement, exercise, and activity skills appropriate to age and context. |
| `blk_0010_item_03` | Type 3 | do_disposition | Confidence and motivation to lead healthy and active lifestyles across different contexts and over time. |

#### Learning Targets

##### Understanding Health and Well-being Factors — `cluster_01_lt_01`

**Definition.** I can explain how physical activity, nutrition, sleep, and other factors support physical health and well-being outcomes.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0007_item_01`, `blk_0010_item_01`

_No band statements produced._

##### Demonstrating Physical Movement Competence — `cluster_01_lt_02`

**Definition.** I can perform movement, exercise, and activity skills appropriate to my age and context with increasing competence.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0010_item_02`

**Band progression** — stability `band_statements_unstable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can perform basic movement skills with adult support and guidance. |
| Progression Step 2 | I can perform fundamental movement skills with increasing independence and control. |
| Progression Step 3 | I can perform movement skills with precision and adapt them to different contexts. |
| Progression Step 4 | I can perform complex movement sequences and explain how to improve my technique. |
| Progression Step 5 | I can perform and evaluate movement skills across varied contexts, justifying choices made. |

##### Sustaining Motivation for Active Healthy Living — `cluster_01_lt_03`

**Definition.** The student sustains confidence and motivation to engage in healthy and active behaviours across different contexts and over time.

**Knowledge type:** Type 3. **Assessment route:** `multi_informant_observation`. **Stability:** `stable`.

**Prerequisites:** `Understanding Health and Well-being Factors`, `Demonstrating Physical Movement Competence`

**KUD items covered:** `blk_0010_item_03`

**Observation protocol** — stability `observation_indicators_unstable`, Mode 3 gate **PASS**.

_Prerequisites (knowledge-contingent Type 3):_ `Understanding Health and Well-being Factors`, `Demonstrating Physical Movement Competence`

**Progression Step 1**

- The student engages in movement activities when invited by an adult and shows visible enjoyment through smiling or continued participation.
- The student returns to the same physical activity or play space on multiple occasions within a week when given the opportunity.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 1):_ Tell me about a time this term when you tried something new. What did you do, and how did it feel?

**Progression Step 2**

- The student initiates participation in familiar active play or movement activities without adult prompting and persists for several minutes.
- The student expresses preference for certain physical activities and seeks them out during free choice time.
- The student attempts new movement challenges after observing peers or receiving encouragement, showing willingness to try despite initial hesitation.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 2):_ Describe one thing you have noticed about yourself this term. When does it happen, and when does it not?

**Progression Step 3**

- The student independently chooses to engage in active play or structured physical activity and sustains effort across a range of different settings.
- The student demonstrates resilience when finding a movement task difficult, adjusting their approach or asking for support rather than withdrawing.
- The student talks positively about their own physical abilities and expresses interest in improving specific skills through practice.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 3):_ Compare what you have noticed in yourself with what your teacher or family has noticed. Where do these accounts agree, and where do they differ?

**Progression Step 4**

- The student maintains commitment to regular physical activity across different contexts and weathers, showing consistent engagement even when motivation fluctuates.
- The student seeks out new physical challenges and activities beyond their immediate experience, exploring different sports or movement forms with sustained interest.
- The student reflects on their own progress in physical activities and sets personal goals for improvement, demonstrating intrinsic motivation to develop competence.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 4):_ Analyse a pattern you can see in yourself across two or more different settings this term. What changes across settings, and why do you think it changes?

**Progression Step 5**

- The student sustains active healthy behaviours as a valued part of their identity and daily routine, maintaining engagement across varied contexts and over extended periods without external reward.
- The student advocates for active play and healthy movement in their peer group and community, encouraging others and modelling sustained participation.
- The student independently adapts their approach to physical activity based on changing circumstances, personal interests, and evolving goals, demonstrating flexible and self-directed motivation.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 5):_ Trace how your understanding of yourself in this area has developed over time. What values now guide how you act, and what would you still like to develop?

**Parent / caregiver prompts**

- What physical activities or types of movement does your child choose to do at home or in the community without being asked, and how often do you notice them returning to these activities?
- When your child finds a physical activity challenging or feels they are not good at something, what do you notice about how they respond—do they keep trying, ask for help, or tend to give up?
- How does your child talk about their own body and physical abilities? Do you hear them express confidence, set goals for themselves, or show interest in getting better at particular activities?

**Developmental conversation protocol.** The synthesising conversation brings together observations of the student's self-initiated physical engagement, their responses to challenge and setback, and their emerging sense of themselves as an active person. The teacher, student, and optionally parent reflect on patterns of sustained motivation across different contexts and discuss what activities and conditions support the student's confidence and persistence in healthy, active behaviours.

### Self-Care and Respect for Self and Others — `cluster_02`

**Definition.** The ability to develop and sustain positive, informed behaviours that care for and respect self and others, supporting well-being and sense of self-worth.

**Dominant knowledge type:** Type 3. **Stability:** `stable`. **Source lines:** L11-11. **KUD items:** 2.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0009_item_01` | Type 3 | do_disposition | Care for and respect themselves and others as a sustained default orientation across contexts. |
| `blk_0009_item_02` | Type 1 | understand | Positive, informed behaviours that care for and respect self and others support learners' sense of self-worth, their overall mood and energy levels. |

#### Learning Targets

##### Caring for Self and Others — `cluster_02_lt_01`

**Definition.** The student enacts care for and respect toward themselves and others as a sustained default orientation across contexts.

**Knowledge type:** Type 3. **Assessment route:** `multi_informant_observation`. **Stability:** `stable`.

**KUD items covered:** `blk_0009_item_01`

**Observation protocol** — stability `stable`, Mode 3 gate **PASS**.

**Progression Step 1**

- The student accepts help with personal hygiene routines when prompted by an adult.
- The student responds to gentle reminders to use kind words or gentle touch with peers during structured activities.
- The student shows awareness of basic comfort needs by communicating when hungry, tired, or uncomfortable.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 1):_ Tell me about a time this term when you tried something new. What did you do, and how did it feel?

**Progression Step 2**

- The student initiates simple self-care tasks such as washing hands or tidying personal belongings with occasional reminders.
- The student notices when a peer is upset and seeks adult guidance on how to help or comfort them.
- The student demonstrates respect for others' belongings by asking permission before using them and returning items when asked.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 2):_ Describe one thing you have noticed about yourself this term. When does it happen, and when does it not?

**Progression Step 3**

- The student manages personal hygiene and grooming routines independently and recognises the connection between self-care and feeling well.
- The student shows consideration for others by offering help or comfort to peers without prompting in familiar situations.
- The student respects personal boundaries and responds appropriately when others express discomfort with physical contact or shared space.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 3):_ Compare what you have noticed in yourself with what your teacher or family has noticed. Where do these accounts agree, and where do they differ?

**Progression Step 4**

- The student makes deliberate choices about diet, rest, and physical activity that reflect awareness of their own wellbeing across different settings.
- The student actively listens to others' concerns and adjusts their behaviour to show respect for different perspectives and emotional needs.
- The student takes responsibility for maintaining a safe and respectful environment by addressing unkind behaviour or supporting peers who are excluded or struggling.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 4):_ Analyse a pattern you can see in yourself across two or more different settings this term. What changes across settings, and why do you think it changes?

**Progression Step 5**

- The student sustains self-care practices that support physical, emotional, and social wellbeing and reflects on how these choices affect their learning and relationships.
- The student demonstrates empathy and respect across unfamiliar contexts by recognising and responding thoughtfully to the needs and dignity of others, including those from different backgrounds or experiences.
- The student advocates for respectful treatment of themselves and others and takes initiative to challenge disrespect or harm when they encounter it.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 5):_ Trace how your understanding of yourself in this area has developed over time. What values now guide how you act, and what would you still like to develop?

**Parent / caregiver prompts**

- What have you noticed about how your child looks after themselves at home—for example, their willingness to wash, dress, or eat without being asked, and how they talk about feeling healthy or unwell?
- When your child is with family or friends, how do they respond when someone is sad, hurt, or upset? Do they show concern or try to help, and how do they treat others' feelings and belongings?
- Have you seen your child stand up for themselves or others when something feels unfair or unkind, or ask questions about why people treat each other differently?

**Developmental conversation protocol.** The teacher, student, and optionally parent reflect together on specific moments when the student showed care for themselves or others, exploring what prompted that care, how it felt, and how the student might sustain or extend that orientation across new situations.

##### Understanding Self-Care Impact — `cluster_02_lt_02`

**Definition.** I can explain how positive, informed behaviours that care for and respect self and others support well-being and sense of self-worth.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0009_item_02`

_No band statements produced._

### Mental Health and Emotional Well-being — `cluster_03`

**Definition.** The ability to understand connections between experiences and emotional well-being, recognise emotions as fluid, and develop strategies to regulate emotions and seek support.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L13-14. **KUD items:** 3.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0011_item_01` | Type 1 | understand | How we process and respond to our experiences affects our mental health and emotional well-being. |
| `blk_0012_item_01` | Type 1 | understand | Connections exist between experiences, mental health and emotional well-being. |
| `blk_0012_item_02` | Type 3 | do_disposition | Recognise that feelings and emotions are neither fixed nor consistent, and hold this recognition as a sustained orientation across contexts and over time. |

#### Learning Targets

##### Connecting Experiences to Emotional Well-being — `cluster_03_lt_01`

**Definition.** I can explain how experiences and emotional responses influence mental health and well-being.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0011_item_01`, `blk_0012_item_01`

**Band progression** — stability `band_statements_unstable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify how my feelings change in response to different experiences. |
| Progression Step 2 | I can describe connections between my experiences and how I feel emotionally. |
| Progression Step 3 | I can explain how specific experiences affect my emotional responses and well-being. |
| Progression Step 4 | I can analyse how my emotional responses to experiences influence my overall mental health. |
| Progression Step 5 | I can evaluate and justify how patterns of experiences shape my emotional well-being across different contexts. |

##### Recognising Emotions as Fluid — `cluster_03_lt_02`

**Definition.** The student recognises that emotions and feelings are dynamic and changeable, sustaining this understanding across varied contexts and time.

**Knowledge type:** Type 3. **Assessment route:** `multi_informant_observation`. **Stability:** `stable`.

**Prerequisites:** `Connecting Experiences to Emotional Well-being`

**KUD items covered:** `blk_0012_item_02`

**Observation protocol** — stability `observation_indicators_unstable`, Mode 3 gate **PASS**.

_Prerequisites (knowledge-contingent Type 3):_ `Connecting Experiences to Emotional Well-being`

**Progression Step 1**

- The student names a feeling they are experiencing in the moment when prompted by an adult.
- The student notices when their feeling changes from one activity to another and mentions it with support.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 1):_ Tell me about a time this term when you tried something new. What did you do, and how did it feel?

**Progression Step 2**

- The student describes how their feeling shifted during a familiar activity without being asked.
- The student recognises that the same situation can produce different feelings at different times.
- The student uses language that acknowledges feelings are not permanent, such as 'I was sad but now I'm happy'.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 2):_ Describe one thing you have noticed about yourself this term. When does it happen, and when does it not?

**Progression Step 3**

- The student explains how their emotions changed in response to events during their day, showing awareness of the sequence.
- The student identifies that their feelings about a person or activity can vary depending on circumstances.
- The student reflects on how the same emotion can feel different in intensity or expression across different moments.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 3):_ Compare what you have noticed in yourself with what your teacher or family has noticed. Where do these accounts agree, and where do they differ?

**Progression Step 4**

- The student articulates how their emotional responses shift across unfamiliar contexts and demonstrates flexibility in managing those shifts.
- The student recognises patterns in how their emotions change over time and discusses what influences those patterns.
- The student applies the understanding that emotions are fluid to support peers who are experiencing difficult feelings.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 4):_ Analyse a pattern you can see in yourself across two or more different settings this term. What changes across settings, and why do you think it changes?

**Progression Step 5**

- The student sustains the understanding that emotions are dynamic across extended periods and varied social, academic, and personal contexts.
- The student independently reflects on how their emotional landscape evolves and uses this insight to make choices about their own well-being.
- The student demonstrates nuanced recognition that emotions can coexist, layer, or transform, and communicates this complexity to others.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 5):_ Trace how your understanding of yourself in this area has developed over time. What values now guide how you act, and what would you still like to develop?

**Parent / caregiver prompts**

- Have you noticed your child describing their feelings differently at different times of the day, or talking about how their mood changed during an activity?
- When your child has felt upset or frustrated, have they mentioned that the feeling got better, or talked about times when they felt differently about the same thing?
- Does your child notice or comment on how their emotions shift in different situations, such as at home versus with friends, or before and after something they enjoy?

**Developmental conversation protocol.** The synthesising conversation between teacher, student, and optionally parent explores specific moments when the student noticed their emotions changing, what they observed about those shifts, and how they are beginning to apply this understanding to navigate their emotional experiences across different settings and relationships.

### Communication About Mental Health — `cluster_04`

**Definition.** The ability to communicate feelings appropriately and sustain a default orientation toward normalising talk about mental health and emotional well-being.

**Dominant knowledge type:** Type 2. **Stability:** `stable`. **Source lines:** L23-23. **KUD items:** 2.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0014_item_01` | Type 1 | do_skill | Communicate their feelings in ways appropriate to context and audience. |
| `blk_0014_item_02` | Type 3 | do_disposition | Sustain a default orientation toward normalising talk about mental health and emotional well-being across peer interactions and community contexts. |

#### Learning Targets

##### Communicating Feelings Appropriately — `cluster_04_lt_01`

**Definition.** I can communicate my feelings in ways that are appropriate to the context and audience.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0014_item_01`

_No band statements produced._

##### Normalising Mental Health Talk — `cluster_04_lt_02`

**Definition.** The student sustains a default orientation toward normalising talk about mental health and emotional well-being across peer interactions and community contexts.

**Knowledge type:** Type 3. **Assessment route:** `multi_informant_observation`. **Stability:** `stable`.

**Prerequisites:** `Communicating Feelings Appropriately`

**KUD items covered:** `blk_0014_item_02`

**Observation protocol** — stability `stable`, Mode 3 gate **PASS**.

_Prerequisites (knowledge-contingent Type 3):_ `Communicating Feelings Appropriately`

**Progression Step 1**

- The student uses simple words to name feelings when prompted by an adult in one-to-one or small group settings.
- The student listens without visible discomfort when a peer or adult mentions feeling sad, worried, or happy in everyday conversation.
- The student responds to direct questions about how they feel by naming a basic emotion rather than deflecting or staying silent.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 1):_ Tell me about a time this term when you tried something new. What did you do, and how did it feel?

**Progression Step 2**

- The student initiates brief mentions of their own feelings or mood during informal peer interactions without adult prompting.
- The student asks a peer or adult a simple question about how they are feeling in response to observing a change in their behaviour or expression.
- The student participates in structured circle time or group discussions about feelings and emotions without withdrawing or showing embarrassment.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 2):_ Describe one thing you have noticed about yourself this term. When does it happen, and when does it not?

**Progression Step 3**

- The student brings up their own emotional experiences or worries in conversation with peers or trusted adults across different settings, showing it as a normal part of talking.
- The student notices when a peer seems upset or withdrawn and asks them directly about their feelings, demonstrating curiosity rather than avoidance.
- The student uses emotional language naturally when describing their day or experiences, integrating feelings talk into everyday storytelling.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 3):_ Compare what you have noticed in yourself with what your teacher or family has noticed. Where do these accounts agree, and where do they differ?

**Progression Step 4**

- The student sustains open conversation about mental health and emotional well-being with peers, including discussing stress, anxiety, or low mood without minimising or joking it away.
- The student responds to a peer's emotional disclosure by validating their feelings and continuing the conversation, rather than changing the subject or offering quick reassurance.
- The student references their own experiences with difficult emotions or mental health in group settings, modelling that such talk is ordinary and acceptable.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 4):_ Analyse a pattern you can see in yourself across two or more different settings this term. What changes across settings, and why do you think it changes?

**Progression Step 5**

- The student consistently initiates or sustains conversations about mental health and emotional well-being across unfamiliar peer groups and community contexts, treating it as a routine part of connection.
- The student actively encourages peers to talk about their feelings and well-being by asking thoughtful follow-up questions and demonstrating genuine interest, even when the peer initially hesitates.
- The student reflects on their own mental health and emotional patterns in conversation with others, connecting their feelings to situations or choices, and inviting peers to do the same.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 5):_ Trace how your understanding of yourself in this area has developed over time. What values now guide how you act, and what would you still like to develop?

**Parent / caregiver prompts**

- When your child talks about their day or their feelings at home, do you notice them mentioning emotions or worries without you having to ask? What kinds of feelings do they bring up naturally?
- Have you observed your child asking a friend or family member how they are feeling, or showing interest in someone else's mood or well-being without being told to do so?
- Does your child seem comfortable talking about difficult feelings like worry, sadness, or frustration in everyday conversation, or do they tend to avoid or change the subject when emotions come up?

**Developmental conversation protocol.** The synthesising conversation between teacher, student, and optionally parent explores the student's comfort and frequency in bringing up feelings and mental health in peer and family contexts, and identifies settings where the student feels safe normalising such talk. The conversation also examines whether the student is noticing and responding to others' emotional cues, and what language or prompts help sustain open emotional conversation.

### Informed Decision-Making — `cluster_05`

**Definition.** The ability to understand how decisions impact self and others, analyse influencing factors, and make informed decisions by considering implications and risks.

**Dominant knowledge type:** Type 2. **Stability:** `stable`. **Source lines:** L24-26. **KUD items:** 6.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0015_item_01` | Type 1 | understand | Our decision-making impacts on the quality of our lives and the lives of others. |
| `blk_0016_item_01` | Type 1 | understand | How decisions and actions impact on themselves, on others and on wider society, both now and in the future |
| `blk_0016_item_02` | Type 1 | understand | The factors that influence decision-making |
| `blk_0016_item_03` | Type 2 | do_skill | Make more informed and considered decisions by analysing how decisions and actions impact on themselves, on others and on wider society, and by considering the factors that influence decision-making |
| `blk_0017_item_01` | Type 2 | do_skill | Consider decision-making in terms of possible implications, including risks, for themselves and others. |
| `blk_0017_item_02` | Type 1 | understand | The importance of their contributions to collective decision-making processes. |

#### Learning Targets

##### Analysing Decision Impacts and Influencing Factors — `cluster_05_lt_01`

**Definition.** I can analyse how decisions and actions impact myself, others, and society, and identify the factors that influence decision-making.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `lt_set_unstable`.

**KUD items covered:** `blk_0015_item_01`, `blk_0016_item_01`, `blk_0016_item_02`, `blk_0016_item_03`

**Band progression** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify simple consequences of my own decisions on myself and others around me. |
| Progression Step 2 | I can describe how decisions affect different people and recognise some factors that influence my choices. |
| Progression Step 3 | I can explain how decisions impact myself, others, and society, and analyse key factors influencing decision-making. |
| Progression Step 4 | I can evaluate complex decision impacts across multiple contexts and justify how various influencing factors shape outcomes. |
| Progression Step 5 | I can analyse decision impacts and influencing factors in unfamiliar situations and apply insights to inform future choices. |

##### Evaluating Implications and Risks in Decisions — `cluster_05_lt_02`

**Definition.** I can evaluate the possible implications and risks of decisions for myself and others before deciding.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `lt_set_unstable`.

**Prerequisites:** `Analysing Decision Impacts and Influencing Factors`

**KUD items covered:** `blk_0017_item_01`

**Band progression** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify simple consequences of my choices with adult support. |
| Progression Step 2 | I can describe possible outcomes of decisions affecting myself and others. |
| Progression Step 3 | I can analyse risks and benefits of decisions in familiar situations independently. |
| Progression Step 4 | I can evaluate implications and risks of decisions, considering multiple perspectives and outcomes. |
| Progression Step 5 | I can evaluate complex implications and risks across unfamiliar contexts, justifying my reasoning. |

##### Valuing Collective Decision-Making Contributions — `cluster_05_lt_03`

**Definition.** The student practises recognising and valuing their own contributions to shared decision-making processes across different contexts.

**Knowledge type:** Type 3. **Assessment route:** `multi_informant_observation`. **Stability:** `lt_set_unstable`.

**Prerequisites:** `Analysing Decision Impacts and Influencing Factors`

**KUD items covered:** `blk_0017_item_02`

**Observation protocol** — stability `observation_indicators_unstable`, Mode 3 gate **PASS**.

_Prerequisites (knowledge-contingent Type 3):_ `Analysing Decision Impacts and Influencing Factors`

**Progression Step 1**

- The student offers a simple idea or preference when invited to contribute to a group decision in structured settings.
- The student notices when their suggestion has been included in a shared choice and shows awareness that their input mattered.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 1):_ Tell me about a time this term when you tried something new. What did you do, and how did it feel?

**Progression Step 2**

- The student volunteers contributions to group decisions without prompting and listens when others share their ideas.
- The student recognises that different people in the group have different views and accepts when the group chooses something other than their own suggestion.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 2):_ Describe one thing you have noticed about yourself this term. When does it happen, and when does it not?

**Progression Step 3**

- The student explains why their contribution matters to a shared decision and asks questions about others' ideas before the group decides.
- The student reflects on how their input influenced what the group chose and identifies moments when their thinking changed because of someone else's contribution.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 3):_ Compare what you have noticed in yourself with what your teacher or family has noticed. Where do these accounts agree, and where do they differ?

**Progression Step 4**

- The student actively builds on others' contributions during decision-making and articulates how collective input strengthens the final choice.
- The student seeks out opportunities to contribute to decisions in unfamiliar groups and adapts their approach based on how that particular group works.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 4):_ Analyse a pattern you can see in yourself across two or more different settings this term. What changes across settings, and why do you think it changes?

**Progression Step 5**

- The student initiates and sustains collaborative decision-making processes across different contexts, consistently valuing and integrating diverse perspectives into shared outcomes.
- The student demonstrates sustained commitment to collective decision-making by reflecting critically on their own contributions, recognising power dynamics, and actively ensuring that quieter voices are heard and valued.

_Self-reflection prompt (calibrated to this source's own developmental expectations at Progression Step 5):_ Trace how your understanding of yourself in this area has developed over time. What values now guide how you act, and what would you still like to develop?

**Parent / caregiver prompts**

- When your child is involved in family decisions, such as planning an outing or choosing what to do together, what have you noticed about whether they offer their ideas and how they respond when the family chooses something different from what they suggested?
- Have you seen your child ask questions about why other family members want something, or change their mind because of what someone else said? What does that look like?
- In situations where your child is part of a group outside the family, such as with friends or in a club, what have you noticed about whether they speak up, listen to others, and seem to value what different people bring to decisions?

**Developmental conversation protocol.** The synthesising conversation brings together observations of the student's contributions across different decision-making contexts, explores what the student notices about their own role and the roles of others, and considers how the student's understanding of collective value has grown. The conversation may include reflection on a specific decision the student participated in and what they learned from hearing different perspectives.

### Career Pathway Decision-Making — `cluster_06`

**Definition.** The ability to understand that career pathway decisions have significant lifelong consequences and make informed choices about future pathways.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L27-27. **KUD items:** 1.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0018_item_01` | Type 1 | understand | Career pathway decisions have significant lifelong consequences for learners. |

#### Learning Targets

##### Identifying Consequences of Career Choices — `cluster_06_lt_01`

**Definition.** I can identify and describe significant lifelong consequences of career pathway decisions across personal, financial, and social domains.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `lt_set_unstable`.

**KUD items covered:** `blk_0018_item_01`

**Band progression** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify one immediate consequence of a career choice in my own life. |
| Progression Step 2 | I can describe consequences of career choices across personal and financial domains with support. |
| Progression Step 3 | I can identify and describe multiple consequences of career choices across personal, financial, and social domains. |
| Progression Step 4 | I can explain how career pathway decisions create interconnected lifelong consequences across personal, financial, and social domains. |
| Progression Step 5 | I can analyse and justify the significance of career choice consequences across domains in unfamiliar contexts. |

##### Making Informed Career Pathway Decisions — `cluster_06_lt_02`

**Definition.** I can evaluate multiple career pathways and justify my choices by reasoning about their alignment with my values, abilities, and long-term goals.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `lt_set_unstable`.

**Prerequisites:** `Identifying Consequences of Career Choices`

**KUD items covered:** `blk_0018_item_01`

**Band progression** — stability `band_statements_unstable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify my interests and describe how they connect to different career pathways. |
| Progression Step 2 | I can compare career pathways and explain which align with my abilities and interests. |
| Progression Step 3 | I can evaluate career pathways against my values and abilities, and justify my preferences with reasoning. |
| Progression Step 4 | I can analyse multiple career pathways, evaluate their fit with my values and long-term goals, and justify my reasoning. |
| Progression Step 5 | I can evaluate complex career pathways, justify choices by reasoning about alignment with values, abilities, and long-term goals across contexts. |

### Understanding Social Influences — `cluster_07`

**Definition.** The ability to understand how social influences shape identity, values and behaviours, and critically analyse how norms and values develop across cultures.

**Dominant knowledge type:** Type 1. **Stability:** `stable`. **Source lines:** L28-40. **KUD items:** 6.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0019_item_01` | Type 1 | understand | How we engage with social influences shapes who we are and affects our health and well-being. |
| `blk_0020_item_01` | Type 1 | understand | Social influences are comprised of rules, social norms, attitudes and values that are created and reinforced by different social groups. |
| `blk_0020_item_02` | Type 1 | understand | Social influences affect identity, values, behaviours and health and well-being, often without our being aware of it. |
| `blk_0020_item_03` | Type 1 | understand | We experience social influences through interaction with social groups. |
| `blk_0021_item_01` | Type 1 | understand | How norms and values develop within cultures and across different cultural contexts |
| `blk_0021_item_02` | Type 2 | do_skill | Engage critically with social influences within own culture and those of others to analyse how own behaviours, relationships and experiences are shaped |

#### Learning Targets

##### Identifying Social Influences on Identity — `cluster_07_lt_01`

**Definition.** I can identify how social influences shape identity, values, behaviours and well-being.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `stable`.

**KUD items covered:** `blk_0019_item_01`, `blk_0020_item_01`, `blk_0020_item_02`, `blk_0020_item_03`

**Band progression** — stability `band_statements_unstable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify people and groups that influence how I think and behave. |
| Progression Step 2 | I can describe how family, friends, and community shape my values and choices. |
| Progression Step 3 | I can explain how different social influences affect my identity, behaviours, and well-being. |
| Progression Step 4 | I can analyse how multiple social influences interact to shape identity and justify my responses. |
| Progression Step 5 | I can evaluate social influences on identity across different contexts and explain their impact on well-being. |

##### Analysing Cultural Development of Norms — `cluster_07_lt_02`

**Definition.** I can analyse how norms and values develop within and across different cultural contexts.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Identifying Social Influences on Identity`

**KUD items covered:** `blk_0021_item_01`, `blk_0021_item_02`

**Band progression** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify norms and values that exist in my own family and community. |
| Progression Step 2 | I can describe how norms and values differ between two familiar cultural contexts. |
| Progression Step 3 | I can explain how norms and values develop over time within a specific cultural group. |
| Progression Step 4 | I can analyse how norms and values are shaped by historical, social, and environmental factors across cultures. |
| Progression Step 5 | I can evaluate how norms and values develop and change across different cultural contexts and justify cultural perspectives. |

### Healthy Relationships and Belonging — `cluster_08`

**Definition.** The ability to understand the importance of healthy relationships, value belonging and connection, and develop sustained capacity to form, nurture and maintain relationships.

**Dominant knowledge type:** Type 3. **Stability:** `stable`. **Source lines:** L41-45. **KUD items:** 7.

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0022_item_01` | Type 1 | understand | Healthy relationships are fundamental to our well-being. |
| `blk_0023_item_01` | Type 1 | understand | Feelings of belonging and connection that come from healthy relationships have a powerful effect on health and well-being. |
| `blk_0023_item_02` | Type 3 | do_disposition | Value how feelings of belonging and connection that come from healthy relationships contribute to health and well-being. |
| `blk_0025_item_01` | Type 1 | understand | Throughout their lives, learners will experience a range of relationships. |
| `blk_0025_item_02` | Type 3 | do_disposition | Learners develop their abilities to form, nurture and maintain relationships as a sustained orientation across contexts. |
| `blk_0026_item_01` | Type 1 | understand | Healthy relationships are vital for a healthy body and mind, allowing us to thrive. |
| `blk_0026_item_02` | Type 3 | do_disposition | Prioritise and enact healthy relationships as a sustained default orientation across contexts, recognising their importance for wellbeing. |

#### Learning Targets

##### Understanding Healthy Relationships and Belonging — `cluster_08_lt_01`

**Definition.** I can explain why healthy relationships and belonging are fundamental to wellbeing and health.

**Knowledge type:** Type 1. **Assessment route:** `rubric_with_clear_criteria`. **Stability:** `lt_set_unstable`.

**KUD items covered:** `blk_0022_item_01`, `blk_0023_item_01`, `blk_0025_item_01`, `blk_0026_item_01`

**Band progression** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify people who care for me and describe how they make me feel safe. |
| Progression Step 2 | I can recognise what makes a relationship healthy and explain why belonging to a group matters. |
| Progression Step 3 | I can describe how healthy relationships and belonging contribute to my physical and emotional wellbeing. |
| Progression Step 4 | I can explain how healthy relationships and belonging support wellbeing across different areas of my life. |
| Progression Step 5 | I can justify why healthy relationships and belonging are fundamental to overall wellbeing and health in varied contexts. |

##### Valuing and Prioritising Healthy Relationships — `cluster_08_lt_02`

**Definition.** The student enacts a sustained orientation to form, nurture and maintain healthy relationships across contexts.

**Knowledge type:** Type 3. **Assessment route:** `multi_informant_observation`. **Stability:** `lt_set_unstable`.

**Prerequisites:** `Understanding Healthy Relationships and Belonging`

**KUD items covered:** `blk_0023_item_02`, `blk_0025_item_02`, `blk_0026_item_02`

_No observation indicator set produced._

### Recognising and Responding to Unhealthy Relationships — `cluster_09`

**Definition.** The ability to recognise unhealthy relationships and evaluate appropriate support resources and strategies to keep safe and seek help.

**Dominant knowledge type:** Type 2. **Stability:** `cluster_unstable`. **Source lines:** L43-43. **KUD items:** 2.

_Stability diagnostics:_
- unmatched_in_run2
- unmatched_in_run3

#### KUD items

| Item ID | Type | Column | Content |
|---|---|---|---|
| `blk_0024_item_01` | Type 2 | do_skill | Recognise when relationships are unhealthy by analysing relationship dynamics and identifying warning signs. |
| `blk_0024_item_02` | Type 2 | do_skill | Evaluate and select appropriate support resources and strategies to keep safe and seek support for themselves and others when relationships are unhealthy. |

#### Learning Targets

##### Analysing Relationship Dynamics for Warning Signs — `cluster_09_lt_01`

**Definition.** I can analyse relationship dynamics and identify warning signs that indicate a relationship is unhealthy.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**KUD items covered:** `blk_0024_item_01`

**Band progression** — stability `stable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify obvious warning signs in relationships with adult support and guidance. |
| Progression Step 2 | I can describe warning signs in relationship dynamics and explain why they are concerning. |
| Progression Step 3 | I can analyse relationship dynamics to identify multiple warning signs and explain their impact. |
| Progression Step 4 | I can analyse complex relationship dynamics, identify subtle warning signs, and justify why they indicate unhealthy patterns. |
| Progression Step 5 | I can analyse relationship dynamics across contexts, identify interconnected warning signs, and evaluate their significance independently. |

##### Evaluating Support Resources and Safety Strategies — `cluster_09_lt_02`

**Definition.** I can evaluate and select appropriate support resources and strategies to keep safe and seek help when relationships are unhealthy.

**Knowledge type:** Type 2. **Assessment route:** `reasoning_quality_rubric`. **Stability:** `stable`.

**Prerequisites:** `Analysing Relationship Dynamics for Warning Signs`

**KUD items covered:** `blk_0024_item_02`

**Band progression** — stability `band_statements_unstable`, quality gate **PASS**.

| Band | Statement |
|---|---|
| Progression Step 1 | I can identify support resources and safety strategies with adult guidance. |
| Progression Step 2 | I can describe how different support resources and strategies help keep me safe. |
| Progression Step 3 | I can compare support resources and strategies to select appropriate ones for unhealthy situations. |
| Progression Step 4 | I can evaluate support resources and strategies, explaining why they are effective for different unhealthy relationships. |
| Progression Step 5 | I can evaluate and justify selection of support resources and strategies across varied unhealthy relationship contexts. |

## Halted items

### KUD halted blocks

- `blk_0002` — severe_underspecification: meta_or_nonteachable
- `blk_0003` — severe_underspecification: meta_or_nonteachable
- `blk_0005` — severe_underspecification: meta_or_nonteachable
- `blk_0006` — severe_underspecification: meta_or_nonteachable
- `blk_0008` — classification_unreliable: no signature achieved 2/3 agreement across runs; observed signatures: [('items', (('understand', 'Type 1'), ('understand', 'Type 1'))), ('items', (('know', 'Type 1'), ('know', 'Type 1'), ('understand', 'Type 1'))), ('items', (('know', 'Type 1'), ('understand', 'Type 1'), ('understand', 'Type 1')))]
- `blk_0013` — classification_unreliable: no signature achieved 2/3 agreement across runs; observed signatures: [('items', (('do_disposition', 'Type 3'), ('understand', 'Type 1'))), ('items', (('do_disposition', 'Type 3'), ('do_disposition', 'Type 3'), ('understand', 'Type 1'), ('understand', 'Type 1'))), ('items', (('do_disposition', 'Type 3'), ('do_disposition', 'Type 3'), ('do_skill', 'Type 1'), ('do_skill', 'Type 2'), ('understand', 'Type 1')))]

### Band-statement stage halted LTs

- `cluster_01_lt_01` (Understanding Health and Well-being Factors) — band_statements_unreliable: no word-count-class signature reached 2/3 agreement; signatures=[(('Progression Step 1', 'medium'), ('Progression Step 2', 'medium'), ('Progression Step 3', 'medium'), ('Progression Step 4', 'medium'), ('Progression Step 5', 'long')), (('Progression Step 1', 'short'), ('Progression Step 2', 'short'), ('Progression Step 3', 'medium'), ('Progression Step 4', 'medium'), ('Progression Step 5', 'medium')), (('Progression Step 1', 'medium'), ('Progression Step 2', 'medium'), ('Progression Step 3', 'medium'), ('Progression Step 4', 'medium'), ('Progression Step 5', 'medium'))]
- `cluster_02_lt_02` (Understanding Self-Care Impact) — band_statements_unreliable: no word-count-class signature reached 2/3 agreement; signatures=[(('Progression Step 1', 'medium'), ('Progression Step 2', 'medium'), ('Progression Step 3', 'long'), ('Progression Step 4', 'long'), ('Progression Step 5', 'long')), (('Progression Step 1', 'short'), ('Progression Step 2', 'medium'), ('Progression Step 3', 'medium'), ('Progression Step 4', 'medium'), ('Progression Step 5', 'long')), (('Progression Step 1', 'medium'), ('Progression Step 2', 'medium'), ('Progression Step 3', 'medium'), ('Progression Step 4', 'long'), ('Progression Step 5', 'long'))]
- `cluster_04_lt_01` (Communicating Feelings Appropriately) — band_statements_gate_failed: 1 format/quality failures
  - failures: ['Progression Step 2:no_observable_verb']

### Observation-indicator stage halted LTs

- `cluster_08_lt_02` (Valuing and Prioritising Healthy Relationships) — observation_indicators_unreliable: no signature reached 2/3 agreement; signatures=[(('Progression Step 1', 3), ('Progression Step 2', 3), ('Progression Step 3', 3), ('Progression Step 4', 3), ('Progression Step 5', 3), ('parents', 3)), (('Progression Step 1', 2), ('Progression Step 2', 2), ('Progression Step 3', 3), ('Progression Step 4', 3), ('Progression Step 5', 3), ('parents', 3)), (('Progression Step 1', 2), ('Progression Step 2', 3), ('Progression Step 3', 3), ('Progression Step 4', 3), ('Progression Step 5', 3), ('parents', 3))]

