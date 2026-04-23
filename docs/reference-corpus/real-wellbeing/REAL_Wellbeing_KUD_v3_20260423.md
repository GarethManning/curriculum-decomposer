# REAL School Budapest — Wellbeing Framework KUD Charts v3
**Consolidated file | 23 April 2026**

This file supersedes `REAL_Wellbeing_KUD_v2_20260423.md` (retained as historical record) following QA Step 6 (whole-chart panel review) and QA Step 8 (T3 observation indicator panel review) on 23 April 2026 and the fix work applied in the same session. v2 itself superseded the three Session files on 23 April 2026 after the v1 panel review; the v2 change log is preserved verbatim below, followed by the v3 change log.

## What changed from v2 (this file's new changes, 23 April 2026)

| # | LT | Band(s) | Change | Authority |
|---|---|---|---|---|
| 1 | LT 7.1 | Bands A–F, Know | Added a standalone **Know** item at each band carrying LT 7.1's own metacognitive terminology (A: thinking about one's own thinking; B: pattern; C: driver; D: origin vs sustaining conditions; E: structured metacognitive protocol; F: personal metacognitive framework). The LT 6.1 neuroscience Know cross-reference is preserved at each band as a companion note. The two Know strands are distinct — neuroscience content is not duplicated. | QA Step 6 panel consensus recommendation (Christodoulou + Koedinger, with Wiliam and Wineburg concurring; Claxton dissenting — dissent recorded in authoring notes). |
| 2 | LT 7.1 | Bands A–F, Understand | Rewritten to retain the implication / pedagogical move at each band after metacognitive vocabulary was demoted to Know. No Understand band was emptied; each now reads as a clean "why / implication" statement paired with the matching Know definition. | Consequence of Change #1. |
| 3 | LT 7.1 | Prerequisites line | **LT 6.1 Bands C–D conceptual accelerator** retyped for the specific LT 6.1 Band C → LT 7.1 Band D pair to **hard prerequisite**, with rationale stated verbatim on the chart (origin-vs-sustaining analytical move requires stress-response mechanism knowledge). Other LT 6.1 → LT 7.1 couplings remain conceptual accelerators. | QA Step 6 panel consensus recommendation (Koedinger primary; Christodoulou concurring). |
| 4 | LT 7.1 | Authoring notes | Claxton dissent recorded verbatim (QA Step 6, 23 April 2026). Existing note "No standalone Know by design" rewritten to reflect the v3 standalone-Know structure. Note on hard-prerequisite pair added. | Companion to Changes #1 and #3. |
| 5 | LT 1.3 | Band D observation indicator | v2 wording "identifying, with genuine reflection rather than surface performance, how at least one unchosen group membership shapes their own experience or perspective in a specific situation" replaced with a behavioural anchor specified by Christodoulou: the student names a specific unchosen group membership and gives a specific example of how it shapes one of their own experiences, where the example is not a repetition of a class discussion example offered by a peer or teacher. Third-person, falsifiable. Band D Know, Understand, progression lever, warrant preserved. | QA Step 8 panel consensus recommendation (Christodoulou primary). |
| 6 | LT 1.3 | Authoring notes | Existing v2 note flagging Band D "genuine reflection" wording as "candidate for observation exemplar in teacher briefing" rewritten to document that the wording has been replaced with a behavioural anchor; companion exemplar library filename recorded. | Consequence of Change #5. |

**Companion artefacts from this v3 session:**
- `LT_1_3_observation_exemplar_library_20260423.md` — observation-indicator exemplar library for LT 1.3 Bands D and F (two "met" anchors, one false-positive anchor, one false-negative anchor per band; Band F partial-evidence note for observers).
- `criterion-bank-v3.json` — edge additions to reflect Change #3: new `hard_prerequisite` edges added from LT 6.1 Band C criteria (crit_0080 stress-response mechanism; crit_0082 habit-loop mechanism) to each LT 7.1 Band D criterion (crit_0101, crit_0102, crit_0180, crit_0181). The `hard_prerequisite` edge_type is new to the schema in this session; schema enum extended accordingly. See `v3-edge-addition-log-lt-6-1-to-7-1-20260423.md` for the full edge log.
- `unified-wellbeing-data-v4.json` and `wellbeing-index-v4.json` — rebuilt from this file and the edge-updated criterion-bank-v3.json.

All other chart content is preserved verbatim from v2.

Known issues **not** addressed in this v3 session — see the out-of-scope statement in the session commit message and `STATE.md` section 5 for the full list. In brief: LT 4.2 Band D cognitive-load split and Band F contested-claim curation protocol (QA Step 6 flag) are deferred to a unit-plan session, not a KUD edit; LT 1.3 Band F four-observation consolidation (Christodoulou recommendation 2(b)) is deferred pending observation-protocol design work; general T3 Band F observer-calibration burden (cross-cutting observation from Step 8) is scoped to an observation-protocol document, not individual KUD edits.

---

## What changed from v1 (three session files) — preserved verbatim from v2

| # | LT | Band(s) | Change | Authority |
|---|---|---|---|---|
| 1 | LT 1.3 | Index classification | Session 3 consolidated index "T2" corrected to **T3** | Authoritative source `lt-1-3-personal-identity-cultural-self-awareness-v1.md` line 17 declares Type 3 — Dispositional. The Session 1 KUD chart was already T3-consistent; only the Session 3 index line was in error. |
| 2 | LT 1.3 | Band D Know | Moved "social identity theory" and "intersectionality" full named concepts to Band E. Band D Know now introduces precursor claims (unchosen group membership + automatic in-group preference) without stacking intersectionality. Band D Understand, Do, progression lever and warrant preserved. | Panel review moderate revision 3a, Option 1. |
| 3 | LT 1.3 | Band E Know | Expanded from 2 items (cultural lens + ethnocentrism) to 4 items: items 1–2 preserved verbatim; items 3–4 are social identity theory and intersectionality promoted verbatim from Band D Know. Band E Understand, Do, progression lever and warrant preserved. | Panel review moderate revision 3a, Option 1. |
| 4 | LT 1.2 | Band F Do | Rewritten so action-adjustment is the primary observable, with recognition as inferred from action. Cross-context qualifier made explicit. Band F Know, Understand, warrant preserved. Progression lever line re-pointed. | Panel review moderate revision 3. |
| 5 | LT 5.2 | Band F Do | Rewritten so traceability between sustained prior engagement and observable post-school choices is the primary anchor. Articulation becomes supporting, not primary. Band F Understand, warrant preserved. Progression lever line re-pointed. | Panel review moderate revision 4. |
| 6 | LT 4.3 | Prerequisites line | "LT 1.2 — hard prerequisite throughout" → "LT 1.2 — soft enabler at Bands A–B, hard prerequisite from Band C onward". No other chart content changes. | Panel review moderate revision 5. |
| 7 | LTs 4.3, 8.1, 8.2, 8.3 | Band statements (Part 1 LT definitions) | Source.md-style parenthetical age ranges replaced with canonical: B 8–10 → B 7–9; C 10–12 → C 9–11; D 12–13 → D 11–13. 11 locations changed. | Panel review minor revision 6. |
| 8 | LTs 1.1, 3.1, 3.2, 5.2, 7.2, 8.3 | Post-chart footnote | Per-chart REAL-specific-term footnotes added below each chart containing any of: Reflection 360, D2R, Light Dragon capstone, Strive, dragon naming. Content of Do statements unchanged. | Panel review minor revision 7. |
| 9 | LT 6.2 | Post-Band-F note | Added: "Hungarian regulatory bodies named at Band F (OGYÉI, NÉBIH) require confirmation at unit-plan stage — institutional restructuring is periodic." Chart content unchanged. | Panel review minor revision 8. |

All other chart content (Know, Understand, Do, progression lever, warrant, authoring notes) is preserved verbatim from v1. See the companion file `REAL_Wellbeing_KUD_fixes_applied_20260423.md` for the complete fix log with current and new text side-by-side.

Known issues **not** addressed in this fix session — see `REAL_Wellbeing_KUD_fixes_applied_20260423.md` Step 8 for the full list.

---

## Consolidated index (corrected)

| # | LT ID | LT Name | Type | Band scope | Session file of origin |
|---|---|---|---|---|---|
| 1 | LT 1.1 | Self-Awareness & Regulation | T3 | A–F | Session 1 |
| 2 | LT 1.2 | Social Awareness & Empathy | T3 | A–F | Session 1 |
| 3 | LT 1.3 | Personal Identity & Cultural Self-Awareness | **T3** | A–F | Session 1 |
| 4 | LT 2.1 | Focused Attention & Strategy | T2 | A–F | Session 1 |
| 5 | LT 2.2 | Reflective Decision-Making | T2 | A–F | Session 1 |
| 6 | LT 3.1 | Health Literacy & Habits | T2 (+ T1 embedded) | A–F | Session 1 |
| 7 | LT 3.2 | Self-Care & Resilience | T3 | A–F | Session 2 |
| 8 | LT 4.1 | Bodies, Boundaries & Consent | T2 | A–F | Session 2 |
| 9 | LT 4.2 | Puberty, Health & Safe Choices | T2 | B–F (A N/A) | Session 2 |
| 10 | LT 4.3 | Active Bystander & Anti-Discrimination | T2 | A–F | Session 2 |
| 11 | LT 5.1 | Interpersonal Skills & Communication | T2 | A–F | Session 2 |
| 12 | LT 5.2 | Community Engagement & Purpose | T3 | A–F | Session 2 |
| 13 | LT 6.1 | Brain, Body & Wellbeing Science | T1 | A–F | Session 2 |
| 14 | LT 6.2 | Health Information Literacy | T2 | A–F | Session 3 |
| 15 | LT 7.1 | Pattern Analysis & Adjustment | T2 | A–F | Session 3 |
| 16 | LT 7.2 | Self-Direction in Practice | T3 | A–F | Session 3 |
| 17 | LT 8.1 | Information Verification & Media Literacy | T2 | A–F | Session 3 |
| 18 | LT 8.2 | Digital Influence & Psychological Agency | T2 (+ T1 embedded) | C–F (A–B N/A) | Session 3 |
| 19 | LT 8.3 | Digital Assertiveness & Wellbeing Strategies | T3 | A–F | Session 3 |

**Canonical band mapping (applies to all charts throughout v2):** Band A ages 5–7 (Water + Air Dragons); Band B ages 7–9 (Earth Dragons); Band C ages 9–11 (Fire Dragons); Band D ages 11–13 (Metal Dragons); Band E ages 13–15 (Light Dragons); Band F ages 15–17 (Post-Metal).

---
---

# PART 1 — New LT definitions (authored Session 1, 21 April 2026; canonical age labels applied)

## LT 4.3 — Active Bystander & Anti-Discrimination

### Knowledge Type Classification
**Type 2 — Horizontal Knowledge (confirmed).** The LT is scoped deliberately to the *reasoning* capacity about bystander situations; the enacted disposition "does this student actually intervene?" is not captured here and would require a separate observation route if the framework wishes to assess it.

**Assessment Route:** Reasoning-quality rubric; written scenario analysis; structured roleplay with novel situations; short-answer scenario tasks.

### LT Definition
**I can identify when a situation involves discrimination, exclusion, or targeted harm, assess what a safe and proportionate bystander response would be, and justify my reasoning about when and how to act or seek help.**

### Required Fields

| Field | Content |
|---|---|
| **LT Name** | Active Bystander & Anti-Discrimination |
| **Competency** | C4 — Consent, Safety & Healthy Relationships |
| **Knowledge Type** | Type 2 — Horizontal |
| **Assessment Route** | Reasoning-quality rubric; scenario analysis; structured roleplay with novel situations |
| **Prerequisites** | **LT 1.2 (Social Awareness & Empathy) — soft enabler at Bands A–B, hard prerequisite from Band C onward.** Students must be able to read others' emotional states and take perspective before they can meaningfully analyse bystander situations, but at Bands A–B basic notice-and-tell bystander response can develop in parallel with empathy rather than gated on it. **LT 6.1 (Brain, Body & Wellbeing Science)** — conceptual accelerator from Band C onward; stress-response knowledge explains why "freezing" happens and why pre-planning matters. **LT 4.1 (Bodies, Boundaries & Consent)** — parallel sibling; shared vocabulary on power dynamics and pressure. |
| **Band Range** | A–F (no N/A bands — framing adjusts by age) |

### Band Statements

**Band A (ages 5–7, Water + Air):** I can notice when someone is left out or treated unkindly, describe what I saw, and tell a trusted adult.
- *Progression lever:* Baseline — perception plus help-seeking.

**Band B (ages 7–9, Earth):** I can describe what happened when someone was excluded or treated unfairly, say how the person might have felt, and choose one helpful action I could take from a short list of options.
- *Progression levers:* **Complexity** (noticing → noticing + attributing feeling); **Reasoning** (report → choice of response).

**Band C (ages 9–11, Fire):** I can identify different forms of exclusion, teasing, or discrimination in a scenario, weigh whether it is safe for me to intervene directly, and explain my choice of response from the four bystander options.
- *Progression levers:* **Complexity** (single form → several forms); **Precision** (general helpful action → named response type — direct intervention, distraction, delegation, delayed support); **Reasoning** (choice → safety-weighted choice).

**Band D (ages 11–13, Metal):** I can analyse a bystander scenario involving discrimination, identify the group and power dynamics at play, and justify a specific response based on safety, proportionality, and the targeted person's likely needs.
- *Progression levers:* **Reasoning** (safety-weighted choice → multi-criterion justification); **Complexity** (individual action → group/power dynamics); **Scope** (what to do → what the targeted person might need).

**Band E (ages 13–15, Light):** I can evaluate competing responses to a discrimination scenario — including my own likely default response — and explain how group norms and institutional context shape which interventions are possible or effective.
- *Progression levers:* **Reasoning** (multi-criterion justification → meta-reasoning about own defaults); **Scope** (interpersonal → contextual/institutional); **Transfer** (scripted scenario → self-analysis).

**Band F (ages 15–17, Post-Metal):** I can construct a reasoned analysis of a bystander success or failure — my own or another's — evaluate what made effective intervention possible or impossible, and propose conditions at the group, school, or community level that would make active bystander response more likely.
- *Progression levers:* **Reasoning** (context analysis → systems-level reasoning); **Independence** (scenario-prompted → self-directed case selection); **Scope** (individual response → systemic conditions).

### Design Notes

- **Scope is deliberately analytical, not dispositional.** The question "does this student actually intervene?" is not assessed through this LT.
- **The four-response framework** (direct / distract / delegate / delay — Hollaback / Right To Be lineage) enters at Band C.
- **"Discrimination" is used across all bands,** but what counts escalates by lever.
- **Teacher review flag:** Band E's "evaluate your own default response" requires psychological safety; pair with restorative, non-judgemental framing in the unit plan.
- **REAL-specific warrant:** In a student body spanning 15+ nationalities, this LT lands the group-dynamics analysis earlier than is typical in CASEL or Welsh CfW.

---

## LT 8.1 — Information Verification & Media Literacy

### Knowledge Type Classification
**Type 2 — Horizontal Knowledge (confirmed).** Reasoning about claims, sources, motivation, and platform context — analytical capacity deployed when the situation calls for it.

**Assessment Route:** Reasoning-quality rubric; scenario analysis with real claims; written evaluation tasks; comparative source analysis.

**Relationship to LT 6.2:** Framework deliberately distinguishes the two. LT 6.2 handles *health-specific* evaluation; LT 8.1 handles *general* digital and media claims.

### LT Definition
**I can locate a claim in digital or media content, assess its credibility using appropriate criteria, identify signs that it has been manipulated or designed to deceive, and justify what I believe, share, or act on as a result.**

### Required Fields

| Field | Content |
|---|---|
| **LT Name** | Information Verification & Media Literacy |
| **Competency** | C8 — Critical Digital Literacy |
| **Knowledge Type** | Type 2 — Horizontal |
| **Assessment Route** | Reasoning-quality rubric; scenario analysis; comparative source evaluation; written analytical tasks |
| **Prerequisites** | None strictly. **LT 2.2 (Reflective Decision-Making)** is a soft enabler from Band C onward. **LT 6.2 (Health Information Literacy)** is a sibling, not a prerequisite. |
| **Band Range** | A–F |

### Band Statements

**Band A (ages 5–7, Water + Air):** I can tell the difference between something real and something made up in a picture, video, or story, and ask a trusted adult when I am not sure.

**Band B (ages 7–9, Earth):** I can identify who made a piece of digital content, check whether it comes from a trusted place, and explain why I do or do not believe it.
- *Progression levers:* **Complexity** (real/pretend → authorship + origin); **Reasoning** (ask an adult → give my own reason).

