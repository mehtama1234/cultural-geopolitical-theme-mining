# Capacity-pattern rurality sensitivity v1

**Checked:** 2026-09-12
**Status:** descriptive stratification; not a migration causal estimate

## Why this check matters

The all-county capacity profiles combine places with very different settlement
structures. A negative growth/capacity relationship could be mostly a
metro/nonmetro composition pattern. This pass repeats the comparison inside
USDA 2023 RUCC groups rather than treating the pooled result as universal.

The frame contains 620 counties above 100,000 residents with population,
foreign-born-share, RUCC, and selected CBP records: 593 metro and 27 nonmetro
counties. The nonmetro sample is small and should not be read as a stable
national estimate.

## Reproduction

```text
python3 scripts/analyze_migration_capacity_by_rurality.py \
  --cbp /tmp/cbp23co.zip \
  --population /tmp/co-est2024-alldata.csv \
  --nativity /tmp/acsdt5y2023-b05002.dat \
  --rucc /tmp/rucc2023.csv \
  --min-population 100000
```

The complete output has 24 sector/measure/axis rows and was reproduced as
`/tmp/migration-rurality.tsv` during this pass.

## Selected sensitivity results

The table reports Pearson correlation between the axis and per-capita capacity;
the quartile columns compare the lowest and highest axis quartiles within each
place group.

| Place group | Sector | Measure | Axis | Pearson | Low-quartile median | High-quartile median |
|---|---|---|---|---:|---:|---:|
| Metro (n=593) | Retail | Establishments/10k | Population growth | -0.2975 | 32.00 | 27.18 |
| Metro (n=593) | Health/social assistance | Establishments/10k | Population growth | -0.3440 | 30.45 | 25.06 |
| Metro (n=593) | Health/social assistance | Employees/10k | Population growth | -0.4637 | 730.34 | 433.61 |
| Metro (n=593) | Accommodation/food | Establishments/10k | Population growth | -0.3725 | 24.00 | 19.13 |
| Metro (n=593) | Retail | Establishments/10k | Foreign-born share | -0.1628 | 32.27 | 28.20 |
| Metro (n=593) | Health/social assistance | Establishments/10k | Foreign-born share | 0.1420 | 26.28 | 30.03 |
| Nonmetro (n=27) | Retail | Establishments/10k | Population growth | 0.0275 | 35.45 | 35.67 |
| Nonmetro (n=27) | Health/social assistance | Establishments/10k | Population growth | 0.0641 | 23.50 | 21.92 |
| Nonmetro (n=27) | Health/social assistance | Employees/10k | Population growth | -0.1011 | 543.08 | 429.12 |
| Nonmetro (n=27) | Accommodation/food | Establishments/10k | Foreign-born share | 0.1412 | 20.47 | 24.74 |

## What this changes

The pooled negative growth/capacity pattern is concentrated in the metro
portion of this thresholded frame. Within the 27 nonmetro counties, the
population-growth correlations are near zero for retail, health, and food
establishments, although the small health-employment comparison remains
negative. Foreign-born-share relationships also differ by place group: metro
health establishments are positive while nonmetro health establishments are
negative.

This is a useful confounder result. It means the broad place hypothesis should
be stated conditionally: growth and capacity may relate differently by settlement
structure. It does not tell us whether differences arise from migration,
commuting, industry mix, housing, measurement, neighboring places, or service
use.

## Limits and next test

RUCC is a place classification, not a measure of access. The comparison remains
cross-sectional, uses 2023 capacity stocks beside 2020–2023 growth and 2023
foreign-born stocks, and has only 27 nonmetro counties above the population
threshold. It does not measure recent migration flows, quality, prices, wages,
travel, ownership, unmet need, belonging, trust, or political action.

Next, use a larger all-county frame or matched metro/nonmetro places with
similar sector mix, then add domestic and international migration flows,
housing supply, commuting, wages, provider capacity, and direct service-use
measures. Preserve metro and nonmetro counterexamples rather than pooling them
into one capacity story.

Related: [all-county migration/place capacity profile](migration-capacity-all-counties-profile-v1.md),
[foreign-born share and capacity profile](nativity-capacity-all-counties-profile-v1.md),
and [migration capacity-sector bridge](migration-capacity-sector-bridge-v1.md).
