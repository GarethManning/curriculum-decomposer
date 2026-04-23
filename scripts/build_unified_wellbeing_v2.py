"""
Build unified-wellbeing-data-v2.json and wellbeing-index-v2.json from
criterion-bank-v3.json (post-regeneration) and the REAL_Wellbeing_KUD_v2
consolidated chart file (23 April 2026).

Differences from build_unified_wellbeing.py:
  - Reads criterion-bank-v3.json (237 criteria).
  - Writes the -v2 suffixed output files.
  - LT 1.3 knowledge_type is T3 (corrected from prior T2 inheritance).
  - LT 1.3 is added to T3_LTS so observation_indicators are emitted per band.
  - LT 1.3 Band D Know uses the v2 Option-1 two-item rewrite.
  - LT 1.3 Band E Know uses the v2 Option-1 four-item expansion.
  - LT 1.2 Band F Do uses the v2 Step 3b rewrite.
  - LT 5.2 Band F Do uses the v2 Step 3c rewrite.
"""
import json
import datetime

CRIT_BANK_PATH = "docs/reference-corpus/real-wellbeing/criterion-bank-v3.json"
UNIFIED_OUT    = "docs/reference-corpus/real-wellbeing/unified-wellbeing-data-v2.json"
INDEX_OUT      = "docs/reference-corpus/real-wellbeing/wellbeing-index-v2.json"

# ── Load criterion bank ──────────────────────────────────────────────────────
with open(CRIT_BANK_PATH) as f:
    crit_bank = json.load(f)

SCHEMA_VERSION = crit_bank["schema_version"]   # "v2"
ALL_CRIT_IDS   = {c["criterion_id"] for c in crit_bank["criteria"]}

# Build (lt_id, band) → {criterion_ids, observation_indicators}
lt_band_data: dict[tuple, dict] = {}
for c in crit_bank["criteria"]:
    for lt in c.get("associated_lt_ids", []):
        key = (lt, c["band"])
        if key not in lt_band_data:
            lt_band_data[key] = {"criterion_ids": [], "observation_indicators": []}
        lt_band_data[key]["criterion_ids"].append(c["criterion_id"])
        if c.get("observation_indicators"):
            lt_band_data[key]["observation_indicators"].extend(c["observation_indicators"])

# ── KUD content ──────────────────────────────────────────────────────────────
# Structure: lt_id → {meta, bands}
# meta keys: lt_name, competency, knowledge_type, compound, band_range, summary, prereq_lt_ids
# bands keys: band_label → {know:[...], understand:[...], do:str}

KUD: dict[str, dict] = {}

# ── LT 1.1 ──
KUD["lt_1_1"] = {
    "lt_name": "Self-Awareness & Regulation",
    "competency": "C1 — Emotional Intelligence",
    "knowledge_type": "T3",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Notice internal states, apply contextually appropriate regulation strategies, and adjust them based on reflective learning across situations.",
    "prereq_lt_ids": ["lt_6_1"],
    "bands": {
        "A": {
            "know": ["Know content for this band lives in LT 6.1 Band A (basic body signals; what sleep and food do for the body and brain)."],
            "understand": ["My feelings have names, and naming them helps me notice them."],
            "do": "The teacher notices the student pausing to name a feeling before reacting, and selecting a practised calming strategy without needing step-by-step adult direction, on most occasions when emotional activation is visible.",
        },
        "B": {
            "know": ["Know content for this band lives in LT 6.1 Band B (fight/flight/freeze response; habit loop)."],
            "understand": ["What I feel is often set off by something specific, and I can learn what sets me off."],
            "do": "The teacher notices the student naming a recurring personal trigger — time of day, type of task, particular social configuration — and selecting a strategy from their practised repertoire before the trigger escalates, across more than one setting.",
        },
        "C": {
            "know": ["Know content for this band lives in LT 6.1 Band C (amygdala and prefrontal cortex functions under stress; neuroplasticity)."],
            "understand": ["A strategy either works for me or doesn't depending on the situation, and I can tell by checking afterwards."],
            "do": "The teacher notices the student applying a regulation strategy in a genuinely challenging situation (not only in rehearsal) and afterwards explaining — spontaneously or on brief prompt — what worked and what didn't, on multiple occasions across a term.",
        },
        "D": {
            "know": ["Know content for this band lives in LT 6.1 Band D (stress, emotion, attention, and habit as an interdependent system; HPA axis)."],
            "understand": ["How I regulate depends on what's available to me in a given context, and adjusting my approach across settings is how regulation gets more reliable."],
            "do": "The teacher notices the student applying different regulation strategies across different settings (school task pressure, social friction, home reports), explaining without adult prompt why one strategy fits one setting and not another, and naming one concrete change they are going to try next.",
        },
        "E": {
            "know": ["Know content for this band lives in LT 6.1 Bands D–E (system-level neuroscience; interoception and co-regulation mechanisms)."],
            "understand": ["Regulation is not only a personal tool — my emotional state shapes the people around me, and taking responsibility for that is part of mature self-regulation."],
            "do": "The teacher notices the student sustaining their regulation practices through a sustained pressure period (extended assessment window, significant personal difficulty, intense group project) without adult scaffolding, and, unprompted, commenting on how their own state is affecting the group or a specific peer.",
        },
        "F": {
            "know": ["Know content for this band lives in LT 6.1 Band F (integrative neuroscience of regulation, co-regulation, and identity)."],
            "understand": ["A mature regulation system is one I can describe and teach, not merely use — and the capacity to support others' regulation deepens my own."],
            "do": "The teacher or mentor notices the student articulating — in a Reflection 360 conversation or spontaneous reflection — their personal regulation system, the conditions that disrupt it, and adaptations built over time, AND supporting a peer or younger student in developing their own, without adult direction.",
        },
    },
}

# ── LT 1.2 ──
KUD["lt_1_2"] = {
    "lt_name": "Social Awareness & Empathy",
    "competency": "C1 — Emotional Intelligence",
    "knowledge_type": "T3",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Read others' emotional states and perspectives, respond to stated needs, and repair relationships after conflict.",
    "prereq_lt_ids": ["lt_1_1"],
    "bands": {
        "A": {
            "know": ["Know content for this band lives in LT 6.1 Band A (body signals as emotion indicators)."],
            "understand": ["Other people have feelings too, and I can sometimes tell what they are."],
            "do": "The teacher notices the student naming a feeling another person is showing — not only their own — and offering either a kind word or a specific helpful action in response, without adult prompt.",
        },
        "B": {
            "know": ["Know content for this band lives in LT 6.1 Band B (basic emotional cues; fight/flight/freeze signs in others)."],
            "understand": ["The same situation can look different to different people, and asking is more reliable than guessing."],
            "do": "The teacher notices the student describing a situation from another's perspective in words, asking 'do you want help?' before acting, and accepting a 'no' without pushing, on multiple occasions.",
        },
        "C": {
            "know": ["Know content for this band lives in LT 6.1 Band C. LT 5.1 Band C provides communication scaffolding."],
            "understand": ["Other people signal what they need both in what they say and in what they do, and paying attention to both makes me more responsive."],
            "do": "The teacher notices the student attending to multiple group members during shared work, checking in with a direct question when signals are unclear, and adjusting their own actions to match what the other has said they need.",
        },
        "D": {
            "know": ["Know content for this band lives in LT 6.1 Band D. Repair vocabulary draws on LT 5.1 Band D."],
            "understand": ["Conflict is a normal part of relationships, and repair is a specific skill that matters more than avoiding conflict in the first place."],
            "do": "The teacher notices the student, after a conflict, listening without interrupting, naming their own contribution to the situation, and proposing a next step that accounts for the other person's position — not only their own — across more than one occasion.",
        },
        "E": {
            "know": ["Know content for this band lives in LT 6.1 Bands D–E (co-regulation, group stress dynamics)."],
            "understand": ["Conflict in groups is shaped by more than individual feelings — group norms, histories, and power dynamics all affect what is possible in repair."],
            "do": "The teacher notices the student facilitating repair in a group context (not only a dyad), naming a group dynamic that contributed to the conflict, and proposing steps that address needs of multiple parties rather than only defending one position.",
        },
        "F": {
            "know": ["Know content for this band lives in LT 6.1 Band F; structural factor content draws on Humanities Identity, Power & Representation competency."],
            "understand": ["Full empathic understanding requires knowing what shapes a person's context, not only what they say they feel — and sometimes the most empathic response is to address the conditions, not just the person."],
            "do": "The teacher notices the student adjusting their response to someone whose experience is being shaped by structural or systemic factors, in ways that address those conditions rather than only the individual person, across more than one observed occasion.",
        },
    },
}

# ── LT 1.3 ──
KUD["lt_1_3"] = {
    "lt_name": "Personal Identity & Cultural Self-Awareness",
    "competency": "C1 — Emotional Intelligence",
    "knowledge_type": "T3",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Describe identity across contexts, recognise how cultural background shapes values and responses, and maintain stable self across contexts.",
    "prereq_lt_ids": ["lt_1_1", "lt_1_2"],
    "bands": {
        "A": {
            "know": [
                "Different families speak different languages, eat different foods, and celebrate different events — these differences are what we call culture.",
                "Everyone has a home culture: the particular mix of ways, stories, and celebrations they grew up with.",
            ],
            "understand": ["The things my family does at home are part of who I am, and what other families do is part of who they are — there isn't one right way to do most things."],
            "do": "The teacher notices the student naming, without prompting, at least one thing that is part of their own home or family life that differs from a classmate's, and doing so without marking the difference as better or worse.",
        },
        "B": {
            "know": [
                "Identity has multiple dimensions — family background, home language(s), cultural traditions, beliefs, personal interests — and they do not have to match.",
                "A person can belong to more than one cultural group at the same time; dual or multiple belonging is normal.",
            ],
            "understand": ["Belonging to different groups at once isn't confusion — it is normal, and most people live this way."],
            "do": "The teacher notices the student describing more than one aspect of their own identity (including at least one cultural dimension) during class reflection, without prompt, on multiple occasions.",
        },
        "C": {
            "know": [
                "Stereotypes are oversimplified beliefs applied to all members of a group regardless of individual differences; they operate automatically and affect how people see others and themselves.",
                "A person's cultural background shapes expectations, communication style, and values in ways they are not fully conscious of — sometimes called a cultural lens.",
            ],
            "understand": ["My background shapes how I see and interpret things — and other people's backgrounds shape how they see and interpret things. Neither view is the whole picture."],
            "do": "The teacher notices the student pausing to consider how their own background might be influencing their reaction or interpretation before responding in a cross-cultural interaction — at least occasionally, without adult prompting.",
        },
        "D": {
            "know": [
                "Some of the groups a person belongs to were not chosen by them — the family they were born into, the nationality on their passport, the first language they grew up with, and in some cases how other people read their body or appearance — and those unchosen memberships still shape how others treat them and how they see the world.",
                "When a person belongs to a group, they typically feel more favourable toward their own group than toward other groups, often without deciding to — this can operate automatically, below conscious intention.",
            ],
            "understand": ["I belong to groups I did not choose, and those groups shape both how the world treats me and how I see the world — in ways that are often invisible until I actively look for them."],
            "do": "The teacher notices the student identifying, with genuine reflection rather than surface performance, how at least one unchosen group membership shapes their own experience or perspective in a specific situation.",
        },
        "E": {
            "know": [
                "The cultural lens concept: every interpretive framework is shaped by cultural context.",
                "Ethnocentrism: the tendency to evaluate other cultures by one's own standards, operating even when the evaluator believes they are being objective.",
                "Social identity theory: people derive part of their self-concept from group memberships and typically evaluate their in-group more favourably than out-groups, partly automatically.",
                "Intersectionality: a person's social position is shaped by multiple overlapping dimensions whose interaction produces experiences that single-dimension analysis misses.",
            ],
            "understand": ["My cultural lens is not neutral — it is one specific angle, not the view from nowhere. Recognising it does not make it disappear, but it changes what I can do with it."],
            "do": "The teacher notices the student voluntarily identifying how their cultural background might be limiting or distorting their interpretation of a text, event, or interaction — with specificity — in contexts where this is not explicitly required.",
        },
        "F": {
            "know": [
                "Personal identity vs. social identity — both dynamic negotiations rather than fixed states.",
                "Code-switching: adjusting language, behaviour, and expression across cultural contexts — both a competency and, when involuntary, a source of documented psychological cost.",
            ],
            "understand": ["Identity is not something I find — it is something I actively negotiate, and that negotiation never finishes. Who I am in one context and who I am in another are both genuinely me."],
            "do": "The teacher notices the student engaging with perspectives that challenge their own identity framework — including uncomfortable ones — without dismissing them or retreating to a fixed position, and without projecting their own resolution process onto peers navigating different questions.",
        },
    },
}

