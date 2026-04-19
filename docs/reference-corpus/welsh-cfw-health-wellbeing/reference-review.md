# Reference review — wales-cfw-health-wellbeing-sow

Source snapshot: `docs/run-snapshots/2026-04-19-session-4a-5-wales-cfw-health-wellbeing-sow`. Classifier: `claude-haiku-4-5-20251001` at temperature 0.3 with 3x self-consistency.

## Progression structure (source-native)

- **source type:** `welsh_cfw_aole`
- **band count:** 5
- **bands (developmental order):** Progression Step 1, Progression Step 2, Progression Step 3, Progression Step 4, Progression Step 5
- **age range hint:** ages 3-16 (Welsh Government Curriculum for Wales overview, statutory under the Curriculum and Assessment (Wales) Act 2021)
- **detection confidence:** `high`
- **detection rationale:** URL host hwb.gov.wales with /curriculum-for-wales path — Welsh Curriculum for Wales uses Progression Steps 1-5 across ages 3-16 per Welsh Government statutory specification.

**Progression philosophy.**

> Progression Steps are reference waypoints, not annual targets. Learners progress at different rates and may be at different Progression Steps for different Areas of Learning and Experience. Each Step describes what learners are typically expected to achieve by the associated age; they are not grade-level checklists. Per Welsh Government statutory specification under the Curriculum and Assessment (Wales) Act 2021.

### Per-band developmental index

| Band | Approximate age | Approximate grade/year | Developmental descriptor |
|---|---|---|---|
| Progression Step 1 | up to age 5 | — | Learners explore and experience the world through play, sensory engagement, and adult-supported activity. They begin to develop awareness of themselves and their immediate environment. |
| Progression Step 2 | up to age 8 | — | Learners develop confidence and work with increasing independence. They make connections between experiences and begin to articulate thoughts about themselves and others. |
| Progression Step 3 | up to age 11 | — | Learners build capacity to manage change and transition. They consider different perspectives, manage emotions with growing skill, and act with increasing autonomy. |
| Progression Step 4 | up to age 14 | — | Learners demonstrate increasing maturity in navigating complex relationships and situations. They develop resilience, critical thinking, and awareness of their impact on others. |
| Progression Step 5 | up to age 16 | — | Learners evaluate their own learning, act ethically and sustainably, and engage with wider society. They exercise independent judgement and articulate reasoned values. |

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
- Criterion rubrics (Type 1/2): **12** (gate pass=11; halted=2)
  - stability: {'stable': 5, 'rubric_unstable': 7}
- Supporting components (Type 1/2): **9** (halted=2)
- Halted at any stage: 14
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

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares independent performance of skills with appropriate control, coordination, and technique, standing alone as evidence the LT is met without hedging language or framing Competent as incomplete.

_Propositional-thin flag:_ this is a factual Type 1 LT; the rubric is necessarily compressed.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to perform movement or exercise skills. |
| emerging | With support, attempts movement skills but demonstrates inconsistent control or incomplete technique. |
| developing | Independently performs basic movement and exercise skills with generally correct technique but inconsistency in execution. |
| competent | Independently performs movement, exercise, and activity skills with control, coordination, and technique appropriate to age and context. |
| extending | Performs movement skills with precision and adapts technique fluently across varied contexts and increasing complexity. |

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students video clips or live demonstrations of the same movement skill performed at different quality levels and ask them to describe what they notice about control and technique.
- stage: Guide students to identify the key differences between attempts that look shaky or incomplete versus smooth and controlled.
- stage: Work together to name what 'control,' 'coordination,' and 'technique' mean in the context of their own age-appropriate activities.
- stage: Have students sort movement examples into levels based on the language they've developed, then refine the descriptors together.
- prompt: What do you see happening with the person's body when they perform this skill smoothly versus when they struggle?
- prompt: What does it mean for a movement to have 'control' or 'good technique'?
- prompt: How would you describe the difference between doing a skill with help and doing it all by yourself?
- prompt: When might you need to change how you do a movement depending on where you are or what you're doing?
- anchor-examples guidance: Choose movement examples from activities students actually do in class or at home, showing the same skill at clearly different levels of control and consistency. Select clips or demonstrations where the difference between shaky/incomplete and smooth/controlled is visually obvious.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to perform the movement or exercise skill. |
| emerging | I can attempt movement skills with help, but my control and technique are not yet steady. |
| developing | I can perform basic movement and exercise skills on my own with mostly correct technique, though I am not always consistent. |
| competent | I can perform movement, exercise, and activity skills on my own with control, coordination, and technique that fit my age and what I am doing. |
| extending | I can perform movement skills with precision and change my technique smoothly when the activity or setting is different or more challenging. |

