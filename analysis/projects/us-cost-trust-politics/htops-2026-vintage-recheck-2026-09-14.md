# HTOPS/HPS 2026 vintage recheck — 2026-09-14

**Status:** official release-state and correction check  
**Scope:** March, May, and July 2026 HTOPS/HPS public-use files

## Result

The Census Bureau's current public-use-file page lists July 2026 as the latest
2026 HTOPS Household Pulse release. It also states that the March and May 2026
PUFs were updated on September 10, 2026 to correct the weights. No August 2026
PUF is listed on the current 2026 release page.

This confirms that the atlas's cross-wave comparison must continue to label May
as **corrected** and must retain the July file as the latest available snapshot.
The check does not create a new observation or justify recalculating March/May
values without the corrected package artifacts.

## Evidence and implications

| Check | Current official state | Atlas action |
|---|---|---|
| March 2026 PUF | Listed; corrected weights noted | Keep corrected March package/hash and replicate-weight estimates |
| May 2026 PUF | Listed; updated September 10, 2026 to correct weights | Keep “May 2026 corrected” label and corrected package/hash |
| July 2026 PUF | Listed; collection July 15–August 3, 2026 | Treat as latest snapshot; preserve cross-sectional denominator |
| August 2026 PUF | Not listed on current 2026 page | Do not infer a missing release or interpolate a trend |
| Design | HTOPS shifted from longitudinal 2025 to cross-sectional HPS-focused releases beginning March 2026 | Keep March/May/July comparisons independent snapshots, not recontact change |

The [cross-wave machine record](../../records/us-census-htops-hps-material-trust-crosswave-2026.json)
already uses the corrected March and May values and preserves the July
comparison. The [question-harmonization audit](htops-2026-question-harmonization-audit-v1.md)
retains field, missingness, and replicate-weight controls.

## Boundary

The release page establishes file availability and correction status. It does
not establish that the corrected weights remove nonresponse, composition,
seasonality, or design-break concerns. The three snapshots remain separate
weighted population estimates; they do not identify the same households or
causal movement in expense difficulty, food sufficiency, energy trade-offs,
trust, or confidence in Congress.

## Official recheck sources

- [Census HTOPS/HPS public-use files](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html)
- [Census HTOPS/HPS data overview](https://www.census.gov/programs-surveys/household-pulse-survey/data.html)
- [Census experimental-product description](https://www.census.gov/data/experimental-data-products/household-pulse-survey.html)
- [Cross-wave finding](findings/us-cost-trust-politics-017.md)
