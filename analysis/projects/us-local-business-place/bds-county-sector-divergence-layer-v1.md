# BDS county-sector divergence layer v1

**Checked:** 2026-09-18  
**Question:** Does a county's aggregate employer turnover describe what happens
in the everyday sectors through which residents actually experience place?

## Result in plain words

No. The 2023 BDS county–sector table contains 3,194 county rows for each of
19 sectors. In a four-sector screen, county-sector dynamics diverge sharply:

| Sector | Comparable entry/exit rows | Median entry rate | Median exit rate | Median net job-creation rate | Negative net-job rows |
|---|---:|---:|---:|---:|---:|
| Retail trade | 2,181 | 7.407% | 6.667% | 0.917% | 1,245 |
| Transportation and warehousing | 1,539 | 13.018% | 13.333% | 0.253% | 1,387 |
| Health care and social assistance | 1,950 | 9.310% | 6.982% | 2.471% | 1,051 |
| Accommodation and food services | 2,067 | 10.952% | 9.195% | 3.575% | 954 |

The same county can therefore show positive health or food job growth while
transport contracts. Aggregate county turnover is not a substitute for the
sector through which access, work, travel, care, or daily dependence is
experienced.

## Source and storage boundary

- [Census BDS program](https://www.census.gov/programs-surveys/bds.html)
- [2023 BDS table directory](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/)
- [2023 county–sector CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv)
- Official file size at recheck: 274,770,797 bytes; last modified 2025-09-25.
- Retrieval used a transient 12,000,000-byte HTTP suffix, SHA-256
  `988039900c4244fba737cbe2bd37c37d2bf42f81d88121207ed9d842cb5a7d7b`.

The suffix contained every 2023 row because the file is ordered by year and
the 2023 block is at the end. The raw table and suffix are not retained in the
repository. The compact derived summary is stored in
`data/bds-county-sector-divergence-2026-09-18.json`.

## Same-county counterexample

State/county FIPS `39/089`, restricted to rows with at least 100 reported
establishments in each selected sector, shows:

| Sector | Net job-creation rate | Establishments |
|---|---:|---:|
| Retail | -2.997% | 406 |
| Transportation | 96.707% | 104 |
| Health care/social assistance | 3.466% | 291 |
| Accommodation/food | 3.572% | 325 |

This is not a causal case study and the transport rate may reflect a small
denominator or large establishment changes. It is still a useful guardrail:
“the county economy grew” does not tell us which service or work system grew,
contracted, or became more volatile.

## What this adds to the atlas

```text
county condition/application signal
  -> sector-specific establishment openings/closings and job flows
  -> [open] service access, prices, work quality, household time, trust, and action
```

This advances the local-business lane from aggregate county realization to a
sector-specific realization stage. It does not link a BFS application to an
opening, identify firms, measure survival, or establish local service use.

## Next test

Select a small pre-specified geography/sector panel and join this layer to
measured service access, prices, wages or hours, ownership, or civic response.
Keep a matched counterexample where the aggregate county signal and the
sector-specific signal point in different directions. Do not infer household
benefit from positive net jobs or treat disclosure marks as zeros.
