# SIPP housing-transition timing report v1

**Checked:** 2026-09-25  
**Status:** real public-file audit complete; no promoted estimate  
**Source:** 2025 SIPP public-use CSV, January–December 2024 reference period

## What was actually run

The additive `housing-transition` profile streamed the official Census public-use
archive without placing the 2.96 GB uncompressed respondent file in the
repository. It retained the existing person-month key (`SSUID` + `SHHADID` +
`PNUM` + `MONTHCODE`) and added housing-assistance, residence-spell,
housing-cost, and corresponding status fields.

The resulting slice contains 379,215 rows, 32,052 distinct people, 13,910
households, and all 12 months. Household fields are repeated on person rows;
these counts are descriptive record counts, not population estimates.

The compact machine-readable summary is
[sipp-housing-transition-timing-audit-2025.json](data/sipp-housing-transition-timing-audit-2025.json).

## What the fields show

| Field | Timing class | Nonblank rows | Blank rows | Safe reading |
|---|---:|---:|---:|---|
| `EHOUSE_ANY` | reference period | 324,671 | 54,544 | housing-assistance context, not monthly receipt |
| `EEHC_RENTSUB` | residence spell | 109,692 | 269,523 | rent-subsidy context for the residence |
| `EEHC_VOUCHER` | residence spell | 13,918 | 365,297 | voucher context for the residence |
| `TRENTMORT` | December reference period | 261,780 | 117,435 | December rent/mortgage amount, not a monthly bill series |
| `EAWBMORT` | reference period | 379,215 | 0 | reported inability-to-pay context |
| `EAWBGAS` | reference period | 379,215 | 0 | reported gas-payment context |
| `RMNUMJOBS` | monthly | 326,099 | 53,116 | monthly job-count context, subject to its universe |
| `THINCPOV` | monthly | 379,052 | 163 | monthly continuous poverty-ratio context |

## Timing result

The adjacent-month diagnostic confirms the central boundary. `EHOUSE_ANY`,
`EAWBMORT`, and `EAWBGAS` had zero raw-code changes across 297,325, 347,163,
and 347,163 complete adjacent pairs respectively. That is consistent with
reference-period values being copied across months; it is not evidence that
households experienced no change.

The residence-spell fields also should not be treated as monthly transitions:
`EEHC_RENTSUB` changed in 66 of 99,943 complete raw pairs and
`EEHC_VOUCHER` in 14 of 12,691. The small change counts reflect the field
timing and coding structure, not a causal persistence estimate.

`RMNUMJOBS` is genuinely monthly in the source and changed in 4,344 of 298,603
complete raw pairs. This is only a raw diagnostic until the field universe,
person/household weights, replicate weights, and transition definition are
implemented. The apparent 90.9% raw-code change rate for `THINCPOV` is not
substantively interpretable because exact string equality is inappropriate for
a continuous monthly ratio; no finding is promoted from it.

## Decision for the broader project

This pass establishes a useful same-person public-data backbone and narrows the
next methodological task. It does **not** close the end-to-end housing route.
SIPP still does not provide, in this extraction, HUD administrative program
identity, benefit amount or adequacy, landlord response, housing quality,
verified recovery, trust, or political action. It also cannot be joined to the
HUD–LEHD or HEARS studies merely because the concepts are similar.

The appropriate status is therefore a verified acquisition and timing boundary:
use SIPP for a carefully weighted descriptive bridge only after defining valid
universes, status/missingness treatment, and a non-arbitrary episode window;
retain the HUD–LEHD and HEARS findings as separate linked evidence; and do not
promote this audit into a claim that assistance caused housing security or
recovery.

## Sources

- [Census 2025 SIPP data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [Census 2025 SIPP public-use archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/pu2025_csv.zip)
- [Census 2025 SIPP API variable catalog](https://api.census.gov/data/2025/sipp/variables.html)
- [Housing-transition field audit](sipp-housing-transition-field-audit-v1.md)
- [Housing-transition next-test protocol](housing-transition-next-test-v1.md)
