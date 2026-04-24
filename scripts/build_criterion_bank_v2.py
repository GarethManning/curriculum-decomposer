#!/usr/bin/env python3
"""
Build criterion-bank-v2.json from criterion-bank-v2-partial.json.

Actions:
1. Restructure existing T3 entries (A-D) for LT 1.1, 1.2, 3.2, 5.2, 7.2
2. Add new T3 entries E-F for those 5 LTs
3. Add LT 1.3 T2 entries (A-F) and LT 1.3 T3 entries (A-F)
4. Add LT 8.3 T3 entries (A-F)
5. Validate DAG, update strand summaries, write output.
"""
import json
import copy
import sys
from collections import defaultdict, deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from band_constants import BAND_LABELS  # noqa: E402

BASE = Path("/Users/garethmanning/Github/curriculum-harness/docs/reference-corpus/real-wellbeing")
IN = BASE / "criterion-bank-v2-partial.json"
OUT = BASE / "criterion-bank-v2.json"

PREFIX = "real-wellbeing-2026-04_crit_"


def cid(n): return f"{PREFIX}{n:04d}"


# ---------------------------------------------------------------------------
# Content for RESTRUCTURED T3 entries (LT 1.1, 1.2, 3.2, 5.2, 7.2 Bands A-D)
# Keyed by criterion_id.
# ---------------------------------------------------------------------------
RESTRUCTURE = {
    # ============= LT 1.1 Self-Awareness & Regulation =============
    cid(1): {
        "criterion_statement": "The student pauses to notice body signals and emotional activation, names what they are feeling, and uses a practised calming strategy to return to learning, without needing step-by-step adult direction.",
        "criterion_label": "[Band A] Self-Awareness & Regulation (dispositional observation)",
        "observation_indicators": [
            "The student pauses to name a feeling (\"I'm frustrated\", \"I'm tired\") before reacting when emotional activation rises, on most occasions visible to the teacher.",
            "The student selects a practised calming strategy (deep breath, water, movement break, quiet corner) without needing step-by-step adult direction.",
            "The student returns to the learning activity after using a strategy, rather than requiring an adult to redirect them each time.",
            "The student names body signals (tight tummy, hot face, fast heart) as they arise, not only after the moment has passed.",
        ],
        "confusable_behaviours": [
            "Compliance with adult-directed calming (following an instruction to \"take a breath\") mistaken for self-regulation. Distinction: the disposition is visible when the adult has not prompted and the student initiates the pause themselves.",
            "Emotional suppression (freezing and going quiet) mistaken for calming. Distinction: suppression is visible as withdrawal of affect; regulation is visible as return to engagement after a brief self-directed pause.",
        ],
        "absence_indicators": [
            "In classroom moments of frustration, the student's first response is consistently externalised (shouting, tears, hitting the desk) with no observable pause.",
            "The student relies on the same adult for every regulation episode, with no transfer to self-directed use of practised strategies.",
        ],
        "conversation_prompts": [
            "Tell me about a time this week when you felt a big feeling. What did your body do?",
            "When you use your calming corner or your breathing, what do you notice changes?",
            "Tell me about a time a feeling surprised you — what was it, and what was going on?",
        ],
    },
    cid(2): {
        "criterion_statement": "The student notices recurring personal triggers, chooses from a practised repertoire of regulation strategies before activation escalates, and does so across more than one setting.",
        "criterion_label": "[Band B] Self-Awareness & Regulation (dispositional observation)",
        "observation_indicators": [
            "The student names a recurring personal trigger (end-of-morning hunger, group work with a specific peer, maths-problem frustration) in their own words, not only after the fact.",
            "The student chooses from a practised repertoire of strategies (not only the single strategy they learned first) based on what the trigger is.",
            "The student applies a regulation strategy before activation escalates in at least two different settings (classroom work, playground, group work).",
            "The student comments on strategies that did or didn't work for them without adult prompting.",
        ],
        "confusable_behaviours": [
            "Routine compliance (using the same strategy every time because it is the one the class was taught) mistaken for trigger-responsive regulation. Distinction: look for the student picking a strategy that fits the situation, not applying a default.",
            "Avoidance (deliberately steering around a known trigger) mistaken for regulation. Distinction: avoidance reduces exposure; regulation shows up when the student stays in the situation and manages their state.",
        ],
        "absence_indicators": [
            "The student can name strategies abstractly but only applies them with adult reminder, even when a known trigger is active.",
            "The student's triggers recur predictably and the response pattern remains unchanged across weeks (same escalation, same adult intervention, no emerging self-action).",
        ],
        "conversation_prompts": [
            "What's something that sets you off at school — and how do you usually know it's starting?",
            "Tell me about a time you caught yourself early this month. What did you do?",
            "Which of your calming strategies feels most like it actually works — and which one doesn't?",
        ],
    },
    cid(3): {
        "criterion_statement": "The student applies a regulation strategy in a genuinely challenging situation and afterwards explains what worked and what didn't, adjusting their choice of strategy based on what they have learned.",
        "criterion_label": "[Band C] Self-Awareness & Regulation (dispositional observation)",
        "observation_indicators": [
            "The student applies a regulation strategy in a genuinely challenging moment (not a rehearsed low-stakes practice), on multiple occasions across a term.",
            "Afterwards — spontaneously or on a brief prompt — the student explains what worked and what didn't, rather than only reporting \"I used my strategy\".",
            "The student adjusts choice of strategy based on what they have learned from earlier attempts, not by sticking to one default.",
            "The student distinguishes strategies that genuinely helped from those that felt like they should have helped but didn't.",
        ],
        "confusable_behaviours": [
            "Post-hoc narration of compliance (\"I did the breathing\") mistaken for strategic reflection. Distinction: the disposition shows when the student can point to something that didn't work and explain why, not only successes.",
            "Rehearsal fluency (being able to describe strategies in a reflection lesson) mistaken for in-the-moment application. Distinction: the evidence is visible in the middle of a hard situation, not in planned reflection.",
        ],
        "absence_indicators": [
            "The student performs regulation language convincingly in low-stakes settings but reverts to pre-strategy patterns the moment genuine difficulty lands.",
            "The student's post-hoc reflections stay at the level of \"it worked\" / \"it didn't work\" with no specificity about what or why.",
        ],
        "conversation_prompts": [
            "When do you find it easiest to use a regulation strategy, and when does it feel hardest?",
            "Tell me about a time a strategy you expected to work didn't — what happened?",
            "How has the set of strategies you rely on changed across this year?",
        ],
    },
    cid(4): {
        "criterion_statement": "The student applies different regulation strategies across different settings, explains without prompt why one fits one setting and not another, and names a specific change they are going to try next.",
        "criterion_label": "[Band D] Self-Awareness & Regulation (dispositional observation)",
        "observation_indicators": [
            "The student applies different regulation strategies across different settings (academic task pressure, peer friction, home-context reports), not a single default everywhere.",
            "The student explains — without adult prompt — why one strategy fits one setting and not another (what the context allows, what the activation pattern is).",
            "The student names a specific, concrete change to their regulation practice they are going to try next, grounded in what they have learned.",
            "The student adjusts strategies when a previously reliable one stops working in a new context.",
        ],
        "confusable_behaviours": [
            "Context-matching as performance (using the \"right\" strategy because that's what the adult expects in this room) mistaken for authentic context-sensitivity. Distinction: the disposition shows in the student's own reasoning about fit, not in conformity to classroom norms.",
            "Sophisticated talk about regulation in reflection without corresponding behaviour change across contexts mistaken for integration. Distinction: the student's practice in home-context and peer-context settings should register the growth, not only in supervised school settings.",
        ],
        "absence_indicators": [
            "The student uses one consistent strategy in all contexts, with no adjustment when context or available resources change.",
            "The student can discuss context-sensitivity fluently but reports from parents and other settings show the same reactivity pattern the student had a year ago.",
        ],
        "conversation_prompts": [
            "Where does your regulation feel most reliable and where does it still feel effortful?",
            "How has your approach shifted between school, home, and friendships this year?",
            "What's the next change you're thinking about making — and what's making you think it's time?",
        ],
    },

    # ============= LT 1.2 Social Awareness & Empathy =============
    cid(5): {
        "criterion_statement": "The student notices and names feelings in others, and offers a kind word or specific helpful action in response, without adult direction.",
        "criterion_label": "[Band A] Social Awareness & Empathy (dispositional observation)",
        "observation_indicators": [
            "The student names a feeling another child is showing (sad, worried, left out) in their own words, not only their own feelings.",
            "The student offers a kind word or a specific helpful action (sitting with, inviting to play, sharing) in response, without adult direction.",
            "The student notices the emotion of a quieter or less visible child, not only children who are loudly upset.",
        ],
        "confusable_behaviours": [
            "Rule-following (reciting \"use kind words\") mistaken for empathic noticing. Distinction: empathic response is triggered by what the student sees in the other child; rule-following is triggered by an adult instruction or routine.",
            "Performative sweetness (being kind because it earns adult approval) mistaken for empathy. Distinction: empathic action usually happens without an audience watching.",
        ],
        "absence_indicators": [
            "When another child is visibly upset nearby, the student proceeds without apparent notice, even in small settings where the signal is clear.",
            "The student's kind actions are tightly tied to being observed by an adult — the behaviour drops when adult attention moves away.",
        ],
        "conversation_prompts": [
            "Tell me about a time this week when you noticed someone felt sad or worried. How did you know?",
            "Tell me about a time you made somebody feel better. What did you do?",
            "When you see someone on their own at break, what goes through your head?",
        ],
    },
    cid(6): {
        "criterion_statement": "The student takes a peer's perspective in their own words, asks before acting on assumption about what the peer needs, and accepts a \"no\" without pushing.",
        "criterion_label": "[Band B] Social Awareness & Empathy (dispositional observation)",
        "observation_indicators": [
            "The student describes a situation from another person's perspective in their own words (not only restating what the other said).",
            "The student asks \"do you want help?\" (or an equivalent check-in) before acting on their assumption about what the other person needs.",
            "The student accepts a \"no\" or \"I'm fine\" from a peer without pushing, continuing to help anyway, or taking the refusal personally.",
            "The student spontaneously verifies rather than guesses when emotional signals are ambiguous, on multiple occasions.",
        ],
        "confusable_behaviours": [
            "Assuming and acting (bringing a peer something without asking because \"I thought you'd want it\") mistaken for empathic responsiveness. Distinction: the disposition shows in checking first, especially when the \"help\" would otherwise be directive.",
            "Ritualised asking (\"do you want help?\" as an automatic phrase) mistaken for genuine check-in. Distinction: the disposition includes actually listening to and acting on the answer.",
        ],
        "absence_indicators": [
            "The student defaults to their own interpretation of what a peer needs and is visibly surprised or upset when the peer's version differs.",
            "The student pushes past a \"no\" when it contradicts their picture of helping, or becomes hurt when help is declined.",
        ],
        "conversation_prompts": [
            "Tell me about a time someone felt differently than you expected about something — what did you learn?",
            "When is it easiest to ask how someone is feeling, and when is it hardest?",
            "Tell me about a time a friend said they were fine but you thought they weren't. What did you do?",
        ],
    },
    cid(7): {
        "criterion_statement": "The student attends to multiple group members during shared work, checks in directly when signals are unclear, and adjusts their own actions to match what the other has said they need.",
        "criterion_label": "[Band C] Social Awareness & Empathy (dispositional observation)",
        "observation_indicators": [
            "The student attends to multiple members of a working group (not only the loudest or closest), tracking who is engaged, who is withdrawing, who is confused.",
            "The student checks in with a direct question when signals are unclear, rather than acting on assumption.",
            "The student adjusts their own actions to match what the other person has said they need, on multiple occasions.",
            "The student attends to what a peer is doing (withdrawn posture, silence, not participating) as well as to what they say, when reading emotional state.",
        ],
        "confusable_behaviours": [
            "Centring the most expressive peer (attending well to the person who says the most) mistaken for broad social awareness. Distinction: the disposition shows in attention to the quieter group members too.",
            "Checking-in-then-doing-what-I-was-going-to-do (ritual check-in followed by the student's own plan anyway) mistaken for responsive empathy. Distinction: the action actually shifts based on the answer.",
        ],
        "absence_indicators": [
            "In group work, the student consistently over-indexes on one or two peers and loses track of the others, without noticing the pattern.",
            "The student asks questions but proceeds without adjusting behaviour to the responses, indicating the asking is ritualised.",
        ],
        "conversation_prompts": [
            "When do you find it easiest to tell what a group member is feeling, and when do you find it hardest?",
            "Tell me about a time you adjusted what you were doing because of what someone else needed — what shifted?",
            "How do you know when someone in your group is fading out without saying so?",
        ],
    },
    cid(8): {
        "criterion_statement": "After a conflict, the student listens without interrupting, names their own contribution to the situation, and proposes a next step that accounts for the other person's position as well as their own.",
        "criterion_label": "[Band D] Social Awareness & Empathy (dispositional observation)",
        "observation_indicators": [
            "After a conflict, the student listens to the other party without interrupting, even when they disagree.",
            "The student names their own contribution to the conflict (what they did, said, or assumed) without only narrating the other person's faults.",
            "The student proposes a next step that accounts for the other person's position — not only a resolution that protects their own.",
            "The student treats repair as part of the relationship, not as an admission of being wholly at fault.",
        ],
        "confusable_behaviours": [
            "Apology performance (\"I said sorry\") mistaken for repair. Distinction: repair includes listening, naming contribution, and proposing change; apology without those elements is conflict-closure, not repair.",
            "Self-blame as a way to end the conflict quickly, mistaken for accountability. Distinction: repair names a specific contribution; self-blame flattens into \"it was all my fault so let's move on\".",
        ],
        "absence_indicators": [
            "After a conflict, the student's account consistently places the cause entirely on the other party, with no observable noticing of their own role.",
            "The student avoids conflict rather than repair, absenting themselves from a peer or context until the situation is forgotten.",
        ],
        "conversation_prompts": [
            "Tell me about a time you and a friend disagreed and then repaired it — what was the hardest part?",
            "When has it been easiest to own your part in a conflict, and when has it felt hardest?",
            "What do you notice about how you react right after a disagreement — what's the move you want to practise?",
        ],
    },

    # ============= LT 3.2 Self-Care & Resilience =============
    cid(37): {
        "criterion_statement": "The student names a specific trusted adult they could go to for help and carries out a simple self-care routine with supportive reminders, across most occasions when it is needed.",
        "criterion_label": "[Band A] Self-Care & Resilience (dispositional observation)",
        "observation_indicators": [
            "The student names a specific trusted adult (parent, class teacher, school counsellor) they could go to for help, unprompted.",
            "The student carries out a simple self-care routine (handwashing, toothbrushing, water, rest) with supportive reminders, on most occasions it is needed.",
            "The student asks for help from a trusted adult in small everyday matters, not only in big or visible distress moments.",
        ],
        "confusable_behaviours": [
            "Help-seeking only at crisis (waiting for visible distress before asking) mistaken for healthy help-seeking. Distinction: the disposition is help-seeking as an ordinary skill, not an emergency reach.",
            "Tattling (seeking adult intervention against a peer) mistaken for trusted-adult relationship. Distinction: help-seeking here is for the student's own wellbeing, not adjudication of peer disputes.",
        ],
        "absence_indicators": [
            "The student waits for visible physical distress (fever, tears, injury) before asking for help, indicating help-seeking is not yet a normal skill.",
            "The student does not have a consistent specific trusted adult named outside their immediate family, over weeks of classroom life.",
        ],
        "conversation_prompts": [
            "Who is a grown-up at school you can ask for help when you need it? Tell me about a time you did.",
            "Tell me about what happens when you feel not-quite-right — what do you do?",
            "Tell me about a time you asked for help and it made something better.",
        ],
    },
    cid(38): {
        "criterion_statement": "The student names a bodily early-warning sign in themselves and selects a practised self-care response before activation escalates, across multiple occasions.",
        "criterion_label": "[Band B] Self-Care & Resilience (dispositional observation)",
        "observation_indicators": [
            "The student names a bodily early-warning sign in themselves (tiredness, irritability, headache, tight chest) in their own words.",
            "The student selects a practised self-care response (water, short break, movement, feeling-naming, calm corner) before activation fully escalates, across multiple occasions.",
            "The student signals to an adult when they have noticed an early sign they do not yet have a response for, rather than waiting for the sign to become unmanageable.",
        ],
        "confusable_behaviours": [
            "After-the-fact narration (\"I was tired so I got grumpy\") mistaken for early self-care. Distinction: the disposition is pre-escalation noticing and response, not retrospective explanation.",
            "Generic tiredness reporting (saying \"I'm tired\" as a regular refrain without changed behaviour) mistaken for signal-responsive care. Distinction: the noticing is followed by an action calibrated to what the student noticed.",
        ],
        "absence_indicators": [
            "Escalation episodes (tears, snapping at a peer, withdrawal) recur weekly with no observable pre-escalation pause or response.",
            "The student can name signals in abstract (lessons on the body) but does not apply the vocabulary to their own in-the-moment state.",
        ],
        "conversation_prompts": [
            "What are the first signs in your body that tell you something's building up?",
            "Tell me about a time you caught a feeling early this month — what did you do?",
            "When do you notice signs early, and when do they sneak up on you?",
        ],
    },
    cid(39): {
        "criterion_statement": "The student articulates a self-care plan with context-specific strategies for home and school, names multiple trusted people or services for support, and acts on the plan across real situations.",
        "criterion_label": "[Band C] Self-Care & Resilience (dispositional observation)",
        "observation_indicators": [
            "The student articulates — spontaneously or on brief prompt — a self-care plan with context-specific strategies for both home and school.",
            "The student names two or more trusted people or services (counsellor, teacher, parent, nurse, external line) they could turn to for support, with specificity about which for which kind of concern.",
            "The student's plan acknowledges that different contexts (home, school, online) need different strategies, rather than applying one strategy everywhere.",
            "The student follows through on their plan in real situations, not only in reflective conversation.",
        ],
        "confusable_behaviours": [
            "Plan fluency (being able to describe the plan on request) mistaken for enacted self-care. Distinction: observation in real stressful moments should match the plan's claims.",
            "Listing adults from a poster (reciting the help-seeking chain) mistaken for having a genuine trusted adult. Distinction: the disposition shows in specificity — which adult for which concern, not just \"a teacher\".",
        ],
        "absence_indicators": [
            "The student can name strategies and people but the real-situation response shows no deployment of either, over multiple observed occasions.",
            "The student's plan flattens home and school into the same thing, indicating they have not yet grasped that contexts differ.",
        ],
        "conversation_prompts": [
            "Where do you find self-care easiest — at home or at school — and why?",
            "When do you find it easiest to ask someone for help, and when does it feel hardest?",
            "Tell me about a plan you have for when a hard day is starting — does it work?",
        ],
    },
    cid(40): {
        "criterion_statement": "The student sustains key self-care routines through genuinely stressful periods without adult scaffolding, and offers non-directive support to a peer at least occasionally.",
        "criterion_label": "[Band D] Self-Care & Resilience (dispositional observation)",
        "observation_indicators": [
            "The student sustains key self-care routines (sleep protection, movement, exit from pressurising group chat, calm corner, food and water) through a genuinely stressful period — assessment window, social friction, demanding project — without adult scaffolding.",
            "The student's self-care pattern under pressure holds consistently with their self-care pattern in calm periods, rather than collapsing when it is most needed.",
            "The student offers a peer a specific non-directive form of support (sitting alongside, asking what they need, gentle checking in) on at least one observed occasion.",
            "The student seeks help when they recognise their own strategies are insufficient, rather than persisting alone past the point they can manage.",
        ],
        "confusable_behaviours": [
            "Performed resilience (\"I'm fine\") under visible strain mistaken for sustained self-care. Distinction: the disposition is observable practice continuing — not the absence of complaint.",
            "Directive peer help (\"you should try X\") mistaken for non-directive support. Distinction: non-directive support asks what the peer needs, does not prescribe.",
        ],
        "absence_indicators": [
            "Self-care routines collapse first in pressure weeks (sleep drops, exercise stops, food becomes irregular) even though the student has the capability in calm weeks.",
            "Under pressure, the student takes on peer support in a way that overextends them (the \"helper\" role as a way to avoid their own self-care).",
        ],
        "conversation_prompts": [
            "Which parts of your self-care hold up under pressure, and which fall off first?",
            "Tell me about a time this term you helped a friend who was struggling — how did you decide what to do?",
            "What does 'looking after yourself' actually mean for you right now?",
        ],
    },

    # ============= LT 5.2 Community Engagement & Purpose =============
    cid(72): {
        "criterion_statement": "The student carries out their classroom job without needing reminders on most occasions, and articulates how that job helps the class function.",
        "criterion_label": "[Band A] Community Engagement & Purpose (dispositional observation)",
        "observation_indicators": [
            "The student carries out their classroom job (monitor, tidying, door-holder, register-helper) on most occasions without adult reminders.",
            "The student articulates — when asked or spontaneously — how their job contributes to the class running, not only that they are doing it.",
            "The student takes small uninvited initiative (picking something up, setting out a chair) that helps the class function, beyond only their named job.",
        ],
        "confusable_behaviours": [
            "Compliance with the job rota (doing it because told to) mistaken for community participation. Distinction: the disposition shows in the student's own account of why it matters, not only task completion.",
            "Showing off the job to earn adult praise, mistaken for genuine contribution. Distinction: the contribution continues when the adult is not watching.",
        ],
        "absence_indicators": [
            "The student needs repeated reminders to do their class job week after week, and shows no shift toward initiating.",
            "The student reports the job as \"what I have to do\" rather than \"what helps our class\".",
        ],
        "conversation_prompts": [
            "Tell me about your classroom job — what does it do for our class?",
            "Tell me about a time you helped even though no-one asked — what made you do it?",
            "What's something you do every week that makes our class work better?",
        ],
    },
    cid(73): {
        "criterion_statement": "The student spontaneously includes peers who appear left out, across multiple occasions and varied group contexts, treating belonging as something the group actively creates.",
        "criterion_label": "[Band B] Community Engagement & Purpose (dispositional observation)",
        "observation_indicators": [
            "The student spontaneously includes a peer who appears left out (sitting alone, not being chosen, quieter than usual, declining to join), across multiple occasions in varied group contexts.",
            "The student invites in peers outside their usual friendship group, not only their closest friends.",
            "The student notices when a new or returning student is still at the edge of the group and does something active to bring them in.",
        ],
        "confusable_behaviours": [
            "Being chosen as \"kind one\" by adults (rotating the left-out peer to pair with the compliant \"kind\" student) mistaken for authentic inclusion. Distinction: the disposition shows in self-initiated inclusion, not in adult-assigned pairings.",
            "One-off inclusion gesture (inviting once, then not sustaining) mistaken for active belonging-building. Distinction: the disposition is a pattern across weeks, not a single act.",
        ],
        "absence_indicators": [
            "The student consistently stays within closest friendship group, with no observable noticing of peers outside it.",
            "When a peer appears left out, the student continues own activity without pause, even when the signal is visible.",
        ],
        "conversation_prompts": [
            "Tell me about a time you helped someone feel included — what did you do?",
            "How do you notice when someone is on the edge of the group?",
            "Tell me about a friend you've made this year who wasn't already in your group — how did it start?",
        ],
    },
    cid(74): {
        "criterion_statement": "Across a D2R project cycle, the student identifies a real school need unprompted, contributes substantively to a team proposal, and follows through on their share of the work to completion.",
        "criterion_label": "[Band C] Community Engagement & Purpose (dispositional observation)",
        "observation_indicators": [
            "Across at least one D2R (discover-to-refine) project cycle, the student identifies a real school need unprompted, rather than only responding to an adult's suggested project.",
            "The student contributes substantively to a team proposal — shaping the idea, not only supplying effort.",
            "The student follows through on their share of the work to project completion, not only at the planning phase.",
            "The student is visible in the doing as well as in the proposing, across the arc of a project.",
        ],
        "confusable_behaviours": [
            "Enthusiastic project-start without follow-through mistaken for community-building disposition. Distinction: the disposition is the arc — notice, propose, do — not only the sparkle at the start.",
            "Leading all aspects of the project at the cost of teammates' contribution mistaken for initiative. Distinction: the disposition is shown in shared contribution, not dominance.",
        ],
        "absence_indicators": [
            "The student contributes ideas at planning meetings but drops off in the execution phase, across multiple projects.",
            "The student participates only when the project is initiated by an adult or assigned by a teacher.",
        ],
        "conversation_prompts": [
            "What do you notice our school needs that people aren't already working on?",
            "When do you find it easiest to follow through on a project to the end, and when do you lose momentum?",
            "Tell me about a project that didn't go as planned — what did you learn about contributing?",
        ],
    },
    cid(75): {
        "criterion_statement": "Through a Light Dragon capstone or extended D2R work, the student collaborates substantively across difference, engages with evidence of whether the work made a difference, and articulates why the work matters to them personally.",
        "criterion_label": "[Band D] Community Engagement & Purpose (dispositional observation)",
        "observation_indicators": [
            "Through a Light Dragon capstone or extended D2R project, the student collaborates substantively with team members different from themselves (background, language, perspective, skill-set).",
            "The student engages with evidence of whether the project made a difference (collecting signal, welcoming disconfirming evidence, not only celebrating effort).",
            "The student articulates — in Reflection 360 or unprompted conversation — why the work matters to them personally, with specificity about the connection to who they are becoming.",
            "The student treats difference within the team as strengthening the work, not as friction to avoid.",
        ],
        "confusable_behaviours": [
            "Project-impact rhetoric (describing outcomes without evidence) mistaken for genuine engagement with whether the work made a difference. Distinction: the disposition is visible in the student's willingness to look at uncomfortable signals.",
            "Collaborating with similar peers by default mistaken for cross-difference collaboration. Distinction: look for real-difference teaming (background, skill, perspective) not just multi-person teaming.",
        ],
        "absence_indicators": [
            "The student's project reflection focuses on effort and process without engagement with impact signal, across multiple projects.",
            "The student gravitates consistently to same-profile teammates even when mixed-team options are available.",
        ],
        "conversation_prompts": [
            "How has working with this team changed what you think you can do together?",
            "What's the evidence you have that your project actually made a difference?",
            "Where does this work connect to who you're becoming — and where is the connection still fuzzy?",
        ],
    },

    # ============= LT 7.2 Self-Direction in Practice =============
    cid(104): {
        "criterion_statement": "When a first attempt does not work, the student tries a different approach without needing to be told, and names what happened rather than dismissing it.",
        "criterion_label": "[Band A] Self-Direction in Practice (dispositional observation)",
        "observation_indicators": [
            "The student stops and tries a different approach when a first attempt does not work, without needing to be told, on most occasions of minor setback.",
            "Across more than one type of task (reading, making, movement, social), the student shows the same \"try differently\" response rather than only in one domain.",
            "After a setback, the student names what happened (\"I got stuck\", \"that didn't work because…\") rather than dismissing it (\"I'm rubbish at this\", \"it's boring anyway\").",
            "The student asks for help once they have tried differently and still need support, not as the first move.",
        ],
        "confusable_behaviours": [
            "Trying-again as repetition (the same attempt, again) mistaken for trying differently. Distinction: the disposition is a shift in the approach, not only in the effort.",
            "Dismissal framed as humour (\"I'm so bad at this lol\") mistaken for light-heartedness. Distinction: the disposition shows the student stays with the difficulty rather than exiting it.",
        ],
        "absence_indicators": [
            "The student exits the task (\"I'm rubbish at this\" / \"this is boring\") on first setback across weeks, without the \"try differently\" move appearing.",
            "The student requires adult prompt to try differently every time, with no internalisation visible across the term.",
        ],
        "conversation_prompts": [
            "Tell me about a time something didn't work the first time and you tried it a different way. What did you try?",
            "When you're stuck, what do you usually do first?",
            "Tell me about a time a setback was actually helpful — what happened?",
        ],
    },
    cid(105): {
        "criterion_statement": "The student refers back to strategies they have previously found helpful in similar situations without prompt, and volunteers specific observations about their own working rather than general evaluations of the task.",
        "criterion_label": "[Band B] Self-Direction in Practice (dispositional observation)",
        "observation_indicators": [
            "The student refers back to a strategy previously found helpful in a similar type of situation, without being prompted (\"Last time I did X, so I'll try it again\").",
            "After a task, the student volunteers one specific observation about how they worked (\"I noticed I kept getting distracted\", \"it helped when I …\"), rather than a general evaluation of the task (\"it was fun / hard\").",
            "The student notices when they have used a known-helpful strategy and when they have forgotten to, and can name the difference.",
        ],
        "confusable_behaviours": [
            "General task evaluation (\"it was hard / boring / fun\") mistaken for self-observation. Distinction: the disposition is about the student's own working, not about the task's quality.",
            "Repeating a strategy because it's the one the class was taught, mistaken for self-directed reuse. Distinction: look for the student's own referring-back language, not lesson-recall.",
        ],
        "absence_indicators": [
            "The student's post-task reflections stay at the level of task-judgement (\"this was easy\", \"this was boring\") over weeks, with no observations about the student's own working surfacing.",
            "The student re-encounters familiar difficulties without re-applying strategies that have previously worked for them.",
        ],
        "conversation_prompts": [
            "What's a strategy you keep coming back to across different tasks? How did you figure out it was yours?",
            "When do you find it easiest to remember a strategy you already know works, and when do you forget?",
            "Tell me about a specific thing you noticed about how you worked this week.",
        ],
    },
    cid(106): {
        "criterion_statement": "The student identifies patterns in their own responses across situations and names them spontaneously, adjusting approach mid-task when something is not working, without teacher prompt.",
        "criterion_label": "[Band C] Self-Direction in Practice (dispositional observation)",
        "observation_indicators": [
            "The student identifies a pattern in how they respond across more than one situation and names it spontaneously (\"I always do this when the work gets harder\"), on multiple occasions across a term.",
            "The student adjusts their approach mid-task in response to noticing that something is not working, without teacher prompt — not only in post-task reflection.",
            "The student's self-observations move from single-domain (\"in maths\") to cross-domain (\"in maths and in music and in chat with my friend\") within the term.",
        ],
        "confusable_behaviours": [
            "Post-hoc pattern-narration (explaining a pattern after the term is over) mistaken for in-the-moment pattern-recognition. Distinction: the disposition is the student catching themselves while the situation is live.",
            "Performance of pattern-language (\"I always do X\") as classroom currency, with no behavioural adjustment to match. Distinction: the evidence is in the mid-task adjustment, not in the talk.",
        ],
        "absence_indicators": [
            "The student can reflect on patterns when prompted in reflection lessons but shows no in-the-moment course correction across weeks of observed work.",
            "The student's pattern language stays tightly scoped to one domain (e.g. only maths), not generalising across contexts.",
        ],
        "conversation_prompts": [
            "What's a pattern in yourself you've caught this term? When did you catch it?",
            "Where do you find it easiest to notice a pattern in real time, and where does it still only land afterwards?",
            "Tell me about a time you changed tack in the middle of something — what made you notice?",
        ],
    },
    cid(107): {
        "criterion_statement": "The student articulates specific adjustments they have made to their thinking or behaviour and describes their effect across more than one domain, applying self-awareness strategies in novel situations without prompt and making unprompted connections between wellbeing learning and other contexts.",
        "criterion_label": "[Band D] Self-Direction in Practice (dispositional observation)",
        "observation_indicators": [
            "The student articulates a specific adjustment they have made to their thinking or behaviour and describes its effect across more than one domain (homework and music, sport and social), without prompting.",
            "In novel or challenging situations, the student applies a self-awareness strategy (the pause, naming, body-signal check-in) without adult prompt.",
            "The student makes connections between wellbeing learning and behaviour in other contexts (academic, social, personal) unprompted, on multiple occasions.",
            "The student treats self-observation as an ongoing stance, not a completed assignment.",
        ],
        "confusable_behaviours": [
            "Articulate reflection without corresponding behaviour change mistaken for dispositional self-direction. Distinction: the disposition shows in cross-domain behavioural shift, not only in fluent reflection.",
            "Technique application in school settings only (uses the pause in class but not in home-context reports) mistaken for dispositional stance. Distinction: the stance carries across observer-free contexts.",
        ],
        "absence_indicators": [
            "The student's reflections are fluent but adjustments stay siloed to one domain, with no cross-domain pickup reported over a term.",
            "In a genuinely novel challenge, the student reverts to pre-strategy reactivity despite being capable of articulating the strategy when asked.",
        ],
        "conversation_prompts": [
            "Where does self-direction feel most like 'just how you are' now, and where does it still feel like a technique you're applying?",
            "Tell me about an adjustment you made in one domain that rippled into another — how did that happen?",
            "What's the stance you're taking toward yourself this year — is it different from last year?",
        ],
    },
}


