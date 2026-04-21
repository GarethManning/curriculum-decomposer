"""CW-2b Step 1 — Re-run Circle Solutions through the full harness pipeline.

All 4 year-level strands had 0 KUD items (API credit exhaustion in CW-2).
This script:
  1. Re-runs KUD classification for each per-strand inventory
  2. Calls run_pipeline --resume-from-kud for each strand
  3. Stitches unified corpus artefacts
  4. Generates band-tagged-circle-solutions-v2.json

Circle Solutions year-level → REAL band mapping:
  Year 2  → [A, B], ambiguity_flag=True
  Year 6  → C,      ambiguity_flag=False
  Year 9  → [D, E], ambiguity_flag=True
  Year 12 → F,      ambiguity_flag=False
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
from curriculum_harness.reference_authoring.strand.detect_strands import (
    StrandDetectionResult,
    StrandResult,
)
from curriculum_harness.reference_authoring.strand.stitch import stitch_corpora
from curriculum_harness.reference_authoring.types import dump_json

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = REPO_ROOT / "docs" / "reference-corpus" / "circle-solutions-sel"
PER_STRAND_ROOT = CORPUS_DIR / "per_strand"

STRAND_SLUGS = ["year-2", "year-6", "year-9", "year-12"]
STRAND_NAMES = {
    "year-2": "YEAR 2",
    "year-6": "YEAR 6",
    "year-9": "YEAR 9",
    "year-12": "YEAR 12",
}

YEAR_TO_REAL = {
    "year-2":  {"band": ["A", "B"], "ambiguity_flag": True,  "confidence": "medium"},
    "year-6":  {"band": "C",        "ambiguity_flag": False, "confidence": "high"},
    "year-9":  {"band": ["D", "E"], "ambiguity_flag": True,  "confidence": "medium"},
    "year-12": {"band": "F",        "ambiguity_flag": False, "confidence": "high"},
}

BAND_RATIONALES = {
    "year-2": (
        "Circle Solutions Year 2 (ages 6-7) spans REAL Bands A (ages 5-7) and B (ages 7-9). "
        "The year-level marker falls at the Band A/B boundary; tagged [A, B] with ambiguity_flag=true."
    ),
    "year-6": (
        "Circle Solutions Year 6 (ages 10-11) maps cleanly to REAL Band C (Fire Dragons, "
        "ages 9-11, G5-6). Single-band assignment; high confidence."
    ),
    "year-9": (
        "Circle Solutions Year 9 (ages 13-14) spans REAL Bands D (ages 11-13) and E (ages 13-15). "
        "Age 13-14 falls at the Band D/E boundary; tagged [D, E] with ambiguity_flag=true."
    ),
    "year-12": (
        "Circle Solutions Year 12 (ages 16-17) maps cleanly to REAL Band F (ages 15-17, G11-12). "
        "Single-band assignment; high confidence."
    ),
}


def _strand_slug_from_item_id(item_id: str) -> str:
    """Extract year-level slug from prefixed item_id: 'year-2_blk_0003_item_01' → 'year-2'."""
    for slug in STRAND_SLUGS:
        if item_id.startswith(f"{slug}_"):
            return slug
    for slug in STRAND_SLUGS:
        if slug in item_id:
            return slug
    return "year-2"


def _reconstruct_strand_result() -> StrandDetectionResult:
    """Reconstruct StrandDetectionResult from strand_detection.json."""
    sd_path = CORPUS_DIR / "strand_detection.json"
    with open(sd_path) as f:
        sd = json.load(f)
    strands = [
        StrandResult(
            name=s["name"],
            line_start=s["line_start"],
            line_end=s["line_end"],
            confidence=s["confidence"],
            signals=s.get("signals", []),
        )
        for s in sd["strands"]
    ]
    return StrandDetectionResult(
        is_multi_strand=sd["is_multi_strand"],
        strands=strands,
        single_strand_rationale=sd.get("single_strand_rationale"),
        overall_confidence=sd["overall_confidence"],
        flags=sd.get("flags", []),
    )


def phase1_rerun_kud() -> None:
    """Re-run KUD classification for all 4 year-level strands."""
    print("\n=== Phase 1: Re-run KUD classification ===", flush=True)
    for slug in STRAND_SLUGS:
        strand_dir = PER_STRAND_ROOT / slug
        inv_path = strand_dir / "inventory.json"
        kud_path = strand_dir / "kud.json"

        print(f"\n[cw2b] {slug}: loading inventory ({inv_path})", flush=True)
        inventory = _load_inventory(str(inv_path))
        classifiable = [b for b in inventory.content_blocks if b.block_type != "heading"]
        print(f"[cw2b] {slug}: {len(classifiable)} classifiable blocks → classifying", flush=True)

        kud = classify_inventory_sync(
            inventory,
            model=DEFAULT_MODEL,
            temperature=DEFAULT_TEMPERATURE,
            runs=DEFAULT_RUNS,
        )
        dump_json(kud.to_dict(), str(kud_path))
        print(
            f"[cw2b] {slug}: KUD done — {len(kud.items)} items, "
            f"{len(kud.halted_blocks)} halted → {kud_path}",
            flush=True,
        )


def phase2_resume_pipeline() -> None:
    """Run pipeline --resume-from-kud for each strand."""
    print("\n=== Phase 2: Resume pipeline (clustering → band statements) ===", flush=True)
    for slug in STRAND_SLUGS:
        strand_dir = PER_STRAND_ROOT / slug
        print(f"\n[cw2b] {slug}: running pipeline --resume-from-kud", flush=True)
        exit_code = pipeline_main([
            "--resume-from-kud",
            "--out", str(strand_dir),
            "--dispositional",
            "--skip-criteria",
            "--sub-run",
        ])
        if exit_code != 0:
            print(f"[cw2b] WARNING: pipeline returned exit_code={exit_code} for {slug}", flush=True)
        else:
            print(f"[cw2b] {slug}: pipeline complete", flush=True)


def phase3_stitch() -> None:
    """Stitch per-strand outputs into unified corpus."""
    print("\n=== Phase 3: Stitch unified corpus ===", flush=True)
    per_strand_dirs = {slug: str(PER_STRAND_ROOT / slug) for slug in STRAND_SLUGS}
    strand_result = _reconstruct_strand_result()
    strand_names_lower = {slug: STRAND_NAMES[slug] for slug in STRAND_SLUGS}
    ledger_by_strand = {slug: {} for slug in STRAND_SLUGS}

    ok, failures = stitch_corpora(
        per_strand_dirs=per_strand_dirs,
        unified_out_dir=str(CORPUS_DIR),
        strand_result=strand_result,
        strand_slugs=STRAND_SLUGS,
        strand_names=strand_names_lower,
        ledger_by_strand=ledger_by_strand,
    )
    if failures:
        print(f"[cw2b] Stitch sanity failures: {failures}", flush=True)
    else:
        print("[cw2b] Stitch complete — all sanity checks passed", flush=True)


def phase4_band_translation() -> None:
    """Generate band-tagged-circle-solutions-v2.json from unified pipeline output."""
    print("\n=== Phase 4: Band translation → v2 ===", flush=True)
    unified_kud_path = CORPUS_DIR / "unified_kud.json"
    unified_lts_path = CORPUS_DIR / "unified_lts.json"

    with open(unified_kud_path) as f:
        unified_kud = json.load(f)
    with open(unified_lts_path) as f:
        unified_lts = json.load(f)

    kud_items = unified_kud.get("items", [])
    lt_items = unified_lts.get("lts", [])
    halted = unified_kud.get("halted_blocks", [])

    print(f"[cw2b] unified KUD: {len(kud_items)} items, {len(halted)} halted", flush=True)
    print(f"[cw2b] unified LTs: {len(lt_items)}", flush=True)

    band_tagged_kud = []
    for item in kud_items:
        item_id = item["item_id"]
        slug = item.get("strand", {}).get("strand_slug") or _strand_slug_from_item_id(item_id)
        band_info = YEAR_TO_REAL[slug]
        rationale = BAND_RATIONALES[slug]
        tagged = {
            "item_id": item_id,
            "content_statement": item["content_statement"],
            "knowledge_type": item["knowledge_type"],
            "school_band": band_info["band"],
            "band_confidence": band_info["confidence"],
            "source_band_preserved": STRAND_NAMES.get(slug, slug),
            "source_voice_preserved": True,
            "ambiguity_flag": band_info["ambiguity_flag"],
            "teacher_review_flag": band_info["ambiguity_flag"],
            "band_rationale": rationale,
            "source_block_id": item.get("source_block_id", ""),
            "strand_slug": slug,
            "pipeline_generated": True,
        }
        band_tagged_kud.append(tagged)

    band_tagged_lts = []
    for lt in lt_items:
        lt_id = lt["lt_id"]
        slug = lt.get("strand", {}).get("strand_slug") or ""
        for s in STRAND_SLUGS:
            if lt_id.startswith(f"{s}_"):
                slug = s
                break
        band_info = YEAR_TO_REAL.get(slug, YEAR_TO_REAL["year-2"])
        rationale = BAND_RATIONALES.get(slug, "")
        tagged_lt = {
            "lt_id": lt_id,
            "lt_name": lt.get("lt_name", ""),
            "lt_definition": lt.get("lt_definition", ""),
            "school_band": band_info["band"],
            "band_confidence": band_info["confidence"],
            "source_band_preserved": STRAND_NAMES.get(slug, slug),
            "source_voice_preserved": True,
            "ambiguity_flag": band_info["ambiguity_flag"],
            "teacher_review_flag": band_info["ambiguity_flag"],
            "band_rationale": rationale,
            "kud_item_ids": lt.get("kud_item_ids", []),
            "knowledge_type": lt.get("knowledge_type", ""),
            "strand_slug": slug,
            "pipeline_generated": True,
        }
        band_tagged_lts.append(tagged_lt)

    def band_key(b):
        return "+".join(b) if isinstance(b, list) else b

    kud_by_band = Counter(band_key(t["school_band"]) for t in band_tagged_kud)
    lt_by_band = Counter(band_key(t["school_band"]) for t in band_tagged_lts)
    teacher_review_kud = sum(1 for t in band_tagged_kud if t["teacher_review_flag"])
    medium_conf = sum(1 for t in band_tagged_kud if t["band_confidence"] == "medium")

    summary_counts = {
        "total_kud_items": len(band_tagged_kud),
        "total_lts": len(band_tagged_lts),
        "kud_by_band": dict(sorted(kud_by_band.items())),
        "lts_by_band": dict(sorted(lt_by_band.items())),
        "teacher_review_flagged_kud": teacher_review_kud,
        "teacher_review_flagged_lts": sum(1 for t in band_tagged_lts if t["teacher_review_flag"]),
        "medium_confidence": medium_conf,
        "high_confidence": len(band_tagged_kud) - medium_conf,
        "halted_blocks_in_pipeline": len(halted),
    }

    skill_flags = [
        (
            "sparse_source_structure: Circle Solutions provides observable indicators at only 4 year "
            "levels (Year 2, 6, 9, 12). REAL Bands B (Earth Dragons, G3-4), C/D boundary, and E/F "
            "boundary are not explicitly represented. Gaps between checkpoints require teacher "
            "interpolation. This is an honest structural limitation of the source, not a quality failure."
        ),
        (
            "year_2_ambiguity: Year 2 (ages 6-7) straddles REAL Bands A and B. Items tagged [A, B] "
            "with ambiguity_flag=true and teacher_review_flag=true. Teacher judgment required to "
            "assign to a specific REAL band for planning purposes."
        ),
        (
            "year_9_ambiguity: Year 9 (ages 13-14) straddles REAL Bands D and E. Items tagged [D, E] "
            "with ambiguity_flag=true and teacher_review_flag=true. Teacher judgment required."
        ),
        (
            "pipeline_generated: Circle Solutions KUD and LT items were classified via the harness "
            "pipeline (LLM-based 3-run self-consistency). This v2 replaces the manually-constructed "
            "v1 (band-tagged-circle-solutions-manual.json in _manual-archive/)."
        ),
    ]

    output = {
        "source_metadata": {
            "source_name": "Circle Solutions SEL Framework (Cowie & Myers, 2016)",
            "source_type": "circle_solutions_sel",
            "source_band_labels": ["Year 2", "Year 6", "Year 9", "Year 12"],
            "target_framework": "REAL School Budapest Bands A-F",
            "skill_version": "2.0",
            "run_timestamp": datetime.now(timezone.utc).isoformat(),
            "session": "CW-2b",
            "note": "Pipeline-generated (harness v3-run self-consistency). Replaces CW-2 manual construction.",
        },
        "band_tagged_kud": band_tagged_kud,
        "band_tagged_lts": band_tagged_lts,
        "summary_counts": summary_counts,
        "skill_flags": skill_flags,
    }

    out_path = CORPUS_DIR / "band-tagged-circle-solutions-v2.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"[cw2b] Written: {out_path}", flush=True)
    print(f"[cw2b] KUD items: {len(band_tagged_kud)} (v1 had 112)", flush=True)
    print(f"[cw2b] LTs: {len(band_tagged_lts)} (v1 had 48)", flush=True)
    print(f"[cw2b] KUD by band: {dict(sorted(kud_by_band.items()))}", flush=True)
    print(f"[cw2b] LTs by band: {dict(sorted(lt_by_band.items()))}", flush=True)
    if len(halted) > 0:
        print(f"[cw2b] WARNING: {len(halted)} blocks still halted in pipeline", flush=True)


def archive_manual_v1() -> None:
    """Move manually-constructed v1 to _manual-archive/."""
    archive_dir = CORPUS_DIR / "_manual-archive"
    archive_dir.mkdir(exist_ok=True)
    v1 = CORPUS_DIR / "band-tagged-circle-solutions-v1.json"
    dest = archive_dir / "band-tagged-circle-solutions-manual.json"
    if v1.exists():
        import shutil
        shutil.move(str(v1), str(dest))
        print(f"[cw2b] Archived: {v1} → {dest}", flush=True)
    else:
        print(f"[cw2b] v1 not found at {v1}, skipping archive", flush=True)


if __name__ == "__main__":
    print("=== CW-2b: Circle Solutions full pipeline re-run ===", flush=True)
    archive_manual_v1()
    phase1_rerun_kud()
    phase2_resume_pipeline()
    phase3_stitch()
    phase4_band_translation()
    print("\n=== Circle Solutions pipeline re-run complete ===", flush=True)
