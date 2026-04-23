# Critique: REAL Wellbeing Scope & Sequence (20260422)
## Five expert personas stress-test the document

*Prepared for Gareth Manning, 22 April 2026, as a first-pass review of the scope-and-sequence output. Personas speak in their own register. Where they disagree with the document, they disagree with specifics; where they agree, they say so briefly and move on.*

---

## Persona 1 — Head of Pedagogy, international continuum school

**Headline verdict:** Rigorous on logic; underweight on translatability. I'd respect it; I'd send it back for a second pass before approving.

**What works.** The three-logic structure — hard prerequisite, soft scaffold, experiential readiness — is epistemically honest in a way I rarely see. Most scope-and-sequence documents collapse everything into "here is the order" without differentiating gating from enriching. The LT 6.1 cascade analysis is the single most useful piece in the document: it names the highest-leverage delivery-quality risk explicitly, which is what operations leaders need. The session-flag carry-forward — teacher-review flags from KUD authoring surfaced inside the sequence — shows the document is read against its own history.

**What doesn't.** Vertical coherence is asserted at "no breaks" without showing the working. The claim that "analytical sophistication genuinely increases" is spot-checked on LT 6.2 only; a proper audit would walk every T2 LT band-by-band. The "ongoing observation throughout Band X" recommendation for six T3 LTs is operationally hand-wavy — I cannot take it to a new teacher. "Run LT 3.2 as ongoing observation" means nothing without specifying frequency, recording medium, summative evidence threshold, and observer calibration. The Band D gap (11 LTs without a named unit) is surfaced but the recommendation is "audit" rather than a concrete unit proposal. The document switches registers between strategic and tactical without flagging which sections are for which audience.

**Specific suggestions.**
1. Add a vertical coherence audit section: for every T2 LT, name the progression lever at each band transition and show it actually shifts.
2. Replace "ongoing observation" with a concrete observation calendar template: one table showing which T3 LT is the "foreground" for each 4–6 week window of the school year, alongside the continuous-background observation.
3. Turn the Band D gap into a named unit proposal. The document already implies a "Designed Environments" Term 1 or Term 4 unit for Band D covering LT 8.2 D + LT 8.1 D + LT 4.3 D anchored in existing LT 6.1 D content from Architects of Agency — commit to it.
4. Split the artefact into two deliverables: a 10-page strategic overview for leadership, and six band-level planning packs for classroom teams.

---

## Persona 2 — Grade 3 classroom teacher, new to REAL this year, teaching Band B

**Headline verdict:** I cannot use this to plan Monday's lesson. I respect it, but it is written for someone senior to me.

**What works.** The Band B section lists the LTs I'm responsible for, which is more than I had before. The prerequisite map tells me I shouldn't teach LT 4.2 B before LT 6.2 B — I wouldn't have guessed that. The specialist-delivery flag tells me LT 4.2 B isn't my job to deliver alone.

**What doesn't.** I don't know what "ongoing observation throughout Band B" means for my weekly timetable. Do I schedule a wellbeing block? Where do my observation notes go? How does this feed into reporting? The document tells me LT 6.1 B is a hard prerequisite for LT 4.2 B but doesn't tell me what that sounds like in a Year 3 classroom. The instruction to "pick a specific repair-routine variant and maintain consistency across subsequent bands per teacher-review flag" tells me what to do but not who owns the decision. Acronyms are undefined — I know what KUD means; I don't know what D2R is. No lesson-length guidance at Band B.

**Specific suggestions.**
1. Add a Band B starter pack appendix: a week-by-week rough map for a full year showing where each LT fits into a plausible calendar. Even a single sample term would help enormously.
2. Add a glossary at the front. D2R, Reflection 360, Light Dragon capstone, Strive — one line each.
3. For each T3 LT at each band, specify observation frequency, recording tool, and summative-evidence threshold.
4. Add ownership for cross-band decisions like "pick a repair-routine variant" — is it a curriculum lead, a head of wellbeing, or the band team collectively?

---

## Persona 3 — School Principal

**Headline verdict:** Strong on what to teach; weak on what it costs and how to staff it.

**What works.** Specialist-delivery requirements are flagged. The LT 4.2 Band D specialist-contracting deadline is surfaced as urgent. The Band E weekly-time concern is raised.