# ---------------------------------------------------------------------------
# Content for NEW T3 Bands E–F for LT 1.1, 1.2, 3.2, 5.2, 7.2
# ---------------------------------------------------------------------------
# Cross-LT references used:
#   LT 6.1 E = crit_0124, LT 6.1 F = crit_0125
#   LT 3.1 E = crit_0112, LT 3.1 F = crit_0113
#   LT 5.1 E = crit_0118, LT 5.1 F = crit_0119
#   LT 7.1 E = crit_0122, LT 7.1 F = crit_0123

def make_t3_new(criterion_id, lt_id, band, criterion_statement, criterion_label,
                observation_indicators, confusable_behaviours, absence_indicators,
                conversation_prompts, source_kud_item_ids,
                decomposition_rationale, prerequisite_criterion_ids,
                prerequisite_edges_detail):
    return {
        "criterion_id": criterion_id,
        "associated_lt_ids": [lt_id],
        "band": band,
        "band_label": BAND_LABELS[band],
        "lt_type": "Type 3",
        "strand": "single_strand",
        "criterion_statement": criterion_statement,
        "criterion_label": criterion_label,
        "source_kud_item_ids": source_kud_item_ids,
        "observation_indicators": observation_indicators,
        "confusable_behaviours": confusable_behaviours,
        "absence_indicators": absence_indicators,
        "conversation_prompts": conversation_prompts,
        "decomposition_rationale": decomposition_rationale,
        "prerequisite_criterion_ids": prerequisite_criterion_ids,
        "prerequisite_edges_detail": prerequisite_edges_detail,
        "schema_version": "v2",
    }


