"""Phase 0 manifest schema.

Every acquisition produces two kinds of artefact:

- A manifest JSON with metadata (this module's ``AcquisitionManifest``).
- One or more content text files referenced by the manifest via path.

The manifest is the source of truth for how an acquisition ran — source
reference, scope requested vs acquired, primitive sequence, per-primitive
trace, content hash, encoding, and any user interactions. Downstream
consumers never read raw URLs; they read manifest + content files.

Schema 0.5.0 (Session 4a-4) — ``scope_requested`` is a discriminated
union of per-source-type scope models defined in ``scope.py``. The
0.4.0 flat ``ScopeSpec`` shape is accepted on load via
``parse_scope`` and normalised to the matching 0.5.0 variant. The
field names ``ScopeSpec``/``Scope`` are both exported so external
callers can use whichever they prefer; ``ScopeSpec`` is now an alias
for the discriminated union.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

from curriculum_harness.phases.phase0_acquisition.scope import (
    ClickStep,
    ClickStepWaitFor,
    FlatPdfLinearScope,
    HtmlNestedDomScope,
    JsRenderedProgressiveDisclosureScope,
    MultiSectionPdfScope,
    Scope,
    SourceTypeLiteral,
    StaticHtmlLinearScope,
    make_scope,
    parse_scope,
)


SourceType = Literal[
    "static_html_linear",
    "flat_pdf_linear",
    "multi_section_pdf",
    "js_rendered_progressive_disclosure",
    "html_nested_dom",
    "unknown",
]


# ``ScopeSpec`` was the 0.4.0 flat-union model. In 0.5.0 it is the
# backwards-compatible callable that infers ``source_type`` from the
# supplied fields and dispatches to the right discriminated-union
# variant. New code should construct the per-type variant directly
# (``StaticHtmlLinearScope(...)`` etc.) for clearer call sites; old
# code calling ``ScopeSpec(url=..., css_selector=...)`` continues to
# work unchanged.
ScopeSpec = make_scope


# Append-only enum of PDF pathologies Phase 0 knows how to handle.
#
# Adding a new value is a deliberate act: it means we have empirically
# observed the pathology in a real source and have chosen a
# deterministic primitive configuration that handles it. Do not add
# speculative values. Manifests may only reference values in this
# enum — the Pydantic model validates on write.
#
# - ``coordinate_level_footer_overlap`` — PDF renders header/footer
#   glyphs twice at near-identical coordinates. Observed in the AP US
#   Gov CED (Session 4a-2a). Handled by
#   ``extract_pdf_text_deduped`` with
#   ``pdf_dedup_coord_tolerance=1``.
# - ``coordinate_level_general_overlap`` — coordinate-level glyph
#   overlap beyond headers/footers (e.g. AODA PDFs with accessibility
#   overlays rendering body text twice). Reserved; not yet observed.
# - ``character_stream_doubling`` — doubling at the content-stream
#   level (Mechanism C in the 4a-2a investigation memo). Reserved;
#   not yet observed in any test source.
# - ``aoda_tagged_content_overlap`` — AODA structure-tagging that
#   produces invisible-text overlap alongside visible text. Reserved.
KnownPathology = Literal[
    "coordinate_level_footer_overlap",
    "coordinate_level_general_overlap",
    "character_stream_doubling",
    "aoda_tagged_content_overlap",
]


class UserInteraction(BaseModel):
    """Record of a user-in-the-loop pause and resume."""

    primitive: str
    needed: str
    request_file: str | None = None
    provided_file: str | None = None
    resolved: bool = False
    timestamp: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
    )


class PrimitiveTraceEntry(BaseModel):
    """Per-primitive trace entry in the acquisition trace."""

    primitive: str
    inputs: dict[str, Any] = Field(default_factory=dict)
    outputs_summary: dict[str, Any] = Field(default_factory=dict)
    duration_ms: int = 0
    error: str | None = None
    user_interaction: UserInteraction | None = None
    started_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
    )


class VerificationEntry(BaseModel):
    """Per-verification-primitive entry in the verification trace."""

    primitive: str
    verdict: str = Field(
        description="One of: 'clean', 'suspicious', 'failed'.",
    )
    checks_run: list[dict[str, Any]] = Field(default_factory=list)
    details: dict[str, Any] = Field(default_factory=dict)
    timestamp: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
    )


class AcquisitionManifest(BaseModel):
    """Top-level manifest for a single Phase 0 acquisition.

    Schema 0.5.0 (Session 4a-4) bumps ``scope_requested`` to a
    discriminated union; otherwise field shapes match 0.4.0.

    The model_validator below makes the load path forward-compatible
    with 0.4.0 manifests: when ``scope_requested`` arrives as a flat
    dict without ``source_type``, the validator copies the
    manifest-level ``source_type`` into the scope dict before
    discriminator-based parsing.
    """

    source_reference: str
    source_type: SourceType
    scope_requested: Scope
    scope_acquired: dict[str, Any] = Field(default_factory=dict)
    primitive_sequence: list[str] = Field(default_factory=list)
    acquisition_trace: list[PrimitiveTraceEntry] = Field(default_factory=list)
    verification_trace: list[VerificationEntry] = Field(default_factory=list)
    content_files: list[str] = Field(default_factory=list)
    content_hash: str | None = None
    detection_hash: str | None = None
    dom_hash: str | None = Field(
        default=None,
        description=(
            "SHA-256 of the rendered DOM HTML at extraction time — only "
            "set for JS-rendered source types. ``content_hash`` hashes "
            "the normalised extracted text; ``dom_hash`` hashes the raw "
            "rendered HTML the primitive saw, so downstream consumers can "
            "detect whether the page shape changed even when the "
            "extracted text is stable. Null for non-JS source types."
        ),
    )
    encoding_detected: str | None = None
    encoding_failure: str | None = None
    user_interactions: list[UserInteraction] = Field(default_factory=list)
    known_pathology_handling: list[KnownPathology] = Field(
        default_factory=list,
        description=(
            "PDF pathologies the acquisition was configured to handle. "
            "Values are drawn from the append-only ``KnownPathology`` "
            "enum. Empty list if none."
        ),
    )
    investigation_memo_refs: list[str] = Field(
        default_factory=list,
        description=(
            "Paths to diagnostic memos relevant to this acquisition "
            "(e.g. a record of the investigation that identified a "
            "pathology). Empty list if none."
        ),
    )
    timestamp: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
    )
    phase0_version: str = "0.5.0"
    notes: str | None = None

    @model_validator(mode="before")
    @classmethod
    def _migrate_scope_requested(cls, data: Any) -> Any:
        """Forward-compat: accept 0.4.0 flat scope dicts.

        A 0.4.0 manifest has ``scope_requested`` as a flat dict
        without a ``source_type`` key (the source_type lives at the
        manifest's top level). Re-route through ``parse_scope`` with
        the manifest-level ``source_type`` as fallback so the
        discriminated-union validator picks the right variant.

        Idempotent on 0.5.0 manifests: if ``source_type`` is already
        present in the scope dict, ``parse_scope`` uses it directly.
        """

        if not isinstance(data, dict):
            return data
        scope = data.get("scope_requested")
        if scope is None:
            return data
        # If already a Pydantic model, leave it.
        if isinstance(scope, BaseModel):
            return data
        if isinstance(scope, dict):
            manifest_source_type = data.get("source_type")
            # ``unknown`` is not a valid scope variant; it appears only
            # at manifest level for failed type-detector runs that
            # never produced a real scope. Skip migration in that case.
            if (
                manifest_source_type
                and manifest_source_type != "unknown"
                and "source_type" not in scope
            ):
                migrated = parse_scope(
                    scope, fallback_source_type=manifest_source_type
                )
                data["scope_requested"] = migrated
        return data

    def append_trace(self, entry: PrimitiveTraceEntry) -> None:
        self.acquisition_trace.append(entry)
        if entry.primitive not in self.primitive_sequence:
            self.primitive_sequence.append(entry.primitive)
        if entry.user_interaction is not None:
            self.user_interactions.append(entry.user_interaction)

    def append_verification(self, entry: VerificationEntry) -> None:
        self.verification_trace.append(entry)


__all__ = [
    "AcquisitionManifest",
    "ClickStep",
    "ClickStepWaitFor",
    "FlatPdfLinearScope",
    "HtmlNestedDomScope",
    "JsRenderedProgressiveDisclosureScope",
    "KnownPathology",
    "MultiSectionPdfScope",
    "PrimitiveTraceEntry",
    "Scope",
    "ScopeSpec",
    "SourceType",
    "SourceTypeLiteral",
    "StaticHtmlLinearScope",
    "UserInteraction",
    "VerificationEntry",
    "parse_scope",
]
