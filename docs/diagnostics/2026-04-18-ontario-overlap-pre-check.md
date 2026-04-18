# Ontario K-8 SS/H/G PDF — coordinate-overlap pre-check (Session 4a-2b Step 3)

## Purpose

Before wiring the `multi_section_pdf` primitive sequence, empirically
determine which (if any) PDF pathology from the `KnownPathology` enum
applies to the Ontario K-8 Social Studies / History / Geography AODA
PDF. Findings drive the default dedup configuration for Ontario in
Step 8 and cross-check the automated TOC detection in Step 10.

## Source

- File: `outputs/phase0-test-ontario-g7-history-2026-04-18/_source.pdf`
- Origin URL: `https://assets-us-01.kc-usercontent.com/fbd574c4-da36-0066-a0c5-849ffb2de96e/f6f2efba-a7aa-4c70-94ce-f7593a7490ca/SocialStudiesHistoryGeography-AODA.pdf`
- Size: 5,774,184 bytes, 369 pages, pdfplumber 0.11.9.
- Embedded outline present (pypdf).

## Manual Grade 7 History page range (ground truth)

From the embedded outline:

- `History, Grade 7` section starts at pypdf 0-indexed page 244.
- `History, Grade 8` (next sibling) starts at pypdf 0-indexed page 266.

**Manual page range (1-indexed, inclusive): pages 245–266.**

Verified by extracting text from boundary pages:

- Page 245: first line `"History, Grade 7"`.
- Page 266: last content page, trailing overall-expectation questions
  about the War of 1812 / Durham Report / Irish Catholics.
- Page 267: next section begins (`"History, Grade 8"`).

Step 10 cross-checks the `detect_toc` primitive's automated
resolution against this manual range.

## Coordinate-overlap analysis

Procedure: for five representative pages across the Grade 7 History
section (245, 246, 252, 259, 265), tabulate `page.chars` grouped by
`(round(x0/tol), round(top/tol), text)` and count groups of size ≥ 2.
Separate whitespace-character duplicates from letter duplicates so
whitespace noise at a shared baseline (normal layout artefact) is not
confused with systematic letter overlap.

### Per-page counts (Grade 7 History)

| page (1-indexed) | chars | all_dup_groups (tol=1) | whitespace_dup_groups | letter_dup_groups |
|------------------|-------|------------------------|------------------------|-------------------|
| 245              | 2,435 | 39                     | 39                     | 0                 |
| 246              | 1,077 | 22                     | 22                     | 0                 |
| 252              | 2,838 | 21                     | 21                     | 0                 |
| 259              | 2,865 | 21                     | 21                     | 0                 |
| 265              | 2,584 | 36                     | 36                     | 0                 |

At tolerances 1 and 2: zero letter-level duplications across all five
pages. At tolerance 3, a handful of letter dups appear (3 groups on
pages 245 and 246, 1 on 265), but this is attributable to tolerance-3
collapsing neighbouring distinct glyphs and is not a systematic
pattern.

### Adjacent-same-char-pair ratios

| page | adj_same | adj_total | ratio |
|------|----------|-----------|-------|
| 245  | 39       | 1,668     | 0.023 |
| 246  | 17       | 731       | 0.023 |
| 253  | 20       | 1,518     | 0.013 |
| 259  | 65       | 1,990     | 0.033 |
| 265  | 40       | 1,753     | 0.023 |

Ratios of 1.3–3.3 % are within the normal English range (words like
"book", "see", "letter", "common" naturally produce adjacent-same
pairs). For comparison, the AP CED pre-fix pages produced ratios in
the 10–32 % range.

## Verifier run on full section

Concatenated extraction of pages 245–266 (normal path, no dedup):

- raw chars: 46,206
- normalised chars: 46,206
- `verify_extraction_quality` verdict: **clean**
- All four checks pass. `character_doubling=0.0`,
  `repeated_bigram=0.184`, `whitespace_runs=0`, `empty_line_ratio=0.0`.

## Classification

**Observed pathologies: `[]` (none).**

The Ontario PDF does not exhibit:

- `coordinate_level_footer_overlap` — no letter duplications at
  header/footer baselines.
- `coordinate_level_general_overlap` — no letter duplications in body
  content either.
- `character_stream_doubling` — `extract_text` is clean and
  verify_extraction_quality returns `clean` on the raw extraction.
- `aoda_tagged_content_overlap` — despite the "-AODA" filename, no
  accessibility tagging produces visible overlap in the character
  stream at tol=1 or tol=2.

No new `KnownPathology` enum value required.

## Step 8 configuration

`multi_section_pdf` for Ontario: **dedup off by default**. Baseline
`extract_pdf_text` produces clean output that passes the verifier.
Ontario validates the non-pathology path of the multi-section
primitive.

If a later Ontario section (e.g. Grade 8, Geography) exhibits a
different pattern, re-run this pre-check on that section and update
this memo.
