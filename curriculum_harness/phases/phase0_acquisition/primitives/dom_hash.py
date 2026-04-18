"""DOM-level content-hash primitive (Session 4a-3 Step 4).

Runs directly after ``fetch_via_browser`` on JS-rendered source types.
Hashes the full rendered HTML so that downstream consumers can detect
"the page shape changed" independently of "the extracted text changed"
— for example, a JS SPA that renders identical visible text but swaps
an accordion for a tab control would have a different ``dom_hash`` and
the same ``content_hash``.

The rendered HTML is carried through the pipeline via
``previous.meta['rendered_html']``. This primitive does not read or
transform ``previous.output`` — it passes the output through unchanged
so the next primitive (``extract_css_selector``) receives the rendered
HTML to extract text from.

Deterministic. No model calls. No side effects.
"""

from __future__ import annotations

import hashlib

from curriculum_harness.phases.phase0_acquisition.primitives.base import (
    PrimitiveResult,
)


class DomHashDivergenceError(RuntimeError):
    """Raised when the dom_hash primitive's digest disagrees with the
    raw-content entry for the rendered HTML.

    Both hashes cover the same ``rendered_html`` string produced by
    ``fetch_via_browser``; if they differ, either the DOM-hash
    computation or the raw-content capture is buggy, and proceeding
    past this point would compound the bug. The exception halts the
    pipeline so the divergence can be investigated.
    """


class DomHashPrimitive:
    name = "dom_hash"
    required_scope_fields: tuple[str, ...] = ()
    optional_scope_fields: tuple[str, ...] = ()
    side_effects: frozenset[str] = frozenset()

    def validate_scope(self, scope) -> None:
        return None

    def run(self, scope, previous: PrimitiveResult | None) -> PrimitiveResult:
        rendered_html: str = ""
        raw_content_entries: list[dict] = []
        if previous is not None:
            # Prefer the dedicated meta field; fall back to output for
            # robustness if a future primitive renames the meta key.
            rendered_html = (
                previous.meta.get("rendered_html") or str(previous.output or "")
            )
            raw_content_entries = list(previous.meta.get("raw_content") or [])
        digest = hashlib.sha256(rendered_html.encode("utf-8")).hexdigest()

        # Session 4a-4.5 equivalence check: the rendered_html raw-cache
        # entry from fetch_via_browser must hash the same bytes this
        # primitive just hashed. Halt on divergence.
        rendered_html_entry = next(
            (e for e in raw_content_entries if e.get("file_type") == "rendered_html"),
            None,
        )
        if rendered_html_entry is not None:
            cached_hash = rendered_html_entry.get("hash")
            if cached_hash and cached_hash != digest:
                raise DomHashDivergenceError(
                    "dom_hash computed over previous.meta['rendered_html'] "
                    f"({digest}) does not match the raw_content "
                    f"rendered_html entry hash ({cached_hash}). Either the "
                    "DOM-hash computation or the raw HTML capture in "
                    "fetch_via_browser is buggy."
                )

        passthrough_output = (
            previous.output if previous is not None else ""
        )
        passthrough_meta = dict(previous.meta) if previous is not None else {}
        passthrough_meta["dom_hash"] = digest
        return PrimitiveResult(
            output=passthrough_output,
            summary={
                "dom_hash": digest,
                "rendered_html_bytes": len(rendered_html),
                "raw_rendered_hash_match": (
                    rendered_html_entry is not None
                    and rendered_html_entry.get("hash") == digest
                ),
            },
            meta=passthrough_meta,
        )