- self-check: Can I do this skill on my own, or do I still need help?
- self-check: Is my movement smooth and controlled, or does it feel shaky or incomplete?

_Feedback moves by level:_
- **no_evidence**
  - Invite the student to try the skill with you modeling it step by step alongside them.
  - Break the skill into smaller, simpler parts and practice one part at a time with encouragement.
- **emerging**
  - Reduce the amount of support gradually and have the student practice the skill independently while you observe for moments of control.
  - Focus feedback on one specific part of the technique that, when improved, will make the whole movement smoother.
- **developing**
  - Ask the student to perform the skill multiple times and notice which attempts feel most controlled; discuss what they did differently.
  - Introduce the skill in a slightly different context or with a small variation to build consistency across situations.
- **competent**
  - Challenge the student to perform the skill in a new or more complex setting and reflect on how they adjusted their technique.
  - Encourage the student to teach or demonstrate the skill to a peer, which deepens their awareness of precision and control.

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

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as independently demonstrated at the LT's level of demand, with no hedging language or framing of incompleteness.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to connect experiences to emotional responses. |
| emerging | With support, identifies one experience and names a feeling, but connection is unclear. |
| developing | Independently describes an experience and its emotional response but lacks depth in explaining well-being impact. |
| competent | Independently explains how specific experiences and emotional responses influence mental health and well-being. |
| extending | Explains how experiences and emotional responses influence well-being and relates this to broader life patterns. |

_Prerequisite edges:_
- `cluster_04_lt_01` [ontological_prerequisite/high] — Learner must be able to identify and name feelings before explaining how those feelings influence well-being.
- `cluster_02_lt_02` [pedagogical_sequencing/medium] — Understanding physical experiences and their effects supports recognition of how embodied experiences connect to emotional well-being.
- `cluster_08_lt_01` [pedagogical_sequencing/medium] — Understanding healthy relationships as fundamental to well-being provides context for recognizing how relational experiences influence emotional responses.

**Supporting components** — stability `stable`.

_Co-construction plan:_
- stage: Show students a short video or image of someone experiencing an emotion and ask them to name what they see.
- stage: Guide students to brainstorm their own experiences and the feelings that came with them.
- stage: Work together to identify what makes a connection between experience and feeling clear and strong.
- stage: Co-create language for each level that describes how well someone can explain this connection and its effect on well-being.
- prompt: What experience have you had that changed how you felt?
- prompt: How did that feeling affect you—your body, your thoughts, or how you treated others?
- prompt: What words would help someone understand the link between what happened and how it made you feel?
- prompt: When you explain this connection really well, what details do you include that make it clear?
- anchor-examples guidance: Choose one anchor that shows a clear, simple connection between an experience and a feeling, and one that goes deeper by explaining how that feeling shaped the student's well-being or behavior over time. Look for examples where the student's own voice is present and the reasoning is visible.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to connect an experience to a feeling or explained how it affected my well-being. |
| emerging | I can name one experience and one feeling, but I need help explaining how they are connected. |
| developing | I can describe an experience and the feeling it caused, but I do not fully explain how it affected my mental health or well-being. |
| competent | I can explain how a specific experience and my emotional response influenced my mental health and well-being. |
| extending | I can explain how experiences and emotional responses influence my well-being and connect this to patterns I notice in my life. |

- self-check: Can I describe a real experience and name the feeling it caused?
- self-check: Can I explain how that feeling affected my well-being, my thoughts, or my actions?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to share one thing that happened to them recently and how it made them feel.
  - Model aloud how you connect an experience to a feeling, then ask them to try with their own example.
- **emerging**
  - Ask follow-up questions to deepen the connection: How did that feeling change what you did next or how you felt about yourself?
  - Provide a sentence frame to help them explain the link: When [experience] happened, I felt [feeling] because …
