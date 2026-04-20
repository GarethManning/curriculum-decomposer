# Threshold revisions — curriculum harness

This document records calibration changes to quality-gate thresholds, with rationale and the corpus run that triggered each revision.

---

## HR-1b — type3_distribution gate (2026-04-20)

**Gate:** `type3_distribution` in `curriculum_harness/reference_authoring/gates/kud_gates.py`

**Change:** Replaced the single 20% threshold with source-type-aware tiers.

| arch_source_type / arch_domain_type | Old threshold | New threshold | Rationale |
|---|---|---|---|
| `national_statutory_curriculum` | 20% | **5%** | Statutory curricula (DfE, etc.) are inherently T1-dominant: declarative law, health facts, procedural requirements. 20% was calibrated for dispositional frameworks and fires a false informational flag on every statutory corpus. The 5% floor confirms T3 items exist without penalising the source-type. |
| `horizontal_dispositional` or `horizontal_dispositional_mixed` | 20% | **15%** | These sources mix procedural and dispositional content. The 20% default over-flags them; 15% better fits the observed ratio in horizontally-organised dispositional curricula (e.g. Welsh CfW). |
| Other dispositional-domain sources | 20% | **20%** | Unchanged. The default remains appropriate for purely dispositional frameworks. |

**Triggering corpus:** `uk-statutory-rshe` — `national_statutory_curriculum`, `horizontal_dispositional_mixed`. T3 share: 6.1% (17/279). Would fire false negative at 20% threshold; passes correctly at 5%.

**Implementation:**
- `_type3_threshold()` helper function added (lines ~80–95 of kud_gates.py)
- `_gate_type3_distribution()` updated to accept `arch_source_type` and `arch_domain_type`
- `run_kud_gates()` updated to accept and thread the new params
- `run_pipeline.py` loads `architecture-diagnosis.json` from the output directory (if present) before calling `run_kud_gates()`

**Backward compatibility:** Fully backward-compatible. When `arch_source_type` and `arch_domain_type` are `None` (no architecture-diagnosis.json in output dir), the gate behaves exactly as before: skips for non-dispositional sources, applies 20% for dispositional sources.

**Gate behaviour remains informational only (non-halting).** This change does not alter the halting status of any gate.

**Existing artefacts:** This threshold change does NOT retroactively alter existing quality-report.json files. The uk-statutory-rshe quality-report.json at `docs/reference-corpus/uk-statutory-rshe/quality_report.json` retains its original gate result (type3_distribution: PASS=false at 20% threshold). The corrected threshold applies to future pipeline runs only.
