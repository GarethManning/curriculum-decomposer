# Dispositional source pre-flight verification

**Date:** 2026-04-19
**Session:** 4a-5 Step 1
**Primary candidate:** Welsh Curriculum for Wales — Health and Well-being, "Statements of what matters"
**Verified URL:** `https://hwb.gov.wales/curriculum-for-wales/health-and-well-being/statements-of-what-matters/`

## Verification outcome: PRIMARY CANDIDATE PASSES

All four pre-flight checks pass for the Welsh CfW Health and Well-being
"Statements of what matters" page. No fallback needed.

## 1. URL discovery

The prompt names `https://hwb.gov.wales/curriculum-for-wales/health-and-well-being/`
as the primary candidate. That URL is the Area of Learning and Experience
**index** page; the sub-pages follow the same pattern as the Welsh
Mathematics AoLE extracted in Session 4a-4 Step 9:

- `/health-and-well-being/statements-of-what-matters/` — SoW sub-page (this run).
- `/health-and-well-being/principles-of-progression/` — separate URL.
- `/health-and-well-being/descriptions-of-learning/` — separate URL (JS-rendered
  accordion, out of scope).

The SoW sub-page is the correct target: it carries the mandatory
Statements of what matters (the dispositional load-bearing content) with
their explanatory paragraphs. The root `/health-and-well-being/` index
page carries only navigation to the three sub-pages.

## 2. Basic accessibility

Plain `curl` with no headers: **HTTP 403** from CloudFront (`Request blocked`).
`curl` with Chrome-like User-Agent + standard Accept headers:
**HTTP 200**, `text/html; charset=utf-8`, body 122,003 bytes.

Phase 0's `fetch_requests` primitive sends a browser-like UA by default, so
this is expected to fetch cleanly through the existing primitive. Confirmed
in Session 4a-4 Step 9's successful Welsh Maths SoW extraction on the same
CDN.

## 3. Content sanity

Key-phrase counts on the fetched HTML:

| Phrase                           | Count |
| -------------------------------- | ----- |
| `Statements of what matters`     | 7     |
| `well-being`                     | 31    |
| `mental health`                  | 6     |
| `physical health`                | 3     |
| `emotional`                      | 9     |
| `values`                         | 12    |
| `relationships`                  | 25    |
| `Mandatory`                      | 1     |

All five mandatory statements are present as `<h3>` siblings inside
`article#aole-v2`:

1. Developing physical health and well-being has lifelong benefits.
2. How we process and respond to our experiences affects our mental
   health and emotional well-being.
3. Our decision-making impacts on the quality of our lives and the lives
   of others.
4. How we engage with social influences shapes who we are and affects
   our health and well-being.
5. Healthy relationships are fundamental to our well-being.

Article-scoped, chrome-stripped body text: **4,644 chars** across the
five statements + their explanatory paragraphs. Comparable volume to
Welsh Maths SoW (3,792 chars / 4 statements) from Session 4a-4 Step 9 —
one more mandatory statement, similarly compact per-statement
exposition.

## 4. Initial category-presence scan

Sampled the extracted body text for visible Category 1 / 2 / 3 framing
(per the session's three-category taxonomy, with the prompt-dependence
diagnostic for Category 2 vs Category 3). Non-binding — this is a
presence check, not the Step 4 classification.

- **Category 1 (propositional about dispositions) — present.**
  "This Area can help learners to understand the factors that affect
  physical health and well-being… including health-promoting behaviours
  such as physical activity… balanced diet… sleep."
- **Category 2 (occasion-prompted / enabling skills) — present.**
  "Supporting learners to develop strategies which help them to regulate
  their emotions" (triggered by emotion arising).
  "Learners need to recognise when relationships are unhealthy and need
  to be aware of how to keep safe, and seek support" (triggered by
  recognising condition).
- **Category 3 (sustained operating states) — present.**
  "Having an awareness of our own feelings and emotions is the
  foundation upon which empathy can be developed" (ongoing orientation,
  not situational trigger).
  "Learners will be encouraged to develop their abilities to form,
  nurture and maintain relationships" (sustained capability, not
  occasion-prompted).

All three categories are visibly present in the page body. The source is
not Category-1-only; it is a plausible candidate for a
`rich_dispositional` archetype classification under Step 4 Check B, but
that is Step 4's call, not this pre-flight's.

## 5. Pre-flight verdict

**PASS** on all four checks. Proceed to Step 2 (investigation) on the
primary candidate. No fallback to Scottish CfE required.

Notes for Step 2:

- The SoW page structure should mirror Welsh Maths SoW (Session 4a-4
  Step 9): `article#aole-v2` as the content root; in-container chrome
  (`nav`, `.tab-next-prev`, `.explore-links`, `.contents`) stripped via
  `exclude_selectors`; no section scoping needed (one URL = one section).
- Volume ~4.6 KB vs Welsh Maths SoW's ~3.8 KB — Check C threshold should
  be tuned to this range.
- No `<details>` elements expected on the SoW page (accordion content
  lives on the Descriptions of learning page, which is JS-rendered and
  out of scope here).
