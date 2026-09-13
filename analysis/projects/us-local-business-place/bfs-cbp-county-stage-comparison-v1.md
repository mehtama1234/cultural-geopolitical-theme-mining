# BFS and CBP county business-stage comparison

**Checked:** 2026-09-12  
**Sources:** [Census annual county Business Formation Statistics](https://www.census.gov/econ/bfs/data/county.html) and [Census County Business Patterns](https://www.census.gov/data/developers/data-sets/cbp-zbp/cbp-api.html)  
**Status:** matched county scale diagnostic; not a formation, survival, or local-service rate.

## The question

The firm/place program needs to separate early interest in starting a business
from a durable employer presence. This pass aligns the 2026 BFS county
application workbook with the 2023 CBP county file:

```text
EIN application flow
  -> projected/actual formation
  -> employer establishment stock
  -> payroll, jobs, services, ownership, and local relationship
```

Only the first and third quantities are used here, and they are deliberately
not treated as a conversion rate.

## Reproduction record

- BFS workbook: `https://www.census.gov/econ/bfs/xlsx/bfs_county_apps_annual.xlsx`
- BFS SHA-256: `327cd7fb8877da4e8d6e82bbe5737c2c78138ff03bd8cd0e68d7707ec3451f5e`
- CBP 2023 county file: `https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip`
- CBP SHA-256: `e9539e96ceb91608ad44ab1cfc651d7c1ff9b88bddfe7a8ff64134ccde6e9603`
- Match key: state FIPS + county FIPS; county names are not used as identifiers.
- CBP measure: `est` in the all-industry `naics="------"` row.
- Reproduction script: `scripts/analyze_bfs_cbp_county_stage_comparison.py`

Run:

```text
python3 scripts/analyze_bfs_cbp_county_stage_comparison.py \
  --bfs /path/to/bfs_county_apps_annual.xlsx \
  --cbp /path/to/cbp23co.zip
```

The files matched for 3,142 counties. Restricting the diagnostic to counties
with at least 10 all-industry employer establishments leaves 3,138 counties.

## Scale diagnostic

Across the matched counties, the median ratio of annual BFS applications to the
2023 CBP employer-establishment count was:

| BFS application year | Median applications / 2023 establishments | Counties with ≥10 establishments |
|---|---:|---:|
| 2023 | 0.487 | 3,138 |
| 2024 | 0.469 | 3,138 |
| 2025 | 0.532 | 3,138 |

This says that the typical county's application flow is a substantial fraction
of its existing establishment stock, not that 47%, 47%, or 53% of applications
became employers. Applications can be non-employer businesses, repeat or
unrealized intentions, relocations, administrative changes, or later firms;
CBP establishments are a stock measured in a different reference period.

## What the diagnostic catches

The matched comparison identifies obvious cells for review. Sheridan County,
Wyoming, for example, has BFS values of 34,032 applications in 2023, 38,208 in
2024, and 47,787 in 2025 against 2,670 CBP establishments in 2023. The ratio is
so far from the county distribution that it should not be interpreted as a
local entrepreneurship surge without resolving the release's disclosure-noise
and data-quality questions.

At the other end, some counties have zero or near-zero annual application
values against positive establishment counts. These may be small-cell or noise
effects, not proof that no businesses formed. The current BFS release warns
that county applications use differentially private geometric noise.

## What can safely be said

The comparison supports three limited statements:

1. Business applications and employer establishments are different stages and
   different statistical objects.
2. County application counts need quality checks and cannot be promoted into
   durable-firm or local-service claims by themselves.
3. The next firm/place test needs a formation or survival measure, not only a
   second application count.

It does not establish which places are entrepreneurial, which applications
became firms, whether firms created jobs or services, or whether local identity
or political voice changed.

## Next stage comparison

For each matched place, add projected or actual employer formation, survival,
employment, payroll, industry, ownership, population, rents, credit,
essential-service access, and local political measures. Use pooled periods and
larger geographies where privacy noise or sparse cells make county estimates
unstable. Include places where applications rise but durable establishments,
jobs, or services do not as counterexamples.

## Relation to the broad program

This is the firm/place counterpart to the program's general rule: a visible
input signal is not the downstream outcome. Just as a complaint is not a remedy
and a vote report is not a political cause, a business application is not a
firm, job, service, local belonging, or geopolitical capability.