- **developing**
  - Ask the student to explain one way their feeling affected their well-being, such as their sleep, mood, or relationships.
  - Encourage them to add one more detail that shows why this experience mattered to their mental health.
- **competent**
  - Invite the student to explore a second experience and compare how different experiences shape their well-being differently.
  - Ask them to reflect on whether they notice patterns in how certain types of experiences affect them over time.

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

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as independently demonstrated at the LT's level of demand, with no hedging language or framing of incompleteness.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to analyse decision impacts or influencing factors. |
| emerging | With support, identifies some impacts or factors but reasoning is incomplete or inaccurate. |
| developing | Independently identifies impacts on self and others and some influencing factors but misses broader societal scope. |
| competent | Independently analyses how decisions impact self, others, and society, and identifies key factors influencing decision-making. |
| extending | Analyses decision impacts and factors across multiple contexts and recognises interconnections between influences. |

_Prerequisite edges:_
- `cluster_03_lt_01` [ontological_prerequisite/high] — Understanding how experiences and emotions influence well-being is foundational to analysing how decisions impact self and others.
- `cluster_07_lt_01` [ontological_prerequisite/high] — Identifying social influences on identity and behaviour is essential to recognising factors that influence decision-making.
- `cluster_02_lt_02` [pedagogical_sequencing/medium] — Demonstrating physical competence provides concrete experience of personal decision-making and its outcomes, supporting analysis of impacts.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a real decision scenario and ask them to list all the people and groups affected by it.
- stage: Guide students to distinguish between immediate impacts and broader societal ripples.
- stage: Introduce the concept of influencing factors and have students brainstorm what shapes how people decide.
- stage: Work together to sort impacts and factors into categories and discuss what makes reasoning complete or incomplete.
- stage: Co-author level descriptors by asking students what evidence would show they can do each level.
- prompt: Who is affected by this decision, and in what ways?
- prompt: What happens beyond the immediate situation—how might this decision affect the wider community or society?
- prompt: What things influence how someone makes a decision—their beliefs, circumstances, information, or something else?
- prompt: How do you know if your analysis of a decision is thorough or if you've missed something important?
- prompt: Can you think of a time when one decision's impact led to another decision being made?
- anchor-examples guidance: Choose decisions that are age-appropriate and familiar to students, with clear impacts on multiple levels (personal, peer, community). Select examples where influencing factors are visible but not obvious, so students must reason through them.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to analyse how decisions affect people or what influences decision-making. |
| emerging | I can identify some people or groups affected by a decision and name some factors that influence decisions, but my reasoning has gaps or mistakes. |
| developing | I can independently identify how a decision affects myself and others, and I can name some factors that influence decisions, but I do not yet consider the wider society. |
| competent | I can independently analyse how a decision impacts myself, others, and society, and I can identify the key factors that influence how people decide. |
| extending | I can analyse decision impacts and influencing factors across different situations and recognise how influences are connected to each other. |

- self-check: Have I considered how this decision affects me, the people around me, and the wider community?
- self-check: Can I explain what factors influenced this decision and how they are connected?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to name one person or group affected by a decision and describe what happened to them.
  - Prompt the student to think of one thing that might make someone choose one way instead of another.
- **emerging**
  - Help the student check their reasoning by asking 'How do you know that?' or 'What evidence shows that?'
  - Guide the student to add one more impact or factor they may have overlooked.
- **developing**
  - Ask the student to step back and consider: 'Who else might be affected by this decision beyond the people we've already named?'
  - Encourage the student to explore how the decision might affect the community or society as a whole.
- **competent**
  - Invite the student to explore a different context or scenario and apply their analysis skills there.
  - Ask the student to trace how one influencing factor connects to or affects another factor.

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

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as independently demonstrated at the LT's level of demand (evaluating implications and risks before deciding) without hedging language or framing it as incomplete.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify or evaluate decision implications or risks. |
| emerging | With support, identifies some possible consequences but reasoning is incomplete or inaccurate. |
| developing | Independently identifies implications and risks for self or others but misses broader or longer-term consequences. |
| competent | Independently evaluates multiple implications and risks of decisions for self and others before deciding. |
| extending | Evaluates implications and risks across interconnected contexts and anticipates second-order consequences. |

