# BDS metro/nonmetro turnover profile v1

**Checked:** 2026-09-18  
**Question:** Does 2023 employer turnover have the same sector profile in
metro and nonmetro counties?

## Result in plain words

No. The place type changes the sector pattern. In the comparable county-sector
rows, nonmetro counties had a higher median retail net-job-creation rate than
metro counties (1.141% versus 0.799%), but lower median health/social-
assistance growth (1.983% versus 3.155%) and accommodation/food growth (2.880%
versus 4.745%). Transportation was near zero in nonmetro counties while still
positive in metro counties (0.000% versus 0.395%).

The negative-row pattern is also different. Nonmetro health rows were negative
in 36.0% of comparable rows versus 24.5% in metro counties; food rows were
negative in 33.7% versus 16.5%. Retail is a counterweight: its negative-row
shares were similar (36.1% nonmetro and 38.5% metro), despite the higher
nonmetro median net-job rate.

| Sector | Metro comparable rows | Metro median net job rate | Nonmetro comparable rows | Nonmetro median net job rate | Metro negative rows | Nonmetro negative rows |
|---|---:|---:|---:|---:|---:|---:|
| Retail trade | 1,021 | 0.799% | 1,141 | 1.141% | 393 (38.5%) | 412 (36.1%) |
| Transportation/warehousing | 864 | 0.395% | 668 | 0.000% | 407 (47.1%) | 317 (47.5%) |
| Health/social assistance | 956 | 3.155% | 976 | 1.983% | 234 (24.5%) | 351 (36.0%) |
| Accommodation/food | 987 | 4.745% | 1,076 | 2.880% | 163 (16.5%) | 363 (33.7%) |

## Source and reproduction

- [Census 2023 county–sector BDS table](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv), official file size 274,770,797 bytes and last modified 2025-09-25.
- [USDA 2023 Rural-Urban Continuum Codes](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes), CSV SHA-256: `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7`.
- BDS retrieval used a transient 12,000,000-byte suffix containing the 2023 block; suffix SHA-256: `988039900c4244fba737cbe2bd37c37d2bf42f81d88121207ed9d842cb5a7d7b`.
- Reproduction: `python3 scripts/analyze_bds_rural_urban_turnover.py --bds-suffix /path/to/bds-suffix.csv --rucc /path/to/rucc2023.csv --output /path/to/output.json`.
- Machine-readable result: [`data/bds-rural-urban-turnover-2026-09-18.json`](data/bds-rural-urban-turnover-2026-09-18.json).

Metro means USDA RUCC codes 1–3; nonmetro means codes 4–9. BDS rows marked
`D`, `N`, or `S` are excluded from rate comparisons rather than treated as
zero. Rows are county-sector aggregates, not firms, workers, establishments
with identifiable owners, or residents.

## What this adds to the atlas

```text
place type
  -> sector-specific establishment entry, exit, and job-flow profile
  -> [open] reachable service alternatives, prices, work quality, and household time
  -> [open] trust, political response, and state or geopolitical consequence
```

This is a useful warning against a single rural/urban capacity score. A
nonmetro retail pattern can coexist with weaker health, food, and transport
job-flow profiles. Higher or lower net job creation is not itself proof of
better access, affordability, quality, or worker security.

## Limits and next test

This is a 2023 cross-sectional descriptive comparison. It does not establish
why the groups differ, whether a new establishment replaced a lost one, where
residents travel, or whether a job-flow change altered care, food, mobility,
prices, wages, trust, or political action. RUCC metro/nonmetro status is also
not a travel-time or service-use measure. The next useful extension is a small
same-geography panel that adds measured vehicle/travel constraints or service
use to one sector contrast, retaining the retail counterexample and the
health/food divergence.
