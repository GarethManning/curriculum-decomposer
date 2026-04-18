"""Phase 0 — content acquisition layer.

Phase 0 takes a source reference (URL or file) and a structured scope
specification, and produces a clean scoped content artefact plus a
manifest describing exactly how it was acquired. Phase 0 is upstream of
Phase 1; downstream phases consume the content text files, not raw
URLs.

Architecture (binding — see Session 4a-0 brief, 2026-04-18):

1. Composable primitives, not monolithic per-source modules.
2. Structured scope specs with per-primitive required-field schemas.
3. Manifest JSON separate from content text files.
4. No model calls inside extraction primitives (deterministic only).
5. User-in-the-loop with hand-editable session state and resumability.
6. SHA-256 content hash for change detection.
7. Full acquisition trace in the manifest.
8. UTF-8 normalised text output with encoding flagged on failure.
"""

from curriculum_harness.phases.phase0_acquisition.manifest import (
    AcquisitionManifest,
    PrimitiveTraceEntry,
    ScopeSpec,
    UserInteraction,
)
from curriculum_harness.phases.phase0_acquisition.primitives.base import (
    Primitive,
    PrimitiveResult,
    ScopeValidationError,
)

__all__ = [
    "AcquisitionManifest",
    "PrimitiveTraceEntry",
    "ScopeSpec",
    "UserInteraction",
    "Primitive",
    "PrimitiveResult",
    "ScopeValidationError",
]
