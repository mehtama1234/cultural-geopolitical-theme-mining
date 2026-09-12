# SIPP resource-stratified population layer v1

**Run date:** 2026-09-12  
**Source:** 2025 SIPP public-use pipe file, 2024 reference year  
**Method:** [analyze_sipp_population_layer.py](../../../scripts/analyze_sipp_population_layer.py) on the full v4 extraction, grouped into monthly `THINCPOV` income-to-poverty-ratio bands, using `WPFINWGT`
**Unit:** person record by reference month; rates below are verified code `1` among nonblank selected records  
**Labels and definitions:** [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

## The comparison

`THINCPOV` is the household income-to-poverty ratio for the month, excluding Type 2 individuals. The table uses four descriptive bands. The rates are not household prevalence estimates; household fields are repeated on person records and weighted with the final person weight.

| Monthly household income-to-poverty ratio | Unable to pay rent/mortgage | Unable to pay utility bills | High/marginal food security | Hungry but did not eat because of money | Carried credit/store-card balance | One job |
|---|---:|---:|---:|---:|---:|---:|
| Below 1.00x | 11.89% | 15.99% | 70.86% | 33.25% | 20.27% | 24.05% |
| 1.00–1.99x | 8.53% | 14.55% | 76.43% | 26.99% | 25.47% | 37.07% |
| 2.00–3.99x | 4.83% | 7.40% | 88.58% | 22.88% | 28.61% | 52.96% |
| 4.00x or more | 1.84% | 2.71% | 95.93% | 19.73% | 28.61% | 65.26% |

## What this adds to the broader map

The material pressures are not distributed evenly by measured resources. In this layer, the below-poverty band has the highest observed nonblank shares for rent/mortgage difficulty, utility-payment difficulty, and severe food hardship, while the highest-resource band has the highest share reporting high or marginal food security. The job-count pattern also differs substantially across bands.

The credit-balance measure does not move in the same simple direction: its observed share is lower below poverty than in the middle and higher-resource bands. That is a useful warning against treating debt as a direct scale of hardship. Access to credit, age, employment, card ownership, borrowing needs, and reporting universe may all differ.

These comparisons support a population-level inequality question for the price/payment → household-room bridge. They do not establish that income ratio caused any outcome, that the same person experienced all outcomes, or that the pattern explains trust, culture, voting, firm behavior, or public policy response.

## Limits

- `THINCPOV` is a monthly household ratio, but this analysis uses person records and `WPFINWGT`.
- The nonblank denominator is an extraction diagnostic. The official universe and status flags must be applied in a production estimate.
- Income-to-poverty ratio is not liquid cash at the moment of a bill; it does not capture wealth, timing, debt terms, local prices, or family help.
- No replicate-weight variance or confidence intervals were computed.
- The table does not link income, a specific bill, a choice, an institutional response, interpretation, or political action for the same person over time.

## Next test

Cross-tab the resource bands with tenure and region, then add a separately measured spending, energy, care, or transport outcome. The goal is to distinguish low annual resources from timing, place, coverage, and institutional rules as different routes into lost household room.
