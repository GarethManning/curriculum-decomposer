"""Brief B Steps 2+3 assembly (inline-Opus run).

Model-discipline deviation (logged): decomposition (Step 2) and tagging
(Step 3) are performed by the in-session Opus agent, not via the Sonnet/Opus
API, because the account's API credit is exhausted. Decomposition on Opus is
faithful to the brief; tagging was briefed for Sonnet and here runs on Opus
(subscription) instead — a cost/model deviation, not a quality one. Primary
CASEL tag and developmental band are deterministic from the source document
and grade band, so only secondary-CASEL and strategy-link suggestions carry
model judgement.

This module does the DETERMINISTIC assembly around the agent's judgement:
- source_verbatim, casel_competency (primary), developmental_band, and
  provenance are pulled FROM THE CORPUS by benchmark_id — never retyped — so
  every target's verbatim trace is exact by construction (audit HIGH-1).
- The agent supplies only: split statements, derivation marker, optional
  secondary CASEL, strategy-link names, modality.

Usage (per batch):
    from build_targets import append_batch
    append_batch([
      {"benchmark_id": "MN.SA.LG1.K-3.01",
       "targets": [
          {"statement": "...", "derivation": "derived",
           "casel_secondary": "", "strategy_links": ["Think with Your Eyes"]},
       ]},
    ])
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from curriculum_harness.types import LearningTarget, MODALITY_VALUES  # noqa: E402

CORPUS = ROOT / "source" / "extractions" / "mn-sel-benchmarks-2026-07-06-v1.json"
MASTER = ROOT / "output" / "mn-sel-targets-2026-07-06-v1.json"

# Grade-band → developmental band. 1:1 orientation mapping of Minnesota's OWN
# published grade bands. Orientation aid, NOT a placement rule. Deliberately
# neutral labels — no external framework's band scheme.
BAND_MAP = [
    ("kindergarten", "Band 1 (K–3)"),
    ("4", "Band 2 (Grades 4–5)"),
    ("6", "Band 3 (Grades 6–8)"),
    ("9", "Band 4 (Grades 9–12)"),
]

# Controlled Social Thinking vocabulary — NAMES ONLY (no teaching content).
# Any strategy_link outside this set is rejected, to prevent inventing content.
STRATEGY_VOCAB = {
    "Smart Guess", "Think with Your Eyes", "Expected/Unexpected",
    "Hidden Rules", "Group Plan", "ILAUGHS", "Whole Body Listening",
    "Thinking Thoughts and Feeling Feelings", "Thinking About You / Thinking About Others",
    "Size of the Problem", "Social Behavior Mapping", "Flexible vs. Stuck Thinking",
    "The Group Plan vs. My Own Plan", "Blue Thoughts and Red Thoughts",
    "Body in the Group", "Brain in the Group", "Perspective Taking",
}


def _band_for(grade_band: str) -> str:
    gb = grade_band.lower()
    for needle, label in BAND_MAP:
        if needle in gb:
            return label
    return "Band ? (unmapped)"


def load_corpus() -> dict:
    data = json.loads(CORPUS.read_text(encoding="utf-8"))
    return {b["benchmark_id"]: b for b in data["benchmarks"]}


def _load_master() -> list:
    if MASTER.exists():
        return json.loads(MASTER.read_text(encoding="utf-8")).get("targets", [])
    return []


def append_batch(batch: list[dict]) -> dict:
    corpus = load_corpus()
    targets = _load_master()
    existing_ids = {t["target_id"] for t in targets}
    added = []
    for entry in batch:
        bid = entry["benchmark_id"]
        if bid not in corpus:
            raise KeyError(f"unknown benchmark_id: {bid}")
        b = corpus[bid]
        specs = entry["targets"]
        for i, spec in enumerate(specs, start=1):
            deriv = spec.get("derivation", "pass-through")
            if deriv not in ("pass-through", "derived"):
                raise ValueError(f"{bid}: bad derivation {deriv!r}")
            # modality rule: source-preserved pass-through targets are decided;
            # derived (re-phrased on split) are proposed pending clinician review.
            modality = spec.get("modality") or ("decided" if deriv == "pass-through" else "proposed")
            if modality not in MODALITY_VALUES:
                raise ValueError(f"{bid}: bad modality {modality!r}")
            for name in spec.get("strategy_links", []):
                if name not in STRATEGY_VOCAB:
                    raise ValueError(f"{bid}: strategy '{name}' not in controlled vocab")
            sec = (spec.get("casel_secondary") or "").strip()
            tid = f"{bid}-t{i:02d}"
            if tid in existing_ids:
                raise ValueError(f"duplicate target_id {tid}")
            existing_ids.add(tid)
            lt = LearningTarget.from_dict({
                "statement": spec["statement"],
                "source_benchmark_id": bid,
                "source_verbatim": b["benchmark_verbatim"],   # from corpus — exact
                "casel_competency": b["casel_competency"],     # from source doc — authoritative
                "casel_secondary": sec,
                "developmental_band": _band_for(b["grade_band"]),
                "strategy_links": [{"name": n, "modality": "proposed"} for n in spec.get("strategy_links", [])],
                "modality": modality,
                "flags": [deriv],
            })
            obj = lt.to_dict()
            obj["target_id"] = tid
            obj["provenance"] = {
                "source_doc": b["source_doc"],
                "page": b["page"],
                "casel_competency": b["casel_competency"],
                "learning_goal_num": b["learning_goal_num"],
                "learning_goal": b["learning_goal"],
                "grade_band": b["grade_band"],
                "benchmark_id": bid,
                "benchmark_verbatim": b["benchmark_verbatim"],
            }
            # integrity: verbatim trace must be exact
            assert obj["source_verbatim"] == b["benchmark_verbatim"]
            targets.append(obj)
            added.append(obj)
    _write(targets)
    return {"added": len(added), "total": len(targets), "objects": added}


def _write(targets: list) -> None:
    corpus_meta = json.loads(CORPUS.read_text(encoding="utf-8"))
    payload = {
        "generated": "2026-07-06",
        "version": "v1",
        "run": "Brief B inline-Opus (Steps 2+3); Step 1 deterministic",
        "band_note": ("developmental_band is a 1:1 orientation mapping of Minnesota's own "
                      "published grade bands (K–3→Band 1, 4–5→Band 2, 6–8→Band 3, 9–12→Band 4). "
                      "Orientation aid, NOT a placement rule."),
        "modality_note": ("pass-through targets = decided (source wording preserved); "
                          "derived targets = proposed (re-phrased on split, clinician confirms). "
                          "Every strategy_link = proposed pending Kari."),
        "source_benchmarks_total": corpus_meta["total_benchmarks"],
        "targets_total": len(targets),
        "targets": targets,
    }
    MASTER.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def reset() -> None:
    if MASTER.exists():
        MASTER.unlink()


if __name__ == "__main__":
    c = load_corpus()
    print(f"corpus: {len(c)} benchmarks; master exists: {MASTER.exists()}")
