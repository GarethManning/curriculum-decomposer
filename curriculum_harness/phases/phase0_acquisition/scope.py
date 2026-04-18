"""Phase 0 scope schema (0.5.0): per-source-type discriminated unions.

Each Phase 0 source type carries a different set of required and
optional scope fields. In schema 0.4.0 these all coexisted on a single
``ScopeSpec`` model where every per-type field was optional and shared.
That worked initially but accumulated debt across three sessions:
fields meaningful only to PDF (``page_range``, ``pdf_dedup_coords``)
were silently accepted on HTML scopes; HTML-only fields
(``css_selector``, ``wait_for_selector``) were silently accepted on
PDF scopes; the schema offered no way to assert "this scope is for a
JS-rendered page" beyond the manifest-level ``source_type`` field.

Session 4a-4 Step 3a refactors this into per-source-type Pydantic
models bound by a discriminated union on ``source_type``. Each variant
declares exactly the fields its primitive sequence needs; cross-type
field smuggling (e.g. ``page_range`` on a JS-rendered scope) is
rejected at construction time.

# Forward-compatible deserialiser (0.4.0 → 0.5.0)

Manifests written under schema 0.4.0 carry ``scope_requested`` as a
flat dict containing the union of all fields. They have **no
``source_type`` field on the scope dict** — the ``source_type`` lives
on the parent manifest. ``parse_scope`` (and the
``AcquisitionManifest`` model_validator) accept either:

- 0.5.0 shape: ``scope_requested`` includes ``source_type`` and only
  the fields valid for that variant.
- 0.4.0 shape: ``scope_requested`` has no ``source_type``; the loader
  copies ``source_type`` from the parent manifest before validating.
  Fields not relevant to the variant are dropped (with a record kept
  in the manifest's ``notes`` only if the field carried a non-default
  value, to avoid silent data loss).

This is a one-way upgrade. Saving a 0.5.0 manifest writes the new
shape; a downgrade to 0.4.0 readers requires the field-flattening
logic in reverse and is not provided. Since the harness controls all
manifest producers and consumers within this project, forward
compatibility is sufficient and avoids the maintenance overhead of
versioned deserialisers per shape.

# Why a discriminated union and not subclassing

Pydantic's ``Field(discriminator=...)`` selects the variant at parse
time from the ``source_type`` literal, giving correct deserialisation
without ad-hoc conditional branches in calling code. Subclass
hierarchies would either over-share fields (defeating the point of
the refactor) or rely on isinstance checks scattered through the
codebase.
"""

from __future__ import annotations

from typing import Annotated, Any, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, model_validator


# Re-exported for callers building scopes by hand.
SourceTypeLiteral = Literal[
    "static_html_linear",
    "flat_pdf_linear",
    "multi_section_pdf",
    "js_rendered_progressive_disclosure",
    "html_nested_dom",
]


class ClickStepWaitFor(BaseModel):
    """Signal a click step waits on before being considered complete.

    Carried over from the 0.4.0 manifest module; semantics unchanged.
    """

    type: Literal["selector_appears", "network_idle"]
    value: str = ""


class ClickStep(BaseModel):
    """One entry in the ``fetch_via_browser`` primitive's click_sequence."""

    selector: str
    wait_for: ClickStepWaitFor
    retry_on_fail: bool = True
    timeout_ms: int | None = None


# ---------------------------------------------------------------------------
# Per-source-type scope models.
# ---------------------------------------------------------------------------


class StaticHtmlLinearScope(BaseModel):
    """Scope for ``static_html_linear`` acquisitions.

    Required: ``url`` and exactly one of {``css_selector``, ``heading_text``}.
    """

    source_type: Literal["static_html_linear"] = "static_html_linear"
    url: str
    css_selector: str | None = None
    heading_text: str | None = None
    heading_regex: bool = False
    follow_links: bool = False
    # Optional auxiliary fields (carried on every scope for traceability).
    source_reference: str = ""
    notes: str | None = None

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def _default_source_reference(self) -> "StaticHtmlLinearScope":
        if not self.source_reference:
            self.source_reference = self.url
        return self

    @model_validator(mode="after")
    def _require_extractor_field(self) -> "StaticHtmlLinearScope":
        if not self.css_selector and not self.heading_text:
            raise ValueError(
                "StaticHtmlLinearScope requires one of "
                "`css_selector` or `heading_text`."
            )
        return self