# ── LT 2.1 ──
KUD["lt_2_1"] = {
    "lt_name": "Focused Attention & Strategy",
    "competency": "C2 — Attention & Reflective Practices",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Apply attention strategies to sustain focus, identify what supports or disrupts attention, and evaluate strategies across contexts.",
    "prereq_lt_ids": ["lt_6_1"],
    "bands": {
        "A": {
            "know": ["Know content for this band lives in LT 6.1 Band A (body signals including tiredness and restlessness)."],
            "understand": ["My attention wanders, and I can bring it back."],
            "do": "I can complete a short sustained-attention task using my senses to stay on it, and describe one thing I did when my attention wandered.",
        },
        "B": {
            "know": ["Know content for this band lives in LT 6.1 Band B (how sleep and stress affect thinking)."],
            "understand": ["Attention is affected by what's going on around me and inside me, and some conditions help more than others."],
            "do": "I can use a practised attention strategy during a task and describe, in writing or conversation, what made it easier or harder to stay focused.",
        },
        "C": {
            "know": ["Know content for this band lives in LT 6.1 Band C (prefrontal cortex function; neuroplasticity)."],
            "understand": ["Strategies work through specific mechanisms, and knowing the mechanism helps me choose the right strategy for the situation."],
            "do": "I can evaluate how an attention strategy affected my focus during a specific task in a written reflection, and explain why the strategy did or didn't help, referencing the mechanism.",
        },
        "D": {
            "know": ["Know content for this band lives in LT 6.1 Band D (stress-emotion-attention-habit integration)."],
            "understand": ["The things that pull my attention away are often more informative about what I need than about the task itself."],
            "do": "I can sustain attention during a challenging task, identify in writing what pulled my attention away, and describe the deliberate strategy I used to return.",
        },
        "E": {
            "know": ["Know content for this band lives in LT 6.1 Band E (attention as a system-level resource)."],
            "understand": ["Attention management is an environment-design problem as much as a personal-discipline problem, and my physical and digital environment shapes what my attention can do."],
            "do": "I can design the conditions for sustained attention in a piece of my own work — including managing digital distractions — and produce a written evaluation of how different attentional strategies interacted with different types of tasks.",
        },
        "F": {
            "know": ["Know content for this band lives in LT 6.1 Band F (integrative attention science; cognitive load and expertise)."],
            "understand": ["Attention is a limited resource that must be strategically protected, not just reactively managed — and knowing how my best attention works is a professional and personal asset."],
            "do": "I can audit my attentional patterns across a sustained period of high-stakes work, produce a written analysis identifying the conditions and strategies that most reliably support my best work, and propose specific adjustments to my workflow.",
        },
    },
}

# ── LT 2.2 ──
KUD["lt_2_2"] = {
    "lt_name": "Reflective Decision-Making",
    "competency": "C2 — Attention & Reflective Practices",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Reflect on situations, weigh options and trade-offs, justify decisions referencing values and evidence, and remain open to revision.",
    "prereq_lt_ids": ["lt_1_1", "lt_6_2"],
    "bands": {
        "A": {
            "know": ["Know content for this band lives in LT 6.1 Band A."],
            "understand": ["I can learn from what I did."],
            "do": "I can retell a short experience orally or in a drawing-plus-sentence format, and state one thing I learned from it.",
        },
        "B": {
            "know": ["Know content for this band lives in LT 6.1 Band B."],
            "understand": ["Most choices have upsides and downsides, and thinking about both before deciding gives me a better chance of choosing well."],
            "do": "I can complete a simple before-after decision reflection: stating one helpful and one harmful possible outcome before making a choice, and writing one sentence afterwards about what happened.",
        },
        "C": {
            "know": ["Know content for this band lives in LT 6.1 Band C."],
            "understand": ["Good decisions consider more than one option and are grounded in what matters to me, not just what's easiest or most obvious."],
            "do": "I can complete a written three-option comparison for a decision I face, state my choice, and give a reason that references a named personal value.",
        },
        "D": {
            "know": ["Know content for this band lives in LT 6.1 Band D. LT 6.2 Band C provides evidence vocabulary."],
            "understand": ["Decisions rarely have a single right answer, and justifying a choice requires being honest about what I'm trading off and for whom."],
            "do": "I can write a structured decision analysis of a real or realistic scenario that names the trade-offs involved and considers how the decision affects at least two different stakeholders or affected parties.",
        },
        "E": {
            "know": ["Know content for this band lives in LT 6.1 Band E and LT 6.2 Band D."],
            "understand": ["The process that produces a decision matters as much as the decision itself — good reasoning under uncertainty is evaluable even before the outcome is known."],
            "do": "I can write a decision analysis that identifies at least one cognitive bias or assumption likely to be affecting my reasoning, describes an adjustment I made to my process to reduce its impact, and evaluates the quality of the reasoning independent of the outcome.",
        },
        "F": {
            "know": ["Know content for this band lives in LT 6.1 Band F and LT 6.2 Band F."],
            "understand": ["Mature decision-making is not certainty — it is the ability to act wisely under uncertainty while maintaining intellectual honesty about what I do not know and openness to changing my view."],
            "do": "I can construct a reasoned written position on a complex, contested, and high-stakes decision: weighing multiple types of evidence, acknowledging irreducible uncertainty, making the logic of my choice explicit, and naming what would cause me to revise.",
        },
    },
}

# ── LT 3.1 ──
KUD["lt_3_1"] = {
    "lt_name": "Health Literacy & Habits",
    "competency": "C3 — Physical Wellbeing & Self-Care",
    "knowledge_type": "T2",
    "compound": True,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Identify bodily needs, design and adjust health habits, and evaluate information quality and structural conditions shaping what is possible.",
    "prereq_lt_ids": ["lt_6_1", "lt_6_2"],
    "bands": {
        "A": {
            "know": [
                "The body needs sleep, food, water, movement, and hygiene routines to stay well.",
                "Hygiene routines include washing hands before eating and after toilet, brushing teeth twice a day, and bathing regularly.",
            ],
            "understand": ["My body needs specific things to feel well."],
            "do": "I can name my body's basic needs using a labelled diagram or sentence-frame reflection, and follow a simple personal hygiene routine with supportive reminders.",
        },
        "B": {
            "know": [
                "Sleep, food, and movement affect how a person feels the next day — not only physically but in mood, focus, and patience.",
                "A daily habit has more cumulative effect on how someone feels than a single big change. (Know layer integrates into LT 6.1 Band B from this band onward.)",
            ],
            "understand": ["How I feel day-to-day is shaped by what I do consistently, not just once."],
            "do": "I can explain in writing or speech how sleep, food, and movement affect how I feel, and set one specific healthy-habit goal using a template.",
        },
        "C": {
            "know": ["Know content for this band lives in LT 6.1 Band C (habit loop mechanism; neuroplasticity; cue-routine-reward cycle)."],
            "understand": ["Habits break down for specific reasons, and noticing the reason is the first step in adjusting the habit."],
            "do": "I can track one habit for a week (paper log or Strive), write a short analysis identifying one specific barrier to consistency, and explain why I want to keep or change it.",
        },
        "D": {
            "know": ["Know content for this band lives in LT 6.1 Band D (system-level neuroscience) and LT 6.2 Band C–D (evidence evaluation)."],
            "understand": ["Designing for my life means planning for the real conditions I live in, including the ones that disrupt me, rather than an idealised version of myself."],
            "do": "I can write a comparative analysis of two health information sources, create a balanced weekly habits plan that accounts for known obstacles, and document adjustments made based on logged results.",
        },
        "E": {
            "know": [
                "Social determinants of health — income, neighbourhood, food access, cultural norms, parental work patterns — shape what healthy habits are realistically available.",
                "Evidence-quality criteria: strength of study design, sample size, replication, and whether claims are about populations or individuals.",
            ],
            "understand": ["Health habits sit inside a social and structural context that shapes what is possible for me — and honest health literacy means understanding both what I can change personally and what requires conditions I do not control alone."],
            "do": "I can write an analysis identifying the structural and social factors affecting my access to healthy habits, evaluate health claims in two sources using evidence-quality criteria, and produce a redesigned habits plan that accounts for conditions I cannot individually control.",
        },
        "F": {
            "know": [
                "Sustainable behaviour change operates at the systems level — environmental design, social norms, policy, availability of resources — as much as the individual level.",
                "Critical health literacy distinguishes personal-agency factors from structural-enablement factors in health outcomes.",
            ],
            "understand": ["Long-term health is not a product of willpower alone — it is enabled or disabled by the environments, relationships, and systems surrounding individuals, and understanding this is what makes health literacy genuinely critical."],
            "do": "I can produce a designed health maintenance approach sustainable across the demands of adult life, accounting for competing priorities, social pressures, and systems-level constraints, and articulate in writing why sustainable habits require external conditions, not only personal willpower.",
        },
    },
}

