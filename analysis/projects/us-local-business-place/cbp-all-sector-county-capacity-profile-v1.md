# CBP all-sector county capacity profile v1

**Checked:** 2026-09-12  
**Question:** How does employer-sector presence vary across counties when the
full 2-digit CBP sector file is used rather than only four essential sectors?

## Scope and data rule

This is a descriptive county stock layer. It uses 2023 CBP establishments and
2023 Census population estimates, expressed as establishments per 10,000
residents. The run matched 3,135 county keys with at least one numeric 2-digit
sector row and a population estimate. For each sector, `numeric_count` is the
number of counties with a numeric establishment value; absent or suppressed
sector rows are excluded from that sector's distribution, not recoded as zero.

That distinction matters: a missing sector value is not evidence that a county
has no establishments.

## Reproduction

- [Census County Business Patterns 2023](https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip), SHA-256: `e9539e96ceb91608ad44ab1cfc651d7c1ff9b88bddfe7a8ff64134ccde6e9603`.
- [Census county population estimates 2020–2024](https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/totals/co-est2024-alldata.csv), SHA-256: `abcc8720d669e793bbfdcd440eeec37a78db3b452adbe4ccd1eadf7c72b522b9`.
- Reproduction: `python3 scripts/analyze_cbp_county_all_sector_capacity.py --cbp /path/to/cbp23co.zip --population /path/to/co-est2024-alldata.csv`.
- Employment reproduction: `PYTHONPATH=scripts python3 scripts/analyze_cbp_county_all_sector_employment.py --cbp /path/to/cbp23co.zip --population /path/to/co-est2024-alldata.csv`.

## 2023 county distributions

| Sector | Numeric counties | Median per 10,000 | 25th percentile | 75th percentile |
|---|---:|---:|---:|---:|
| Agriculture, forestry, fishing, hunting | 1,905 | 1.70 | 0.62 | 4.11 |
| Mining, quarrying, oil and gas | 1,386 | 1.38 | 0.44 | 4.88 |
| Utilities | 1,814 | 1.13 | 0.58 | 2.23 |
| Construction | 3,074 | 23.00 | 16.40 | 32.61 |
| Manufacturing | 2,888 | 9.19 | 6.58 | 12.73 |
| Wholesale trade | 2,905 | 8.56 | 5.90 | 12.80 |
| Retail trade | 3,124 | 33.21 | 27.46 | 40.73 |
| Transportation and warehousing | 3,002 | 8.61 | 6.09 | 12.94 |
| Information | 2,588 | 3.66 | 2.75 | 5.11 |
| Finance and insurance | 3,022 | 12.27 | 9.19 | 16.34 |
| Real estate, rental, leasing | 2,754 | 8.27 | 5.84 | 12.10 |
| Professional, scientific, technical | 3,012 | 14.29 | 10.22 | 20.75 |
| Management of companies | 1,240 | 1.11 | 0.76 | 1.65 |
| Administrative, support, waste management | 2,816 | 9.53 | 6.96 | 13.06 |
| Educational services | 1,887 | 2.28 | 1.58 | 3.38 |
| Health care and social assistance | 3,072 | 23.14 | 16.96 | 29.91 |
| Arts, entertainment, recreation | 2,496 | 3.74 | 2.60 | 5.57 |
| Accommodation and food | 3,083 | 20.94 | 15.96 | 26.30 |
| Other services | 3,101 | 24.65 | 19.82 | 30.26 |
| Unclassified | 628 | 0.30 | 0.21 | 0.51 |

## Employment scale

The same file reports employment for a different subset of sector/county rows.
These figures use only numeric `emp` values and the same population denominator;
they are not staffing adequacy or job-quality measures.

| Sector | Numeric counties | Median employees per 10,000 | 25th percentile | 75th percentile |
|---|---:|---:|---:|---:|
| Agriculture, forestry, fishing, hunting | 1,905 | 6.83 | 1.97 | 22.62 |
| Mining, quarrying, oil and gas | 1,386 | 13.04 | 3.72 | 67.64 |
| Utilities | 1,814 | 18.38 | 10.49 | 34.37 |
| Construction | 3,074 | 146.46 | 92.20 | 217.40 |
| Manufacturing | 2,888 | 345.10 | 161.32 | 634.24 |
| Wholesale trade | 2,905 | 101.92 | 53.82 | 176.24 |
| Retail trade | 3,124 | 404.91 | 296.61 | 511.66 |
| Transportation and warehousing | 3,002 | 84.45 | 45.09 | 163.81 |
| Information | 2,588 | 27.69 | 16.12 | 49.28 |
| Finance and insurance | 3,022 | 76.21 | 49.23 | 114.67 |
| Real estate, rental, leasing | 2,754 | 26.07 | 14.11 | 48.28 |
| Professional, scientific, technical | 3,012 | 69.47 | 41.14 | 121.82 |
| Management of companies | 1,240 | 32.87 | 12.88 | 84.43 |
| Administrative, support, waste management | 2,816 | 88.23 | 41.28 | 161.88 |
| Educational services | 1,887 | 36.56 | 17.45 | 83.74 |
| Health care and social assistance | 3,072 | 438.56 | 284.27 | 623.16 |
| Arts, entertainment, recreation | 2,496 | 32.95 | 15.77 | 61.66 |
| Accommodation and food | 3,083 | 290.86 | 185.35 | 413.69 |
| Other services | 3,101 | 114.16 | 80.84 | 154.13 |
| Unclassified | 628 | 0.36 | 0.19 | 0.67 |

Employment and establishment presence can diverge. Retail and health/social
assistance have similar broad numeric coverage, but their employment medians
and the scale of each establishment can differ. That is a reason to carry both
measures into the next place comparison rather than treating an establishment
count as capacity by itself.

## What this adds

1. Retail, construction, other services, health/social assistance, and food
   are the most broadly represented sectors among the numeric county rows;
   specialized sectors have thinner coverage and should not be compared as if
   their missingness were zero capacity.
2. Everyday local capacity has different sector shapes. Construction and
   health/social assistance have similar median establishment presence, while
   retail is higher and information is lower; those are stocks, not measures
   of staffing, quality, affordability, or use.
3. The distribution itself is a place hypothesis. A county can have visible
   establishments in one sector and sparse numeric coverage in another, so
   residents may face different combinations of work, care, food, transport,
   and information options.

## Boundaries and next test

Establishments and reported employment are not services delivered. This profile
does not measure hours, prices, quality, public provision, neighboring-county
access, ownership, worker power, or local cultural/political meaning. Numeric
coverage varies by sector and measure. Next, combine sector stocks with
employment,
openings/closings, rurality, travel, prices, public capacity, and actual use or
unmet need. Preserve missingness and retain places where visible capacity does
not produce practical access as counterexamples.

Related: [CBP county essential-sector capacity](cbp-county-essential-capacity-population-layer-v1.md),
[complete BFS–BDS sector profile](bfs-bds-complete-sector-profile-v1.md), and the
[capacity and mobility bridge](capacity-mobility-cross-source-bridge-v1.md).
