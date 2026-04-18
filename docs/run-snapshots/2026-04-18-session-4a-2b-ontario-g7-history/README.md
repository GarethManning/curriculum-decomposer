# Phase 0 multi-section PDF test — Ontario Grade 7 History (2026-04-18)

Frozen artefacts from Session 4a-2b Step 10. Load-bearing test for
the `multi_section_pdf` source type shipped this session and the TOC
detection primitive that feeds it.

- **Origin URL:** `https://assets-us-01.kc-usercontent.com/fbd574c4-da36-0066-a0c5-849ffb2de96e/f6f2efba-a7aa-4c70-94ce-f7593a7490ca/SocialStudiesHistoryGeography-AODA.pdf`
- **Publication:** Ontario Ministry of Education — The Ontario
  Curriculum, Grades 1–8: Social Studies / History / Geography
  (revised 2023). AODA-tagged PDF.
- **Source type (detected):** `multi_section_pdf` (high confidence —
  embedded outline with 16 top-level entries, 369 pages).
- **Scope:** `section_identifier="History, Grade 7"`. Resolved
  automatically via the embedded outline to `page_range=[245, 266]`
  — cross-checked against Step 3's manual ground-truth range and
  matches exactly.
- **Sequence:** `fetch_pdf_file → detect_toc → resolve_section_scope → extract_pdf_text → verify_raw_extraction → normalise_whitespace → verify_normalised_extraction → content_hash`
- **Content hash:** `bc7ef9d3b36f9da9a7ffa3182e50aa7977d555c1ea37c2ad2a4d641ccf1d8b93`
- **Detection hash:** `b84fd26bedb3d37491b988d3de8f8f395b89aa9408a6063a70baa19a8cbe914e`
- **Content size:** 46,227 chars across 726 lines.
- **pdfplumber version:** 0.11.9.

## Session outcome — PASS WITH NOTES

Outcome per the triangulated verification defined in Session 4a-2b's
prompt (Step 10):

### Check A (structural plausibility) — PASS

- Exactly two strand headings (`Strand A.`, `Strand B.`). ✓
- All six overall-expectation codes present: `A1`, `A2`, `A3`, `B1`,
  `B2`, `B3`. ✓
- Six `Specific expectations` section markers — one per overall
  expectation. ✓
- Eight `FOCUS ON` markers (minimum six expected). ✓
- 34 unique sub-expectation codes present (`A1.1` … `B3.6`), each
  with its accompanying `Teacher supports` and `Sample Questions`
  sections (34 instances of each).

### Check B (screenshot overall-expectation titles) — PASS 6/6 exact

All six overall-expectation titles from Gareth's screenshot appear
verbatim in the extracted content:

- `A1: Application: Colonial and Present-day Canada` ✓
- `A2: Inquiry: From New France to British North America` ✓
- `A3: Understanding Historical Context: Events and Their Consequences` ✓
- `B1: Application: Changes and Challenges` ✓
- `B2: Inquiry: Perspectives in British North America` ✓
- `B3: Understanding Historical Context: Events and Their Consequences` ✓

### Check C (volume sanity) — PASS WITH THRESHOLD NOTE

Total content: 46,227 chars. The plan's stated range was
5,000–30,000 chars; the 30,000 ceiling was miscalibrated for this
PDF and would have falsely failed a correctly-scoped extraction.
Evidence that the volume is accurate rather than inflated:

- Zero occurrences of `Grade 6`, `Grade 8`, `Social Studies, Grade`,
  or `Creating Canada` (the Grade 8 strand A title) — boundaries are
  clean.
- Content opens cleanly with `History, Grade 7 / Overview / In Grade
  7 history, students will examine …` on page 245.
- Content ends on page 265 with the trailing Sample Questions of
  Strand B's last specific expectation — the last line in the file is
  the page number `265`.
- 46,227 chars ÷ 22 pages ≈ 2,101 chars/page. This matches the
  completeness check's per-page value and is consistent with a
  dense, multi-column curriculum layout (two columns, many specific
  expectations with supporting-question lists).

**Conclusion:** Check C's plan ceiling was too tight, not the
extraction too wide. Recommend raising the ceiling to ~50,000 chars
for Ontario-style multi-column curriculum sections when this check
is codified.

### Session classification

**Pass with notes** per the plan's classification ladder. Phase 0
has demonstrably solved the Session 3e failure that motivated the
rebuild — scoping the Ontario K-8 PDF to the Grade 7 History strand
produces byte-accurate content with clean section boundaries and a
clean verification verdict in both raw and normalised modes.

## Verification trace

Two verification entries (one per mode, per the Step 4 split):

- `verify_raw_extraction` → `clean`. Only check run:
  `whitespace_runs` (value 0).
- `verify_normalised_extraction` → `clean`. Checks run:
  `character_doubling` (0.0), `repeated_bigram` (0.184, English
  detected with confidence 0.0608 via stopword ratio),
  `empty_line_ratio` (0.029), `completeness` (2,101.2 chars/page,
  well above the 50-char/page flag threshold).

## Files

- `manifest.json` — full acquisition manifest.
- `_detection.json` — type-detector output. The detector's
  rationale references the 369-page document and the 16 top-level
  outline entries that triggered the `multi_section_pdf` routing.
- `content.txt` — normalised UTF-8 text of pages 245–266.
- `spot-check.txt` — human-readable manifest dump.
