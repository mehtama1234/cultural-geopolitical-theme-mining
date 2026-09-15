# HTOPS 2025 panel linkage audit v1

**Checked:** 2026-09-14  
**Scope:** April 2025 and June 2025 HTOPS public-use files  
**Status:** linked respondent surface verified; attrition-adjusted population
estimate not claimed

## Linkage result

The April PUF contains 8,850 respondents and the June PUF contains 7,485.
`SCRAMID` is present in both public-use files and their replicate-weight files.
An inner join produces 6,564 linked respondents, equal to 74.2% of the April
file and 87.7% of the June file.

The following substantive fields are present in both files with shared coding:
`EXPNS_DIF`, `CURFOODSUF`, `HSE16`, `PRICECHNG`, `WRKLOSSRV`, `ANYWORK`,
`FEDSTAT_TRUST`, and `TRUST2_CONGRESS`. The dictionaries retain the item
universes and missing codes; the extractor excludes `-88` and `-99` per item.

## Weight boundary

Both releases provide person weights and 80 replicate weights. The linked
transition extractor uses April `PWEIGHT` and April replicate weights for the
retained linked sample. This supplies a reproducible conditional precision
screen, but it is not a longitudinal attrition-adjusted weight. No national
transition estimate is promoted until a documented panel weight or appropriate
nonresponse adjustment is available.

The [machine-readable attrition audit](data/htops-2025-panel-attrition-audit.json)
shows nonuniform retention diagnostics: unweighted retention is 69.5% for
under-$50,000 households, 76.7% for $100,000-plus households, 70.8% for the
baseline expense-difficulty group, and 63.0% for the small food-insufficient
cell. These strengthen the selection warning but do not provide an attrition
correction.

## Retrieval hashes

| Artifact | SHA-256 |
|---|---|
| April 2025 PUF ZIP | `c6976130ec387f0555200fa1197bd4875966b8b8a4ad847ba3220749a939673e` |
| June 2025 PUF ZIP | `8d14cf52f5c3bc4fab5e74e3136cb753ab1195a06314725f00761035158172d4` |

## Interpretation boundary

This audit proves a reproducible same-ID linkage and shared field surface. It
does not prove that linked respondents are representative, that a transition is
caused by a measured event, or that the public files contain follow-up remedy,
care-time, trust-attribution, civic-action, or recovery fields.

## Sources

- [Census 2025 HTOPS/HPS public-use page](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.2025.html)
- [Linked-panel record](../../records/us-census-htops-material-trust-panel-april-june-2025.json)
- [Linked-panel builder](../../../scripts/build_htops_2025_panel_2504_2506_record.py)
- [Attrition audit data](data/htops-2025-panel-attrition-audit.json)
- [Attrition audit builder](../../../scripts/audit_htops_2025_panel_attrition.py)
- [Cross-lagged material-to-outcome audit](data/htops-2025-cross-lagged-panel-audit.json)
- [Cross-lagged audit builder](../../../scripts/build_htops_2025_cross_lagged_panel_audit.py)
