# Minnesota SEL Target Library — Repair Log · 2026-07-06 · v2

Branch: `learnos-minnesota`. **Status: COMPLETE.** Executed `learnos-target-repair-brief-2026-07-06-v1.md` end to end, governed by `learnos-measurement-foundations-2026-07-06-v3.md` (authority where the brief is silent).

- **Input:** `mn-sel-targets-2026-07-06-v1.json` (235 targets)
- **Output:** `mn-sel-targets-2026-07-06-v2.json` (**254 targets** = 234 Minnesota-derived + 20 integrative) + regenerated markdown + this log
- **Transform:** `minnesota-sel/repair_targets.py` (per-target judgement authored in session on Opus; applied deterministically so provenance is exact by construction)

## Model discipline — as run

All five passes and the verification ran **in-session on Opus (Claude Code subscription)**. The brief marks Pass 5 and the markdown regeneration for Sonnet; both ran on Opus instead. This is the same authorised deviation logged in the v1 run: the account's Anthropic API credit is exhausted (every metered call returns `400: credit balance too low`), so no `/model` switch to a metered Sonnet call was possible. Pass 5 is a deterministic regex sweep and the markdown is a deterministic render — running them on Opus is a cost/model deviation, not a quality one. No API tokens billed.

---

## Pass 1 — Re-split by assessability (not grammar)

Applied the corrected single-construct test to all **34 split groups (68 derived targets)**: *split only if an external observer can gather distinct evidence for each element; where one element is the sole observable evidence of the other (recognize/label class), remerge onto the observable verb.*

- **Remerged: 1.** `MN.SA.LG1.K-3.01` "Recognize and label their emotions and feelings" → single target **"I can name my emotions and feelings"** (anchored on the observable verb, *label*). *Recognize* is covert; naming/labeling is its only observable evidence, so the two collapse to one instrument. The unobservable element (whether the student **recognized** unprompted) is captured by the **support dimension** of the event ladder, not by a separate target (foundations §2–§3). `-t02` dropped; `-t01` retained as the merged target, provenance intact.
- **Kept split: 33.** Every other pair joins two **separately assessable** verbs — identify/apply, monitor/adjust, describe/implement, receive/act-on, balance/prioritize, analyze/implement, define/recognize-examples, identify/execute, take-turns/share, etc. In each, neither element is the sole evidence of the other (the paired verbs sit on different channels or name genuinely distinct performances), so distinct evidence is gatherable → split stands.

**Boundary calls re-examined (all three kept as single integrated constructs):**

| Benchmark | Verbatim | Ruling |
|---|---|---|
| `MN.RDM.LG2.9-12.14` | "Analyze and evaluate evidence, arguments, claims, and beliefs…" | **Single.** *Analyze* and *evaluate* form one critical-appraisal act; you cannot evidence analyzing the evidence distinctly from evaluating it in a real appraisal task. |
| `MN.RS.LG3.6-8.11` | "…de-escalate, defuse, and resolve differences." | **Single.** Three near-synonymous facets of one conflict-resolution performance; no distinct evidence per verb. |
| `MN.SM.LG1.4-5.08` | "Adapt for and overcome obstacles by demonstrating perseverance." | **Single (weakest of the three).** Ruled one perseverance construct; a stricter reading could separate *adapt* from *overcome*, but in a live obstacle they co-occur as one persistence performance. Flagged as the most reviewable ruling. |

---

## Pass 2 — Canonical I-can form

Every target rewritten to canonical schema form: **"I can …"**, present tense, one observable verb, no parentheses, no inline examples / "such as" / "e.g.", no bare comparatives, no third-person subject. Minnesota vocabulary preserved wherever compatible. Provenance untouched — `source_benchmark_id` and `source_verbatim` carry forward on **100% (234/234)** of MN targets.

