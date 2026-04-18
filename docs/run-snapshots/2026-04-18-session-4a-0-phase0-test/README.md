# Phase 0 first-primitive test — Common Core 7.RP (2026-04-18)

Frozen artefacts from Session 4a-0 Step 4, re-emitted under the v0.2.0
manifest schema during Session 4a-1 Step 1 cleanup (content unchanged —
same `content_hash` `c48297f2…0162d3`).

- **Source:** `https://www.thecorestandards.org/Math/Content/7/RP/`
- **Source type (detected):** `static_html_linear`
- **Scope:** `css_selector='article section.content'`
- **Sequence:** `fetch_requests → encoding_detection → extract_css_selector → normalise_whitespace → content_hash`
- **Content hash:** `c48297f2cd0daecc97afc2a861deb036940f1799919b90e3ed3b7a60ec0162d3`
- **Detection hash:** `d067e2827c868ae47417dc8e9ef1c2ace340365cff1d72cf3ce4784570d2d1d4`
- **Content size:** 1,799 chars
- **Encoding:** detected `utf_8` (declared `ISO-8859-1`; no failure)
- **Manifest schema version:** `0.2.0` (adds `detection_hash`; replaces `scope_acquired.first_line` with structured `verification_excerpt`).

## Files

- `manifest.json` — full acquisition manifest
- `_detection.json` — type-detector output
- `content.txt` — extracted 7.RP cluster text
- `spot-check.txt` — output of `scripts/phase0/spot_check.py`

## Expected vs acquired

Expected: the 7.RP cluster heading ("Analyze proportional relationships…"), 7.RP.A.1, 7.RP.A.2 + sub-standards a/b/c/d, 7.RP.A.3. Excluded: navigation, footer, unrelated clusters, site chrome.

Acquired content matches expectation. `<i>` tags in embedded examples surface as separate lines — not a defect; the substance is preserved and downstream `source_bullets` extraction in Phase 1 already handles this pattern.
