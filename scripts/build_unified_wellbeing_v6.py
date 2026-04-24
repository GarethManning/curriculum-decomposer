"""
Build unified-wellbeing-data-v6.json and wellbeing-index-v6.json from
criterion-bank-v5_1.json (269 criteria, 523 edges) plus v5 unified data
(20 LTs: 18 from KUD v4 + LT 4.4 KUD v2) plus LT 4.5 KUD v2.

This script adds LT 4.5 — Emotional Self-Management in Practice — as the
21st learning target (inserted after lt_4_4 in the C4 competency group).

Does NOT overwrite unified-wellbeing-data-v5.json or wellbeing-index-v5.json.
"""
import json

CRIT_BANK_PATH = "docs/reference-corpus/real-wellbeing/criterion-bank-v5_1.json"
V5_UNIFIED     = "docs/reference-corpus/real-wellbeing/unified-wellbeing-data-v5.json"
V5_INDEX       = "docs/reference-corpus/real-wellbeing/wellbeing-index-v5.json"
UNIFIED_OUT    = "docs/reference-corpus/real-wellbeing/unified-wellbeing-data-v6.json"
INDEX_OUT      = "docs/reference-corpus/real-wellbeing/wellbeing-index-v6.json"

# ── Load inputs ───────────────────────────────────────────────────────────────
with open(CRIT_BANK_PATH) as f:
    bank = json.load(f)

with open(V5_UNIFIED) as f:
    v5_unified = json.load(f)

with open(V5_INDEX) as f:
    v5_index = json.load(f)

# ── Build (lt_id, band) → {criterion_ids, observation_indicators} from v5_1 ──
lt_band_data: dict = {}
for c in bank["criteria"]:
    for lt in c.get("associated_lt_ids", []):
        key = (lt, c["band"])
        if key not in lt_band_data:
            lt_band_data[key] = {"criterion_ids": [], "observation_indicators": []}
        lt_band_data[key]["criterion_ids"].append(c["criterion_id"])
        if c.get("observation_indicators"):
            lt_band_data[key]["observation_indicators"].extend(c["observation_indicators"])

# ── T3 LTs — these get observation_indicators populated from the criterion bank ──
T3_LTS = {"lt_1_1", "lt_1_2", "lt_1_3", "lt_3_2", "lt_4_5", "lt_5_2", "lt_7_2", "lt_8_3"}

