# SIPP Fay-BRR tenure estimates v1

**Run date:** 2026-09-12  
**Primary input:** 35-field full v4 extraction from [SIPP acquisition v1](sipp-bounded-acquisition-v1.md)  
**Replicate input:** [2025 SIPP replicate-weight CSV archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)  
**Method:** [analyze_sipp_fay_brr.py](../../../scripts/analyze_sipp_fay_brr.py), grouped by `ETENURE`, 240-replicate Fay BRR, perturbation factor 0.5  
**Unit:** person record by reference month; code `1` share among nonblank selected records

## Verification

The run read 379,215 primary rows, read 379,215 replicate rows, and matched all 378,291 positive-primary-weight rows by `SSUID + PNUM + SPANEL + SWAVE + MONTHCODE`.

## Estimates by tenure

| Tenure | Measure | Estimate | Fay-BRR SE (percentage points) | Approx. 95% interval |
|---|---|---:|---:|---:|
| Owned or being bought | Unable to pay rent/mortgage | 2.432% | 0.203 | 2.034–2.830% |
| Owned or being bought | Unable to pay utility bills | 4.671% | 0.321 | 4.042–5.301% |
| Owned or being bought | Hungry but did not eat because of money | 19.922% | 1.639 | 16.710–23.135% |
| Rented | Unable to pay rent/mortgage | 9.614% | 0.645 | 8.350–10.878% |
| Rented | Unable to pay utility bills | 12.103% | 0.737 | 10.658–13.548% |
| Rented | Hungry but did not eat because of money | 30.426% | 1.698 | 27.098–33.754% |
| Occupied without payment of rent | Unable to pay rent/mortgage | 2.699% | 0.916 | 0.905–4.494% |
| Occupied without payment of rent | Unable to pay utility bills | 10.076% | 2.377 | 5.417–14.736% |
| Occupied without payment of rent | Hungry but did not eat because of money | 21.979% | 6.191 | 9.844–34.114% |

The intervals are normal approximations from the Census Fay-BRR variance formula and are bounded to 0–100. They are presented for a first quality check, not as a substitute for a final publication table with every field universe, status flag, imputation review, and multiple-comparison decision.

## What this changes

The renter differences in the earlier tenure comparison are not merely point estimates. In this person-weighted diagnostic, the renter estimate is above the owner estimate for all three measures, with substantially wider uncertainty for the rent-free group. This sharpens the distributional question for the housing/energy → household-room bridge.

It still does not show that tenure caused the difference. Tenure is associated with income, age, household composition, location, housing quality, insurance, energy systems, health, and access to family or public help. The table also does not show the same person’s bill, choice, repair, move, trust judgment, or political action.

## Limits

- Person weights and person replicate weights were used; no household weight was constructed.
- Rates use nonblank selected records, not a full field-specific universe implementation.
- No tenure × resource replicate table has yet been calculated.
- The result covers the 2024 reference year and does not establish a trend or causal effect.

## Next test

Run the Fay-BRR calculation for a small pre-registered tenure × income-to-poverty set, beginning with rent/mortgage difficulty, utility-payment difficulty, and food hardship. Apply official universes and status flags before interpreting intersections.
