#!/usr/bin/env python3
"""
Criterion bank v3 regeneration — Steps 2, 3, 4, 5, 6.

Input: docs/reference-corpus/real-wellbeing/criterion-bank-v3.json (already a copy of v2)
Output: same file, rewritten in place (v3 working copy only — v2 never touched)
Side-effect: prints a full audit log of everything done.
"""
import json
import copy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V3 = ROOT / "docs/reference-corpus/real-wellbeing/criterion-bank-v3.json"
EDGE_LOG = ROOT / "docs/reference-corpus/real-wellbeing/v3-edge-removal-log.md"

IDS_TO_REMOVE = {
    "real-wellbeing-2026-04_crit_0156",
    "real-wellbeing-2026-04_crit_0283",
    "real-wellbeing-2026-04_crit_0284",
    "real-wellbeing-2026-04_crit_0285",
    "real-wellbeing-2026-04_crit_0286",
    "real-wellbeing-2026-04_crit_0287",
    "real-wellbeing-2026-04_crit_0288",
    "real-wellbeing-2026-04_crit_0289",
    "real-wellbeing-2026-04_crit_0290",
    "real-wellbeing-2026-04_crit_0291",
    "real-wellbeing-2026-04_crit_0292",
    "real-wellbeing-2026-04_crit_0293",
    "real-wellbeing-2026-04_crit_0294",
}


def load():
    with open(V3) as f:
        return json.load(f)


