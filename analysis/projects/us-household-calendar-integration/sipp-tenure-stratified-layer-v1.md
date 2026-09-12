# SIPP tenure-stratified population layer v1

**Run date:** 2026-09-12  
**Source:** 2025 SIPP public-use pipe file, 2024 reference year  
**Method:** [analyze_sipp_population_layer.py](../../../scripts/analyze_sipp_population_layer.py), grouped by `ETENURE`, using `WPFINWGT`  
**Unit:** person record by reference month; rates below are code `1` among nonblank selected records  
**Labels and universes:** [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

## The comparison

| Tenure group | Unable to pay rent/mortgage | Unable to pay utility bills | High/marginal food security | Hungry but did not eat because of money | Carried credit/store-card balance | One job |
|---|---:|---:|---:|---:|---:|---:|
| Owned or being bought | 2.43% | 4.67% | 93.18% | 19.92% | 26.60% | 53.54% |
| Rented | 9.61% | 12.10% | 79.00% | 30.43% | 29.25% | 56.30% |
| Occupied without payment of rent | 2.70% | 10.08% | 80.57% | 21.98% | 27.79% | 44.95% |

## What this suggests, and what it does not

In this selected person-weighted layer, renters show higher observed nonblank shares for rent/mortgage payment difficulty, utility-payment difficulty, and the two food-hardship diagnostics than owners. The gap is a useful comparison for the broad housing/energy/household-room bridge. It is not evidence that renting caused the hardship, that the same people experienced every condition, or that tenure explains the difference after income, age, family structure, place, health, and other factors are considered.

The credit-balance and one-job differences are smaller and do not carry the same meaning as the housing and food measures. A job count does not show hours, pay, schedule control, benefits, commute, or whether multiple jobs were available or necessary. A carried balance does not show the purchase, interest, delinquency, or later recovery.

## Measurement limits

- These are person-weighted diagnostics. Household fields are repeated across household members, so the results describe represented people living in the tenure group, not households counted once.
- Each field has its own official universe. The nonblank denominator here is an extraction diagnostic, not a replacement for applying every universe and status flag.
- The comparison covers the 2024 reference year in the 2025 SIPP release and has no design-based variance estimate.
- It does not connect a housing condition to a specific price, bill, repair, insurance decision, move, health outcome, firm response, trust judgment, or vote.
- The three tenure categories should not be collapsed into a simple secure/insecure split; ownership can carry mortgage, repair, insurance, and energy exposure that this table does not measure.

## Next comparison

Repeat the table with income or poverty group and region, then add housing payment amount, utility amount, insurance, repair, health, and mobility measures from the appropriate source families. The important test is whether the tenure pattern remains after resources and place are held comparable, and which missing step connects material pressure to staying, moving, or political interpretation.
