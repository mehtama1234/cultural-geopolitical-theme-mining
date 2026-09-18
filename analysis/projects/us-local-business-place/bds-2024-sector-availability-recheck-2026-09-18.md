# BDS 2024 sector release-availability recheck

**Checked:** 2026-09-18  
**Question:** Can the existing 2023 national BDS sector baseline be promoted to a 2023→2024 sector-dynamics comparison?

## Result

Not yet. The official Census BDS time-series index currently lists directories
for 2018 through 2023 and does not list a 2024 directory. The direct 2024
directory and the expected national sector CSV both returned HTTP 404:

- [Official BDS time-series index](https://www2.census.gov/programs-surveys/bds/tables/time-series/)
- [Probed 2024 directory](https://www2.census.gov/programs-surveys/bds/tables/time-series/2024/)
- [Existing 2023 sector CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_sec.csv)

The recheck is stored in
`data/bds-2024-sector-availability-recheck-2026-09-18.json`.

## Interpretation boundary

This is a source-release/path boundary, not a finding that 2024 business
dynamics were absent, unchanged, or unavailable through every Census route.
It does not justify computing a 2023→2024 national comparison from another
vintage or silently treating the 2023 baseline as current.

The existing 2023 national sector layer remains useful as a realized entry,
exit, job-creation, and job-destruction baseline, but it still does not connect
an application to a particular opening, closing, household burden, service
replacement, political response, or exit.

## Consequence for the broad atlas

The application→realized-firm arrow remains open at the national time-series
level. The next executable BDS route is a state/county-sector pass using an
official available table, retaining geography, sector, year, openings,
closings, jobs created/destroyed, and denominator definitions. A valid pass
must retain a counterexample such as high application activity without
corresponding employer-stage growth, or stable stock with high turnover.

If the geographic route cannot be made comparable, defer this lane until a
2024 national file is officially exposed and rotate to a dated institutional
event ledger rather than treating release absence as substantive evidence.
