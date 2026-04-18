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

| Source type                          | Primitive sequence                                                                      | Status       |
| ------------------------------------ | --------------------------------------------------------------------------------------- | ------------ |
| `static_html_linear`                 | `fetch_requests → encoding_detection → extract_* → normalise_whitespace → content_hash` | implemented  |
| `flat_pdf_linear`                    | `fetch_pdf_file → extract_pdf_text → normalise_whitespace → content_hash`               | implemented  |
| `multi_section_pdf`                  | pending (Session 4a-2)                                                                  | deferred     |
| `js_rendered_progressive_disclosure` | pending                                                                                 | deferred     |
| `html_nested_dom`                    | pending                                                                                 | deferred     |

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

**Known limitations (Session 4a-1).**

- **Image-only PDFs** (no embedded text layer) need OCR. Not in scope
  for 4a-1; pdfplumber will return empty text, which the primitive
  surfaces via `chars_out: 0`. An OCR-first fallback is a candidate
  for a later session.
- **Encrypted PDFs** need a decryption key. Not in scope. pdfplumber
  raises on open, and the primitive records the failure via
  `extract_failure: pdfplumber_open_failed: ...` in the trace.
- **Multi-column layouts on topic-content pages** (e.g. CED-style
  learning-objective tables) suffer Y-aligned sidebar/body
  interleaving with pdfplumber's default and `layout=True` extraction.
  Substance preserved; line sequencing mixed. See the AP US Gov Unit
  1 run snapshot for a worked example. Fix path: per-page column
  bounding-box cropping, scheduled with Session 4a-2
  (`multi_section_pdf`).
- **Form-filled PDFs** extract the form's static text; filled-field
  values are partially recovered depending on the encoding used by
  the form author.

**Test artefacts (Session 4a-1).**

- `docs/run-snapshots/2026-04-18-session-4a-1-phase0-test-dfe-ks3/` —
  UK DfE statutory KS3 Maths programme of study. Full-document
  extraction; single-column; all six subject-content strands present.
- `docs/run-snapshots/2026-04-18-session-4a-1-phase0-test-ap-usgov/` —
  AP US Government and Politics CED, Unit 1. Scoped `page_range`
  extraction; demonstrates two-column limitation on topic pages.

## Scope spec

`ScopeSpec` (Pydantic) carries the union of fields across all primitive
sequences. Each primitive validates the subset it needs and raises
`ScopeValidationError` if any required field is missing; the executor
converts that into a hand-editable `request.md` + `state.json` pause.

## Manifest schema (v0.2.0)

- `content_hash` — SHA-256 of the final normalised content bytes.
- `detection_hash` — SHA-256 of the `_detection.json` payload, so the
  type-detector output is tamper-evident and part of the audit trail.
- `scope_acquired.verification_excerpt` — `{first_chars, last_chars,
  line_count}` snapshot for visual inspection without loading the full
  content file.

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
should expect fragmented inline content: fractions, italic emphasis,
inline formulae and citation markers can appear on separate lines. The
Common Core 7.RP test artefact shows this pattern (embedded-example
fractions on three lines: `1/2`, `/`, `1/4`).

**Responsibility.** Phase 0 preserves fragments. Phase 1 (or whichever
phase owns semantic reconstitution) is responsible for stitching them
back together where needed.

### Multi-column PDF page interleaving

See `flat_pdf_linear` — known limitations. Downstream phases consuming
two-column CED-style PDFs should expect sidebar labels (e.g.
"Government Power / Individual Rights") interleaved into body
sentences. Until Session 4a-2 ships column-aware extraction, semantic
extractors should not treat a single line as a single semantic unit on
multi-column layouts.
