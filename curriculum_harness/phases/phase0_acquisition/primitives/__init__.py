"""Phase 0 extraction primitives.

Primitives are deterministic callables. No primitive in this package may
invoke an LLM — extraction must be rule-based. The type detector
(``curriculum_harness.phases.phase0_acquisition.type_detector``) is the
only place where a model call is permitted, and only for classification,
never for extraction.
"""