def edges(target, sources_with_types):
    return [{"from": s, "to": target, "edge_type": t} for s, t in sources_with_types]


NEW_ENTRIES = []

# ----- LT 1.1 Band E (crit_0142) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(142), lt_id="lt_1_1", band="E",
    criterion_statement="The student sustains regulation practices through extended pressure periods without adult scaffolding and comments unprompted on how their own state is affecting the group or a specific peer.",
    criterion_label="[Band E] Self-Awareness & Regulation (dispositional observation)",
    observation_indicators=[
        "The student sustains regulation practices through extended pressure periods (assessment windows, significant personal difficulty, intense group project) without adult scaffolding.",
        "The student comments unprompted on how their own state is affecting the group or a specific peer, not only on their own feelings.",
        "The student's regulation practice holds consistently across observed and observer-free contexts (home, peer group, online) over a term.",
        "The student takes small proactive steps (sleep protection, withdrawal from pressurising interaction, rest scheduling) in anticipation of known stressors, not only in response.",
    ],
    confusable_behaviours=[
        "Performed stoicism (\"I'm fine\") under visible strain mistaken for sustained regulation. Distinction: the disposition is visible in continuing practice — not in the absence of complaint.",
        "Regulating-for-the-group (suppressing own state to keep the group calm) mistaken for group-aware regulation. Distinction: the disposition includes acknowledgement of own state, not its concealment for others' benefit.",
    ],
    absence_indicators=[
        "Regulation practices visibly fray in pressure weeks across multiple markers (sleep, mood, output), with no adjustment or help-seeking.",
        "The student acts as though their state is private and has no effect on the group, even when peer reports show the contrary.",
    ],
    conversation_prompts=[
        "How has your regulation held up through this year's hardest patches — where did it hold, where did it fray?",
        "When have you noticed your own state shaping the group's — and what did you do?",
        "How has what 'looking after yourself' means changed for you between last year and now?",
    ],
    source_kud_item_ids=["kud_lt_1_1_E_01"],
    decomposition_rationale="Single Band E criterion — the dispositional capability at this band integrates sustained regulation across pressure periods with awareness of one's own state as shaping the group; both are present or absent together.",
    prerequisite_criterion_ids=[cid(4), cid(124)],
    prerequisite_edges_detail=edges(cid(142), [(cid(4), "within_lt_band"), (cid(124), "cross_lt_source_stated")]),
))

