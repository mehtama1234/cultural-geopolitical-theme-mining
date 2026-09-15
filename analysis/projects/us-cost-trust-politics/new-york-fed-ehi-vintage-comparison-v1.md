# New York Fed EHI vintage comparison: December 2025 to April 2026

**Checked:** 2026-09-13  
**Status:** reproducible bounded vintage comparison

## What changed

The April 2026 vintage should not be read as a simple update to a fixed group ranking. It reports a gasoline-driven reversal in several inflation positions and a new real-spending response after the March 2026 shock. The table preserves missing prior-vintage values instead of manufacturing a change score.

| Measure | December 2025 | April 2026 | Unit / interpretation |
|---|---:|---:|---|
| Hispanic inflation position | -0.4 | above national average | constructed demographic-CPI position |
| Rural inflation gap | not recorded in this vintage | 0.8 | percentage points from national inflation |
| Black/white earnings ratio | 78.7 | 78.0 | percent of white workers' earnings |
| Hispanic/white earnings ratio | 77.5 | 76.4 | percent of white workers' earnings |
| Noncollege/college earnings ratio | 57.4 | 57.0 | percent of workers with a college degree's earnings |
| Women/men earnings ratio | 81.1 | 80.7 | percent of men's earnings |

## Spending response in the new vintage

The April release reports that real gasoline and real retail-ex-auto spending fell for nearly all groups after the March 2026 gasoline shock. Lower-income groups reduced real gasoline spending more than higher-income groups, while higher-income groups increased nominal gasoline spending more. This is a group-level receipt-panel direction, not a same-household event-study estimate.

## Reading rule

The comparison is not a causal before/after estimate. Demographic inflation uses prior Consumer Expenditure Survey budget shares and CPI categories; earnings ratios condition on employment; spending uses Numerator receipts and permissioned-email data. The source also states that EHI indicators are not official estimates of the Federal Reserve System or FOMC.

## Next test

Align household fuel exposure, commuting and care trips, income, liquid assets, debt, actual prices, spending, and later trust or political judgment around a dated shock. Retain groups and households whose behavior did not change.

## Sources

- [December 2025 EHI record](../../records/us-nyfed-economic-heterogeneity-2025.json)
- [April 2026 EHI record](../../records/us-nyfed-economic-heterogeneity-april-2026.json)
- [New York Fed EHI release page](https://www.newyorkfed.org/research/economic-heterogeneity-indicators)
