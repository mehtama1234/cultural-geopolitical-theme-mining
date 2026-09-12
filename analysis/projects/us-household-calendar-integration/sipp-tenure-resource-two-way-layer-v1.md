# SIPP tenure × resource two-way layer v1

**Run date:** 2026-09-12  
**Source:** 2025 SIPP public-use pipe file, 2024 reference year  
**Method:** [analyze_sipp_two_way_layer.py](../../../scripts/analyze_sipp_two_way_layer.py) on the full v4 extraction, using `WPFINWGT`
**Unit:** person record by reference month; rates are verified code `1` among nonblank selected records  
**Grouping:** `ETENURE` × monthly `THINCPOV` income-to-poverty-ratio band  
**Labels and definitions:** [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

## The intersectional comparison

| Tenure | Monthly income-to-poverty ratio | Unable to pay rent/mortgage | Unable to pay utility bills | Hungry but did not eat because of money | One job |
|---|---|---:|---:|---:|---:|
| Owned/bought | Below 1.00x | 7.02% | 13.69% | 30.54% | 24.92% |
| Owned/bought | 1.00–1.99x | 4.87% | 12.01% | 24.07% | 32.78% |
| Owned/bought | 2.00–3.99x | 2.88% | 5.19% | 15.43% | 47.18% |
| Owned/bought | 4.00x or more | 1.28% | 2.10% | 15.65% | 62.90% |
| Rented | Below 1.00x | 16.29% | 18.11% | 33.95% | 22.80% |
| Rented | 1.00–1.99x | 12.82% | 17.08% | 29.97% | 42.31% |
| Rented | 2.00–3.99x | 8.67% | 11.50% | 29.44% | 63.44% |
| Rented | 4.00x or more | 4.24% | 5.31% | 27.15% | 75.03% |
| Rent-free | Below 1.00x | 3.58% | 11.67% | 39.97% | 29.51% |
| Rent-free | 1.00–1.99x | 3.54% | 17.30% | 15.14% | 30.95% |
| Rent-free | 2.00–3.99x | 1.83% | 7.92% | 6.09% | 54.22% |
| Rent-free | 4.00x or more | 1.99% | 3.30% | 9.40% | 62.12% |

## What this adds

The two-way layer makes the distribution more specific than either tenure or resource band alone. In the selected records, below-poverty renters have the highest observed shares for rent/mortgage difficulty, utility-payment difficulty, and hunger because of money. The renter gradient persists across resource bands for the housing and utility measures, although the size of the gap changes.

This supports a sharper research question: how much of the housing/energy burden pattern is associated with resources, tenure, local prices, household composition, coverage, or institutional rules? It does not answer that question. Income-to-poverty ratio and tenure are correlated with many omitted conditions, and the measures have different official universes.

The one-job column is not a welfare score. It changes sharply across resource bands, but job count does not reveal hours, pay, schedule, commute, benefits, or whether work was freely chosen. The rent-free group also should not be interpreted as secure: its housing arrangement may involve family dependence, informal exchange, crowding, or other unmeasured conditions.

## Limits

- Results are person-weighted diagnostics, not household counts.
- Household fields are repeated on person records.
- The nonblank denominator is not a replacement for every official field universe and status flag.
- No survey-design variance, confidence intervals, or multiple-comparison adjustment was computed.
- The table does not connect a specific bill or institutional decision to a later choice, health outcome, trust judgment, political action, firm response, or geopolitical effect.

The design-based uncertainty check is now recorded in the [Fay-BRR tenure × resource estimates](sipp-fay-brr-tenure-resource-estimates-v1.md). Treat this point-only table as exploratory and use that companion for the uncertainty-aware comparison.

## Next test

Add region and household composition, then estimate design-based uncertainty. Pair the SIPP strata with CE, RECS, NHTS, MEPS, utility, insurance, or administrative records only as separate population/place layers unless a valid person or household join exists.
