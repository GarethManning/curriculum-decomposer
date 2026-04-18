# Phase 0 — Acquisition

Phase 0 separates **acquisition** from extraction. It takes a source
reference (URL or local path) plus a structured scope spec, classifies
the source into a supported type, runs the matching primitive sequence,
and emits a manifest plus one or more content text files.

Downstream phases never read raw URLs. They read:

- `manifest.json` — acquisition trace, content hash, detection hash,
  scope requested vs acquired, any user interactions.
- `content.txt` (and siblings) — normalised UTF-8 text.

## Supported source types

| Source type                          | Primitive sequence                                                                                                                                                                                                                                               | Status       |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `static_html_linear`                 | `fetch_requests → encoding_detection → extract_* → verify_raw → normalise_whitespace → verify_normalised → content_hash`                                                                                                                                        | implemented  |
| `flat_pdf_linear`                    | `fetch_pdf_file → (extract_pdf_text \| extract_pdf_text_deduped) → verify_raw → normalise_whitespace → verify_normalised → content_hash`                                                                                                                        | implemented  |
| `multi_section_pdf`                  | `fetch_pdf_file → detect_toc → resolve_section_scope → (extract_pdf_text \| extract_pdf_text_deduped) → verify_raw → normalise_whitespace → verify_normalised → content_hash`                                                                                   | implemented  |
| `js_rendered_progressive_disclosure` | `fetch_via_browser → dom_hash → extract_css_selector → verify_raw → normalise_whitespace → verify_normalised → content_hash`                                                                                                                                     | implemented  |
| `html_nested_dom`                    | pending                                                                                                                                                                                                                                                          | deferred     |

Deferred types raise `Phase0Paused` with a user-in-the-loop request file.

## `flat_pdf_linear` primitive sequence

pdfplumber-backed, deterministic, no model calls.

**Scope.** Required: `source_reference` (URL or local filesystem path).
Optional: `page_range` (`[start, end]` 1-indexed inclusive, or the legacy
string form `"start-end"`); `section_heading` (literal or regex, toggled
by `heading_regex`). When both scope fields are set, `page_range` wins
and `section_heading` is recorded as verification-only in the primitive
trace (`heading_verification.heading_found`).

**No encoding_detection step.** pdfplumber handles PDF encoding
internally and emits UTF-8 strings directly. The absence of
`encoding_detection` from the sequence is deliberate and visible in
the manifest's `primitive_sequence` list.

**Coordinate-level overlaid text (Session 4a-2a, handled).** Some PDFs
render running headers/footers twice at identical `(x0, top)`
coordinates — pdfplumber emits every character in the stream, so
`extract_text` produces `"RR"` `"ee"` `"tt"` runs. Observed on the AP
US Gov CED. The fix is `extract_pdf_text_deduped`, which groups
`page.chars` by `(round(x0/tol), round(top/tol), text)` and keeps one
representative per group before reassembling text. Opt-in via
`pdf_dedup_coords=True` in the scope spec (see
`docs/diagnostics/2026-04-18-ap-ced-doubling-investigation.md`). Body
text is untouched; only duplicated glyphs are removed.

**Known limitations.**

- **Image-only PDFs** (no embedded text layer) need OCR. pdfplumber
  returns empty text, surfaced via `chars_out: 0` in the trace.
- **Encrypted PDFs** need a decryption key. pdfplumber raises on
  open, recorded as `extract_failure: pdfplumber_open_failed: ...`.
- **Multi-column layouts on topic-content pages** (e.g. AP CED-style
  learning-objective tables) suffer Y-aligned sidebar/body
  interleaving with pdfplumber's default and `layout=True` extraction.
  Substance preserved; line sequencing mixed. See the AP US Gov Unit
  1 run snapshot for a worked example.
- **Form-filled PDFs** extract the form's static text; filled-field
  values are partially recovered depending on the encoding used by
  the form author.

**Test artefacts.**

- `docs/run-snapshots/2026-04-18-session-4a-1-phase0-test-dfe-ks3/` —
  UK DfE statutory KS3 Maths programme of study. Full-document
  extraction; single-column; all six subject-content strands present.
  Regression-verified byte-clean under schema 0.4.0 in
  `docs/run-snapshots/2026-04-18-session-4a-2a-regression-dfe-ks3/`.
- `docs/run-snapshots/2026-04-18-session-4a-1-phase0-test-ap-usgov/` —
  AP US Gov CED, Unit 1. **Superseded** by the 4a-2a requeue;
  retained for audit under schema 0.4.0 with a `SUPERSEDED.md` note.
