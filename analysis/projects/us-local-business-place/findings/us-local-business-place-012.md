# Finding 012: Shortage designations and provider stock do not equal reachable local care

**Status:** provisional cross-source place-capacity synthesis · **Checked:** 2026-09-17

## The bounded finding

The local place evidence supports a narrower conclusion than “more providers
improve health” or “a shortage designation means no care is available.” Three
committed layers—CDC PLACES county estimates, HRSA HPSA designation components,
and HRSA operational fields—show that local care capacity has at least three
different objects:

```text
shortage designation and designated population
  -> reported FTE, shortage, and score fields
  -> modeled county social/health measures
  -> [open] reachable provider, appointment, price, travel, use, and recovery
```

The first two stages are observable in administrative and modeled place data.
The final stage remains open. A county median, designation, or reported FTE
cannot be treated as the care that a particular resident can actually obtain.

## What the local layers show

| Evidence layer | Unit and result | Interpretation boundary |
|---|---|---|
| PLACES 2024–2025 vintage comparison | 2,885 common county FIPS; routine-checkup median rose from 75.5% to 76.8%, while uninsured median rose from 9.2% to 10.1% | Different BRFSS, ACS, population, geography, and model inputs; not a resident-level change or capacity effect |
| HPSA component comparison | Among 2,685 counties with a PLACES record and HPSA component, low-income-code counties had higher modeled food, housing, utility, mental-distress, and uninsured medians than geographic-type counties; migrant/seasonal-code counties were a counterexample | Overlapping county categories and county-wide denominators do not identify the designated population's access or quality |
| HRSA operational-field audit | 20,905 designated primary-care rows across 2,888 counties; score populated for all rows, but FTE for 16,582 and estimated underserved population for 16,039 | Available fields are conditional and overlap; score/shortage are designation inputs, not appointments, active hours, acceptance, wait, or use |
| Facility/site components | FTE available for only 543 of 4,866 facility/site rows; estimated underserved population unavailable for all facility/site rows in the retained extract | A facility designation does not supply a complete site-capacity denominator |

The comparison is intentionally not a single capacity index. The county,
designation-component, row, facility, and modeled-health units answer different
questions and cannot be summed without double counting.

## The important counterexample

The migrant/seasonal population-code group has lower median modeled
transportation insecurity, food insecurity, utility shut-off threat, mental
distress, and lack of insurance than the low-income-code group, while routine
checkups are slightly higher. This does not show better access. It demonstrates
why a simple monotonic story fails: the groups differ in geography, population
composition, designation purpose, rurality, provider arrangements, and the
relationship between a designated population and a county-wide PLACES
denominator.

The vintage comparison supplies a second counterexample. High-capacity and
low-capacity county groups both show higher routine-checkup medians in the
newer release, while social-needs measures move in different directions. A
visible county-level capacity split therefore does not mechanically determine
every modeled health or social outcome.

## What this adds to the broad atlas

### Capacity is not the same as usable choice

The place program must distinguish:

- a shortage designation from the people and geography it covers;
- a designated population from the broader county denominator;
- FTE from active hours, new-patient availability, and continuity;
- an establishment or facility from a reachable appointment;
- routine use from unmet or delayed care; and
- nominal neighboring capacity from a viable alternative after travel, price,
  language, insurance, disability, or waiting costs.

This connects the place lane to household room, time as a hidden price, unequal
exposure, care, firm/provider power, and public-system legitimacy. It does not
yet establish a downstream health, work, trust, or political effect.

### Missingness is part of the institutional story

The absence of FTE and underserved-population fields for many facility/site
rows is not a harmless formatting detail. It means that the administrative
file is better at recording that a designation exists than at revealing the
operational capacity of each named site. Treating missing fields as zero would
turn an incomplete administrative view into a false shortage or capacity
estimate.

### Place exposure must be linked to a service episode

The next meaningful unit is not another county median. It is a dated resident,
household, provider, or service episode that records an attempted route,
travel/wait/price, insurance or eligibility, successful or failed use,
substitution, work/time displacement, and later recovery or trust. A closure,
opening, designation change, or staffing change can supply the event anchor;
the resident-level outcome still needs a compatible source.

## Coding rule

```text
HPSA designation        != resident-level shortage exposure
HPSA score/shortage     != appointment availability
FTE                     != active reachable service
county median           != same-resident outcome
establishment presence  != completed use
neighboring capacity    != practical alternative
```

Code this as **overlapping administrative designation and modeled county
comparison with substantive operational missingness; reachable service,
resident alternatives, household time/money response, trust, and political
action remain open**. Do not create a care-adequacy score from the three
layers.

## Next decisive test

Build one small matched-place episode ledger with:

```text
component boundary and designated population
  -> named active provider/site and staffing/hours
  -> insurance acceptance, new-patient status, price, wait, and travel
  -> resident attempt and completed/delayed/foregone use
  -> work, care, money, health, or household-time consequence
  -> substitute, recovery, complaint, trust, or exit
```

Retain a neighboring-capacity counterexample and a designated population that
does not share the county median. Keep PLACES vintages, HPSA components, FTE,
and service episodes separate until their denominators and timing are valid.
No bulk provider or patient file is needed to define this test.

## Sources and storage boundary

- [CDC PLACES vintage comparison finding](us-local-business-place-008.md)
- [HRSA HPSA component finding](us-local-business-place-009.md)
- [HRSA operational-field audit](us-local-business-place-010.md)
- [CDC PLACES](https://www.cdc.gov/places/)
- [HRSA shortage-area data](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas)

This synthesis uses already retained compact summaries and adds no new raw
provider, patient, or household data.
