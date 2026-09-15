# ACS PUMS mobility subgroups v1

**Checked:** 2026-09-13  
**Source:** [2024 ACS PUMS](https://www2.census.gov/programs-surveys/acs/data/pums/2024/1-Year/) and [2024 PUMS data dictionary](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2020-2024.csv)  
**Analysis:** [analyze_acs_pums_mobility_subgroups.py](../../../scripts/analyze_acs_pums_mobility_subgroups.py)

## Result

The person/household microdata sharpen the aggregate mobility picture:

| Subgroup | No vehicle | Commute 30+ min |
|---|---:|---:|
| Household income under $35k | 22.25% | 32.30% |
| Household income $75k+ | 3.74% | 40.98% |
| Black workers | — | 42.64% |
| White workers | — | 36.64% |

Two currencies move differently. Vehicle scarcity is strongly income-graded,
while long commute exposure is higher among higher-income households and Black
workers in this unadjusted screen. That is not a contradiction: commute length
can reflect housing/job sorting and metropolitan structure, while vehicle
scarcity reflects a different resource constraint.

## Method and coding audit

Housing records are grouped by `HINCP` and weighted with `WGTP`; person records
are joined by `SERIALNO` and commute measures use `PWGTP`. Positive `JWMNP`
defines the non-work-from-home commute universe, and 30-plus minutes combines
the direct numeric commute measure. The 2024 PUMS dictionary was checked before
promotion: `RAC1P=6` is Asian, `RAC1P=4–5` are American Indian/Alaska Native
categories, and `RAC1P=7` is Native Hawaiian/Pacific Islander.

## Boundaries and next test

This is a cross-sectional descriptive comparison with no replicate-weight
interval in the first release. Household income is past-year income, not
liquid cash or affordability; race differences are not mechanisms; commute
duration is not total travel or care access. The next test is design-based
uncertainty plus explicit state, urban-form, transit-mode, disability, and
household-income interactions, followed by links to actual fares, fuel/repair
costs, care trips, and missed activities.

The bounded results are preserved in the [machine-readable trend record](../../records/us-acs-pums-mobility-subgroups-2024.json).