# ── LT 3.2 ──
KUD["lt_3_2"] = {
    "lt_name": "Self-Care & Resilience",
    "competency": "C3 — Physical Wellbeing & Self-Care",
    "knowledge_type": "T3",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Notice early warning signs, apply self-care responses, maintain them under pressure, and build a personal resilience framework over time.",
    "prereq_lt_ids": ["lt_3_1", "lt_6_1", "lt_1_2"],
    "bands": {
        "A": {
            "know": [
                "A trusted adult is someone whose job or role is to help keep a child safe (parent, teacher, school counsellor, named family adult).",
                "A self-care routine includes handwashing before eating and after toilet, brushing teeth twice daily, drinking water, and resting when tired.",
            ],
            "understand": ["Asking for help is a normal part of taking care of myself, not something that happens only when something is wrong."],
            "do": "The teacher notices the student naming a specific trusted adult they could go to for help, and carrying out a simple self-care routine with supportive reminders, on most occasions when it is needed.",
        },
        "B": {
            "know": [
                "Early warning signs the body gives before someone is fully overwhelmed include tiredness, headache, irritability, tight chest or tummy, and losing interest in things that normally feel enjoyable.",
                "A short break, water, fresh air, movement, or naming a feeling are self-care responses that can reduce activation before it escalates.",
            ],
            "understand": ["My body signals before my mind catches up, and responding early is more effective than responding late."],
            "do": "The teacher notices the student naming a bodily early-warning sign in themselves — fatigue, irritability, a specific tension pattern — and selecting a practised self-care response before activation escalates, across multiple occasions.",
        },
        "C": {
            "know": [
                "Trusted people and services available to students at this school include the school counsellor, the school nurse, named teachers, parents or family adults, and external services appropriate to the jurisdiction.",
                "Different contexts (home, school, online) often require different self-care strategies because of what is available and what causes stress in each.",
            ],
            "understand": ["Self-care has to work in the actual conditions of my life, and knowing who to turn to is as important as knowing what to do for myself."],
            "do": "The teacher notices the student articulating — spontaneously or on brief prompt — a self-care plan with context-specific strategies for both home and school, and naming two or more trusted people or services they could turn to for support, across multiple occasions.",
        },
        "D": {
            "know": ["Know content for this band lives in LT 6.1 Band D (HPA axis, stress-system integration) and LT 1.2 Band D (relational repair and offering perspective-aware support)."],
            "understand": ["Self-care practices are most valuable precisely when they are hardest to do, and helping others maintain theirs strengthens rather than depletes my own."],
            "do": "The teacher notices the student sustaining their key self-care routines through genuinely stressful periods (assessment window, social friction, demanding project) without adult scaffolding, AND, on at least one observed occasion, offering a peer a specific non-directive form of support.",
        },
        "E": {
            "know": ["Know content for this band lives in LT 6.1 Band E (allostatic load and chronic stress mechanisms) and LT 3.1 Band E (structural and social determinants of what self-care is realistically available)."],
            "understand": ["Sustainable resilience is grounded in a realistic view of my own limits — knowing when to extend myself and when to rest is as important as the ability to persevere."],
            "do": "The teacher notices the student sustaining self-care through extended pressure periods without prompting, seeking help when their own strategies are insufficient (neither too early nor too late), and participating in peer-group self-care norms in a way that registers as authentic rather than performative, across more than one context.",
        },
        "F": {
            "know": ["Know content for this band lives in LT 6.1 Band F (integrative stress neuroscience and allostatic load over life course) and LT 7.2 Band F (metacognitive self-direction as personal framework)."],
            "understand": ["Resilience is not a trait I either have or lack — it is a system I have built, which I can describe, maintain, and continue to develop in adult life."],
            "do": "The teacher or mentor notices the student articulating — in a Reflection 360 conversation or spontaneous reflection — their personal resilience framework: non-negotiable self-care commitments, early-warning signals, recovery protocols, and how this framework has developed across their years at school, unprompted and with specificity.",
        },
    },
}

# ── LT 4.1 ──
KUD["lt_4_1"] = {
    "lt_name": "Bodies, Boundaries & Consent",
    "competency": "C4 — Consent, Safety & Healthy Relationships",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Recognise and respect bodily autonomy, apply consent principles across everyday, sexual, and online contexts, and analyse power dynamics.",
    "prereq_lt_ids": ["lt_1_2", "lt_5_1", "lt_6_1"],
    "bands": {
        "A": {
            "know": [
                "Anatomically correct names for private body parts (penis, vulva, vagina, bottom, chest), taught matter-of-factly using the same register as other body parts.",
                "A trusted adult in this school is a named specific person — a class teacher, the school counsellor, the school nurse, or a designated family adult.",
            ],
            "understand": ["My body is mine, and there are specific people whose job is to help keep it safe."],
            "do": "I can name private body parts using correct terminology in a short scenario-response task, identify at least two trusted adults in my specific context (home and school), and state one situation in which I would tell a trusted adult.",
        },
        "B": {
            "know": [
                "Consent means clear, freely-given agreement to what is happening — a 'yes' that is not a result of pressure, confusion, or fear of what will happen if the answer is 'no'.",
                "Pressure sounds like repeated asking after a 'no', reminders of what will be lost if the answer stays 'no', making the person feel unkind or childish, or invoking friendship or loyalty to shift the answer.",
            ],
            "understand": ["Everyone has a right to say yes or no, and healthy relationships honour that right every time, not only when the person asking feels like it."],
            "do": "I can complete a written scenario analysis identifying whether consent was freely given, unclear, or overridden by pressure, and describe what a clear request, a clear answer, and a help-seeking response sound like.",
        },
        "C": {
            "know": [
                "Consent applies beyond sexual contexts — borrowing belongings, physical touch, taking or sharing photos, and forwarding messages all require agreement.",
                "Online consent is specific: permission to send a photo is not permission to share it; agreement in a private message is not agreement to screenshot and redistribute.",
                "Clear boundary-statement language to peers includes naming the behaviour, naming the limit, and naming the ask — 'When you X, I need you to Y.'",
            ],
            "understand": ["Consent is the same principle across every kind of interaction, not a special rule for one area — which means it shows up in everyday choices, not only in big moments."],
            "do": "I can complete a scenario-response task that applies consent reasoning to non-sexual, physical, and online scenarios, and state a specific clear boundary to a peer in a structured roleplay.",
        },
        "D": {
            "know": [
                "Power imbalance occurs when one person has more age, status, role authority, peer-group standing, or control over outcomes than the other — and those imbalances affect how freely a 'yes' or 'no' can be given.",
                "An exit plan is a pre-rehearsed line and action for leaving a situation (a specific phrase to say, a specific place to go, a specific person to contact) — prepared before pressure hits, not during.",
                "Confidential help routes include the school counsellor, a trusted teacher, and — depending on jurisdiction and age — a GP or youth health service.",
            ],
            "understand": ["Power and pressure affect what feels possible to say, not just what is technically allowed — and recognising the dynamic is part of being able to refuse, exit, or help someone else do either."],
            "do": "I can complete a written analysis of a pressure scenario that names the specific power or peer-pressure dynamics at play, states a refusal and a prepared exit plan in direct language, and describes how I would support a peer to access confidential help.",
        },
        "E": {
            "know": [
                "Legal consent thresholds (jurisdiction-appropriate): age of consent in Hungary is 14 (with specific conditions); grooming is recognised in Hungarian criminal law; image-based abuse laws apply to non-consensual sharing.",
                "Grooming patterns include targeted isolation, escalating secrecy, flattery followed by implicit exchange, and gradual normalisation of contact outside appropriate boundaries.",
                "Institutional power contexts — teacher/student, coach/athlete, employer/employee, older-peer/younger-peer — carry structural consent-constraints recognised in safeguarding policy and law.",
                "Rights and reporting pathways in this jurisdiction include specific confidential services, the role of Mandatory Reporters, and what happens when a disclosure is made.",
            ],
            "understand": ["Consent exists in legal, ethical, and relational dimensions that do not always align — understanding where they diverge, and whose interests are protected in each, is part of sophisticated consent literacy."],
            "do": "I can complete a written analysis of a coercion, grooming, or exploitation scenario (online or institutional) that applies the relevant legal framework, evaluates the institutional context, and drafts a non-directive, trauma-aware response to a friend disclosing a similar situation.",
        },
        "F": {
            "know": [
                "Myths commonly requiring correction in consent education include: 'silence means yes'; 'if they didn't say no, it was consent'; 'once given, always given'; 'clothing or drinking signals consent'; 'asking for consent kills the mood.'",
                "Principles of facilitation with younger peers: maintain age-appropriate language, use open questions rather than leading ones, avoid explicit personal disclosure, name feelings of discomfort as legitimate, and refer rather than counsel when someone discloses.",
                "Rights-based framing holds consent as a positive right grounded in bodily autonomy, not only a prohibition against harm.",
            ],
            "understand": ["Consent education is not a one-time lesson but an ongoing cultural practice — and people who understand it well are positioned to model, teach, and protect it in the communities they belong to."],
            "do": "I can facilitate a rubric-assessed 20-minute structured discussion about consent, power, and boundaries with peers or younger students that applies age-appropriate language, surfaces and corrects at least two common myths using evidence, and closes with a rights-based framing.",
        },
    },
}

# ── LT 4.2 ──
KUD["lt_4_2"] = {
    "lt_name": "Puberty, Health & Safe Choices",
    "competency": "C4 — Consent, Safety & Healthy Relationships",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "B", "end": "F"},
    "summary": "Understand puberty changes, assess reproductive and substance-use health risks, and access trustworthy support and information as an independent agent.",
    "prereq_lt_ids": ["lt_6_2", "lt_6_1", "lt_4_1"],
    "bands": {
        "B": {
            "know": [
                "Physical changes of puberty include growth spurt, body-hair growth, increased oil production and acne, body-odour onset, breast development and menstruation (for those with ovaries), and genital growth, voice change, and first ejaculation (for those with testes).",
                "Emotional changes include mood fluctuations linked to hormone changes, increased desire for privacy, and changing relationship dynamics with parents and peers.",
                "Puberty hygiene includes daily washing, using deodorant, washing hair regularly, changing clothes after sweating, and using appropriate menstrual products.",
                "A reliable puberty-information source is one authored by qualified health professionals and non-commercial.",
            ],
            "understand": ["My body will change in predictable ways during puberty, and knowing what to expect makes the changes less confusing and easier to respond to."],
            "do": "I can complete a written or oral explanation identifying at least five physical and two emotional changes of puberty, describe an appropriate personal hygiene routine, and name two reliable health information sources for puberty questions.",
        },
        "C": {
            "know": [
                "Reproductive anatomy: ovaries produce eggs (typically one released per menstrual cycle); testes produce sperm; the uterus is where a fertilised egg can implant and develop.",
                "Human reproduction at age-appropriate level: when a sperm fertilises an egg, the resulting cell (zygote) divides and develops in the uterus over approximately nine months.",
                "Criteria distinguishing a trusted health source from an unreliable one: named qualified author, transparent evidence base, non-commercial, currency, and consistency with major health-body guidance.",
                "Puberty-specific hygiene routines by body type (menstrual-product options and use; care of newly active sweat glands; skin care for acne).",
            ],
            "understand": ["My body is changing in ways I can understand scientifically, and scientific understanding is more useful than rumour or fear for making sense of what is happening."],
            "do": "I can complete a written explanation of human reproduction at an age-appropriate level, describe the hygiene routines relevant to my own pubertal development, and apply stated criteria to distinguish a trusted health source from an unreliable one in a short source-comparison task.",
        },
        "D": {
            "know": [
                "STIs transmit through unprotected sexual contact; common STIs include chlamydia, gonorrhoea, HPV, HSV, and HIV; many are asymptomatic; testing is the primary identification route.",
                "Pregnancy risk: pregnancy can result from any unprotected penile-vaginal sex including first occurrence; probability varies but is never zero.",
                "Protection methods: condoms (barrier, protect against both STI and pregnancy); hormonal contraception — pill, IUD, implant, injection — (protect against pregnancy only); emergency contraception available up to 72–120 hours depending on method.",
                "Substance-use risks: alcohol and nicotine are dose-dependent harms with adolescent-brain-specific vulnerabilities; cannabis use in adolescence is associated with mental-health risks in genetically susceptible individuals; polysubstance use multiplies risks non-linearly.",
                "Confidential health access in Hungary: general practice, youth health clinics, specific NGOs — age thresholds and confidentiality rules must be verified in unit plan.",
            ],
            "understand": ["Decisions about bodies and relationships involve real risks that can be understood and reduced, and knowing how to access confidential help is part of being able to make informed choices."],
            "do": "I can complete a written scenario-based risk-assessment task covering STI, pregnancy, and substance-use scenarios, identify the relevant protection methods for each, and describe specific steps for accessing confidential health advice in this jurisdiction.",
        },
        "E": {
            "know": [
                "Healthcare navigation: how to register with a GP, how to book a confidential appointment as a young person, what youth-specific health services exist in this jurisdiction.",
                "Young person's rights: specific to Hungary — age of consent to medical treatment, confidentiality thresholds, parental-notification exceptions. Must be verified in unit plan.",
                "Evidence-based SRH guidelines: WHO adolescent health guidance, NICE (UK) or equivalent national clinical guidelines, and BMJ Best Practice as named reference sources.",
                "How to evaluate SRH information against a named guideline (cross-check specific claims, check dates, identify commercial or advocacy conflict of interest).",
            ],
            "understand": ["My reproductive and sexual health is my own responsibility and right — accessing accurate information and appropriate support is not something I should need to depend on someone else to arrange for me."],
            "do": "I can complete a written analysis of a reproductive or sexual-health question that identifies the relevant healthcare service, states the access pathway and confidentiality conditions in this jurisdiction, and evaluates at least two information sources against stated evidence-based guideline criteria.",
        },
        "F": {
            "know": [
                "Examples of currently contested SRH claims: the efficacy of abstinence-only education; health effects of pornography consumption; hormonal contraception risk communication; youth vaping claims; the cannabis–mental-health debate.",
                "Commercial and institutional interests in SRH: period-products industry; pharmaceutical pricing and marketing of contraception; tobacco/vape industry; wellness-influencer economy.",
                "Ideological framings in SRH discourse: abstinence-until-marriage vs. comprehensive education; pro-life vs. pro-choice framings; debates in gender-related clinical practice.",
                "Principles of critical appraisal in SRH: quality of study design (RCT, observational, qualitative); effect size and confidence intervals; replication status; declared conflicts of interest; whether guidance reflects single studies or systematic reviews.",
            ],
            "understand": ["Sexual and reproductive health is a contested terrain where evidence, culture, politics, and personal values intersect — mature health literacy means being able to navigate this complexity without either uncritical acceptance or cynical dismissal of evidence."],
            "do": "I can construct a written critical evaluation of a contested SRH claim that weighs the quality of evidence on each side, identifies the ideological, cultural, or commercial interests shaping the discourse, acknowledges what remains uncertain, and articulates my reasoned personal position.",
        },
    },
}

