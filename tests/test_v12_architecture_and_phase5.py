"""v1.2: ArchitectureStrand migration and Phase 5 strand mapping."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from curriculum_harness.phases.phase5_formatting import map_lt_to_strand_label, _level_statement_validation_flags
from curriculum_harness.types import ArchitectureDiagnosis, ArchitectureStrand

REPO_ROOT = Path(__file__).resolve().parent.parent
UK_CONFIG = REPO_ROOT / "configs" / "uk_national_curriculum_history_v1_0.json"


def test_legacy_horizontal_migrates_to_content_theme() -> None:
    legacy = {
        "architecture_type": "mixed",
        "proportions": {"hierarchical": 0.4, "horizontal": 0.4, "dispositional": 0.2},
        "hierarchical_elements": ["Chronological concepts"],
        "horizontal_elements": ["Church State Relations Perspective", "Reformation Lens"],
        "dispositional_elements": ["Historical curiosity"],
        "structural_flaw": "",
        "auto_assessable_pct": 0.5,
    }
    d = ArchitectureDiagnosis.from_dict(legacy)
    assert len(d.strands) == 4
    hz = [s for s in d.strands if s.lane == "content_theme"]
    assert len(hz) == 2
    assert all("legacy horizontal_elements" in s.values_basis for s in hz)
    analytical = [s for s in d.strands if s.lane == "horizontal_analytical"]
    assert analytical == []


def test_t2_never_maps_to_content_theme_strand() -> None:
    strands = [
        ArchitectureStrand(
            id="church",
            label="Church State Relations",
            lane="content_theme",
            expected_lt_types=[],
            values_basis="Topic strand.",
        ),
        ArchitectureStrand(
            id="think",
            label="Historical Thinking",
            lane="horizontal_analytical",
            expected_lt_types=[2],
            values_basis="Skills.",
        ),
    ]
    lt = {
        "type": 2,
        "knowledge_type": "horizontal",
        "statement": "I can evaluate the reliability of historical sources about religion and state.",
        "kud_source": "understand: interpretation",
    }
    label, _ = map_lt_to_strand_label(lt, strands)
    assert label == "Historical Thinking"


def test_t3_only_dispositional_candidates() -> None:
    strands = [
        ArchitectureStrand(
            id="t",
            label="Topics",
            lane="content_theme",
            expected_lt_types=[],
            values_basis="x",
        ),
        ArchitectureStrand(
            id="h",
            label="Historical Thinking",
            lane="horizontal_analytical",
            expected_lt_types=[2],
            values_basis="x",
        ),
        ArchitectureStrand(
            id="d",
            label="Curiosity disposition",
            lane="dispositional",
            expected_lt_types=[3],
            values_basis="x",
        ),
    ]
    lt = {
        "type": 3,
        "knowledge_type": "dispositional",
        "statement": "I can show curiosity when encountering unfamiliar historical accounts.",
        "kud_source": "do: curiosity",
    }
    label, _ = map_lt_to_strand_label(lt, strands)
    assert label == "Curiosity disposition"


def test_level_statement_drift_flags_required() -> None:
    bad_domain = _level_statement_validation_flags(
        "History",
        1,
        {"ks1": "I can describe basic rules in my community and school"},
    )
    assert "LEVEL_STATEMENT_DOMAIN_DRIFT" in bad_domain

    bad_type = _level_statement_validation_flags(
        "History",
        3,
        {"ks3": "I can evaluate the reliability and perspective of different historical sources"},
    )
    assert "LEVEL_STATEMENT_TYPE_DRIFT" in bad_type

    clean = _level_statement_validation_flags(
        "History",
        3,
        {"ks3": "I can show curiosity when presented with unfamiliar historical stories"},
    )
    assert "LEVEL_STATEMENT_DOMAIN_DRIFT" not in clean
    assert "LEVEL_STATEMENT_TYPE_DRIFT" not in clean


def _latest_run_artifact(out_dir: Path, run_id: str, artifact_base: str, ext: str) -> Path | None:
    """Newest `{run_id}_{artifact_base}_v{n}.{ext}` by mtime."""
    rid = (run_id or "run").strip() or "run"
    paths = sorted(
        out_dir.glob(f"{rid}_{artifact_base}_v*.{ext.lstrip('.')}"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return paths[0] if paths else None


@pytest.mark.integration
def test_uk_nc_full_pipeline_v12_invariants(tmp_path: Path) -> None:
    import asyncio
    import csv
    import os

    if not os.environ.get("ANTHROPIC_API_KEY"):
        pytest.skip("ANTHROPIC_API_KEY required for full pipeline integration test")

    if not UK_CONFIG.is_file():
        pytest.skip("UK config missing")

    cfg = json.loads(UK_CONFIG.read_text(encoding="utf-8"))
    out_path = tmp_path / "out"
    cfg["outputPath"] = str(out_path)
    cfg["checkpointDb"] = str(tmp_path / "cp.db")
    run_id = "test_uk_nc_v12_integration"
    cfg["runId"] = run_id

    async def _run() -> None:
        from curriculum_harness.graph import build_initial_state, compile_graph

        st = build_initial_state(str(UK_CONFIG), cfg)
        st["output_structure"] = cfg.get("outputStructure")
        cp = Path(st["checkpoint_db_resolved"])
        graph = await compile_graph(cp)
        # Return value is only the last node's update — read artifacts from disk instead.
        await graph.ainvoke(dict(st), config={"configurable": {"thread_id": st["run_id"]}})

    asyncio.run(_run())

    csv_path = _latest_run_artifact(out_path, run_id, "structured_lts", "csv")
    assert csv_path and csv_path.is_file(), f"structured_lts CSV not found under {out_path}"

    arch_path = _latest_run_artifact(out_path, run_id, "architecture", "json")
    assert arch_path and arch_path.is_file(), f"architecture JSON not found under {out_path}"

    arch = json.loads(arch_path.read_text(encoding="utf-8"))
    diag = ArchitectureDiagnosis.from_dict(arch)
    label_to_lane = {s.label: s.lane for s in diag.strands}

    lt_path = _latest_run_artifact(out_path, run_id, "learning_targets", "json")
    t2_lts: list[dict] = []
    if lt_path and lt_path.is_file():
        lt_data = json.loads(lt_path.read_text(encoding="utf-8"))
        t2_lts = [
            lt
            for lt in (lt_data.get("learning_targets") or [])
            if int(lt.get("type") or 0) == 2
        ]

    structured: list[dict[str, str]] = []
    with open(csv_path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            structured.append({k: (v or "") for k, v in row.items()})

    assert structured, "structured_lts CSV has no data rows — pipeline incomplete"
    analytical = [s for s in diag.strands if s.lane == "horizontal_analytical"]
    if t2_lts and not analytical:
        pytest.fail(
            "Phase 2 produced no horizontal_analytical strands but T2 LTs exist — "
            "check MCP JSON / Phase 2 strands output"
        )
    if t2_lts:
        t2_rows = [r for r in structured if r.get("Knowledge Type", "").strip() == "T2"]
        assert t2_rows, "T2 LTs existed but none in structured CSV (strand assignment dropped all T2)"

    # (a) no T2 LT assigned to content_theme strand
    for row in structured:
        if row.get("Knowledge Type", "").strip() != "T2":
            continue
        comp = row.get("Competency", "").strip()
        lane = label_to_lane.get(comp)
        assert lane is not None, f"(a) competency {comp!r} not in architecture strands"
        assert lane != "content_theme", f"(a) T2 row mapped to content_theme: {comp}"
        assert lane == "horizontal_analytical", f"(a) T2 expected horizontal_analytical, got {lane}"

    # (b) T3 LTs assigned only to dispositional strands
    for row in structured:
        if row.get("Knowledge Type", "").strip() != "T3":
            continue
        comp = row.get("Competency", "").strip()
        lane = label_to_lane.get(comp)
        assert lane is not None, f"(b) competency {comp!r} not in architecture strands"
        assert lane == "dispositional", f"(b) T3 expected dispositional, got {lane} for {comp}"

    # (c) level statement columns preserve anchor knowledge type (no drift flags)
    for row in structured:
        flags_raw = row.get("Flags", "").strip()
        flags = [x.strip() for x in flags_raw.split("|") if x.strip()]
        lt_name = row.get("LT Name", "")
        assert "LEVEL_STATEMENT_TYPE_DRIFT" not in flags, (
            f"(c) LEVEL_STATEMENT_TYPE_DRIFT in row {lt_name!r}: {flags}"
        )
        assert "LEVEL_STATEMENT_DOMAIN_DRIFT" not in flags, (
            f"(c) LEVEL_STATEMENT_DOMAIN_DRIFT in row {lt_name!r}: {flags}"
        )
