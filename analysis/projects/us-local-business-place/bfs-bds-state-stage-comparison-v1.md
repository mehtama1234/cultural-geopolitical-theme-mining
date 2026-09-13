# BFS applications and BDS realized state dynamics v1

**Checked:** 2026-09-12  
**Question:** Do states with more business-application activity also show more realized establishment entry, exit, and job turnover?

## What this adds

The firm/place sequence now has a geographic test:

```text
EIN applications (BFS)
  -> establishment openings/closings and job flows (BDS)
  -> employer capacity (CBP/BDS stock)
  -> services, work, prices, place, culture, and politics
```

This is a state-level descriptive comparison for 2023. It does not match the same businesses, and it does not show that an application became an establishment. State size is controlled only in the simple diagnostic by dividing applications by BDS establishments; this is not a population rate or causal estimate.

## Sources and reproduction

- [Census Business Formation Statistics state applications](https://www.census.gov/econ/bfs/csv/bfs_state_apps_weekly_nsa.csv), summed across 2023 weeks; SHA-256: `eb956eba3cdb4192b6c49a49365cab66a1596fd415e54877f7729dd4ae9ff815`.
- [Census BDS 2023 state table directory](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/).
- [BDS 2023 state CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st.csv), SHA-256: `9e0c86610ee685c2f7c8c4dec60bd213177cd8644fe539e5f66457efc8ef603c`.
- Reproduction: `python3 scripts/analyze_bfs_bds_state_stage_comparison.py --bfs /path/to/bfs_state_apps_weekly_nsa.csv --bds /path/to/bds2023_st.csv --year 2023`.

BFS defines applications from EIN applications and publishes state-level weekly series. BDS publishes annual establishment openings/closings and employment dynamics. The two programs use different constructions and reference rhythms.

## 2023 descriptive result

The files matched 51 states and the District of Columbia. Across matched states, the median was **64.93 BFS applications per 100 BDS establishments** when 2023 applications were divided by the 2023 BDS establishment stock.

The Pearson correlations between that normalized application measure and BDS state measures were:

| BDS measure | Correlation |
|---|---:|
| Establishment entry rate | 0.607 |
| Establishment exit rate | 0.458 |
| Net job creation rate | 0.423 |
| Reallocation rate | 0.367 |

The largest normalized application values were Wyoming (306.74), Delaware (222.63), Georgia (119.74), Florida (118.00), and Nevada (96.85). Wyoming is already flagged in the county BFS quality review; it should be treated as a data-quality case, not a substantive entrepreneurship finding.

## Interpretation for the broad program

The positive descriptive association with entry rates is a reason to continue the comparison, not a conclusion that applications produce growth. It may reflect population, state composition, industry mix, reporting, timing, or the same underlying economic conditions. The weaker association with net job creation reinforces that “more applications” and “more jobs” are different downstream outcomes.

This supports a broader societal question: where is business dynamism producing durable capacity, and where is it producing churn, exit, or concentrated dependence? That question can feed cultural and political analysis only after service access, worker conditions, consumer prices, ownership, local trust, or civic action are separately measured.

## Next bounded depth pass

1. Re-run this by sector using BDS state-sector tables where the BFS industry series supports a comparable classification.
2. Add population, industry mix, urban/rural context, and CBP establishment stocks before interpreting state differences.
3. Select contrasting states or counties: high applications/high entry, high applications/high exit, and low applications/high realized entry.
4. Attach observed downstream measures—service access, employment quality, prices, closures, local political participation, or public response—without treating the stage comparison as proof of a cultural or political effect.