- `docs/run-snapshots/2026-04-18-session-4a-2a-ap-usgov-requeued/` —
  Clean re-acquisition under the coordinate-dedup primitive and
  `verify_extraction_quality`. Verification verdict `clean`.
  `known_pathology_handling: ['coordinate_level_footer_overlap']`.

## `multi_section_pdf` primitive sequence (Session 4a-2b)

For PDFs with a multi-section structure — a table of contents, an
embedded outline, or clearly heading-demarcated sections. The
detector routes a PDF here when `page_count >= 50` and either the
embedded outline has >= 2 top-level entries or the TOC-page
heuristic detects >= 3 dot-leader entries.

**Scope.** Required: `source_reference`. One of `page_range`,
`section_identifier` (exact TOC-title match), or `section_heading`
(case-insensitive prefix / regex match) must resolve — the
`resolve_section_scope` primitive pauses Phase 0 with the available
TOC entries if none does. Optional: `pdf_dedup_coords=True` for PDFs
with a coordinate-level pathology (none observed on Ontario per
Step 3's pre-check).

**`detect_toc` primitive.** Three-tier deterministic TOC detection,
no model calls:

1. **Embedded outline** via pypdf's outline tree. Yields
   `{title, page_number (1-indexed), depth, source}`. When an AODA
   structure tree (`/StructTreeRoot`) is present, it is flagged in
   the detection trace as `struct_tree_present: true` but the primary
   outline continues to drive section resolution — downstream
   consumers can opt into the structure tree in a later session.
2. **TOC-page heuristic** when no embedded outline exists. Scans the
   first 20 pages for a page titled `Contents` / `Table of Contents`,
   then parses leader lines (`title……… page_number`).
3. **Heading-structure inference** (last-resort fallback). Classifies
   lines by predominant char-height from `page.chars`; lines whose
   font is 1.35× the body-text median are flagged as headings,
   tagged `source: heading_inference` with lower confidence.

**`resolve_section_scope` primitive.** Reads the TOC from
`detect_toc`'s meta and the scope spec, producing an explicit
`[start, end]` range. Priority: explicit `page_range` wins, else
`section_identifier` (exact), else `section_heading` (fuzzy /
regex). The resolved range is propagated via `meta` so the extractor
honours it preferentially over `scope.page_range`. When no field
resolves, Phase 0 pauses with a prompt listing the available TOC
entries.

**Multi-pathology handling.** Step 3's Ontario pre-check found no
letter-level coordinate overlap at tolerances 1 or 2; the multi-
section sequence therefore defaults dedup off. Sources with a single
confirmed pathology route through the deduped extractor via
`pdf_dedup_coords=True`. Chained multi-pathology dedup is deferred
until a source with >1 confirmed pathology is observed.

**Test artefact.**

- `docs/run-snapshots/2026-04-18-session-4a-2b-ontario-g7-history/` —
  Ontario K-8 Social Studies / History / Geography (2023),
  Grade 7 History strand. `section_identifier="History, Grade 7"`
  auto-resolves to pages 245–266 via the embedded outline.
  Triangulated verification (Step 10): Check A structural PASS,
  Check B 6/6 exact overall-expectation titles, Check C volume
  46,227 chars over 22 pages with clean grade boundaries. Session
  outcome PASS WITH NOTES (Check C threshold recalibration
  recommended).

## `js_rendered_progressive_disclosure` primitive sequence (Session 4a-3)

For JS-heavy curriculum sites: SPA shells with content injected
client-side (React / Vue / Angular), or heavy-scripted server-rendered
pages that ship enough JS that a requests-based fetch is unreliable.
The detector routes a URL here when JS framework markers
(`#root`, `#app`, `__NUXT__`, `__INITIAL_STATE__`, `data-reactroot`,
`ng-version`, `<mat-*>` Angular Material custom elements) are present
AND the visible-text ratio is thin. Callers can also force-route via
`detection_override` when the auto-detector is ambiguous.

**Scope.** Required: `url`, `wait_for_selector`, `css_selector` (the
extract selector). Optional: `dismiss_modal_selector`, `click_sequence`,
`browser_timeout_ms` (default 30 000).

**`fetch_via_browser` primitive.** Pure capability — Playwright
headless Chromium, no site-specific branching:

- **Fixed viewport 1280 × 720.** Non-configurable by design. The
  rendered-state hash and extraction are tied to the viewport;
  leaving it configurable invites silent reproducibility breakage.
- **Navigation waits for `networkidle`**, not `domcontentloaded`.
  JS frameworks frequently render content via post-DCL XHR, and a
  DCL-level wait lets `wait_for_selector` match an empty shell —
  caught in Session 4a-3's smoke test.
- **Per-click observability.** `click_sequence` is a list of steps,
  each traced individually in the manifest (one entry per click).
  The v3 review chose this explicitly over a terser DSL.
- **Bot-detection taxonomy.** Three distinct pause reasons:
  `bot_detection_http_403`, `bot_detection_rate_limited`
  (429 or Retry-After on a non-2xx), `bot_detection_challenge_page`
  (Cloudflare / verify-human markers). Each pauses Phase 0 for user-
  in-the-loop rather than retrying silently.
- **Side artefacts.** The primitive emits a full-page screenshot as
  `rendered_state.png`; the executor writes it to the output
  directory and appends it to `manifest.content_files`.

**`dom_hash` primitive.** Runs directly after `fetch_via_browser`.
SHA-256s the rendered HTML so consumers can detect "page shape
changed" independently of "extracted text changed" — a JS SPA that
ships identical visible text but swaps an accordion for a tab control
has the same `content_hash` and a different `dom_hash`. The manifest's
`dom_hash` field is null for non-JS source types.

**Multi-source generalisation.** Session 4a-3 validates the primitive
on two structurally different curriculum sites — Ontario DCP (Angular
Material SPA, grade-based) and NZ Curriculum Online (custom CMS,
levels-based, consent modal present). The same primitive handles both
with scope-level differences only (NZ adds `dismiss_modal_selector`,
Ontario does not). Extended multi-jurisdiction robustness testing
(Australian Curriculum, Singapore MOE, US state standards) is
deferred to a potential Session 4a-3.5.

**Site-specific choreography lives in the scope, not in the primitive.**
If the primitive grows an `if site == ...` branch, that is a design
failure — refactor to scope before merging.

**Test artefacts.**

- `docs/run-snapshots/2026-04-18-session-4a-3-ontario-dcp-g7-history/` —
  Ontario Grade 7 History strand-index route. Cross-validated against
  the 4a-2b PDF extraction: Check A structural PASS, Check B 6/6
  exact overall-expectation titles, Check B2 6/6 FOCUS ON match,
  Check C flagged (3 706 < 5 000 threshold, scope caveat — `/strands`
  route intentionally excludes specific-expectations content, which
  lives on SPA-routed sub-pages). Outcome PASS WITH NOTES.
- `docs/run-snapshots/2026-04-18-session-4a-3-nz-curriculum/` —
  NZ Social Sciences Phase 2 (Years 4–6). Check A structural PASS
  (four strands × Knowledge + Practices), Check C volume PASS
  (37 245 chars). Architectural verdict: validated — same primitive,
  one extra optional scope field.

## Source composition and selection

**Current capability.** Phase 0 extracts a single source given an
explicit source reference. A user (or runner script) specifies which
URL or PDF to extract from; the harness does not currently discover
candidate sources or rank them by completeness. One Phase 0 invocation
yields one acquired artefact (manifest + content files).

**Known limitation.** Some curricula are documented across multiple
authoritative sources at different levels of completeness. Concrete
example from this corpus: Ontario Grade 7 History has two extracted
sources —

- `multi_section_pdf` from the K-8 PDF
  (`docs/run-snapshots/2026-04-18-session-4a-2b-ontario-g7-history/`):
  contains both overall and specific expectations, ~46 K chars.
- `js_rendered_progressive_disclosure` from the DCP website
  (`docs/run-snapshots/2026-04-18-session-4a-3-ontario-dcp-g7-history/`):
  overall expectations only, ~3.7 K chars (specific-expectations text
  lives on SPA-routed sub-pages).

For applications that need the full curriculum content, the PDF source
is more authoritative; for applications that need the per-strand
overview that Ontario publishes online, the DCP source is the
canonical wording.

**Multi-source composition is supported today** by running Phase 0
multiple times on the same curriculum and treating the outputs as
complementary artefacts at the consumer layer. There is no built-in
merge / deduplication step.

**Future work hint.** Multi-source selection will likely need a
`sources_catalog` data structure that maps a curriculum reference
(jurisdiction + subject + grade) to the known sources for that
reference, with metadata about each source's coverage and
authoritativeness. Implementation specifics are deferred until
Session 4b establishes which source compositions teachers and AI
tutors actually find useful — premature schema choices here would
constrain the wrong axis.

## Scope spec

`ScopeSpec` is the back-compat constructor (callable) that infers
`source_type` from supplied fields and dispatches to the matching
discriminated-union variant. New code should construct the variant
directly (e.g. `StaticHtmlLinearScope(url=..., css_selector=...)`)
for clearer call sites. Per-type variants live in
`curriculum_harness/phases/phase0_acquisition/scope.py`:

- `StaticHtmlLinearScope` — `url`, one of `css_selector` /
  `heading_text`.
- `FlatPdfLinearScope` — `source_reference`; optional `page_range`,
  `section_heading`, `pdf_dedup_coords`.
- `MultiSectionPdfScope` — `source_reference`, one of `page_range` /
  `section_identifier` / `section_heading`.
- `JsRenderedProgressiveDisclosureScope` — `url`, `wait_for_selector`,
  `css_selector`; optional `dismiss_modal_selector`, `click_sequence`.
- `HtmlNestedDomScope` — `url`, `content_root_selector`; optional
  `exclude_selectors`, `section_scope_selector` *or*
  `section_anchor_selector` (mutually exclusive),
  `section_anchor_stop_selector`, `include_details_content`,
  `preserve_headings`.

Each variant uses Pydantic's `extra="forbid"` so cross-type field
smuggling (e.g. `page_range` on a JS scope) is rejected at
construction time. The forward-compatible deserialiser in `scope.py`
upgrades 0.4.0 flat-shaped manifests to the discriminated union on
load. See `docs/diagnostics/2026-04-18-session-4a-4-step-3b-regression-report.md`
for the regression evidence that the upgrade is byte-stable.

> **Phase 0 expects a specific source reference per run.**
> Multi-source curriculum composition is future work (Session 4b
> onwards). See the "Source composition and selection" section above
> for the current single-source posture and the rationale for
> deferring composition.

## Manifest schema (v0.4.0)

- `content_hash` — SHA-256 of the final normalised content bytes.
- `detection_hash` — SHA-256 of the `_detection.json` payload, so the
  type-detector output is tamper-evident and part of the audit trail.
- `scope_acquired.verification_excerpt` — `{first_chars, last_chars,
  line_count}` snapshot for visual inspection without loading the full
  content file.
- `verification_trace` (schema 0.3.0+) — list of `VerificationEntry`
  records, one per verification primitive. Multi-section and flat-PDF
  sequences now produce two entries (raw-mode and normalised-mode —
  see the `verify_extraction_quality` section below).
- `known_pathology_handling` (new in 0.4.0) — list of
  `KnownPathology` enum values the acquisition was configured to
  handle. Append-only enum with four reserved entries
  (`coordinate_level_footer_overlap` observed in AP CED; three others
  reserved for future confirmed pathologies). Pydantic rejects
  unknown values on write.
- `investigation_memo_refs` (new in 0.4.0) — list of diagnostic-memo
  paths relevant to this acquisition (e.g. a memo recording the
  investigation that identified a pathology).
- `dom_hash` (new in 0.4.0 via Session 4a-3) — SHA-256 of the
  rendered DOM HTML for JS-rendered acquisitions, null for
  PDF / static-HTML acquisitions. Complements `content_hash`: the
  latter tracks extracted text, the former tracks rendered shape.

## `verify_extraction_quality` primitive

A mandatory step in every primitive sequence. Runs deterministic
statistical checks on the extracted content and returns a verdict.
As of Session 4a-2b Step 4 the primitive runs in **two modes** within
every production sequence — the raw-mode pass catches signals that
`normalise_whitespace` would destroy, the normalised-mode pass does
the rest.

- **raw mode** (`verify_raw_extraction`, inserted between the
  extractor and `normalise_whitespace`):
  - `whitespace_runs` — count of 80+ contiguous whitespace runs.
    Must run pre-normalise; the normalise step would collapse the
    pattern into a single space and make the check a false
    reassurance.
- **normalised mode** (`verify_normalised_extraction`, inserted
  after `normalise_whitespace`):
  - `character_doubling` — per-line ratio of identical adjacent
    non-whitespace pairs, plus systematic-pattern detection (≥ 5
    lines with mean ratio ≥ 0.4) to catch footer-only doubling that
    would fall below a document-wide threshold.
  - `repeated_bigram` — top-10 letter-bigram share (typical English
    ~0.25; failure at 0.75). **Language-aware calibration** (Step 5):
    a conservative stopword-based English detector runs first; on
    non-English or low-confidence text a bigram failure is
    downgraded to `suspicious` rather than `failed`, with the
    downgrade reason recorded in the trace. Rationale: the project
    has no calibration data for non-English bigram statistics.
  - `empty_line_ratio` — fraction of lines that are empty or
    whitespace-only.
  - `completeness` (new in Step 6) — expected content volume
    against source metadata harvested by the executor. HTML: flagged
    below 5 % of fetched bytes, failed below 2 %. PDF: flagged
    below 50 chars/page, failed below 20 chars/page. Skipped with
    a recorded reason when neither metric is available.

Verdict `failed` pauses the pipeline with a user-in-the-loop request
that suggests a recovery scope change (e.g. `pdf_dedup_coords: true`
for systematic character-doubling). Verdict `suspicious` continues
with a warning recorded in the trace. Verdict `clean` is the happy
path.

No model calls. Thresholds are constructor arguments, exposed in the
trace so the audit record is reproducible. Adversarial regression
tests live in `tests/phase0/test_verify_extraction_quality.py` and
cover all five checks plus the language-aware downgrade and the
"whitespace runs are dead after normalisation" contract.

## Triangulated verification (Session 4a-2b Step 10)

For load-bearing new-source tests, a single check is not enough. The
Ontario Grade 7 History test used a three-check triangulation:

- **Check A — structural plausibility.** Shape assertions on the
  extracted content (strand headings, overall-expectation codes,
  section markers). Independent of what the content says.
- **Check B — screenshot title match.** Assertion that specific
  titles from an independent ground-truth source (a curriculum-site
  screenshot) appear in the extracted content verbatim.
- **Check C — volume sanity.** Total character count against a
  plausible range derived from the source's page count and
  per-page density.

No single check bears full weight. A mismatch in one, where the
other two pass and boundary inspection confirms clean scoping, is
evidence that the specific check's threshold is miscalibrated rather
than evidence of extraction failure. The Ontario test's PASS WITH
NOTES classification (Check C's 30k ceiling was too tight for a
2,100-char/page curriculum) is the worked example documented in the
run-snapshot README.

## Known downstream risks

### Tag-boundary line fragmentation

The `normalise_whitespace` primitive preserves line separators produced
by source tag boundaries — an HTML `<i>` inside a paragraph surfaces as
a new line, a span split inside a PDF paragraph surfaces as a new line.
Phase 0 is deliberately **faithful to source structure**; it does not
re-flow text across tag boundaries because re-flowing would be a lossy
decision that belongs in a semantic layer.

**Implication for downstream phases.** Any code that treats each line
as a semantic unit — notably `source_bullets` extraction in Phase 1 —
should expect fragmented inline content. The Common Core 7.RP test
artefact shows this pattern (embedded-example fractions on three
lines: `1/2`, `/`, `1/4`).

**Responsibility.** Phase 0 preserves fragments. Phase 1 (or
whichever phase owns semantic reconstitution) is responsible for
stitching them back together where needed.

### Multi-column PDF page interleaving

See `flat_pdf_linear` — known limitations. The Ontario Grade 7
artefact extracts cleanly under single-column per-page reading order
because the curriculum's multi-column layout is less dense than the
AP CED's sidebar/body columns. Downstream consumers of two-column
PDFs should still expect interleaving on sidebar-heavy pages until a
column-aware extraction primitive is shipped.

## Scheduled (next sessions)

- Session 4a-4: `html_nested_dom` source-type primitive sequence
  (UK gov.uk-style deeply nested / tabbed HTML).
- Session 4a-3.5 (optional): extended multi-source robustness test of
  the browser primitive against additional jurisdictions (Australian
  Curriculum, Singapore MOE, US state standards).
- Scope-aware volume thresholds so Check C in triangulated
  verification can honour "overall-expectations-only" scopes without
  flagging correctly-extracted content below the full-document
  threshold (Session 4a-3 Step 6 caveat).
- Column-aware extraction for dense multi-column pages (per-page
  bounding-box cropping or x-sorted column-band grouping).
- Multi-pathology chained dedup (only when a source with >1
  confirmed pathology is observed in the test corpus).
- Multi-URL aggregation primitive for sites that split sections
  across SPA-routed sub-URLs (Ontario DCP specific-expectations
  use case).
