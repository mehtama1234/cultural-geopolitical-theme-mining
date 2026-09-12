# SIPP weighted descriptive scan v2

**Run date:** 2026-09-12  
**Input:** full v2 slice from [SIPP acquisition v1](sipp-bounded-acquisition-v1.md)  
**Analysis:** [analyze_sipp_weighted_codes.py](../../../scripts/analyze_sipp_weighted_codes.py)  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`, final person weight
**Value labels:** verified against the [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

## What was measured

The scan read 379,215 selected rows. Of these, 378,291 had a positive final person weight. It computes weighted distributions of SIPP codes and missingness; it does not treat the person weight as a household weight.

| Field | Weighted share with verified code `1` | Weighted blank share | Raw nonblank codes |
|---|---:|---:|---|
| `ETENURE` (code `1` = owned/bought) | 67.23% | 0.00% | 1, 2, 3 |
| `EUTILITIES` (code `1` = yes) | 2.01% | 97.06% | 1, 2 |
| `EENERGY_ASST` (code `1` = yes) | 3.54% | 44.77% | 1, 2 |
| `EAWBMORT` (code `1` = yes) | 4.64% | 0.00% | 1, 2 |
| `EAWBGAS` (code `1` = yes) | 7.06% | 0.00% | 1, 2 |
| `EOWN_SAV` (code `1` = yes) | 52.08% | 18.26% | 1, 2 |
| `EDEBT_CC` (code `1` = yes) | 22.42% | 18.26% | 1, 2 |
| `RFOODS` (code `1` = high/marginal security) | 88.56% | 0.00% | 1, 2, 3 |
| `RFOODR` (code `1` = one affirmative response) | 5.51% | 0.00% | 0, 1, 2, 3, 4, 5, 6 |
| `EFOOD1` (code `1` = often true) | 2.98% | 0.00% | 1, 2, 3 |
| `EFOOD3` (code `1` = yes) | 6.55% | 0.00% | 1, 2 |
| `EFOOD6` (code `1` = yes) | 4.34% | 83.05% | 1, 2 |
| `EPAY` (code `1` = yes) | 2.19% | 92.73% | 1, 2 |
| `EPAYHELP` (code `1` = yes) | 0.46% | 92.73% | 1, 2 |
| `EWORKMORE` (code `1` = yes) | 0.36% | 90.70% | 1, 2 |
| `RMNUMJOBS` (code `1` = one job) | 45.06% | 16.85% | 0, 1, 2, 3, 4, 5 |

The labels are now verified. The percentages are still only distribution checks because the scan mixes fields with different universes and applies a person weight to person records, including repeated household fields.

For fields with blanks, the corresponding code-`1` share among nonblank selected records is: `EUTILITIES` 68.50%, `EENERGY_ASST` 6.40%, `EOWN_SAV` 63.72%, `EDEBT_CC` 27.43%, `EFOOD6` 25.60%, `EPAY` 30.08%, `EPAYHELP` 6.38%, `EWORKMORE` 3.88%, and `RMNUMJOBS` 54.20%. These are conditional scan diagnostics, not official universe estimates, because the extractor did not carry every status flag or construct each field's universe.

## Verified value labels and universes

- `ETENURE`: `1` owned or being bought, `2` rented, `3` occupied without rent; household field.
- `EAWBMORT` and `EAWBGAS`: `1` yes, `2` no; household questions asked of the reference person.
- `RFOODS`: `1` high or marginal food security, `2` low, `3` very low; household field for households including a person aged 15 or older.
- `RFOODR`: `0` through `6` affirmative-response count; same household universe.
- `EUTILITIES`: `1` yes, `2` no; household field within the rent-subsidy and assistance-screen universe, not all households.
- `EENERGY_ASST`: `1` yes, `2` no; household field within the program-eligibility screening universe.
- `EOWN_SAV` and `EDEBT_CC`: `1` yes, `2` no; person fields for people aged 15 or older at the December reference month.
- `EPAY`, `EPAYHELP`, and `EWORKMORE`: child-care-specific person/reference-parent universes, not all adults.
- `RMNUMJOBS`: numeric count, `0` through `17`, for respondents aged 15 or older.

The table must not be paraphrased as “the national share of households unable to pay utilities” or “the share of all parents blocked by child care.” Those claims require universe-specific estimates and, for household outcomes, an explicit household-weight method.

## What this adds

The full selected SIPP file can now support a person-level weighted descriptive layer. The scan also exposes where conditional fields are sparse: energy assistance, separate utilities, food hardship detail, child-care payment, and work-limit questions have substantial blank shares. Those blanks must remain `unknown` or outside the field universe, not be recoded as “no.”

## What it does not add

This is not a household prevalence table. Monthly household fields are repeated on person records, and the final person weight is not silently converted into a household weight. It is not a causal estimate, a full event history, or evidence that utility, food, debt, work, or care pressure occurred in the same household after one shock.

The scan also does not establish a national trend: it covers the 2024 reference year in the 2025 SIPP release. Month-to-month differences require the survey design, variable universes, appropriate weights, and variance estimation.

## Next analysis

Produce person-level weighted tables by month and selected strata, with field-specific universes, denominators, status flags, missingness, and—where needed—survey-design variance. For household-level claims, define and document a household selection or household-weight method before estimating joint outcomes. Use the results as one population layer across the broad research bridges, not as a substitute for CE, ATUS, SHED, MEPS, RECS, administrative records, or a true event panel.
