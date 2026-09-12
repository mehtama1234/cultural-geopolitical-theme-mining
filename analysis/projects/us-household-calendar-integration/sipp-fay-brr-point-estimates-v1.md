# SIPP Fay-BRR point estimates v1

**Run date:** 2026-09-12  
**Primary input:** 35-field full v4 extraction from [SIPP acquisition v1](sipp-bounded-acquisition-v1.md)  
**Replicate input:** [2025 SIPP replicate-weight CSV archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)  
**Method:** [analyze_sipp_fay_brr.py](../../../scripts/analyze_sipp_fay_brr.py), 240-replicate Fay BRR with perturbation factor 0.5  
**Join key:** `SSUID` + `PNUM` + `SPANEL` + `SWAVE` + `MONTHCODE`  
**Unit:** person record by reference month; code `1` share among nonblank selected records

## Verification

The run read 379,215 primary rows, read 379,215 replicate rows, and matched all 378,291 positive-primary-weight rows. The primary and replicate files were not assumed to have the same row order; every match used the documented key.

## Estimates

| Measure | Verified code `1` meaning | Estimate | Fay-BRR SE (percentage points) | Approx. 95% interval |
|---|---|---:|---:|---:|
| `EAWBMORT` | unable to pay rent or mortgage | 4.637% | 0.250 | 4.147–5.128% |
| `EAWBGAS` | unable to pay utility bills | 7.063% | 0.322 | 6.432–7.695% |
| `RFOODS` | high or marginal food security | 88.563% | 0.383 | 87.813–89.313% |
| `EFOOD6` | hungry but did not eat because of money | 25.597% | 1.177 | 23.291–27.903% |
| `RMNUMJOBS` | one job | 54.200% | 0.308 | 53.595–54.804% |

The interval is a normal-approximation presentation of the Fay-BRR standard error, bounded to 0–100. It is included for orientation and is not a substitute for a full publication review of small-cell, imputation, or multiple-comparison issues.

## What this changes

The broad program now has a design-based uncertainty check for a small full-sample set rather than only point diagnostics. The estimates are still not household counts, and the conditional nonblank denominator remains visible. `EFOOD6`, for example, is asked within a food-hardship universe; its 25.597% is not the share of all people or households in the country.

This run does not provide uncertainty for the tenure, income, region, or tenure × resource tables. Those subgroup estimates remain descriptive point diagnostics until their exact universes and replicate-weight calculations are run.

## Limits

- The primary slice uses person weights; no household weight was constructed.
- The analyzer did not yet apply every official status flag and field universe.
- The result covers the 2024 reference year in the 2025 SIPP release and does not establish a time trend.
- Fay-BRR uncertainty does not create evidence for causality or connect a material condition to a bill, choice, institutional response, culture, trust, politics, company behavior, or geopolitical consequence.

## Next test

Run the same Fay-BRR calculation for a pre-registered small set of tenure, income-to-poverty, region, and tenure × resource cells, applying each field's universe and status flag. Publish standard errors only for cells with adequate support, and retain a comparison with the full-sample estimate.
