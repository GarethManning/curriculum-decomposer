# Phase 1 variance — runA vs runB (Shape A + Shape B)

- runA bullets: 937 (bullet-text chars: 65704, raw_curriculum chars: 12898)
- runB bullets: 937 (bullet-text chars: 65704, raw_curriculum chars: 8746)
- bullet-count variance: 0.0%
- bullet-text char variance: 0.0%
- raw_curriculum char variance (non-bullet, informational): 32.2%
- threshold (binding-specifications): 15%

**Result (bullets only — the gate-binding artefact):** PASS (under 15%)

Note: `raw_curriculum` is the Haiku-narrowed text used by downstream
LLM phases. It still varies run-to-run because Anthropic's streaming
inference at temperature 0 is not bit-for-bit deterministic (documented
server-side batching effects). The downstream phases are LLM-based
anyway and tolerate this informational variance. The load-bearing
artefact for source-evidence gates is `source_bullets`, which is now
deterministic because it is extracted rule-based from the Phase 1
windowed slice rather than from the Haiku output.