# ----- LT 1.1 Band F (crit_0143) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(143), lt_id="lt_1_1", band="F",
    criterion_statement="The student articulates a personal regulation system grounded in specific practice and supports a peer or younger student in developing their own, without adult direction.",
    criterion_label="[Band F] Self-Awareness & Regulation (dispositional observation)",
    observation_indicators=[
        "The student articulates — in Reflection 360 or spontaneous reflection — their personal regulation system: non-negotiables, early-warning signals, known disruptors, adaptations built over years.",
        "The student supports a peer or younger student in developing their own regulation, without adult direction, using questions more than prescription.",
        "The student's regulation language is authored (their own), not imported from the programme vocabulary, and is recognisably coherent across contexts.",
        "The student maintains regulation practices when no adult is tracking, in consequential life contexts (applications, work, significant relationships).",
    ],
    confusable_behaviours=[
        "Articulate vocabulary about regulation (\"my nervous system\", \"my HPA axis\") mistaken for authored system. Distinction: an authored system has specific content — the student's own non-negotiables, their own known disruptors — not only rehearsed neuroscience.",
        "Directive peer advice (\"you should try box breathing\") mistaken for supporting others' development. Distinction: support here is non-directive and centred on the peer's own discovery.",
    ],
    absence_indicators=[
        "The student can describe regulation neuroscience fluently but cannot specify their own system's particulars.",
        "The student's peer-support mode is advice-giving, not inquiry-led, even after practice.",
    ],
    conversation_prompts=[
        "Walk me through your regulation system — the bits that are non-negotiable, the bits that are still in progress.",
        "How has supporting other people's regulation changed yours?",
        "What in your regulation system are you planning to carry into life after school, and what do you expect will need to shift?",
    ],
    source_kud_item_ids=["kud_lt_1_1_F_01"],
    decomposition_rationale="Single Band F criterion — authored regulation system and non-directive support of peers in developing theirs are the two faces of a mature regulation disposition; the KUD treats them as a single observational cell.",
    prerequisite_criterion_ids=[cid(142), cid(125)],
    prerequisite_edges_detail=edges(cid(143), [(cid(142), "within_lt_band"), (cid(125), "cross_lt_source_stated")]),
))

# ----- LT 1.2 Band E (crit_0144) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(144), lt_id="lt_1_2", band="E",
    criterion_statement="The student facilitates repair in group conflict, naming a group dynamic that contributed to the conflict, and proposes steps that address the needs of multiple parties rather than only defending one position.",
    criterion_label="[Band E] Social Awareness & Empathy (dispositional observation)",
    observation_indicators=[
        "The student facilitates repair in group conflict (not only one-on-one), holding space for multiple perspectives, rather than only advocating for their own.",
        "The student names a group dynamic (in-group/out-group, airtime imbalance, historical friction between two members) that contributed to the conflict.",
        "The student proposes steps that address the needs of multiple parties rather than only defending one position — including parties with less social power in the group.",
        "The student tracks the repair over time, not only in the moment of the first conversation.",
    ],
    confusable_behaviours=[
        "\"Mediator\" role as performance (appearing to facilitate while steering toward own position) mistaken for genuine facilitation. Distinction: the disposition shows in the quality of airtime other parties get, not only in the mediator's language.",
        "Naming group dynamics in analytical terms (\"this is pluralistic ignorance\") mistaken for empathic facilitation. Distinction: the disposition is about what it does for the parties, not about correctly labelling the phenomenon.",
    ],
    absence_indicators=[
        "In group conflict, the student consistently ends up advocating for the position closest to their own, without noticing this pattern.",
        "The student's facilitation breaks down when power dynamics surface (older peer, higher-status peer, conflict with a teacher).",
    ],
    conversation_prompts=[
        "When a group conflict shows up, where does your instinct take you — advocate, facilitate, withdraw — and why?",
        "Tell me about a repair you helped with where power dynamics were in play. How did you notice?",
        "How has the way you hold conflict in groups changed through this year?",
    ],
    source_kud_item_ids=["kud_lt_1_2_E_01"],
    decomposition_rationale="Single Band E criterion — group-context repair and naming group dynamics are inseparable at this band in the KUD.",
    prerequisite_criterion_ids=[cid(8), cid(124)],
    prerequisite_edges_detail=edges(cid(144), [(cid(8), "within_lt_band"), (cid(124), "cross_lt_source_stated")]),
))

# ----- LT 1.2 Band F (crit_0145) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(145), lt_id="lt_1_2", band="F",
    criterion_statement="The student recognises when structural or systemic factors are shaping someone's experience, adjusts their response accordingly, and — where appropriate — advocates for change beyond the individual interaction while respecting the affected person's agency.",
    criterion_label="[Band F] Social Awareness & Empathy (dispositional observation)",
    observation_indicators=[
        "The student recognises when structural or systemic factors (cultural context, institutional policy, economic circumstance, group history) are shaping someone's experience, and adjusts their response accordingly.",
        "The student advocates, where appropriate, for change beyond the individual interaction (raising a concern in a group context, proposing a practice change, questioning an assumption) — without taking over someone else's voice.",
        "The student distinguishes performative structural empathy (the language of advocacy, without the relational work) from substantive structural empathy (naming the dynamic and doing the work the situation calls for).",
        "The student's advocacy respects the agency of the person affected, checking rather than speaking-for.",
    ],
    confusable_behaviours=[
        "Performative advocacy language (\"the system is oppressive\") without corresponding relational care mistaken for structural empathy. Distinction: the disposition is shown in both the naming and the ongoing relationship.",
        "Speaking-for (advocating on behalf of someone without checking with them) mistaken for empathic advocacy. Distinction: the disposition centres the affected person's own voice and permission.",
    ],
    absence_indicators=[
        "The student analyses structure fluently in class but does not adjust in-person behaviour across contexts where the structural factor is operating.",
        "The student's advocacy appears on high-visibility occasions (public assemblies, social media) but not in lower-visibility moments where it would matter to the affected peer.",
    ],
    conversation_prompts=[
        "When have you noticed a structural factor shaping a friend's experience in a way that changed what you did?",
        "Where does advocacy feel like the right response, and where does it feel like it would take over?",
        "How do you tell the difference between empathy that respects someone's agency and empathy that speaks over them?",
    ],
    source_kud_item_ids=["kud_lt_1_2_F_01"],
    decomposition_rationale="Single Band F criterion — structural recognition, calibrated advocacy, and respect for affected-person agency are one integrated move at this band.",
    prerequisite_criterion_ids=[cid(144), cid(125)],
    prerequisite_edges_detail=edges(cid(145), [(cid(144), "within_lt_band"), (cid(125), "cross_lt_source_stated")]),
))

# ----- LT 3.2 Band E (crit_0146) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(146), lt_id="lt_3_2", band="E",
    criterion_statement="The student sustains self-care through extended pressure periods without prompting, seeks help when their own strategies are insufficient with appropriate timing, and participates authentically in peer-group self-care norms.",
    criterion_label="[Band E] Self-Care & Resilience (dispositional observation)",
    observation_indicators=[
        "The student sustains self-care through extended pressure periods (assessment terms, high-commitment projects, personal-life turbulence) without prompting.",
        "The student seeks help when their own strategies are insufficient — neither too early (outsourcing effort) nor too late (after burnout is evident).",
        "The student participates in peer-group self-care norms (group sleep protection, group exit from escalating chat, group check-ins) in a way that registers as authentic rather than performative, across more than one context.",
        "The student's self-care extends to what they refuse, not only what they do (saying no to over-commitment, declining to pile on to a pressured peer).",
    ],
    confusable_behaviours=[
        "Performative wellness participation (joining the meditation group visibly; posting self-care content) mistaken for sustained self-care. Distinction: the disposition shows in what happens when no-one is watching.",
        "Early help-seeking as pattern (asking adults to intervene before attempting own strategies) mistaken for calibrated help-seeking. Distinction: the disposition shows in timing — waiting long enough to have tried, not long enough to have collapsed.",
    ],
    absence_indicators=[
        "The student's self-care collapses first in pressure periods and the collapse is recurrent across terms, without meaningful adjustment.",
        "The student reports wellness practices convincingly but peer and parent observations show them dropping under any strain.",
    ],
    conversation_prompts=[
        "Where are your self-care limits — the places where pressing on stops helping?",
        "Tell me about a time this year when asking for help was the right call, and one when waiting longer was.",
        "Which of your self-care practices feel like yours, and which still feel like school-y rituals?",
    ],
    source_kud_item_ids=["kud_lt_3_2_E_01"],
    decomposition_rationale="Single Band E criterion — sustained practice, calibrated help-seeking, and authentic peer participation are the integrated disposition at this band.",
    prerequisite_criterion_ids=[cid(40), cid(124), cid(112)],
    prerequisite_edges_detail=edges(cid(146), [(cid(40), "within_lt_band"), (cid(124), "cross_lt_source_stated"), (cid(112), "cross_lt_source_stated")]),
))

# ----- LT 3.2 Band F (crit_0147) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(147), lt_id="lt_3_2", band="F",
    criterion_statement="The student articulates a personal resilience framework — non-negotiables, early-warning signals, recovery protocols — developed across years, recognisably authored rather than borrowed, and continuing to develop.",
    criterion_label="[Band F] Self-Care & Resilience (dispositional observation)",
    observation_indicators=[
        "The student articulates — in Reflection 360 or spontaneous reflection — their personal resilience framework: non-negotiable self-care commitments, early-warning signals, recovery protocols.",
        "The student describes how the framework has developed across their school years, with specific references to what changed and why.",
        "The student's framework is recognisably theirs (particular to their life, not a generic version of the programme's language).",
        "The student continues to adjust the framework as circumstances change, rather than holding it as complete.",
    ],
    confusable_behaviours=[
        "Articulate use of the programme's resilience vocabulary, without the specificity of the student's own framework, mistaken for authored resilience. Distinction: the disposition shows in particulars — this student's non-negotiables, this student's warning signs.",
        "Framework-as-performance (presenting a clean resilience story for Reflection 360) mistaken for lived framework. Distinction: the framework should correspond to behaviour in the rest of the week.",
    ],
    absence_indicators=[
        "The student's resilience language borrows entirely from programme materials with no personal specificity visible, even after sustained Reflection 360 work.",
        "The student's framework and the observed week-to-week self-care practice diverge, with the framework being more coherent than the practice.",
    ],
    conversation_prompts=[
        "Walk me through your resilience system — the parts that are settled, the parts still in progress.",
        "What in your framework is unmistakably yours, and what is still the programme's voice?",
        "What's the version of this you expect to need in the first year after school — what will change?",
    ],
    source_kud_item_ids=["kud_lt_3_2_F_01"],
    decomposition_rationale="Single Band F criterion — the framework articulation and its continued development are one integrated identity-level disposition.",
    prerequisite_criterion_ids=[cid(146), cid(125), cid(113)],
    prerequisite_edges_detail=edges(cid(147), [(cid(146), "within_lt_band"), (cid(125), "cross_lt_source_stated"), (cid(113), "cross_lt_source_stated")]),
))

