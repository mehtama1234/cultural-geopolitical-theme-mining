# Ohio HPSA component and mobility surface v1

**Checked:** 2026-09-18  
**Question:** What does the retained primary-care shortage file actually add to
the Ohio mobility/outcome panel?

## Result in plain words

It adds an institutional shortage-designation surface, not a county provider
inventory. In the current Ohio file, 81 of 88 counties contain at least one
designated primary-care HPSA component. Those 81 counties contain 1,139
designated rows, including 989 census-tract rows, 58 single-county rows, and
92 rows whose component type is unknown. Reported FTE is present on 1,071 rows,
but the components overlap and cannot be summed into county capacity.

The mobility split makes the object problem visible:

| Mobility group | Counties | Counties with designated component | Designated rows | Census-tract rows | Single-county rows | Median reported FTE per row |
|---|---:|---:|---:|---:|---:|---:|
| Low zero-vehicle share | 44 | 39 | 197 | 144 | 24 | 1.7500 |
| High zero-vehicle share | 44 | 42 | 942 | 845 | 34 | 8.7780 |

The much larger high-zero-vehicle row count is not evidence that those
counties have 4.8 times the provider shortage. It is largely a difference in
component granularity and designation objects: many tract-level rows can sit
inside the same county, while a single-county designation has a different
meaning.

## What this adds to the atlas

```text
mobility context + modeled burden
  -> formal shortage component / institutional classification
  -> [open] provider reach, appointment availability, travel, wait, and use
  -> [open] household consequence, trust, action, recovery, or exit
```

This is a useful institutional-response and measurement layer. It prevents the
atlas from converting “HPSA county” into a universal resident-level shortage
claim and shows why component type and designated population must travel with
the label.

## Source and method

- [HRSA primary-care HPSA CSV](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv), local artifact SHA-256: `9601da6ee010869ac090464212537786cd139ca31793c2cc42655a53316684cf`, file create date 2026-09-14.
- [ACS 2023 B08201 vehicle table](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08201.dat), SHA-256: `71e502d0d2b456cb49af97cf9ff2d43fcbd9a7f9c2ee737fdb41721f9ad87a8b`.
- [ACS 2023 B08303 travel-time table](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b08303.dat), SHA-256: `8dc1b696d93c28a684784281211cf4e5011f01d9ca84694df2d7fb3b4ad84f51`.
- Reproduction: `python3 scripts/analyze_bds_ohio_hrsa_provider_surface.py --vehicle /path/to/acsdt5y2023-b08201.dat --commute /path/to/acsdt5y2023-b08303.dat --hrsa /path/to/BCD_HPSA_FCT_DET_PC.csv --output /path/to/output.json`.
- Machine-readable result: [`data/bds-ohio-hrsa-provider-surface-2026-09-18.json`](data/bds-ohio-hrsa-provider-surface-2026-09-18.json).

The frame is all 88 Ohio counties with ACS vehicle and commute fields. The
zero-vehicle split is the Ohio median (6.241%). Only current `Designated`
primary-care rows are counted. The HPSA file is current-vintage administrative
data, not a 2023 provider-use panel.

## Limits and next test

HPSA components may be geographic, population-based, tract-based,
facility-based, or county-based. Reported FTE is incomplete and does not
establish active appointment supply, insurance acceptance, wait time, quality,
travel, or successful use. The next decisive care extension is a provider/site
and travel-time surface with a clearly defined population, or a dated care-use
record; do not rank counties by raw HPSA row count or sum overlapping FTE.
