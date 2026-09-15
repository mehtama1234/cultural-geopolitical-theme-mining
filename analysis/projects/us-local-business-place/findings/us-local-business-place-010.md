# Finding 010: HPSA designations carry operational fields, but those fields are unevenly populated and not service capacity

**Status:** provisional HRSA designation-field audit · **Checked:** 2026-09-15

## The bounded finding

The current HRSA primary-care HPSA file contains more than a binary shortage
flag. It carries designated population, estimated underserved population, FTE,
shortage, and score fields. But the fields are not uniformly available across
designation types, and none is an observed measure of appointments, active
hours, insurance acceptance, travel, quality, or household care use.

Among 20,905 designated primary-care rows covering 2,888 US counties in the
downloaded current file:

- HPSA score is populated for all rows, with a row-level median of 16;
- designated population is populated for 20,895 rows;
- FTE and shortage are populated for 16,582 rows;
- estimated underserved population is populated for 16,039 rows; and
- formal ratio is not populated in the downloaded file.

The main result is therefore an operational-data boundary:

> HRSA designation data can describe the institutional basis and scale of a
> shortage designation, but its fields cannot be treated as a complete provider
> capacity ledger or a county-level outcome.

## Type-conditioned operational fields

| Row category | Rows | Counties | Median FTE (available rows) | Median designated population | Median estimated underserved population | Median score | Median shortage |
|---|---:|---:|---:|---:|---:|---:|---:|
| All designated primary-care rows | 20,905 | 2,888 | 5.1802 (16,582 available) | 42,551 | 23,715 (16,039 available) | 16 | 7.14 (16,582 available) |
| Geographic HPSA type | 3,886 | 996 | 7.0 | 38,497 | 11,651 | 13 | 3.33 |
| Population HPSA type | 12,153 | 1,673 | 5.18 | 51,723 | 27,919 | 16 | 9.306 |
| Facility/site HPSA type | 4,866 | 1,884 | 0.375 (543 available) | 24,165.5 | unavailable | 16 | 0.99 (543 available) |
| Census-tract component | 12,238 | 243 | 6.592 | 63,603 | 35,170 | 16 | 11.133 |
| County/subdivision component | 3,801 | 2,371 | 1.034 | 10,312 | 5,161 | 14 | 1.63 |
| Low-income population code | 9,934 | 1,553 | 4.369 | 42,551 | 23,916 | 16 | 7.97 |
| Migrant/seasonal population code | 2,321 | 124 | 9.992 | 95,378 | 65,139 | 16 | 21.717 |

The rows and counties overlap. The table is not a ranking of shortage severity,
and national sums would be misleading because the same county, population, or
facility can appear in multiple designation components.

## The missingness is substantive

The facility/site category illustrates why field availability matters. FTE is
available for only 543 of 4,866 facility/site rows, and estimated underserved
population is unavailable for all 4,866 rows in this extract. A low median FTE
among the available rows cannot be interpreted as low facility capacity for the
whole category; it is a conditional statistic on a selected subset of rows.

Likewise, the overall FTE median is calculated over rows that report FTE, not
over all designated components. It should not be multiplied by component count
to estimate national primary-care staffing. The same caution applies to
designated and underserved population fields because components overlap.

This is a useful correction to a common analytical shortcut: a dataset may
contain a variable named “FTE” or “underserved population” without providing a
complete denominator for every institutional object in the file.

## What the score and shortage fields do not mean

The score is populated across rows and can help describe designation context,
but it is not an outcome score for residents. The shortage field is available
for many rows and varies substantially by category; it still does not measure
the number of clinicians accepting new patients, appointment delay, distance,
continuity, price, or quality.

The migrant/seasonal category is a useful counterexample. It has a higher
median FTE and shortage field than the low-income category, but that does not
mean its designated population receives better or worse care. Seasonal and
migrant service arrangements may require a different interpretation of
provider timing, geography, and population exposure than a year-round county
average.

## How this connects to the PLACES outcome screen

The component-level PLACES finding showed different modeled county social-need
medians by HPSA type and population code. This operational audit explains why
those patterns cannot yet be converted into a capacity effect:

```text
HPSA designation object and score
  -> partially populated FTE / underserved / shortage fields
  -> unknown active provider hours, reach, acceptance, and wait
  -> modeled county social-need measure
  -> unknown patient use, household time, health, trust, or political response
```

The first arrow is directly recorded for the designated row. The second and
third arrows require new data. A county-level PLACES median is not the outcome
of the designated component, and a designation field is not a patient episode.

## Counterexamples retained

- A high score does not prove long wait, and a low shortage value does not prove
  adequate care.
- A facility/site designation can have a population field but no usable FTE or
  underserved-population field in the current extract.
- A county/subdivision component can have low row-level FTE while neighboring
  or overlapping facilities provide care; row-level values are not county totals.
- Migrant/seasonal components have high designated and underserved population
  medians but do not map cleanly onto county-wide PLACES denominators.
- A current designation file is not a frozen historical panel; update dates and
  component status must be time-aligned before interpreting change.

## Next decisive test

The next place acquisition should join HRSA component identifiers to provider
locations and operational records:

1. component geometry and designated population boundary;
2. provider name/type, active status, FTE definition, hours, and specialty;
3. insurance acceptance, new-patient status, appointment wait, and price;
4. travel time and neighboring-county alternatives; and
5. patient-level utilization or a compatible household event after a dated
   closure, opening, designation change, or service interruption.

Until then, keep HPSA score, FTE, underserved population, PLACES social need,
and CBP establishments as separate evidence surfaces. Do not call any one of
them care adequacy, health impact, trust change, or political response.

## Reproduction and sources

- [HRSA primary-care HPSA component CSV](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv)
- [HRSA shortage-area definitions and downloads](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas)
- [Operational-field reproduction script](../../../../scripts/analyze_hpsa_operational_fields.py)
- [Committed operational summary](../data/hpsa-operational-fields-summary.json)
- [Machine-readable HPSA operational-fields record](../../../records/us-hrsa-hpsa-operational-fields-2026.json)
- [HPSA component/PLACES finding](us-local-business-place-009.md)

**Evidence status:** official current HRSA designation-field audit with row-level
missingness and overlapping category comparisons. No claim of provider adequacy,
patient access, causal health effect, household burden, trust, or political
action.
