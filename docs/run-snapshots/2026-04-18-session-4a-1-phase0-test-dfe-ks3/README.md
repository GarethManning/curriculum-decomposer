# Phase 0 flat-PDF primitive test — DfE KS3 Maths (2026-04-18)

Frozen artefacts from Session 4a-1 Step 4. First of the two PDF-source
tests for the `flat_pdf_linear` primitive sequence. Simple/linear case:
full-document extraction, no page_range, no section_heading.

- **Source:** `https://assets.publishing.service.gov.uk/media/5a7c1408e5274a1f5cc75a68/SECONDARY_national_curriculum_-_Mathematics.pdf`
- **Publication:** UK DfE / statutory National Curriculum in England —
  Mathematics programme of study, Key Stage 3.
- **Source type (detected):** `flat_pdf_linear`
- **Scope:** `source_reference` only (full-document extraction).
- **Sequence:** `fetch_pdf_file → extract_pdf_text → normalise_whitespace → content_hash`
- **Content hash:** `260154d50a6016f499e866d6e6e71c4f90dae7ac1c8f7800eeb552fa8336bafa`
- **Detection hash:** `82db12aa4671a79871cfa6e1cddef86b5aa4201bc895b0342a56f40c9c28193f`
- **Content size:** 15,737 chars across 282 lines.
- **pdfplumber version:** 0.11.9.

## Files

- `manifest.json` — full acquisition manifest (v0.2.0 schema).
- `_detection.json` — type-detector output.
- `content.txt` — normalised UTF-8 text of the full PDF.

## Expected vs acquired

Expected: KS3 Maths programme of study — purpose/aims/attainment
front-matter, plus the six subject-content strands (Working
mathematically, Number, Algebra, Ratio/proportion/rates of change,
Geometry and measures, Probability, Statistics).

Acquired content contains all seven sections at the expected line
positions (see `grep -n '^(Number|Algebra|Ratio|Geometry|Probability|Statistics|Working)'`):
Working mathematically (L64), Number (L110), Algebra (L150),
Ratio/proportion (L192), Geometry (L214), Probability (L256),
Statistics (L266). Front matter (purpose of study, aims, attainment
targets) precedes the strand content as expected for a full-document
extraction. No scope exclusions requested; pdfplumber's natural
full-document output is faithful to the source.

## Primitive behaviour notes

pdfplumber handled the single-column DfE layout cleanly. No
`pdfplumber_warnings` recorded. No encoding_detection primitive in the
sequence — pdfplumber emits UTF-8 directly.