def save(bank):
    with open(V3, "w") as f:
        json.dump(bank, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Step 2 + Step 3: remove entries and edges, log everything
# ---------------------------------------------------------------------------

def step_2_and_3(bank, log_lines):
    removed_edges = []  # list of (from_id, to_id, edge_type)

    criteria = bank["criteria"]
    id_to_crit = {c["criterion_id"]: c for c in criteria}

    # A) Collect edges where a removed ID is `to` (stored inside the removed crit).
    for rid in sorted(IDS_TO_REMOVE):
        c = id_to_crit.get(rid)
        if c is None:
            continue
        for edge in c.get("prerequisite_edges_detail", []):
            removed_edges.append((edge["from"], edge["to"], edge.get("edge_type", "unknown"), f"removed-because-{rid}-deleted"))

    # B) Collect edges where a removed ID is `from` (stored on OTHER criteria that depend on it).
    for c in criteria:
        if c["criterion_id"] in IDS_TO_REMOVE:
            continue
        for edge in c.get("prerequisite_edges_detail", []):
            if edge["from"] in IDS_TO_REMOVE:
                removed_edges.append((edge["from"], edge["to"], edge.get("edge_type", "unknown"), f"removed-because-{edge['from']}-deleted"))

    # C) Now actually delete the 13 criteria.
    new_criteria = [c for c in criteria if c["criterion_id"] not in IDS_TO_REMOVE]
    assert len(new_criteria) == len(criteria) - len(IDS_TO_REMOVE), \
        f"expected {len(criteria) - len(IDS_TO_REMOVE)} after removal, got {len(new_criteria)}"

    # D) Scrub removed-ID references from every remaining criterion's
    #    prerequisite_criterion_ids + prerequisite_edges_detail.
    for c in new_criteria:
        c["prerequisite_criterion_ids"] = [
            pid for pid in c.get("prerequisite_criterion_ids", [])
            if pid not in IDS_TO_REMOVE
        ]
        c["prerequisite_edges_detail"] = [
            e for e in c.get("prerequisite_edges_detail", [])
            if e["from"] not in IDS_TO_REMOVE and e["to"] not in IDS_TO_REMOVE
        ]

    bank["criteria"] = new_criteria

    # E) Step 3 addition — remove hard-prereq edges from LT 4.3 Bands A,B
    #    criteria pointing to LT 1.2 Bands A,B criteria.
    lt43_ab_ids = {
        c["criterion_id"]
        for c in new_criteria
        if "lt_4_3" in c.get("associated_lt_ids", []) and c.get("band") in ("A", "B")
    }
    lt12_ab_ids = {
        c["criterion_id"]
        for c in new_criteria
        if "lt_1_2" in c.get("associated_lt_ids", []) and c.get("band") in ("A", "B")
    }

    log_lines.append(f"\n### LT 4.3 A/B criteria ({len(lt43_ab_ids)}): {sorted(lt43_ab_ids)}")
    log_lines.append(f"### LT 1.2 A/B criteria ({len(lt12_ab_ids)}): {sorted(lt12_ab_ids)}")

    lt43_edge_removals = []
    for c in new_criteria:
        if c["criterion_id"] not in lt43_ab_ids:
            continue
        # Edges on this LT 4.3 A/B criterion pointing into it from LT 1.2 A/B
        # (from = prerequisite, to = this crit)
        keep_edges = []
        for e in c.get("prerequisite_edges_detail", []):
            if e["from"] in lt12_ab_ids and e["to"] == c["criterion_id"]:
                lt43_edge_removals.append((e["from"], e["to"], e.get("edge_type", "unknown"), "LT 4.3 A/B → LT 1.2 A/B hard edge: audit §4 remove"))
            else:
                keep_edges.append(e)
        c["prerequisite_edges_detail"] = keep_edges
        c["prerequisite_criterion_ids"] = [pid for pid in c.get("prerequisite_criterion_ids", []) if pid not in lt12_ab_ids]

    log_lines.append(f"\n### Removed edges: T2-entry-touching ({len(removed_edges)}) + LT 4.3→LT 1.2 ({len(lt43_edge_removals)}) = {len(removed_edges) + len(lt43_edge_removals)}")
    log_lines.append("\n#### A. Edges removed because of LT 1.3 T2-entry deletion\n")
    log_lines.append("| from | to | edge_type | reason |")
    log_lines.append("|---|---|---|---|")
    for fr, to, et, why in removed_edges:
        log_lines.append(f"| {fr} | {to} | {et} | {why} |")

    log_lines.append("\n#### B. LT 4.3 A/B → LT 1.2 A/B hard prerequisite edges removed (audit §4)\n")
    log_lines.append("| from | to | edge_type | reason |")
    log_lines.append("|---|---|---|---|")
    if not lt43_edge_removals:
        log_lines.append("| — | — | — | none found |")
    for fr, to, et, why in lt43_edge_removals:
        log_lines.append(f"| {fr} | {to} | {et} | {why} |")

    return len(removed_edges), len(lt43_edge_removals)


# ---------------------------------------------------------------------------
# Step 4: regenerate LT 1.3 Band D and Band E T3 entries with new IDs
# ---------------------------------------------------------------------------

def step_4(bank):
    # Remove the OLD Band D and Band E T3 entries (crit_0161, crit_0162)
    OLD_IDS = {"real-wellbeing-2026-04_crit_0161", "real-wellbeing-2026-04_crit_0162"}
    # Also scrub any references from other criteria (edges pointing into these).
    new_criteria = []
    old_incoming_edges = []
    for c in bank["criteria"]:
        if c["criterion_id"] in OLD_IDS:
            # Capture edges stored on this crit (to = this crit) for logging.
            for e in c.get("prerequisite_edges_detail", []):
                old_incoming_edges.append((e["from"], e["to"], e.get("edge_type", "unknown")))
            continue
        new_criteria.append(c)
    for c in new_criteria:
        c["prerequisite_criterion_ids"] = [pid for pid in c.get("prerequisite_criterion_ids", []) if pid not in OLD_IDS]
        c["prerequisite_edges_detail"] = [e for e in c.get("prerequisite_edges_detail", []) if e["from"] not in OLD_IDS and e["to"] not in OLD_IDS]
    bank["criteria"] = new_criteria

    # New IDs continue from the highest ID confirmed in Step 0 (crit_0294),
    # per the session brief — do NOT reuse any removed/retired IDs.
    # The 13 removed T2 IDs include 0283–0294; crit_0161/0162 are retired.
    HIGHEST_EXISTING_AT_STEP_0 = 294
    new_d_id = f"real-wellbeing-2026-04_crit_{HIGHEST_EXISTING_AT_STEP_0+1:04d}"
    new_e_id = f"real-wellbeing-2026-04_crit_{HIGHEST_EXISTING_AT_STEP_0+2:04d}"

    # --- Band D entry (regenerated from v2 Band D Know/Understand/Do) -----
    band_d = {
        "criterion_id": new_d_id,
        "associated_lt_ids": ["lt_1_3"],
        "band": "D",
        "band_label": "Metal Dragons (ages 11–13)",
        "lt_type": "Type 3",
        "strand": "single_strand",
        "criterion_statement": (
            "The student recognises, in context, that some of their own group memberships were unchosen and that in-group preference "
            "operates automatically — shown by the student naming how an unchosen membership or automatic in-group preference is "
            "shaping their own experience, reaction, or interpretation in a specific situation they are inside of, not only as an "
            "abstract claim."
        ),
        "criterion_label": "[Band D] Personal Identity & Cultural Self-Awareness (dispositional observation)",
        "source_kud_item_ids": ["kud_lt_1_3_D_01"],
        "decomposition_rationale": (
            "Regenerated 23 April 2026 under Option 1 (see REAL_Wellbeing_KUD_fixes_applied_20260423.md Step 3a). Single T3 criterion "
            "because the Band D Do specifies a unified dispositional move — recognising in context how unchosen group membership or "
            "in-group preference is operating on the student's own experience — which cannot be split without losing the "
            "in-situation qualifier."
        ),
        "prerequisite_criterion_ids": [],
        "prerequisite_edges_detail": [],
        "schema_version": "v2",
        "observation_indicators": [
            "The student names an unchosen group membership they hold (family of origin, nationality, first language, how others read their body or appearance) AS it is shaping a specific situation they are inside of — spontaneously or when a situation makes it relevant — not only as an abstract claim that 'in-group preference exists'.",
            "The student catches themselves, in a classroom discussion, group task, or social exchange, in a moment of automatic in-group preference (favouring a peer from their own group, dismissing an out-group perspective) and says so, without adult prompting to do so.",
            "When interpreting a text, event, or peer's account, the student notes how an unchosen membership of theirs is shaping what they are noticing or missing — using concrete reference to the situation, not reciting the claim in the abstract.",
            "In a cross-cultural or cross-group exchange, the student pauses and attributes their own reaction (confusion, irritation, quick agreement) to an unchosen membership or in-group preference, before concluding whose view is correct."
        ],
        "confusable_behaviours": [
            "Fluently stating the Band D Know claims (\"unchosen group memberships shape experience\", \"in-group preference operates automatically\") in the abstract when asked. Distinction: the disposition is visible only when the student applies the claim to a specific situation they are inside of, with enough concrete reference to show they are tracking the mechanism, not reciting it.",
            "Pointing at other people's unchosen memberships or in-group preference (\"that's why they voted that way\", \"that's why group X dismisses group Y\") without ever examining the student's own. Distinction: Band D requires the student to locate the mechanism in their own perspective, not only in others.",
            "Performative self-critique that foregrounds a single marked identity (\"as a [nationality/gender/etc.] I…\") in the way an adult audience expects, with no specific situation and no change in behaviour. Distinction: authentic recognition refers to a real moment of reaction and adjusts the student's response in it."
        ],
        "absence_indicators": [
            "Across a term, the student treats their own reactions, judgements, and interpretations as neutral observation — never locating any of their own views in an unchosen group membership or in-group preference, even when the situation plainly involves one.",
            "When an out-group perspective is raised, the student dismisses it on merit without any self-check, showing no evidence that automatic in-group preference is recognisable to them as a mechanism operating in themselves.",
            "When asked directly \"how might your own background be shaping what you're noticing here?\" the student either denies it applies or produces an off-the-shelf label without any situation-specific reference."
        ],
        "conversation_prompts": [
            "Think about a moment this month when you felt strongly that a peer, group, or source was right or wrong. Can you point at anything you didn't choose about your own background that might have been shaping that reaction?",
            "Have you ever caught yourself preferring your own group without deciding to — not as a big claim, but in a specific moment? Tell me what you noticed.",
            "When you read or watched [recent shared text/event], were there parts where something about your own background made some things obvious to you and other things easy to miss?"
        ],
    }

    # --- Band E entry (regenerated from v2 Band E Know/Understand/Do, 4-item Know) --
    band_e = {
        "criterion_id": new_e_id,
        "associated_lt_ids": ["lt_1_3"],
        "band": "E",
        "band_label": "Light Dragons (ages 13–15)",
        "lt_type": "Type 3",
        "strand": "single_strand",
        "criterion_statement": (
            "The student voluntarily identifies, with specificity, how their own cultural lens — now analysable through the named "
            "Band E concepts (cultural lens, ethnocentrism, social identity theory, intersectionality) — is limiting or distorting "
            "their interpretation of a text, event, or interaction, in contexts where this is not explicitly required of them."
        ),
        "criterion_label": "[Band E] Personal Identity & Cultural Self-Awareness (dispositional observation)",
        "source_kud_item_ids": ["kud_lt_1_3_E_01"],
        "decomposition_rationale": (
            "Regenerated 23 April 2026 under Option 1 (see REAL_Wellbeing_KUD_fixes_applied_20260423.md Step 3a). Single T3 criterion "
            "because the Band E Do specifies a unified dispositional move — voluntary, self-initiated identification of one's own "
            "lens effects in contexts where nobody asked — which is evidenced as a pattern of initiation across occasions rather "
            "than as component steps."
        ),
        "prerequisite_criterion_ids": [],
        "prerequisite_edges_detail": [],
        "schema_version": "v2",
        "observation_indicators": [
            "In a discussion, essay, or reflection where lens analysis is not required, the student voluntarily identifies a specific way their cultural lens, ethnocentric assumption, in-group identification, or intersectional position is shaping what they are reading into the material — with enough specificity that the named concept is doing real work, not acting as label.",
            "The student names a limit of their own interpretation before defending it — on more than one occasion across the term, and across more than one subject or context — using the Band E vocabulary correctly but not ornamentally.",
            "In a cross-cultural or contested exchange, the student self-initiates a revision of their position after recognising that their reading was narrowed by their own lens, rather than waiting for the opposing view to push them.",
            "In Reflection 360 or a comparable conversation, the student can trace a recent change in their own view to a specific lens-awareness move they made, with a concrete example rather than a generalised account."
        ],
        "confusable_behaviours": [
            "Deploying the Band E vocabulary (cultural lens, ethnocentrism, social identity theory, intersectionality) fluently when prompted to apply it, but never self-initiating the move in unprompted contexts. Distinction: Band E is dispositional — it requires the move to appear when nobody cued it.",
            "Using the named concepts as blanket disclaimers (\"of course my intersectional position shapes this\") without any specific content or change in interpretation. Distinction: authentic lens awareness narrows the claim or changes the reading; it does not preface an unchanged position.",
            "Analysing lens effects only in other people's views (a text author, a political speaker, an opposing peer) without turning the same analysis on the student's own position. Distinction: Band E requires the student to be inside the analysis, not only performing it on others."
        ],
        "absence_indicators": [
            "Across the term, the student uses the Band E concepts only when asked to, only in assessed tasks, and only on other people's views — never self-initiating lens analysis on their own position in unprompted contexts.",
            "When faced with a text or event at the edge of the student's experience, the student defends their first interpretation on content grounds alone, with no evidence the named Band E concepts are available to them as working tools for self-analysis.",
            "The student treats \"everyone has a lens\" as a conversation-ender rather than a starting point — used to deflect specificity rather than to do any specific self-examination."
        ],
        "conversation_prompts": [
            "Think of a recent opinion of yours that changed or sharpened. Can you say what about your own lens was limiting the earlier version — with specifics, not in general?",
            "Where in the last month did you catch your own ethnocentrism, in-group identification, or a missing intersection in your reading of a situation, without anyone pointing it out to you? Tell me the situation.",
            "When you use words like 'cultural lens' or 'intersectionality', are they doing real work in your thinking right now, or are they labels? Give me an example where they were doing real work."
        ],
    }

    bank["criteria"].append(band_d)
    bank["criteria"].append(band_e)
    return new_d_id, new_e_id, old_incoming_edges


# ---------------------------------------------------------------------------
# Step 5: regenerate crit_0145 (LT 1.2 Band F) — retain ID
# ---------------------------------------------------------------------------

def step_5(bank):
    for c in bank["criteria"]:
        if c["criterion_id"] == "real-wellbeing-2026-04_crit_0145":
            c["lt_type"] = "Type 3"
            if "competency_level_descriptors" in c:
                del c["competency_level_descriptors"]
            c["criterion_statement"] = (
                "The student adjusts their response, in a specific situation, to someone whose experience is being shaped by "
                "structural or systemic factors, in ways that address those conditions rather than only the individual person — "
                "across more than one observed occasion, such that recognition of structure is inferred from the adjustment, not "
                "from verbal recognition alone."
            )
            c["criterion_label"] = "[Band F] Social Awareness & Empathy (dispositional observation)"
            c["decomposition_rationale"] = (
                "Regenerated 23 April 2026 (see REAL_Wellbeing_KUD_fixes_applied_20260423.md Step 3b). Single T3 criterion because "
                "the Band F Do specifies one unified observable — structural-aware action-adjustment across more than one occasion — "
                "which cannot be split without losing the cross-context qualifier."
            )
            c["observation_indicators"] = [
                "Across more than one observed occasion in different interactions, the student responds to someone shaped by a structural factor (language access, migration status, gender-based targeting, class resource gap, racialised treatment) with a response that addresses the condition — advocating quietly to a teacher, reallocating the group's resource, adjusting the format of a shared task — not only the momentary feeling.",
                "The student modifies their own behaviour (how they divide work, whom they defer to, what they propose in a group) in the presence of structural disadvantage affecting a peer, without waiting for the peer to name the disadvantage and without announcing their own awareness of it.",
                "The teacher notices the student's response to the same person changes across contexts when the structural factor does — e.g. at a social moment vs in an institutional moment vs in a peer-pressure moment — showing the adjustment is to the condition, not a generic empathic posture.",
                "The student, in repair after an incident, names what about the conditions mattered — not only how the affected person felt — and proposes a next step that changes those conditions in the peer group or classroom."
            ]
            c["confusable_behaviours"] = [
                "Verbally recognising structural or systemic factors fluently in an assessed task or assembly, with no corresponding change in the student's response toward an affected peer in everyday interaction. Distinction: Band F requires action-adjustment as the primary observable; verbal recognition is supporting, not primary.",
                "Performative advocacy — public statements, social-media-style framing, badge-wearing — produced for an audience, with no evidence of adjustment in ordinary peer interactions. Distinction: the adjustment must show up when no audience is watching for it, and across more than one occasion.",
                "A single dramatic intervention (a single stand-up-to-a-bully moment) with no pattern either side of it. Distinction: Band F is dispositional — it requires the pattern across occasions."
            ]
            c["absence_indicators"] = [
                "The student's response to someone shaped by structural factors does not vary with the conditions — only with the immediate emotional display — showing that empathy is operating at the Band E level, not the structural level.",
                "When structural factors are relevant (a recently arrived peer navigating language access, a peer targeted on a gendered or racial basis), the student engages only through generalised kind words or avoidance, with no observable adjustment of what they do.",
                "In repair or reflection, the student frames the incident entirely as an interpersonal misunderstanding, showing no working awareness of conditions as a layer to address."
            ]
            c["conversation_prompts"] = [
                "Think of a time this term when someone you were working with was being affected by something bigger than the moment — their situation, how the school treats something, how a group was being read. What did you actually do differently?",
                "Where in the last month did you change how you were doing something — not just what you were saying — because of what was shaping a peer's experience?",
                "What's the difference, for you, between noticing that structural stuff is in play and actually adjusting what you do? Can you give me a recent example of each?"
            ]
            return c
    raise RuntimeError("crit_0145 not found")


# ---------------------------------------------------------------------------
# Step 6: regenerate crit_0149 (LT 5.2 Band F) — retain ID
# ---------------------------------------------------------------------------

def step_6(bank):
    for c in bank["criteria"]:
        if c["criterion_id"] == "real-wellbeing-2026-04_crit_0149":
            c["lt_type"] = "Type 3"
            if "competency_level_descriptors" in c:
                del c["competency_level_descriptors"]
            c["criterion_statement"] = (
                "The student's post-school choices (path, community involvement, roles) trace specifically and observably to their "
                "sustained prior engagement, as evidenced across Reflection 360 and the preceding two years of engagement history — "
                "and when asked about purpose the student points to that engagement with specificity rather than to abstracted "
                "articulation."
            )
            c["criterion_label"] = "[Band F] Community Engagement & Purpose (dispositional observation)"
            c["decomposition_rationale"] = (
                "Regenerated 23 April 2026 (see REAL_Wellbeing_KUD_fixes_applied_20260423.md Step 3c). Single T3 criterion because "
                "the Band F Do specifies one unified observable — traceability between sustained prior engagement and observable "
                "post-school choices, evidenced longitudinally — which cannot be split without losing the engagement-history evidence base."
            )
            c["observation_indicators"] = [
                "Across Reflection 360 and at least two years of project, initiative, or community-engagement records, the post-school choice the student is actually making (course, role, service commitment, team, apprenticeship, gap placement) traces specifically to particular prior engagements — not to a generic statement of values.",
                "When asked about purpose, the student points to specific prior engagements (named D2R projects, named initiatives, specific people they worked with, specific problems they kept returning to) rather than to abstracted articulation, and names what that engagement taught them that is now showing up in the choice.",
                "The teacher or mentor can trace — from records, not only from the student's narration — how the student's engagement over Bands D and E concentrated on particular communities or problems, and the Band F choices are on the same line, not a switch.",
                "When the student's post-school choice narrows or shifts, the student narrates the change as a revision based on what was learned in specific engagements, not as a reinvention of self, and the change is legible in the record."
            ]
            c["confusable_behaviours"] = [
                "Articulate, well-rehearsed purpose statements delivered in Reflection 360 or capstone presentations that are not traceable to specific prior engagement — the language is coherent but the line back to what the student actually did is missing. Distinction: Band F requires the engagement history + choices, not articulation alone.",
                "A single capstone project or final-year commitment offered as evidence of purpose without the preceding two-year pattern. Distinction: Band F is longitudinal; single-occasion articulation cannot substitute for the traceable history.",
                "Purpose framed entirely in terms of what the student stands for in abstract (values language) with no concrete engagement-to-choice line. Distinction: mature purpose at Band F shows up as choices whose origins are legible in engagement, not as identity claims."
            ]
            c["absence_indicators"] = [
                "The student's post-school choice is not traceable to their engagement history — the records show one set of sustained commitments and the choice points elsewhere, without an explicit revision narrative.",
                "In Reflection 360, the student produces values language and aspirational articulation but cannot point to specific prior engagements that the choice builds on, even when prompted to do so.",
                "The teacher or mentor cannot, without the student's narration, see the line between what the student did over two years and what they are choosing next — the choice reads as unconnected to the record."
            ]
            c["conversation_prompts"] = [
                "Walk me through how your choice for next year traces back to specific things you did here — name particular projects, particular people, particular moments, not values words.",
                "If I look at your engagement record from Bands D and E, what should I expect your post-school choice to be about? Does the choice you're making line up with that, or is it a turn — and if it's a turn, what made it turn?",
                "What is the engagement you kept coming back to even when it wasn't assigned? How is that showing up in what you're choosing to do next?"
            ]
            return c
    raise RuntimeError("crit_0149 not found")


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def main():
    bank = load()
    orig_count = len(bank["criteria"])
    print(f"[start] criteria count: {orig_count}")

    log_lines = ["# v3 edge-removal log — 23 April 2026\n"]

    # Step 2 + 3
    n_t2_edges, n_lt43_edges = step_2_and_3(bank, log_lines)
    post_removal = len(bank["criteria"])
    print(f"[Step 2] after removing 13 T2 entries: {post_removal}")
    print(f"[Step 3] edges removed — T2-entry-touching: {n_t2_edges}; LT 4.3→LT 1.2: {n_lt43_edges}; total: {n_t2_edges + n_lt43_edges}")

    # Step 4
    new_d, new_e, step4_edges_dropped = step_4(bank)
    print(f"[Step 4] regenerated LT 1.3 Band D → {new_d}; Band E → {new_e}")
    print(f"[Step 4] incoming edges lost by retiring crit_0161/0162: {len(step4_edges_dropped)} (these were already edges into OLD Band D/E entries)")
    log_lines.append(f"\n#### C. Edges lost by retiring prior crit_0161 and crit_0162 ({len(step4_edges_dropped)})\n")
    log_lines.append("| from | to | edge_type |")
    log_lines.append("|---|---|---|")
    for fr, to, et in step4_edges_dropped:
        log_lines.append(f"| {fr} | {to} | {et} |")

    # Step 5 + Step 6
    step_5(bank)
    step_6(bank)
    print("[Step 5] regenerated crit_0145 (LT 1.2 Band F) as T3")
    print("[Step 6] regenerated crit_0149 (LT 5.2 Band F) as T3")

    # Total tally
    final_count = len(bank["criteria"])
    print(f"[end] criteria count: {final_count}")

    # Update bank-level stats
    # total_criteria field
    bank["total_criteria"] = final_count

    # Save
    save(bank)

    # Write edge log
    total_edges_removed = n_t2_edges + n_lt43_edges
    log_lines.append(f"\n## Summary\n")
    log_lines.append(f"- T2-entry-touching edges removed (Step 3 part 1): **{n_t2_edges}**")
    log_lines.append(f"- LT 4.3 A/B → LT 1.2 A/B hard edges removed (Step 3 part 2, audit §4): **{n_lt43_edges}**")
    log_lines.append(f"- Edges lost by retiring prior crit_0161/0162 Band D/E T3 entries (Step 4): **{len(step4_edges_dropped)}**")
    log_lines.append(f"- Total edges removed across Steps 3 and 4: **{total_edges_removed + len(step4_edges_dropped)}**")
    EDGE_LOG.write_text("\n".join(log_lines) + "\n")
    print(f"\n[log] edge removal log → {EDGE_LOG}")

if __name__ == "__main__":
    main()
