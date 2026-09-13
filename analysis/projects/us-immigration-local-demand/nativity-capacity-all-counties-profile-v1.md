# Foreign-born share and county capacity profile v1

**Checked:** 2026-09-12  
**Status:** descriptive cross-sectional comparison; not a migration causal
estimate

## Why add this layer

Total population growth and foreign-born share are different signals. Growth
includes births, deaths, domestic moves, and international migration; a
foreign-born share is a stock, not a recent-arrival flow. Keeping both axes
visible prevents a population-capacity pattern from being mislabeled as a
migration effect.

## Reproduction

```text
python3 scripts/analyze_nativity_capacity_all_counties.py \
  --cbp /tmp/cbp23co.zip \
  --population /tmp/co-est2024-alldata.csv \
  --nativity /tmp/acsdt5y2023-b05002.dat \
  --min-population 100000
```

The run covered 620 counties, divided into four equal quartiles on each axis.
The CBP, population, and ACS source hashes are recorded in the [all-county
capacity profile](migration-capacity-all-counties-profile-v1.md) and [migration
capacity-sector bridge](migration-capacity-sector-bridge-v1.md).

## Results

| Sector | Measure | Axis | Pearson correlation | Lowest quartile median | Highest quartile median |
|---|---|---|---:|---:|---:|
| Retail | Establishments/10k | Population growth | -0.2854 | 32.06 | 27.18 |
| Retail | Establishments/10k | Foreign-born share | -0.1717 | 32.66 | 28.07 |
| Retail | Employees/10k | Population growth | -0.1598 | 502.07 | 464.64 |
| Retail | Employees/10k | Foreign-born share | -0.1955 | 496.00 | 457.65 |
| Health/social assistance | Establishments/10k | Population growth | -0.3253 | 30.30 | 25.01 |
| Health/social assistance | Establishments/10k | Foreign-born share | 0.1463 | 26.29 | 30.01 |
| Health/social assistance | Employees/10k | Population growth | -0.4475 | 712.44 | 437.94 |
| Health/social assistance | Employees/10k | Foreign-born share | 0.0431 | 586.84 | 641.79 |
| Accommodation/food | Establishments/10k | Population growth | -0.3472 | 24.05 | 19.14 |
| Accommodation/food | Establishments/10k | Foreign-born share | 0.0834 | 21.57 | 22.81 |
| Accommodation/food | Employees/10k | Population growth | -0.1742 | 426.31 | 377.49 |
| Accommodation/food | Employees/10k | Foreign-born share | 0.0296 | 398.82 | 399.61 |

The complete quartile output retains Q2 and Q3 in the reproducible TSV; this
short table shows only the endpoints for readability.

## What this changes

The population-growth axis and foreign-born-share axis do not produce the same
capacity pattern. Retail establishments and employment are lower in the
highest quartiles on both axes. Health establishments and employment decline
across population-growth quartiles, while foreign-born-share quartiles show a
small positive establishment association and near-zero employment association.
Food capacity is nearly flat across foreign-born-share quartiles but lower in
the highest-growth quartile.

This is evidence for multiple place mechanisms, not evidence that foreign-born
residents caused capacity changes. It suggests that “migration pressure” cannot
be represented by one county variable or one uniform effect.

## Limits and next test

The comparison is cross-sectional, unweighted beyond county inclusion, and
uses 2023 stocks beside 2020–2023 growth. It does not measure recent migration
flows, domestic migration, service use, quality, prices, wages, housing supply,
travel, ownership, belonging, trust, or political action. Correlation is not a
causal estimate.

Next, compare counties with similar foreign-born shares but different growth,
and similar growth but different foreign-born shares. Add arrival timing,
domestic migration, housing permits/vacancy, wages, travel, provider capacity,
and direct service-use and belonging measures. Retain places where the same
population signal produces different capacity outcomes as counterexamples.

Related: [all-county migration/place capacity profile](migration-capacity-all-counties-profile-v1.md),
[migration capacity-sector bridge](migration-capacity-sector-bridge-v1.md), and
the [broad counterexample register](../../US-BROAD-COUNTEREXAMPLE-REGISTER_V1.md).
