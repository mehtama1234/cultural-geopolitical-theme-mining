# CBP county essential-sector capacity per population v1

**Checked:** 2026-09-12  
**Question:** How unevenly are basic employer-sector establishments distributed across US counties?

## Why this matters

The project needs to distinguish a sector's national growth from the capacity residents can reach in a particular place. This layer combines 2023 County Business Patterns establishments with 2023 Census county population estimates:

```text
employer establishments by sector + residents
  -> rough local capacity distribution
  -> access, travel, waiting, price, quality, and dependence questions
  -> cultural attachment, trust, and political response (only if measured)
```

The result is a capacity baseline, not an access or quality measure. Residents may use establishments in neighboring counties; one establishment may differ greatly in size and service; and non-employer, informal, mobile, or public provision is not captured.

## Sources and reproduction

- [Census County Business Patterns 2023](https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip), SHA-256: `e9539e96ceb91608ad44ab1cfc651d7c1ff9b88bddfe7a8ff64134ccde6e9603`.
- [Census county population estimates 2020–2024](https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/totals/co-est2024-alldata.csv), SHA-256: `abcc8720d669e793bbfdcd440eeec37a78db3b452adbe4ccd1eadf7c72b522b9`.
- Reproduction: `python3 scripts/analyze_cbp_county_capacity_per_capita.py --cbp /path/to/cbp23co.zip --population /path/to/co-est2024-alldata.csv --year 2023`.
- Match key: state FIPS + county FIPS; 3,142 county records matched.

## 2023 distribution

Establishment counts are expressed per 10,000 residents. Counties include zero-establishment observations in the distribution.

| Sector | Median | 25th percentile | 75th percentile | Counties with zero establishments |
|---|---:|---:|---:|---:|
| Manufacturing | 8.66 | 5.86 | 12.34 | 254 |
| Retail trade | 33.14 | 27.35 | 40.63 | 18 |
| Health care and social assistance | 22.95 | 16.62 | 29.64 | 70 |
| Accommodation and food services | 20.74 | 15.63 | 26.15 | 59 |

Establishment counts hide scale, so the same CBP file's employment field gives a second descriptive measure. Because CBP employment is suppressed or unavailable in some small cells, each row below uses only counties with numeric sector employment:

| Sector | Median employees per 10,000 residents | 25th percentile | 75th percentile | Counties with zero reported employees |
|---|---:|---:|---:|---:|
| Manufacturing | 345.10 | 161.32 | 634.24 | 2,888 |
| Retail trade | 404.91 | 296.61 | 511.66 | 3,124 |
| Health care and social assistance | 438.56 | 284.27 | 623.16 | 3,072 |
| Accommodation and food services | 290.86 | 185.35 | 413.69 | 3,083 |

The final column is the number of counties with numeric employment, not a zero-employment count; suppressed or unavailable cells are excluded. The establishment and employment distributions answer different questions: a county can have a sector establishment but little employment, or a small number of establishments with substantial employment. Neither measure captures hours, staffing adequacy, quality, prices, travel, or whether the service meets local need.

## What the distribution suggests

1. **Retail is broadly present but not uniformly present.** Its median is about 33 establishments per 10,000 residents, with a wide county spread. Presence alone says nothing about affordability, hours, quality, or whether a county's residents can reach the establishments.
2. **Care capacity is more uneven and has more zero counties.** Seventy matched counties have no CBP health/social-assistance establishment in this measure. That is a signal for a travel and neighboring-place test, not proof that residents have no care.
3. **Production capacity is highly place-selective.** Manufacturing has 254 zero counties and a lower median per-capita presence. That can shape local work, identity, tax base, and political economy differently from consumer-facing sectors, but those downstream effects need separate evidence.
4. **Food and care are different kinds of everyday infrastructure.** Their county distributions should not be collapsed into a single “service availability” score; establishment counts do not measure meals, clinical capacity, staffing, or continuity.

## Boundaries and next test

This is a descriptive stock measure, not a causal or household-access estimate. The next pass should add establishment employment/size, neighboring-county travel, rural/urban classification, prices, closures/openings, public provision, and actual service-use or unmet-need measures. Then test whether places with low capacity show different work, food, health, mobility, trust, or political patterns while retaining counterexamples.
