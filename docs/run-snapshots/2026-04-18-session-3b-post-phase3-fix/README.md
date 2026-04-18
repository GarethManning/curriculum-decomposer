# Session 3b end-to-end re-runs — post Phase 3 fix (2026-04-18)

Two full-pipeline runs with Phase 1 stabilisation (Shape A+B) and the
Phase 3 profile-conditional branch both active. No Phase 4 regeneration
loop (Session 3c work), no exam-spec output-shape changes (also 3c).

- Ontario (`ontario/`): `configs/ontario_session3b_e2e.json`.
- Felveteli (`felveteli/`): `configs/felveteli_session3b_e2e.json`.

Phase 3 MCP returned `Connection error` on both runs, so the Sonnet-
direct fallback ran — in the Ontario run that's `_direct_sonnet_kud`
(strand_aggregated), in the felveteli run that's
`_direct_sonnet_kud_per_bullet`. Fallback wiring for the new branch
works.

## Measurements

### Ontario — strand_aggregated branch (as expected for `national_framework`)

| Measure | Session 3a run | Session 3b run |
|---|---:|---:|
| Source bullets | 5 | **937** |
| Phase 3 branch | strand_aggregated (implicit) | **strand_aggregated (logged)** |
| KUD items | 14 | 17 |
| LTs | 14 | 17 |
| Phase 3 KUD flagged (faithfulness) | 14 / 14 (100 %) | 13 / 17 (76.5 %) |
| Phase 4 LTs flagged (faithfulness) | 14 / 14 (100 %) | 15 / 17 (88.2 %) |
| Phase 3 merge events | n/a | 0 |

Ontario was expected to remain in strand_aggregated mode; it did. The
stabilised 937-bullet corpus gives faithfulness a real signal — 4 of 17
KUD items now find ≥0.35 matches against the source, and 2 of 17 LTs
do. Session 3a's 0-of-14 signal was corpus-limited (5 bullets); the
stable corpus lifts the floor.

### Felveteli — per_bullet branch (Shape C fix)

| Measure | Session 2 run (pre-fix) | Session 3b run (post-fix) |
|---|---:|---:|
| Source bullets | 32 | **32** |
| Phase 3 branch | strand_aggregated (implicit) | **per_bullet (logged)** |
| KUD items | 14 (3 + 7 + 3 + 1, if recall included) | **32** (18 + 4 + 10 + 0) |
| Bullet → KUD consolidation ratio | **~2.3 : 1** | **1 : 1** |
| LTs | 31 | **32** |
| Phase 3 merge events | n/a | **0** |
| Phase 4 LTs flagged (faithfulness) | ~100 % (language boundary) | 32 / 32 (100 %) |

The Shape C fix achieves the consolidation-ratio target Session 1
diagnosed: Phase 3 now emits exactly one KUD item per source bullet
with zero merges. Source-bullet-to-KUD is 1:1 as specified. LT count
tracks KUD count within ±1 (32 vs 32, one T2 absorbed into T1 phrasing
in Phase 4).

Exam-spec mode output discipline is NOT applied in this session — per
the brief, Understands and Dispositions are still produced at current
behaviour (4 Understands, 0 Dispositions; note the 0 Dispositions is
Sonnet's judgement on this source, not a v4.1 refusal). That shape
change is Session 3c.

Faithfulness flagging remains 100 % for Phase 4 LTs. Mechanism
unchanged since Session 2: matcher is English-only, bullets are
Hungarian, so English LTs score ~0 against Hungarian bullets.
Interestingly Phase 3 KUD items scored 0 / 32 flagged — because the
per_bullet fallback (Sonnet-direct) quoted the Hungarian bullet text
into the KUD `content` field, so the Hungarian-to-Hungarian match
clears 0.35. The Phase 4 LT generation then paraphrases into English
and the language boundary bites. This is a real signal but the
underlying blocker (multilingual matcher) is unchanged; the gate
measurements will only move once the matcher is upgraded.

## Factorial LT guarantee — still holds

The factorial LT at felvételi LT index 0 is flagged
`SOURCE_FAITHFULNESS_FAIL`. All 32 felvételi LTs are flagged, so the
factorial LT is among them by construction. Hard requirement holds.

## Phase errors

Both runs: `phase3: MCP/tools failed: Connection error.` — the MCP
endpoint at `mcp-server-sigma-sooty.vercel.app` was intermittently
unreachable during the run. Sonnet-direct fallback activated and the
correct per_bullet vs strand_aggregated fallback path ran for each
config.

Ontario also carried: `phase1: scoped extraction returned empty or
unfound — using profile-aware fallback slice` (felvételi). This is the
pre-existing `_scoped_content_ok` cue-word miss on Hungarian text; it
falls back to the deterministic profile-aware slice, which is exactly
what Shape B now feeds to `extract_source_bullets` anyway.
