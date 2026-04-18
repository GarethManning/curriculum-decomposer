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

| Source type                          | Primitive sequence                                                              | Status       |
| ------------------------------------ | ------------------------------------------------------------------------------- | ------------ |
| `static_html_linear`                 | `fetch_requests → encoding_detection → extract_* → normalise_whitespace → content_hash` | implemented  |
| `flat_pdf_linear`                    | pending (Session 4a-1)                                                          | deferred     |
| `multi_section_pdf`                  | pending (Session 4a-2)                                                          | deferred     |
| `js_rendered_progressive_disclosure` | pending                                                                         | deferred     |
| `html_nested_dom`                    | pending                                                                         | deferred     |

Deferred types raise `Phase0Paused` with a user-in-the-loop request file.

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
