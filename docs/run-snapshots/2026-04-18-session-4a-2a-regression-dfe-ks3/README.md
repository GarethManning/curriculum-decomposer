# Phase 0 regression — DfE KS3 Maths under schema 0.3.0

Re-acquisition run under Phase 0 schema 0.3.0 (Session 4a-2a Step 6)
to verify that the new mandatory `verify_extraction_quality` step does
not regress the PDF extraction that was already clean under 4a-1.

- **Scope:** unchanged from Session 4a-1 — `source_reference` URL only,
  no `page_range` / `section_heading`, no `pdf_dedup_coords`.
- **Sequence:** `fetch_pdf_file → extract_pdf_text → normalise_whitespace → verify_extraction_quality → content_hash`
  (Session 4a-1 sequence + `verify_extraction_quality`).
- **Stored content hash (4a-1):**
  `260154d50a6016f499e866d6e6e71c4f90dae7ac1c8f7800eeb552fa8336bafa`.
- **New content hash (4a-2a):**
  `260154d50a6016f499e866d6e6e71c4f90dae7ac1c8f7800eeb552fa8336bafa`
  — **identical**.
- **Verification verdict:** `clean`.
- **phase0_version:** 0.3.0.

No regression. The DfE KS3 Maths PDF does not exhibit the coordinate-
level doubling that the AP CED does, so the fast path
(`extract_pdf_text`) remains appropriate for this source. The dedup
opt-in flag is not set.