**Band C (ages 9–11, Fire):** I can compare two sources making the same claim, identify signs that a piece of content has been edited or designed to mislead, and explain which source I trust more and why.
- *Progression levers:* **Complexity** (one source → comparison); **Precision** (trust/distrust → named signals of manipulation); **Reasoning** (own reason → comparative justification).

**Band D (ages 11–13, Metal):** I can analyse a digital claim by examining its origin, the evidence behind it, and the motivation of its source, and justify my conclusion about what to believe, share, or act on.
- *Progression levers:* **Complexity** (comparison → multi-criterion analysis); **Reasoning** (comparison → motivation/stake analysis); **Scope** (believe → believe/share/act — three distinct decisions).

**Band E (ages 13–15, Light):** I can evaluate a contested claim by weighing evidence across multiple sources, identify how algorithmic context or platform incentives shaped how the claim reached me, and justify my conclusion while accounting for my own likely biases.
- *Progression levers:* **Reasoning** (analysis → evaluation under contest); **Scope** (source-level → platform/algorithmic layer); **Precision** (source motivation → self-bias awareness).

**Band F (ages 15–17, Post-Metal):** I can evaluate synthetic, AI-generated, or sophisticated disinformation, compare my verification process against recognised critical-appraisal criteria, and construct a reasoned conclusion on a real-world contested claim that acknowledges what I cannot know.
- *Progression levers:* **Complexity** (contested → synthetic/AI-era); **Reasoning** (own process → meta-evaluation against external standard); **Transfer** (scripted scenarios → genuine real-world claim); **Independence** (prompted → self-directed).

### Design Notes

- **Three decisions, not one.** From Band D the framework distinguishes *believe / share / act*.
- **Algorithmic context enters at Band E,** not earlier.
- **Bias-of-self enters at Band E,** parallels LT 2.2 Band E.
- **Band F "what I cannot know"** is the genuinely mature move — epistemic humility as part of the capacity.
- **No tool or platform names in LT statements.**
- **Warrant / evidence base:** Wineburg & McGrew (Stanford Civic Online Reasoning); Caulfield (SIFT); boyd; van der Linden; Pennycook & Rand.
- **Teacher review flag:** Contested claim material should be handled deliberately in an international student body.

---

## LT 8.2 — Digital Influence & Psychological Agency

### Knowledge Type Classification
**Type 2 — Horizontal Knowledge, with substantial embedded Type 1 Know layer.** The T1 content (dopamine → variable reward → attention capture → feed curation → algorithmic amplification) is not assessed on its own — it is always mobilised in service of reasoning about a specific product or experience. Structurally identical to LT 4.2 and LT 3.1.

**Assessment Route:** Reasoning-quality rubric; product/platform analysis task; written evaluation of a specific feature or experience. Vocabulary checks may support the embedded Know layer.

### LT Definition
**I can identify how a digital product or platform is designed to shape attention, emotion, or behaviour, analyse the effect that design is having on me, and justify a reasoned response.**

### Required Fields

| Field | Content |
|---|---|
| **LT Name** | Digital Influence & Psychological Agency |
| **Competency** | C8 — Critical Digital Literacy |
| **Knowledge Type** | Type 2 — Horizontal (with embedded Type 1 Know layer on persuasive design, attention economy, and algorithmic curation) |
| **Assessment Route** | Reasoning-quality rubric; product/platform analysis; written self-analysis task; vocabulary checks on Know layer |
| **Prerequisites** | **LT 6.1 (Brain, Body & Wellbeing Science)** — knowledge-contingent. Habit-loop, dopamine, and attention mechanisms from LT 6.1 Bands C–D are required. **LT 2.1 (Focused Attention & Strategy)** — conceptual enabler. **LT 2.2 (Reflective Decision-Making)** — soft enabler from Band E onward. |
| **Band Range** | C–F. **Bands A and B are N/A** — meta-cognitive move required (analysing design intent from inside the experience) is not reliably present before ~age 10, and platform usage at A–B is primarily parent-mediated. Early digital hygiene is handled through LT 3.2 and LT 2.1. |

### Band Statements

**Bands A and B:** N/A — see rationale above.

**Band C (ages 9–11, Fire):** I can identify a specific feature of a digital product that is designed to keep me using it, describe one reason the design works on people, and explain one effect I notice on myself.
- Baseline for this LT.

**Band D (ages 11–13, Metal):** I can analyse how a digital product uses persuasive design to shape attention, emotion, or behaviour, and explain the effect I notice on my own thinking, mood, or time.
- *Progression levers:* **Complexity** (one feature → multiple interacting features); **Precision** (general effect → named dimension — attention / emotion / behaviour); **Reasoning** (identify → analyse mechanism).

**Band E (ages 13–15, Light):** I can evaluate how a digital platform algorithmically curates what I see, explain the psychological or economic incentives driving that design, and justify a change I will make to my use based on what I find.
- *Progression levers:* **Scope** (product features → platform-level curation); **Reasoning** (mechanism → incentive analysis); **Complexity** (product → platform + its business model).

**Band F (ages 15–17, Post-Metal):** I can evaluate the cumulative effect of persuasive design on my attention, relationships, and identity, compare my analysis against recognised research on digital wellbeing, and articulate a reasoned position on where I will and will not allow these systems to operate on me.
- *Progression levers:* **Scope** (single product/platform → cumulative self-impact); **Reasoning** (incentive analysis → research-anchored position); **Independence** (scenario-prompted → self-directed stance); **Transfer** (evaluating features → articulating a values-based position).

### Design Notes

- **Band D is the AoA band.** Attention triangle, habit loop, Elephant/Rider vocabulary are the teaching apparatus.
- **Relationship to LT 2.1:** LT 2.1 is the attentional capacity; LT 8.2 is the systems that operate on it.
- **Relationship to LT 8.1:** LT 8.1 asks "is this true?"; LT 8.2 asks "what is this doing to me?"
- **Band scope rationale:** Early-year digital hygiene is handled by LT 3.2 and adult-mediated boundaries — N/A at A–B is honest about what this analytical capacity requires.
- **"Allow these systems to operate on me" at Band F** refuses addiction/willpower frames in favour of consent and agency.
- **Warrant / evidence base:** Mark (attention research); Harris / Center for Humane Technology; Twenge / Haidt (contested but canonical); Zuboff; Eyal/Hoover (taught as object of study, not endorsement).
- **Teacher review flag — Band F:** Haidt/Twenge effect sizes are disputed. Unit designers should curate sources representing the debate rather than picking a side.

---

## LT 8.3 — Digital Assertiveness & Wellbeing Strategies

### Knowledge Type Classification
**Type 3 — Dispositional (confirmed).** Only exists as enacted across time and contexts. The three bundled facets (boundaries, assertive communication, wellbeing-supporting practices) are manifestations of one underlying disposition — being an agent inside digital environments rather than being used by them. Structurally parallel to LT 1.1.

**Assessment Route:** Multi-informant observation. **No rubric. Not summatively graded.** Evidence: teacher observation, student self-reflection, optional parent input, Strive data where applicable. Synthesised in Reflection 360.

### LT Definition
**I maintain healthy boundaries, communicate assertively, and sustain wellbeing-supporting practices inside digital environments across platforms and contexts.**

*This LT is dispositional and is assessed through multi-informant observation across time and contexts, not through a single task or rubric.*

### Required Fields

| Field | Content |
|---|---|
| **LT Name** | Digital Assertiveness & Wellbeing Strategies |
| **Competency** | C8 — Critical Digital Literacy |
| **Knowledge Type** | Type 3 — Dispositional |
| **Assessment Route** | Multi-informant observation; Reflection 360; not summatively graded; no rubric |
| **Prerequisites** | **LT 1.1 (Self-Awareness & Regulation)** — knowledge-contingent. **LT 5.1 (Interpersonal Skills & Communication)** — knowledge-contingent. **LT 8.2 (Digital Influence & Psychological Agency)** — conceptual accelerator from Band C onward. **LT 4.1 (Bodies, Boundaries & Consent)** — parallel sibling. |
| **Band Range** | A–F |

### Band Indicators (Mode 3 — Observation Indicator Set)

Third-person observation indicators, three per band.

**Band A (ages 5–7, Water + Air):**
- The child stops using a digital device when a trusted adult asks, without significant distress.
- The child tells a trusted adult when they see or are shown something online that makes them feel confused, scared, or uncomfortable.
- The child does not share personal information with strangers in digital contexts — their name, address, school, or family details.

**Band B (ages 7–9, Earth):**
- The child exits digital content they recognise as unkind, distressing, or inappropriate for them, without needing an adult to direct them.
- The child uses simple assertive language in digital communication — "I don't want to," "please stop," "I'm going to tell an adult" — when a peer behaves unkindly online.
- The child keeps to family or school rules about device use — time, place, content — without constant reminders.

**Band C (ages 9–11, Fire):**
- The student names their own digital boundaries — when they will and will not use a device, what they will and will not engage with — and largely keeps to them without external reminders.
- The student speaks up or exits group chats, games, or platform interactions where peers behave unkindly, excludingly, or unsafely.
- The student takes independent action when content or interaction is affecting their wellbeing — muting, blocking, unfollowing, reporting, stepping away.

**Band D (ages 11–13, Metal):**
- The student maintains their stated digital boundaries under social pressure.
- The student uses assertive communication in difficult digital interactions without escalating, abandoning, or capitulating.
- The student adjusts their digital practice in response to evidence they have collected about its effects on their attention, mood, or sleep.

**Band E (ages 13–15, Light):**
- The student sustains digital wellbeing practices across extended periods — not only in a week when someone is tracking, but as an integrated part of their life.
- The student holds their position in digital disagreements or conflicts without becoming harsh, performative, or retreating.
- The student notices when their digital practice is not serving them well and adjusts proactively, rather than waiting for a crisis.

**Band F (ages 15–17, Post-Metal):**
- The student treats their digital life as an expression of their values — what they engage with, what they create, what they refuse — and can articulate this stance when asked, without performing it publicly.
- The student supports peers navigating digital pressure, conflict, or harm, without taking over or shaming.
- The student holds consistent digital practices across contexts without the quality shifting based on who is watching.

### Design Notes

- **This is the enacted counterpart to LT 8.2.** Both needed — a student can be strong in one and weak in the other.
- **Parent input is more valuable here than for most T3 LTs.** Much of students' digital life is invisible to teachers.
- **Strive is appropriate as process evidence, not outcome.** The disposition shows when no one is tracking.
- **"Without becoming harsh or performative" at Band E** is deliberate — substantive vs. performative assertiveness distinction.
- **"Without making it a public performance" at Band F** — mature digital values are lived, not advertised.
- **Warrant:** Ryan & Deci (self-determination theory); Przybylski, Orben (adolescent digital wellbeing); Alberti & Emmons (assertiveness); Vanden Abeele (digital boundary-setting).
- **Safeguarding note:** Band A–B indicator on personal information is a safeguarding concern if failed — follow school protocol, not assessment data pathway.

---
---

# PART 2 — KUD charts 1 through 19

All 19 charts below. Content in Know, Understand, Do, progression lever, and warrant columns is identical to v1 except for the surgical edits listed in "What changed from v1" above. Those edits are marked **[REVISED v2]** in-place.

---

## KUD 1 of 19 — LT 1.1 — Self-Awareness & Regulation

**Routing note:** null

**LT Definition:** I can notice my internal state, apply regulation strategies appropriate to the situation, and adjust them based on what I learn about what works across contexts.
**Knowledge Type:** T3 — Dispositional. Self-regulation only exists as enacted across time and contexts; a single task cannot evidence it, and the pattern of behaviour across varied situations IS the capability.
**Do Evidence Type:** Disposition. Third-person observation indicators throughout. No single-occasion performance substitutes for the cross-context observation required.
**Band Scope:** A–F. All bands developmentally appropriate. *(Band A ages 5–7 Water+Air; B 7–9 Earth; C 9–11 Fire; D 11–13 Metal; E 13–15 Light; F 15–17 Post-Metal.)*
**Prerequisites:** LT 6.1 — **soft enabler** at Band A–B (the disposition can develop through practised strategies and adult co-regulation without factual grounding); **conceptual accelerator** at Band C+ (understanding the amygdala, prefrontal cortex, and HPA axis is what makes regulation portable to novel contexts and teachable to others).

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | Know content for this band lives in LT 6.1 Band A (basic body signals; what sleep and food do for the body and brain). | My feelings have names, and naming them helps me notice them. | The teacher notices the student pausing to name a feeling before reacting, and selecting a practised calming strategy without needing step-by-step adult direction, on most occasions when emotional activation is visible. | Baseline — no prior band. | Lieberman, M. D., Eisenberger, N. I., Crockett, M. J., Tom, S. M., Pfeifer, J. H., & Way, B. M. (2007). Putting feelings into words: Affect labeling disrupts amygdala activity in response to affective stimuli. *Psychological Science*, 18(5), 421–428. |
| **B** | Know content for this band lives in LT 6.1 Band B (fight/flight/freeze response; habit loop). | What I feel is often set off by something specific, and I can learn what sets me off. | The teacher notices the student naming a recurring personal trigger — time of day, type of task, particular social configuration — and selecting a strategy from their practised repertoire before the trigger escalates, across more than one setting. | **Complexity** — feeling-naming → linking feeling to cause. | Gross, J. J. (2015). Emotion regulation: Current status and future prospects. *Psychological Inquiry*, 26(1), 1–26. |
| **C** | Know content for this band lives in LT 6.1 Band C (amygdala and prefrontal cortex functions under stress; neuroplasticity). | A strategy either works for me or doesn't depending on the situation, and I can tell by checking afterwards. | The teacher notices the student applying a regulation strategy in a genuinely challenging situation (not only in rehearsal) and afterwards explaining — spontaneously or on brief prompt — what worked and what didn't, on multiple occasions across a term. | **Reasoning** — pattern-naming → post-hoc strategy evaluation. **Transfer** — practised contexts → challenging contexts. | Zimmerman, B. J. (2000). Attaining self-regulation: A social cognitive perspective. In M. Boekaerts, P. R. Pintrich, & M. Zeidner (Eds.), *Handbook of self-regulation* (pp. 13–39). Academic Press. |
| **D** | Know content for this band lives in LT 6.1 Band D (stress, emotion, attention, and habit as an interdependent system; HPA axis). | How I regulate depends on what's available to me in a given context, and adjusting my approach across settings is how regulation gets more reliable. | The teacher notices the student applying different regulation strategies across different settings (school task pressure, social friction, home reports), explaining without adult prompt why one strategy fits one setting and not another, and naming one concrete change they are going to try next. | **Scope** — single setting → multiple settings. **Reasoning** — evaluation → context-sensitive adjustment. | Aldao, A. (2013). The future of emotion regulation research: Capturing context. *Perspectives on Psychological Science*, 8(2), 155–172. |
| **E** | Know content for this band lives in LT 6.1 Bands D–E (system-level neuroscience; interoception and co-regulation mechanisms). | Regulation is not only a personal tool — my emotional state shapes the people around me, and taking responsibility for that is part of mature self-regulation. | The teacher notices the student sustaining their regulation practices through a sustained pressure period (extended assessment window, significant personal difficulty, intense group project) without adult scaffolding, and, unprompted, commenting on how their own state is affecting the group or a specific peer. | **Independence** — prompted → proactive. **Transfer** — personal performance → interpersonal impact. | Coan, J. A., & Sbarra, D. A. (2015). Social Baseline Theory: The social regulation of risk and effort. *Current Opinion in Psychology*, 1, 87–91. |
| **F** | Know content for this band lives in LT 6.1 Band F (integrative neuroscience of regulation, co-regulation, and identity). | A mature regulation system is one I can describe and teach, not merely use — and the capacity to support others' regulation deepens my own. | The teacher or mentor notices the student articulating — in a Reflection 360 conversation or spontaneous reflection — their personal regulation system, the conditions that disrupt it, and adaptations built over time, AND supporting a peer or younger student in developing their own, without adult direction. | **Reasoning** — evaluated adjustment → system-level articulation. **Transfer** — self-regulation → coaching and modelling for others. | Boekaerts, M., & Corno, L. (2005). Self-regulation in the classroom: A perspective on assessment and intervention. *Applied Psychology*, 54(2), 199–231. |

**Authoring Notes:**
- Prerequisite typing split by band: soft enabler A–B, conceptual accelerator from C. Do not gate A–B assessment on LT 6.1.
- Band F Do requires triangulation across more than one observer and more than one occasion. Reflection 360 is primary.
- Band E Understand (regulation shapes others) is developmentally correct but emotionally weighty — teacher framing matters.
- International-context: observation protocol should accommodate different baseline regulation profiles across cultural backgrounds.