# ── LT 4.3 ──
KUD["lt_4_3"] = {
    "lt_name": "Active Bystander & Anti-Discrimination",
    "competency": "C4 — Consent, Safety & Healthy Relationships",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Identify discrimination and targeted harm, assess safe bystander responses, and justify reasoning about when and how to act or seek help.",
    "prereq_lt_ids": ["lt_1_2", "lt_6_1", "lt_4_1"],
    "bands": {
        "A": {
            "know": [
                "Who counts as a trusted adult in this school context (teacher, counsellor, playground supervisor, family adult).",
                "Language for describing what happened: 'They were left out.' / 'Someone was unkind to them.' / 'They weren't allowed to play.'",
            ],
            "understand": ["When someone is hurt or left out, it matters to tell a grown-up — I don't have to fix it myself."],
            "do": "I can complete a short scenario-response (oral or drawing-plus-sentence) that describes a situation where someone was left out or treated unkindly, names what I saw, and identifies a specific trusted adult I could tell.",
        },
        "B": {
            "know": [
                "Common forms of exclusion or unfair treatment at this age: deliberate leaving-out, mean teasing, name-calling, spreading gossip, physical pushing.",
                "Helpful actions available to a Band B student include: saying something kind to the person who was targeted, inviting them to join, telling an adult, and making sure a friend tells an adult if they can't.",
                "The person affected is the one who decides whether something was unkind — not the person who did it.",
            ],
            "understand": ["Unkindness isn't always the same as an accident — what's 'just a joke' to one person can really hurt another, and the person affected is the one who knows which it was."],
            "do": "I can complete a written or oral scenario-response task that describes what happened when someone was excluded or treated unfairly, suggests how the person might have felt, and selects one helpful action from a short list of options with one-sentence reasoning for my choice.",
        },
        "C": {
            "know": [
                "Forms of exclusion and discrimination include teasing based on a personal or group characteristic (body, family background, nationality, ability), excluding from games or activities, spreading gossip, and mocking language or imitation.",
                "The four bystander response options: direct (intervene safely), distract (interrupt the situation without directly confronting), delegate (get help from an adult or someone who can act), delay (check in with the targeted person after the fact).",
                "A safety check before direct intervention: is the person doing harm likely to escalate; am I physically safe; is there an adult nearby; are the group dynamics stacked against me.",
            ],
            "understand": ["There are several ways to help in a hard situation, and the best one depends on whether I can stay safe, not on whether I feel brave."],
            "do": "I can complete a written scenario-response task that identifies the form of exclusion or discrimination present, assesses whether it is safe to intervene directly, and names and justifies my choice from the four bystander options.",
        },
        "D": {
            "know": [
                "Forms of discrimination include racism, sexism, homophobia/transphobia, ableism, and religious or cultural discrimination — at age-appropriate introduction. Know content for stress-response and freeze lives in LT 6.1 Band D. Know content for power dynamics lives in LT 4.1 Band D.",
                "Group dynamics factors in bystander situations: group size (larger groups show less intervention — diffusion of responsibility), status of the person causing harm within the group, and in-group vs. out-group composition.",
                "What the targeted person may need: to be believed, to feel safe, to not be made more visible against their will, to have their version of events validated, to have the incident named and addressed without being spoken for.",
            ],
            "understand": ["Discrimination isn't just one person being mean — it's behaviour shaped by group norms and power differences, and naming the dynamic is part of responding well."],
            "do": "I can complete a written analytical task on a bystander scenario that identifies the forms of discrimination present, names the specific group and power dynamics at play, and justifies a proposed response based on safety, proportionality, and what the targeted person is likely to need.",
        },
        "E": {
            "know": [
                "Know content for stress-response and freeze lives in LT 6.1 Band E.",
                "Bystander effect research: larger bystander pools reduce individual probability of intervention (Darley & Latané 1968); interventions require someone to notice, interpret as needing help, feel responsible, know what to do, and implement.",
                "Group-norm factors in intervention: perceived group norms often diverge from actual group views (pluralistic ignorance); establishing that intervention is normal within a group increases its probability.",
                "Institutional context factors: whether reporting pathways are trusted; whether leadership models intervention; whether history of past incidents has been addressed; power imbalances between targeted and non-targeted groups within the institution.",
            ],
            "understand": ["My instinct to freeze or go along in a discrimination situation isn't cowardice but a predictable response to group pressure and stress — and knowing that is how I can plan around it rather than blame myself for it."],
            "do": "I can complete a written evaluation that compares two or more possible responses to a discrimination scenario, identifies my own likely default response and its probable sources, and explains how specific group norms and institutional context factors shape which interventions are possible or effective.",
        },
        "F": {
            "know": [
                "Know content for systems-level analysis lives in LT 6.1 Band F and LT 8.2 Band E–F.",
                "Conditions associated with higher bystander intervention rates: trusted reporting pathways, explicit group norms supporting intervention, repeated situated practice, modelled intervention by leadership, and perceived support from peers.",
                "Principles of ethical intervention design: the targeted person is the centre, not the intervener; visibility is sometimes harmful; evidence-based intervention differs from performative gesture.",
            ],
            "understand": ["Whether bystanders act isn't mainly about individual courage — it's about the conditions a group or institution creates, and changing those conditions is more powerful than asking individuals to be braver."],
            "do": "I can construct a written or presented analysis of a real bystander success or failure (self-selected, my own or another's), evaluate what made effective intervention possible or impossible in that specific context, and propose specific group, school, or community-level conditions that would make active bystander response more likely, with reasoning grounded in bystander research.",
        },
    },
}

# ── LT 5.1 ──
KUD["lt_5_1"] = {
    "lt_name": "Interpersonal Skills & Communication",
    "competency": "C5 — Community, Purpose & Belonging",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Communicate clearly across contexts — including disagreement — by listening actively, calibrating language to the situation, and facilitating when needed.",
    "prereq_lt_ids": ["lt_1_2", "lt_1_1"],
    "bands": {
        "A": {
            "know": [
                "I-statement structure: 'I feel [feeling] when [what happened].'",
                "Kind words versus hurtful words — named examples appropriate to context.",
                "Turn-taking cues: waiting for a pause; looking at the person speaking; not talking over.",
            ],
            "understand": ["How I talk to someone doesn't just describe what I feel — it shapes what happens next in the conversation."],
            "do": "I can complete a short observed roleplay in which I take turns in conversation, use kind language, and apply an I-statement when something bothered me — followed by a brief verbal reflection on my word choice.",
        },
        "B": {
            "know": [
                "Needs-expression stems: 'I need…' / 'I'd like…' / 'It would help me if…'",
                "Boundary-asking stems: 'Is it okay if…?' / 'Would you be willing to…?' / 'Can we try…?'",
                "Proposing fair options: stating two alternatives that are workable for both people — 'What if we did X or Y?'",
            ],
            "understand": ["Being clear about what I need, and curious about what others need, makes working things out easier than trying to guess or push."],
            "do": "I can complete a structured roleplay or scenario-response that uses an I-statement to state a specific need, asks about the other person's boundaries using a named stem, and proposes two options for a fair solution with one-sentence reasoning.",
        },
        "C": {
            "know": [
                "The repair routine — four named steps: (i) what happened, from both perspectives; (ii) what I contributed; (iii) what I need now; (iv) what I commit to trying next time.",
                "Respectful word choice under disagreement: name behaviour not character — 'When you said X, I felt Y' rather than 'You're always Z.'",
                "Active listening markers: not interrupting; letting the person finish; reflecting what you heard before responding.",
            ],
            "understand": ["Staying in a conversation when I disagree is a different skill than avoiding it — and it's one I have to practise, not one I'm supposed to have automatically."],
            "do": "I can complete a rubric-assessed roleplay of a disagreement in which I listen without interrupting, respond using language that names behaviour not character, and apply the four-step repair routine when the moment calls for it.",
        },
        "D": {
            "know": [
                "Paraphrasing technique — check-understanding stems: 'Let me check I've understood — you're saying…' / 'So what matters to you most here is…' / 'If I heard you right, X is important because Y.'",
                "Situation-calibrated word choice: register (formal/informal), directness (direct/indirect), and framing (personal/structural) all change with audience and stakes.",
                "Clear boundary-stating language for high-stakes contexts: name the behaviour, name the limit, name the ask. Know content for self-regulation under conflict lives in LT 1.1 Band D.",
            ],
            "understand": ["Communication quality matters most when stakes are high — the same skills that work in calm conversations need to be deliberately applied in difficult ones, not assumed."],
            "do": "I can complete a rubric-assessed conflict roleplay or scenario-based analysis in which I state a clear boundary, paraphrase the other person's position before responding, and demonstrably calibrate my word choice to a specific described context.",
        },
        "E": {
            "know": [
                "Facilitation techniques: open questions (start with 'what' / 'how' / 'when'); process-observation statements ('I notice we've heard from three people but not from four'); airtime-management moves (inviting quieter voices without calling them out); summarising without taking a side.",
                "The facilitator role: hold the process, not the content — the facilitator's job is not to win or resolve but to ensure a legitimate conversation happens. Know content on stress and group dynamics lives in LT 6.1 Band E and LT 1.2 Band E.",
            ],
            "understand": ["Facilitating a group conversation under disagreement requires a different role than participating — the facilitator holds the process, not the positions."],
            "do": "I can facilitate a rubric-assessed 15-minute structured group conversation in which participants disagree on a substantive question, managing the process rather than the positions, ensuring all voices are heard, and maintaining a constructive tone across the session.",
        },
        "F": {
            "know": [
                "Cross-cultural communication variables: high-context vs. low-context cultures (indirectness vs. directness); hierarchy norms; formality conventions; relationship-first vs. task-first conversation structures.",
                "Power-dynamics factors affecting who-gets-heard: status (age, role, perceived expertise); numerical majority vs. minority in the conversation; who set the agenda; whose language is being used. Know content for power dynamics cross-references LT 4.1 Band D–E.",
                "Adjusting register without losing perspective: matching tone and formality while retaining content.",
            ],
            "understand": ["Communicating across significant difference isn't about giving up my own perspective — it's about recognising the conditions that make genuine dialogue possible and creating them deliberately."],
            "do": "I can complete a rubric-assessed communication task across significant difference (cultural, generational, or positional) in which I adjust my register and tone to the context without losing my own perspective, and demonstrate in written reflection my awareness of the power dynamics shaping who gets heard.",
        },
    },
}

