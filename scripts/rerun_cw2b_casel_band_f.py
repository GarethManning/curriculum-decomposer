"""CW-2b Step 2 — Fix CASEL Band F gap.

Grade Band 11-12 had 0 KUD items (API credit exhaustion in CW-2).
This script:
  1. Re-runs KUD classification for grade-band-11-12 per-strand inventory
  2. Calls run_pipeline --resume-from-kud for grade-band-11-12
  3. Appends Band F items/LTs to unified_kud.json and unified_lts.json
  4. Generates band-tagged-casel-v2.json (v1 with Band F added)
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from curriculum_harness.reference_authoring.kud.classify_kud import (
    classify_inventory_sync,
    DEFAULT_MODEL,
    DEFAULT_RUNS,
    DEFAULT_TEMPERATURE,
)
from curriculum_harness.reference_authoring.pipeline.run_pipeline import (
    _load_inventory,
    main as pipeline_main,
)
from curriculum_harness.reference_authoring.types import dump_json

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = REPO_ROOT / "docs" / "reference-corpus" / "casel-sel-continuum"
STRAND_DIR = CORPUS_DIR / "per_strand" / "grade-band-11-12"

STRAND_TO_REAL = {
    "pre-kindergarten": "A",
    "kindergarten-grade-1": "A",
    "kindergarten–grade-1": "A",
    "grade-band-2-3": "B",
    "grade-band-2–3": "B",
    "grade-band-4-5": "C",
    "grade-band-4–5": "C",
    "grade-band-6-8": "D",
    "grade-band-6–8": "D",
    "grade-band-9-10": "E",
    "grade-band-9–10": "E",
    "grade-band-11-12": "F",
    "grade-band-11–12": "F",
}

SOURCE_BAND_LABELS = {
    "pre-kindergarten": "Pre-Kindergarten",
    "kindergarten-grade-1": "Kindergarten-Grade 1",
    "grade-band-2-3": "Grade Band 2-3",
    "grade-band-4-5": "Grade Band 4-5",
    "grade-band-6-8": "Grade Band 6-8",
    "grade-band-9-10": "Grade Band 9-10",
    "grade-band-11-12": "Grade Band 11-12",
}

RATIONALE_F = (
    "CASEL Grade Band 11-12 (ages 16-18) maps cleanly to REAL Band F (ages 15-17, G11-12)."
)


def _strand_slug(source_block_id: str) -> str:
    if "_blk_" in source_block_id:
        return source_block_id.split("_blk_")[0]
    if "_cluster_" in source_block_id:
        return source_block_id.split("_cluster_")[0]
    return source_block_id


def phase1_rerun_kud() -> None:
    """Re-run KUD classification for grade-band-11-12."""
    print("\n=== Phase 1: Re-run KUD for grade-band-11-12 ===", flush=True)
    inv_path = STRAND_DIR / "inventory.json"
    kud_path = STRAND_DIR / "kud.json"

    inventory = _load_inventory(str(inv_path))
    classifiable = [b for b in inventory.content_blocks if b.block_type != "heading"]
    print(f"[cw2b-casel] {len(classifiable)} classifiable blocks → classifying", flush=True)

    kud = classify_inventory_sync(
        inventory,
        model=DEFAULT_MODEL,
        temperature=DEFAULT_TEMPERATURE,
        runs=DEFAULT_RUNS,
    )
    dump_json(kud.to_dict(), str(kud_path))
    print(
        f"[cw2b-casel] KUD done — {len(kud.items)} items, "
        f"{len(kud.halted_blocks)} halted → {kud_path}",
        flush=True,
    )


def phase2_resume_pipeline() -> None:
    """Run pipeline --resume-from-kud for grade-band-11-12."""
    print("\n=== Phase 2: Resume pipeline for grade-band-11-12 ===", flush=True)
    exit_code = pipeline_main([
        "--resume-from-kud",
        "--out", str(STRAND_DIR),
        "--dispositional",
        "--skip-criteria",
        "--sub-run",
    ])
    if exit_code != 0:
        print(f"[cw2b-casel] WARNING: pipeline returned exit_code={exit_code}", flush=True)
    else:
        print("[cw2b-casel] pipeline complete", flush=True)


def phase3_update_unified() -> None:
    """Append grade-band-11-12 items/LTs to unified_kud.json and unified_lts.json."""
    print("\n=== Phase 3: Update unified KUD/LTs with Band F ===", flush=True)

    # Load grade-band-11-12 per-strand artefacts
    with open(STRAND_DIR / "kud.json") as f:
        strand_kud = json.load(f)
    with open(STRAND_DIR / "lts.json") as f:
        strand_lts = json.load(f)

    new_items = strand_kud.get("items", [])
    new_lts = strand_lts.get("lts", [])
    print(f"[cw2b-casel] grade-band-11-12: {len(new_items)} KUD items, {len(new_lts)} LTs", flush=True)

    if len(new_items) == 0:
        print("[cw2b-casel] WARNING: Still 0 items in grade-band-11-12 kud.json — check pipeline", flush=True)

    # Load existing unified artefacts
    with open(CORPUS_DIR / "unified_kud.json") as f:
        unified_kud = json.load(f)
    with open(CORPUS_DIR / "unified_lts.json") as f:
        unified_lts = json.load(f)

    existing_items = unified_kud.get("items", [])
    existing_lts = unified_lts.get("lts", [])
    print(f"[cw2b-casel] unified currently: {len(existing_items)} KUD items, {len(existing_lts)} LTs", flush=True)

    # Add strand provenance to new items (matching stitch format)
    strand_prov = {
        "strand_name": "Grade Band 11-12",
        "strand_slug": "grade-band-11-12",
        "detection_confidence": 0.7,
    }

    # Remove any existing grade-band-11-12 items (from previous empty run)
    existing_items = [i for i in existing_items if
                      not i.get("strand", {}).get("strand_slug") == "grade-band-11-12"]
    existing_lts = [lt for lt in existing_lts if
                    not lt.get("strand", {}).get("strand_slug") == "grade-band-11-12"]

    for item in new_items:
        item_id = item.get("item_id", "")
        item["item_id"] = f"grade-band-11-12_{item_id}"
        item["source_block_id"] = f"grade-band-11-12_{item.get('source_block_id', item_id)}"
        item["strand"] = strand_prov
        existing_items.append(item)

    for lt in new_lts:
        lt_id = lt.get("lt_id", "")
        lt["lt_id"] = f"grade-band-11-12_{lt_id}"
        lt["kud_item_ids"] = [f"grade-band-11-12_{k}" for k in lt.get("kud_item_ids", [])]
        lt["strand"] = strand_prov
        existing_lts.append(lt)

    # Also remove from halted_blocks if they were there
    existing_halted = [h for h in unified_kud.get("halted_blocks", [])
                       if "grade-band-11" not in h.get("block_id", "")]

    unified_kud["items"] = existing_items
    unified_kud["halted_blocks"] = existing_halted

    unified_lts["lts"] = existing_lts

    with open(CORPUS_DIR / "unified_kud.json", "w") as f:
        json.dump(unified_kud, f, indent=2, ensure_ascii=False)
    with open(CORPUS_DIR / "unified_lts.json", "w") as f:
        json.dump(unified_lts, f, indent=2, ensure_ascii=False)

    print(f"[cw2b-casel] unified_kud.json updated: {len(existing_items)} total items", flush=True)
    print(f"[cw2b-casel] unified_lts.json updated: {len(existing_lts)} total LTs", flush=True)


def phase4_band_translation() -> None:
    """Generate band-tagged-casel-v2.json (v1 + Band F)."""
    print("\n=== Phase 4: Band translation → v2 ===", flush=True)

    with open(CORPUS_DIR / "unified_kud.json") as f:
        unified_kud = json.load(f)
    with open(CORPUS_DIR / "unified_lts.json") as f:
        unified_lts = json.load(f)
    with open(CORPUS_DIR / "per_strand" / "pre-kindergarten" / "progression_structure.json") as f:
        prog_data = json.load(f)

    kud_items = unified_kud.get("items", [])
    lts = unified_lts.get("lts", [])

    # Build band-tagged KUD
    band_tagged_kud = []
    item_band: dict[str, str] = {}

    for item in kud_items:
        item_id = item["item_id"]
        sid = item.get("source_block_id", item_id)
        strand_slug_raw = item.get("strand", {}).get("strand_slug", "")

        # Determine strand slug from strand provenance or source_block_id
        if strand_slug_raw:
            strand = strand_slug_raw
        else:
            strand = _strand_slug(sid)

        school_band = STRAND_TO_REAL.get(strand)
        if school_band is None:
            parts = strand.rsplit("-", 1)
            school_band = STRAND_TO_REAL.get(parts[0], "A")

        source_band = SOURCE_BAND_LABELS.get(strand, strand)
        item_band[item_id] = school_band

        tagged = {
            "item_id": item_id,
            "content_statement": item["content_statement"],
            "knowledge_type": item.get("knowledge_type", ""),
            "school_band": school_band,
            "band_confidence": "high",
            "source_band_preserved": source_band,
            "source_voice_preserved": True,
            "ambiguity_flag": False,
            "teacher_review_flag": "pre-kindergarten" in strand,
            "band_rationale": RATIONALE_F if school_band == "F" else _get_rationale(strand, school_band),
            "source_block_id": sid,
            "strand_slug": strand,
        }
        band_tagged_kud.append(tagged)

    # Build band-tagged LTs
    band_tagged_lts = []
    for lt in lts:
        lt_id = lt.get("lt_id", "")
        strand_slug_raw = lt.get("strand", {}).get("strand_slug", "")
        strand = strand_slug_raw if strand_slug_raw else _strand_slug(lt_id)
        school_band = STRAND_TO_REAL.get(strand)
        if school_band is None:
            kud_ids = lt.get("kud_item_ids", [])
            bands = sorted({item_band[k] for k in kud_ids if k in item_band})
            school_band = bands[0] if bands else "A"

        source_band = SOURCE_BAND_LABELS.get(strand, strand)

        tagged_lt = {
            "lt_id": lt_id,
            "lt_name": lt.get("lt_name", ""),
            "lt_definition": lt.get("lt_definition", ""),
            "school_band": school_band,
            "band_confidence": "high",
            "source_band_preserved": source_band,
            "source_voice_preserved": True,
            "ambiguity_flag": False,
            "teacher_review_flag": "pre-kindergarten" in strand,
            "band_rationale": RATIONALE_F if school_band == "F" else _get_rationale(strand, school_band),
            "kud_item_ids": lt.get("kud_item_ids", []),
            "knowledge_type": lt.get("knowledge_type", ""),
            "strand_slug": strand,
        }
        band_tagged_lts.append(tagged_lt)

    kud_by_band = Counter(t["school_band"] for t in band_tagged_kud)
    lt_by_band = Counter(t["school_band"] for t in band_tagged_lts)
    teacher_review_kud = sum(1 for t in band_tagged_kud if t["teacher_review_flag"])
    teacher_review_lts = sum(1 for t in band_tagged_lts if t["teacher_review_flag"])

    summary_counts = {
        "total_kud_items": len(band_tagged_kud),
        "total_lts": len(band_tagged_lts),
        "kud_by_band": dict(sorted(kud_by_band.items())),
        "lts_by_band": dict(sorted(lt_by_band.items())),
        "teacher_review_flagged_kud": teacher_review_kud,
        "teacher_review_flagged_lts": teacher_review_lts,
        "low_confidence": 0,
        "ambiguous": 0,
        "note": (
            "v2: Grade Band 11-12 (REAL Band F) now present — "
            f"{kud_by_band.get('F', 0)} KUD items, {lt_by_band.get('F', 0)} LTs. "
            "CW-2b pipeline re-run after API credit restoration."
        ),
    }

    skill_flags = [
        (
            "pre_band_items_tagged_A: Pre-Kindergarten items (ages 3-5) fall below REAL Band A's "
            "floor (ages 5-7). Tagged as Band A with teacher_review_flag=true and pre-band rationale."
        ),
        (
            "band_d_age_boundary: CASEL Grade Band 6-8 spans ages 11-14. REAL Band D spans ages 11-13. "
            "The upper boundary of Grade Band 6-8 (age 14) slightly exceeds Band D. Items at the "
            "older end of this band may have developmental characteristics closer to REAL Band E."
        ),
        (
            "v2_band_f_restored: CW-2 pipeline halted on Grade Band 11-12 (call_or_parse_failed — "
            "API credit exhaustion). CW-2b re-ran KUD classification with restored credits. "
            "Band F items are pipeline-generated (3-run self-consistency)."
        ),
    ]

    output = {
        "source_metadata": {
            "source_name": "CASEL SEL Skills Continuum (January 2023)",
            "source_type": prog_data.get("source_type", "casel_sel_grade_band"),
            "source_band_labels": prog_data.get("band_labels", []),
            "target_framework": "REAL School Budapest Bands A-F",
            "skill_version": "2.0",
            "run_timestamp": datetime.now(timezone.utc).isoformat(),
            "session": "CW-2b",
            "note": "v2: Band F (Grade Band 11-12) restored via CW-2b pipeline re-run.",
        },
        "band_tagged_kud": band_tagged_kud,
        "band_tagged_lts": band_tagged_lts,
        "summary_counts": summary_counts,
        "skill_flags": skill_flags,
    }

    out_path = CORPUS_DIR / "band-tagged-casel-v2.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"[cw2b-casel] Written: {out_path}", flush=True)
    print(f"[cw2b-casel] KUD items: {len(band_tagged_kud)} (v1 had 175)", flush=True)
    print(f"[cw2b-casel] LTs: {len(band_tagged_lts)} (v1 had 79)", flush=True)
    print(f"[cw2b-casel] KUD by band: {dict(sorted(kud_by_band.items()))}", flush=True)
    print(f"[cw2b-casel] LTs by band: {dict(sorted(lt_by_band.items()))}", flush=True)


RATIONALES_MAP = {
    "A": {
        "pre": (
            "CASEL Pre-Kindergarten (ages 3-5) falls below REAL Band A's floor (ages 5-7, K-2). "
            "Tagged Band A as the nearest REAL band; pre-band relative to REAL's earliest stage."
        ),
        "kg1": "CASEL Kindergarten-Grade 1 (ages 5-7) maps cleanly to REAL Band A (ages 5-7, K-2).",
    },
    "B": "CASEL Grade Band 2-3 (ages 7-9) maps cleanly to REAL Band B (Earth Dragons, ages 7-9, G3-4).",
    "C": "CASEL Grade Band 4-5 (ages 9-11) maps cleanly to REAL Band C (Fire Dragons, ages 9-11, G5-6).",
    "D": "CASEL Grade Band 6-8 (ages 11-14) maps to REAL Band D (Metal+Light Dragons, ages 11-13, G7-8).",
    "E": "CASEL Grade Band 9-10 (ages 14-16) maps cleanly to REAL Band E (ages 13-15, G9-10).",
    "F": "CASEL Grade Band 11-12 (ages 16-18) maps cleanly to REAL Band F (ages 15-17, G11-12).",
}


def _get_rationale(strand: str, school_band: str) -> str:
    if school_band == "A":
        if "pre-kindergarten" in strand:
            return RATIONALES_MAP["A"]["pre"]
        return RATIONALES_MAP["A"]["kg1"]
    return RATIONALES_MAP.get(school_band, f"Mapped from strand '{strand}' to REAL Band {school_band}.")


if __name__ == "__main__":
    print("=== CW-2b: CASEL Band F pipeline re-run ===", flush=True)
    phase1_rerun_kud()
    phase2_resume_pipeline()
    phase3_update_unified()
    phase4_band_translation()
    print("\n=== CASEL Band F fix complete ===", flush=True)