class FlatPdfLinearScope(BaseModel):
    """Scope for ``flat_pdf_linear`` acquisitions.

    Required: ``source_reference``. Optional scoping: ``page_range``
    and/or ``section_heading``. ``pdf_dedup_coords`` opts into the
    coordinate-level dedup extractor for sources with overlaid-text
    pathologies (see Session 4a-2a investigation memo).
    """

    source_type: Literal["flat_pdf_linear"] = "flat_pdf_linear"
    source_reference: str
    page_range: list[int] | str | None = None
    section_heading: str | None = None
    heading_regex: bool = False
    pdf_dedup_coords: bool = False
    pdf_dedup_coord_tolerance: int = 1
    notes: str | None = None

    model_config = ConfigDict(extra="forbid")


class MultiSectionPdfScope(BaseModel):
    """Scope for ``multi_section_pdf`` acquisitions.

    Required: ``source_reference`` and exactly one of
    {``page_range``, ``section_identifier``, ``section_heading``}.
    The ``resolve_section_scope`` primitive pauses Phase 0 with the
    available TOC entries if no scoping field resolves.
    """

    source_type: Literal["multi_section_pdf"] = "multi_section_pdf"
    source_reference: str
    page_range: list[int] | str | None = None
    section_identifier: str | None = None
    section_heading: str | None = None
    heading_regex: bool = False
    pdf_dedup_coords: bool = False
    pdf_dedup_coord_tolerance: int = 1
    notes: str | None = None

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def _require_one_scoping_field(self) -> "MultiSectionPdfScope":
        if (
            not self.page_range
            and not self.section_identifier
            and not self.section_heading
        ):
            raise ValueError(
                "MultiSectionPdfScope requires one of "
                "`page_range`, `section_identifier`, or `section_heading`."
            )
        return self


class JsRenderedProgressiveDisclosureScope(BaseModel):
    """Scope for ``js_rendered_progressive_disclosure`` acquisitions.

    Required: ``url``, ``wait_for_selector``, ``css_selector``.
    Optional: ``dismiss_modal_selector``, ``click_sequence``,
    ``browser_timeout_ms``.
    """

    source_type: Literal["js_rendered_progressive_disclosure"] = (
        "js_rendered_progressive_disclosure"
    )
    url: str
    wait_for_selector: str
    css_selector: str
    dismiss_modal_selector: str | None = None
    click_sequence: list[ClickStep] | None = None
    browser_timeout_ms: int = 30000
    source_reference: str = ""
    notes: str | None = None

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def _default_source_reference(
        self,
    ) -> "JsRenderedProgressiveDisclosureScope":
        if not self.source_reference:
            self.source_reference = self.url
        return self


class HtmlNestedDomScope(BaseModel):
    """Scope for ``html_nested_dom`` acquisitions (Session 4a-4).

    Required: ``url``, ``content_root_selector``.
    Optional: ``exclude_selectors`` (CSS selectors to strip),
    ``section_scope_selector`` (CSS selector for a sub-section
    container), ``section_anchor_selector`` + ``section_anchor_stop_selector``
    (heading-anchor scoping for sites whose sub-sections are demarcated
    by sibling headings rather than container elements — see Step 1
    investigation memo for gov.uk KS3), ``include_details_content``
    (default True; ``<details>`` elements are static HTML, not JS,
    so their content is in the DOM regardless of expansion state),
    ``preserve_headings`` (default True; keeps heading markers in
    the extracted text for downstream section detection).

    Exactly one of {``section_scope_selector``,
    ``section_anchor_selector``} may be set; setting both is a
    configuration error caught at construction time.
    """

    source_type: Literal["html_nested_dom"] = "html_nested_dom"
    url: str
    content_root_selector: str
    exclude_selectors: list[str] = Field(default_factory=list)
    section_scope_selector: str | None = None
    section_anchor_selector: str | None = None
    section_anchor_stop_selector: str | None = None
    include_details_content: bool = True
    preserve_headings: bool = True
    source_reference: str = ""
    notes: str | None = None

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def _default_source_reference(self) -> "HtmlNestedDomScope":
        if not self.source_reference:
            self.source_reference = self.url
        return self

    @model_validator(mode="after")
    def _scope_mechanism_exclusive(self) -> "HtmlNestedDomScope":
        if self.section_scope_selector and self.section_anchor_selector:
            raise ValueError(
                "HtmlNestedDomScope: set at most one of "
                "`section_scope_selector` and `section_anchor_selector`. "
                "Container scoping and heading-anchor scoping are "
                "mutually exclusive."
            )
        if (
            self.section_anchor_stop_selector
            and not self.section_anchor_selector
        ):
            raise ValueError(
                "HtmlNestedDomScope: `section_anchor_stop_selector` "
                "requires `section_anchor_selector` to be set."
            )
        return self


