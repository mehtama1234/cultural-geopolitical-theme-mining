# BDS–ACS–PLACES Ohio outcome panel v1

**Checked:** 2026-09-18  
**Question:** After adding mobility context to county-sector flow, do modeled
county health and social-need measures move in the same direction?

## Result in plain words

The mobility split is more visible in modeled social-need measures than in the
routine-checkup measure. Across all 88 Ohio counties, high-zero-vehicle
counties had nearly the same median modeled routine-checkup estimate as
low-zero-vehicle counties (76.95% versus 77.05%), but higher medians for
transportation insecurity (8.80% versus 7.45%), food insecurity (15.95% versus
13.20%), frequent mental distress (20.25% versus 18.85%), and lack of health
insurance (9.15% versus 8.35%).

| Mobility context | Counties | Routine checkup | Transportation insecurity | Food insecurity | Mental distress | Lack of insurance |
|---|---:|---:|---:|---:|---:|---:|
| Low zero-vehicle share | 44 | 77.05% | 7.45% | 13.20% | 18.85% | 8.35% |
| High zero-vehicle share | 44 | 76.95% | 8.80% | 15.95% | 20.25% | 9.15% |

This is a useful counterexample to a simple “more mobility constraint means
less routine care” interpretation: the routine-checkup medians are nearly
unchanged even while several burden measures differ.

## Adding health-sector flow

The high-zero-vehicle/negative-health-flow cell contained 20 counties and had
modeled medians of 16.25% food insecurity, 20.55% frequent mental distress,
8.85% transportation insecurity, and 76.75% routine checkups. Its
high-zero-vehicle/nonnegative-health-flow counterpart contained 24 counties
and had 15.75%, 19.95%, 8.80%, and 77.10%, respectively.

That contrast is modest relative to the mobility split and should not be read
as a health-employer-flow effect. It instead shows why employer turnover alone
does not identify a resident outcome: mobility context and modeled need carry
more visible separation here than the sign of health-sector net job flow.

## Source and method

- [Census 2023 county–sector BDS table](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv), read through the retained transient 12 MB suffix.
- [ACS 2023 B08201 vehicle table](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08201.dat), SHA-256: `71e502d0d2b456cb49af97cf9ff2d43fcbd9a7f9c2ee737fdb41721f9ad87a8b`.
- [ACS 2023 B08303 travel-time table](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08303.dat), SHA-256: `8dc1b696d93c28a684784281211cf4e5011f01d9ca84694df2d7fb3b4ad84f51`.
- [CDC PLACES 2025 county release](https://data.cdc.gov/d/swc5-untb), data year 2023, retained file SHA-256: `0f093ce4a185a46eaaa53a09d556cbd37dee7d6d8059666c1a08d03db754d73f`.
- BDS suffix SHA-256: `988039900c4244fba737cbe2bd37c37d2bf42f81d88121207ed9d842cb5a7d7b`.
- Reproduction: `python3 scripts/analyze_bds_ohio_places_outcome_panel.py --bds-suffix /path/to/bds-suffix.csv --vehicle /path/to/acsdt5y2023-b08201.dat --commute /path/to/acsdt5y2023-b08303.dat --places /path/to/cdc-places-county-2025.csv --output /path/to/output.json`.
- Machine-readable result: [`data/bds-ohio-places-outcome-panel-2026-09-18.json`](data/bds-ohio-places-outcome-panel-2026-09-18.json).

The panel uses all 88 Ohio counties with a complete four-sector BDS profile,
ACS mobility fields, and age-adjusted PLACES values for all five selected
measures. The zero-vehicle split is the Ohio median (6.241%). PLACES measures
are age-adjusted prevalence estimates; rows with unavailable or disclosure-
marked BDS values are excluded.

## What this adds to the atlas

```text
sector flow + vehicle/commute context
  -> modeled social-need and routine-care context
  -> [open] provider reach, attempted/completed use, price, time, and recovery
  -> [open] trust, action, persistence, and exit
```

This is a same-state, same-year county comparison, stronger than a national
juxtaposition but still ecological. It does not follow residents, identify a
provider, measure a completed visit, or establish causation.

## Limits and next test

PLACES is modeled county-level prevalence, not an observed patient or visit
record. ACS vehicle and commute measures do not capture nonwork travel,
transit reliability, destination, fare, appointment wait, or telehealth. BDS
net job flow does not measure provider capacity or service continuity. The next
decisive extension is a provider/travel/use surface or a dated local closure
and care-use record with a compatible denominator—not another county median.