> **REAL-specific terms used in this chart (for external readers):**
> - *Reflection 360* — structured reflective conversation between student and teacher or mentor, conducted periodically across the year.

---

## KUD 2 of 19 — LT 1.2 — Social Awareness & Empathy

**Routing note:** null

**LT Definition:** I can read others' emotional states and perspectives, respond in ways that meet their stated needs, and repair relationships after conflict.
**Knowledge Type:** T3 — Dispositional. Empathy across contexts cannot be evidenced in a single task; it only exists as a pattern of noticing, asking, and adjusting across real interactions.
**Do Evidence Type:** Disposition. Third-person observation indicators throughout.
**Band Scope:** A–F. *(Band A ages 5–7 Water+Air; B 7–9 Earth; C 9–11 Fire; D 11–13 Metal; E 13–15 Light; F 15–17 Post-Metal.)*
**Prerequisites:** LT 1.1 — **soft enabler**. Self-awareness of emotion enriches reading of others' emotion, but empathy can also develop through mimicry, guided perspective-taking, and repair practice without full LT 1.1 mastery; do not gate LT 1.2 on LT 1.1.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | Know content for this band lives in LT 6.1 Band A (body signals as emotion indicators). | Other people have feelings too, and I can sometimes tell what they are. | The teacher notices the student naming a feeling another person is showing — not only their own — and offering either a kind word or a specific helpful action in response, without adult prompt. | Baseline — no prior band. | Wellman, H. M. (2014). *Making Minds: How Theory of Mind Develops.* Oxford University Press. |
| **B** | Know content for this band lives in LT 6.1 Band B (basic emotional cues; fight/flight/freeze signs in others). | The same situation can look different to different people, and asking is more reliable than guessing. | The teacher notices the student describing a situation from another's perspective in words, asking "do you want help?" before acting, and accepting a "no" without pushing, on multiple occasions. | **Complexity** — noticing feelings → taking perspective. **Reasoning** — assumption → verification. | Selman, R. L. (2003). *The Promotion of Social Awareness.* Russell Sage Foundation. |
| **C** | Know content for this band lives in LT 6.1 Band C. LT 5.1 Band C provides communication scaffolding. | Other people signal what they need both in what they say and in what they do, and paying attention to both makes me more responsive. | The teacher notices the student attending to multiple group members during shared work, checking in with a direct question when signals are unclear, and adjusting their own actions to match what the other has said they need. | **Complexity** — individual → group. **Precision** — general empathy → specific responsiveness. | Fiske, S. T., & Taylor, S. E. (2013). *Social Cognition: From Brains to Culture* (2nd ed.). Sage. |
| **D** | Know content for this band lives in LT 6.1 Band D. Repair vocabulary draws on LT 5.1 Band D. | Conflict is a normal part of relationships, and repair is a specific skill that matters more than avoiding conflict in the first place. | The teacher notices the student, after a conflict, listening without interrupting, naming their own contribution to the situation, and proposing a next step that accounts for the other person's position — not only their own — across more than one occasion. | **Reasoning** — responsiveness → repair. **Transfer** — daily interaction → conflict. **Scope** — one-directional help → mutual resolution. | Gottman, J. M. (2015). *The Seven Principles for Making Marriage Work.* Harmony; Zehr, H. (2015). *The Little Book of Restorative Justice.* Good Books. |
| **E** | Know content for this band lives in LT 6.1 Bands D–E (co-regulation, group stress dynamics). | Conflict in groups is shaped by more than individual feelings — group norms, histories, and power dynamics all affect what is possible in repair. | The teacher notices the student facilitating repair in a group context (not only a dyad), naming a group dynamic that contributed to the conflict, and proposing steps that address needs of multiple parties rather than only defending one position. | **Complexity** — dyadic repair → group dynamics. **Scope** — two parties → multiple. **Reasoning** — mutual resolution → systemic factors. | Lewin, K. (1947). Frontiers in group dynamics. *Human Relations*, 1(1), 5–41. |
| **F** | Know content for this band lives in LT 6.1 Band F; structural factor content draws on Humanities Identity, Power & Representation competency. | Full empathic understanding requires knowing what shapes a person's context, not only what they say they feel — and sometimes the most empathic response is to address the conditions, not just the person. | **[REVISED v2]** The teacher notices the student adjusting their response to someone whose experience is being shaped by structural or systemic factors, in ways that address those conditions rather than only the individual person, across more than one observed occasion. | **[REVISED v2]** **Reasoning** — group dynamics → structural analysis expressed in action. **Transfer** — interpersonal empathy → structural-aware adjustment. **Independence** — prompted → self-initiated. | Hollan, D., & Throop, C. J. (Eds.). (2011). *The Anthropology of Empathy.* Berghahn Books. |

**Authoring Notes:**
- Band F Do (v2) rewrites the primary observable as action-adjustment to conditions, with recognition inferred from action rather than the primary observable. The authoring-note concern that "a fluent student can simulate structural empathy without enacting it" is addressed by requiring the observer to see the adjustment and the cross-context qualifier ("across more than one observed occasion").
- Cross-cultural signal-reading shows up at Band C and sharpens at Band E.
- Relationship to LT 4.3: Band D repair and Band F systemic move share conceptual ground. Teach adjacent, not parallel.

---

## KUD 3 of 19 — LT 1.3 — Personal Identity & Cultural Self-Awareness

**Routing note:** null