# ── LT 5.2 ──
KUD["lt_5_2"] = {
    "lt_name": "Community Engagement & Purpose",
    "competency": "C5 — Community, Purpose & Belonging",
    "knowledge_type": "T3",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Contribute meaningfully to communities, act with others on real needs, reflect on impact, and develop a personal sense of purpose over time.",
    "prereq_lt_ids": ["lt_1_2", "lt_5_1", "lt_7_2"],
    "bands": {
        "A": {
            "know": ["Names of specific classroom jobs available; what each job does to help the class run."],
            "understand": ["I'm part of a group, and what I do makes a difference to it."],
            "do": "The teacher notices the student carrying out their classroom job on most occasions without needing reminders, and articulating — when asked or spontaneously — how that job helps the class function.",
        },
        "B": {
            "know": ["Signs someone might be left out (sitting alone, not being chosen, quieter than usual, declining invitations)."],
            "understand": ["Belonging is something groups create on purpose, not something that just happens — and I can help create it."],
            "do": "The teacher notices the student spontaneously including a peer who appears left out, on multiple occasions across varied group contexts (classroom, playground, collaborative work).",
        },
        "C": {
            "know": ["The structure of D2R project design — identify the need, propose, plan, do, reflect. Know content for team collaboration lives in LT 5.1 Band C."],
            "understand": ["Making something happen in a community is a practice — noticing what's missing, proposing a response, and following through with others — not a moment of inspiration."],
            "do": "The teacher notices the student, across at least one D2R project cycle, identifying a real school need unprompted, contributing to a team proposal, and following through on their share of the work to completion.",
        },
        "D": {
            "know": ["What makes a group 'diverse' in the REAL context (nationality, language, ability, identity, prior experience); what 'impact' means as distinct from 'completion'. Know content for working across difference lives in LT 1.2 Band D and LT 5.1 Band D."],
            "understand": ["What I contribute to community is part of who I'm becoming, and working across difference strengthens what's possible, not just what I know."],
            "do": "The teacher notices the student, through their Light Dragon capstone or extended D2R work, collaborating substantively with team members different from themselves (background, perspective, skill), engaging with evidence of whether their project made a difference, and articulating why the work matters to them personally — in Reflection 360 or unprompted conversation.",
        },
        "E": {
            "know": ["Know content for this band lives in LT 6.1 Band E (stress under sustained effort) and LT 5.1 Band E (facilitation under disagreement). The distinction between community action (changeable by participants) and structural conditions (requiring institutional change)."],
            "understand": ["Sustained community engagement requires understanding the systems that shape what is possible — and knowing those limits isn't defeatism but honest civic literacy."],
            "do": "The teacher or mentor notices the student leading a sustained initiative (beyond a single project cycle) addressing a genuine need, navigating specific institutional and relational obstacles as they arise, and articulating — in Reflection 360 or unprompted — both the impact of what was achieved and the limits that institutional context imposed.",
        },
        "F": {
            "know": ["Know content for this band lives in LT 7.2 Band F (metacognitive self-direction as personal framework). The distinction between purpose-as-role (what I do) and purpose-as-orientation (what I stand for); stability and revision in purpose over time."],
            "understand": ["Purpose is not discovered once — it is developed through accumulated engagement and reflection, and leaving school with a clear sense of it is one of the most significant outcomes of a wellbeing education."],
            "do": "The teacher or mentor notices — across Reflection 360 and the preceding two years of engagement — that the student's post-school choices (path, community involvement, roles) trace specifically to prior sustained engagement, and that when asked about purpose the student points to that engagement with specificity rather than to abstracted articulation.",
        },
    },
}

# ── LT 6.1 ──
KUD["lt_6_1"] = {
    "lt_name": "Brain, Body & Wellbeing Science",
    "competency": "C6 — Wellbeing Science & Literacy",
    "knowledge_type": "T1",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Explain stress, emotion, attention, and habit mechanisms using accurate vocabulary, and evaluate claims about brain and wellbeing interventions.",
    "prereq_lt_ids": [],
    "bands": {
        "A": {
            "know": [
                "Body signals include heart beating fast, tight tummy or chest, feeling hot or shaky, tiredness, hunger, thirst — each tells me something specific.",
                "Sleep helps the body rest and grow, and during deep sleep the brain sorts and stores what we have learned.",
                "Food gives the body and brain the fuel they need to work; regular meals help mood and focus stay steady.",
            ],
            "understand": ["My body gives me information about how I feel before I think about it."],
            "do": "I can complete a rubric-assessed oral or written explanation task that names at least three body signals and what each typically indicates, and describes in my own words what sleep and food do for the body and brain.",
        },
        "B": {
            "know": [
                "The fight-flight-freeze response: when the brain detects a threat, the heart beats faster, breathing quickens, muscles tense, and the body prepares to defend, escape, or stay still.",
                "The amygdala is a brain region that detects threat and triggers this response.",
                "Habits run on a three-part loop: cue (what triggers the habit), routine (what I do), reward (what my brain gets out of it).",
            ],
            "understand": ["My body's stress response happens automatically to protect me, and my habits run as a repeated loop — neither is a choice in the moment."],
            "do": "I can complete a rubric-assessed written or oral explanation that describes what happens in the body during a fight, flight, or freeze response, and explains the three parts of the habit loop using my own example.",
        },
        "C": {
            "know": [
                "The amygdala is a threat-detection region; when it fires strongly, it reduces activity in the prefrontal cortex, making clear thinking harder during stress.",
                "The prefrontal cortex handles planning, self-control, weighing options, and overriding automatic responses; it matures later than limbic regions.",
                "Neuroplasticity: the brain physically rewires based on repetition — 'neurons that fire together, wire together' (Hebb's rule).",
                "Habit-loop mechanism: repeated cue-routine-reward cycles strengthen specific neural pathways, moving behaviour from conscious control (prefrontal) toward automatic execution (basal ganglia).",
            ],
            "understand": ["Specific brain structures have specific functions, and my brain changes in response to what I repeatedly practise or experience."],
            "do": "I can complete a rubric-assessed written explanation that describes how the amygdala and prefrontal cortex interact during a stressful moment, explains neuroplasticity in my own words with a concrete example, and describes how the habit loop explains behaviour change at mechanism level.",
        },
        "D": {
            "know": [
                "Core neuroscience vocabulary: amygdala, prefrontal cortex, hippocampus, basal ganglia, hypothalamus, pituitary, adrenal glands, cortisol, dopamine, autonomic nervous system (sympathetic and parasympathetic branches).",
                "The HPA axis: when threat is detected, the hypothalamus signals the pituitary, which signals the adrenal glands to release cortisol — mobilising energy and downregulating non-essential functions.",
                "System interactions: sustained stress narrows attention; narrowed attention shapes which habits are triggered; habits in turn shape mood and stress-response baseline — these don't operate independently.",
                "Dopamine anticipates reward (not only confirms it), which is why cravings feel urgent before the reward arrives.",
            ],
            "understand": ["Stress, emotion, attention, and habit are not separate domains I can work on one at a time — they operate as an interdependent system where a change in one affects the others."],
            "do": "I can complete a rubric-assessed written explanation that uses accurate neuroscience vocabulary to describe how stress, emotion, attention, and habit interact as a system, and explains the role of the HPA axis in the stress response.",
        },
        "E": {
            "know": [
                "Allostatic load: cumulative wear on the body from repeated or chronic stress-system activation; long-term effects include immune suppression, cardiovascular risk, and mental-health effects.",
                "Acute stress response (time-limited, adaptive) differs from chronic stress response (prolonged, maladaptive) — same mechanism, different downstream effects.",
                "Adolescent-brain specifics: prefrontal cortex matures later than limbic structures, producing relative imbalance where reward-seeking and emotional activation outpace regulation capacity; adolescent neuroplasticity is heightened, making experience more formative.",
                "Criteria for evaluating a neuroscience claim: peer-reviewed? Controlled or observational study? Mechanism plausibly connected to claimed effect? Replicated?",
            ],
            "understand": ["Understanding a mechanism is useful only if I can apply it — applying neuroscience means evaluating claims made in its name, not just restating the system."],
            "do": "I can complete a rubric-assessed written evaluation of a specific wellbeing intervention (mindfulness, exercise, breathwork, sleep-hygiene, or similar), explaining its proposed mechanism, summarising what the evidence suggests about its effectiveness, and articulating what it would and would not change in the stress-emotion-attention-habit system.",
        },
        "F": {
            "know": [
                "Affective neuroscience is a developing field with unresolved debates (e.g. discrete-emotion vs. constructionist theory; cross-cultural generalisability of emotion categories).",
                "Named cases of popular misrepresentation of wellbeing research: the amygdala as 'the emotion centre' (oversimplification); learning styles (not supported by evidence); growth-mindset interventions showing smaller meta-analytic effect sizes than single-study reports.",
                "Contested areas in adolescent mental-health research: social-media effects on mental health; screen-time debates; the MYRIAD trial results on school-based mindfulness showing smaller effects than expected.",
                "Principles of critical neuroscience literacy: distinguish mechanism from correlation; distinguish brain-based evidence from behavioural evidence; notice when 'brain' is being used to add authority rather than substance.",
            ],
            "understand": ["Neuroscience is a developing field with unresolved debates, and the gap between research findings and popular application is often large — mature wellbeing literacy includes knowing where the science is solid, contested, or simply unknown."],
            "do": "I can construct a rubric-assessed critical essay on a contested claim in wellbeing science that identifies where the evidence is strong, where it is uncertain, where popular accounts have oversimplified or misrepresented research, and states my reasoned position with specific evidence.",
        },
    },
}

