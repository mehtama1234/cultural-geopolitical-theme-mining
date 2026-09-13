# CBP essential-sector capacity by rural/urban place v1

**Checked:** 2026-09-12  
**Question:** Are essential-sector establishments distributed differently in metropolitan and nonmetropolitan counties?

## Result in plain words

Yes, but the pattern is sector-specific. Using the 2023 USDA Rural-Urban Continuum Codes, 1,185 matched counties were metropolitan (codes 1–3) and 1,943 were nonmetropolitan (codes 4–9). In the population-weighted comparison, nonmetro counties had more retail establishments per 10,000 residents and more manufacturing establishments, while metro counties had more health/social-assistance establishments. Food-service capacity was nearly the same on a population-weighted basis.

This is a place-capacity pattern, not proof that rural residents have better retail access or that metro residents receive better care. Travel across county lines, establishment size, public provision, prices, quality, and unmet need are not measured here.

## Sources and method

- [Census County Business Patterns 2023](https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip), SHA-256: `e9539e96ceb91608ad44ab1cfc651d7c1ff9b88bddfe7a8ff64134ccde6e9603`.
- [Census county population estimates](https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/totals/co-est2024-alldata.csv), SHA-256: `abcc8720d669e793bbfdcd440eeec37a78db3b452adbe4ccd1eadf7c72b522b9`.
- [USDA ERS 2023 Rural-Urban Continuum Codes](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes), [CSV](https://www.ers.usda.gov/media/5768/2023-rural-urban-continuum-codes.csv?v=94035), SHA-256: `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7`.
- Reproduction: `python3 scripts/analyze_cbp_capacity_rural_urban.py --cbp /path/to/cbp23co.zip --population /path/to/co-est2024-alldata.csv --rucc /path/to/rucc2023.csv`.

Capacity is establishments per 10,000 residents. “Population-weighted” divides all establishments in the group by all residents in the group. The county median gives the typical county a different weight and is reported alongside it.

## 2023 population-weighted capacity

| Sector | Metro counties | Nonmetro counties | Metro matched counties | Nonmetro matched counties |
|---|---:|---:|---:|---:|
| Manufacturing | 8.09 | 10.63 | 1,185 | 1,943 |
| Retail trade | 30.04 | 36.84 | 1,185 | 1,943 |
| Health care and social assistance | 30.56 | 24.73 | 1,185 | 1,943 |
| Accommodation and food services | 23.24 | 23.65 | 1,185 | 1,943 |

County medians tell a related but not identical story: manufacturing 7.85 metro versus 9.51 nonmetro; retail 29.16 versus 36.46; health/social assistance 24.04 versus 22.52; and food 20.12 versus 21.23.

## What this contributes to the broad program

1. **Rural and urban consumer life is sectorally different.** A single rural/urban “service access” label hides different patterns for production, retail, care, and food.
2. **Capacity and access can diverge.** A higher establishment count per resident may coexist with longer travel, fewer hours, lower staffing, or higher prices.
3. **The pattern points toward different social dependencies.** Low local care capacity may increase travel or family-care burdens; low manufacturing capacity may change work and local identity; retail presence may not imply bargaining power or affordability.
4. **Place is an intermediary, not a conclusion.** The next evidence must measure travel, service use, unmet need, wages, prices, ownership, and political response.

## Boundaries and next test

The 2023 RUCC classification uses updated metro and urban criteria, and ERS warns that changes over time reduce comparability across decades. This pass is therefore a 2023 cross-sectional profile. Next, combine it with establishment employment, BDS turnover, Census travel/commuting measures, HRSA care-shortage or service-use measures, food-access data, and local political outcomes.