# ----- LT 5.2 Band E (crit_0148) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(148), lt_id="lt_5_2", band="E",
    criterion_statement="The student leads a sustained initiative addressing a genuine need, navigates institutional and relational obstacles as they arise, and articulates both achieved impact and the limits imposed by institutional context.",
    criterion_label="[Band E] Community Engagement & Purpose (dispositional observation)",
    observation_indicators=[
        "The student leads a sustained initiative (beyond a single project cycle) addressing a genuine need, visibly carrying it through setbacks.",
        "The student navigates specific institutional and relational obstacles (approvals, budget, scheduling, friction with a gatekeeper) as they arise, rather than stalling at each one.",
        "The student articulates — in Reflection 360 or unprompted — both the impact of what was achieved and the limits that institutional context imposed.",
        "The student continues contribution to the initiative across terms, even when the visibility fades.",
    ],
    confusable_behaviours=[
        "Initiative-as-performance (highly visible launch, quiet fade after the audience moves on) mistaken for sustained engagement. Distinction: the disposition is shown in continuity after the spotlight.",
        "Over-personalising the institutional obstacles (framing friction as \"they're against me\") mistaken for navigating systems. Distinction: the disposition shows in reading the constraint as system rather than persecution.",
    ],
    absence_indicators=[
        "The student's initiatives are highly visible at launch and drop without follow-through, across multiple projects.",
        "The student gives up at the first institutional obstacle, without attempting alternative routes or sustained negotiation.",
    ],
    conversation_prompts=[
        "Where has sustaining this initiative taken something from you — and where has it given something back?",
        "Tell me about an obstacle you hit this term — what was the institutional lesson in it?",
        "What's the difference, for you, between giving up and knowing when a project has genuinely run its course?",
    ],
    source_kud_item_ids=["kud_lt_5_2_E_01"],
    decomposition_rationale="Single Band E criterion — sustained leadership, institutional navigation, and honest impact-and-limits articulation are inseparable at this band.",
    prerequisite_criterion_ids=[cid(75), cid(124), cid(118)],
    prerequisite_edges_detail=edges(cid(148), [(cid(75), "within_lt_band"), (cid(124), "cross_lt_source_stated"), (cid(118), "cross_lt_source_stated")]),
))

# ----- LT 5.2 Band F (crit_0149) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(149), lt_id="lt_5_2", band="F",
    criterion_statement="The student articulates a clear sense of purpose grounded in specific prior engagement and makes deliberate post-school choices that pursue it, with specificity about which communities and roles and why.",
    criterion_label="[Band F] Community Engagement & Purpose (dispositional observation)",
    observation_indicators=[
        "In Reflection 360 or final-year capstone, the student articulates a clear sense of purpose grounded in specific prior engagement, not only aspirational statement.",
        "The student makes deliberate choices about post-school path, community involvement, or roles, that pursue that purpose — and can say which choices and why.",
        "The student's purpose language is recognisably their own: specific communities, specific roles, specific reasons.",
        "The student holds the purpose as developing rather than fixed, including what would cause it to revise.",
    ],
    confusable_behaviours=[
        "Confident purpose articulation (crisp, polished) without underlying engagement history mistaken for authentic purpose. Distinction: the disposition is grounded in what the student has actually done, not only in what they say.",
        "Purpose borrowed from family expectation or peer consensus mistaken for authored purpose. Distinction: the student can describe the specific moments of engagement that shaped it, not only the outcome.",
    ],
    absence_indicators=[
        "The student's post-school plans do not connect to any specific prior engagement — no through-line from what they have done to what they are choosing.",
        "The student's purpose narrative is glossy when presenting to adults but fragile or absent in informal conversation with peers.",
    ],
    conversation_prompts=[
        "Where did your sense of purpose come from — what concrete experiences shaped it?",
        "Which parts of the community work you did in school are you actually carrying forward, and which are you leaving behind?",
        "What would have to happen to cause your current sense of purpose to shift — and would you welcome or resist that?",
    ],
    source_kud_item_ids=["kud_lt_5_2_F_01"],
    decomposition_rationale="Single Band F criterion — articulated purpose grounded in engagement history and deliberate forward choices form one integrated identity-level disposition.",
    prerequisite_criterion_ids=[cid(148), cid(125), cid(119)],
    prerequisite_edges_detail=edges(cid(149), [(cid(148), "within_lt_band"), (cid(125), "cross_lt_source_stated"), (cid(119), "cross_lt_source_stated")]),
))

# ----- LT 7.2 Band E (crit_0150) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(150), lt_id="lt_7_2", band="E",
    criterion_statement="The student initiates metacognitive reflection without external prompt across sustained periods, facilitates peer self-reflection through open questions rather than advice, and shows stable self-directedness when feedback challenges their self-assessment.",
    criterion_label="[Band E] Self-Direction in Practice (dispositional observation)",
    observation_indicators=[
        "The student initiates metacognitive reflection without external prompt across sustained periods of challenging work — not only at reflection checkpoints.",
        "Working with peers, the student naturally facilitates peer self-reflection through open questions (\"what do you notice?\", \"what might be going on?\"), rather than giving advice or answers.",
        "When feedback challenges the student's self-assessment, the student shows stable self-directedness — neither collapsing into self-criticism nor defending against the feedback.",
        "The student's reflection continues in the unglamorous middle weeks of a term, not only in the opening and closing phases.",
    ],
    confusable_behaviours=[
        "Performative reflection at checkpoints (a polished pause for reflection lessons) mistaken for initiated reflection. Distinction: the disposition is present in the absence of a reflection prompt.",
        "Advice disguised as inquiry (\"what if you … ?\" as a leading question) mistaken for open peer-facilitation. Distinction: the disposition is question-shape plus willingness to accept an answer the student didn't anticipate.",
    ],
    absence_indicators=[
        "Reflection appears only in scheduled checkpoint moments; spontaneous reflection is absent across the observed term.",
        "The student's response to challenging feedback consistently either collapses into self-criticism or hardens into defence, without a stable middle.",
    ],
    conversation_prompts=[
        "When does self-direction happen spontaneously for you, and when does it still require a prompt?",
        "Tell me about a time you helped a peer reflect — how did you keep from giving them an answer?",
        "How has your response to hard feedback shifted across this year?",
    ],
    source_kud_item_ids=["kud_lt_7_2_E_01"],
    decomposition_rationale="Single Band E criterion — initiation of reflection, peer facilitation through questions, and feedback-stable self-directedness are one integrated disposition.",
    prerequisite_criterion_ids=[cid(107), cid(122), cid(124)],
    prerequisite_edges_detail=edges(cid(150), [(cid(107), "within_lt_band"), (cid(122), "cross_lt_source_stated"), (cid(124), "cross_lt_source_stated")]),
))

# ----- LT 7.2 Band F (crit_0151) -----
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(151), lt_id="lt_7_2", band="F",
    criterion_statement="The student demonstrates a stable, articulated metacognitive identity that persists across novel, high-stakes, or unfamiliar contexts without scaffolding, connecting wellbeing learning to who they are becoming with specificity.",
    criterion_label="[Band F] Self-Direction in Practice (dispositional observation)",
    observation_indicators=[
        "The student demonstrates a stable, articulated metacognitive identity — a consistent pattern of how they learn, reflect, and adjust — that they can describe without rehearsing, and that persists across highly novel, high-stakes, or unfamiliar contexts without scaffolding.",
        "The student connects wellbeing learning to their sense of who they are and who they are becoming, unprompted and with specificity (\"I notice I now X where I used to Y\"), across multiple occasions including Reflection 360.",
        "The student's self-direction holds across observed and unobserved settings, including contexts where no school staff are present (work placement, family, significant life events).",
        "The student treats their own learning about themselves as open-ended — still in development at end of school, not complete.",
    ],
    confusable_behaviours=[
        "Rehearsed reflection narrative (a polished growth story for Reflection 360) mistaken for identity-deep self-direction. Distinction: the disposition is shown in spontaneous specificity — \"I notice I now X\" with examples, not a prepared arc.",
        "Self-direction present in school but absent in novel high-stakes contexts (internships, family crises) mistaken for identity-deep disposition. Distinction: the disposition holds outside the school context.",
    ],
    absence_indicators=[
        "The student's reflections rely on programme phrasing rather than their own voice, even after years in the programme.",
        "In high-stakes or unfamiliar contexts, the student reverts to pre-programme patterns of reactivity, without visible carry-over of the metacognitive practice.",
    ],
    conversation_prompts=[
        "Walk me through who you've become as a learner — with examples, not adjectives.",
        "Where does self-direction hold for you in contexts beyond school, and where do you lose it?",
        "What in your metacognitive practice do you expect will need to change in the first year after school?",
    ],
    source_kud_item_ids=["kud_lt_7_2_F_01"],
    decomposition_rationale="Single Band F criterion — identity-level metacognitive practice and its cross-context stability form one integrated disposition.",
    prerequisite_criterion_ids=[cid(150), cid(123), cid(125)],
    prerequisite_edges_detail=edges(cid(151), [(cid(150), "within_lt_band"), (cid(123), "cross_lt_source_stated"), (cid(125), "cross_lt_source_stated")]),
))


# ---------------------------------------------------------------------------
# LT 1.3 T2 entries (Bands A-F) — analytical capability with competency_level_descriptors
# ---------------------------------------------------------------------------
def make_t2_entry(criterion_id, lt_id, band, criterion_statement, criterion_label,
                  source_kud_item_ids, decomposition_rationale,
                  prerequisite_criterion_ids, prerequisite_edges_detail):
    descriptors = {
        "no_evidence": f"The student has not produced work that demonstrates any aspect of this learning target at Band {band}.",
        "emerging": f"The student shows initial engagement with the Band {band} Do statement but requires significant support or prompting.",
        "developing": f"The student demonstrates some but not all components of the Band {band} Do statement consistently.",
        "competent": criterion_statement,
        "extending": f"The student demonstrates the Band {band} Do statement and additionally transfers the capability to an unfamiliar context, teaches or explains it to others, or demonstrates unusual depth beyond the band expectation.",
    }
    return {
        "criterion_id": criterion_id,
        "associated_lt_ids": [lt_id],
        "band": band,
        "band_label": BAND_LABELS[band],
        "lt_type": "Type 2",
        "strand": "single_strand",
        "criterion_statement": criterion_statement,
        "criterion_label": criterion_label,
        "source_kud_item_ids": source_kud_item_ids,
        "competency_level_descriptors": descriptors,
        "decomposition_rationale": decomposition_rationale,
        "prerequisite_criterion_ids": prerequisite_criterion_ids,
        "prerequisite_edges_detail": prerequisite_edges_detail,
        "schema_version": "v2",
    }


# LT 1.3 T2 A (crit_0152)
NEW_ENTRIES.append(make_t2_entry(
    criterion_id=cid(152), lt_id="lt_1_3", band="A",
    criterion_statement="I can name something that is part of my own home or family life that is different from a classmate's, describe it in my own words, and talk about the difference without saying one is better than the other.",
    criterion_label="[Band A] Personal Identity & Cultural Self-Awareness (analytical)",
    source_kud_item_ids=["kud_lt_1_3_A_01"],
    decomposition_rationale="Single Band A criterion — naming a specific home/family difference and framing it non-evaluatively are one integrated Band A capability.",
    prerequisite_criterion_ids=[cid(1)],
    prerequisite_edges_detail=edges(cid(152), [(cid(1), "cross_lt_source_stated")]),
))

