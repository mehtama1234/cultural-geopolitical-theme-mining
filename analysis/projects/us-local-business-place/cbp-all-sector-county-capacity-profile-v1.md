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

Establishments are not services delivered. This profile does not measure
employment size, hours, prices, quality, public provision, neighboring-county
access, ownership, worker power, or local cultural/political meaning. Numeric
coverage also varies by sector. Next, combine sector stocks with employment,
openings/closings, rurality, travel, prices, public capacity, and actual use or
unmet need. Preserve missingness and retain places where visible capacity does
not produce practical access as counterexamples.

Related: [CBP county essential-sector capacity](cbp-county-essential-capacity-population-layer-v1.md),
[complete BFS–BDS sector profile](bfs-bds-complete-sector-profile-v1.md), and the
[capacity and mobility bridge](capacity-mobility-cross-source-bridge-v1.md).
