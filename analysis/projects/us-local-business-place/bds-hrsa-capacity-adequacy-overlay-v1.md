# BDS–HRSA capacity versus adequacy overlay v1

**Checked:** 2026-09-18  
**Question:** Does realized county-sector employer growth imply adequate
primary-care capacity?

## Result in plain words

No. A 2023 BDS county-sector flow can be overlaid with the current HRSA
primary-care designation surface, but the result is not a simple shortage or
growth gradient. In the local HRSA artifact checked on 2026-09-14, 2,918 US
county FIPS were represented by at least one currently designated primary-care
HPSA component. Among BDS rows with a reported net-job rate, the selected
sector medians were:

| Sector | HPSA-represented counties: median net-job rate | Other counties: median net-job rate | HPSA negative-net share | Other negative-net share |
|---|---:|---:|---:|---:|
| Retail trade | 0.936% | 0.505% | 39.17% | 40.96% |
| Transportation and warehousing | 0.244% | 0.433% | 46.05% | 45.59% |
| Health care and social assistance | 2.366% | 3.678% | 33.79% | 33.33% |
| Accommodation and food services | 3.521% | 4.470% | 31.69% | 25.00% |

The differences are descriptive and cross-vintage. They do not establish that
HPSA status caused business outcomes, or that a positive health-sector flow
resolved primary-care access.

## Sources and method

- [HRSA shortage-area downloads](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas)
- [HRSA primary-care HPSA CSV](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv), local artifact SHA-256: `721ede7da4d4ea579d7fd54bfe705ebde3a2adfa988276e03fc2abf5ef3e66bd`
- [2023 BDS county–sector CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv)
- BDS retrieval: transient 12 MB suffix containing all 60,686 2023 rows; suffix SHA-256: `988039900c4244fba737cbe2bd37c37d2bf42f81d88121207ed9d842cb5a7d7b`.

An HPSA-represented county means that at least one designated HPSA component
has that county FIPS. HPSA components can be geographic, population-based,
facility-based, or partial-county; the label does not assign the same shortage
to every resident. “Other counties” are counties without a matching designated
component in this particular current file, not counties proven to have
adequate care.

The derived comparison is stored in
`data/bds-hrsa-capacity-adequacy-overlay-2026-09-18.json`.

## What this adds to the atlas

```text
county-sector employer flow
  + institutional primary-care shortage designation
  -> [open] actual provider access, travel, appointment capacity, insurance, use, and outcomes
```

This is a direct counterexample to treating establishment presence or job
growth as service adequacy. Health-sector flows are an employer measure;
HPSA is an institutional shortage designation; neither is appointment use or
patient recovery.

## Boundaries and next test

The BDS year is 2023 while the HRSA file is a current designation surface
updated in 2026. The join does not measure HPSA population coverage, provider
hours, appointment waits, travel, accepted insurance, prices, quality, care
use, unmet need, household time, trust, or political response. The next test
should use component type/population, provider counts, travel or wait measures,
and a dated care or household outcome rather than interpreting this overlay as
a causal or county-wide shortage estimate.