# LT 1.3 T2 B (crit_0153)
NEW_ENTRIES.append(make_t2_entry(
    criterion_id=cid(153), lt_id="lt_1_3", band="B",
    criterion_statement="I can describe more than one aspect of my own identity — including at least one cultural aspect — in my own words, and explain that belonging to more than one group at once is a normal part of identity.",
    criterion_label="[Band B] Personal Identity & Cultural Self-Awareness (analytical)",
    source_kud_item_ids=["kud_lt_1_3_B_01"],
    decomposition_rationale="Single Band B criterion — multi-dimensional identity description and the understanding of multiple belonging as normal are one capability at this band.",
    prerequisite_criterion_ids=[cid(152), cid(2)],
    prerequisite_edges_detail=edges(cid(153), [(cid(152), "within_lt_band"), (cid(2), "cross_lt_source_stated")]),
))

# LT 1.3 T2 C (crit_0154)
NEW_ENTRIES.append(make_t2_entry(
    criterion_id=cid(154), lt_id="lt_1_3", band="C",
    criterion_statement="I can describe how my own cultural background shapes how I see and interpret things, identify one way someone with a different background might see the same situation differently, and recognise stereotypes as oversimplifications.",
    criterion_label="[Band C] Personal Identity & Cultural Self-Awareness (analytical)",
    source_kud_item_ids=["kud_lt_1_3_C_01"],
    decomposition_rationale="Single Band C criterion — cultural-lens self-description, perspective-taking, and stereotype recognition form one integrated analytical capability at this band.",
    prerequisite_criterion_ids=[cid(153), cid(3), cid(7)],
    prerequisite_edges_detail=edges(cid(154), [(cid(153), "within_lt_band"), (cid(3), "cross_lt_source_stated"), (cid(7), "cross_lt_source_stated")]),
))

# LT 1.3 T2 D (crit_0155)
NEW_ENTRIES.append(make_t2_entry(
    criterion_id=cid(155), lt_id="lt_1_3", band="D",
    criterion_statement="I can identify at least one group I did not choose to belong to, analyse how that group membership shapes my experience or perspective in a specific situation, and explain how intersecting identities produce experiences that single-dimension analysis misses.",
    criterion_label="[Band D] Personal Identity & Cultural Self-Awareness (analytical)",
    source_kud_item_ids=["kud_lt_1_3_D_01"],
    decomposition_rationale="Single Band D criterion — unchosen-group analysis and intersectional reasoning are the integrated analytical move at this band.",
    prerequisite_criterion_ids=[cid(154), cid(4), cid(8)],
    prerequisite_edges_detail=edges(cid(155), [(cid(154), "within_lt_band"), (cid(4), "cross_lt_source_stated"), (cid(8), "cross_lt_source_stated")]),
))

# LT 1.3 T2 E (crit_0156)
NEW_ENTRIES.append(make_t2_entry(
    criterion_id=cid(156), lt_id="lt_1_3", band="E",
    criterion_statement="I can analyse how my cultural lens might be limiting or distorting my interpretation of a specific text, event, or interaction, and articulate with specificity what I might be missing that a different lens would surface.",
    criterion_label="[Band E] Personal Identity & Cultural Self-Awareness (analytical)",
    source_kud_item_ids=["kud_lt_1_3_E_01"],
    decomposition_rationale="Single Band E criterion — lens-analysis and specific articulation of missed perspective form one integrated capability.",
    prerequisite_criterion_ids=[cid(155), cid(142), cid(144)],
    prerequisite_edges_detail=edges(cid(156), [(cid(155), "within_lt_band"), (cid(142), "cross_lt_source_stated"), (cid(144), "cross_lt_source_stated")]),
))

# LT 1.3 T2 F (crit_0157)
NEW_ENTRIES.append(make_t2_entry(
    criterion_id=cid(157), lt_id="lt_1_3", band="F",
    criterion_statement="I can construct a reasoned analysis of how my identity has been negotiated across different contexts, engage with perspectives that challenge my identity framework without dismissing them or retreating to fixed positions, and acknowledge that my resolution is mine and not a model for others.",
    criterion_label="[Band F] Personal Identity & Cultural Self-Awareness (analytical)",
    source_kud_item_ids=["kud_lt_1_3_F_01"],
    decomposition_rationale="Single Band F criterion — reasoned identity-negotiation analysis, engagement with challenging perspectives, and non-projection of resolution form one integrated analytical capability.",
    prerequisite_criterion_ids=[cid(156), cid(143), cid(145)],
    prerequisite_edges_detail=edges(cid(157), [(cid(156), "within_lt_band"), (cid(143), "cross_lt_source_stated"), (cid(145), "cross_lt_source_stated")]),
))


# ---------------------------------------------------------------------------
# LT 1.3 T3 entries (Bands A-F) — dispositional observation
# ---------------------------------------------------------------------------
LT13_T3_STATEMENT = "The student navigates personal identity and cultural context with growing authenticity and self-awareness in real interactions and contexts."

# LT 1.3 T3 A (crit_0158)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(158), lt_id="lt_1_3", band="A",
    criterion_statement=LT13_T3_STATEMENT,
    criterion_label="[Band A] Personal Identity & Cultural Self-Awareness (dispositional observation)",
    observation_indicators=[
        "The student names, without prompting, at least one thing that is part of their own home or family life that differs from a classmate's.",
        "The student talks about the difference as a difference, without marking it as better or worse.",
        "The student shows curiosity about a classmate's different practice rather than distancing from it.",
    ],
    confusable_behaviours=[
        "Reciting cultural-differences content from class lessons mistaken for self-situated naming. Distinction: the disposition shows in the student's own family / home specifics, not in taught general categories.",
        "Avoiding difference (never volunteering anything about home) mistaken for polite neutrality. Distinction: the disposition includes being visible in the student's particular home life, not hiding it.",
    ],
    absence_indicators=[
        "The student describes family life only in generic terms, with no specific difference surfacing across weeks of class sharing.",
        "When a classmate shares a different practice, the student treats it as strange or funny rather than as a normal difference.",
    ],
    conversation_prompts=[
        "Tell me about something your family does that you love.",
        "Tell me about something at home that might be different from your classmates.",
        "What's something we do in your home that makes us us?",
    ],
    source_kud_item_ids=["kud_lt_1_3_A_01"],
    decomposition_rationale="Single Band A criterion — the disposition at this band is naming own-family specifics non-evaluatively as one integrated move.",
    prerequisite_criterion_ids=[cid(152)],
    prerequisite_edges_detail=edges(cid(158), [(cid(152), "cross_lt_source_stated")]),
))

# LT 1.3 T3 B (crit_0159)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(159), lt_id="lt_1_3", band="B",
    criterion_statement=LT13_T3_STATEMENT,
    criterion_label="[Band B] Personal Identity & Cultural Self-Awareness (dispositional observation)",
    observation_indicators=[
        "The student describes more than one aspect of their own identity (family background, home languages, interests, traditions), including at least one cultural dimension, during class reflection, without prompt.",
        "The student is comfortable holding multiple identities at once (dual-nationality, multilingual, multiple-traditions) rather than presenting one as \"the real one\".",
        "The student treats belonging to more than one group as normal, not as confusion to resolve.",
    ],
    confusable_behaviours=[
        "Choosing one \"best\" identity to present in each context mistaken for navigation. Distinction: the disposition shows in holding multiple at once, not in code-switching to fit.",
        "Passing compliments to the class's most visible cultures while hiding own specifics mistaken for cultural inclusivity. Distinction: the disposition is the student's own multiplicity being visible.",
    ],
    absence_indicators=[
        "The student consistently presents a single identity dimension and performs visible discomfort when another dimension is surfaced.",
        "The student defers to the dominant group identity in the class, with their other identities staying private even in safe reflection contexts.",
    ],
    conversation_prompts=[
        "Tell me about the different groups you belong to — what makes each one yours?",
        "Tell me about a time you were the same you in different places — what was the same, what was different?",
        "When is being part of more than one group easy, and when does it feel like a stretch?",
    ],
    source_kud_item_ids=["kud_lt_1_3_B_01"],
    decomposition_rationale="Single Band B criterion — multi-dimensional identity visibility as an integrated disposition at this band.",
    prerequisite_criterion_ids=[cid(158), cid(153)],
    prerequisite_edges_detail=edges(cid(159), [(cid(158), "within_lt_band"), (cid(153), "cross_lt_source_stated")]),
))

# LT 1.3 T3 C (crit_0160)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(160), lt_id="lt_1_3", band="C",
    criterion_statement=LT13_T3_STATEMENT,
    criterion_label="[Band C] Personal Identity & Cultural Self-Awareness (dispositional observation)",
    observation_indicators=[
        "The student pauses, at least occasionally, to consider how their own background might be influencing their reaction or interpretation before responding in a cross-cultural interaction, without adult prompt.",
        "The student asks rather than assumes when a classmate's reaction is from a different frame (different family practice, different cultural norm).",
        "The student self-corrects in real time when they notice they have interpreted something through their own frame only.",
    ],
    confusable_behaviours=[
        "Saying \"that's just my culture\" as an explanation-without-reflection, mistaken for cultural self-awareness. Distinction: the disposition is visible in the pause before the explanation, not in the phrase itself.",
        "Performing openness to other cultures (fluent cultural-sensitivity language) without changing the student's own interpretive reactions mistaken for genuine self-awareness. Distinction: the evidence is in behaviour change mid-interaction.",
    ],
    absence_indicators=[
        "In cross-cultural interactions, the student consistently interprets the other through their own frame without noticing, even after direct teaching on the concept.",
        "The student defaults to \"that's weird / wrong\" when another cultural practice surfaces, with no pause for their own frame.",
    ],
    conversation_prompts=[
        "When has your cultural background shaped how you saw something — and you noticed it happening?",
        "Where do you find it easiest to notice your own lens, and where is it hardest?",
        "Tell me about a time you were surprised by a classmate's reaction — what did you do with the surprise?",
    ],
    source_kud_item_ids=["kud_lt_1_3_C_01"],
    decomposition_rationale="Single Band C criterion — in-the-moment lens-awareness as an integrated disposition at this band.",
    prerequisite_criterion_ids=[cid(159), cid(154)],
    prerequisite_edges_detail=edges(cid(160), [(cid(159), "within_lt_band"), (cid(154), "cross_lt_source_stated")]),
))

# LT 1.3 T3 D (crit_0161)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(161), lt_id="lt_1_3", band="D",
    criterion_statement=LT13_T3_STATEMENT,
    criterion_label="[Band D] Personal Identity & Cultural Self-Awareness (dispositional observation)",
    observation_indicators=[
        "The student identifies — with genuine reflection, not surface performance — how at least one unchosen group membership (nationality, first language, gender, family configuration, ability) shapes their own experience or perspective in a specific situation.",
        "The student names intersecting identities (what the combination produces that single dimensions do not) when that complexity is actually operating.",
        "The student describes unchosen-group experience without either minimising it or turning it into the whole of who they are.",
    ],
    confusable_behaviours=[
        "Articulating group-membership analysis in class discussion (\"because I'm a [group], I ...\") without specificity about the actual situation, mistaken for reflective identification. Distinction: the disposition is specific-situation-grounded.",
        "Performing intersectional fluency (using the vocabulary) without integration into how the student actually interprets their experience, mistaken for genuine reflection. Distinction: integration is shown in the student's interpretation of their own moments, not in vocabulary deployment.",
    ],
    absence_indicators=[
        "The student's group-membership analysis stays abstract or performative, without specific situations surfacing across reflective conversations.",
        "The student consistently denies that unchosen group membership shapes their experience, even in contexts where it is visibly operating.",
    ],
    conversation_prompts=[
        "Where has an unchosen group membership shaped your experience this year — and how did you notice?",
        "When does thinking about intersecting identities feel useful, and when does it feel forced?",
        "What's something about your experience that only makes sense once you look at more than one dimension at once?",
    ],
    source_kud_item_ids=["kud_lt_1_3_D_01"],
    decomposition_rationale="Single Band D criterion — situation-grounded unchosen-group and intersectional reflection as one integrated disposition.",
    prerequisite_criterion_ids=[cid(160), cid(155)],
    prerequisite_edges_detail=edges(cid(161), [(cid(160), "within_lt_band"), (cid(155), "cross_lt_source_stated")]),
))

