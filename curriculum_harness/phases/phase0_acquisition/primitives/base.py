"""Primitive base interface.

A primitive is a small deterministic callable with a declared scope
schema and a declared set of side-effects. Primitives compose into
sequences that the type detector routes a source through.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


class ScopeValidationError(Exception):
    """Raised when a scope spec is missing required fields for a primitive.

    Phase 0 catches this and writes a user-in-the-loop request file
    describing exactly which fields the user must provide.
    """

    def __init__(self, primitive: str, missing: list[str], message: str = ""):
        self.primitive = primitive
        self.missing = missing
        super().__init__(
            message
            or (
                f"Primitive '{primitive}' requires scope fields: "
                f"{', '.join(missing)}"
            )
        )


@dataclass
class PrimitiveResult:
    """Uniform return type for a primitive.

    ``output`` is the primary payload passed to the next primitive.
    ``summary`` is a small dict recorded in the manifest trace (no large
    blobs). ``meta`` carries primitive-specific structured facts (fetch
    status code, encoding detected, hash value) that later primitives
    may need or that belong in the manifest.
    """

    output: Any
    summary: dict[str, Any] = field(default_factory=dict)
    meta: dict[str, Any] = field(default_factory=dict)


class Primitive(Protocol):
    """Callable primitive interface.

    Attributes:
        name: Stable identifier recorded in the manifest.
        required_scope_fields: ``ScopeSpec`` fields this primitive needs.
        optional_scope_fields: Fields the primitive reads if present.
        side_effects: Tags — any of ``{"network", "fs_read", "fs_write",
            "user_prompt"}``.
    """

    name: str
    required_scope_fields: tuple[str, ...]
    optional_scope_fields: tuple[str, ...]
    side_effects: frozenset[str]

    def validate_scope(self, scope: Any) -> None:
        """Raise ``ScopeValidationError`` if required fields are missing."""
        ...

    def run(self, scope: Any, previous: PrimitiveResult | None) -> PrimitiveResult:
        """Execute the primitive and return a ``PrimitiveResult``."""
        ...


def check_required_scope(
    primitive_name: str,
    scope: Any,
    required: tuple[str, ...],
) -> None:
    """Shared helper — raise ``ScopeValidationError`` if any required
    field on ``scope`` is None or empty string."""
    missing: list[str] = []
    for field_name in required:
        value = getattr(scope, field_name, None)
        if value is None or (isinstance(value, str) and not value.strip()):
            missing.append(field_name)
    if missing:
        raise ScopeValidationError(primitive_name, missing)
