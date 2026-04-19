"""Run the Type 1/2 criterion + supporting-components stages only.

Reads an existing reference corpus's ``lts.json`` and
``progression_structure.json``, runs the criterion generator, applies
the criterion gates, runs the supporting-components generator for
rubrics that passed, and writes:

- ``criteria.json`` — RubricCollection (gate-annotated)
- ``criteria_quality_report.json`` / ``criteria_quality_report.md``
- ``supporting_components.json``

It does NOT touch inventory.json, kud.json, competency_clusters.json,
lts.json, band_statements.json, or observation_indicators.json. It is
the appropriate tool for adding Type 1/2 criterion artefacts to a
corpus that was generated before the criterion stage existed.

Usage:

    python -m scripts.reference_authoring.run_criteria \\
        --corpus docs/reference-corpus/common-core-g7-rp/

Optional:

    --runs N            self-consistency runs per LT (default 3)
    --model NAME        override model (default Haiku)
    --skip-supporting   skip supporting-components stage
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from dotenv import load_dotenv

from curriculum_harness.reference_authoring.criterion.generate_criteria import (
    DEFAULT_MODEL,
    DEFAULT_RUNS,
    generate_criteria_sync,
)
from curriculum_harness.reference_authoring.criterion.generate_supporting_components import (
    generate_supporting_components_sync,
)
from curriculum_harness.reference_authoring.gates.criterion_gates import (
    criterion_report_to_markdown,
    run_criterion_gates,
)
from curriculum_harness.reference_authoring.progression import (
    load_progression_structure,
)
from curriculum_harness.reference_authoring.types import (
    LearningTarget,
    LearningTargetSet,
    RubricCollection,
    dump_json,
)


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True, help="Path to a reference-corpus directory.")
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--skip-supporting", action="store_true")
    return parser.parse_args(argv)


def _load_lt_set(path: str) -> LearningTargetSet:
    with open(path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
    return LearningTargetSet(
        source_slug=raw["source_slug"],
        model=raw.get("model", ""),
        temperature=raw.get("temperature", 0.3),
        runs=raw.get("runs", 3),
        lts=[LearningTarget(**lt) for lt in raw.get("lts", [])],
        halted_clusters=list(raw.get("halted_clusters", [])),
    )


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    load_dotenv()

    corpus = os.path.abspath(args.corpus)
    lts_path = os.path.join(corpus, "lts.json")
    progression_path = os.path.join(corpus, "progression_structure.json")
    if not os.path.exists(lts_path) or not os.path.exists(progression_path):
        print(
            f"[refauth:criteria] missing lts.json or progression_structure.json under {corpus}",
            flush=True,
        )
        return 2

    lt_set = _load_lt_set(lts_path)
    progression = load_progression_structure(progression_path)
    type12_count = sum(
        1 for lt in lt_set.lts if lt.knowledge_type in ("Type 1", "Type 2")
    )
    print(
        f"[refauth:criteria] corpus={corpus}; {type12_count} Type 1/2 LT(s); "
        f"bands={progression.band_labels}",
        flush=True,
    )

    print(f"[refauth:criteria] generating rubrics (runs={args.runs}, model={args.model})", flush=True)
    rubric_coll = generate_criteria_sync(
        lt_set, progression, runs=args.runs, model=args.model
    )
    dump_json(rubric_coll.to_dict(), os.path.join(corpus, "criteria.json"))
    print(
        f"[refauth:criteria] rubrics: {len(rubric_coll.rubrics)} "
        f"(halted: {len(rubric_coll.halted_lts)})",
        flush=True,
    )

    print("[refauth:criteria] running criterion gates", flush=True)
    report, rubric_coll = run_criterion_gates(rubric_coll)
    dump_json(
        report.to_dict(),
        os.path.join(corpus, "criteria_quality_report.json"),
    )
    with open(
        os.path.join(corpus, "criteria_quality_report.md"),
        "w",
        encoding="utf-8",
    ) as fh:
        fh.write(criterion_report_to_markdown(report))
    dump_json(rubric_coll.to_dict(), os.path.join(corpus, "criteria.json"))

    gate_failed = sum(1 for r in rubric_coll.rubrics if not r.quality_gate_passed)
    judge_fail = sum(
        1 for r in rubric_coll.rubrics
        if (r.competent_framing_flag or "").lower() == "fail"
    )
    thin = sum(1 for r in rubric_coll.rubrics if r.propositional_lt_rubric_thin_flag)
    print(
        f"[refauth:criteria] gate summary: {gate_failed} halting fails; "
        f"judge_fail={judge_fail}; propositional_thin={thin}",
        flush=True,
    )

    if args.skip_supporting:
        print("[refauth:criteria] --skip-supporting set; stopping.", flush=True)
        return 0

    passing_rubrics = [r for r in rubric_coll.rubrics if r.quality_gate_passed]
    print(
        f"[refauth:criteria] generating supporting components for "
        f"{len(passing_rubrics)} passing rubric(s)",
        flush=True,
    )
    passing_coll = RubricCollection(
        source_slug=rubric_coll.source_slug,
        rubrics=passing_rubrics,
        halted_lts=list(rubric_coll.halted_lts),
        model=rubric_coll.model,
        temperature=rubric_coll.temperature,
        runs=rubric_coll.runs,
    )
    supporting_coll = generate_supporting_components_sync(
        lt_set, passing_coll, runs=args.runs, model=args.model
    )
    dump_json(
        supporting_coll.to_dict(),
        os.path.join(corpus, "supporting_components.json"),
    )
    print(
        f"[refauth:criteria] supporting components: {len(supporting_coll.components)} "
        f"(halted: {len(supporting_coll.halted_lts)})",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