_Prerequisite edges:_
- `cluster_05_lt_01` [ontological_prerequisite/high] — Analysing decision impacts and influencing factors is foundational; evaluation of implications and risks builds directly on that analytical capability.
- `cluster_03_lt_01` [pedagogical_sequencing/medium] — Understanding how experiences and emotions influence well-being supports recognition of emotional and personal implications in decision-making.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a real or realistic decision scenario and ask them to list every possible outcome they can think of.
- stage: Guide students to sort their outcomes into categories: effects on self, effects on others, short-term, and long-term.
- stage: Introduce the idea of risk and have students identify which outcomes are risky or uncertain.
- stage: Work together to distinguish between surface-level consequences and deeper, connected consequences that ripple outward.
- stage: Co-author level descriptors by asking students what it looks like when someone does or does not think through implications before deciding.
- prompt: What could happen if you make this decision—for you and for people around you?
- prompt: Which of these consequences might happen soon, and which might take weeks or months to show up?
- prompt: What could go wrong, and how confident are you that you've thought of all the risks?
- prompt: If one consequence happens, what else might that trigger down the line?
- prompt: How would you describe someone who rushes into a decision without thinking, and someone who carefully weighs what might happen?
- anchor-examples guidance: Choose decisions that are age-appropriate and personally relevant to students, with consequences that span both immediate and delayed effects, and that touch multiple people or contexts. Look for examples where surface-level thinking misses important ripple effects.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to think about what might happen before I decide. |
| emerging | I can name some things that might happen if I make a decision, but I need help and my thinking might be incomplete or mixed up. |
| developing | I can figure out on my own what might happen for me and for others, but I might miss consequences that take longer to show up or affect people further away. |
| competent | I can think through several different implications and risks of a decision for myself and others before I decide. |
| extending | I can evaluate how implications and risks connect across different situations and predict consequences that trigger other consequences. |

- self-check: Have I thought about what happens to me and to other people if I make this choice?
- self-check: Am I seeing only what happens right away, or am I also thinking about what might happen later or in other areas of my life?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to pause and name one thing that could happen if they make this decision.
  - Model thinking aloud about a consequence, then ask them to name one more consequence you did not mention.
- **emerging**
  - Ask: Who else might be affected by this decision, and what might happen to them?
  - Help the student separate immediate consequences from ones that might take longer to appear.
- **developing**
  - Push the student to think beyond the people directly involved: What other situations or people might be touched by this decision?
  - Ask: If that consequence happens, what else might it cause to happen?
- **competent**
  - Invite the student to map out how one consequence might trigger a chain of other consequences.
  - Challenge them to identify a risk they had not considered by asking about less obvious contexts or longer time horizons.

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

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor directly mirrors the LT definition without hedging language, frames the capability as demonstrated, and stands alone as evidence the target is met.

_Propositional-thin flag:_ this is a factual Type 1 LT; the rubric is necessarily compressed.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify consequences of career choices. |
| emerging | With support, names one or two consequences but descriptions lack detail or accuracy. |
| developing | Independently identifies consequences across one or two domains but misses depth or breadth. |
| competent | Identifies and describes significant lifelong consequences of career choices across personal, financial, and social domains. |
| extending | Identifies consequences and explains how they interconnect across domains or evolve over time. |

_Prerequisite edges:_
- `cluster_05_lt_01` [ontological_prerequisite/high] — Identifying consequences requires understanding how decisions and actions impact self and others.
- `cluster_07_lt_01` [pedagogical_sequencing/medium] — Understanding social influences on identity supports recognition of social consequences of career choices.
- `cluster_03_lt_01` [pedagogical_sequencing/medium] — Understanding emotional well-being supports recognition of personal consequences of career pathways.

**Supporting components** — stability `stable`.