- **Rewritten (modality `proposed`): 157** — material change (verb swap off `understand`/`know`/`appreciate`/`develop`/`recognize`/`realize`; stripped parentheses/examples; fixed vague modifiers; folded/removed non-atomic qualifiers).
- **Already-canonical (modality `decided`): 77** — pass-throughs whose verbatim needed only the mechanical "I can" prefix + first-person rendering.
- **All 68 derived / remerged targets → `proposed`** (re-phrased on split, clinician confirms).

**Foundations-driven judgement (brief silent):** support-condition qualifiers baked into a few source statements (e.g. "…with assistance from an adult") were **removed from the statement** — the unified support ladder scores *how much support* on every event, so hard-coding a support level into the target would double-count and fix the level (foundations §3). Affected: `MN.SM.LG2.K-3.02`, `MN.SM.LG2.K-3.03`.

---

## Pass 3 — Channel affinity

Each target tagged `explain` (declarative/conceptual — evidenced by explaining), `do` (performance in situation), or `both`. This replaces Type 1/2/3 routing; knowledge types are claim-requirement presets, not target categories (foundations §2–§3, §10).

Distribution: **explain 141 · do 111 · both 2.** The two `both` targets are the collaborative-analysis pair (`MN.SOA.LG3.6-8.07-t01`, `MN.SOA.LG3.9-12.08-t01`) — "work collaboratively with peers to analyze…" requires both the doing (collaboration) and the explaining (analysis).

---

## Pass 4 — Integrative targets (new content)

Authored **20 integrative targets** (5 CASEL competencies × 4 developmental bands) — each a whole-situation performance requiring that competency's components in concert, in language a school SLP would recognize (foundations §8.4 atomistic-fallacy guard). All: canonical I-can form, `channel: do`, `integrative: true`, `modality: proposed`, `strategy_links: []` (left for Kari), and **provenance `source: learnos-integrative`** with an explicit note that there is no Minnesota benchmark. These are the only targets in the corpus without an MN benchmark trace, by design.

---

## Pass 5 — Vague-modifier sweep

Deterministic regex sweep over all 254 final statements for `more`, `better`, `appropriate(ly)`, `effective(ly)`, `complex` (unanchored), `various`, `relevant`, learner-referring `they/their`, parentheses, and example markers. **Zero unresolved hits.** Fixes folded into the Pass-2 rewrites (e.g. `effective→removed`, `various→different`, `complex emotions→difficult/intense-or-mixed`, `a variety of→different`, `foster better→support`). No item flagged unresolvable.

---

## Verification (before commit) — PASS

**Seeded random sample of 15 (seed 20260706):** each target one construct by the assessability test; canonical form compliant; verbatim trace exact to source; channel tag defensible; zero clean-room signatures. **15/15 pass.**

**Full-corpus (all 254):**
- Provenance carry-forward exact (MN targets): **234/234**
- Integrative provenance = `learnos-integrative`: **20/20**
- Modality all valid (`decided`/`proposed`): ✅
- Strategy links all `proposed`: ✅ (none upgraded)
- Channel present & valid on every target: ✅
- Integrative present and grid-complete (5×4, each = 1): ✅ (20/20)
- Clean-room forbidden-signature scan (`real school`, `budapest`, `dragon`, `five-level`, `no_evidence`/`emerging`/`developing`/`competent`/`extending`): **ZERO hits**
- Pass-5 banned-modifier sweep: **0 flags**

**Counts reported (brief requirement):** remerged **1** · kept-split **33** · rewritten **157** · already-canonical **77** · integrative **20**.

---

## Carried-forward open items (unchanged from v1, still for human review)
- Excluded fragment `MN.SOA.LG3.X-X.10` still needs a manual re-read of the source page (not re-introduced here).
- Secondary CASEL tags remain Opus judgement — Kari to confirm.
- Strategy links remain conservative, all `proposed` — Kari to validate and expand.
- Boundary ruling on `MN.SM.LG1.4-5.08` (adapt/overcome) is the most reviewable Pass-1 call.
