# Migration/place capacity all-county profile v1

**Checked:** 2026-09-12  
**Status:** descriptive county comparison; not a migration causal estimate

## Question

Does the capacity contrast seen in the selected 12-county screen remain visible
when the comparison uses every county above 100,000 residents with usable
2020–2023 population and CBP records?

Population change is only a proxy for local demographic change. It is not a
measure of immigration, and the capacity measures are stocks observed in 2023.
The comparison therefore tests a place hypothesis, not a migration effect.

```text
2020→2023 population change
  -> quartile comparison of 2023 sector establishments and employment
  -> capacity-lag hypothesis
  -> housing, travel, service-use, ownership, belonging, and political tests
```

## Reproduction

```text
python3 scripts/analyze_migration_capacity_all_counties.py \
  --cbp /tmp/cbp23co.zip \
  --population /tmp/co-est2024-alldata.csv \
  --min-population 100000
```

The run covered 620 counties. Each growth quartile contains 155 counties.
CBP and population source hashes are recorded in the [all-sector county
capacity profile](../us-local-business-place/cbp-all-sector-county-capacity-profile-v1.md).

## Results

| Sector | Measure | Pearson correlation with population change | Lowest-growth quartile median | Q2 median | Q3 median | Highest-growth quartile median |
|---|---|---:|---:|---:|---:|---:|
| Retail | Establishments/10k | -0.2854 | 32.06 | 30.39 | 30.09 | 27.18 |
| Retail | Employees/10k | -0.1598 | 502.07 | 505.38 | 512.77 | 464.64 |
| Health/social assistance | Establishments/10k | -0.3253 | 30.30 | 29.32 | 28.66 | 25.01 |
| Health/social assistance | Employees/10k | -0.4475 | 712.44 | 664.77 | 626.40 | 437.94 |
| Accommodation/food | Establishments/10k | -0.3472 | 24.05 | 22.86 | 22.36 | 19.14 |
| Accommodation/food | Employees/10k | -0.1742 | 426.31 | 405.22 | 426.31 | 377.49 |

## What the result supports

Among these larger counties, higher population growth is descriptively
associated with lower 2023 per-capita establishment presence in all three
selected everyday sectors. Health/social-assistance employment has the largest
negative association in this screen, and its highest-growth-quartile median is
lower than its lowest-growth-quartile median.

This is consistent with a capacity-lag hypothesis: demand or population can
grow faster than visible local capacity. It is also consistent with other
explanations, including metropolitan structure, commuting and neighboring-place
access, sector composition, housing selection, measurement timing, and the
difference between residents and jobs. The profile does not distinguish them.

## What it does not establish

It does not establish that migration caused lower capacity, that lower capacity
means unmet need, or that residents cannot use neighboring places. It does not
measure foreign-born change, service quality, prices, wages, hours, ownership,
worker bargaining, housing supply, travel, language access, belonging, trust,
or political response. County population growth can reflect births, deaths,
domestic moves, and international migration together.

## Next matched test

Add ACS nativity and arrival measures, domestic migration, housing permits and
vacancy, commuting and travel time, wages, provider and school capacity, prices,
and direct service use or unmet need. Compare places with similar growth but
different capacity trajectories, and places with similar capacity but different
growth. Preserve a counterexample where rapid growth coexists with adequate
capacity and one where capacity appears high but practical access is poor.

Related: [migration capacity-sector bridge](migration-capacity-sector-bridge-v1.md),
[all-sector county capacity](../us-local-business-place/cbp-all-sector-county-capacity-profile-v1.md),
and the [broad counterexample register](../../US-BROAD-COUNTEREXAMPLE-REGISTER_V1.md).