# ── LT 4.5 KUD content (from LT_4_5_KUD_v2_20260423.md) ──────────────────────
LT_4_5_META = {
    "lt_name":        "Emotional Self-Management in Practice",
    "competency":     "C4 — Consent, Safety & Healthy Relationships",
    "knowledge_type": "T3",
    "compound":       False,
    "band_range":     {"start": "A", "end": "F"},
    "summary":        "I can manage my own emotional activation in practice — noticing it as it arises, using regulation strategies I have been taught, seeking support when I recognise I am overwhelmed, and repairing relationships after conflict — consistently across contexts and with decreasing reliance on adult scaffolding over time.",
    "prereq_lt_ids":  ["lt_4_4", "lt_1_1", "lt_4_2"],
    "bands": {
        "A": {
            "know": [
                "A regulation strategy is something specific a person can do to help their body calm down when a feeling is strong — for example: slow breathing, moving to a quiet space, or asking a trusted adult.",
            ],
            "understand": [
                "When a feeling is big, there are things I can do that help — I do not have to wait for the feeling to disappear on its own.",
            ],
            "do": "The teacher notices the student, when experiencing a strong feeling (anger, fear, distress, or overwhelm), accepting a trusted adult's co-regulation support — such as being guided to breathe, moving to a calm space, or receiving appropriate physical comfort where school and family norms permit — and attempting to use at least one named regulation strategy alongside or following that adult support, across multiple occasions in the observation window.",
        },
        "B": {
            "know": [
                "A regulation strategy works best when used before a feeling becomes overwhelming — noticing the feeling early gives more options than waiting until it is very big.",
            ],
            "understand": [
                "I can feel a feeling and still choose how to act — the feeling does not have to choose for me.",
            ],
            "do": "The teacher notices the student, when upset or emotionally activated, using at least one named regulation strategy with adult prompting; and beginning, on some occasions across the observation window, to initiate a regulation strategy independently before the situation escalates — without needing the adult to suggest it first.",
        },
        "C": {
            "know": [
                "Automatic reactions — such as snapping, going quiet, or walking away — are fast responses that happen before conscious thinking catches up. A person can practise interrupting an automatic reaction by noticing the feeling before acting on it.",
            ],
            "understand": [
                "Noticing what I feel before I act gives me a moment of choice — and that moment of choice is where my self-management lives.",
            ],
            "do": "The teacher notices the student, in familiar emotional situations (peer conflict, disappointment, or frustration during collaborative work), using a named regulation strategy without adult prompting; and across the observation window, on at least one occasion attempting to interrupt an automatic response before acting, or seeking a trusted adult proactively before a situation escalates.",
        },
        "D": {
            "know": [
                "Cross-reference LT 4.4 Band D Know item 4 (dual-process models, stress-response window, habit formation). Applied to practice: the stress-response window concept explains why regulation strategies learned in calm moments are harder to access when emotional activation is already high — this is not failure of willpower but the predictable effect of moving outside the window of tolerance. Knowing the window makes it nameable in the moment.",
            ],
            "understand": [
                "I can prepare for hard emotional moments before they arrive — if I know what my window of tolerance feels like from the inside and what helps me stay within it, I have a plan I can use when the moment comes rather than searching for a strategy mid-crisis.",
            ],
            "do": "The teacher notices the student, across multiple emotional situations over the observation window, using taught regulation strategies in practice (not only naming or explaining them); seeking support from a trusted adult when they recognise they are approaching or exceeding their stress-response window; and attempting to repair a relational rupture on at least one occasion — by acknowledging their part in a conflict and proposing a forward step — rather than waiting for the other person to initiate.",
        },
        "E": {
            "know": [
                "Cross-reference LT 4.4 Band D Know item 4 (habit formation). Applied to practice: regulation strategies practised consistently across varied contexts become more accessible during high-activation moments — the strategy that feels effortful in early practice becomes a reliable resource over time. Strategies practised in only one type of situation tend not to transfer to different situations.",
            ],
            "understand": [
                "The strategies that help me most may not be the same across every situation — learning to notice when a strategy is not working and shifting to a different one rather than persisting with it or abandoning self-management entirely is itself a regulation skill.",
            ],
            "do": "The teacher notices the student, across multiple contexts and situations over the observation window, consistently applying regulation strategies without adult prompting — including in situations that are not practised or familiar (new social groups, unfamiliar stressors, relational conflicts outside usual friendships); recovering from emotional setbacks in ways that do not significantly impair their subsequent functioning; and, on at least one occasion, adapting their regulation approach when a strategy is not working rather than persisting with it or abandoning self-management effort entirely.",
        },
        "F": {
            "know": [
                "Cross-reference LT 4.4 Band F Know item 3 (relational repair — acknowledgement, accountability, and negotiated restoration of trust). Applied to practice: effective repair following conflict requires the person to first regulate their own emotional activation sufficiently to engage. Acknowledgement and accountability are not consistently accessible while the person is still inside the reactive response — regulation is therefore a prerequisite for repair, not a subsequent separate act. A student who attempts repair while still reactive tends to produce defensive acknowledgement, conditional accountability, or repair that functions as counter-accusation.",
            ],
            "understand": [
                "My pattern of self-management is built through repeated occasions — some chosen, some shaped by what I have lived through — and unlike a fixed trait, a pattern can be changed if I understand what sustains it. Knowing my own pattern (what activates me, what helps me most, what I tend to avoid and why) gives me the most leverage over it and makes my self-management portable to situations I have not yet encountered.",
            ],
            "do": "The teacher notices the student, across a sustained observation window and multiple contexts (academic, social, and out-of-school when triangulated), consistently managing their emotional activation in high-stakes or accumulating-stress situations without requiring adult scaffolding; initiating relational repair after conflict rather than waiting for the other person to act first; recovering from significant emotional setbacks in ways that allow re-engagement with their commitments; and, on at least one occasion, accurately articulating their own emotional pattern — what activates them, what helps them most, what tends not to help — as a working model they use to make decisions, not as a performed reflection for an observer.",
        },
    },
}