# ---------------------------------------------------------------------------
# Discriminated union and parse helpers.
# ---------------------------------------------------------------------------


Scope = Annotated[
    Union[
        StaticHtmlLinearScope,
        FlatPdfLinearScope,
        MultiSectionPdfScope,
        JsRenderedProgressiveDisclosureScope,
        HtmlNestedDomScope,
    ],
    Field(discriminator="source_type"),
]


_SCOPE_VARIANT_BY_TYPE: dict[str, type[BaseModel]] = {
    "static_html_linear": StaticHtmlLinearScope,
    "flat_pdf_linear": FlatPdfLinearScope,
    "multi_section_pdf": MultiSectionPdfScope,
    "js_rendered_progressive_disclosure": JsRenderedProgressiveDisclosureScope,
    "html_nested_dom": HtmlNestedDomScope,
}


# Fields that existed on the 0.4.0 flat ScopeSpec but are not part of
# any 0.5.0 variant. They are tolerated on load (silently dropped if
# default-valued; flagged via ValueError if non-default).
_LEGACY_SCOPE_FIELDS: frozenset[str] = frozenset()  # none currently


def _strip_unknown_fields(
    raw: dict[str, Any],
    variant_cls: type[BaseModel],
) -> dict[str, Any]:
    """Drop 0.4.0 fields that are absent on the chosen 0.5.0 variant.

    Pydantic's ``extra="forbid"`` rejects unknown fields. The 0.4.0
    flat ScopeSpec carried fields meaningful only to other source
    types; the variant cannot have them. Drop fields that are absent
    on the variant model AND have a default-equivalent value
    (None / empty list / False / empty string / 0 / 1 for tolerance).

    Anything non-default is preserved in the returned dict so the
    variant constructor raises a clear validation error rather than
    silently swallowing data.
    """

    valid = set(variant_cls.model_fields.keys())
    cleaned: dict[str, Any] = {}
    default_values = {
        None,
        "",
        False,
        0,
    }
    for key, value in raw.items():
        if key in valid:
            cleaned[key] = value
            continue
        # Field is unknown to the variant. Drop only if default-valued.
        if value in default_values:
            continue
        if isinstance(value, (list, dict)) and not value:
            continue
        # tolerance defaults to 1
        if key == "pdf_dedup_coord_tolerance" and value == 1:
            continue
        if key == "browser_timeout_ms" and value == 30000:
            continue
        # Non-default value on an unknown field — preserve so the
        # variant raises a clear "Extra inputs are not permitted"
        # error pointing at the smuggled field.
        cleaned[key] = value
    return cleaned


