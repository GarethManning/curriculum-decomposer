"""Phase 0 manifest schema.

Every acquisition produces two kinds of artefact:

- A manifest JSON with metadata (this module's ``AcquisitionManifest``).
- One or more content text files referenced by the manifest via path.

The manifest is the source of truth for how an acquisition ran — source
reference, scope requested vs acquired, primitive sequence, per-primitive
trace, content hash, encoding, and any user interactions. Downstream
consumers never read raw URLs; they read manifest + content files.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, Field


SourceType = Literal[
    "static_html_linear",
    "flat_pdf_linear",
    "multi_section_pdf",
    "js_rendered_progressive_disclosure",
    "html_nested_dom",
    "unknown",
]


class ScopeSpec(BaseModel):
    """Structured scope specification.

    Free-text scope is rejected by design. Each primitive declares its
    required/optional fields; ``ScopeSpec`` carries the union. Primitives
    validate the subset they need and raise ``ScopeValidationError`` on
    missing fields, which Phase 0 converts to a user-in-the-loop request.
    """

    source_reference: str = Field(
        description="URL or local file path to acquire from.",
    )
    url: str | None = Field(
        default=None,
        description="Explicit URL (overrides source_reference if set).",
    )
    css_selector: str | None = Field(
        default=None,
        description="CSS selector identifying the target content block.",
    )
    heading_text: str | None = Field(
        default=None,
        description="Heading text (or regex) marking the section start.",
    )
    heading_regex: bool = Field(
        default=False,
        description="Interpret heading_text as a regex.",
    )
    page_range: list[int] | str | None = Field(
        default=None,
        description=(
            "PDF page range. Preferred form: ``[start, end]`` (1-indexed, "
            "inclusive on both ends). String form ``'start-end'`` is "
            "accepted for legacy configs."
        ),
    )
    section_heading: str | None = Field(
        default=None,
        description=(
            "Section heading (literal or regex) to scope a PDF extraction. "
            "Used by PDF primitives; interpreted as a regex if "
            "heading_regex is True."
        ),
    )
    section_identifier: str | None = Field(
        default=None,
        description="Source-internal section id. Reserved for future primitives.",
    )
    follow_links: bool = Field(
        default=False,
        description="Whether to follow sub-links into deeper content.",
    )
    notes: str | None = Field(
        default=None,
        description="Human-readable note about why this scope was chosen.",
    )
    pdf_dedup_coords: bool = Field(
        default=False,
        description=(
            "When True, route PDF extraction through the "
            "``extract_pdf_text_deduped`` primitive instead of the fast "
            "``extract_pdf_text`` path. Use for PDFs where the source "
            "renders text twice at identical coordinates (e.g. overlaid "
            "headers/footers). See Session 4a-2a investigation memo."
        ),
    )
    pdf_dedup_coord_tolerance: int = Field(
        default=1,
        description=(
            "Coordinate rounding precision in pixels used by the deduped "
            "extraction primitive to identify overlapping characters. "
            "Only read when ``pdf_dedup_coords`` is True."
        ),
    )


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


class AcquisitionManifest(BaseModel):
    """Top-level manifest for a single Phase 0 acquisition.

    ``scope_acquired`` is a dict whose canonical shape is:

    - ``chars`` — int, total characters of extracted content.
    - ``verification_excerpt`` — dict with ``first_chars`` (first 200
      characters), ``last_chars`` (last 100 characters) and
      ``line_count``. A lightweight, stable summary for visual
      inspection without reading the full content file.

    ``detection_hash`` is the SHA-256 of the ``_detection.json`` payload
    written alongside the manifest, so the type-detector output is
    tamper-evident and part of the audit trail.
    """

    source_reference: str
    source_type: SourceType
    scope_requested: ScopeSpec
    scope_acquired: dict[str, Any] = Field(default_factory=dict)
    primitive_sequence: list[str] = Field(default_factory=list)
    acquisition_trace: list[PrimitiveTraceEntry] = Field(default_factory=list)
    content_files: list[str] = Field(default_factory=list)
    content_hash: str | None = None
    detection_hash: str | None = None
    encoding_detected: str | None = None
    encoding_failure: str | None = None
    user_interactions: list[UserInteraction] = Field(default_factory=list)
    timestamp: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
    )
    phase0_version: str = "0.2.0"
    notes: str | None = None

    def append_trace(self, entry: PrimitiveTraceEntry) -> None:
        self.acquisition_trace.append(entry)
        if entry.primitive not in self.primitive_sequence:
            self.primitive_sequence.append(entry.primitive)
        if entry.user_interaction is not None:
            self.user_interactions.append(entry.user_interaction)
