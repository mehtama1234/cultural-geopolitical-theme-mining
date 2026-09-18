# BDS county realized turnover profile v1

**Checked:** 2026-09-18  
**Question:** Does a positive national or state business-dynamics signal imply
that counties have stable employer capacity?

## Result in plain words

No. The 2023 Census BDS state–county aggregate file contains 3,194 county
rows across 51 state codes (50 states plus DC). Among 3,107 county rows with
both establishment entry and exit rates reported, 907 had an exit rate above
the entry rate. Among the same broad county universe, 885 had negative net job
creation rates. The median entry rate was 9.463%, the median exit rate 8.527%,
and the median net job-creation rate 1.912%.

This is a realized employer-flow layer at county scale. It is not a sector
result: the selected nationwide file is aggregated across industries. The
existing BDS state-sector layer remains the appropriate source for sector
differences.

## Source and reproducibility

- [Census BDS program](https://www.census.gov/programs-surveys/bds.html)
- [2023 BDS state–county table directory](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/)
- [2023 BDS state–county CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty.csv)
- SHA-256: `7592cb39c1dcd712815c29a6452b258674529d4aed0de07acb5eb13c76d309114`

The raw 18.9 MB table is not retained in the repository. The compact derived
summary is stored in
`data/bds-county-turnover-profile-2026-09-18.json`.

## Bounded 2023 profile

| Measure | Result |
|---|---:|
| County rows | 3,194 |
| Rows with positive reported establishments | 3,192 |
| Rows with comparable entry and exit rates | 3,107 |
| Rows with negative net job-creation rate | 885 |
| Rows where exit rate exceeded entry rate | 907 |
| Median establishment entry rate | 9.463% |
| Median establishment exit rate | 8.527% |
| Median net job-creation rate | 1.912% |

The county patterns include both high-turnover expansion and contraction. For
example, state/county FIPS `56/033` reports 26.599% entry and 14.366% exit
with 7.214% net job creation, while `48/033` reports equal 36.364% entry and
exit with -3.922% net job creation. `32/021` reports 10.256% entry, 22.222%
exit, and -57.448% net job creation. These are illustrative records, not
representative county case studies; small denominators and disclosure marks
matter.

## What this adds to the atlas

```text
business application signal
  -> realized county employer openings/closings and job flows
  -> [open] sector/service composition, survival, wages, access, and local response
```

The layer makes “local business capacity” less likely to be read as a stock or
national average. A county can have positive net jobs while experiencing high
entry and exit, or have visible openings while net employment falls. That is a
useful counterexample to treating entry as durable local option creation.

## Boundaries and next test

The file does not identify individual firms, industry, ownership, wages,
service quality, prices, customer use, worker control, household burden,
political response, or geopolitical consequence. It also does not link a BFS
application to a BDS opening. Suppressed values are not zeros, and county
FIPS rows are not named places in this summary.

The next decisive bridge is a matched county–sector or dated event design
that preserves a comparable denominator and attaches measured service access,
work/time, price, ownership, or civic response. Keep both counterexamples:
high turnover with positive net jobs, and entry/exit activity with negative net
jobs.
