# Phase 0 regression — Common Core 7.RP under schema 0.3.0

Re-acquisition run under Phase 0 schema 0.3.0 (Session 4a-2a Step 6)
to verify that the new mandatory `verify_extraction_quality` step and
the coordinate-dedup primitive do not regress existing working
extractions.

- **Scope:** unchanged from Session 4a-0 — `url` +
  `css_selector="article section.content"`.
- **Sequence:** `fetch_requests → encoding_detection → extract_css_selector → normalise_whitespace → verify_extraction_quality → content_hash`
  (Session 4a-0 sequence + `verify_extraction_quality`).
- **Stored content hash (4a-0):**
  `c48297f2cd0daecc97afc2a861deb036940f1799919b90e3ed3b7a60ec0162d3`.
- **New content hash (4a-2a):**
  `c48297f2cd0daecc97afc2a861deb036940f1799919b90e3ed3b7a60ec0162d3`
  — **identical**. Schema-bump is byte-clean for this source.
- **Verification verdict:** `clean`.
- **phase0_version:** 0.3.0.

No regression.
