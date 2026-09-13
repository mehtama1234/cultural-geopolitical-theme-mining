# BFS–BDS state application/dynamics archetype layer v1

**Checked:** 2026-09-13  
**Unit:** 50 states plus Washington, D.C.; 2023  
**Status:** descriptive state comparison; not a firm-conversion, causal, or
local-service estimate

## The question

The earlier state comparison showed positive but incomplete associations between
normalized business applications and BDS dynamics. This pass asks what kinds of
states sit in different application-intensity groups.

```text
state application intensity
  -> establishment entry and exit
  -> job creation, destruction, and reallocation
  -> local employer/service capacity and political-economic meaning
```

The state is the comparison unit. The same businesses are not matched across
files.

## Application-intensity quartiles

Application intensity is 2023 BFS applications per 100 BDS establishments.
Rates below are BDS state rates, summarized within the application quartile.

| Application quartile | States | Median applications per 100 establishments | Median entry rate | Median exit rate | Median net-job-creation rate |
|---|---:|---:|---:|---:|---:|
| 1 (lowest) | 13 | 44.453 | 9.177 | 8.413 | 1.823 |
| 2 | 13 | 60.667 | 9.526 | 8.785 | 2.135 |
| 3 | 13 | 69.600 | 10.049 | 8.918 | 2.379 |
| 4 (highest) | 12 | 91.266 | 12.130 | 10.240 | 2.784 |

At the broad quartile level, higher application intensity coincides with higher
median entry, exit, and net-job-creation rates. That is a descriptive
association, not evidence that applications produce those outcomes. It may
reflect state composition, industry, population, reporting, timing, or shared
economic conditions.

## The counterexample states

The highest application quartile is not one social condition. It includes
places with both high entry and high exit, and places with different net-job
outcomes. In the matched file, Arizona, Colorado, Delaware, Florida, Georgia,
Nevada, Utah, and Wyoming are simultaneously in the highest application and
highest exit quartiles. Mississippi is in the highest application quartile but
not the highest entry or net-job quartile. By contrast, Alaska and Nebraska
are in the lowest application quartile while appearing in the highest net-job
quartile.

Wyoming has the largest normalized application value (306.743) and remains a
quality-sensitive case already flagged in the BFS data audit. It is retained
for transparency and should not carry the substantive conclusion by itself.

These counterexamples matter because “business dynamism” can mean expansion,
churn, or a small number of jobs created alongside substantial movement in and
out. A single application count cannot distinguish them.

## What this adds to the societal map

1. **Place-level economic change has archetypes.** High application intensity
   can coexist with high entry and high exit, moderate job growth, or a
   quality-sensitive signal.
2. **More applications do not specify local life.** The next observed layer
   must measure whether jobs become stable work, whether services reach
   residents, and who owns or controls the new capacity.
3. **State averages are sampling frames, not explanations.** The archetypes
   identify places for matched service, worker, consumer, and political tests;
   they do not explain why the places differ.

## Arrow status

| Arrow | Status | Safe conclusion | Missing evidence |
|---|---|---|---|
| Application intensity → state entry/exit | Compared | Higher application quartiles have higher median entry and exit rates | Firm matching, timing, industry mix, survival |
| State entry/exit → job creation | Compared | Job outcomes vary inside application groups; high entry/exit is not one job result | Job quality, duration, wages, worker control |
| State dynamics → service capacity | Open | Archetypes identify candidate places for access tests | Local service use, prices, quality, ownership, travel |
| State dynamics → trust/politics | Open | Place-level economic change can define a sampling frame | Attribution, local meaning, civic action, policy response |

## Boundaries and reproduction

- BFS applications are EIN-application flows; BDS establishments and jobs use a
  separate annual statistical construction.
- The normalized application measure is not a population rate or a conversion
  rate. It does not establish that an application became an establishment.
- State-level quartiles hide county, sector, ownership, race, migration,
  urban/rural, and industry differences.
- The analysis retains all 51 matched records and labels the known Wyoming
  quality issue rather than silently deleting it.

```text
python3 scripts/analyze_bfs_bds_state_archetypes.py \
  --bfs /path/to/bfs_state_apps_weekly_nsa.csv \
  --bds /path/to/bds2023_st.csv \
  --year 2023 \
  --output /tmp/bfs-bds-state-archetypes.json
```

The reusable analysis is [analyze_bfs_bds_state_archetypes.py](../../../scripts/analyze_bfs_bds_state_archetypes.py).
Related: [BFS applications and BDS realized state dynamics](bfs-bds-state-stage-comparison-v1.md),
[capacity and mobility bridge](capacity-mobility-cross-source-bridge-v1.md),
and the [broad place/firm coverage matrix](../../US-BROAD-THEME-COVERAGE-MATRIX_V1.md).
