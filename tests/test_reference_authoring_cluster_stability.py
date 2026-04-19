"""Deterministic tests for the competency-clustering stability check.

The stability check is a pure function of three clustering runs. These
tests exercise the behaviour without any Anthropic calls.
"""

from __future__ import annotations

from curriculum_harness.reference_authoring.lt.cluster_competencies import (
    _check_stability,
    _membership_drift,
    _align_clusters,
    MEMBERSHIP_DRIFT_THRESHOLD,
)


def _make_run(clusters: list[tuple[str, str, list[str]]]) -> list[dict]:
    return [
        {
            "competency_name": name,
            "competency_definition": f"definition for {name}",
            "dominant_knowledge_type": dkt,
            "kud_item_ids": list(members),
            "source_section_label": name,
        }
        for name, dkt, members in clusters
    ]


def test_stability_all_three_runs_identical() -> None:
    run = _make_run([
        ("Physical Health", "Type 3", ["i1", "i2", "i3"]),
        ("Mental Health", "Type 3", ["i4", "i5"]),
    ])
    diagnostics, alignments = _check_stability(runs=[run, run, run])
    assert diagnostics == []
    assert alignments == [[0, 1], [0, 1]]


def test_stability_cluster_count_differs() -> None:
    r1 = _make_run([
        ("Phys", "Type 3", ["i1", "i2"]),
        ("Mental", "Type 3", ["i3", "i4"]),
    ])
    r2 = _make_run([
        ("Combined", "Type 3", ["i1", "i2", "i3", "i4"]),
    ])
    r3 = _make_run([
        ("Phys", "Type 3", ["i1", "i2"]),
        ("Mental", "Type 3", ["i3", "i4"]),
    ])
    diagnostics, _ = _check_stability(runs=[r1, r2, r3])
    assert any("cluster_count_differs" in d for d in diagnostics)


def test_stability_membership_drift_triggers_flag() -> None:
    # 4 items, run2 reassigns 2 of 4 (50% drift > 20% threshold)
    r1 = _make_run([
        ("A", "Type 1", ["i1", "i2"]),
        ("B", "Type 3", ["i3", "i4"]),
    ])
    r2 = _make_run([
        ("A", "Type 1", ["i1", "i3"]),
        ("B", "Type 3", ["i2", "i4"]),
    ])
    diagnostics, _ = _check_stability(runs=[r1, r2, r1])
    assert any("membership_drift" in d for d in diagnostics)


def test_stability_dominant_type_drift() -> None:
    r1 = _make_run([
        ("A", "Type 3", ["i1", "i2"]),
        ("B", "Type 1", ["i3", "i4"]),
    ])
    r2 = _make_run([
        ("A", "Type 1", ["i1", "i2"]),  # dominant type flipped
        ("B", "Type 1", ["i3", "i4"]),
    ])
    diagnostics, _ = _check_stability(runs=[r1, r2, r1])
    assert any("dominant_type_drift" in d for d in diagnostics)


def test_stability_unmatched_cluster() -> None:
    r1 = _make_run([
        ("A", "Type 3", ["i1", "i2"]),
        ("B", "Type 3", ["i3", "i4"]),
    ])
    # run2 loses cluster B entirely (all members reassigned elsewhere
    # so its best-Jaccard candidate falls below threshold)
    r2 = _make_run([
        ("A", "Type 3", ["i1", "i2", "i3", "i4"]),
    ])
    diagnostics, _ = _check_stability(runs=[r1, r2, r1])
    assert any("cluster_missing_in_run" in d or "cluster_count_differs" in d
               for d in diagnostics)


def test_jaccard_alignment_matches_by_best_score() -> None:
    canonical = [["i1", "i2", "i3"], ["i4", "i5"]]
    other = [["i4", "i5"], ["i1", "i2", "i3"]]
    align = _align_clusters(canonical, other)
    assert align == [1, 0]


def test_membership_drift_zero_for_identical_runs() -> None:
    r = [["i1", "i2"], ["i3", "i4"]]
    assert _membership_drift(r, r) == 0.0


def test_membership_drift_fraction() -> None:
    # Swap i2 and i3 between clusters — 2 of 4 items drift (50%)
    r1 = [["i1", "i2"], ["i3", "i4"]]
    r2 = [["i1", "i3"], ["i2", "i4"]]
    drift = _membership_drift(r1, r2)
    assert drift > MEMBERSHIP_DRIFT_THRESHOLD
    assert abs(drift - 0.5) < 1e-9