# ── LT 6.2 ──
KUD["lt_6_2"] = {
    "lt_name": "Health Information Literacy",
    "competency": "C6 — Wellbeing Science & Literacy",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Evaluate health information for trustworthiness, evidence quality, and bias using progressively more sophisticated analytical criteria across bands.",
    "prereq_lt_ids": ["lt_6_1"],
    "bands": {
        "A": {
            "know": [
                "A trusted adult for health questions is a specific named person — a parent, a named teacher, the school nurse, or a doctor — whose role includes helping children with questions about their body and wellbeing.",
                "When a child hears or sees a health claim they are unsure about (from an advert, a video, a friend, or a stranger), the correct first response is to check with a trusted adult before believing or acting on it.",
            ],
            "understand": ["Some people know more about health than others, and asking a specific person whose job is to know is a skill I can use on purpose, not just something I do when I'm worried."],
            "do": "I can complete a short rubric-assessed oral or written task in which I am presented with a simple health claim, and I identify whether it came from a trusted source, who I would ask, and why.",
        },
        "B": {
            "know": [
                "A reliable health source names its author, and the author has relevant qualifications — doctor, registered nurse, registered dietitian, recognised health organisation.",
                "A reliable source is transparent about where its information comes from (names the research, studies, or guidelines it is based on) rather than presenting claims as self-evident.",
                "A reliable source discloses how it is funded or published — who paid for this information to be produced — and is not primarily selling a product it is also endorsing.",
            ],
            "understand": ["Where a piece of health information came from matters at least as much as what it says — a claim without a traceable origin is a claim I cannot check."],
            "do": "I can complete a rubric-assessed written task comparing two health information sources on the same topic, stating which I trust more and naming two specific reasons from the three reliability criteria (author, evidence origin, funding/transparency).",
        },
        "C": {
            "know": [
                "Types of evidence used in health claims: anecdote (one person's story — weakest for generalising); correlation (two things appearing together — does not establish cause); controlled study (compares a group receiving a treatment with a matched group that does not — strongest of these three).",
                "Common bias indicators: financial interest (the claim-maker profits from the claim); ideological stake (the claim reinforces a pre-held worldview the source is committed to); selective data (only favourable findings cited, contradicting evidence ignored); undisclosed conflicts of interest (the source has a stake not declared upfront).",
            ],
            "understand": ["Different kinds of evidence carry different weight, and the person making a health claim almost always has something at stake — recognising both is the foundation of thinking about claims rather than just reacting to them."],
            "do": "I can complete a rubric-assessed written analysis of a single health claim that names the type of evidence it rests on (anecdote / correlation / controlled study), names any bias indicators present in the source, and states and justifies my conclusion about how much weight to give the claim.",
        },
        "D": {
            "know": [
                "Evidence hierarchy in health research: systematic reviews of randomised controlled trials (strongest) > single RCT > cohort study > case-control study > cross-sectional study > expert opinion > anecdote (weakest).",
                "Signals of a stronger argument: consistency with multiple independent sources; specific rather than sweeping claims; acknowledges what it does not explain; cites peer-reviewed evidence.",
                "Signals of a weaker argument: rests on a single study; uses absolute language ('always', 'never', 'cures'); substitutes tradition or authority for evidence; dismisses rather than addresses contradicting evidence.",
                "Principles of critical appraisal: check the source (who); check the evidence type (what kind); check for replication (has it been reproduced); check for conflicts of interest; check the argument's logical structure.",
            ],
            "understand": ["Health claims frequently contradict each other, and judging them well is a matter of weighing the quality of the evidence rather than the certainty of the tone or the closeness of the messenger."],
            "do": "I can complete a rubric-assessed written evaluation of a contested health claim (two or more sources disagreeing) that applies the evidence hierarchy, identifies the specific strongest and weakest arguments on each side, and justifies my conclusion with reference to the criteria of critical appraisal.",
        },
        "E": {
            "know": [
                "Peer review is the process by which other experts in a field assess a study before publication; its limitations include reviewer bias, slow pace, and routine failure to detect subtle methodological flaws.",
                "Clinical trial design: the randomised controlled trial (RCT) is the gold standard; what an RCT does prove — a specified treatment produces a specified outcome in a specified population under controlled conditions; what it does not prove — real-world effectiveness outside trial conditions, long-term effects beyond trial duration, applicability to populations excluded from the trial.",
                "Relative vs. absolute risk: a '50% increased risk' can mean 3 in 1000 instead of 2 in 1000 — the relative figure sounds alarming; the absolute figure is what is actually happening to an individual. Statistical significance (conventionally p < 0.05) indicates how unlikely an observed result is under a null hypothesis; confidence intervals (e.g. 95% CI) show the range within which the true effect is likely to lie.",
                "Funding and publication biases: industry-funded studies are more likely to report findings favourable to the funder's product; publication bias means negative findings are systematically under-published; selective outcome reporting within a study distorts the literature.",
            ],
            "understand": ["Health information is produced inside systems — funding, commercial interests, publication incentives, peer-review imperfections — and strong health literacy means being able to think about how that system shapes what reaches me, not only whether the last source I read was trustworthy."],
            "do": "I can complete a rubric-assessed written analysis of an evidence base supporting a specific health claim that judges whether the body of evidence warrants the confidence placed in the claim, identifies the commercial or institutional interests that may have shaped what research was done and published, and justifies my conclusion using peer-review, RCT-design, statistical, and funding-bias criteria.",
        },
        "F": {
            "know": [
                "Reading a systematic review or meta-analysis: key sections include the PICO question (Population / Intervention / Comparison / Outcome), search strategy, inclusion/exclusion criteria, risk-of-bias assessment, forest plot showing pooled effect sizes, heterogeneity measures (I²), and the GRADE evidence-quality summary.",
                "GRADE framework assesses evidence on four levels — high, moderate, low, very low — using study design, risk of bias, inconsistency, indirectness, imprecision, and publication bias.",
                "Regulatory bodies translating evidence into guidelines include WHO (global), NICE (UK clinical), EMA (European medicines), and the corresponding Hungarian bodies; each operates under its own mandate, review cycle, and political context.",
                "Guidelines are contested or revised when new evidence emerges, values or priorities shift, conflicts of interest are exposed, or external pressure reframes the risk-benefit calculation.",
            ],
            "understand": ["The distance between an individual research finding and a public-health guideline I am advised or required to follow is long and politically mediated — critical health literacy at the highest level is being able to trace that journey and judge its integrity."],
            "do": "I can complete a rubric-assessed analysis that reads and interprets a provided systematic review or meta-analysis at an introductory level (identifying PICO, risk-of-bias findings, pooled effect, and GRADE rating), traces how a named policy recommendation or guideline was derived from an evidence base, and evaluates whether that guideline is well-supported, weakly-supported, or contested, articulating what I am certain of, what remains uncertain, and why.",
        },
    },
}

# ── LT 7.1 ──
KUD["lt_7_1"] = {
    "lt_name": "Pattern Analysis & Adjustment",
    "competency": "C7 — Metacognitive Self-Direction",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Notice patterns in thinking or behaviour, analyse what drives them, design targeted adjustments, and build a structured personal metacognitive practice.",
    "prereq_lt_ids": ["lt_1_1", "lt_2_2", "lt_6_1"],
    "bands": {
        "A": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band A (basic body signals; what sleep and food do for the body and brain)."],
            "understand": ["Thinking about how I did something — not just what I did — is a different kind of thinking, and it helps me choose what to do next time."],
            "do": "I can complete a rubric-assessed short oral or written reflection in which I describe one specific thing I noticed about how I reacted to a given situation and state one thing I might do differently next time.",
        },
        "B": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band B (fight/flight/freeze; the habit loop — cue, routine, reward)."],
            "understand": ["Most of what I do in similar situations isn't random — I tend to respond in similar ways to similar triggers, and that repetition is data about me that I can use."],
            "do": "I can complete a rubric-assessed written or oral task in which I identify a specific pattern in how I tend to respond in a named type of situation, and offer one plausible reason for why that pattern might have formed.",
        },
        "C": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band C (amygdala and prefrontal cortex interaction under stress; neuroplasticity; habit-loop mechanism)."],
            "understand": ["Patterns have drivers — a specific thing that sets them off or a specific thing that keeps them going — and identifying the driver is what makes adjustment possible. Noticing a pattern on its own doesn't change much."],
            "do": "I can complete a rubric-assessed written analysis of a pattern across two or more situations that names the pattern specifically, identifies what drives it (cue, emotion, context, belief), and describes a specific adjustment I have made or will make based on the analysis.",
        },
        "D": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band D (stress, emotion, attention, and habit as interdependent system; HPA axis)."],
            "understand": ["What started a pattern is often different from what sustains it — old triggers, current reinforcement, environmental cues, social payoffs — and adjustments that only address the origin rarely hold. Lasting change has to address the sustaining conditions."],
            "do": "I can complete a rubric-assessed written analysis that evaluates a pattern in my thinking or responses across different contexts, distinguishes what originally set up the pattern from what now sustains it, describes a specific adjustment I have implemented, and reports the effect observed.",
        },
        "E": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band E (allostatic load; adolescent-brain-specific mechanisms; intervention-evaluation criteria)."],
            "understand": ["Applying metacognition systematically to high-stakes work is a different practice from everyday reflection — it requires being honest about patterns that are uncomfortable to see, and holding myself accountable to the specific adjustments I committed to, including when results are disappointing."],
            "do": "I can complete a rubric-assessed structured metacognitive protocol applied to a named high-stakes academic or personal challenge, comprising: a mapping of my typical patterns in this domain, an identification of the sustaining conditions, a specific intervention designed against those conditions, a tracking record of the intervention's effects over a defined period, and an iteration based on what the tracking showed.",
        },
        "F": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band F (integrative neuroscience; critical neuroscience literacy) and LT 6.2 Band F (evidence-to-policy tracing)."],
            "understand": ["Metacognitive self-direction is not a school skill I apply only inside a classroom — it is the mechanism by which I continue to learn, adjust, and develop in any domain I enter next, and making it explicit as a personal framework is how I carry it forward into contexts no teacher will be present for."],
            "do": "I can construct a rubric-assessed personal metacognitive framework document: a named, explicit set of strategies, prompts, and monitoring practices I have developed and tested across at least two domains, with evidence of testing and iteration, and an articulated application plan for the next phase of my learning and life beyond school.",
        },
    },
}

