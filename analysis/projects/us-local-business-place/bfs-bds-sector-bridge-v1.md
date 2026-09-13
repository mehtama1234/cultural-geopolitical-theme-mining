# BFS applications to BDS sector dynamics bridge v1

**Checked:** 2026-09-12  
**Question:** Which sectors attract application activity, and how does that compare with realized establishment and job flows?

## Why this is a societal trend layer

The project is not asking whether one household started one business. It is asking whether changing economic conditions are reorganizing the sectors through which people encounter work, prices, care, food, transport, information, and local services.

This national sector bridge compares an early signal with a realized annual flow:

```text
EIN applications by sector (BFS)
  -> establishment openings/closings and jobs (BDS)
  -> sector capacity and turnover
  -> consumer access, work, prices, culture, and politics
```

## Sources and method

- [Census weekly BFS by industry](https://www.census.gov/econ/bfs/data/weeklynaics.html), [sector CSV](https://www.census.gov/econ/bfs/csv/naics2.csv): weekly national applications by 2-digit NAICS sector, summed across 2023 weeks.
- [Census BDS 2023 sector table](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_sec.csv): annual national establishment and job dynamics.
- BFS SHA-256: `4f8c6f5b8c56c7b6e856845609e2b9a374db649326f99f897c10160098212f4a`.
- BDS SHA-256: `758a263b166167e9557d4fc4ba8cd60229c5e05d341214b7494982c4764cf224`.
- Reproduction: `python3 scripts/analyze_bfs_bds_sector_bridge.py --bfs /path/to/naics2.csv --bds /path/to/bds2023_sec.csv --year 2023`.

BFS application counts are rounded weekly estimates and are not expected to sum exactly to the published total. Census also warns that the industry series may be revised and that the current release was restated to the 2022 NAICS vintage. BDS establishment openings are not the same thing as BFS applications becoming firms; the annual timing and construction differ.

## 2023 selected sectors

| Sector | BFS applications | BDS establishment openings | BDS establishment closings | BDS net job creation |
|---|---:|---:|---:|---:|
| Construction | 546,160 | 90,679 | 77,211 | 242,798 |
| Manufacturing | 95,440 | 18,443 | 18,782 | 154,526 |
| Retail trade | 971,630 | 77,369 | 69,636 | 52,232 |
| Transportation and warehousing | 393,310 | 37,750 | 37,291 | 128,978 |
| Health care and social assistance | 325,200 | 98,281 | 70,254 | 881,400 |
| Accommodation and food services | 302,250 | 78,150 | 64,285 | 791,588 |

The application-to-opening ratios are not conversion rates, but they show why the stages must remain separate: roughly 12.6 applications per BDS opening in retail, 10.4 in transportation, 6.0 in construction, 5.2 in manufacturing, 3.9 in accommodation/food, and 3.3 in health/social assistance under this simple same-year comparison.

## What the contrast suggests

1. **Consumer-facing volume is not the same as job expansion.** Retail has the largest application count among these sectors but comparatively small net job creation in 2023.
2. **Care and food combine entry, exit, and employment growth.** High net job creation coexists with substantial openings and closings, so sector growth may still mean churn for workers and uneven access for consumers.
3. **A sector can be socially important without attracting the most applications.** Health/social assistance has fewer applications than retail or construction but much larger net job creation and a large employer base.
4. **“Entrepreneurship” is not one cultural trend.** The meaning of application growth depends on whether it represents independent work, employer formation, replacement, platform-mediated activity, care capacity, local access, or speculative entry.

## Boundaries

This bridge is national and descriptive. It does not identify firms, owners, workers, customers, locations, quality, wages, ownership concentration, informal activity, or political attitudes. It cannot establish that an application caused an opening, that an opening improved access, or that sector change caused a cultural or political response.

## Next depth pass

Use the sector bridge to select contrasting mechanisms, then connect them to additional evidence: retail price/access and closures; health-care availability and work; transport and delivery dependence; food-service schedules and household time; manufacturing wages and regional identity. The test should preserve the full chain and seek counterexamples where sector entry rises without improved access or bargaining power.
