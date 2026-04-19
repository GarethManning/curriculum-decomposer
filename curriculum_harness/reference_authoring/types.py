"""Dataclasses shared across the reference-authoring pipeline.

These are structurally independent from ``curriculum_harness.types`` —
the reference-authoring subsystem does not reuse harness primitives.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any

KUD_COLUMNS = ("know", "understand", "do_skill", "do_disposition")
KNOWLEDGE_TYPES = ("Type 1", "Type 2", "Type 3")
ASSESSMENT_ROUTES = (
    "rubric_with_clear_criteria",
    "reasoning_quality_rubric",
    "multi_informant_observation",
)
UNDERSPECIFICATION_FLAGS = (None, "mild", "moderate", "severe")
STABILITY_FLAGS = (
    "stable",
    "classification_unstable",
    "classification_unreliable",
)

REFERENCE_AUTHORING_VERSION = "0.2.0"

BANDS = ("A", "B", "C", "D")
CLUSTER_STABILITY_FLAGS = (
    "stable",
    "cluster_unstable",
    "cluster_unreliable",
)
LT_STABILITY_FLAGS = (
    "stable",
    "lt_set_unstable",
    "lt_set_unreliable",
)
BAND_STABILITY_FLAGS = (
    "stable",
    "band_statements_unstable",
    "band_statements_unreliable",
)
INDICATOR_STABILITY_FLAGS = (
    "stable",
    "observation_indicators_unstable",
    "observation_indicators_unreliable",
)


@dataclass
class ContentBlock:
    """One verbatim unit of source content with traceability metadata."""

    block_id: str
    raw_text: str
    block_type: str
    line_start: int
    line_end: int
    heading_path: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SourceInventory:
    source_slug: str
    snapshot_path: str
    manifest_content_hash: str
    phase0_version: str
    source_reference: str
    content_blocks: list[ContentBlock] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "reference_authoring_version": REFERENCE_AUTHORING_VERSION,
            "source_slug": self.source_slug,
            "snapshot_path": self.snapshot_path,
            "manifest_content_hash": self.manifest_content_hash,
            "phase0_version": self.phase0_version,
            "source_reference": self.source_reference,
            "content_blocks": [b.to_dict() for b in self.content_blocks],
        }


@dataclass
class KUDItem:
    """One reference KUD item with full traceability and self-consistency flags."""

    item_id: str
    kud_column: str
    knowledge_type: str
    assessment_route: str
    content_statement: str
    source_block_id: str
    classification_rationale: str
    underspecification_flag: str | None = None
    prerequisite_lts: list[str] = field(default_factory=list)
    stability_flag: str = "stable"
    per_run_classifications: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class HaltedBlock:
    """A source block whose KUD classification failed self-consistency or hit severe underspec."""

    block_id: str
    source_block_raw_text: str
    halt_reason: str
    per_run_classifications: list[dict[str, Any]] = field(default_factory=list)
    diagnostic: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ReferenceKUD:
    source_slug: str
    snapshot_path: str
    items: list[KUDItem] = field(default_factory=list)
    halted_blocks: list[HaltedBlock] = field(default_factory=list)
    classification_model: str = ""
    classification_temperature: float = 0.3
    self_consistency_runs: int = 3

    def to_dict(self) -> dict[str, Any]:
        return {
            "reference_authoring_version": REFERENCE_AUTHORING_VERSION,
            "source_slug": self.source_slug,
            "snapshot_path": self.snapshot_path,
            "classification_model": self.classification_model,
            "classification_temperature": self.classification_temperature,
            "self_consistency_runs": self.self_consistency_runs,
            "items": [i.to_dict() for i in self.items],
            "halted_blocks": [b.to_dict() for b in self.halted_blocks],
        }


@dataclass
class GateResult:
    name: str
    passed: bool
    halting: bool
    diagnostic: str
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class QualityReport:
    source_slug: str
    gate_results: list[GateResult] = field(default_factory=list)
    halted_by: str | None = None
    summary: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "reference_authoring_version": REFERENCE_AUTHORING_VERSION,
            "source_slug": self.source_slug,
            "halted_by": self.halted_by,
            "summary": self.summary,
            "gate_results": [g.to_dict() for g in self.gate_results],
        }


@dataclass
class CompetencyCluster:
    """One competency cluster grouping KUD items that together form a coherent capability."""

    cluster_id: str
    competency_name: str
    competency_definition: str
    kud_item_ids: list[str] = field(default_factory=list)
    source_block_ids: list[str] = field(default_factory=list)
    source_position_start: int = 0
    source_position_end: int = 0
    dominant_knowledge_type: str = ""
    knowledge_type_breakdown: dict[str, int] = field(default_factory=dict)
    stability_flag: str = "stable"
    per_run_signatures: list[dict[str, Any]] = field(default_factory=list)
    stability_diagnostics: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class CompetencyClusterSet:
    source_slug: str
    clusters: list[CompetencyCluster] = field(default_factory=list)
    model: str = ""
    temperature: float = 0.3
    runs: int = 3
    unassigned_kud_item_ids: list[str] = field(default_factory=list)
    overall_stability_flag: str = "stable"
    overall_stability_diagnostics: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "reference_authoring_version": REFERENCE_AUTHORING_VERSION,
            "source_slug": self.source_slug,
            "model": self.model,
            "temperature": self.temperature,
            "runs": self.runs,
            "overall_stability_flag": self.overall_stability_flag,
            "overall_stability_diagnostics": list(self.overall_stability_diagnostics),
            "unassigned_kud_item_ids": list(self.unassigned_kud_item_ids),
            "clusters": [c.to_dict() for c in self.clusters],
        }


@dataclass
class LearningTarget:
    """One Learning Target — Type 1/2 or Type 3.

    Band statements live on the Type-1/2 payload; observation indicator
    sets live on the Type-3 payload. Both are generated in later stages
    and stored on separate dataclasses so this structure stays stable
    across the LT, band-statement, and indicator stages.
    """

    lt_id: str
    cluster_id: str
    competency_name: str
    lt_name: str
    lt_definition: str
    knowledge_type: str
    assessment_route: str
    kud_item_ids: list[str] = field(default_factory=list)
    prerequisite_lts: list[str] = field(default_factory=list)
    stability_flag: str = "stable"
    per_run_signatures: list[dict[str, Any]] = field(default_factory=list)
    stability_diagnostics: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class LearningTargetSet:
    source_slug: str
    lts: list[LearningTarget] = field(default_factory=list)
    halted_clusters: list[dict[str, Any]] = field(default_factory=list)
    model: str = ""
    temperature: float = 0.3
    runs: int = 3

    def to_dict(self) -> dict[str, Any]:
        return {
            "reference_authoring_version": REFERENCE_AUTHORING_VERSION,
            "source_slug": self.source_slug,
            "model": self.model,
            "temperature": self.temperature,
            "runs": self.runs,
            "lts": [lt.to_dict() for lt in self.lts],
            "halted_clusters": list(self.halted_clusters),
        }


@dataclass
class BandStatement:
    band: str
    statement: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class BandStatementSet:
    """Band progression A-D for a single Type 1/2 LT."""

    lt_id: str
    knowledge_type: str
    statements: list[BandStatement] = field(default_factory=list)
    stability_flag: str = "stable"
    per_run_signatures: list[dict[str, Any]] = field(default_factory=list)
    stability_diagnostics: list[str] = field(default_factory=list)
    quality_gate_passed: bool = True
    quality_gate_failures: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class BandStatementCollection:
    source_slug: str
    sets: list[BandStatementSet] = field(default_factory=list)
    halted_lts: list[dict[str, Any]] = field(default_factory=list)
    model: str = ""
    temperature: float = 0.3
    runs: int = 3

    def to_dict(self) -> dict[str, Any]:
        return {
            "reference_authoring_version": REFERENCE_AUTHORING_VERSION,
            "source_slug": self.source_slug,
            "model": self.model,
            "temperature": self.temperature,
            "runs": self.runs,
            "sets": [s.to_dict() for s in self.sets],
            "halted_lts": list(self.halted_lts),
        }


@dataclass
class ObservationBand:
    """Observable indicators for one band of a Type 3 LT."""

    band: str
    observable_behaviours: list[str] = field(default_factory=list)
    self_reflection_prompt: str = ""


    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ObservationIndicatorSet:
    """Full Mode 3 observation scaffold for a single Type 3 LT."""

    lt_id: str
    bands: list[ObservationBand] = field(default_factory=list)
    parent_prompts: list[str] = field(default_factory=list)
    prerequisite_lts: list[str] = field(default_factory=list)
    developmental_conversation_protocol: str = ""
    stability_flag: str = "stable"
    per_run_signatures: list[dict[str, Any]] = field(default_factory=list)
    stability_diagnostics: list[str] = field(default_factory=list)
    quality_gate_passed: bool = True
    quality_gate_failures: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ObservationIndicatorCollection:
    source_slug: str
    sets: list[ObservationIndicatorSet] = field(default_factory=list)
    halted_lts: list[dict[str, Any]] = field(default_factory=list)
    model: str = ""
    temperature: float = 0.3
    runs: int = 3

    def to_dict(self) -> dict[str, Any]:
        return {
            "reference_authoring_version": REFERENCE_AUTHORING_VERSION,
            "source_slug": self.source_slug,
            "model": self.model,
            "temperature": self.temperature,
            "runs": self.runs,
            "sets": [s.to_dict() for s in self.sets],
            "halted_lts": list(self.halted_lts),
        }


# Mode 3 generic developmental self-reflection prompts, calibrated by
# band (per LT authoring skill). These are generic across ALL Type 3
# LTs — the LT-specific tailoring happens in the observable-behaviour
# indicators and the parent prompts, not in these developmental
# prompts.
MODE3_SELF_REFLECTION_PROMPTS: dict[str, str] = {
    "A": "Name a moment this term when you tried something hard. What happened, and how did it feel?",
    "B": "Describe one pattern you have noticed in yourself this term. When does it show up, and when does it not?",
    "C": "Compare what you have noticed in yourself with what your teacher has observed. Where do the two accounts agree, and where do they differ?",
    "D": "Analyse a pattern you see in yourself across two or more different contexts. What has shifted, and what do you think caused the shift?",
}


def dump_json(obj: Any, path: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
