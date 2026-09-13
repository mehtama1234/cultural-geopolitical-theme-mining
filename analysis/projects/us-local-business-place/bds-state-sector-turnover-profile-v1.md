# BDS state-sector turnover profile v1

**Checked:** 2026-09-12  
**Question:** Does “business dynamism” mean the same thing in every sector and state?

## Result in plain words

No. The 2023 BDS state-sector table shows distinct turnover profiles. Food services had positive median net job growth in every state in this selected set, while transportation had establishment exit rates above entry rates in 36 of 51 states and retail had negative net job growth in 17 states. Manufacturing had exit above entry in 26 states. These are sector and place patterns, not evidence that a particular household or business experienced them.

## Source and method

- [Census BDS program](https://www.census.gov/programs-surveys/bds.html).
- [2023 state-sector CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_sec.csv), SHA-256: `ba73f1ad58749d57f04c6bb56b0618c92384897a3e9f793de0df7b23f1f1868a`.
- Reproduction: `python3 scripts/analyze_bds_state_sector_profile.py --csv /path/to/bds2023_st_sec.csv --year 2023`.
- Unit: 51 states plus DC; each row is a state-sector aggregate.

The file reports establishment entry and exit rates and net job creation rates. Rates are useful for comparing places of different size, but they do not measure service quality, wages, ownership, or consumer access.

## 2023 selected profile

| Sector | Median entry rate | Entry-rate p25–p75 | Median exit rate | Median net job-creation rate | States with negative net job rate | States where exit exceeded entry |
|---|---:|---:|---:|---:|---:|---:|
| Construction | 12.77% | 11.40–13.52% | 10.54% | 3.67% | 3 | 4 |
| Manufacturing | 6.81% | 5.78–8.04% | 6.79% | 1.39% | 6 | 26 |
| Retail trade | 7.48% | 6.83–8.33% | 6.60% | 0.70% | 17 | 4 |
| Transportation and warehousing | 12.98% | 11.85–15.05% | 13.43% | 1.56% | 15 | 36 |
| Health care and social assistance | 10.23% | 9.11–11.56% | 7.50% | 2.94% | 5 | 1 |
| Accommodation and food services | 10.82% | 10.37–11.61% | 9.00% | 5.27% | 0 | 1 |

## What this contributes to the broad societal program

1. **Sector growth has different social meanings.** Retail, care, transport, and food are all everyday systems, but their entry, exit, and job profiles differ. “More businesses” cannot stand in for more access, stability, or bargaining power.
2. **Churn can be a hidden part of expansion.** A sector may add jobs nationally while some states experience high exit or negative net job change. Workers and consumers can therefore experience instability inside aggregate growth.
3. **Place mediates the trend.** The same sector can be expanding in one state and contracting in another. Any cultural or political interpretation needs the local exposure, attribution, and response—not only a national average.
4. **The firm layer connects to consumer themes.** High turnover may change travel, waiting, prices, service continuity, schedule control, or dependence on large providers. Each downstream claim needs its own measure.

## Boundaries and next test

This is descriptive and cross-sectional. It does not establish causes, firm survival, worker quality, consumer welfare, local identity, or political response. The next test should select contrasting state-sector cases—for example, transport with exit above entry, retail with negative net jobs, and food with positive net jobs—then attach measured prices, access, wages, working time, ownership, complaints, and civic response.
