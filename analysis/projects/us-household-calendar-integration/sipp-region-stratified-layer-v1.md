# SIPP region-stratified population layer v1

**Run date:** 2026-09-12  
**Source:** 2025 SIPP public-use pipe file, 2024 reference year  
**Method:** [analyze_sipp_population_layer.py](../../../scripts/analyze_sipp_population_layer.py), grouped by `TEHC_REGION`, using `WPFINWGT`  
**Unit:** person record by reference month; rates are verified code `1` among nonblank selected records  
**Region labels:** official SIPP Data Dictionary values: Northeast, Midwest, South, West

## The place comparison

| Monthly region | Unable to pay rent/mortgage | Unable to pay utility bills | High/marginal food security | Hungry but did not eat because of money | One job |
|---|---:|---:|---:|---:|---:|
| Northeast | 4.71% | 7.36% | 88.19% | 19.72% | 53.87% |
| Midwest | 3.83% | 7.59% | 90.15% | 24.05% | 55.42% |
| South | 5.19% | 7.07% | 87.60% | 27.74% | 53.60% |
| West | 4.38% | 6.38% | 89.05% | 27.95% | 54.37% |

## What this adds

In this selected person-weighted layer, reported food hardship differs more across regions than rent/mortgage payment difficulty. The South and West have the highest observed shares for the severe food-hardship diagnostic, while the Midwest has the highest one-job share. The payment-difficulty differences are present but smaller than the tenure and income-resource differences already recorded.

This is a place-distribution result, not evidence that region itself caused the outcome. Region bundles local prices, housing markets, climate, wages, industry, public programs, transport, family structure, and many other conditions. It does not identify the specific infrastructure, policy, or market mechanism.

## Limits

- `TEHC_REGION` is a four-region classification, not a state, county, ZIP, or neighborhood measure.
- Results are person-weighted diagnostics, not household counts.
- Household fields are repeated on person records, and the nonblank denominator is not a replacement for each official field universe.
- No survey-design variance or confidence intervals were computed.
- The table does not connect region to a specific bill, service failure, repair, health outcome, move, political interpretation, firm response, or geopolitical exposure.

## Next test

Cross region with tenure and income-to-poverty ratio, then bring in state/local price, energy, transport, insurance, health, and political measures as separate place layers. The objective is to identify which local mechanism survives resource and household-composition comparisons.
