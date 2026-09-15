# Finding 009: HPSA component type changes what a county shortage label can mean

**Status:** provisional component-level place diagnostic · **Checked:** 2026-09-15

## The bounded finding

The county-level HPSA flag was too coarse for the place program. The current
HRSA primary-care file contains different kinds of designations: geographic,
population-based, facility/site-based, census-tract, county/subdivision, and
population-code categories such as low-income or migrant/seasonal. A county can
appear in several categories at once.

The new component-level screen conditions 2025 CDC PLACES county estimates on
those categories. Among 2,685 counties with both a selected PLACES record and
at least one designated primary-care HPSA row:

- counties with a population-based HPSA type have higher median modeled food,
  housing, utility, mental-distress, and uninsured measures than counties with
  a geographic HPSA type;
- counties with low-income population codes show still higher median modeled
  food insecurity, housing insecurity, utility shut-off threat, mental distress,
  and lack of insurance;
- facility/site-type counties sit between some of the population and geographic
  patterns; and
- migrant/seasonal population-code counties have lower medians on several
  selected measures, a counterexample that may reflect composition, geography,
  selection, or the narrow designated population rather than better access.

The substantive result is a classification warning:

> “HPSA county” is not one exposure. The component and population being
> designated changes the interpretation, and none of the categories is a
> person-level measure of reachable, affordable, or effective care.

## Component-conditioned PLACES measures

| HRSA category present in county | Counties | Transportation | Food insecurity | Housing insecurity | Utility shut-off threat | Mental distress | Uninsured 18–64 | Routine checkup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Geographic HPSA type | 921 | 8.3% | 15.0% | 11.9% | 8.1% | 17.7% | 10.5% | 75.5% |
| Population HPSA type | 1,566 | 9.0% | 16.6% | 13.1% | 9.3% | 18.4% | 10.6% | 77.3% |
| Facility/site HPSA type | 1,767 | 8.7% | 15.8% | 12.5% | 8.7% | 17.9% | 10.2% | 76.7% |
| Census-tract component | 233 | 8.0% | 14.55% | 12.0% | 7.6% | 17.0% | 9.4% | 76.1% |
| County/subdivision component | 2,201 | 8.9% | 16.4% | 12.9% | 9.1% | 18.3% | 10.7% | 76.8% |
| Low-income population code | 1,446 | 9.2% | 17.0% | 13.25% | 9.4% | 18.5% | 10.85% | 77.2% |
| Migrant/seasonal population code | 124 | 8.1% | 14.7% | 12.4% | 7.8% | 17.25% | 8.25% | 77.65% |

These are unweighted county medians, and the rows overlap. A county with a
low-income population code may also have a facility or geographic designation;
the table is not a mutually exclusive typology or a ranking of HPSA severity.

## What the component distinction adds

The earlier CBP–HRSA bridge established that employer health-sector presence
does not resolve primary-care adequacy. The first PLACES screen added modeled
social need but still used a binary “any HPSA component” flag. This pass shows
why the next data layer must preserve the object of designation:

| HPSA object | What a county presence can indicate | What remains unknown |
|---|---|---|
| Geographic | A geographic area has a designated shortage context | Whether the respondent lives in the component, can travel to care, or faces a shortage at the time of the PLACES estimate |
| Population | A defined population is designated within a place | Whether the modeled county median represents that population or the broader county |
| Facility/site | A named or qualifying care site is part of the designation | Whether it is open, accepting patients, affordable, staffed, or reachable |
| Census tract/subdivision | The shortage is spatially narrower than a county | Whether neighboring capacity substitutes for the affected tract or subdivision |
| Low-income / migrant-seasonal code | A particular population criterion is part of the designation | Whether the county-level social-need estimate measures the designated population |

The mismatch between the designated object and the PLACES denominator is not a
technical footnote. It determines whether the comparison speaks about a local
population, a facility catchment, a geography, or a county average.

## Counterexample: lower modeled need does not resolve the access question

The migrant/seasonal population-code group has lower median modeled
transportation insecurity, food insecurity, utility threat, and lack of health
insurance than the low-income-code group, while routine checkups are slightly
higher. This should not be narrated as evidence that migrant/seasonal HPSA
populations have better care.

Possible explanations include different states and rurality, seasonal
population composition, county-level rather than population-specific PLACES
denominators, different provider arrangements, or the fact that only 124 common
counties carry the code. The counterexample is useful precisely because it
blocks a simple “shortage designation → uniformly worse county outcome” story.

## Why this is still not a lived-access result

The HRSA file records designation components and codes. PLACES supplies modeled
county estimates, not patient records. The join does not reveal:

- whether someone attempted to obtain care;
- travel distance, transportation reliability, or appointment wait;
- insurance acceptance, price, clinician workload, or quality;
- delayed or foregone care;
- unpaid family care or work-time displacement; or
- later trust, local belonging, public demand, or political action.

It also does not establish that HPSA designation causes the PLACES outcome.
Designation may respond to the same underlying need, and the data vintages do
not provide a clean policy experiment.

## Next decisive test

The next place pass should move from designation categories to component
boundaries and service events:

1. retain component polygons or tract/subdivision identifiers;
2. link designated and underserved population fields without summing overlapping
   components into a false county total;
3. add provider locations, specialty, hours, staffing, insurance acceptance,
   appointment availability, and neighboring-county alternatives;
4. measure travel and actual care use with a compatible person, household, or
   utilization source; and
5. attach a dated opening, closure, designation change, or service disruption
   to delayed care, work/time, health, or household recovery.

Only then can the program test whether a shortage designation corresponds to
usable access and downstream social reproduction. Political meaning still
requires separately measured attribution, trust, belonging, and action.

## Reproduction and sources

- [HRSA shortage-area downloads](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas)
- [HRSA primary-care HPSA component CSV](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv)
- [CDC PLACES 2025 county release](https://data.cdc.gov/d/swc5-untb)
- [HRSA/PLACES component reproduction script](../../../../scripts/analyze_hpsa_component_places.py)
- [Committed component summary](../data/hpsa-component-places-summary.json)
- [Machine-readable HPSA component record](../../../records/us-hrsa-hpsa-component-places-2025.json)
- [Earlier capacity/outcome diagnostic](us-local-business-place-007.md)

**Evidence status:** compared ecological diagnostic using HRSA designation
components and CDC modeled county estimates. No claim of resident-level
shortage, care adequacy, causal effect, household outcome, trust, or political
response.