_Co-construction plan:_
- stage: Show students a career choice scenario and ask them to brainstorm all the ways that choice might affect someone's life over time.
- stage: Guide students to sort their brainstormed consequences into three domains: personal, financial, and social.
- stage: Work together to distinguish between surface-level and significant consequences, discussing what makes a consequence worth describing.
- stage: Co-create descriptors for each level by asking students what evidence would show they can identify and describe consequences well.
- prompt: If someone chose to become a teacher, what are all the ways that decision might change their life—not just at the start, but years later?
- prompt: Which of these consequences fit into personal (how you feel, your skills, your lifestyle), financial (money and resources), or social (relationships, community, status) categories?
- prompt: Which consequences are surface-level and which ones are truly significant or life-changing?
- prompt: What would it look like if you could identify consequences in all three domains with real detail and accuracy?
- anchor-examples guidance: Choose career scenarios that naturally generate consequences across all three domains and that students can relate to or research easily. Select student work samples that show varying levels of depth—from naming one consequence vaguely to explaining how a financial consequence ripples into personal and social effects over decades.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to identify or describe consequences of career choices. |
| emerging | I can name one or two consequences of a career choice, but my descriptions are unclear or not quite accurate. |
| developing | I can identify consequences across one or two domains on my own, but I miss some important details or do not explore them deeply enough. |
| competent | I can identify and describe significant lifelong consequences of career choices across personal, financial, and social domains. |
| extending | I can identify consequences and explain how they connect to each other across domains or how they change over time. |

- self-check: Have I identified consequences in all three domains: personal, financial, and social?
- self-check: Are my descriptions detailed and accurate, and do they show why these consequences matter over a lifetime?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to pick one career and name just one thing that might change in their life because of that choice.
  - Provide a sentence starter: 'If someone chose this career, they might experience a change in their [personal life / money / relationships] because…'
- **emerging**
  - Ask the student to pick one consequence they named and add two or three details that explain why it matters.
  - Introduce the three domains and ask: 'Which domain does this consequence belong to, and can you find one consequence in a different domain?'
- **developing**
  - Ask the student to identify at least one consequence in the domain they have not yet explored.
  - Prompt them to explain how one consequence might lead to another consequence over time.
- **competent**
  - Ask the student to trace how a consequence in one domain affects or connects to consequences in another domain.
  - Invite them to predict how a consequence might change or deepen as someone moves through different life stages.

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

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated independently ('Identifies how...with clear reasoning') without hedging language, incompleteness markers, or positioning it as a way-station to Extending.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify social influences on identity. |
| emerging | With support, names one or two social influences but descriptions lack clarity or accuracy. |
| developing | Independently identifies several social influences on identity but explanations remain surface-level or incomplete. |
| competent | Identifies how family, peers, culture, and media shape identity, values, behaviours, and well-being with clear reasoning. |
| extending | Analyses how multiple social influences interact and conflict to shape identity across different contexts and life stages. |

_Prerequisite edges:_
- `cluster_03_lt_01` [ontological_prerequisite/high] — Understanding how experiences and emotional responses influence well-being is foundational to recognising how social influences shape identity and well-being.
- `cluster_02_lt_02` [pedagogical_sequencing/medium] — Understanding self-care and respect for self supports recognition of how social influences affect behaviours and sense of self-worth.
- `cluster_08_lt_01` [pedagogical_sequencing/medium] — Understanding healthy relationships and belonging provides context for identifying how social connections influence identity formation.

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

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated ('Analyses how norms and values develop within and across different cultural contexts with reasoned explanation') and directly mirrors the LT's demand without hedging, incompleteness framing, or positioning it as a way-station to Extending.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to analyse cultural norms or values. |
| emerging | With support, identifies some norms or values but analysis lacks depth or cultural context. |
| developing | Independently describes how norms develop in one culture but struggles to compare across contexts. |
| competent | Analyses how norms and values develop within and across different cultural contexts with reasoned explanation. |
| extending | Analyses norms and values development across cultures and relates patterns to broader social systems. |

_Prerequisite edges:_
- `cluster_07_lt_01` [ontological_prerequisite/high] — Identifying social influences on identity is foundational to analysing how norms develop culturally.
- `cluster_05_lt_01` [pedagogical_sequencing/medium] — Analysing decision impacts and influencing factors supports understanding how cultural norms shape behaviour.

**Supporting components** — stability `supporting_unstable`.