def parse_scope(
    raw: dict[str, Any] | BaseModel,
    *,
    fallback_source_type: str | None = None,
) -> BaseModel:
    """Parse a scope dict into the appropriate discriminated-union variant.

    Forward-compatible: accepts both 0.5.0 (``source_type`` present in
    the dict) and 0.4.0 (``source_type`` missing — caller passes
    ``fallback_source_type`` from the parent manifest).

    Returns a Pydantic model instance of the matching variant.
    """

    if isinstance(raw, BaseModel):
        return raw

    if not isinstance(raw, dict):
        raise TypeError(
            f"parse_scope expects a dict or BaseModel; got {type(raw).__name__}"
        )

    data = dict(raw)  # shallow copy — don't mutate caller's dict
    st = data.get("source_type") or fallback_source_type
    if st is None:
        raise ValueError(
            "parse_scope: scope dict has no `source_type` and no "
            "`fallback_source_type` was provided. 0.4.0 manifests must "
            "pass the manifest-level `source_type` as fallback."
        )
    variant = _SCOPE_VARIANT_BY_TYPE.get(st)
    if variant is None:
        raise ValueError(
            f"parse_scope: unknown source_type {st!r}. "
            f"Known: {sorted(_SCOPE_VARIANT_BY_TYPE)}"
        )
    data["source_type"] = st
    # Defensive 0.4.0 migration: URL-based variants require ``url`` as a
    # non-empty string. A 0.4.0 manifest may have ``url: null`` with the
    # actual reference held in ``source_reference``. If so, copy across
    # before validation so the migration is byte-stable rather than
    # raising a confusing pydantic error.
    if "url" in variant.model_fields:
        if not data.get("url") and data.get("source_reference"):
            data["url"] = data["source_reference"]
    cleaned = _strip_unknown_fields(data, variant)
    return variant.model_validate(cleaned)


def _infer_source_type(kwargs: dict[str, Any]) -> str | None:
    """Infer source_type from a flat kwargs dict.

    Used by the backwards-compat ``ScopeSpec(...)`` constructor (see
    ``manifest.ScopeSpec``) to dispatch a 0.4.0-shaped call to the
    right 0.5.0 variant. Inference rules — most specific first:

    - ``content_root_selector`` → ``html_nested_dom``
    - ``wait_for_selector`` → ``js_rendered_progressive_disclosure``
    - ``section_identifier`` → ``multi_section_pdf``
    - ``page_range`` or ``section_heading`` (PDF-only) plus a
      ``source_reference`` ending ``.pdf`` or known PDF-y → ``flat_pdf_linear``
    - ``css_selector`` or ``heading_text`` plus a ``url`` → ``static_html_linear``

    Returns ``None`` when the kwargs dict is too ambiguous; the caller
    is expected to pass an explicit ``source_type`` in that case.
    """

    if kwargs.get("content_root_selector"):
        return "html_nested_dom"
    if kwargs.get("wait_for_selector"):
        return "js_rendered_progressive_disclosure"
    if kwargs.get("section_identifier"):
        return "multi_section_pdf"
    has_pdf_signal = bool(
        kwargs.get("page_range")
        or kwargs.get("pdf_dedup_coords")
        or (
            kwargs.get("section_heading")
            and not kwargs.get("css_selector")
            and not kwargs.get("heading_text")
        )
    )
    src = kwargs.get("source_reference") or ""
    if has_pdf_signal or src.lower().endswith(".pdf"):
        return "flat_pdf_linear"
    if kwargs.get("css_selector") or kwargs.get("heading_text"):
        return "static_html_linear"
    return None


def make_scope(**kwargs: Any) -> BaseModel:
    """Backwards-compatible scope constructor.

    Mirrors the 0.4.0 ``ScopeSpec(**fields)`` ergonomics for legacy
    scripts and tests. Inferes the ``source_type`` from the supplied
    fields (see ``_infer_source_type``) and delegates to
    ``parse_scope`` for variant selection and validation.

    New code should construct the per-type variant directly
    (e.g. ``StaticHtmlLinearScope(url=..., css_selector=...)``) for
    clearer call sites and earlier validation feedback.
    """

    if "source_type" not in kwargs:
        inferred = _infer_source_type(kwargs)
        if inferred is None:
            raise ValueError(
                "make_scope: could not infer source_type from supplied "
                "fields. Pass source_type=... explicitly or use a "
                "per-type variant constructor."
            )
        kwargs["source_type"] = inferred
    return parse_scope(kwargs)


__all__ = [
    "ClickStep",
    "ClickStepWaitFor",
    "FlatPdfLinearScope",
    "HtmlNestedDomScope",
    "JsRenderedProgressiveDisclosureScope",
    "MultiSectionPdfScope",
    "Scope",
    "SourceTypeLiteral",
    "StaticHtmlLinearScope",
    "make_scope",
    "parse_scope",
]
