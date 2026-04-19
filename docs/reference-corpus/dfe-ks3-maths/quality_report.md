# KUD quality report — 5-dfe-ks3-maths-pdf

**Overall:** HALTED
**Halted by gate:** `artefact_count_ratio`

## Summary

- **source_domain:** hierarchical
- **inventory_blocks_total:** 46
- **inventory_non_heading_blocks:** 46
- **kud_items_total:** 71
- **halted_blocks_total:** 34
- **halted_severe:** 29
- **halted_unreliable:** 5
- **knowledge_type_distribution:** Type 1=54, Type 2=16, Type 3=1
- **kud_column_distribution:** do_disposition=1, do_skill=44, know=13, understand=13
- **stability_distribution:** classification_unstable=64, stable=7
- **underspecification_distribution:** mild=14, null=57

## Gate results

### `source_coverage` — PASS

all non-severe, non-unreliable inventory blocks produced ≥1 KUD item

### `traceability` — PASS

every KUD item has a valid source_block_id

### `artefact_count_ratio` — FAIL (halts)

KUD items / expected-yield blocks = 71/17 = 4.176 (denominator excludes 29 severely-underspecified blocks) outside hierarchical-domain target band [0.8, 2.5]

### `type3_distribution` — PASS

type3_distribution gate skipped — source is not marked as dispositional-domain

### `no_compound_unsplit` — PASS

every KUD item carries a single knowledge type with consistent column and route

