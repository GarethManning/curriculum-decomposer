# Minnesota SEL Transform — Open Questions · 2026-07-06 · v1

Items requiring human judgement or follow-up. None block the deliverable; all are flagged for Kari / Ivana / Gareth review.

## Extraction

1. **One benchmark excluded as a fragment.** `MN.SOA.LG3.X-X.10` extracted as `"civic groups, in defining and addressing the common good."` with no grade band. The Social Awareness LG3 Grades 9–12 table on that page interleaved during extraction (the raw reading-order text there is also garbled). Excluded from the target set rather than decomposed from a partial. **Action:** manually re-read that page of `mn-sel-social-awareness-MDE073514.pdf` and add the full benchmark + grade band. Net: 201 of 202 extracted benchmarks carried into targets.

2. **Source punctuation anomaly.** `MN.RS.LG2.4-5.07` ends `"…peer mediation or adult assistance, etc.)"` — an unbalanced parenthesis in the published PDF (not a truncation; the guard flagged it). Resolved during decomposition by rephrasing the derived split; noted for awareness.

## Decomposition (Step 2 — one construct per target)

3. **Coordinate-verb boundary calls.** Separable coordinate verbs were split (recognize/label, identify/apply, describe/implement, monitor/adjust, receive/act-on, balance/prioritize, analyze/implement). Tightly-coupled verbs naming **one integrated capability** were kept together, by design:
   - `MN.RDM.LG2.9-12.14` — "Analyze and evaluate evidence…" kept as one appraisal construct.
   - `MN.RS.LG3.6-8.11` — "de-escalate, defuse, and resolve" kept as one conflict-resolution skill.
   - `MN.SM.LG1.4-5.08` — "Adapt for and overcome obstacles" kept as one perseverance construct.
   These boundary calls are reviewable; a stricter reading would split them.

4. **No benchmark fully resisted decomposition.** All 34 composite benchmarks split cleanly into atomic targets (235 targets from 201 benchmarks; 68 derived, 167 pass-through).

## Tagging (Step 3)

5. **Ambiguous CASEL fits → secondary tags.** 32 targets carry a secondary CASEL competency where a benchmark genuinely spans two (e.g., Self-Awareness responsibility items touching Responsible Decision-Making; Social-Awareness collaboration items touching Relationship Skills). Primary CASEL is authoritative (= the source document); **secondaries are Opus judgement — confirm.**

6. **Social Thinking strategy links are conservative, illustrative suggestions.** Drawn from a controlled vocabulary (names only, no teaching content), all marked PROPOSED. Many targets have none where nothing fit cleanly. **Kari to validate, correct, and expand.** Assumed licence for vocabulary use per brief; no Social Thinking teaching content was scraped or reproduced.

7. **Developmental band = orientation mapping only.** `developmental_band` is a 1:1 orientation of Minnesota's own grade bands (K–3→Band 1 … 9–12→Band 4). Neutral labels, no external framework's scheme. If LearnOS adopts a canonical band system, remap. Never a placement rule.

## Grade bands

8. **No missing grade bands** beyond the single excluded fragment — all 201 usable benchmarks carried an explicit MN grade band.