_Co-construction plan:_
- stage: Show students a short video or image of a cultural practice and ask them to list what they notice without judgment.
- stage: Guide students to distinguish between a norm they observed and the reasons or values that might underlie it.
- stage: Introduce the idea of comparing how the same value appears differently across two cultures.
- stage: Work together to identify what 'depth of analysis' means by examining a weak versus strong explanation of cultural development.
- stage: Co-create the five levels by having students sort example statements into categories of quality.
- prompt: What norm or value did you spot in this cultural practice, and what clues tell you it matters to that community?
- prompt: Why might this norm have developed in this culture—what problem or need might it solve?
- prompt: How is this value expressed differently in another culture you know about, and what might explain the difference?
- prompt: What makes an explanation of cultural norms 'surface-level' versus 'deep'—what details matter?
- prompt: Which of these statements about cultural norms shows the strongest thinking, and why?
- anchor-examples guidance: Choose anchor examples that show a clear progression from naming a norm without context, to explaining its origin in one culture, to comparing how similar values function differently across two or more cultures. Prioritize examples that reveal student reasoning, not just factual knowledge.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet attempted to analyse how cultural norms or values develop. |
| emerging | I can identify some norms or values in a culture with support, but my explanation of why they developed is unclear or missing cultural context. |
| developing | I can independently explain how norms develop within one culture, but I struggle to compare how similar norms function across different cultures. |
| competent | I can analyse how norms and values develop within and across different cultural contexts and explain my reasoning clearly. |
| extending | I can analyse how norms and values develop across cultures and connect these patterns to larger social systems and historical forces. |

- self-check: Can I explain not just what a norm is, but why it developed and what it does for that culture?
- self-check: Have I compared how the same value or need shows up differently in at least two cultures, and explained what causes those differences?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to name one norm they observe in a cultural practice and describe what it looks like in action.
  - Prompt them to think of a reason that norm might exist—what does it help the community do or believe?
- **emerging**
  - Help the student dig deeper by asking 'What in the environment, history, or beliefs of this culture might have caused this norm to develop?'
  - Introduce a second culture and ask how a similar value or need is expressed there, then guide them to notice the difference.
- **developing**
  - Challenge the student to select a second culture and systematically compare how the same underlying value appears in different forms.
  - Ask them to explain what factors in each culture might account for the different expressions of that value.
- **competent**
  - Invite the student to explore how the norms they analysed connect to larger patterns in society, such as economics, power, or survival.
  - Encourage them to consider how understanding these patterns helps explain cultural change over time.

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