**What doesn't.** No cost estimate — how many specialist hours per year across Bands B–F for C4? That's a budget question and the document doesn't answer it. No staffing pattern — Diana co-teaches LT 4.1 and LT 4.3, but is she the specialist for both at Bands C–F? Is the model "train internal, contract external, or both"? Not resolved. No timetable implications — Band E "may need more than 90 minutes" is a flag, not a proposal. Parent communication is mentioned once (LT 4.1 A body-part names) but not structured into a year-round schedule. No mid-entry-student pathway, despite high student mobility at REAL being flagged in session 2.

**Specific suggestions.**
1. Add an operational appendix: specialist-hours estimate per band per year; named responsible adults for each specialist requirement; a parent-communication schedule.
2. Add a mid-entry-student policy. For each band, specify the minimum prerequisite content a joining student must have (or be given in catch-up).
3. Add a reporting-and-assessment view: what actually goes on a report card at Band B? Band D? Band F? The document produces evidence types but doesn't resolve how they become formal school records.
4. Propose a Band E figure, not a flag — "120 minutes weekly" or "two blocks of 75 minutes" or similar, so the flag has a resolution.

---

## Persona 4 — AI-in-education product lead (builds tools on top of curriculum frameworks)

**Headline verdict:** Partially machine-usable. Good semantic content; weak structural format. I'd need a parser pass before feeding this to any downstream AI tool.

**What works.** Prerequisite relationships are explicitly typed (hard / conceptual accelerator / soft enabler / sibling) — that's rare and useful. LT identifiers are consistent throughout. The architecture summary (1 T1 / 12 T2 / 6 T3 / 1 hybrid) gives a programmatic profile that downstream outputs can be checked against. The priority-actions section has clear imperative form that another AI can convert to task lists.

**What doesn't.** The document is a single markdown file. Relationships are asserted in multiple places (Section 0 table, Section 2 table, Section 3 prose) without a single canonical source. If one drifts from another in a future edit, there is no way for an AI to know which to trust. Band scoping of relationships is inconsistent — "LT 6.1 C+ → LT 4.2 C+" — does "C+" mean "at and above Band C"? Usually yes, but Section 3 prose occasionally reads as band-specific, and a parser has to guess. Cross-references to unshared session documents ("per teacher-review flag") are unresolvable for any downstream AI that doesn't have those handoffs. No stable IDs for flags — "LT 4.3 Band E psychological safety flag" is a content description, not an ID, so no downstream tool can track whether it's been addressed. No versioning.

**Specific suggestions.**
1. Extract a `relationships.yaml` companion. Every prerequisite as a machine-readable row: `{from: LT_6.1, to: LT_4.2, type: hard, from_band: C, applies_to_bands: [C,D,E,F], rationale: "..."}`. Prose document is human-readable; YAML is canonical; downstream AI consumes the YAML.
2. Assign stable IDs to every flag and recommendation: `FLAG-C-CASCADE-001`, `REC-BAND-D-UNIT-001`. Downstream tooling can then track status (open / addressed / deferred) over time.
3. Add a "machine view" JSON appendix: the document's content compressed to a structure suitable for a unit-planner AI or rubric-generator to consume without prose parsing.
4. Add explicit "this document depends on" and "this document is depended on by" metadata at the top. What inputs produced it; what outputs will consume it.
5. Version it: `v1.0 (2026-04-22)` with a changelog section that future edits append to.

---

## Persona 5 — Curriculum ontologist / knowledge engineer

**Headline verdict:** The underlying conceptual architecture is unusually well-specified. The artefact is not. There is a graph here trying to escape from the prose.

**What works.** The three-knowledge-type taxonomy (T1/T2/T3) is clear and consistently applied. The four-relation prerequisite typing will hold up under scrutiny. Cross-competency cross-references (LT 8.3 Know via LT 6.1 + LT 8.2 + LT 1.3 + LT 5.1) are explicit — this is graph-shaped content.

**What doesn't.** The document presents a graph as a linear list. There is a dependency graph, a developmental-axis structure, and a typed-edge overlay — none are shown visually. No formal definition of "conceptual accelerator" vs. "soft enabler" beyond the skill's default; a downstream auditor cannot verify where the line falls. Cross-framework dependencies (LT 1.2 F → Humanities Identity, Power & Representation) are real but implicit. The T3 category is ontologically under-specified: is LT 8.3's "cross-platform" requirement equivalent to LT 1.1's "cross-situation" requirement? They look similar but the evidence structure differs substantially.

