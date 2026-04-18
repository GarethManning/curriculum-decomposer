# Session 4a-3 Step 6 — Ontario DCP Grade 7 History (JS-rendered)

- **Source:** `https://www.dcp.edu.gov.on.ca/en/curriculum/elementary-sshg/grades/g7-history/strands`
- **Source type:** `js_rendered_progressive_disclosure`
- **Schema version:** 0.4.0 (extended with `dom_hash`)
- **Run date:** 2026-04-18
- **Runner:** `scripts/phase0/run_ontario_dcp_g7_history.py`

## Primitive sequence

`fetch_via_browser → dom_hash → extract_css_selector → verify_raw_extraction → normalise_whitespace → verify_normalised_extraction → content_hash`

No click sequence — Ontario DCP's `/strands` route renders all six
overall expectations and their FOCUS ON tags inline after
`networkidle`. Consent modal absent. See
`docs/diagnostics/2026-04-18-ontario-dcp-investigation.md`.

## Hashes

- `content_hash`: `3587c48c97efc32b3a2830ead58ba448fe843e63c2ca97d62408a046671ec4e4`
- `dom_hash`: `f158ec221b2aef79fb594fc0144ff9e3f901bb3c6a7eb7504470bf2a0bf0ca38`

## Verification verdicts

Both automated passes `clean`:

- `verify_raw_extraction`: whitespace_runs 0.
- `verify_normalised_extraction`: character_doubling 0.0,
  repeated_bigram 0.196 (english_confident), empty_line_ratio below
  threshold, completeness not flagged for HTML.

## Triangulated cross-validation (Ontario K-8 PDF as ground truth)

Ground truth: `docs/run-snapshots/2026-04-18-session-4a-2b-ontario-g7-history/content.txt`.

### Check A — structural plausibility

- Strand A heading ("New France and British North America, 1713–1800")
  present.
- Strand B heading ("Canada, 1800–1850: Conflict and Challenges")
  present.
- 6 `FOCUS ON` markers counted (expected 6).
- All six overall-expectation codes (A1, A2, A3, B1, B2, B3) present
  as headings.

**Verdict: PASS.**

### Check B — overall-expectation title match vs PDF

| Code | PDF title | DCP title | Match |
| --- | --- | --- | --- |
| A1 | Application: Colonial and Present-day Canada | Application: Colonial and Present-day Canada | **exact** |
| A2 | Inquiry: From New France to British North America | Inquiry: From New France to British North America | **exact** |
| A3 | Understanding Historical Context: Events and Their Consequences | Understanding Historical Context: Events and Their Consequences | **exact** |
| B1 | Application: Changes and Challenges | Application: Changes and Challenges | **exact** |
| B2 | Inquiry: Perspectives in British North America | Inquiry: Perspectives in British North America | **exact** |
| B3 | Understanding Historical Context: Events and Their Consequences | Understanding Historical Context: Events and Their Consequences | **exact** |

**Verdict: STRONG PASS — 6/6 exact.**

### Check B2 — FOCUS ON tag comparison

| Code | PDF FOCUS ON | DCP FOCUS ON | Match |
| --- | --- | --- | --- |
| A1 | Continuity and Change; Historical Perspective | Continuity and Change; Historical Perspective | **match** |
| A2 | Historical Significance; Historical Perspective | Historical Significance; Historical Perspective | **match** |
| A3 | Historical Significance; Cause and Consequence | Historical Significance; Cause and Consequence | **match** |
| B1 | Continuity and Change; Historical Perspective | Continuity and Change; Historical Perspective | **match** |
| B2 | Historical Significance; Historical Perspective | Historical Significance; Historical Perspective | **match** |
| B3 | Historical Significance; Cause and Consequence | Historical Significance; Cause and Consequence | **match** |

**Verdict: STRONG PASS — 6/6 match.**

### Check C — volume sanity

- Extracted content: **3,706 chars**.
- Threshold: 5,000–50,000 chars.
- Outcome: **below threshold.**

**Verdict: FLAG — documented scope caveat, not extraction failure.**

The `/strands` route carries the six overall expectations plus FOCUS
ON tags plus the Specific Expectations section **headings** (no
content beneath them — per-expectation specific-expectations text
lives on SPA-routed sub-pages `/a/a1` … `/b/b3`). At the `/strands`
scope, 3,706 chars is the correct full volume. The PDF's 46,227 chars
is a superset covering overall expectations AND specific expectations;
Check B and Check B2 are the fair comparisons.

Check C's threshold is calibrated from 4a-2b's Ontario PDF run (≈ 2.1
kchars/page × 22 pages = 46k), which is the wrong reference for this
JS scope. Future work: allow the primitive sequence to declare a
scope-appropriate volume range (tracked, not actioned this session).

## Session-level outcome classification

**Pass with notes.**

Rationale: Checks A, B, and B2 pass cleanly and are the load-bearing
cross-validation claims; Check C flags a scope-calibration issue that
is not an extraction bug. Same pattern as Session 4a-2b's own
Ontario K-8 PDF test (which was classified pass-with-notes for a
Check C recalibration).

## Files

- `manifest.json` — full acquisition manifest with primitive trace.
- `content.txt` — normalised UTF-8 extracted text.
- `rendered_state.png` — full-page screenshot from the browser
  primitive (fixed viewport 1280×720), archived as rendered-state
  audit evidence.
- `_detection.json` — detector output (JS classification).
- `spot-check.txt` — `scripts/phase0/spot_check.py` output.

## Next session hooks

- Structured cross-validation record inside `verification_trace`:
  Session 4a-3 Step 9 adds a `manual_cross_validation` entry with the
  four-column PDF/DCP/title-match/FOCUS-ON table encoded as JSON.
- Volume-threshold scope-awareness: future session.