# ── LT 7.2 ──
KUD["lt_7_2"] = {
    "lt_name": "Self-Direction in Practice",
    "competency": "C7 — Metacognitive Self-Direction",
    "knowledge_type": "T3",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Consistently direct own thinking and learning — noticing, analysing, and adjusting patterns without external prompting across time and contexts.",
    "prereq_lt_ids": ["lt_7_1", "lt_1_1", "lt_6_1"],
    "bands": {
        "A": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band A (basic body signals; what sleep and food do for the body and brain)."],
            "understand": ["When something doesn't work, trying differently is a choice I have — not a sign I have failed, and not something that has to happen only if an adult tells me."],
            "do": "The teacher notices the student stopping and trying a different approach when the first attempt does not work, without needing to be told, on most occasions of minor setback across more than one type of task. After a setback, the student names what happened rather than dismissing it.",
        },
        "B": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band B (fight/flight/freeze; habit loop)."],
            "understand": ["What I've learned about myself only becomes useful when I remember to use it — and remembering is a habit I can build, not a sign of how smart I am."],
            "do": "The teacher notices the student referring back to a strategy they have previously found helpful in a similar type of situation, without being prompted to do so. After a task, the student volunteers one specific observation about how they worked, not a general evaluation of the task.",
        },
        "C": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band C (amygdala and prefrontal cortex under stress; neuroplasticity; habit-loop mechanism)."],
            "understand": ["Pattern-recognition about myself is most valuable when I catch it in the moment — because that is when I can do something about it — not only when I reflect on it afterwards."],
            "do": "The teacher notices the student identifying a pattern in how they respond across more than one situation and naming it spontaneously in conversation, on multiple occasions across a term. In a task, the student adjusts their approach mid-way in response to noticing that something is not working, without teacher prompt.",
        },
        "D": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band D (stress, emotion, attention, habit as interdependent system; HPA axis)."],
            "understand": ["Metacognitive self-direction is not a single habit I can check off but a disposition to treat myself as someone I am learning about continuously — a stance, not a technique."],
            "do": "The teacher notices the student articulating a specific adjustment they have made to their thinking or behaviour and describing its effect across more than one domain, without prompting. In novel or challenging situations, the student applies a self-awareness strategy without an adult prompt. The student makes connections between wellbeing learning and behaviour in other contexts unprompted, on multiple occasions.",
        },
        "E": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band E (allostatic load; adolescent-brain specifics; intervention-evaluation criteria)."],
            "understand": ["Self-direction is not only about my own development — supporting it in others through questions rather than answers is how a genuine learning community is built, and doing that strengthens rather than depletes my own practice."],
            "do": "The teacher notices the student initiating metacognitive reflection without any external prompt across sustained periods of challenging work. When working with peers, the student naturally facilitates the peers' self-reflection through open questions rather than giving advice or answers, on multiple observed occasions. The student demonstrates stable self-directedness when feedback challenges their self-assessment.",
        },
        "F": {
            "know": ["None standalone. Know content supporting this band lives in LT 6.1 Band F (integrative neuroscience; critical neuroscience literacy) and LT 7.1 Band F (personal metacognitive framework)."],
            "understand": ["By this band, metacognitive self-direction should be identity-deep — not a set of techniques I apply when I remember but a way of being in relation to my own growth that I carry with me into any context, including ones no teacher is present for."],
            "do": "The teacher or mentor notices the student demonstrating a stable, articulated metacognitive identity — a consistent pattern of how they learn, reflect, and adjust — that they can describe to others without rehearsing it, and that persists across highly novel, high-stakes, or unfamiliar contexts without any scaffolding. The student connects their wellbeing learning to their sense of who they are and who they are becoming, unprompted and with specificity, on multiple occasions including in Reflection 360.",
        },
    },
}

# ── LT 8.1 ──
KUD["lt_8_1"] = {
    "lt_name": "Information Verification & Media Literacy",
    "competency": "C8 — Critical Digital Literacy",
    "knowledge_type": "T2",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Locate claims in digital content, assess credibility, identify manipulation signs, and justify what to believe, share, or act on as a result.",
    "prereq_lt_ids": ["lt_2_2"],
    "bands": {
        "A": {
            "know": [
                "Something 'real' is something that actually happened in the world the way it is shown; something 'made up' is something a person imagined or created for a story, game, or joke.",
                "When a child is not sure whether something they saw online, in a video, or in a picture is real, the correct response is to ask a specific trusted adult (parent, teacher, school counsellor).",
            ],
            "understand": ["Things I see on a screen are not automatically true — people make them up sometimes, and checking with a grown-up is a skill, not a sign I don't know."],
            "do": "I can complete a rubric-assessed short oral or written task in which I am shown an age-appropriate piece of digital content, say whether I think it is real or made up, explain my reasoning in a sentence, and name a trusted adult I would ask if I wasn't sure.",
        },
        "B": {
            "know": [
                "Every piece of digital content — a video, a post, an article, a picture — has a maker: a named person, an organisation, or an account. Finding the maker is the first step in deciding whether to trust the content.",
                "A trusted place for information has a specific marker: it is from a named, real organisation (school, library, newspaper, health service), or from a person whose qualifications relate to what they are talking about, not just from someone with a lot of followers.",
                "A claim is not more true just because more people have shared it or reacted to it.",
            ],
            "understand": ["Where something came from matters at least as much as what it says — and the maker of a claim is information I can look for, not a mystery."],
            "do": "I can complete a rubric-assessed short written task, given two pieces of digital content on the same topic, in which I identify the maker of each, state whether each maker is from a 'trusted place' and why, and explain why I do or do not believe each piece of content.",
        },
        "C": {
            "know": [
                "Lateral reading is the practice of opening a new tab and searching for information about the source before deciding whether to trust what it says — rather than reading only within the source itself.",
                "Signs a piece of content has been edited or designed to mislead: cropped images (showing only part of what happened), out-of-context quotes, misleading headlines, staged or reused video, emotionally-loaded language that does not match the evidence, missing date or context.",
                "A comparison of two sources can reveal where they agree, where they disagree, and where one of them is leaving something out.",
            ],
            "understand": ["A claim on its own tells me less than the same claim compared to other sources — and deception usually leaves specific signs I can learn to spot, not a vague feeling."],
            "do": "I can complete a rubric-assessed written comparison of two sources making the same claim in which I apply lateral reading to find out who is behind each source, name specific manipulation signs present or absent in each, and justify which source I trust more with at least two named criteria.",
        },
        "D": {
            "know": [
                "A verification process (e.g. SIFT: Stop, Investigate the source, Find better coverage, Trace claims to the original context) is a named sequence of steps that can be applied to any claim, not just ones already flagged as suspicious.",
                "The motivation of a source refers to what the source has to gain from the claim being believed — money, attention, political outcome, reputation, advocacy. Motivation does not automatically mean a source is wrong, but an undisclosed motivation is a reason to check further.",
                "Believe, share, and act are three different decisions about a claim: I might believe something is plausibly true, still choose not to share it because I cannot verify it, and not act on it until I have stronger evidence.",
            ],
            "understand": ["What I believe, what I share, and what I act on are three different decisions about the same claim — and treating them as separate is what keeps me from accidentally amplifying something I haven't actually checked."],
            "do": "I can complete a rubric-assessed written analysis of a digital claim in which I apply a named verification process (e.g. SIFT) to the claim, identify the origin, the evidence behind it, and the motivation of the source, and justify my separate conclusions about what I would believe, what I would share, and what I would act on.",
        },
        "E": {
            "know": [
                "Recommendation algorithms on major platforms are typically optimised for engagement — time on platform, clicks, reactions — not for accuracy or user wellbeing; content that provokes strong emotional reactions is amplified more than neutral content.",
                "Platform incentives shape what is produced: creators whose livelihood depends on reach will tend to produce content the algorithm rewards.",
                "Filter-bubble and echo-chamber effects: repeated engagement with a viewpoint tends to increase recommendations for similar content, narrowing exposure over time; the effect is partial and contested in magnitude, but the mechanism is real.",
                "Confirmation bias is the tendency to believe, share, and remember claims that align with what one already thinks; it operates below conscious awareness and is stronger under emotional activation.",
                "Motivated reasoning: when a conclusion serves an identity or group belonging, the reasoning process selects evidence supporting that conclusion and dismisses evidence against it.",
            ],
            "understand": ["A claim does not arrive in my feed by accident — the system that chose to show it to me, and the mental system that receives it, both have biases I can learn to read."],
            "do": "I can complete a rubric-assessed written evaluation of a contested claim in which I weigh evidence across multiple sources using named criteria, identify at least two specific algorithmic, platform, or production-incentive factors that shaped how the claim reached me, name the self-bias most likely to affect my interpretation, and justify my conclusion with explicit awareness of that bias.",
        },
        "F": {
            "know": [
                "Synthetic media: AI-generated images, video, and audio can now pass casual perception in ways earlier manipulation could not; detection methods include reverse image search, metadata inspection, and specialised detectors, but no detection method is reliable on all cases.",
                "Sophisticated disinformation is purpose-built to pass early verification — plausible source, credible-looking evidence, multiple corroborating posts generated or coordinated by the same actor.",
                "Recognised critical-appraisal criteria for claims include: source provenance, evidence traceability, corroboration across independent sources, plausibility against base rates, internal coherence, and epistemic transparency.",
                "Epistemic humility in verification: for some real-world contested claims, the honest conclusion is 'the available evidence does not let me decide with confidence, and here is specifically what I cannot know' — and that is a legitimate analytical output, not a failure.",
            ],
            "understand": ["At the highest level of media literacy, knowing what I cannot know — and being specific about the boundary — is a more reliable guide than any verification tool, because the tools can be defeated but the honest acknowledgement of limits cannot."],
            "do": "I can complete a rubric-assessed written analysis of a real-world contested claim involving synthetic, AI-generated, or sophisticated disinformation, in which I apply detection and verification methods, compare my verification process against a recognised critical-appraisal framework, and construct a reasoned conclusion that states what I believe, what I would share, what I would act on, and — specifically — what I cannot know and why.",
        },
    },
}

# ── LT 8.2 ──
KUD["lt_8_2"] = {
    "lt_name": "Digital Influence & Psychological Agency",
    "competency": "C8 — Critical Digital Literacy",
    "knowledge_type": "T2",
    "compound": True,
    "band_range": {"start": "C", "end": "F"},
    "summary": "Identify how digital products shape attention and behaviour, analyse personal effects, and justify reasoned responses to persuasive design systems.",
    "prereq_lt_ids": ["lt_6_1", "lt_2_1", "lt_2_2"],
    "bands": {
        "C": {
            "know": [
                "Persuasive design is a general term for features built into digital products deliberately to keep people using them or returning to them — not an accident, not a free service, but engineered for a business purpose.",
                "Named persuasive-design features students should be able to identify: infinite scroll (no natural stopping point); pull-to-refresh (a small action that produces a new result — the same mechanism as a slot machine); autoplay (next content starts without a decision); notifications (interruptions optimised to trigger checking); streaks and daily rewards (rewards for returning).",
                "Variable reward: when a reward comes at unpredictable intervals rather than on a fixed schedule, the brain anticipates it more strongly — because the uncertainty itself triggers dopamine.",
                "An 'effect on me' is observable and specific: how long I ended up using it vs. how long I planned, how I felt during use, how I felt afterwards, what I did or didn't do because of it.",
            ],
            "understand": ["Digital products are not neutral tools — they are environments designed to affect how I use my time, attention, and feelings, and noticing this is different from liking or disliking them."],
            "do": "I can complete a rubric-assessed short written analysis of a chosen digital product in which I identify one specific persuasive-design feature using correct vocabulary, describe one reason (drawing on dopamine / reward / habit-loop mechanism) the design works on people, and explain one specific effect I have noticed on myself (time, mood, behaviour).",
        },
        "D": {
            "know": [
                "Vocabulary load for design analysis: variable reward, intermittent reinforcement, novelty bias, social-validation feedback (likes, views, comments), push notifications, interruption cost, scroll friction, dark patterns.",
                "Three dimensions of design effect — attention (what captures it, for how long); emotion (what it triggers — anxiety, envy, outrage, anticipation); behaviour (what I do or don't do as a result).",
                "Attention residue is the finding that even brief task-switching into a digital product leaves a trail — cognitive performance remains degraded for several minutes after the interruption.",
                "The attention triangle (from LT 2.1 Band C): persuasive design primarily operates on the environment lever, not on awareness or energy — which is why 'just try harder' fails as a response.",
            ],
            "understand": ["Persuasive design isn't about individual willpower — it is about the environment acting on the person, and the most useful response is environmental rather than effortful."],
            "do": "I can complete a rubric-assessed written analysis of a chosen digital product using the 'attention / emotion / behaviour' framework in which I identify at least two interacting persuasive-design features using correct vocabulary, analyse how each shapes attention, emotion, or behaviour in the product, and explain one specific effect I have noticed on my own thinking, mood, or time.",
        },
        "E": {
            "know": [
                "Recommendation algorithms are optimised for engagement metrics (time on platform, clicks, reactions, shares), not accuracy, wellbeing, or diversity of viewpoint.",
                "Engagement-driven amplification: content producing stronger emotional reactions (outrage, anxiety, awe, desire) spreads faster and further than neutral content — so the feed I see is systematically more emotionally activating than a random sample of the content posted.",
                "The attention economy business model: the product is free to the user; the user's attention is sold to advertisers; therefore the platform's financial incentive is aligned with maximising attention captured, not with maximising user benefit.",
                "Surveillance capitalism names the specific way personal behavioural data is extracted, processed, and sold as a commodity — not an incidental side effect but the core product for the platform.",
                "The distinction between persuasion and manipulation: persuasion respects the target's capacity to refuse; manipulation bypasses that capacity.",
            ],
            "understand": ["A claim does not arrive in my feed by accident — the system that chose to show it has specific psychological and economic reasons to choose it, and those reasons are not the same as my interests."],
            "do": "I can complete a rubric-assessed written evaluation of a chosen digital platform in which I evaluate how the platform algorithmically curates what I see (with evidence from my own observation or documentation), explain at least two specific psychological or economic incentives driving that design decision, and justify one specific change I will make to my use of the platform based on my analysis — including why that change addresses the mechanism, not just the symptom.",
        },
        "F": {
            "know": [
                "Research domains on digital wellbeing: Twenge and Haidt argue adolescent mental-health declines since ~2012 are substantially attributable to smartphone and social-media use; Orben, Przybylski, and others argue effect sizes are small, confounded, and the direction of causation is contested. Neither position is settled; both are published in peer-reviewed literature.",
                "Mechanisms most credibly supported by current evidence: sleep displacement; social-comparison effects (especially for adolescent girls and image-based platforms); attention fragmentation; some association (weaker effect sizes) with anxiety and depression in heavy users.",
                "Mechanisms less credibly supported: strong unidirectional causation from screen time alone to mental illness; universal effects across populations and content types.",
                "Identity effects of sustained platform use: the self that is repeatedly presented for feedback becomes the self that is reinforced; curation of a presented self over time shapes the felt self.",
                "Consent and agency framing: the mature question is not 'should screens be banned?' but 'under what specific conditions am I prepared for these systems to operate on me, and under what conditions am I not?'",
            ],
            "understand": ["At the most sophisticated level of this capability, the relevant question is not whether these systems affect me but which specific effects I consent to, which I refuse, and where the line is for me — held with awareness that the research on their cumulative effects is still being established."],
            "do": "I can complete a rubric-assessed written analysis that evaluates the cumulative effect of persuasive design across a sustained period on my attention, relationships, and identity — drawing on my own evidence, compares my analysis against at least two recognised pieces of research on digital wellbeing, including at least one that contests a claim I find sympathetic, and articulates a reasoned personal position specifying where I will and will not allow these systems to operate on me, acknowledging what the evidence supports strongly, weakly, and where it remains genuinely uncertain.",
        },
    },
}

