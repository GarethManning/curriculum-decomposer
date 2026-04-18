"""SHA-256 content-hash primitive.

Deterministic. Hashes the UTF-8 encoded bytes of the content string.
Downstream consumers use this to detect "this source changed since we
last acquired it" without re-running the pipeline.
"""

from __future__ import annotations

import hashlib

from curriculum_harness.phases.phase0_acquisition.primitives.base import (
    PrimitiveResult,
)


class ContentHashPrimitive:
    name = "content_hash"
    required_scope_fields: tuple[str, ...] = ()
    optional_scope_fields: tuple[str, ...] = ()
    side_effects: frozenset[str] = frozenset()

    def validate_scope(self, scope) -> None:
        return None

    def run(self, scope, previous: PrimitiveResult | None) -> PrimitiveResult:
        text = "" if previous is None else str(previous.output or "")
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        return PrimitiveResult(
            output=text,
            summary={"content_hash": digest, "bytes": len(text.encode("utf-8"))},
            meta={"content_hash": digest},
        )