# LT 1.3 T3 E (crit_0162)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(162), lt_id="lt_1_3", band="E",
    criterion_statement=LT13_T3_STATEMENT,
    criterion_label="[Band E] Personal Identity & Cultural Self-Awareness (dispositional observation)",
    observation_indicators=[
        "The student voluntarily identifies — in contexts where it is not required — how their cultural background might be limiting or distorting their interpretation of a text, event, or interaction, with specificity.",
        "The student names what they might be missing that a different lens would see, not only \"there are other perspectives\".",
        "The student holds their own lens without defending it as neutral, while also not dismissing it as entirely unreliable.",
    ],
    confusable_behaviours=[
        "Generic acknowledgement of multiple perspectives (\"there are many views\") mistaken for lens-awareness. Distinction: the disposition is specific about what the student's lens is doing, not a generic disclaimer.",
        "Self-deprecating lens-talk (disclaiming the student's own view entirely) mistaken for humility. Distinction: the disposition holds the lens as one view, not as invalid.",
    ],
    absence_indicators=[
        "The student's interpretations of texts, events, and interactions consistently claim view-from-nowhere status, even when challenged.",
        "The student's lens-language appears only when assessed for it, and disappears in informal interpretive work.",
    ],
    conversation_prompts=[
        "Where has your cultural lens shaped an interpretation this year in a way you only saw afterwards?",
        "What's an example of a situation where you now think you missed something a different lens would catch?",
        "How has thinking about your lens changed what you do with your interpretations?",
    ],
    source_kud_item_ids=["kud_lt_1_3_E_01"],
    decomposition_rationale="Single Band E criterion — voluntary lens-naming and specific articulation of potential misses are integrated at this band.",
    prerequisite_criterion_ids=[cid(161), cid(156)],
    prerequisite_edges_detail=edges(cid(162), [(cid(161), "within_lt_band"), (cid(156), "cross_lt_source_stated")]),
))

# LT 1.3 T3 F (crit_0163)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(163), lt_id="lt_1_3", band="F",
    criterion_statement=LT13_T3_STATEMENT,
    criterion_label="[Band F] Personal Identity & Cultural Self-Awareness (dispositional observation)",
    observation_indicators=[
        "The student engages with perspectives that challenge their own identity framework — including uncomfortable ones — without dismissing them.",
        "The student holds their position without retreating to a fixed identity-as-certainty stance.",
        "The student does not project their own resolution process onto peers navigating different questions.",
        "The student treats identity as an active negotiation, with examples of where the student's own position has shifted.",
    ],
    confusable_behaviours=[
        "Confidently articulated identity narrative (polished, stable, well-rehearsed) mistaken for identity integration. Distinction: integration is shown in the student staying in difficult conversations and allowing challenge to land, not only in the polish of the statement.",
        "Prescribing the student's own identity resolution to others (telling a peer \"you need to decide where you stand\") mistaken for mature identity work. Distinction: the disposition respects that others' questions are their own.",
    ],
    absence_indicators=[
        "The student exits identity conversations that challenge their framework, or deflects them with performance of certainty.",
        "The student projects their own resolution onto peers, especially peers from similar backgrounds, pressuring them to adopt the same position.",
    ],
    conversation_prompts=[
        "Tell me about an identity question that's still genuinely open for you — what are you holding?",
        "Where has someone else's identity framework landed in a way that changed yours? Where did you hold ground?",
        "How do you stay in a conversation that challenges who you think you are without collapsing or defending?",
    ],
    source_kud_item_ids=["kud_lt_1_3_F_01"],
    decomposition_rationale="Single Band F criterion — engagement with challenging perspectives, non-retreat, and non-projection onto peers form one integrated identity-level disposition.",
    prerequisite_criterion_ids=[cid(162), cid(157)],
    prerequisite_edges_detail=edges(cid(163), [(cid(162), "within_lt_band"), (cid(157), "cross_lt_source_stated")]),
))


# ---------------------------------------------------------------------------
# LT 8.3 T3 entries (Bands A-F)
# Cross-LT prerequisites per spec:
#   LT 1.1 same-band hard prereq across all bands
#   LT 5.1 same-band hard prereq from Band B onward
#   LT 8.2 same-band conceptual accelerator from Band C onward
#
# LT 5.1 T2 IDs: A=[60,61,62], B=[63,64,65], C=[66,67,68], D=[69,70,71], E=[118], F=[119]
# LT 8.2 T2 IDs: C=138, D=139, E=140, F=141
# ---------------------------------------------------------------------------

LT83_BASE_STATEMENT = "The student sustains assertive, wellbeing-supporting digital practices across platforms and contexts over time, as an enacted disposition rather than a single performance."

# LT 8.3 T3 A (crit_0164)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(164), lt_id="lt_8_3", band="A",
    criterion_statement=LT83_BASE_STATEMENT,
    criterion_label="[Band A] Digital Assertiveness & Wellbeing Strategies (dispositional observation)",
    observation_indicators=[
        "The child stops using a digital device when a trusted adult asks, without significant distress, on most occasions. (Parental observation is primary at this band; teacher observation supplements.)",
        "The child tells a trusted adult when they see or are shown something online that makes them feel confused, scared, or uncomfortable, on more than one observed occasion.",
        "The child does not share personal information (name, address, school, family details) with strangers in digital contexts. (Safeguarding observation — failure here triggers safeguarding pathway, not assessment.)",
        "The child reports something confusing online rather than hiding it, without treating the report as getting anyone in trouble.",
    ],
    confusable_behaviours=[
        "Device-stopping only when parental tone is angry mistaken for responsive practice. Distinction: the disposition is shown when the adult asks in an ordinary tone, not only under pressure.",
        "Reporting \"fine\" to every adult asking about online activity mistaken for safe online practice. Distinction: the disposition includes the child volunteering something was confusing, not only responding to questions with reassurance.",
    ],
    absence_indicators=[
        "The child shows significant distress or resistance when asked to stop using a device, consistently across weeks.",
        "The child does not mention online experiences that were confusing or upsetting, even in contexts designed to invite sharing (bedtime chat, reflection at home).",
    ],
    conversation_prompts=[
        "Tell me about a time something on a screen made you feel worried — what did you do? (Ask the parent too.)",
        "Tell me about a grown-up you can tell when something online doesn't feel right.",
        "When you're asked to stop using a device, what's it like inside?",
    ],
    source_kud_item_ids=["kud_lt_8_3_A_01"],
    decomposition_rationale="Single Band A criterion — at this band, parent-observation-primary indicators of safe, adult-connected digital practice are one integrated observational cell. Safeguarding indicator separated from assessment pathway per KUD.",
    prerequisite_criterion_ids=[cid(1)],
    prerequisite_edges_detail=edges(cid(164), [(cid(1), "cross_lt_source_stated")]),
))

# LT 8.3 T3 B (crit_0165)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(165), lt_id="lt_8_3", band="B",
    criterion_statement=LT83_BASE_STATEMENT,
    criterion_label="[Band B] Digital Assertiveness & Wellbeing Strategies (dispositional observation)",
    observation_indicators=[
        "The child exits digital content they recognise as unkind, distressing, or inappropriate, without needing an adult to direct them, on most observed occasions. (Parental observation remains primary.)",
        "The child uses simple assertive language in digital communication (\"I don't want to\", \"please stop\", \"I'm going to tell an adult\") when a peer behaves unkindly online.",
        "The child keeps to family or school rules about device use (time, place, content) without constant reminders.",
        "The child brings the assertive moves they use face-to-face (saying no, walking away, telling someone) into digital contexts when the same situation arises.",
    ],
    confusable_behaviours=[
        "Rule-following only when being watched mistaken for self-directed digital practice. Distinction: the disposition shows in unsupervised moments as reported by parents.",
        "Exiting content the adult disapproves of, while continuing to engage with content that is also unkind but less visible to adults, mistaken for discernment. Distinction: the disposition is child-led exit based on what feels wrong to them, not adult-curated exit.",
    ],
    absence_indicators=[
        "The child needs constant reminders to follow device-use rules, and the pattern does not shift across the year.",
        "The child stays in group-chat or game interactions that are visibly unkind, without using assertive language they have demonstrated face-to-face.",
    ],
    conversation_prompts=[
        "Tell me about a time online when someone wasn't nice — what did you say or do?",
        "Tell me about a rule for screens that is easy to keep, and one that is hard — why?",
        "When someone online wants you to keep going and you want to stop, what do you do?",
    ],
    source_kud_item_ids=["kud_lt_8_3_B_01"],
    decomposition_rationale="Single Band B criterion — parent-observation-primary indicators of self-directed exit, assertive language transfer, and rule-following without reminder form one integrated disposition at this band.",
    prerequisite_criterion_ids=[cid(164), cid(2), cid(63), cid(64), cid(65)],
    prerequisite_edges_detail=edges(cid(165), [
        (cid(164), "within_lt_band"),
        (cid(2), "cross_lt_source_stated"),
        (cid(63), "cross_lt_source_stated"),
        (cid(64), "cross_lt_source_stated"),
        (cid(65), "cross_lt_source_stated"),
    ]),
))

# LT 8.3 T3 C (crit_0166)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(166), lt_id="lt_8_3", band="C",
    criterion_statement=LT83_BASE_STATEMENT,
    criterion_label="[Band C] Digital Assertiveness & Wellbeing Strategies (dispositional observation)",
    observation_indicators=[
        "The student names their own digital boundaries — when they will and will not use a device, what they will and will not engage with — and largely keeps to them without external reminders, across home, school, and friend contexts.",
        "The student speaks up or exits group chats, games, or platform interactions where peers behave unkindly, excludingly, or unsafely, on more than one observed occasion.",
        "The student takes independent action (muting, blocking, unfollowing, reporting, stepping away) when content or interaction is affecting their wellbeing, without adult prompt.",
        "The student treats their digital boundaries as self-authored, not as rules handed to them — they can explain why the boundary is theirs.",
    ],
    confusable_behaviours=[
        "Citing adult-given rules (\"my mum said\") as the reason for a digital boundary mistaken for self-authored practice. Distinction: the disposition shows in the student's own reason for the boundary, not in citing an external authority.",
        "Exiting only the most-visibly-unacceptable content while staying in lower-grade unkind interactions mistaken for active boundary-setting. Distinction: the disposition includes responsiveness to subtler signals, not only the obvious ones.",
    ],
    absence_indicators=[
        "The student's digital boundaries are visibly enforced by adults (phone in kitchen, parental controls) and collapse in their absence.",
        "The student stays in group chats or platform interactions they privately find distressing, without using the specific named actions (mute, block, unfollow, report, step away).",
    ],
    conversation_prompts=[
        "What's a digital boundary that is genuinely yours — and how did you come to it?",
        "When do you find it easiest to exit a group chat that isn't working, and when is it hardest?",
        "Tell me about a time you muted or blocked or unfollowed — what drove the choice?",
    ],
    source_kud_item_ids=["kud_lt_8_3_C_01"],
    decomposition_rationale="Single Band C criterion — self-authored boundaries, exit/speak-up behaviour, and named platform-specific self-protection actions form one integrated disposition.",
    prerequisite_criterion_ids=[cid(165), cid(3), cid(66), cid(67), cid(68), cid(138)],
    prerequisite_edges_detail=edges(cid(166), [
        (cid(165), "within_lt_band"),
        (cid(3), "cross_lt_source_stated"),
        (cid(66), "cross_lt_source_stated"),
        (cid(67), "cross_lt_source_stated"),
        (cid(68), "cross_lt_source_stated"),
        (cid(138), "cross_lt_source_stated"),
    ]),
))

