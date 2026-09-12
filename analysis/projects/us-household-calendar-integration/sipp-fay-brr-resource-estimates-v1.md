# SIPP Fay-BRR resource estimates v1

**Run date:** 2026-09-12  
**Primary input:** 35-field full v4 extraction from [SIPP acquisition v1](sipp-bounded-acquisition-v1.md)  
**Replicate input:** [2025 SIPP replicate-weight CSV archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)  
**Method:** [analyze_sipp_fay_brr.py](../../../scripts/analyze_sipp_fay_brr.py), grouped by monthly `THINCPOV`, 240-replicate Fay BRR, perturbation factor 0.5  
**Unit:** person record by reference month; code `1` share among nonblank selected records

## Verification

The run read 379,215 primary rows, read 379,215 replicate rows, and matched all 378,291 positive-primary-weight rows by `SSUID + PNUM + SPANEL + SWAVE + MONTHCODE`.

## Estimates by monthly income-to-poverty ratio

| Monthly ratio band | Measure | Estimate | Fay-BRR SE (percentage points) | Approx. 95% interval |
|---|---|---:|---:|---:|
| Below 1.00x | Unable to pay rent/mortgage | 11.893% | 1.080 | 9.776–14.010% |
| Below 1.00x | Unable to pay utility bills | 15.993% | 1.192 | 13.656–18.330% |
| Below 1.00x | Hungry but did not eat because of money | 33.248% | 2.526 | 28.297–38.199% |
| 1.00–1.99x | Unable to pay rent/mortgage | 8.529% | 0.751 | 7.056–10.001% |
| 1.00–1.99x | Unable to pay utility bills | 14.551% | 1.139 | 12.318–16.784% |
| 1.00–1.99x | Hungry but did not eat because of money | 26.989% | 2.288 | 22.506–31.473% |
| 2.00–3.99x | Unable to pay rent/mortgage | 4.827% | 0.450 | 3.944–5.710% |
| 2.00–3.99x | Unable to pay utility bills | 7.398% | 0.549 | 6.322–8.475% |
| 2.00–3.99x | Hungry but did not eat because of money | 22.881% | 1.909 | 19.139–26.622% |
| 4.00x or more | Unable to pay rent/mortgage | 1.835% | 0.217 | 1.410–2.261% |
| 4.00x or more | Unable to pay utility bills | 2.707% | 0.257 | 2.204–3.210% |
| 4.00x or more | Hungry but did not eat because of money | 19.734% | 2.277 | 15.272–24.196% |

The intervals are normal approximations from the Census Fay-BRR variance formula and are bounded to 0–100. They are a first uncertainty check, not a final publication table with every field universe, status flag, imputation review, or multiple-comparison decision.

## What this changes

The resource gradient in the earlier point comparison survives the replicate-weight check: lower monthly income-to-poverty bands have higher estimates for payment difficulty, utility difficulty, and severe food hardship. The gradient is a population distribution, not a complete explanation of why the conditions differ.

The ratio is measured for a month and is not the same as liquid cash at the exact moment of a bill. It does not capture wealth, timing, local prices, debt terms, family help, health, or institutional access. The table therefore supports an inequality axis for the price/payment → household-room bridge, while leaving the mechanism and later cultural or political meaning open.

## Limits

- Person weights and person replicate weights were used; no household weight was constructed.
- Rates use nonblank selected records, not a full field-specific universe implementation.
- The result covers the 2024 reference year in the 2025 SIPP release.
- The table does not connect income, a specific bill, a choice, an institutional response, trust, political action, firm behavior, or geopolitical consequence for the same person.

## Next test

Run a small tenure × resource Fay-BRR table with adequate cell support, then apply official universes and status flags. Preserve the two-way point comparison as exploratory until that uncertainty check is complete.