**LT Definition:** I can describe who I am across different contexts, recognise how my cultural background shapes my values and responses, and maintain a stable sense of self when contexts change.
**Knowledge Type:** **T3 — Dispositional.** *(Authoritative source: `lt-1-3-personal-identity-cultural-self-awareness-v1.md` line 17. v1 Session 3 consolidated index incorrectly recorded T2; corrected in this v2 file's consolidated index above.)*
**Do Evidence Type:** Disposition. Third-person observation indicators throughout. Exception at Band F: a structured reflective portfolio piece can provide supplementary evidence of the K/U layer, but observation remains primary.
**Band Scope:** A–F. *(Band A ages 5–7 Water+Air; B 7–9 Earth; C 9–11 Fire; D 11–13 Metal; E 13–15 Light; F 15–17 Post-Metal.)*
**Prerequisites:** LT 1.1 — **soft enabler**. LT 1.2 — **soft enabler** from Band C onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. Different families speak different languages, eat different foods, and celebrate different events — these differences are what we call culture. 2. Everyone has a home culture: the particular mix of ways, stories, and celebrations they grew up with. | The things my family does at home are part of who I am, and what other families do is part of who they are — there isn't one right way to do most things. | The teacher notices the student naming, without prompting, at least one thing that is part of their own home or family life that differs from a classmate's, and doing so without marking the difference as better or worse. | Baseline — no prior band. | Bronfenbrenner, U. (1979). *The Ecology of Human Development.* Harvard University Press. |
| **B** | 1. Identity has multiple dimensions — family background, home language(s), cultural traditions, beliefs, personal interests — and they do not have to match. 2. A person can belong to more than one cultural group at the same time; dual or multiple belonging is normal. | Belonging to different groups at once isn't confusion — it is normal, and most people live this way. | The teacher notices the student describing more than one aspect of their own identity (including at least one cultural dimension) during class reflection, without prompt, on multiple occasions. | **Scope** — single trait → multiple identity dimensions including cultural ones. | Erikson, E. H. (1968). *Identity: Youth and Crisis.* W. W. Norton. |
| **C** | 1. Stereotypes are oversimplified beliefs applied to all members of a group regardless of individual differences; they operate automatically and affect how people see others and themselves. 2. A person's cultural background shapes expectations, communication style, and values in ways they are not fully conscious of — sometimes called a cultural lens. | My background shapes how I see and interpret things — and other people's backgrounds shape how they see and interpret things. Neither view is the whole picture. | The teacher notices the student pausing to consider how their own background might be influencing their reaction or interpretation before responding in a cross-cultural interaction — at least occasionally, without adult prompting. | **Reasoning** — naming identity attributes → recognising how identity shapes interpretation. | Hofstede, G. (2001). *Culture's Consequences* (2nd ed.). Sage. |
| **D** | **[REVISED v2 — Option 1]** 1. Some of the groups a person belongs to were not chosen by them — the family they were born into, the nationality on their passport, the first language they grew up with, and in some cases how other people read their body or appearance — and those unchosen memberships still shape how others treat them and how they see the world. 2. When a person belongs to a group, they typically feel more favourable toward their own group than toward other groups, often without deciding to — this can operate automatically, below conscious intention. | I belong to groups I did not choose, and those groups shape both how the world treats me and how I see the world — in ways that are often invisible until I actively look for them. | **[REVISED v3]** The teacher notices the student, in classroom discussion or a reflective written task, naming a specific unchosen group membership they hold (for example: the family they were born into, the first language they grew up with, the nationality on their passport, or how others read their body or appearance) and giving a specific example of how that membership has shaped one of their own experiences — where the example is not a repetition of a class discussion example offered by a peer or teacher. | **Precision** — background shapes reactions → unchosen group membership shapes experience. | Tajfel, H., & Turner, J. C. (1979). An integrative theory of intergroup conflict. In W. G. Austin & S. Worchel (Eds.), *The Social Psychology of Intergroup Relations.* Brooks/Cole. |
| **E** | **[REVISED v2 — Option 1]** 1. The cultural lens concept: every interpretive framework is shaped by cultural context. 2. Ethnocentrism: the tendency to evaluate other cultures by one's own standards, operating even when the evaluator believes they are being objective. 3. Social identity theory: people derive part of their self-concept from group memberships and typically evaluate their in-group more favourably than out-groups, partly automatically. 4. Intersectionality: a person's social position is shaped by multiple overlapping dimensions whose interaction produces experiences that single-dimension analysis misses. | My cultural lens is not neutral — it is one specific angle, not the view from nowhere. Recognising it does not make it disappear, but it changes what I can do with it. | The teacher notices the student voluntarily identifying how their cultural background might be limiting or distorting their interpretation of a text, event, or interaction — with specificity — in contexts where this is not explicitly required. | **Transfer** — structured prompted analysis → self-initiated identification of lens effects. | Geertz, C. (1973). *The Interpretation of Cultures.* Basic Books. |
| **F** | 1. Personal identity vs. social identity — both dynamic negotiations rather than fixed states. 2. Code-switching: adjusting language, behaviour, and expression across cultural contexts — both a competency and, when involuntary, a source of documented psychological cost. | Identity is not something I find — it is something I actively negotiate, and that negotiation never finishes. Who I am in one context and who I am in another are both genuinely me. | The teacher notices the student engaging with perspectives that challenge their own identity framework — including uncomfortable ones — without dismissing them or retreating to a fixed position, and without projecting their own resolution process onto peers navigating different questions. *(Supplementary: a structured reflective portfolio piece can evidence the K/U layer.)* | **Independence and depth** — supported analysis → self-initiated negotiation across contexts with genuine stakes. | Schwartz, S. J., Luyckx, K., & Vignoles, V. L. (Eds.). (2011). *Handbook of Identity Theory and Research.* Springer. |

**Authoring Notes:**
- **Classification (v2):** Authoritative Knowledge Type is T3 — Dispositional per `lt-1-3-personal-identity-cultural-self-awareness-v1.md`. The Session 3 consolidated index T2 entry was an error and has been corrected. Criterion bank entries for this LT require regeneration per `REAL_Wellbeing_criterion_bank_audit_20260423.md`.
- **Band D grain (v2, Option 1):** Full named concepts "social identity theory" and "intersectionality" are held at Band E. Band D introduces the underlying claims (unchosen group membership; automatic in-group preference) without the university-grade vocabulary. Tajfel & Turner retained as warrant for Band D because the claim space is Tajfel-derived even without the named construct.
- Band F code-switching Know item — "documented psychological cost" is important but potentially sensitive in an international school where many students code-switch involuntarily.
- **[REVISED v3]** Band D Do — v2 wording ("genuine reflection rather than surface performance") replaced with a behavioural anchor specified by Christodoulou in QA Step 8: the student names a specific unchosen group membership and gives a specific example of how it shapes one of their own experiences, where the example is not a repetition of a class discussion example. Companion observation-indicator exemplar library authored at `LT_1_3_observation_exemplar_library_20260423.md` (Band D and Band F).

---

## KUD 4 of 19 — LT 2.1 — Focused Attention & Strategy

**Routing note:** null

**LT Definition:** I can apply attention strategies to sustain focus on demanding tasks, identify what supports or disrupts my attention, and evaluate the effectiveness of different strategies across contexts.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Scenario-based tasks, reflective writing, and strategy-evaluation reports are all appropriate evidence formats.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** None directly. LT 6.1 — **soft enabler (conceptual accelerator)** from Band C onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | Know content for this band lives in LT 6.1 Band A (body signals including tiredness and restlessness). | My attention wanders, and I can bring it back. | I can complete a short sustained-attention task using my senses to stay on it, and describe one thing I did when my attention wandered. | Baseline — no prior band. | Posner, M. I., & Rothbart, M. K. (2007). *Educating the Human Brain.* American Psychological Association. |
| **B** | Know content for this band lives in LT 6.1 Band B (how sleep and stress affect thinking). | Attention is affected by what's going on around me and inside me, and some conditions help more than others. | I can use a practised attention strategy during a task and describe, in writing or conversation, what made it easier or harder to stay focused. | **Complexity** — attention wanders → attention has identifiable supports and disruptors. | Rueda, M. R., Pozuelos, J. P., & Cómbita, L. M. (2015). Cognitive neuroscience of attention. *AIMS Neuroscience*, 2(4), 183–202. |
| **C** | Know content for this band lives in LT 6.1 Band C (prefrontal cortex function; neuroplasticity). | Strategies work through specific mechanisms, and knowing the mechanism helps me choose the right strategy for the situation. | I can evaluate how an attention strategy affected my focus during a specific task in a written reflection, and explain why the strategy did or didn't help, referencing the mechanism. | **Reasoning** — observation → mechanism. **Precision** — general supports → specific strategy-effects. | Flavell, J. H. (1979). Metacognition and cognitive monitoring. *American Psychologist*, 34(10), 906–911. |
| **D** | Know content for this band lives in LT 6.1 Band D (stress-emotion-attention-habit integration). | The things that pull my attention away are often more informative about what I need than about the task itself. | I can sustain attention during a challenging task, identify in writing what pulled my attention away, and describe the deliberate strategy I used to return. | **Reasoning** — mechanism-awareness → diagnostic use. **Transfer** — chosen strategies → in-context adjustment. | Mark, G. (2023). *Attention Span.* Hanover Square Press. |
| **E** | Know content for this band lives in LT 6.1 Band E (attention as a system-level resource). | Attention management is an environment-design problem as much as a personal-discipline problem, and my physical and digital environment shapes what my attention can do. | I can design the conditions for sustained attention in a piece of my own work — including managing digital distractions — and produce a written evaluation of how different attentional strategies interacted with different types of tasks. | **Complexity** — single-task strategy → multi-domain environment design. **Reasoning** — diagnostic → design-oriented. **Transfer** — attention strategy → attention environment. | Ward, A. F., Duke, K., Gneezy, A., & Bos, M. W. (2017). Brain drain: The mere presence of one's own smartphone reduces available cognitive capacity. *Journal of the Association for Consumer Research*, 2(2), 140–154. |
| **F** | Know content for this band lives in LT 6.1 Band F (integrative attention science; cognitive load and expertise). | Attention is a limited resource that must be strategically protected, not just reactively managed — and knowing how my best attention works is a professional and personal asset. | I can audit my attentional patterns across a sustained period of high-stakes work, produce a written analysis identifying the conditions and strategies that most reliably support my best work, and propose specific adjustments to my workflow. | **Independence** — full self-direction. **Reasoning** — in-session adjustment → longitudinal audit. **Scope** — single task → sustained period. | Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review*, 100(3), 363–406. |

**Authoring Notes:**
- Band D Understand (distraction as information) is the pedagogically richest move — worth highlighting in teacher briefing.
- Band E digital-environment design integrates with LT 8.3 practice at the same band.
- MYRIAD caveat: frame mindfulness-style strategies as one tool, not a universal solution.

---

## KUD 5 of 19 — LT 2.2 — Reflective Decision-Making

**Routing note:** null

**LT Definition:** I can reflect on a situation, weigh options and trade-offs, justify my decision with reference to values and evidence, and remain open to revising it.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Written decision analyses, scenario responses, case-study reasoning tasks.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** None directly. LT 1.1 — **soft enabler**. LT 6.2 — **soft enabler** from Band C.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | Know content for this band lives in LT 6.1 Band A. | I can learn from what I did. | I can retell a short experience orally or in a drawing-plus-sentence format, and state one thing I learned from it. | Baseline — no prior band. | Dewey, J. (1933). *How We Think.* D. C. Heath. |
| **B** | Know content for this band lives in LT 6.1 Band B. | Most choices have upsides and downsides, and thinking about both before deciding gives me a better chance of choosing well. | I can complete a simple before-after decision reflection: stating one helpful and one harmful possible outcome before making a choice, and writing one sentence afterwards about what happened. | **Complexity** — single outcome → dual outcomes. **Reasoning** — reflection → anticipation. | Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus and Giroux. |
| **C** | Know content for this band lives in LT 6.1 Band C. | Good decisions consider more than one option and are grounded in what matters to me, not just what's easiest or most obvious. | I can complete a written three-option comparison for a decision I face, state my choice, and give a reason that references a named personal value. | **Complexity** — two outcomes → multiple options. **Reasoning** — outcomes → values. | Schwartz, S. H. (2012). An overview of the Schwartz theory of basic values. *Online Readings in Psychology and Culture*, 2(1). |
| **D** | Know content for this band lives in LT 6.1 Band D. LT 6.2 Band C provides evidence vocabulary. | Decisions rarely have a single right answer, and justifying a choice requires being honest about what I'm trading off and for whom. | I can write a structured decision analysis of a real or realistic scenario that names the trade-offs involved and considers how the decision affects at least two different stakeholders or affected parties. | **Reasoning** — values-grounding → trade-off analysis. **Scope** — self → others affected. | Kohlberg, L. (1981). *The Philosophy of Moral Development.* Harper & Row. |
| **E** | Know content for this band lives in LT 6.1 Band E and LT 6.2 Band D. | The process that produces a decision matters as much as the decision itself — good reasoning under uncertainty is evaluable even before the outcome is known. | I can write a decision analysis that identifies at least one cognitive bias or assumption likely to be affecting my reasoning, describes an adjustment I made to my process to reduce its impact, and evaluates the quality of the reasoning independent of the outcome. | **Reasoning** — trade-off analysis → meta-reasoning. **Precision** — stakeholder consideration → process quality. | Evans, J. S. B. T. (2008). Dual-processing accounts of reasoning, judgment, and social cognition. *Annual Review of Psychology*, 59, 255–278. |
| **F** | Know content for this band lives in LT 6.1 Band F and LT 6.2 Band F. | Mature decision-making is not certainty — it is the ability to act wisely under uncertainty while maintaining intellectual honesty about what I do not know and openness to changing my view. | I can construct a reasoned written position on a complex, contested, and high-stakes decision: weighing multiple types of evidence, acknowledging irreducible uncertainty, making the logic of my choice explicit, and naming what would cause me to revise. | **Reasoning** — process quality → wisdom under uncertainty. **Independence** — structured framework → self-constructed. **Transfer** — scenarios → consequential real-world decisions. | Sternberg, R. J., & Glück, J. (Eds.). (2019). *The Cambridge Handbook of Wisdom.* Cambridge University Press. |

**Authoring Notes:**
- Band F "name what would cause me to revise" is the Popperian falsifiability move and strongest end-state — guards against using reflection to dress up an already-made decision.
- Band E "evaluate decision framework by reasoning not outcome" is counter-intuitive and requires careful teaching — this is the pedagogical centerpiece of Band E.

---

## KUD 6 of 19 — LT 3.1 — Health Literacy & Habits

**Routing note:** null

**LT Definition:** I can identify what my body needs to feel well, design and adjust habits to meet those needs, and evaluate the quality of health information and the conditions that shape what is possible for me.
**Knowledge Type:** T2 — Horizontal (with embedded T1 Know layer at Bands A, E, F).
**Do Evidence Type:** Performance. Habit design documents, tracked data + written reflection, source comparisons, redesign analyses.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** LT 6.1 — **soft enabler** at A–B, **conceptual accelerator** at B, **hard prerequisite** at C+ (habit-loop mechanism is logically required). LT 6.2 — **soft enabler** from Band D onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. The body needs sleep, food, water, movement, and hygiene routines to stay well. 2. Hygiene routines include washing hands before eating and after toilet, brushing teeth twice a day, and bathing regularly. | My body needs specific things to feel well. | I can name my body's basic needs using a labelled diagram or sentence-frame reflection, and follow a simple personal hygiene routine with supportive reminders. | Baseline — no prior band. | World Health Organization. (2022). *School health services: a call for action.* WHO. |
| **B** | 1. Sleep, food, and movement affect how a person feels the next day — not only physically but in mood, focus, and patience. 2. A daily habit has more cumulative effect on how someone feels than a single big change. | How I feel day-to-day is shaped by what I do consistently, not just once. | I can explain in writing or speech how sleep, food, and movement affect how I feel, and set one specific healthy-habit goal using a template. | **Reasoning** — needs → consistency. **Transfer** — momentary needs → patterned practice. | Wood, W., & Rünger, D. (2016). Psychology of habit. *Annual Review of Psychology*, 67, 289–314. |
| **C** | Know content for this band lives in LT 6.1 Band C (habit loop mechanism; neuroplasticity; cue-routine-reward cycle). | Habits break down for specific reasons, and noticing the reason is the first step in adjusting the habit. | I can track one habit for a week (paper log or Strive), write a short analysis identifying one specific barrier to consistency, and explain why I want to keep or change it. | **Complexity** — pattern → pattern with barriers. **Reasoning** — observation → causal analysis. | Fogg, B. J. (2019). *Tiny Habits.* Houghton Mifflin Harcourt. |
| **D** | Know content for this band lives in LT 6.1 Band D and LT 6.2 Band C–D. | Designing for my life means planning for the real conditions I live in, including the ones that disrupt me, rather than an idealised version of myself. | I can write a comparative analysis of two health information sources, create a balanced weekly habits plan that accounts for known obstacles, and document adjustments made based on logged results. | **Scope** — single habit → balanced plan. **Reasoning** — reactive adjustment → anticipatory design. | Gollwitzer, P. M. (1999). Implementation intentions. *American Psychologist*, 54(7), 493–503. |
| **E** | 1. Social determinants of health — income, neighbourhood, food access, cultural norms, parental work patterns — shape what healthy habits are realistically available. 2. Evidence-quality criteria: strength of study design, sample size, replication, and whether claims are about populations or individuals. | Health habits sit inside a social and structural context that shapes what is possible for me — and honest health literacy means understanding both what I can change personally and what requires conditions I do not control alone. | I can write an analysis identifying the structural and social factors affecting my access to healthy habits, evaluate health claims in two sources using evidence-quality criteria, and produce a redesigned habits plan that accounts for conditions I cannot individually control. | **Scope** — personal plan → social/structural context. **Reasoning** — anticipatory design → structural analysis. **Complexity** — individual habits → health equity awareness. | Marmot, M. (2005). Social determinants of health inequalities. *The Lancet*, 365(9464), 1099–1104. |
| **F** | 1. Sustainable behaviour change operates at the systems level — environmental design, social norms, policy, availability of resources — as much as the individual level. 2. Critical health literacy distinguishes personal-agency factors from structural-enablement factors in health outcomes. | Long-term health is not a product of willpower alone — it is enabled or disabled by the environments, relationships, and systems surrounding individuals, and understanding this is what makes health literacy genuinely critical. | I can produce a designed health maintenance approach sustainable across the demands of adult life, accounting for competing priorities, social pressures, and systems-level constraints, and articulate in writing why sustainable habits require external conditions, not only personal willpower. | **Independence** — self-directed across complexity. **Reasoning** — structural analysis → critical health literacy. **Transfer** — student life → adult life contexts. | Nutbeam, D. (2008). The evolving concept of health literacy. *Social Science & Medicine*, 67(12), 2072–2078. |

**Authoring Notes:**
- Hard prerequisite at Band C is load-bearing: LT 6.1 Band C (habit loop) must be in place before Band C Do is meaningful.
- Strive integration most useful at Bands C–E.
- Band E structural determinants expansion is the key developmental move.

> **REAL-specific terms used in this chart (for external readers):**
> - *Strive* — REAL's habit-tracking application; provides process evidence only, not outcome evidence, for T3 LTs.

---

## KUD 7 of 19 — LT 3.2 — Self-Care & Resilience

**Routing note:** null

**LT Definition:** I can notice early warning signs from my body and mind, apply self-care responses that work in the conditions of my life, maintain them under pressure, and build a personal resilience framework over time.
**Knowledge Type:** T3 — Dispositional.
**Do Evidence Type:** Disposition. Third-person observation indicators throughout. Strive longitudinal data supports but does not substitute for cross-context observation.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** LT 3.1 — **soft enabler** throughout. LT 6.1 — **soft enabler** at Bands A–B, **conceptual accelerator** from Band C onward. LT 1.2 — **soft enabler** from Band D onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. A trusted adult is someone whose job or role is to help keep a child safe (parent, teacher, school counsellor, named family adult). 2. A self-care routine includes handwashing before eating and after toilet, brushing teeth twice daily, drinking water, and resting when tired. | Asking for help is a normal part of taking care of myself, not something that happens only when something is wrong. | The teacher notices the student naming a specific trusted adult they could go to for help, and carrying out a simple self-care routine with supportive reminders, on most occasions when it is needed. | Baseline — no prior band. | Rickwood, D., Deane, F. P., Wilson, C. J., & Ciarrochi, J. (2005). Young people's help-seeking for mental health problems. *Australian e-Journal for the Advancement of Mental Health*, 4(3), 218–251. |
| **B** | 1. Early warning signs the body gives before someone is fully overwhelmed include tiredness, headache, irritability, tight chest or tummy, and losing interest in things that normally feel enjoyable. 2. A short break, water, fresh air, movement, or naming a feeling are self-care responses that can reduce activation before it escalates. | My body signals before my mind catches up, and responding early is more effective than responding late. | The teacher notices the student naming a bodily early-warning sign in themselves — fatigue, irritability, a specific tension pattern — and selecting a practised self-care response before activation escalates, across multiple occasions. | **Complexity** — external help-seeking → self-noticing. **Precision** — generic care → signal-responsive care. | McEwen, B. S. (1998). Stress, adaptation, and disease: Allostasis and allostatic load. *Annals of the New York Academy of Sciences*, 840, 33–44. |
| **C** | 1. Trusted people and services available to students at this school include the school counsellor, the school nurse, named teachers, parents or family adults, and external services appropriate to the jurisdiction. 2. Different contexts (home, school, online) often require different self-care strategies because of what is available and what causes stress in each. | Self-care has to work in the actual conditions of my life, and knowing who to turn to is as important as knowing what to do for myself. | The teacher notices the student articulating — spontaneously or on brief prompt — a self-care plan with context-specific strategies for both home and school, and naming two or more trusted people or services they could turn to for support, across multiple occasions. | **Scope** — single context → multiple contexts. **Complexity** — self-care → self-care plus support networks. | Cohen, S., & Wills, T. A. (1985). Stress, social support, and the buffering hypothesis. *Psychological Bulletin*, 98(2), 310–357. |
| **D** | Know content for this band lives in LT 6.1 Band D (HPA axis, stress-system integration) and LT 1.2 Band D (relational repair and offering perspective-aware support). | Self-care practices are most valuable precisely when they are hardest to do, and helping others maintain theirs strengthens rather than depletes my own. | The teacher notices the student sustaining their key self-care routines through genuinely stressful periods (assessment window, social friction, demanding project) without adult scaffolding, AND, on at least one observed occasion, offering a peer a specific non-directive form of support. | **Reasoning** — maintenance → maintenance-under-pressure. **Transfer** — self-focused → mutual. | Neff, K. D. (2003). Self-compassion: An alternative conceptualization of a healthy attitude toward oneself. *Self and Identity*, 2(2), 85–101. |
| **E** | Know content for this band lives in LT 6.1 Band E (allostatic load and chronic stress mechanisms) and LT 3.1 Band E (structural and social determinants of what self-care is realistically available). | Sustainable resilience is grounded in a realistic view of my own limits — knowing when to extend myself and when to rest is as important as the ability to persevere. | The teacher notices the student sustaining self-care through extended pressure periods without prompting, seeking help when their own strategies are insufficient (neither too early nor too late), and participating in peer-group self-care norms in a way that registers as authentic rather than performative, across more than one context. | **Independence** — peer-supported → fully self-directed. **Reasoning** — mutual support → self-knowledge of limits. **Precision** — broad self-care → calibrated to personal thresholds. | Fletcher, D., & Sarkar, M. (2013). Psychological resilience: A review and critique of definitions, concepts, and theory. *European Psychologist*, 18(1), 12–23. |
| **F** | Know content for this band lives in LT 6.1 Band F (integrative stress neuroscience and allostatic load over life course) and LT 7.2 Band F (metacognitive self-direction as personal framework). | Resilience is not a trait I either have or lack — it is a system I have built, which I can describe, maintain, and continue to develop in adult life. | The teacher or mentor notices the student articulating — in a Reflection 360 conversation or spontaneous reflection — their personal resilience framework: non-negotiable self-care commitments, early-warning signals, recovery protocols, and how this framework has developed across their years at school, unprompted and with specificity. | **Independence** — full. **Reasoning** — calibrated self-knowledge → authored personal system. **Transfer** — school contexts → adult-life preparedness. **Scope** — routines → framework. | Richardson, G. E. (2002). The metatheory of resilience and resiliency. *Journal of Clinical Psychology*, 58(3), 307–321. |

**Authoring Notes:**
- Bands A–C carry a real Know layer, not cross-reference. Deliberate design choice — children at these bands need concrete facts before they can enact the disposition.
- Band D Understand ("hardest to do is when it matters most") confirmed as disposition-oriented not aspirational.
- Strive longitudinal data is useful process evidence at Bands C–E but cannot substitute for multi-informant observation.
- Band E "without making it performative" is observer-calibration-sensitive.
- Band F "across years at school" presumes continuity — viable at REAL; adjustable for high-mobility cohorts.

> **REAL-specific terms used in this chart (for external readers):**
> - *Reflection 360* — structured reflective conversation between student and teacher or mentor, conducted periodically across the year.
> - *Strive* — REAL's habit-tracking application; provides process evidence only, not outcome evidence, for T3 LTs.

---

## KUD 8 of 19 — LT 4.1 — Bodies, Boundaries & Consent

**Routing note:** null

**LT Definition:** I can recognise and respect bodily autonomy — my own and others' — apply consent skills across everyday, sexual, online, and institutional contexts, analyse power and pressure dynamics, and support others in understanding their rights and options.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Written scenario analyses, structured roleplay, rubric-assessed facilitation. Specialist delivery recommended from Band C.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** LT 1.2 — **soft enabler** throughout. LT 5.1 — **soft enabler** from Band B onward. LT 6.1 — **conceptual accelerator** from Band D onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. Anatomically correct names for private body parts (penis, vulva, vagina, bottom, chest), taught matter-of-factly using the same register as other body parts. 2. A trusted adult in this school is a named specific person — a class teacher, the school counsellor, the school nurse, or a designated family adult. | My body is mine, and there are specific people whose job is to help keep it safe. | I can name private body parts using correct terminology in a short scenario-response task, identify at least two trusted adults in my specific context (home and school), and state one situation in which I would tell a trusted adult. | Baseline — no prior band. | Dwyer, S. C., & Letourneau, M. J. (2013). *Child Abuse Review*, 22(6), 412–426. |
| **B** | 1. Consent means clear, freely-given agreement to what is happening — a "yes" that is not a result of pressure, confusion, or fear of what will happen if the answer is "no". 2. Pressure sounds like repeated asking after a "no", reminders of what will be lost if the answer stays "no", making the person feel unkind or childish, or invoking friendship or loyalty to shift the answer. | Everyone has a right to say yes or no, and healthy relationships honour that right every time, not only when the person asking feels like it. | I can complete a written scenario analysis identifying whether consent was freely given, unclear, or overridden by pressure, and describe what a clear request, a clear answer, and a help-seeking response sound like. | **Complexity** — safety → reciprocal autonomy. **Precision** — general safety awareness → consent vocabulary. | Beres, M. A. (2007). *Feminism & Psychology*, 17(1), 93–108. |
| **C** | 1. Consent applies beyond sexual contexts — borrowing belongings, physical touch, taking or sharing photos, and forwarding messages all require agreement. 2. Online consent is specific: permission to send a photo is not permission to share it; agreement in a private message is not agreement to screenshot and redistribute. 3. Clear boundary-statement language to peers includes naming the behaviour, naming the limit, and naming the ask — "When you X, I need you to Y." | Consent is the same principle across every kind of interaction, not a special rule for one area — which means it shows up in everyday choices, not only in big moments. | I can complete a scenario-response task that applies consent reasoning to non-sexual, physical, and online scenarios, and state a specific clear boundary to a peer in a structured roleplay. | **Transfer** — named safety contexts → everyday, physical, and online contexts. **Complexity** — sexual/safety frame → any-interaction frame. | boyd, d. (2014). *It's Complicated.* Yale University Press. |
| **D** | 1. Power imbalance occurs when one person has more age, status, role authority, peer-group standing, or control over outcomes than the other — and those imbalances affect how freely a "yes" or "no" can be given. 2. An exit plan is a pre-rehearsed line and action for leaving a situation (a specific phrase to say, a specific place to go, a specific person to contact) — prepared before pressure hits, not during. 3. Confidential help routes include the school counsellor, a trusted teacher, and — depending on jurisdiction and age — a GP or youth health service. | Power and pressure affect what feels possible to say, not just what is technically allowed — and recognising the dynamic is part of being able to refuse, exit, or help someone else do either. | I can complete a written analysis of a pressure scenario that names the specific power or peer-pressure dynamics at play, states a refusal and a prepared exit plan in direct language, and describes how I would support a peer to access confidential help. | **Complexity** — reciprocal consent → power-aware consent. **Scope** — self → peer support. **Reasoning** — recognising pressure → naming the dynamic. | Haste, H. (2013). *Palgrave Handbook of Childhood Studies.* |
| **E** | 1. Legal consent thresholds (jurisdiction-appropriate): age of consent in Hungary is 14 (with specific conditions); grooming is recognised in Hungarian criminal law; image-based abuse laws apply to non-consensual sharing. 2. Grooming patterns include targeted isolation, escalating secrecy, flattery followed by implicit exchange, and gradual normalisation of contact outside appropriate boundaries. 3. Institutional power contexts — teacher/student, coach/athlete, employer/employee, older-peer/younger-peer — carry structural consent-constraints recognised in safeguarding policy and law. 4. Rights and reporting pathways in this jurisdiction include specific confidential services, the role of Mandatory Reporters, and what happens when a disclosure is made. | Consent exists in legal, ethical, and relational dimensions that do not always align — understanding where they diverge, and whose interests are protected in each, is part of sophisticated consent literacy. | I can complete a written analysis of a coercion, grooming, or exploitation scenario (online or institutional) that applies the relevant legal framework, evaluates the institutional context, and drafts a non-directive, trauma-aware response to a friend disclosing a similar situation. | **Precision** — refusal strategy → legal/ethical literacy. **Scope** — dyadic/peer → institutional and digital. **Reasoning** — power-recognition → rights-based analysis. | Herman, J. L. (2015). *Trauma and Recovery.* Basic Books. |
| **F** | 1. Myths commonly requiring correction in consent education include: "silence means yes"; "if they didn't say no, it was consent"; "once given, always given"; "clothing or drinking signals consent"; "asking for consent kills the mood." 2. Principles of facilitation with younger peers: maintain age-appropriate language, use open questions rather than leading ones, avoid explicit personal disclosure, name feelings of discomfort as legitimate, and refer rather than counsel when someone discloses. 3. Rights-based framing holds consent as a positive right grounded in bodily autonomy, not only a prohibition against harm. | Consent education is not a one-time lesson but an ongoing cultural practice — and people who understand it well are positioned to model, teach, and protect it in the communities they belong to. | I can facilitate a rubric-assessed 20-minute structured discussion about consent, power, and boundaries with peers or younger students that applies age-appropriate language, surfaces and corrects at least two common myths using evidence, and closes with a rights-based framing. | **Independence** — self-directed and outward-facing. **Transfer** — personal literacy → community-level contribution. **Reasoning** — rights-based analysis → educational facilitation. **Scope** — individual → community/cultural. | Fine, M., & McClelland, S. I. (2006). *Harvard Educational Review*, 76(3), 297–338. |

**Authoring Notes:**
- Band E legal content is jurisdiction-specific; Hungarian thresholds require teacher-lead verification against current criminal code.
- Specialist delivery required C–F.
- Band A Know is deliberately direct (anatomically correct body-part names) — evidence-based; parent communication in unit plan.
- Band F facilitation rubric needs separate design with worked exemplars.
- Myth list at Band F non-exhaustive; select three to five locally relevant.

---

## KUD 9 of 19 — LT 4.2 — Puberty, Health & Safe Choices

**Routing note:** null

**LT Definition:** I can understand the changes of puberty, assess risks to my reproductive, sexual, and substance-use-related health, access trustworthy health information and confidential support, and critically evaluate contested claims in this domain.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Written scenario analyses, explanation tasks, critical evaluations. Specialist delivery required at Bands C, D, E, and F.
**Band Scope:** B–F. Band A N/A — puberty and sexual-health content is developmentally inappropriate for ages 5–7. *(Band B ages 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** LT 6.2 — **hard prerequisite** from Band C onward. LT 6.1 — **soft enabler** from Band C onward. LT 4.1 — **soft enabler** throughout.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | N/A. | N/A. | N/A — not applicable at this developmental stage. | — | — |
| **B** | 1. Physical changes of puberty include growth spurt, body-hair growth, increased oil production and acne, body-odour onset, breast development and menstruation (for those with ovaries), and genital growth, voice change, and first ejaculation (for those with testes). 2. Emotional changes include mood fluctuations linked to hormone changes, increased desire for privacy, and changing relationship dynamics with parents and peers. 3. Puberty hygiene includes daily washing, using deodorant, washing hair regularly, changing clothes after sweating, and using appropriate menstrual products. 4. A reliable puberty-information source is one authored by qualified health professionals and non-commercial. | My body will change in predictable ways during puberty, and knowing what to expect makes the changes less confusing and easier to respond to. | I can complete a written or oral explanation identifying at least five physical and two emotional changes of puberty, describe an appropriate personal hygiene routine, and name two reliable health information sources for puberty questions. | Baseline for this LT. | Tanner, J. M., & Davies, P. S. W. (1985). *The Journal of Pediatrics*, 107(3), 317–329. |
| **C** | 1. Reproductive anatomy: ovaries produce eggs; testes produce sperm; the uterus is where a fertilised egg can implant and develop. 2. Human reproduction at age-appropriate level. 3. Criteria distinguishing a trusted health source from an unreliable one: named qualified author, transparent evidence base, non-commercial, currency, consistency with major health-body guidance. 4. Puberty-specific hygiene routines by body type. | My body is changing in ways I can understand scientifically, and scientific understanding is more useful than rumour or fear for making sense of what is happening. | I can complete a written explanation of human reproduction at an age-appropriate level, describe the hygiene routines relevant to my own pubertal development, and apply stated criteria to distinguish a trusted health source from an unreliable one in a short source-comparison task. | **Complexity** — changes → biological mechanisms. **Precision** — general awareness → mechanism-based explanation. | UNESCO. (2018). *International Technical Guidance on Sexuality Education* (Rev. ed.). |
| **D** | 1. STIs transmit through unprotected sexual contact; common STIs (chlamydia, gonorrhoea, HPV, HSV, HIV); many asymptomatic; testing primary identification route. 2. Pregnancy risk can result from any unprotected penile-vaginal sex; probability varies but never zero. 3. Protection methods: condoms; hormonal contraception; emergency contraception. 4. Substance-use risks: alcohol, nicotine dose-dependent adolescent-brain vulnerabilities; cannabis-mental-health risks in susceptible individuals; polysubstance use multiplies risks non-linearly. 5. Confidential health access in Hungary (unit-plan verification). | Decisions about bodies and relationships involve real risks that can be understood and reduced, and knowing how to access confidential help is part of being able to make informed choices. | I can complete a written scenario-based risk-assessment task covering STI, pregnancy, and substance-use scenarios, identify the relevant protection methods for each, and describe specific steps for accessing confidential health advice in this jurisdiction. | **Reasoning** — mechanism → risk assessment. **Scope** — self → access to confidential support. **Complexity** — hygiene and reproduction → full risk domain. | Kirby, D. (2007). *Emerging Answers 2007.* |
| **E** | 1. Healthcare navigation. 2. Young person's rights in Hungary (unit-plan verification). 3. Evidence-based SRH guidelines (WHO, NICE/national clinical, BMJ Best Practice). 4. How to evaluate SRH information against a named guideline. | My reproductive and sexual health is my own responsibility and right — accessing accurate information and appropriate support is not something I should need to depend on someone else to arrange for me. | I can complete a written analysis of a reproductive or sexual-health question that identifies the relevant healthcare service, states the access pathway and confidentiality conditions in this jurisdiction, and evaluates at least two information sources against stated evidence-based guideline criteria. | **Independence** — accessed with support → independently navigated. **Precision** — protection methods → rights and system navigation. **Reasoning** — risk assessment → healthcare agency. **Transfer** — individual risk → broader health system. | WHO. (2014). *Health for the World's Adolescents.* |
| **F** | 1. Examples of contested SRH claims (unit-plan curation). 2. Commercial and institutional interests in SRH. 3. Ideological framings in SRH discourse. 4. Principles of critical appraisal in SRH. | Sexual and reproductive health is a contested terrain where evidence, culture, politics, and personal values intersect — mature health literacy means being able to navigate this complexity without either uncritical acceptance or cynical dismissal of evidence. | I can construct a written critical evaluation of a contested SRH claim that weighs the quality of evidence on each side, identifies the ideological, cultural, or commercial interests shaping the discourse, acknowledges what remains uncertain, and articulates my reasoned personal position. | **Reasoning** — healthcare agency → critical health literacy. **Complexity** — individual claims → contested discourse. **Transfer** — personal decisions → cultural and political literacy. **Independence** — fully self-directed. | Fine, M., & McClelland, S. I. (2006). *Harvard Educational Review*, 76(3), 297–338. |

**Authoring Notes:**
- Jurisdictional facts in Bands D, E, F require verification against current Hungarian law/guidelines.
- Specialist delivery required from Band C.
- Band F contested-claim selection requires deliberate curation.
- Band D substance-use framing should be harm-reduction; confirm with school administration.

---

## KUD 10 of 19 — LT 4.3 — Active Bystander & Anti-Discrimination

**Routing note:** null

**LT Definition:** I can identify when a situation involves discrimination, exclusion, or targeted harm, assess what a safe and proportionate bystander response would be, and justify my reasoning about when and how to act or seek help.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Written and oral scenario analyses, comparative evaluations, and structured case studies. Deliberately scoped to *reasoning*; enacted disposition not assessed here.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** **[REVISED v2]** **LT 1.2 — soft enabler at Bands A–B, hard prerequisite from Band C onward.** LT 6.1 — **soft enabler** at Band A–B, **conceptual accelerator** from Band C onward. LT 4.1 — **soft enabler**.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. Who counts as a trusted adult in this school context (teacher, counsellor, playground supervisor, family adult). 2. Language for describing what happened: "They were left out." / "Someone was unkind to them." / "They weren't allowed to play." | When someone is hurt or left out, it matters to tell a grown-up — I don't have to fix it myself. | I can complete a short scenario-response (oral or drawing-plus-sentence) that describes a situation where someone was left out or treated unkindly, names what I saw, and identifies a specific trusted adult I could tell. | Baseline — no prior band. | Olweus, D. (1993). *Bullying at School.* Blackwell. |
| **B** | 1. Common forms of exclusion or unfair treatment at this age. 2. Helpful actions available to a Band B student. 3. The person affected is the one who decides whether something was unkind. | Unkindness isn't always the same as an accident — what's "just a joke" to one person can really hurt another, and the person affected is the one who knows which it was. | I can complete a written or oral scenario-response task that describes what happened when someone was excluded or treated unfairly, suggests how the person might have felt, and selects one helpful action from a short list of options with one-sentence reasoning for my choice. | **Complexity** — noticing → noticing + attributing feeling. **Reasoning** — report → choice of response with reasoning. | Salmivalli, C. (2010). *Aggression and Violent Behavior*, 15(2), 112–120. |
| **C** | 1. Forms of exclusion and discrimination. 2. The four bystander response options: **direct / distract / delegate / delay**. 3. A safety check before direct intervention. | There are several ways to help in a hard situation, and the best one depends on whether I can stay safe, not on whether I feel brave. | I can complete a written scenario-response task that identifies the form of exclusion or discrimination present, assesses whether it is safe to intervene directly, and names and justifies my choice from the four bystander options. | **Complexity** — single form → several forms. **Precision** — general helpful action → named response type from a framework. **Reasoning** — choice → safety-weighted choice. | Latané, B., & Darley, J. M. (1970). *The Unresponsive Bystander.* Appleton-Century-Crofts. |
| **D** | 1. Forms of discrimination (racism, sexism, homophobia/transphobia, ableism, religious/cultural). Know content for stress-response lives in LT 6.1 Band D. Power-dynamics content lives in LT 4.1 Band D. 2. Group dynamics factors in bystander situations. 3. What the targeted person may need. | Discrimination isn't just one person being mean — it's behaviour shaped by group norms and power differences, and naming the dynamic is part of responding well. | I can complete a written analytical task on a bystander scenario that identifies the forms of discrimination present, names the specific group and power dynamics at play, and justifies a proposed response based on safety, proportionality, and what the targeted person is likely to need. | **Reasoning** — safety-weighted choice → multi-criterion justification. **Complexity** — individual action → group and power dynamics. **Scope** — what to do → what the targeted person likely needs. | Haste, H. (2013). *Palgrave Handbook of Childhood Studies.* |
| **E** | 1. Know content for stress-response lives in LT 6.1 Band E. 2. Bystander effect research (Darley & Latané 1968). 3. Group-norm factors (pluralistic ignorance). 4. Institutional context factors. | My instinct to freeze or go along in a discrimination situation isn't cowardice but a predictable response to group pressure and stress — and knowing that is how I can plan around it rather than blame myself for it. | I can complete a written evaluation that compares two or more possible responses to a discrimination scenario, identifies my own likely default response and its probable sources, and explains how specific group norms and institutional context factors shape which interventions are possible or effective. | **Reasoning** — multi-criterion justification → meta-reasoning about own defaults. **Scope** — interpersonal → contextual and institutional. **Transfer** — scripted scenario → self-analysis. | Darley, J. M., & Latané, B. (1968). *Journal of Personality and Social Psychology*, 8(4), 377–383. |
| **F** | 1. Systems-level analysis lives in LT 6.1 Band F and LT 8.2 Band E–F. 2. Conditions associated with higher bystander intervention rates. 3. Principles of ethical intervention design. | Whether bystanders act isn't mainly about individual courage — it's about the conditions a group or institution creates, and changing those conditions is more powerful than asking individuals to be braver. | I can construct a written or presented analysis of a real bystander success or failure (self-selected, my own or another's), evaluate what made effective intervention possible or impossible in that specific context, and propose specific group, school, or community-level conditions that would make active bystander response more likely, with reasoning grounded in bystander research. | **Reasoning** — context analysis → systems-level. **Independence** — scenario-prompted → self-directed case selection. **Scope** — individual response → systemic conditions. | Banyard, V. L., Moynihan, M. M., & Plante, E. G. (2007). *Journal of Community Psychology*, 35(4), 463–481. |

**Authoring Notes:**
- **Prerequisite (v2):** LT 1.2 downgraded to soft enabler at Bands A–B per panel review; basic notice-and-tell at A–B develops in parallel with empathy, not gated on prior mastery. Hard prerequisite from Band C onward where four-response framework logic genuinely requires LT 1.2's perspective-taking.
- Band E "my own likely default response" requires psychologically-safe, non-judgemental framing.
- Four-response framework introduced at Band C.
- Band F own-case analysis is clinically sensitive; preserve option of third-party case study.
- Discrimination registers vary by national origin; unit plans must not privilege one national register.

---

## KUD 11 of 19 — LT 5.1 — Interpersonal Skills & Communication

**Routing note:** null

**LT Definition:** I can communicate clearly and respectfully across contexts — including disagreement, conflict, and significant difference — by asking about boundaries, listening actively, calibrating my words to the situation, and facilitating the conversation process when the situation calls for it.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Rubric-assessed roleplays, scenario-response tasks, facilitated conversations.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** LT 1.2 — **soft enabler** throughout. LT 1.1 — **soft enabler** from Band C onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. I-statement structure. 2. Kind words versus hurtful words. 3. Turn-taking cues. | How I talk to someone doesn't just describe what I feel — it shapes what happens next in the conversation. | I can complete a short observed roleplay in which I take turns in conversation, use kind language, and apply an I-statement when something bothered me — followed by a brief verbal reflection on my word choice. | Baseline — no prior band. | Gordon, T. (1970). *Parent Effectiveness Training.* |
| **B** | 1. Needs-expression stems. 2. Boundary-asking stems. 3. Proposing fair options. | Being clear about what I need, and curious about what others need, makes working things out easier than trying to guess or push. | I can complete a structured roleplay or scenario-response that uses an I-statement to state a specific need, asks about the other person's boundaries using a named stem, and proposes two options for a fair solution with one-sentence reasoning. | **Complexity** — politeness → needs-expression plus boundary-asking. **Precision** — kind words → named technique. | Rosenberg, M. B. (2015). *Nonviolent Communication* (3rd ed.). |
| **C** | 1. The repair routine — four named steps. 2. Respectful word choice under disagreement: name behaviour not character. 3. Active listening markers. | Staying in a conversation when I disagree is a different skill than avoiding it — and it's one I have to practise, not one I'm supposed to have automatically. | I can complete a rubric-assessed roleplay of a disagreement in which I listen without interrupting, respond using language that names behaviour not character, and apply the four-step repair routine when the moment calls for it. | **Reasoning** — expression → regulated expression. **Scope** — agreement → disagreement. | Zehr, H. (2002). *The Little Book of Restorative Justice.* |
| **D** | 1. Paraphrasing technique. 2. Situation-calibrated word choice. 3. Clear boundary-stating language for high-stakes contexts. Self-regulation content lives in LT 1.1 Band D. | Communication quality matters most when stakes are high — the same skills that work in calm conversations need to be deliberately applied in difficult ones, not assumed. | I can complete a rubric-assessed conflict roleplay or scenario-based analysis in which I state a clear boundary, paraphrase the other person's position before responding, and demonstrably calibrate my word choice to a specific described context. | **Transfer** — calm contexts → conflict contexts. **Precision** — respectful words → situation-calibrated words. | Stone, D., Patton, B., & Heen, S. (2010). *Difficult Conversations.* |
| **E** | 1. Facilitation techniques. 2. The facilitator role. Stress/group-dynamics content lives in LT 6.1 Band E and LT 1.2 Band E. | Facilitating a group conversation under disagreement requires a different role than participating — the facilitator holds the process, not the positions. | I can facilitate a rubric-assessed 15-minute structured group conversation in which participants disagree on a substantive question, managing the process rather than the positions, ensuring all voices are heard, and maintaining a constructive tone across the session. | **Complexity** — dyadic conflict → group facilitation. **Scope** — peer → multi-stakeholder. **Independence** — participant → process-holder. | Schwarz, R. M. (2017). *The Skilled Facilitator* (3rd ed.). |
| **F** | 1. Cross-cultural communication variables. 2. Power-dynamics factors (cross-ref LT 4.1 Band D–E). 3. Adjusting register without losing perspective. | Communicating across significant difference isn't about giving up my own perspective — it's about recognising the conditions that make genuine dialogue possible and creating them deliberately. | I can complete a rubric-assessed communication task across significant difference (cultural, generational, or positional) in which I adjust my register and tone to the context without losing my own perspective, and demonstrate in written reflection my awareness of the power dynamics shaping who gets heard. | **Transfer** — intra-group → cross-difference. **Reasoning** — situation-calibration → power-aware dialogue design. **Precision** — calibrated words → identity-aware register. **Independence** — full. | Bennett, M. J. (2013). *Basic Concepts of Intercultural Communication* (2nd ed.). |

**Authoring Notes:**
- Band A Understand was rewritten from source.md's "How I talk to people affects how they feel" (flagged as restating Do) — new version adds generative claim.
- Repair routine at Band C specified as four named steps; REAL should specify which variant and maintain consistency.
- Band E facilitation is ambitious for ages 13–15; rubric should reflect achievable scope via structured protocols.
- Band B Rosenberg (NVC) warrant slightly stretched; Nelsen (2006) *Positive Discipline* as alternate.

---

## KUD 12 of 19 — LT 5.2 — Community Engagement & Purpose

**Routing note:** null

**LT Definition:** I can contribute meaningfully to communities I belong to — noticing what's needed, acting with others, reflecting on impact, and developing a personal sense of purpose over time.
**Knowledge Type:** T3 — Dispositional.
**Do Evidence Type:** Disposition. Third-person observation indicators throughout. Evidence aggregated across D2R project records, Light Dragon capstone work (primary Band D evidence), and Reflection 360 conversations.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** LT 1.2 — **soft enabler** throughout. LT 5.1 — **soft enabler** from Band B onward. LT 7.2 — **soft enabler** from Band F onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | Light local Know: names of specific classroom jobs available; what each job does to help the class run. | I'm part of a group, and what I do makes a difference to it. | The teacher notices the student carrying out their classroom job on most occasions without needing reminders, and articulating — when asked or spontaneously — how that job helps the class function. | Baseline — no prior band. | Baumeister, R. F., & Leary, M. R. (1995). *Psychological Bulletin*, 117(3), 497–529. |
| **B** | Light local Know: signs someone might be left out. | Belonging is something groups create on purpose, not something that just happens — and I can help create it. | The teacher notices the student spontaneously including a peer who appears left out, on multiple occasions across varied group contexts (classroom, playground, collaborative work). | **Complexity** — passive membership → active inclusion. | Juvonen, J. (2006). Sense of belonging, social bonds, and school functioning. In *Handbook of Educational Psychology* (2nd ed.). |
| **C** | Light local Know: the structure of D2R project design — identify the need, propose, plan, do, reflect. Team collaboration content lives in LT 5.1 Band C. | Making something happen in a community is a practice — noticing what's missing, proposing a response, and following through with others — not a moment of inspiration. | The teacher notices the student, across at least one D2R project cycle, identifying a real school need unprompted, contributing to a team proposal, and following through on their share of the work to completion. | **Complexity** — inclusion → initiative. **Reasoning** — participation → project completion. | Damon, W., Menon, J., & Bronk, K. C. (2003). *Applied Developmental Science*, 7(3), 119–128. |
| **D** | Light local Know: what makes a group "diverse" in the REAL context; what "impact" means as distinct from "completion". Working-across-difference content lives in LT 1.2 Band D and LT 5.1 Band D. | What I contribute to community is part of who I'm becoming, and working across difference strengthens what's possible, not just what I know. | The teacher notices the student, through their Light Dragon capstone or extended D2R work, collaborating substantively with team members different from themselves (background, perspective, skill), engaging with evidence of whether their project made a difference, and articulating why the work matters to them personally — in Reflection 360 or unprompted conversation. | **Scope** — homogeneous team → diverse team. **Reasoning** — project completion → reflective purpose. **Transfer** — doing → identity. | Bronk, K. C. (2013). *Purpose in Life.* Springer. |
| **E** | Know content lives in LT 6.1 Band E and LT 5.1 Band E. Light local Know: distinction between community action (changeable by participants) and structural conditions (requiring institutional change). | Sustained community engagement requires understanding the systems that shape what is possible — and knowing those limits isn't defeatism but honest civic literacy. | The teacher or mentor notices the student leading a sustained initiative (beyond a single project cycle) addressing a genuine need, navigating specific institutional and relational obstacles as they arise, and articulating — in Reflection 360 or unprompted — both the impact of what was achieved and the limits that institutional context imposed. | **Independence** — collaborative participant → initiative leader. **Reasoning** — reflective purpose → systemic understanding. **Scope** — single project → sustained initiative. **Complexity** — project outcomes → institutional navigation. | Youniss, J., McLellan, J. A., & Yates, M. (1997). *American Behavioral Scientist*, 40(5), 620–631. |
| **F** | Know content lives in LT 7.2 Band F. Light local Know: distinction between purpose-as-role (what I do) and purpose-as-orientation (what I stand for); stability and revision in purpose over time. | Purpose is not discovered once — it is developed through accumulated engagement and reflection, and leaving school with a clear sense of it is one of the most significant outcomes of a wellbeing education. | **[REVISED v2]** The teacher or mentor notices — across Reflection 360 and the preceding two years of engagement — that the student's post-school choices (path, community involvement, roles) trace specifically to prior sustained engagement, and that when asked about purpose the student points to that engagement with specificity rather than to abstracted articulation. | **[REVISED v2]** **Independence** — full. **Reasoning** — systemic understanding → purpose traceable in choices. **Transfer** — school community → life beyond school. **Scope** — initiative → life direction. Evidence: engagement history + choices, not articulation alone. | Damon, W. (2008). *The Path to Purpose.* Free Press. |

**Authoring Notes:**
- Band F Do (v2) reweights the primary observable from articulation to traceability between prior sustained engagement and observable post-school choices. Articulation remains present as supporting evidence (the student points to engagement with specificity when asked) but is not the rubric anchor.
- Band D dependence on Light Dragon capstone is load-bearing. Source.md flagged this; confirmed.
- Band B "identifies when someone is left out" overlaps with LT 4.3 Band B — distinct indicators (LT 5.2 = spontaneous inclusion; LT 4.3 = reasoning through bystander situations). Observation protocols should distinguish.
- Observer calibration needed Bands D–F to distinguish authentic responses from rehearsed ones.
- Mid-entry students (high student mobility) need accommodated assessment pathway.

> **REAL-specific terms used in this chart (for external readers):**
> - *D2R* — REAL's "Design to Realise" project structure: identify-need → propose → plan → do → reflect.
> - *Light Dragon capstone* — REAL's Grade 7–8 (Band D) capstone project.
> - *Reflection 360* — structured reflective conversation between student and teacher or mentor, conducted periodically across the year.
> - *Dragon naming (Water, Air, Earth, Fire, Metal, Light, Post-Metal)* — REAL developmental band naming convention.

---

## KUD 13 of 19 — LT 6.1 — Brain, Body & Wellbeing Science

**Routing note:** null

**LT Definition:** I can explain the mechanisms behind stress, emotion, attention, and habit using accurate scientific vocabulary, and apply that understanding to evaluate claims about the brain, body, and wellbeing interventions.
**Knowledge Type:** T1 — Hierarchical. Later bands require specific factual content from earlier bands.
**Do Evidence Type:** Performance. Rubric-assessed explanation tasks, written evaluations, vocabulary checks.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** None (foundational). **Downstream:** LT 6.1 is a **hard prerequisite** for LT 6.2, LT 4.2 (Bands C+), LT 8.2 (Bands C+); a **conceptual accelerator** for LT 1.1, LT 2.1, LT 3.1, LT 3.2, LT 4.3, LT 7.1, LT 7.2, LT 8.3.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. Body signals (heart beating fast, tight tummy/chest, feeling hot/shaky, tiredness, hunger, thirst). 2. Sleep helps the body rest and grow; deep sleep sorts and stores learning. 3. Food gives the body and brain fuel. | My body gives me information about how I feel before I think about it. | I can complete a rubric-assessed oral or written explanation task that names at least three body signals and what each typically indicates, and describes in my own words what sleep and food do for the body and brain. | Baseline — no prior band. | Craig, A. D. (2002). *Nature Reviews Neuroscience*, 3(8), 655–666. |
| **B** | 1. Fight-flight-freeze response. 2. The amygdala detects threat and triggers this response. 3. Habits run on a three-part loop: **cue → routine → reward**. | My body's stress response happens automatically to protect me, and my habits run as a repeated loop — neither is a choice in the moment. | I can complete a rubric-assessed written or oral explanation that describes what happens in the body during a fight, flight, or freeze response, and explains the three parts of the habit loop using my own example. | **Complexity** — one mechanism → two mechanisms. | Sapolsky, R. M. (2004). *Why Zebras Don't Get Ulcers* (3rd ed.). |
| **C** | 1. The **amygdala** as threat-detection region. 2. The **prefrontal cortex**: planning, self-control, weighing options. 3. **Neuroplasticity** (Hebb's rule). 4. Habit-loop mechanism at mechanism level. | Specific brain structures have specific functions, and my brain changes in response to what I repeatedly practise or experience. | I can complete a rubric-assessed written explanation that describes how the amygdala and prefrontal cortex interact during a stressful moment, explains neuroplasticity in my own words with a concrete example, and describes how the habit loop explains behaviour change at mechanism level. | **Precision** — general mechanism → structure-specific. **Transfer** — mechanism description → applied to own change. | Doidge, N. (2007). *The Brain That Changes Itself.* |
| **D** | 1. Core neuroscience vocabulary: amygdala, prefrontal cortex, hippocampus, basal ganglia, hypothalamus, pituitary, adrenal glands, cortisol, dopamine, ANS. 2. The **HPA axis**: hypothalamus → pituitary → adrenal glands → cortisol. 3. Stress/attention/habit system interactions. 4. Dopamine anticipates reward. | Stress, emotion, attention, and habit are not separate domains I can work on one at a time — they operate as an interdependent system where a change in one affects the others. | I can complete a rubric-assessed written explanation that uses accurate neuroscience vocabulary to describe how stress, emotion, attention, and habit interact as a system, and explains the role of the HPA axis in the stress response. | **Reasoning** — single mechanisms → system-level integration. | McEwen, B. S. (2007). *Physiological Reviews*, 87(3), 873–904. |
| **E** | 1. **Allostatic load**. 2. Acute vs chronic stress. 3. Adolescent-brain specifics. 4. Criteria for evaluating a neuroscience claim. | Understanding a mechanism is useful only if I can apply it — applying neuroscience means evaluating claims made in its name, not just restating the system. | I can complete a rubric-assessed written evaluation of a specific wellbeing intervention, explaining its proposed mechanism, summarising what the evidence suggests about its effectiveness, and articulating what it would and would not change in the stress-emotion-attention-habit system. | **Transfer** — system description → applied evaluation. **Reasoning** — system-level → critical application. **Precision** — mechanism vocabulary → intervention-evaluation vocabulary. | Dahl, R. E., Allen, N. B., Wilbrecht, L., & Suleiman, A. B. (2018). *Nature*, 554(7693), 441–450. |
| **F** | 1. Affective neuroscience debates. 2. Named cases of popular misrepresentation. 3. Contested areas in adolescent mental-health research. 4. Principles of critical neuroscience literacy. | Neuroscience is a developing field with unresolved debates, and the gap between research findings and popular application is often large — mature wellbeing literacy includes knowing where the science is solid, contested, or simply unknown. | I can construct a rubric-assessed critical essay on a contested claim in wellbeing science that identifies where the evidence is strong, where it is uncertain, where popular accounts have oversimplified or misrepresented research, and states my reasoned position with specific evidence. | **Reasoning** — critical application → scientific literacy. **Complexity** — evaluating single interventions → evaluating contested fields. **Transfer** — classroom knowledge → critical reading of research. **Independence** — full. | Choudhury, S., & Slaby, J. (Eds.). (2012). *Critical Neuroscience.* Wiley-Blackwell. |

**Authoring Notes:**
- Band F contested-areas list is time-sensitive.
- Band E intervention-evaluation task — rubric should reward honest assessment over confident advocacy.
- Band D vocabulary list non-exhaustive but represents core terminology load.
- Band C Understand is the pedagogically central move.
- Scaffolding concern: LT 6.1 gaps cascade; mid-entry students may need a catch-up pathway.

---

## KUD 14 of 19 — LT 6.2 — Health Information Literacy

**Routing note:** null

**LT Definition:** I can evaluate health information and health claims for trustworthiness, evidence quality, and bias — applying progressively more sophisticated analytical criteria across bands to make informed decisions about what to believe and act on.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Written analyses, comparative source tasks, structured evaluations, systematic-review interpretation tasks.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** **LT 6.1 — hard prerequisite** from all bands.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. A trusted adult for health questions is a specific named person. 2. Check with a trusted adult before believing a health claim. | Some people know more about health than others, and asking a specific person whose job is to know is a skill I can use on purpose. | I can complete a short rubric-assessed oral or written task in which I am presented with a simple health claim, and I identify whether it came from a trusted source, who I would ask, and why. | Baseline — no prior band. | Sperber, D., et al. (2010). *Mind & Language*, 25(4), 359–393. |
| **B** | 1. A reliable source names its qualified author. 2. A reliable source is transparent about its evidence. 3. A reliable source discloses funding. | Where a piece of health information came from matters at least as much as what it says. | I can complete a rubric-assessed written task comparing two health information sources on the same topic, stating which I trust more and naming two specific reasons from the three reliability criteria (author, evidence origin, funding/transparency). | **Complexity** — ask-an-adult epistemics → source-characteristic epistemics. **Reasoning** — authority-based trust → criterion-based trust. | Wineburg, S. (2021). *Why Learn History.* University of Chicago Press. |
| **C** | 1. Types of evidence: **anecdote / correlation / controlled study**. 2. Common bias indicators. | Different kinds of evidence carry different weight, and the person making a health claim almost always has something at stake. | I can complete a rubric-assessed written analysis of a single health claim that names the evidence type, names any bias indicators present, and justifies my conclusion about how much weight to give the claim. | **Complexity** — source-level → evidence-type and bias. **Precision** — trust/distrust → named evidence types and named bias indicators. **Reasoning** — source-trust → claim-analysis. | Ioannidis, J. P. A. (2005). *PLOS Medicine*, 2(8), e124. |
| **D** | 1. **Evidence hierarchy**. 2. **Signals of stronger/weaker arguments**. 3. **Principles of critical appraisal**. | Health claims frequently contradict each other, and judging them well is a matter of weighing the quality of the evidence rather than the certainty of the tone. | I can complete a rubric-assessed written evaluation of a contested health claim (two or more sources disagreeing) that applies the evidence hierarchy, identifies the specific strongest and weakest arguments on each side, and justifies my conclusion with reference to the criteria of critical appraisal. | **Reasoning** — single-claim analysis → comparative evaluation. **Complexity** — one claim → contested discourse. **Transfer** — applied across unfamiliar contested domain. | Greenhalgh, T. (2019). *How to Read a Paper* (6th ed.). |
| **E** | 1. **Peer review** and its limitations. 2. **Clinical trial design** (RCT — what it proves and doesn't). 3. **Relative vs. absolute risk**; statistical significance; confidence intervals. 4. **Funding and publication biases**. | Health information is produced inside systems — funding, commercial interests, publication incentives, peer-review imperfections — and strong health literacy means being able to think about how that system shapes what reaches me. | I can complete a rubric-assessed written analysis of an evidence base supporting a specific health claim (not a single study — the cumulative research) that judges whether the body of evidence warrants the confidence placed in the claim, identifies the commercial or institutional interests that may have shaped what research was done and published, and justifies my conclusion using peer-review, RCT-design, statistical, and funding-bias criteria. | **Reasoning** — individual claims → research-production systems. **Scope** — source-level → research-production. **Precision** — critical-appraisal → methodological evaluation. | Ioannidis, J. P. A. (2008). *Epidemiology*, 19(5), 640–648. |
| **F** | 1. **Reading a systematic review or meta-analysis** (PICO, risk-of-bias, forest plot, I², GRADE). 2. **GRADE framework**. 3. **Regulatory bodies** (WHO, NICE, EMA, Hungarian bodies). 4. **Guidelines are contested when...** | The distance between an individual research finding and a public-health guideline I am advised or required to follow is long and politically mediated — critical health literacy at the highest level is being able to trace that journey and judge its integrity. | I can complete a rubric-assessed analysis that (a) reads and interprets a provided systematic review or meta-analysis at an introductory level, (b) traces how a named policy recommendation or guideline was derived from an evidence base, and (c) evaluates whether that guideline is well-supported, weakly-supported, or contested. | **Reasoning** — evidence-base assessment → evidence-to-policy tracing. **Complexity** — research production → research synthesis and guideline translation. **Transfer** — consumer → near-professional critical reading. **Independence** — full. | Guyatt, G. H., et al. (2008). GRADE. *BMJ*, 336(7650), 924–926. |

**[REVISED v2]** *Hungarian regulatory bodies named at Band F (OGYÉI, NÉBIH) require confirmation at unit-plan stage — institutional restructuring is periodic.*

**Authoring Notes:**
- Band E Know item 3 (relative vs. absolute risk) is pedagogically pivotal but cognitively demanding. Worked examples required in unit plan.
- Band F systematic-review task scoped to "introductory level" deliberately.
- Funding-bias content at Band E taught without cynicism collapse.
- LT 6.1 dependency escalates by band; mid-entry students missing LT 6.1 Bands C+ will struggle with LT 6.2 Bands C+.

---

## KUD 15 of 19 — LT 7.1 — Pattern Analysis & Adjustment

**Routing note:** null

**LT Definition:** I can notice a pattern in my own thinking or behaviour, analyse what drives and sustains it, design and track a specific adjustment, and build this into a structured personal metacognitive practice.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Rubric-assessed reflective tasks, structured metacognitive protocols, portfolio entries.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** **[REVISED v3]** **LT 1.1 — soft enabler** throughout. **LT 2.2 — soft enabler** throughout. **LT 6.1 Band C — hard prerequisite for LT 7.1 Band D.** Students cannot meaningfully distinguish the origin of a personal pattern from its sustaining conditions (the Band D analytical move) without the stress-response mechanism knowledge that LT 6.1 Band C provides (amygdala / prefrontal-cortex interaction under stress; neuroplasticity; habit-loop mechanism). **LT 6.1 Bands C–D — conceptual accelerator** for LT 7.1 at Bands C and E–F.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | **[REVISED v3]** 1. There are two different kinds of thinking: thinking about *what* I did and thinking about *how* I did it. The second kind — noticing how I did something — is called thinking about my own thinking. *(Neuroscience Know content for this band continues to live in LT 6.1 Band A.)* | **[REVISED v3]** Thinking about *how* I did something — not just *what* I did — helps me choose what to do next time. | I can complete a rubric-assessed short oral or written reflection in which I describe one specific thing I noticed about how I reacted to a given situation and state one thing I might do differently next time. | Baseline — no prior band. | Flavell, J. H. (1979). *American Psychologist*, 34(10), 906–911. |
| **B** | **[REVISED v3]** 1. A pattern is a response I make in a similar way in similar kinds of situations. When something happens the same way more than once, that repetition is information about me that I can use. *(Neuroscience Know content for this band continues to live in LT 6.1 Band B.)* | **[REVISED v3]** Most of what I do in similar situations isn't random, and noticing that my responses repeat changes what I can do next time. | I can complete a rubric-assessed written or oral task in which I identify a specific pattern in how I tend to respond in a named type of situation, and offer one plausible reason for why that pattern might have formed. | **Complexity** — single-instance reflection → pattern recognition. **Precision** — "I reacted" → named recurring response to a named type of trigger. | Wilson, T. D. (2002). *Strangers to Ourselves.* |
| **C** | **[REVISED v3]** 1. A *driver* of a pattern is a specific thing that sets the pattern off or keeps it going — a cue, an emotion, a context, or a belief. Finding the driver is what turns noticing a pattern into a deliberate adjustment. *(Neuroscience Know content for this band continues to live in LT 6.1 Band C.)* | **[REVISED v3]** Identifying what drives a pattern is what opens up the choice to adjust it; without a named driver, an attempted change has nothing specific to act on. | I can complete a rubric-assessed written analysis of a pattern across two or more situations that names the pattern specifically, identifies what drives it (cue, emotion, context, belief), and describes a specific adjustment I have made or will make based on the analysis. | **Reasoning** — pattern-noticing → causal analysis. **Transfer** — observation → deliberate change. **Scope** — single situation → across more than one situation. | Zimmerman, B. J. (2000). *Handbook of self-regulation.* |
| **D** | **[REVISED v3]** 1. The *origin* of a pattern (what originally set it up) and its *sustaining conditions* (what keeps it going now) are two different things. An adjustment that only addresses the origin can fail to change the pattern if the sustaining conditions remain in place. *(Neuroscience Know content for this band continues to live in LT 6.1 Band D, which is hard-prerequisite for this band.)* | **[REVISED v3]** Lasting change has to address what now sustains a pattern, not only what first set it up. | I can complete a rubric-assessed written analysis that evaluates a pattern in my thinking or responses across different contexts, distinguishes what originally set up the pattern from what now sustains it, describes a specific adjustment I have implemented, and reports the effect observed. | **Reasoning** — causal analysis → origin-vs-sustaining distinction. **Scope** — one context → multiple contexts. **Transfer** — planned adjustment → evaluated adjustment. | Wood, W., & Neal, D. T. (2007). *Psychological Review*, 114(4), 843–863. |
| **E** | **[REVISED v3]** 1. A *structured metacognitive protocol* is a named sequence of steps applied in advance to a high-stakes challenge: (a) map typical patterns, (b) identify sustaining conditions, (c) design a specific intervention targeting those conditions, (d) track the intervention's effects across a defined period, and (e) iterate based on what the tracking shows. It differs from everyday reflection in being named, defined in advance, and tracked rather than recalled. *(Neuroscience Know content for this band continues to live in LT 6.1 Band E.)* | **[REVISED v3]** Applying a structured protocol to high-stakes work requires being honest about patterns that are uncomfortable to see, and holding myself accountable to the specific adjustments I committed to — which is why a protocol produces different evidence from everyday reflection. | I can complete a rubric-assessed structured metacognitive protocol applied to a named high-stakes academic or personal challenge, comprising: (a) a mapping of my typical patterns, (b) an identification of sustaining conditions, (c) a specific intervention designed against those conditions, (d) a tracking record of the intervention's effects over a defined period, and (e) an iteration based on what the tracking showed. | **Complexity** — everyday reflection → high-stakes structured protocol. **Precision** — general analysis → named protocol with distinct phases. **Reasoning** — sustaining-conditions analysis → designed-and-tracked intervention with iteration. | Zimmerman, B. J., & Schunk, D. H. (Eds.). (2011). *Handbook of Self-Regulation of Learning and Performance.* |
| **F** | **[REVISED v3]** 1. A *personal metacognitive framework* is an explicit, named set of strategies, prompts, and monitoring practices that a person has developed and tested across more than one domain. Unlike a single protocol applied to a single challenge, a framework is portable — it can be carried into any new domain. It consists of (a) strategies the person has chosen deliberately, (b) prompts that trigger their use, and (c) monitoring practices that check whether they are working. *(Neuroscience Know content for this band continues to live in LT 6.1 Band F and LT 6.2 Band F.)* | **[REVISED v3]** A personal metacognitive framework is not a school skill applied only inside a classroom — it is the mechanism by which I continue to learn, adjust, and develop in any domain I enter next. | I can construct a rubric-assessed personal metacognitive framework document: a named, explicit set of strategies, prompts, and monitoring practices I have developed and tested across at least two domains, with evidence of testing and iteration, and an articulated application plan for the next phase of my learning and life beyond school. | **Reasoning** — structured protocol → authored personal framework. **Transfer** — school tasks → cross-domain and post-school. **Scope** — single domain → cross-domain portability. **Independence** — full. | Kegan, R. (1994). *In Over Our Heads.* |

**Authoring Notes:**
- **[REVISED v3]** Standalone Know at each band carries LT 7.1's metacognitive terminology (pattern, driver, origin/sustaining conditions, structured metacognitive protocol, personal metacognitive framework). The neuroscience Know content continues to live in LT 6.1 and is cross-referenced per band; the two Know strands are distinct and are not duplicated.
- **[REVISED v3]** LT 6.1 Band C is a **hard prerequisite** for LT 7.1 Band D (stress-response mechanism knowledge is required for the origin-vs-sustaining distinction). This replaces the v2 conceptual-accelerator typing at this specific prerequisite pair. Other LT 6.1 → LT 7.1 couplings remain conceptual accelerators.
- Band E "honesty about uncomfortable patterns" is pedagogically pivotal; held in Understand, not rubric.
- Band F framework construction graded on evidence of real testing and iteration, not document polish.
- Relationship to LT 7.2 is intentional T2/T3 split.
- **Claxton dissent (QA Step 6, 23 April 2026): cross-referencing Know to LT 6.1 is correct curriculum hygiene — metacognitive work should build on neuroscience rather than duplicate it. Adding a standalone Know layer risks producing a second content strand where one was intentional. This dissent is recorded; the Know-layer addition was adopted on the basis of Christodoulou and Koedinger's structural-assessability argument.**

---

## KUD 16 of 19 — LT 7.2 — Self-Direction in Practice

**Routing note:** null

**LT Definition:** I consistently direct my own thinking and learning — noticing, analysing, and intentionally adjusting my own patterns across time and contexts without external prompting, and supporting others to do the same.
**Knowledge Type:** T3 — Dispositional.
**Do Evidence Type:** Disposition. Third-person observation indicators throughout. Multi-informant observation synthesised in Reflection 360. Not summatively graded. No rubric.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** **LT 7.1 — hard prerequisite**. **LT 1.1 — soft enabler** throughout. **LT 6.1 Bands C–D — conceptual accelerator** from Band C onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | None standalone. Know content lives in LT 6.1 Band A. | When something doesn't work, trying differently is a choice I have — not a sign I have failed, and not something that has to happen only if an adult tells me. | The teacher notices the student stopping and trying a different approach when the first attempt does not work, without needing to be told, on most occasions of minor setback across more than one type of task. After a setback, the student names what happened ("I got stuck", "that didn't work because…") rather than dismissing it. | Baseline — no prior band. | Dweck, C. S. (2006). *Mindset.* Random House. [Applied with care — effect sizes in interventions are smaller than single-study reports; see Sisk et al., 2018.] |
| **B** | None standalone. Know content lives in LT 6.1 Band B. | What I've learned about myself only becomes useful when I remember to use it — and remembering is a habit I can build, not a sign of how smart I am. | The teacher notices the student referring back to a strategy they have previously found helpful in a similar type of situation, without being prompted. After a task, the student volunteers one specific observation about how they worked, not a general evaluation of the task. | **Complexity** — in-the-moment adjustment → reference back to prior learned strategy. **Transfer** — single occasion → deliberate reuse. | Barnett, S. M., & Ceci, S. J. (2002). *Psychological Bulletin*, 128(4), 612–637. |
| **C** | None standalone. Know content lives in LT 6.1 Band C. | Pattern-recognition about myself is most valuable when I catch it in the moment — because that is when I can do something about it — not only when I reflect on it afterwards. | The teacher notices the student identifying a pattern in how they respond across more than one situation and naming it spontaneously in conversation, on multiple occasions across a term. In a task, the student adjusts their approach mid-way in response to noticing that something is not working, without teacher prompt. | **Reasoning** — retrospective reflection → real-time pattern-recognition. **Scope** — single-domain → across-domain pattern-naming. | Efklides, A. (2011). *Educational Psychologist*, 46(1), 6–25. |
| **D** | None standalone. Know content lives in LT 6.1 Band D. | Metacognitive self-direction is not a single habit I can check off but a disposition to treat myself as someone I am learning about continuously — a stance, not a technique. | The teacher notices the student articulating a specific adjustment they have made to their thinking or behaviour and describing its effect across more than one domain, without prompting. In novel or challenging situations, the student applies a self-awareness strategy without an adult prompt. The student makes connections between wellbeing learning and behaviour in other contexts unprompted, on multiple occasions. | **Reasoning** — situational strategy use → dispositional stance. **Transfer** — named contexts → unprompted cross-domain. **Scope** — one domain → multiple domains. | Kegan, R. (1994). *In Over Our Heads.* |
| **E** | None standalone. Know content lives in LT 6.1 Band E. | Self-direction is not only about my own development — supporting it in others through questions rather than answers is how a genuine learning community is built. | The teacher notices the student initiating metacognitive reflection without any external prompt across sustained periods of challenging work. When working with peers, the student naturally facilitates the peers' self-reflection through open questions rather than giving advice, on multiple observed occasions. The student demonstrates stable self-directedness when feedback challenges their self-assessment — neither collapsing nor defending. | **Independence** — unprompted in moments → unprompted across sustained periods. **Transfer** — personal practice → modelling and facilitating for others. **Reasoning** — own disposition → community-building. | Wenger, E. (1998). *Communities of Practice.* |
| **F** | None standalone. Know content lives in LT 6.1 Band F and LT 7.1 Band F. | By this band, metacognitive self-direction should be identity-deep — not a set of techniques I apply when I remember but a way of being in relation to my own growth that I carry with me into any context. | The teacher or mentor notices the student demonstrating a stable, articulated metacognitive identity — a consistent pattern of how they learn, reflect, and adjust — that they can describe to others without rehearsing it, and that persists across highly novel, high-stakes, or unfamiliar contexts without any scaffolding. The student connects their wellbeing learning to their sense of who they are and who they are becoming, unprompted and with specificity, on multiple occasions including in Reflection 360. | **Independence** — full across sustained periods → identity-level. **Reasoning** — community-building → identity-as-practice. **Transfer** — all school contexts → any future context. **Scope** — school learning → life beyond school. | Marcia, J. E. (1980). In J. Adelson (Ed.), *Handbook of adolescent psychology.* [Combined with: Claxton, G. (2008). *What's the Point of School?*] |

**Authoring Notes:**
- Relationship to LT 7.1 is load-bearing. A student who is Band D on LT 7.1 can be Band B on LT 7.2 — intentional T2/T3 gap.
- No rubric, no summative grade. Reflection 360 is the synthesis moment.
- Band A warrant uses Dweck with caveat.
- Band E feedback-challenge stability is observer-calibration-sensitive.
- Band F identity depth weighted on behaviour consistency over articulation quality.

> **REAL-specific terms used in this chart (for external readers):**
> - *Reflection 360* — structured reflective conversation between student and teacher or mentor, conducted periodically across the year.

---

## KUD 17 of 19 — LT 8.1 — Information Verification & Media Literacy

**Routing note:** null

**LT Definition:** I can locate a claim in digital or media content, assess its credibility using appropriate criteria, identify signs that it has been manipulated or designed to deceive, and justify what I believe, share, or act on as a result.
**Knowledge Type:** T2 — Horizontal.
**Do Evidence Type:** Performance. Rubric-assessed scenario analyses, comparative source evaluations, written conclusions.
**Band Scope:** A–F. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** **LT 2.2 — soft enabler** from Band C onward. **LT 6.2 — sibling, not prerequisite.**

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | 1. Real vs made-up definitions. 2. Ask a trusted adult when unsure. | Things I see on a screen are not automatically true — people make them up sometimes, and checking with a grown-up is a skill, not a sign I don't know. | I can complete a rubric-assessed short oral or written task in which I am shown an age-appropriate piece of digital content, say whether I think it is real or made up, explain my reasoning in a sentence, and name a trusted adult I would ask. | Baseline — no prior band. | Sperber et al. (2010). *Mind & Language*, 25(4), 359–393. |
| **B** | 1. Every piece of digital content has a **maker**. 2. A **trusted place** has a specific marker. 3. Shares/reactions don't make a claim more true. | Where something came from matters at least as much as what it says. | I can complete a rubric-assessed short written task, given two pieces of digital content on the same topic, in which I identify the maker of each, state whether each maker is from a "trusted place" and why, and explain why I do or do not believe each piece. | **Complexity** — real/made-up → authorship and origin. **Reasoning** — ask an adult → give my own reason. | Wineburg, S. (2021). *Why Learn History.* |
| **C** | 1. **Lateral reading**. 2. **Signs of edited/misleading content**. 3. **Source comparison**. | A claim on its own tells me less than the same claim compared to other sources — and deception usually leaves specific signs I can learn to spot. | I can complete a rubric-assessed written comparison of two sources making the same claim in which I apply lateral reading to find out who is behind each source, name specific manipulation signs present or absent in each, and justify which source I trust more with at least two named criteria. | **Complexity** — single source → comparison. **Precision** — trust/distrust → named manipulation signals. **Reasoning** — own reason → comparative justification. | Wineburg, S., & McGrew, S. (2019). *Teachers College Record*, 121(11), 1–40. |
| **D** | 1. A **verification process** (e.g. SIFT). 2. The **motivation of a source**. 3. **Believe, share, and act** as three different decisions. | What I believe, what I share, and what I act on are three different decisions about the same claim — and treating them as separate is what keeps me from accidentally amplifying something I haven't actually checked. | I can complete a rubric-assessed written analysis of a digital claim in which I apply a named verification process to the claim, identify the origin, the evidence behind it, and the motivation of the source, and justify my separate conclusions about what I would believe, what I would share, and what I would act on. | **Complexity** — comparison → multi-criterion. **Reasoning** — comparative judgement → motivation and verification-process. **Scope** — believe → believe + share + act. | Caulfield, M. (2017). *Web Literacy for Student Fact-Checkers.* |
| **E** | 1. **Recommendation algorithms** optimised for engagement. 2. **Platform incentives**. 3. **Filter-bubble/echo-chamber effects**. 4. **Confirmation bias**. 5. **Motivated reasoning**. | A claim does not arrive in my feed by accident — the system that chose to show it to me, and the mental system that receives it, both have biases I can learn to read. | I can complete a rubric-assessed written evaluation of a contested claim in which I weigh evidence across multiple sources using named criteria, identify at least two specific algorithmic/platform/production-incentive factors, name the self-bias most likely to affect my interpretation, and justify my conclusion with explicit awareness of that bias. | **Scope** — source-level → platform/algorithmic layer. **Reasoning** — motivation → incentive-system analysis. **Precision** — source bias → self-bias awareness. | Pariser, E. (2011). *The Filter Bubble.* Supplemented by: Kahan, D. M. (2013). *Judgment and Decision Making*, 8(4), 407–424. |
| **F** | 1. **Synthetic media**. 2. **Sophisticated disinformation**. 3. **Recognised critical-appraisal criteria**. 4. **Epistemic humility**. | At the highest level of media literacy, knowing what I cannot know — and being specific about the boundary — is a more reliable guide than any verification tool. | I can complete a rubric-assessed written analysis of a real-world contested claim involving synthetic, AI-generated, or sophisticated disinformation, in which I apply detection and verification methods appropriate to the claim, compare my verification process against a recognised critical-appraisal framework, and construct a reasoned conclusion that states what I believe, what I would share, what I would act on, and — specifically — what I cannot know and why. | **Complexity** — contested → synthetic / AI-era. **Reasoning** — own process → meta-evaluation against external standard. **Transfer** — scripted → genuine real-world claim. **Independence** — prompted → self-directed, with explicit epistemic humility. | van der Linden, S., Roozenbeek, J., & Compton, J. (2020). *Frontiers in Psychology*, 11, 566790. Supplemented by: Pennycook, G., & Rand, D. G. (2021). *Trends in Cognitive Sciences*, 25(5), 388–402. |

**Authoring Notes:**
- Platform-neutral framing throughout; SIFT named as example at Band D, not as *the* required protocol.
- Band E self-bias framed as human universal to be worked with.
- Band F warrant pair time-sensitive.
- Synthetic-media detection scoped to "methods include… but no method is reliable" — ages better than naming tools.

---

## KUD 18 of 19 — LT 8.2 — Digital Influence & Psychological Agency

**Routing note:** null

**LT Definition:** I can identify how a digital product or platform is designed to shape attention, emotion, or behaviour, analyse the effect that design is having on me, and justify a reasoned response.
**Knowledge Type:** T2 — Horizontal with substantial embedded T1 Know layer.
**Do Evidence Type:** Performance. Rubric-assessed product/platform analyses and self-analysis tasks.
**Band Scope:** C–F. **Bands A and B N/A.** *(Band C ages 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** **LT 6.1 — hard prerequisite from Band C onward.** **LT 2.1 — conceptual enabler** throughout. **LT 2.2 — soft enabler** from Band E onward.

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | N/A. | N/A. | N/A. | — | — |
| **B** | N/A. | N/A. | N/A. | — | — |
| **C** | 1. **Persuasive design**. 2. **Named persuasive-design features**: infinite scroll, pull-to-refresh, autoplay, notifications, streaks. 3. **Variable reward** (applies LT 6.1 Band C — dopamine). 4. **An "effect on me"** — observable and specific. | Digital products are not neutral tools — they are environments designed to affect how I use my time, attention, and feelings. | I can complete a rubric-assessed short written analysis (200–300 words) of a chosen digital product in which I identify one specific persuasive-design feature using correct vocabulary, describe one reason the design works on people, and explain one specific effect I have noticed on myself. | Baseline for this LT. | Eyal, N. (2014). *Hooked.* [Taught as *object of study*, not endorsement.] |
| **D** | 1. **Vocabulary load for design analysis** (variable reward, intermittent reinforcement, novelty bias, social-validation feedback, dark patterns). 2. **Three dimensions of design effect** — attention / emotion / behaviour. 3. **Attention residue**. 4. **The attention triangle** (from LT 2.1 Band C). | Persuasive design isn't about individual willpower — it is about the environment acting on the person, and the most useful response is environmental rather than effortful. | I can complete a rubric-assessed written analysis of a chosen digital product using the "attention / emotion / behaviour" framework in which I identify at least two interacting persuasive-design features using correct vocabulary, analyse how each shapes attention/emotion/behaviour, and explain one specific effect I have noticed on my own thinking, mood, or time. | **Complexity** — one feature → multiple interacting. **Precision** — general effect → named dimension. **Reasoning** — identify → analyse mechanism. | Mark, G. (2023). *Attention Span.* |
| **E** | 1. **Recommendation algorithms** optimised for engagement. 2. **Engagement-driven amplification**. 3. **The attention economy business model**. 4. **"Surveillance capitalism"**. 5. **Persuasion vs manipulation**. | A claim does not arrive in my feed by accident — the system that chose to show it has specific psychological and economic reasons to choose it, and those reasons are not the same as my interests. | I can complete a rubric-assessed written evaluation of a chosen digital platform in which I evaluate how the platform algorithmically curates what I see, explain at least two specific psychological or economic incentives driving that design decision, and justify one specific change I will make to my use of the platform based on my analysis — including why that change addresses the mechanism, not just the symptom. | **Scope** — product features → platform-level. **Reasoning** — mechanism → incentive-system. **Complexity** — product → platform + business model. | Zuboff, S. (2019). *Surveillance Capitalism.* |
| **F** | 1. **Research domains on digital wellbeing** — Twenge/Haidt vs. Orben/Przybylski debate. 2. Mechanisms most credibly supported. 3. Mechanisms less credibly supported. 4. **Identity effects of sustained platform use**. 5. **"Consent and agency" framing**. | At the most sophisticated level of this capability, the relevant question is not whether these systems affect me but *which specific effects I consent to, which I refuse, and where the line is for me*. | I can complete a rubric-assessed written analysis that evaluates the cumulative effect of persuasive design across a sustained period on my attention, relationships, and identity — drawing on my own evidence, compares my analysis against at least two recognised pieces of research on digital wellbeing including at least one that contests a claim I find sympathetic, and articulates a reasoned personal position specifying where I will and will not allow these systems to operate on me. | **Scope** — single product → cumulative self-impact. **Reasoning** — incentive → research-anchored position. **Independence** — scenario-prompted → self-directed stance. **Transfer** — evaluating features → articulating values-based position. | Orben, A., & Przybylski, A. K. (2019). *Nature Human Behaviour*, 3(2), 173–182. Supplemented by: Haidt, J. (2024). *The Anxious Generation.* [Teacher note: present as active debate.] |

**Authoring Notes:**
- Eyal as object of study, not endorsement.
- Band D attention-triangle cross-reference is load-bearing.
- Band E "mechanism, not just symptom" is the pivotal reasoning move.
- Band F debate-representation non-negotiable — present both sides.
- No platform names in framework text — teachers instantiate with current products.

---

## KUD 19 of 19 — LT 8.3 — Digital Assertiveness & Wellbeing Strategies

**Routing note:** null

**LT Definition:** I maintain healthy boundaries, communicate assertively, and sustain wellbeing-supporting practices inside digital environments across platforms and contexts.
**Knowledge Type:** T3 — Dispositional.
**Do Evidence Type:** Disposition. Multi-informant observation (teacher, parent where possible, peer, self). No rubric. Not summatively graded. Strive contributes process evidence only.
**Band Scope:** A–F. Bands A–B require parental observation as primary evidence source. *(Band A ages 5–7; B 7–9; C 9–11; D 11–13; E 13–15; F 15–17.)*
**Prerequisites:** **LT 1.1 — hard prerequisite** throughout. **LT 5.1 — hard prerequisite** from Band B. **LT 8.2 — conceptual accelerator** from Band C onward. **LT 4.1 — parallel sibling.**

| Band | Know | Understand | Do | Progression lever | Disciplinary warrant |
|---|---|---|---|---|---|
| **A** | Know content lives in LT 6.1 Band A and LT 4.1 Band A. | When something on a screen makes me feel confused or upset, telling a grown-up I trust is what keeps me safe — it is not getting someone in trouble and it is not a sign I did something wrong. | The child stops using a digital device when a trusted adult asks, without significant distress, on most occasions. The child tells a trusted adult when they see or are shown something online that makes them feel confused, scared, or uncomfortable, across more than one observed occasion. The child does not share personal information with strangers in digital contexts. | Baseline — no prior band. | Livingstone, S., Mascheroni, G., & Staksrud, E. (2018). *New Media & Society*, 20(3), 1103–1122. |
| **B** | Know content lives in LT 6.1 Band B and LT 5.1 Band B. | The ways I protect myself in person — saying no, walking away, telling someone — are the same moves I can make online, even when the person is far away and I can't see them. | The child exits digital content they recognise as unkind, distressing, or inappropriate for them, without needing an adult to direct them, on most observed occasions. The child uses simple assertive language in digital communication when a peer behaves unkindly online. The child keeps to family or school rules about device use without constant reminders. | **Independence** — adult-directed → self-directed for content exit. **Transfer** — face-to-face assertiveness → digital context. | Przybylski, A. K., & Nash, V. (2018). *Cyberpsychology, Behavior, and Social Networking*, 21(7), 405–410. |
| **C** | Know content lives in LT 6.1 Band C, LT 8.2 Band C, and LT 5.1 Band C. | A digital boundary I set for myself is different from a rule someone set for me — I can keep it not because I am told to but because I have chosen what kind of digital life I want to have. | The student names their own digital boundaries and largely keeps to them without external reminders, across multiple contexts. The student speaks up or exits group chats, games, or platform interactions where peers behave unkindly, excludingly, or unsafely, on more than one observed occasion. The student takes independent action when content or interaction is affecting their wellbeing — muting, blocking, unfollowing, reporting, stepping away — without adult prompt. | **Independence** — rule-following → self-authored. **Scope** — single setting → multiple contexts. **Precision** — general assertiveness → named specific actions. | Vanden Abeele, M. M. P. (2021). *Communication Theory*, 31(4), 932–955. |
| **D** | Know content lives in LT 6.1 Band D, LT 8.2 Band D, and LT 5.1 Band D. | Self-care in a digital environment is a deliberate practice, not a default — because the environment is actively working against it, my wellbeing-supporting practices have to be designed and sustained on purpose. | The student maintains their stated digital boundaries under social pressure, on more than one observed occasion. The student uses assertive communication in difficult digital interactions without escalating into harshness, abandoning the conversation, or capitulating. The student adjusts their digital practice in response to evidence they have collected about its effects — and can point to the adjustment and the evidence that drove it when asked. | **Reasoning** — general wellbeing response → evidence-driven adjustment. **Transfer** — non-pressured → under-pressure boundary-keeping. **Complexity** — single move → sustained assertiveness. | Alberti, R. E., & Emmons, M. L. (2017). *Your Perfect Right* (10th ed.). |
| **E** | Know content lives in LT 6.1 Band E, LT 8.2 Band E, and LT 5.1 Band E. | Sustained digital wellbeing is not a performance I put on when tracked and drop when not — it is what I actually do, which is why the test is what happens in the ordinary weeks when nobody is watching. | The student sustains digital wellbeing practices across extended periods — not only in a week when someone is tracking, but as an integrated part of their life, across terms. The student holds their position in digital disagreements without becoming harsh, performative, or retreating. The student notices when their digital practice is not serving them well and adjusts proactively — before a crisis or a forced break — on more than one observed occasion across the year. | **Independence** — tracked → untracked periods. **Scope** — individual response → sustained lived practice. **Precision** — assertiveness → substantive (non-performative) assertiveness. | Ryan, R. M., & Deci, E. L. (2017). *Self-Determination Theory.* |
| **F** | Know content lives in LT 6.1 Band F, LT 8.2 Band F, LT 1.3 Band F, and LT 5.1 Band F. | Mature digital agency is an expression of who I am — not a set of rules I follow, not a performance I curate for others, and not a protest I advertise — and the proof is that the way I behave online is the way I behave, full stop. | The student treats their digital life as an expression of their values, and can articulate this stance when asked without turning it into a public performance. The student supports peers navigating digital pressure, conflict, or harm, without taking over the situation, without shaming the peer, and with authentic respect for the peer's own agency. The student holds consistent digital practices across contexts without the quality shifting based on who is watching — teacher-observed, parent-observed, peer-observed, and self-reported behaviours align. | **Independence** — self-directed → identity-integrated. **Transfer** — personal practice → peer support without overreach. **Scope** — behaviour consistency within → across observed and unobserved contexts. | Deci, E. L., & Ryan, R. M. (2000). *Psychological Inquiry*, 11(4), 227–268. Supplemented by: Vanden Abeele (2021). |

**Authoring Notes:**
- Parent input essential at A–B, not supplementary.
- A–B safeguarding indicator on personal information is a safeguarding concern requiring school protocol action — not assessment data.
- Relationship to LT 8.2 load-bearing; student can be Band E on 8.2 while Band C on 8.3.
- "Without performance" at E/F is observer-calibration-sensitive.
- Strive as process evidence only.

> **REAL-specific terms used in this chart (for external readers):**
> - *Strive* — REAL's habit-tracking application; provides process evidence only, not outcome evidence, for T3 LTs.
> - *Reflection 360* — implied in multi-informant T3 evidence aggregation; structured reflective conversation between student and teacher or mentor, conducted periodically across the year.

---

*End of v2 consolidated file.*

*Companion files:*
- *`REAL_Wellbeing_KUD_fixes_applied_20260423.md` — fix log with verbatim current/new text + Step 1 audit table.*
- *`REAL_Wellbeing_criterion_bank_audit_20260423.md` — criterion bank audit; regeneration deferred to separate session.*