# ── Build the LT 4.5 unified entry ───────────────────────────────────────────
ALL_BANDS = ["A", "B", "C", "D", "E", "F"]

def build_lt45_entry() -> dict:
    meta = LT_4_5_META
    start = meta["band_range"]["start"]
    end   = meta["band_range"]["end"]
    active_bands = ALL_BANDS[ALL_BANDS.index(start): ALL_BANDS.index(end) + 1]

    bands_out = {}
    for band in active_bands:
        band_kud = meta["bands"][band]
        cb = lt_band_data.get(("lt_4_5", band), {"criterion_ids": [], "observation_indicators": []})
        is_t3 = "lt_4_5" in T3_LTS  # True for LT 4.5
        obs = cb["observation_indicators"] if is_t3 else []

        bands_out[band] = {
            "know":                   band_kud["know"],
            "understand":             band_kud["understand"],
            "do":                     band_kud["do"],
            "criterion_ids":          cb["criterion_ids"],
            "prerequisite_lt_ids":    meta["prereq_lt_ids"],
            "observation_indicators": obs,
        }

    return {
        "lt_id":          "lt_4_5",
        "lt_name":        meta["lt_name"],
        "competency":     meta["competency"],
        "knowledge_type": meta["knowledge_type"],
        "compound":       meta["compound"],
        "band_range":     meta["band_range"],
        "summary":        meta["summary"],
        "bands":          bands_out,
    }


lt_4_5_entry = build_lt45_entry()

# ── Build v6 unified data ─────────────────────────────────────────────────────
v6_lts = []
for lt in v5_unified["learning_targets"]:
    v6_lts.append(lt)
    if lt["lt_id"] == "lt_4_4":
        v6_lts.append(lt_4_5_entry)

v6_unified = {
    "meta": {
        "schema_version": v5_unified["meta"]["schema_version"],
        "generated_date": "2026-04-24",
        "lt_count": len(v6_lts),
    },
    "learning_targets": v6_lts,
}

with open(UNIFIED_OUT, "w") as f:
    json.dump(v6_unified, f, indent=2, ensure_ascii=False)

print(f"Wrote {UNIFIED_OUT} ({len(v6_lts)} LTs)")

# ── Build v6 index ────────────────────────────────────────────────────────────
v6_index_entries = []
for entry in v5_index["learning_targets"]:
    v6_index_entries.append(entry)
    if entry["lt_id"] == "lt_4_4":
        v6_index_entries.append({
            "lt_id":          "lt_4_5",
            "lt_name":        LT_4_5_META["lt_name"],
            "competency":     LT_4_5_META["competency"],
            "knowledge_type": LT_4_5_META["knowledge_type"],
            "band_range":     LT_4_5_META["band_range"],
            "summary":        LT_4_5_META["summary"],
        })

v6_index = {
    "meta": {
        "schema_version": v5_index["meta"]["schema_version"],
        "generated_date": "2026-04-24",
        "lt_count": len(v6_index_entries),
    },
    "learning_targets": v6_index_entries,
}

with open(INDEX_OUT, "w") as f:
    json.dump(v6_index, f, indent=2, ensure_ascii=False)

print(f"Wrote {INDEX_OUT} ({len(v6_index_entries)} LTs)")