**Specific suggestions.**
1. Produce a DOT-format or GraphML dependency graph as a companion artefact. Nodes: LTs (sized by centrality, coloured by T-type). Edges: prerequisites (line style = hard / conceptual / soft). Render once per band to show how relationships activate as bands progress.
2. Add formal definitions for each relationship type with acceptance criteria — when is a relationship "hard" vs. "conceptual accelerator"? Write the test.
3. Treat cross-framework dependencies as first-class. A separate section listing LTs whose content depends on other subjects (Humanities, Science) so those interfaces are visible.
4. Sub-taxonomise T3: cross-situation (LT 1.1, 3.2, 7.2), cross-platform (LT 8.3), cross-relationship (LT 1.2, 5.2). Each has a different observation-design implication.

---

# Synthesis: three highest-leverage improvements

Three themes recur across all five personas.

**(1) Produce companion artefacts, not a bigger document.** The 30-page prose file is the wrong shape for any single reader. Split into: a strategic summary for leadership; six band-level planning packs for teachers; a `relationships.yaml` for downstream AI; a rendered dependency graph. The prose becomes an index rather than the product.

**(2) Operationalise the T3 recommendation.** "Ongoing observation throughout Band X" is conceptually correct but cannot be implemented as written. Build a T3 observation calendar template: frequency, recording medium, summative-evidence threshold, observer calibration approach, for each T3 LT at each band.

**(3) Commit on Band D.** The document flags 11 Band D LTs without named units and recommends "audit". Personas 1, 2, and 3 all want a concrete unit proposal. The strongest candidate — a Term 1 or Term 4 "Designed Environments" unit covering LT 8.2 D + LT 8.1 D + LT 4.3 D leveraging LT 6.1 D from Architects of Agency — is already implied by the logic. Name it and scope it.

---

# On visualisation

The document's logic is defensible. Its format is not. Five visualisations would raise utility sharply; the first two are the highest-leverage.

**V1 — LT × Band matrix (single page).** A 19-row × 6-column grid. Rows are LTs in C1–C8 order; columns are Bands A–F. Each cell is coloured by knowledge type (T1 / T2 / T3 / hybrid / N/A) and annotated with the progression lever used at that band transition. This is the single most-missed view in the current document. It shows the whole framework on one page. A head of pedagogy gets more from this image than from reading thirty pages of prose.

**V2 — Prerequisite dependency graph.** Nodes are LTs, sized by centrality (LT 6.1 largest). Edges are typed prerequisites — solid = hard, dashed = conceptual accelerator, dotted = soft enabler. Render one overview graph, then six band-specific renders showing which edges activate at each band. The "LT 6.1 cascade" concept becomes visually obvious and the Band C pressure point lights up without needing to be described.

**V3 — Band timeline / term map.** For each band, a grid of school weeks (30–36 wide) showing which LTs are foregrounded in which weeks. T2 LTs as blocks; T3 LTs as continuous bars with darker shading during foreground weeks. Existing REAL units (Architects of Agency, Becoming, Light Dragon capstone) overlay as framed regions. This is the answer to Persona 2's "what do I do Monday" problem.

**V4 — Specialist-delivery swimlane.** Horizontal timeline with three lanes: classroom teacher, Diana (counsellor co-teach), external specialist. Each band's specialist requirements plotted in the appropriate lane with hour estimates. Operational cost becomes visible at a glance. Answers Persona 3's staffing question.

**V5 — Risk heat map.** A 19-LT × 6-band grid coloured by risk level from the document's own flags. Dark red for prerequisite-cascade risks (LT 6.1 C), orange for contracting-deadline risks (LT 4.2 D), yellow for observer-calibration risks (T3 at E–F), pale for routine. Turns scattered flags into a single prioritised picture.

All five can be generated from the relationship data already in the document. I'd suggest producing V1 and V2 first — between them they solve most of what all five personas raised.

---

*If you want, I can produce V1 (the matrix) and V2 (the dependency graph) as the next step. They're both buildable directly from the data in the current scope-and-sequence output. V1 is the faster of the two and probably the higher-leverage; V2 is more elegant but takes more design care to render legibly with 19 nodes and the typed-edge overlay.*
