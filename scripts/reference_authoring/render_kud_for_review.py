"""Render a reference KUD as a human-readable markdown review document.

Reads ``kud.json`` from a reference-corpus directory and emits
``kud-review.md`` alongside it. The review document is what Gareth
reads at a session checkpoint to react to pipeline output.

Usage:

    python -m scripts.reference_authoring.render_kud_for_review \\
        --corpus docs/reference-corpus/welsh-cfw-health-wellbeing
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from typing import Any


_COLUMN_ORDER = ("know", "understand", "do_skill", "do_disposition")
_COLUMN_LABELS = {
    "know": "Know",
    "understand": "Understand",
    "do_skill": "Do-Skill",
    "do_disposition": "Do-Disposition",
}
_HALT_LABELS = {
    "severe_underspecification": "Severe underspecification",
    "classification_unreliable": "Classification unreliable (≤1/3 agreement)",
}


def _load_kud(corpus_dir: str) -> dict[str, Any]:
    path = os.path.join(corpus_dir, "kud.json")
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _load_inventory(corpus_dir: str) -> dict[str, Any] | None:
    path = os.path.join(corpus_dir, "inventory.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _load_quality_report(corpus_dir: str) -> dict[str, Any] | None:
    path = os.path.join(corpus_dir, "quality_report.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _pct(n: int, total: int) -> str:
    if not total:
        return "n/a"
    return f"{n / total * 100:.1f}%"


def _escape_md(text: str) -> str:
    # Minimal escaping for table cells: newlines → space, pipes → \|.
    return (text or "").replace("\n", " ").replace("|", "\\|").strip()


def _block_excerpt(inventory: dict[str, Any] | None, block_id: str) -> str:
    if not inventory:
        return "(inventory not available)"
    for block in inventory.get("content_blocks", []):
        if block.get("block_id") == block_id:
            text = block.get("raw_text", "")
            line_start = block.get("line_start")
            line_end = block.get("line_end")
            span = f"L{line_start}" if line_start == line_end else f"L{line_start}-{line_end}"
            return f"`{block_id}` {span}: {text}"
    return f"`{block_id}`: (not found in inventory)"


def _flag_summary(item: dict[str, Any]) -> str:
    parts: list[str] = []
    stab = item.get("stability_flag")
    if stab and stab != "stable":
        parts.append(stab)
    usf = item.get("underspecification_flag")
    if usf:
        parts.append(f"underspec:{usf}")
    prereqs = item.get("prerequisite_lts") or []
    if prereqs:
        parts.append(f"prereqs:{len(prereqs)}")
    return ", ".join(parts) if parts else "—"


def render_review(corpus_dir: str) -> str:
    kud = _load_kud(corpus_dir)
    inventory = _load_inventory(corpus_dir)
    quality = _load_quality_report(corpus_dir)

    items: list[dict[str, Any]] = kud.get("items", [])
    halted: list[dict[str, Any]] = kud.get("halted_blocks", [])
    total = len(items)

    type_counts: Counter[str] = Counter(i.get("knowledge_type", "") for i in items)
    col_counts: Counter[str] = Counter(i.get("kud_column", "") for i in items)
    stab_counts: Counter[str] = Counter(i.get("stability_flag", "") for i in items)
    usf_counts: Counter[str] = Counter(
        (i.get("underspecification_flag") or "null") for i in items
    )
    halt_reason_counts: Counter[str] = Counter(h.get("halt_reason", "") for h in halted)

    lines: list[str] = []
    lines.append(f"# Reference KUD review — {kud.get('source_slug', '(unknown)')}")
    lines.append("")
    lines.append(
        f"Source snapshot: `{kud.get('snapshot_path', '')}`. "
        f"Classifier: `{kud.get('classification_model', '')}` at temperature "
        f"{kud.get('classification_temperature', '')} with "
        f"{kud.get('self_consistency_runs', '')}x self-consistency."
    )
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total KUD items: **{total}**")
    lines.append(f"- Halted blocks: **{len(halted)}**")
    if quality and quality.get("halted_by"):
        lines.append(f"- Pipeline halted by gate: `{quality['halted_by']}`")
    elif quality:
        lines.append("- Pipeline gates: all halting gates passed")
    lines.append("")
    lines.append("### Knowledge-type distribution")
    lines.append("")
    lines.append("| Type | Count | Percentage |")
    lines.append("|---|---|---|")
    for t in ("Type 1", "Type 2", "Type 3"):
        lines.append(f"| {t} | {type_counts.get(t, 0)} | {_pct(type_counts.get(t, 0), total)} |")
    lines.append("")
    lines.append("### KUD column distribution")
    lines.append("")
    lines.append("| Column | Count | Percentage |")
    lines.append("|---|---|---|")
    for c in _COLUMN_ORDER:
        lines.append(
            f"| {_COLUMN_LABELS[c]} | {col_counts.get(c, 0)} | {_pct(col_counts.get(c, 0), total)} |"
        )
    lines.append("")
    lines.append("### Classification stability")
    lines.append("")
    lines.append("| Stability flag | Count |")
    lines.append("|---|---|")
    for flag, count in stab_counts.most_common():
        lines.append(f"| {flag} | {count} |")
    lines.append("")
    lines.append("### Underspecification flags")
    lines.append("")
    lines.append("| Flag | Count |")
    lines.append("|---|---|")
    for flag, count in sorted(usf_counts.items()):
        lines.append(f"| {flag} | {count} |")
    lines.append("")
    if halt_reason_counts:
        lines.append("### Halted blocks by reason")
        lines.append("")
        lines.append("| Reason | Count |")
        lines.append("|---|---|")
        for reason, count in halt_reason_counts.most_common():
            label = _HALT_LABELS.get(reason, reason)
            lines.append(f"| {label} | {count} |")
        lines.append("")

    # Four column sections.
    for column in _COLUMN_ORDER:
        col_items = [i for i in items if i.get("kud_column") == column]
        lines.append(f"## {_COLUMN_LABELS[column]} ({len(col_items)})")
        lines.append("")
        if not col_items:
            lines.append("_No items in this column._")
            lines.append("")
            continue
        lines.append(
            "| Item ID | Content | Knowledge type | Assessment route | Source | Flags |"
        )
        lines.append("|---|---|---|---|---|---|")
        for i in col_items:
            src_excerpt = _block_excerpt(inventory, i.get("source_block_id", ""))
            lines.append(
                "| `{item_id}` | {content} | {kt} | `{route}` | {src} | {flags} |".format(
                    item_id=i.get("item_id", ""),
                    content=_escape_md(i.get("content_statement", "")),
                    kt=i.get("knowledge_type", ""),
                    route=i.get("assessment_route", ""),
                    src=_escape_md(src_excerpt)[:160],
                    flags=_flag_summary(i),
                )
            )
        lines.append("")
        # Per-item rationales (so the review is actionable)
        lines.append("### Rationales")
        lines.append("")
        for i in col_items:
            lines.append(
                f"- **`{i.get('item_id', '')}`** — {_escape_md(i.get('classification_rationale', ''))}"
            )
            prereqs = i.get("prerequisite_lts") or []
            if prereqs:
                lines.append(f"  - prerequisites: {', '.join(f'`{p}`' for p in prereqs)}")
        lines.append("")

    # Halted blocks.
    if halted:
        lines.append(f"## Halted blocks ({len(halted)})")
        lines.append("")
        lines.append(
            "These inventory blocks produced no KUD items. "
            "Severe underspecification = pure meta/navigation content. "
            "Classification unreliable = ≤1/3 self-consistency agreement across 3 runs."
        )
        lines.append("")
        for h in halted:
            lines.append(f"### `{h.get('block_id', '')}` — {h.get('halt_reason', '')}")
            lines.append("")
            lines.append(f"**Source:** {_escape_md(h.get('source_block_raw_text', ''))}")
            lines.append("")
            lines.append(f"**Diagnostic:** {_escape_md(h.get('diagnostic', ''))}")
            lines.append("")
            runs = h.get("per_run_classifications") or []
            if runs:
                lines.append("Per-run observations:")
                for r in runs:
                    ok = r.get("ok")
                    if not ok:
                        lines.append(f"- run {r.get('run')}: failed ({r.get('diagnostic', '')})")
                    else:
                        sig = r.get("items_signature", [])
                        sig_str = (
                            ", ".join(f"{s.get('kud_column')}/{s.get('knowledge_type')}" for s in sig)
                            if sig
                            else "(no items — severe underspec)"
                        )
                        lines.append(
                            f"- run {r.get('run')}: flag={r.get('underspecification_flag')}, items=[{sig_str}]"
                        )
                lines.append("")

    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--corpus",
        required=True,
        help="Path to the reference-corpus directory (contains kud.json).",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output markdown path (defaults to <corpus>/kud-review.md).",
    )
    args = parser.parse_args(argv)

    out = args.out or os.path.join(args.corpus, "kud-review.md")
    markdown = render_review(args.corpus)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(markdown)
    print(f"[kud-review] wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
