# County growth, provider-shortage context, and visible capacity v1

**Checked:** 2026-09-13  
**Status:** exploratory conditioned county comparison; not a migration or service-access causal estimate

## Question

The existing growth/capacity screen found lower visible health-sector capacity
per resident in faster-growing counties. This pass asks whether that contrast
is simply an artifact of provider-shortage composition by showing population
growth quartile and designated HPSA status together.

```text
population change
  + provider-shortage context
  -> visible health-sector establishments/employment
  -> housing and practical-access questions
```

The unit is a county with at least 100,000 residents, usable 2020 and 2023
population estimates, CBP 2023 sector fields, and the HPSA context flag. The
620-county panel is deduplicated before forming four equal-count growth
quartiles. HPSA status is not a person-level or provider-quality measure.

## Results

Median values within each growth-quartile/HPSA cell:

| Growth quartile | HPSA counties | Median health establishments/10k | Median health employment/10k | Median gross rent |
|---|---:|---:|---:|---:|
| Q1 lowest growth | 149 | 30.32 | 724.25 | $1,087 |
| Q2 | 141 | 29.07 | 670.92 | $1,162 |
| Q3 | 140 | 28.84 | 647.23 | $1,209 |
| Q4 highest growth | 124 | 25.80 | 460.75 | $1,319 |

The non-HPSA cells are small: Q1 n=6, Q2 n=14, Q3 n=15, and Q4 n=31. Their
health-employment medians are 505.60, 658.85, 547.49, and 359.34 per 10,000,
respectively. They should be treated as context and counterexamples, not as
stable comparison estimates.

Within the HPSA majority, the health-employment median falls from 724.25 in
the lowest-growth quartile to 460.75 in the highest-growth quartile. Health
establishment presence also falls from 30.32 to 25.80 per 10,000. This is
consistent with the earlier capacity-lag screen, but it does not establish
that growth caused lower capacity or that a lower stock means residents lack
care: commuting, neighboring counties, provider mix, hours, prices, quality,
and within-county inequality remain unmeasured.

## Broader interpretation

Fast-growing places can show more demand and housing pressure without showing
proportionally more visible health-sector employment. That makes “growth” an
insufficient description of local social capacity. The practical societal
question is whether residents can reach, afford, and use care—not merely
whether establishments or jobs exist in the county.

The HPSA conditioning also supplies a boundary test: shortage designation and
sector capacity do not collapse into one measure. A county can be designated
and have a visible health-sector stock; a county without the flag can still
have low employment per resident. The next step must observe provider
adequacy, travel, wages, service use, and unmet need.

## What this changes in the broad program

This deepens themes 6, 7, and 8: care/social reproduction, place/mobility, and
unequal exposure. It strengthens the place hypothesis while preserving the
distinction between demographic change, institutional shortage designation,
visible firm capacity, and lived access.

## Limits and reproduction

Population change is a mixed demographic proxy, not immigration. HPSA is a
designated shortage-context flag. CBP measures establishment/employment stock,
not appointments, prices, quality, travel, or unmet need. The output has no
survey-weighted uncertainty and no respondent-level political or cultural
meaning measure.

```text
python3 scripts/analyze_migration_growth_hpsa_capacity.py \
  --panel /tmp/migration-all-620.tsv \
  --output /tmp/migration-growth-hpsa-capacity.json
```

The panel and generated JSON remain outside the repository. The reusable
analysis script is [analyze_migration_growth_hpsa_capacity.py](../../../scripts/analyze_migration_growth_hpsa_capacity.py).
