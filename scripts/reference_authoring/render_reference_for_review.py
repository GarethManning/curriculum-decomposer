"""Render the full reference (KUD + LTs + bands + indicators) as a readable markdown review.

Produces ``reference-review.md`` alongside the reference corpus
artefacts. The renderer uses each source's native progression
structure (Welsh Progression Steps 1-5, US/Ontario single grade,
Scottish CfE Levels, etc.) for all band/indicator sections —
``progression_structure.json`` is required.

Usage:

    python -m scripts.reference_authoring.render_reference_for_review \\
        --corpus docs/reference-corpus/welsh-cfw-health-wellbeing

The renderer is strictly a view over the corpus JSON. It does not run
any stages. It does not consult the harness output. If a file is
missing, the corresponding section is omitted with a note.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from typing import Any

from curriculum_harness.reference_authoring.progression import (
    load_progression_structure,
)


def _load(path: str) -> dict[str, Any] | None:
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def _pct(n: int, total: int) -> str:
    if not total:
        return "n/a"
    return f"{n / total * 100:.1f}%"


def _band_order_factory(band_labels: list[str]):
    order = {label: i for i, label in enumerate(band_labels)}

    def _band_order(band: str) -> int:
        return order.get(band, 99)

    return _band_order


def render(corpus_dir: str) -> str:
    kud = _load(os.path.join(corpus_dir, "kud.json"))
    clusters = _load(os.path.join(corpus_dir, "competency_clusters.json"))
    lts = _load(os.path.join(corpus_dir, "lts.json"))
    bands = _load(os.path.join(corpus_dir, "band_statements.json"))
    indicators = _load(os.path.join(corpus_dir, "observation_indicators.json"))
    quality = _load(os.path.join(corpus_dir, "quality_report.json"))

    progression_path = os.path.join(corpus_dir, "progression_structure.json")
    if not os.path.exists(progression_path):
        return (
            "# Reference review\n\n"
            f"_Missing `progression_structure.json` at `{progression_path}`. The "
            "renderer uses each source's native band labels and does NOT "
            "default to A-D. Re-run the pipeline (or copy the structure file) "
            "before rendering._\n"
        )
    progression = load_progression_structure(progression_path)
    band_labels = list(progression.band_labels)
    _band_order = _band_order_factory(band_labels)

    if not kud:
        return "# Reference review\n\n_No `kud.json` in corpus; nothing to render._\n"

    source_slug = kud.get("source_slug", "(unknown)")
    lines: list[str] = []
    lines.append(f"# Reference review — {source_slug}")
    lines.append("")
    lines.append(
        f"Source snapshot: `{kud.get('snapshot_path', '')}`. "
        f"Classifier: `{kud.get('classification_model', '')}` at temperature "
        f"{kud.get('classification_temperature', '')} with "
        f"{kud.get('self_consistency_runs', '')}x self-consistency."
    )
    lines.append("")
    lines.append("## Progression structure (source-native)")
    lines.append("")
    lines.append(f"- **source type:** `{progression.source_type}`")
    lines.append(f"- **band count:** {progression.band_count}")
    if progression.is_single_band():
        lines.append(
            f"- **band:** {progression.band_labels[0]} (single-grade source — "
            "no progression sequence inside the source)"
        )
    else:
        lines.append(
            "- **bands (developmental order):** "
            + ", ".join(progression.band_labels)
        )
    lines.append(f"- **age range hint:** {progression.age_range_hint}")
    lines.append(
        f"- **detection confidence:** `{progression.detection_confidence}`"
    )
    if progression.uncertain():
        lines.append(
            "- **flag:** `progression_structure_uncertain` — band framework "
            "may need human verification."
        )
    lines.append(f"- **detection rationale:** {progression.detection_rationale}")
    lines.append("")

    # --- Summary ---
    lines.append("## Summary")
    lines.append("")
    kud_items: list[dict[str, Any]] = kud.get("items", [])
    halted_blocks: list[dict[str, Any]] = kud.get("halted_blocks", [])
    lts_list: list[dict[str, Any]] = (lts or {}).get("lts", [])
    cluster_list: list[dict[str, Any]] = (clusters or {}).get("clusters", [])
    band_sets: list[dict[str, Any]] = (bands or {}).get("sets", [])
    indicator_sets: list[dict[str, Any]] = (indicators or {}).get("sets", [])
    halted_clusters: list[dict[str, Any]] = (lts or {}).get("halted_clusters", [])
    halted_band_lts: list[dict[str, Any]] = (bands or {}).get("halted_lts", [])
    halted_indicator_lts: list[dict[str, Any]] = (indicators or {}).get("halted_lts", [])

    lines.append(f"- KUD items: **{len(kud_items)}**")
    lines.append(f"- Halted KUD blocks: **{len(halted_blocks)}**")
    lines.append(f"- Competency clusters: **{len(cluster_list)}**")
    if clusters:
        lines.append(
            f"  - overall stability: `{clusters.get('overall_stability_flag', '')}`"
        )
    lines.append(f"- Learning Targets: **{len(lts_list)}**")
    lt_kt_counts: Counter[str] = Counter(lt.get("knowledge_type", "") for lt in lts_list)
    lt_stab_counts: Counter[str] = Counter(lt.get("stability_flag", "") for lt in lts_list)
    lines.append(
        f"  - knowledge types: Type 1={lt_kt_counts.get('Type 1', 0)}, "
        f"Type 2={lt_kt_counts.get('Type 2', 0)}, "
        f"Type 3={lt_kt_counts.get('Type 3', 0)}"
    )
    lines.append(f"  - stability: {dict(lt_stab_counts)}")
    lines.append(f"- Band-statement sets (Type 1/2): **{len(band_sets)}**")
    band_stab: Counter[str] = Counter(bs.get("stability_flag", "") for bs in band_sets)
    lines.append(f"  - stability: {dict(band_stab)}")
    lines.append(f"- Observation indicator sets (Type 3): **{len(indicator_sets)}**")
    ind_stab: Counter[str] = Counter(s.get("stability_flag", "") for s in indicator_sets)
    lines.append(f"  - stability: {dict(ind_stab)}")
    lines.append(f"- Halted at any stage: {len(halted_blocks) + len(halted_clusters) + len(halted_band_lts) + len(halted_indicator_lts)}")
    if quality:
        if quality.get("halted_by"):
            lines.append(f"- Pipeline halted by KUD gate: `{quality['halted_by']}`")
        else:
            lines.append("- Pipeline: all KUD halting gates passed")
    lines.append("")

    # Build lookup tables.
    kud_by_id: dict[str, dict[str, Any]] = {i["item_id"]: i for i in kud_items}
    bands_by_lt: dict[str, dict[str, Any]] = {b["lt_id"]: b for b in band_sets}
    indicators_by_lt: dict[str, dict[str, Any]] = {s["lt_id"]: s for s in indicator_sets}
    lts_by_cluster: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for lt in lts_list:
        lts_by_cluster[lt.get("cluster_id", "")].append(lt)

    # --- Per-competency sections ---
    lines.append("## Competencies")
    lines.append("")
    if not cluster_list:
        lines.append("_No clusters; LTs and indicators are ungrouped._")
        lines.append("")
    for c in cluster_list:
        cid = c.get("cluster_id", "")
        lines.append(f"### {c.get('competency_name', '(unnamed)')} — `{cid}`")
        lines.append("")
        lines.append(f"**Definition.** {c.get('competency_definition', '')}")
        lines.append("")
        lines.append(
            f"**Dominant knowledge type:** {c.get('dominant_knowledge_type', '')}. "
            f"**Stability:** `{c.get('stability_flag', '')}`. "
            f"**Source lines:** L{c.get('source_position_start', '?')}-{c.get('source_position_end', '?')}. "
            f"**KUD items:** {len(c.get('kud_item_ids', []))}."
        )
        if c.get("stability_diagnostics"):
            lines.append("")
            lines.append("_Stability diagnostics:_")
            for d in c["stability_diagnostics"]:
                lines.append(f"- {d}")
        lines.append("")

        # KUD items in this cluster (compact table)
        lines.append("#### KUD items")
        lines.append("")
        lines.append("| Item ID | Type | Column | Content |")
        lines.append("|---|---|---|---|")
        for iid in c.get("kud_item_ids", []):
            it = kud_by_id.get(iid)
            if not it:
                lines.append(f"| `{iid}` | ? | ? | (not found) |")
                continue
            lines.append(
                "| `{iid}` | {kt} | {col} | {content} |".format(
                    iid=iid,
                    kt=it.get("knowledge_type", ""),
                    col=it.get("kud_column", ""),
                    content=_escape(it.get("content_statement", ""))[:200],
                )
            )
        lines.append("")

        # LTs in this cluster
        lines.append("#### Learning Targets")
        lines.append("")
        for lt in lts_by_cluster.get(cid, []):
            lt_id = lt.get("lt_id", "")
            lines.append(f"##### {lt.get('lt_name', '')} — `{lt_id}`")
            lines.append("")
            lines.append(f"**Definition.** {lt.get('lt_definition', '')}")
            lines.append("")
            lines.append(
                f"**Knowledge type:** {lt.get('knowledge_type', '')}. "
                f"**Assessment route:** `{lt.get('assessment_route', '')}`. "
                f"**Stability:** `{lt.get('stability_flag', '')}`."
            )
            if lt.get("prerequisite_lts"):
                lines.append("")
                lines.append(
                    f"**Prerequisites:** "
                    + ", ".join(f"`{p}`" for p in lt.get("prerequisite_lts", []))
                )
            lines.append("")
            lines.append(
                "**KUD items covered:** "
                + ", ".join(f"`{x}`" for x in lt.get("kud_item_ids", []))
            )
            lines.append("")

            kt = lt.get("knowledge_type", "")
            if kt in ("Type 1", "Type 2"):
                bs = bands_by_lt.get(lt_id)
                if not bs:
                    lines.append("_No band statements produced._")
                    lines.append("")
                    continue
                gate = "PASS" if bs.get("quality_gate_passed", True) else "FAIL"
                progression_label = (
                    "Single-grade band"
                    if progression.is_single_band()
                    else "Band progression"
                )
                lines.append(
                    f"**{progression_label}** — stability `{bs.get('stability_flag', '')}`, "
                    f"quality gate **{gate}**."
                )
                if bs.get("quality_gate_failures"):
                    lines.append("")
                    lines.append(
                        "_Gate failures:_ " + ", ".join(bs.get("quality_gate_failures", []))
                    )
                lines.append("")
                lines.append("| Band | Statement |")
                lines.append("|---|---|")
                for bstatement in sorted(
                    bs.get("statements", []), key=lambda x: _band_order(x.get("band", ""))
                ):
                    lines.append(
                        f"| {bstatement.get('band', '')} | {_escape(bstatement.get('statement', ''))} |"
                    )
                lines.append("")
            elif kt == "Type 3":
                iset = indicators_by_lt.get(lt_id)
                if not iset:
                    lines.append("_No observation indicator set produced._")
                    lines.append("")
                    continue
                gate = "PASS" if iset.get("quality_gate_passed", True) else "FAIL"
                lines.append(
                    f"**Observation protocol** — stability `{iset.get('stability_flag', '')}`, "
                    f"Mode 3 gate **{gate}**."
                )
                if iset.get("quality_gate_failures"):
                    lines.append("")
                    lines.append(
                        "_Gate failures:_ " + ", ".join(iset.get("quality_gate_failures", []))
                    )
                if iset.get("prerequisite_lts"):
                    lines.append("")
                    lines.append(
                        "_Prerequisites (knowledge-contingent Type 3):_ "
                        + ", ".join(f"`{p}`" for p in iset.get("prerequisite_lts", []))
                    )
                lines.append("")
                for band in sorted(
                    iset.get("bands", []), key=lambda x: _band_order(x.get("band", ""))
                ):
                    lines.append(f"**{band.get('band', '')}**")
                    lines.append("")
                    for be in band.get("observable_behaviours", []):
                        lines.append(f"- {_escape(be)}")
                    lines.append("")
                    lines.append(
                        "_Self-reflection prompt (calibrated to this source's "
                        f"own developmental expectations at {band.get('band', '')}):_ "
                        + _escape(band.get("self_reflection_prompt", ""))
                    )
                    lines.append("")
                lines.append("**Parent / caregiver prompts**")
                lines.append("")
                for p in iset.get("parent_prompts", []):
                    lines.append(f"- {_escape(p)}")
                lines.append("")
                lines.append(
                    "**Developmental conversation protocol.** "
                    + _escape(iset.get("developmental_conversation_protocol", ""))
                )
                lines.append("")
            else:
                lines.append("_Unknown knowledge type; no band statements or indicators._")
                lines.append("")

    # --- Halted items ---
    any_halted = (
        bool(halted_blocks)
        or bool(halted_clusters)
        or bool(halted_band_lts)
        or bool(halted_indicator_lts)
    )
    if any_halted:
        lines.append("## Halted items")
        lines.append("")
        if halted_blocks:
            lines.append("### KUD halted blocks")
            lines.append("")
            for h in halted_blocks:
                lines.append(
                    f"- `{h.get('block_id', '')}` — {h.get('halt_reason', '')}: "
                    + _escape(h.get("diagnostic", ""))
                )
            lines.append("")
        if halted_clusters:
            lines.append("### LT stage halted clusters")
            lines.append("")
            for h in halted_clusters:
                lines.append(
                    f"- `{h.get('cluster_id', '')}` — {h.get('halt_reason', '')}: "
                    + _escape(str(h.get("diagnostic", "")))
                )
            lines.append("")
        if halted_band_lts:
            lines.append("### Band-statement stage halted LTs")
            lines.append("")
            for h in halted_band_lts:
                lines.append(
                    f"- `{h.get('lt_id', '')}` ({h.get('lt_name', '')}) — "
                    f"{h.get('halt_reason', '')}: "
                    + _escape(str(h.get("diagnostic", "")))
                )
                if h.get("failures"):
                    lines.append(f"  - failures: {h.get('failures')}")
            lines.append("")
        if halted_indicator_lts:
            lines.append("### Observation-indicator stage halted LTs")
            lines.append("")
            for h in halted_indicator_lts:
                lines.append(
                    f"- `{h.get('lt_id', '')}` ({h.get('lt_name', '')}) — "
                    f"{h.get('halt_reason', '')}: "
                    + _escape(str(h.get("diagnostic", "")))
                )
                if h.get("failures"):
                    lines.append(f"  - failures: {h.get('failures')}")
            lines.append("")

    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--corpus",
        required=True,
        help="Path to the reference-corpus directory.",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output markdown path (defaults to <corpus>/reference-review.md).",
    )
    args = parser.parse_args(argv)
    out = args.out or os.path.join(args.corpus, "reference-review.md")
    markdown = render(args.corpus)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(markdown)
    print(f"[reference-review] wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