**Criterion rubric** — stability `stable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as demonstrated ('Explains why...with clear reasoning') without hedging language, incompleteness markers, or framing Competent as a stepping stone to Extending.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to explain healthy relationships or belonging. |
| emerging | With support, names some features of healthy relationships but explanations lack depth or accuracy. |
| developing | Independently explains some reasons why healthy relationships matter but misses connections to broader wellbeing. |
| competent | Explains why healthy relationships and belonging are fundamental to wellbeing and health with clear reasoning. |
| extending | Explains healthy relationships and belonging's role in wellbeing and connects to multiple health dimensions. |

_Prerequisite edges:_
- `cluster_03_lt_01` [ontological_prerequisite/high] — Understanding how emotional responses influence wellbeing is foundational to explaining why relationships matter to health.
- `cluster_04_lt_01` [pedagogical_sequencing/medium] — Ability to communicate feelings appropriately supports understanding healthy relationship dynamics but is not strictly required to explain their importance.
- `cluster_07_lt_01` [pedagogical_sequencing/medium] — Identifying social influences on identity helps learners understand belonging's role but explanation of healthy relationships can precede this.

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

**Criterion rubric** — stability `rubric_unstable`, quality gate **PASS**.

_Competent-framing judge:_ `pass` — The descriptor declares the capability as independently demonstrated at the LT's level of demand without hedging language, incompleteness framing, or positioning it as a way-station to Extending.

| Level | Descriptor |
|---|---|
| no_evidence | No attempt to identify or analyse relationship dynamics. |
| emerging | With support, names some warning signs but analysis is incomplete or inaccurate. |
| developing | Independently identifies several warning signs but analysis lacks depth or nuance in unfamiliar contexts. |
| competent | Independently analyses relationship dynamics and accurately identifies multiple warning signs of unhealthy relationships. |
| extending | Analyses relationship dynamics across diverse contexts and connects warning signs to underlying patterns of harm. |

_Prerequisite edges:_
- `cluster_08_lt_01` [ontological_prerequisite/high] — Learner must understand what healthy relationships are before identifying deviations from that standard.
- `cluster_03_lt_01` [ontological_prerequisite/high] — Recognising emotional responses and their influence on well-being is essential to identifying unhealthy relationship impacts.
- `cluster_04_lt_01` [pedagogical_sequencing/medium] — Ability to communicate feelings supports reflection on relationship dynamics and articulation of concerns.
- `cluster_05_lt_01` [pedagogical_sequencing/medium] — Analysing decision impacts and influencing factors provides analytical frameworks applicable to relationship dynamics.

**Supporting components** — stability `stable`.

_Co-construction plan:_
- stage: Show students a short scenario of a relationship and ask them to spot what feels wrong or concerning.
- stage: Guide students to name the specific behaviours or patterns they noticed and discuss why those matter.
- stage: Work together to sort their observations into categories of warning signs.
- stage: Build shared language for what 'analysis' means by asking students how they would explain why a warning sign matters.
- stage: Co-author level descriptors by asking students what it looks like when someone can do this well, with help, or not yet.
- prompt: What behaviours or words in this relationship made you uncomfortable or worried?
- prompt: Why do you think that behaviour is a warning sign rather than just a normal disagreement?
- prompt: What pattern do you see—does this warning sign connect to other problems in the relationship?
- prompt: How would you explain to someone else why this relationship dynamic is unhealthy?
- anchor-examples guidance: Choose scenarios that show clear warning signs but vary in context and subtlety—one obvious example and one more nuanced case help students see that analysis requires looking beyond surface behaviour. Avoid examples that centre on only one type of relationship or harm.

_Student-facing rubric:_

| Level | Descriptor |
|---|---|
| no_evidence | I have not yet tried to identify warning signs or explain what makes a relationship unhealthy. |
| emerging | I can name some warning signs when someone helps me, but my explanation of why they matter is incomplete or not quite accurate. |
| developing | I can identify several warning signs on my own, but my analysis does not go deep enough or does not work well when the situation is new or different. |
| competent | I can analyse relationship dynamics on my own and accurately identify multiple warning signs that show a relationship is unhealthy. |
| extending | I can analyse relationship dynamics in many different contexts and connect warning signs to the deeper patterns of harm underneath them. |

- self-check: Can I name at least three warning signs and explain why each one matters?
- self-check: Have I looked at the relationship as a whole pattern, or just picked out single moments?

_Feedback moves by level:_
- **no_evidence**
  - Ask the student to point to one behaviour in the scenario and describe what they see happening.
  - Offer a sentence starter: 'This is a warning sign because…' and ask them to complete it.
- **emerging**
  - Ask the student to explain why each warning sign they named is unhealthy rather than just normal conflict.
  - Prompt them to find a second or third warning sign they might have missed in the same scenario.
- **developing**
  - Ask the student to show how two or three warning signs connect to each other or repeat over time.
  - Introduce a slightly different context and ask them to identify whether the same warning signs apply and why.
- **competent**
  - Ask the student to explain what deeper need or power imbalance might be driving the warning signs they identified.
  - Challenge them to analyse a relationship scenario from a perspective they have not considered before.

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

### Criterion-rubric stage halted LTs

- `cluster_06_lt_02` (Making Informed Career Pathway Decisions) — rubric_unreliable: only 0/3 runs produced parseable output
- `cluster_09_lt_02` (Evaluating Support Resources and Safety Strategies) — rubric_unreliable: only 1/3 runs produced parseable output

### Supporting-components stage halted LTs

- `cluster_07_lt_01` (Identifying Social Influences on Identity) — supporting_unreliable: no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]
- `cluster_08_lt_01` (Understanding Healthy Relationships and Belonging) — supporting_unreliable: no structural signature reached 2/3 agreement; signatures=[(('stages', 5), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 5), ('student_prompts', 5), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2))), (('stages', 4), ('student_prompts', 4), ('student_rubric_levels', ('no_evidence', 'emerging', 'developing', 'competent', 'extending')), ('self_check_prompts', 2), (('moves', 'no_evidence', 2), ('moves', 'emerging', 2), ('moves', 'developing', 2), ('moves', 'competent', 2)))]