# LT 8.3 T3 D (crit_0167)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(167), lt_id="lt_8_3", band="D",
    criterion_statement=LT83_BASE_STATEMENT,
    criterion_label="[Band D] Digital Assertiveness & Wellbeing Strategies (dispositional observation)",
    observation_indicators=[
        "The student maintains stated digital boundaries under social pressure — friends pushing them back into a chat, a game, a notification check — on more than one observed occasion.",
        "The student uses assertive communication in difficult digital interactions (disagreement, exclusion dynamics, pressure) without escalating into harshness, abandoning the conversation, or capitulating against their stated position.",
        "The student adjusts their digital practice based on evidence they have collected about its effects on their attention, mood, or sleep — and can point to the adjustment and the evidence that drove it.",
        "The student distinguishes \"the feature is designed to pull me back\" from \"I have to go back\", and operates accordingly.",
    ],
    confusable_behaviours=[
        "Holding a boundary in public while breaking it in private (\"I told them no but later I joined\") mistaken for under-pressure maintenance. Distinction: the disposition shows in the follow-through when the audience has moved on.",
        "Assertiveness that flips into harshness (\"leave me alone, idiots\") mistaken for mature assertiveness. Distinction: the disposition holds position without attacking the person.",
    ],
    absence_indicators=[
        "The student's stated boundaries reliably collapse under peer pressure, across multiple observed weeks, with the pattern unchanged.",
        "The student's digital practice is insensitive to evidence about its effects on them, even when the evidence is clear (sleep reports, mood, academic drop).",
    ],
    conversation_prompts=[
        "Tell me about a digital boundary you held under pressure — what was the pressure and what held you?",
        "Where has your digital practice changed this year based on what you noticed was happening to you?",
        "When does assertiveness tip into harshness for you online — and what do you do with that?",
    ],
    source_kud_item_ids=["kud_lt_8_3_D_01"],
    decomposition_rationale="Single Band D criterion — under-pressure boundary maintenance, non-escalating assertiveness, and evidence-driven adjustment form one integrated disposition.",
    prerequisite_criterion_ids=[cid(166), cid(4), cid(69), cid(70), cid(71), cid(139)],
    prerequisite_edges_detail=edges(cid(167), [
        (cid(166), "within_lt_band"),
        (cid(4), "cross_lt_source_stated"),
        (cid(69), "cross_lt_source_stated"),
        (cid(70), "cross_lt_source_stated"),
        (cid(71), "cross_lt_source_stated"),
        (cid(139), "cross_lt_source_stated"),
    ]),
))

# LT 8.3 T3 E (crit_0168)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(168), lt_id="lt_8_3", band="E",
    criterion_statement=LT83_BASE_STATEMENT,
    criterion_label="[Band E] Digital Assertiveness & Wellbeing Strategies (dispositional observation)",
    observation_indicators=[
        "The student sustains digital wellbeing practices across extended periods — not only in a tracked week, but as an integrated part of their life across terms.",
        "The student holds their position in digital disagreements or conflicts without becoming harsh, performative, or retreating — substantive assertiveness addressing the other's argument, not their identity or the audience.",
        "The student notices when their digital practice is not serving them well and adjusts proactively — before a crisis or a forced break — on more than one observed occasion across the year.",
        "The student's digital practice quality is the same whether or not they are being tracked or observed.",
    ],
    confusable_behaviours=[
        "Visible performance of digital restraint (\"I don't use my phone anymore\") mistaken for sustained practice. Distinction: the disposition is quiet and continuous — often not visible unless specifically asked.",
        "Assertiveness that plays to the audience rather than addresses the other person (\"he's wrong and I'm going to take him down\") mistaken for substantive assertiveness. Distinction: the disposition is aimed at the argument, not the optics.",
    ],
    absence_indicators=[
        "Digital wellbeing practices collapse between terms or during breaks, resuming only when school tracking resumes.",
        "The student's online conflicts consistently feature harshness, performance, or retreat, without the stable substantive-disagreement move appearing.",
    ],
    conversation_prompts=[
        "Where does your digital practice hold across untracked weeks, and where does it slip?",
        "Tell me about a digital disagreement you held substantively — what kept you from performing or retreating?",
        "What's a proactive adjustment you made this year before a crisis — what made you see it coming?",
    ],
    source_kud_item_ids=["kud_lt_8_3_E_01"],
    decomposition_rationale="Single Band E criterion — untracked-period sustained practice, substantive (non-performative) assertiveness, and proactive adjustment form one integrated lived-practice disposition.",
    prerequisite_criterion_ids=[cid(167), cid(142), cid(118), cid(140)],
    prerequisite_edges_detail=edges(cid(168), [
        (cid(167), "within_lt_band"),
        (cid(142), "cross_lt_source_stated"),
        (cid(118), "cross_lt_source_stated"),
        (cid(140), "cross_lt_source_stated"),
    ]),
))

# LT 8.3 T3 F (crit_0169)
NEW_ENTRIES.append(make_t3_new(
    criterion_id=cid(169), lt_id="lt_8_3", band="F",
    criterion_statement=LT83_BASE_STATEMENT,
    criterion_label="[Band F] Digital Assertiveness & Wellbeing Strategies (dispositional observation)",
    observation_indicators=[
        "The student treats their digital life as an expression of their values — what they engage with, what they create, what they refuse — and can articulate this stance when asked, without turning it into a public performance.",
        "The student supports peers navigating digital pressure, conflict, or harm, without taking over the situation, without shaming the peer for being in it, and with authentic respect for the peer's own agency.",
        "The student holds consistent digital practices across contexts — teacher-observed, parent-observed, peer-observed, self-reported — with no quality shift based on who is watching.",
        "The student's digital identity aligns with their face-to-face identity; the student is recognisably the same person online and offline.",
    ],
    confusable_behaviours=[
        "Public performance of digital values (regular posts advocating digital restraint) mistaken for integrated values. Distinction: the disposition is the consistency of practice, visible without being advertised.",
        "Taking over a peer's digital situation (\"I'll deal with it for you\") mistaken for peer support. Distinction: the disposition respects the peer's own agency — support is offered, not imposed.",
    ],
    absence_indicators=[
        "The student's digital practice diverges across observed contexts — visibly good when supervised, visibly different when not — even after years in the programme.",
        "The student's peer support in digital situations consistently takes over or shames, without the agency-respecting move appearing.",
    ],
    conversation_prompts=[
        "Walk me through how your digital life is actually an expression of your values — with examples, not slogans.",
        "Tell me about a time you supported a peer through a digital situation without taking over. What kept you from taking over?",
        "Where is the consistency between your online self and your offline self — and where is the gap that still catches you?",
    ],
    source_kud_item_ids=["kud_lt_8_3_F_01"],
    decomposition_rationale="Single Band F criterion — values-integrated digital life, agency-respecting peer support, and cross-context behavioural consistency form one identity-level integrated disposition.",
    prerequisite_criterion_ids=[cid(168), cid(143), cid(119), cid(141)],
    prerequisite_edges_detail=edges(cid(169), [
        (cid(168), "within_lt_band"),
        (cid(143), "cross_lt_source_stated"),
        (cid(119), "cross_lt_source_stated"),
        (cid(141), "cross_lt_source_stated"),
    ]),
))


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    with open(IN) as f:
        bank = json.load(f)

    # Restructure existing T3 entries
    restructured_count = 0
    for c in bank["criteria"]:
        if c["criterion_id"] in RESTRUCTURE:
            d = RESTRUCTURE[c["criterion_id"]]
            c.pop("competency_level_descriptors", None)
            c["criterion_statement"] = d["criterion_statement"]
            c["criterion_label"] = d["criterion_label"]
            c["observation_indicators"] = d["observation_indicators"]
            c["confusable_behaviours"] = d["confusable_behaviours"]
            c["absence_indicators"] = d["absence_indicators"]
            c["conversation_prompts"] = d["conversation_prompts"]
            c["schema_version"] = "v2"
            restructured_count += 1
    assert restructured_count == 20, f"Expected 20 restructured, got {restructured_count}"

    # Add new entries
    bank["criteria"].extend(NEW_ENTRIES)
    assert len(NEW_ENTRIES) == 28, f"Expected 28 new, got {len(NEW_ENTRIES)}"

    # Update file-level metadata
    bank["schema_version"] = "v2"
    if "note" in bank:
        del bank["note"]
    bank["total_criteria"] = len(bank["criteria"])

    # Rebuild strand_summaries
    strand_counts = defaultdict(int)
    # Map LT ID prefix -> strand
    lt_to_strand = {
        "lt_1_1": "comp_1", "lt_1_2": "comp_1", "lt_1_3": "comp_1",
        "lt_2_1": "comp_2", "lt_2_2": "comp_2",
        "lt_3_1": "comp_3", "lt_3_2": "comp_3",
        "lt_4_1": "comp_4", "lt_4_2": "comp_4", "lt_4_3": "comp_4",
        "lt_5_1": "comp_5", "lt_5_2": "comp_5",
        "lt_6_1": "comp_6", "lt_6_2": "comp_6",
        "lt_7_1": "comp_7", "lt_7_2": "comp_7",
        "lt_8_1": "comp_8", "lt_8_2": "comp_8", "lt_8_3": "comp_8",
    }
    for c in bank["criteria"]:
        for lt in c["associated_lt_ids"]:
            strand_counts[lt_to_strand[lt]] += 1

    strand_names = {
        "comp_1": "Emotional Intelligence",
        "comp_2": "Attention & Reflective Practices",
        "comp_3": "Physical Wellbeing & Self-Care",
        "comp_4": "Consent, Safety & Healthy Relationships",
        "comp_5": "Community, Purpose & Belonging",
        "comp_6": "Wellbeing Science & Literacy",
        "comp_7": "Metacognitive Self-Direction",
        "comp_8": "Critical Digital Literacy",
    }
    bank["strand_summaries"] = [
        {"strand": s, "strand_name": strand_names[s], "criteria_count": strand_counts[s]}
        for s in ["comp_1", "comp_2", "comp_3", "comp_4", "comp_5", "comp_6", "comp_7", "comp_8"]
    ]

    # DAG validation
    all_ids = {c["criterion_id"] for c in bank["criteria"]}
    edges_all = []
    unresolved_ids = set()
    self_loops = []
    for c in bank["criteria"]:
        for e in c.get("prerequisite_edges_detail", []):
            edges_all.append((e["from"], e["to"]))
            if e["from"] == e["to"]:
                self_loops.append(e["from"])
            if e["from"] not in all_ids:
                unresolved_ids.add(e["from"])
            if e["to"] not in all_ids:
                unresolved_ids.add(e["to"])
        for p in c.get("prerequisite_criterion_ids", []):
            if p not in all_ids:
                unresolved_ids.add(p)

    # Cycle detection via Kahn's algorithm
    in_degree = defaultdict(int)
    graph = defaultdict(list)
    for src, dst in edges_all:
        graph[src].append(dst)
        in_degree[dst] += 1
    queue = deque([n for n in all_ids if in_degree[n] == 0])
    visited = 0
    while queue:
        n = queue.popleft()
        visited += 1
        for nxt in graph[n]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)
    cycles = []
    if visited < len(all_ids):
        remaining = [n for n in all_ids if in_degree.get(n, 0) > 0]
        cycles = [remaining]  # at least one cycle exists among remaining

    bank["dag_validation"] = {
        "dag_valid": len(cycles) == 0 and len(self_loops) == 0 and len(unresolved_ids) == 0,
        "status": "PASS" if (len(cycles) == 0 and len(self_loops) == 0 and len(unresolved_ids) == 0) else "FAIL",
        "total_criteria": len(bank["criteria"]),
        "total_edges": len(edges_all),
        "cycles": cycles,
        "self_loops": self_loops,
        "unresolved_ids": sorted(unresolved_ids),
    }

    with open(OUT, "w") as f:
        json.dump(bank, f, indent=2, ensure_ascii=False)

    print(f"Wrote {OUT}")
    print(f"Total criteria: {bank['total_criteria']}")
    print(f"Schema version: {bank['schema_version']}")
    print(f"DAG validation: {bank['dag_validation']['status']}")
    print(f"Total edges: {bank['dag_validation']['total_edges']}")
    print(f"Strand summaries:")
    for s in bank["strand_summaries"]:
        print(f"  {s['strand']}: {s['criteria_count']} — {s['strand_name']}")


if __name__ == "__main__":
    main()