# ── LT 8.3 ──
KUD["lt_8_3"] = {
    "lt_name": "Digital Assertiveness & Wellbeing Strategies",
    "competency": "C8 — Critical Digital Literacy",
    "knowledge_type": "T3",
    "compound": False,
    "band_range": {"start": "A", "end": "F"},
    "summary": "Maintain healthy digital boundaries, communicate assertively online, and sustain wellbeing-supporting practices across platforms and contexts over time.",
    "prereq_lt_ids": ["lt_1_1", "lt_5_1", "lt_8_2", "lt_4_1"],
    "bands": {
        "A": {
            "know": ["Know content for this band lives in LT 6.1 Band A (basic body signals) and the parallel work in LT 4.1 Band A (trusted adults in specific settings; my body is mine)."],
            "understand": ["When something on a screen makes me feel confused or upset, telling a grown-up I trust is what keeps me safe — it is not getting someone in trouble and it is not a sign I did something wrong."],
            "do": "The child stops using a digital device when a trusted adult asks, without significant distress, on most occasions. The child tells a trusted adult when they see or are shown something online that makes them feel confused, scared, or uncomfortable, across more than one observed occasion. The child does not share personal information with strangers in digital contexts — their name, address, school, or family details.",
        },
        "B": {
            "know": ["Know content for this band lives in LT 6.1 Band B (fight/flight/freeze; habit loop) and LT 5.1 Band B (simple assertive language — 'I don't want to', 'please stop')."],
            "understand": ["The ways I protect myself in person — saying no, walking away, telling someone — are the same moves I can make online, even when the person is far away and I can't see them."],
            "do": "The child exits digital content they recognise as unkind, distressing, or inappropriate for them, without needing an adult to direct them, on most observed occasions. The child uses simple assertive language in digital communication — 'I don't want to', 'please stop', 'I'm going to tell an adult' — when a peer behaves unkindly online. The child keeps to family or school rules about device use — time, place, content — without constant reminders.",
        },
        "C": {
            "know": ["Know content for this band lives in LT 6.1 Band C (amygdala and prefrontal cortex under stress; habit-loop mechanism), LT 8.2 Band C (named persuasive-design features, variable reward), and LT 5.1 Band C (repair routine and direct boundary statements)."],
            "understand": ["A digital boundary I set for myself is different from a rule someone set for me — I can keep it not because I am told to but because I have chosen what kind of digital life I want to have."],
            "do": "The student names their own digital boundaries — when they will and will not use a device, what they will and will not engage with — and largely keeps to them without external reminders, across multiple contexts. The student speaks up or exits group chats, games, or platform interactions where peers behave unkindly, excludingly, or unsafely. The student takes independent action when content or interaction is affecting their wellbeing — muting, blocking, unfollowing, reporting, stepping away — without adult prompt.",
        },
        "D": {
            "know": ["Know content for this band lives in LT 6.1 Band D (stress/emotion/attention/habit as system), LT 8.2 Band D (attention/emotion/behaviour framework; attention residue; dark patterns), and LT 5.1 Band D (paraphrase technique; I-statements under pressure)."],
            "understand": ["Self-care in a digital environment is a deliberate practice, not a default — because the environment is actively working against it, my wellbeing-supporting practices have to be designed and sustained on purpose."],
            "do": "The student maintains their stated digital boundaries under social pressure — friends pushing them to re-join a chat, return to a game, check a notification — on more than one observed occasion. The student uses assertive communication in difficult digital interactions without escalating into harshness, abandoning the conversation, or capitulating against their stated position. The student adjusts their digital practice in response to evidence they have collected about its effects on their attention, mood, or sleep — and can point to the adjustment and the evidence that drove it when asked.",
        },
        "E": {
            "know": ["Know content for this band lives in LT 6.1 Band E (allostatic load; adolescent-brain specifics), LT 8.2 Band E (algorithmic curation; attention economy; motivated reasoning), and LT 5.1 Band E (facilitation of difficult conversations)."],
            "understand": ["Sustained digital wellbeing is not a performance I put on when tracked and drop when not — it is what I actually do, which is why the test is what happens in the ordinary weeks when nobody is watching."],
            "do": "The student sustains digital wellbeing practices across extended periods — not only in a week when someone is tracking, but as an integrated part of their life, across terms. The student holds their position in digital disagreements or conflicts without becoming harsh, performative, or retreating — showing substantive assertiveness that addresses the other person's argument rather than their identity or the audience. The student notices when their digital practice is not serving them well and adjusts proactively — before a crisis or a forced break — on more than one observed occasion across the year.",
        },
        "F": {
            "know": ["Know content for this band lives in LT 6.1 Band F (integrative neuroscience; critical wellbeing-science literacy), LT 8.2 Band F (research-anchored position on persuasive design), LT 1.3 Band F (integrated personal identity across contexts), and LT 5.1 Band F (mature facilitation)."],
            "understand": ["Mature digital agency is an expression of who I am — not a set of rules I follow, not a performance I curate for others, and not a protest I advertise — and the proof is that the way I behave online is the way I behave, full stop."],
            "do": "The student treats their digital life as an expression of their values — what they engage with, what they create, what they refuse — and can articulate this stance when asked, without turning it into a public performance. The student supports peers navigating digital pressure, conflict, or harm, without taking over the situation, without shaming the peer for being in it, and with authentic respect for the peer's own agency. The student holds consistent digital practices across contexts without the quality shifting based on who is watching.",
        },
    },
}

# ── LT order ─────────────────────────────────────────────────────────────────
LT_ORDER = [
    "lt_1_1", "lt_1_2", "lt_1_3",
    "lt_2_1", "lt_2_2",
    "lt_3_1", "lt_3_2",
    "lt_4_1", "lt_4_2", "lt_4_3",
    "lt_5_1", "lt_5_2",
    "lt_6_1", "lt_6_2",
    "lt_7_1", "lt_7_2",
    "lt_8_1", "lt_8_2", "lt_8_3",
]

T3_LTS = {"lt_1_1", "lt_1_2", "lt_1_3", "lt_3_2", "lt_5_2", "lt_7_2", "lt_8_3"}
ALL_BANDS = ["A", "B", "C", "D", "E", "F"]

# ── Build unified entries ────────────────────────────────────────────────────
def band_label_full(band: str) -> str:
    labels = {
        "A": "A", "B": "B", "C": "C",
        "D": "D", "E": "E", "F": "F",
    }
    return labels[band]


def build_entry(lt_id: str) -> dict:
    meta = KUD[lt_id]
    start = meta["band_range"]["start"]
    end   = meta["band_range"]["end"]
    active_bands = ALL_BANDS[ALL_BANDS.index(start) : ALL_BANDS.index(end) + 1]

    bands_out = {}
    for band in active_bands:
        band_kud = meta["bands"][band]
        cb = lt_band_data.get((lt_id, band), {"criterion_ids": [], "observation_indicators": []})

        is_t3 = lt_id in T3_LTS
        obs = cb["observation_indicators"] if is_t3 else []

        bands_out[band] = {
            "know":                  band_kud["know"],
            "understand":            band_kud["understand"],
            "do":                    band_kud["do"],
            "criterion_ids":         cb["criterion_ids"],
            "prerequisite_lt_ids":   meta["prereq_lt_ids"],
            "observation_indicators": obs,
        }

    return {
        "lt_id":          lt_id,
        "lt_name":        meta["lt_name"],
        "competency":     meta["competency"],
        "knowledge_type": meta["knowledge_type"],
        "compound":       meta["compound"],
        "band_range":     meta["band_range"],
        "summary":        meta["summary"],
        "bands":          bands_out,
    }


learning_targets = [build_entry(lt_id) for lt_id in LT_ORDER]

unified = {
    "meta": {
        "schema_version": SCHEMA_VERSION,
        "generated_date": "2026-04-23",
        "lt_count": len(learning_targets),
    },
    "learning_targets": learning_targets,
}

with open(UNIFIED_OUT, "w") as f:
    json.dump(unified, f, indent=2, ensure_ascii=False)

print(f"Wrote {UNIFIED_OUT}")

# ── Build index ──────────────────────────────────────────────────────────────
index_entries = []
for lt_id in LT_ORDER:
    meta = KUD[lt_id]
    index_entries.append({
        "lt_id":          lt_id,
        "lt_name":        meta["lt_name"],
        "competency":     meta["competency"],
        "knowledge_type": meta["knowledge_type"],
        "band_range":     meta["band_range"],
        "summary":        meta["summary"],
    })

index = {
    "meta": {
        "schema_version": SCHEMA_VERSION,
        "generated_date": "2026-04-23",
        "lt_count": len(index_entries),
    },
    "learning_targets": index_entries,
}

with open(INDEX_OUT, "w") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print(f"Wrote {INDEX_OUT}")
print("Done.")
