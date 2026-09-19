# BDS–ACS Ohio mobility and sector-flow panel v1

**Checked:** 2026-09-18  
**Question:** Within one state and one year, do counties with different vehicle
constraints show different sector turnover profiles?

## Result in plain words

In this bounded Ohio panel, yes—but the pattern is not a simple access story.
Among 50 counties with comparable 2023 BDS rates in all four selected sectors,
counties above the within-panel median share of zero-vehicle households had
lower median health/social-assistance net-job growth (1.001% versus 3.466%) and
lower accommodation/food growth (4.296% versus 5.535%). Negative health rows
were also much more common (11 of 25 versus 1 of 25). Retail was a counterweight:
its median net-job rate was slightly higher in the high-zero-vehicle group
(0.463% versus 0.166%).

| Within-Ohio mobility group | Counties | Median zero-vehicle households | Median 30+ minute commute | Health median net-job rate | Food median net-job rate | Health negative rows |
|---|---:|---:|---:|---:|---:|---:|
| Low zero-vehicle share | 25 | 4.557% | 30.750% | 3.466% | 5.535% | 1/25 |
| High zero-vehicle share | 25 | 7.429% | 27.412% | 1.001% | 4.296% | 11/25 |

The commute result is itself a warning: the high-zero-vehicle counties had a
lower median long-commute share. That could reflect denser settlement,
different work geography, transit, nonwork travel, or other composition. A
vehicle constraint measure is not a complete measure of practical mobility.

## Same-county counterexample

The retained county `39089` is a useful guardrail against a smooth story. It
has a 5.338% zero-vehicle-household share, a 41.540% long-commute share, and
the following sector net-job rates:

| Retail | Transportation | Health/social assistance | Accommodation/food |
|---:|---:|---:|---:|
| -2.997% | 96.707% | 3.466% | 3.572% |

The transport figure may reflect a small or volatile denominator. The point is
not to explain that county from these aggregates; it is to preserve the fact
that one county can contract in retail while transport, health, and food move
in different directions.

## Source and method

- [Census 2023 county–sector BDS table](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv), official file size 274,770,797 bytes and last modified 2025-09-25.
- [ACS 2023 B08201 vehicle table](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08201.dat), SHA-256: `71e502d0d2b456cb49af97cf9ff2d43fcbd9a7f9c2ee737fdb41721f9ad87a8b`.
- [ACS 2023 B08303 travel-time table](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08303.dat), SHA-256: `8dc1b696d93c28a684784281211cf4e5011f01d9ca84694df2d7fb3b4ad84f51`.
- [USDA 2023 Rural-Urban Continuum Codes](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes), SHA-256: `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7`.
- BDS used the retained transient 12,000,000-byte suffix, SHA-256: `988039900c4244fba737cbe2bd37c37d2bf42f81d88121207ed9d842cb5a7d7b`.
- Reproduction: `python3 scripts/analyze_bds_ohio_mobility_panel.py --bds-suffix /path/to/bds-suffix.csv --vehicle /path/to/acsdt5y2023-b08201.dat --commute /path/to/acsdt5y2023-b08303.dat --rucc /path/to/rucc2023.csv --output /path/to/output.json`.
- Machine-readable result: [`data/bds-ohio-mobility-panel-2026-09-18.json`](data/bds-ohio-mobility-panel-2026-09-18.json).

The geography was pre-specified as Ohio because the preceding BDS divergence
layer retained an Ohio county counterexample. The four sectors were retained
from that layer. Counties were split at the panel median zero-vehicle share
(5.750%). Rows with BDS disclosure values were excluded, not converted to zero.

## What this adds to the atlas

```text
sector-specific employer flow + county mobility constraint context
  -> [open] reachable alternatives, service use, price, and time cost
  -> [open] household/work adaptation, trust, action, and exit
```

This is stronger than a national cross-source juxtaposition because the BDS
and ACS observations share state, county, and year. It remains an ecological
comparison: it does not observe the same resident, destination, trip, service
attempt, or causal pathway.

## Limits and next test

The panel is 2023 and descriptive. Zero-vehicle households, commute time, and
sector job flow do not establish provider reach, nonwork travel, prices,
appointment use, worker quality, or household burden. The next decisive step
is not another split; it is a small service-specific outcome surface—such as
primary-care travel/provider availability or a dated local closure/use record—
with neighboring alternatives and a compatible denominator.
