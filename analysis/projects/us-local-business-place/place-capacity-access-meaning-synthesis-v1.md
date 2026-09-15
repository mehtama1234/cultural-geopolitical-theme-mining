# What “capacity” means in a place: from business formation to lived access

**Status:** reader-facing cross-source synthesis · **Checked:** 2026-09-15  
**Scope:** US counties, firms, services, mobility, care, households, and local public meaning

## The question

When a place is described as growing, declining, underserved, or full of new
businesses, what has actually changed for the people who live there?

The answer cannot be read from one number. A business application is not a
lasting employer. An establishment is not necessarily a usable service. A
shortage designation is not a resident-level measure of delay or distance. A
county health estimate is not a record of the same people becoming healthier.

The long-term program therefore follows a chain:

```text
money, credit, rent, labor, demand, and population change
  → applications, openings, closures, employer stock, and jobs
  → sector capacity and institutional designations
  → price, hours, staffing, mobility, eligibility, and neighboring options
  → attempted use, delay, substitution, unpaid care, or missed work
  → household security, local attachment, trust, voice, and public response
```

The current evidence reaches different points in this chain. The central
finding is not that one factor explains local life. It is that “capacity” has
several layers, and collapsing them produces confident but unsupported stories.

## The short answer

The evidence supports five durable conclusions:

1. **Interest in starting a business is not the same as durable local capacity.**
   Applications, employer openings, surviving establishments, jobs, and usable
   services are different stages.
2. **Visible supply is not practical access.** Establishment counts do not tell
   us whether a service is open when needed, affordable, staffed, accepting a
   person, reachable without a car, or replaceable by a nearby place.
3. **Care shortage is not one county condition.** HRSA designations can be
   geographic, population-based, facility-based, tract-based, or tied to a
   low-income or migrant/seasonal population. A county label can hide the
   actual object of designation.
4. **Local need can remain high alongside visible health-sector capacity.** In
   the matched CBP–HRSA–PLACES screen, lower health-establishment density is
   descriptively associated with higher modeled social-need measures, but
   routine-checkup estimates are nearly the same across the low- and
   high-capacity groups. This is not a causal access result.
5. **Place conditions do not translate into one automatic political response.**
   Trust, civic action, belonging, and immigration judgments vary with party,
   identity, composition, attribution, and local experience. They must be
   measured, not inferred from a county capacity score.

## 1. The first trap: counting intention as a local outcome

Census Business Formation Statistics (BFS) and Business Dynamics Statistics
(BDS) show the first stage boundary clearly. In the national 2023 comparison,
retail had the largest application count among the selected sectors, but much
lower BDS job intensity than health/social assistance, accommodation/food, or
construction. Administrative/support and waste management showed positive
establishment movement while its comparison had negative net-job intensity.

That does not mean applications are unimportant. They can indicate aspiration,
entry pressure, or local economic response. It means the program must ask a
more precise question:

> Did the activity become an employer, remain open, create jobs, provide a
> service, and become available to the residents who need it?

The current firm evidence measures applications, openings, closings, employer
stocks, and job flows in separate national, state, sector, and county layers.
It does not yet follow the same application into the same firm and then into a
customer or worker outcome. A rise in applications is therefore an early
signal, not a completed local transformation.

See the [BFS–BDS finding](findings/us-local-business-place-011.md) and the [firm and
place program record](README.md).

## 2. The second trap: treating presence as access

The county capacity layers add establishments and employment in retail, food,
health/social assistance, manufacturing, and other sectors. They are useful
because they show what is nominally present and how that stock differs by
sector, rurality, and county population.

They cannot answer several practical questions:

| A count can show | A count cannot show |
|---|---|
| an employer establishment exists in a county | whether it is open at the needed time |
| employment or establishment stock | whether staffing is adequate for demand |
| sector presence per resident | whether a person can pay, qualify, or be accepted |
| a formal shortage component overlaps a county | whether the resident lives inside it or can reach care |
| a place has nominal local options | whether a neighboring place is the real substitute |

The mobility layer makes this limitation concrete. NHTS shows different
vehicle and work-trip patterns in urban and rural settings, but it is not a
county-matched destination or service-use file. A county with establishments
may still offer a narrow option set to someone without a vehicle, with a rigid
work schedule, with a disability, or without enough money for fuel, fares, or
copays.

The relevant object is therefore an **option stack**:

```text
nominal local supply
  + mobility and neighboring supply
  + hours and staffing
  + price and eligibility
  + quality and continuity
  + time available to make the trip or wait
  → practical access, substitution, delay, or abandonment
```

The program's place screen is valuable as a targeting tool, but it is not a
resident access index.

## 3. The care result: visible health capacity and shortage can coexist

The matched county screen joins 2023 Census health/social-assistance
establishments, population estimates, current HRSA primary-care HPSA
components, and CDC PLACES modeled county estimates.

Among 3,072 matched counties, 2,785 had at least one represented primary-care
HPSA component. Counties in the lowest quartile of visible health-establishment
capacity had higher median modeled transportation, food, housing, utility,
mental-distress, and uninsured measures than counties in the highest quartile.
Yet routine-checkup medians were nearly unchanged: 75.8% in the low-capacity
group and 75.2% in the high-capacity group in the 2024 screen.

This combination matters. It blocks two opposite mistakes:

- **“More establishments solve access.”** The routine-care counterexample and
  the persistent social-need differences do not support that shortcut.
- **“A shortage designation proves the county has no care.”** HPSA components
  can cover a facility, a population, a tract, or part of a county, and people
  may use neighboring or alternative care.

The safe interpretation is narrower: nominal local health-sector capacity and
modeled social need are related place-level surfaces, but the mechanism between
them remains unmeasured.

## 4. Why the HPSA label must be opened up

The HRSA operational-field audit shows that a designation file contains useful
institutional information but is not a complete provider ledger. In the
current primary-care extract there are 20,905 designated rows across 2,888
counties. The score is populated across rows, but FTE and underserved-population
fields are missing for substantial portions of the file. Facility/site rows are
especially important: FTE is available for only 543 of 4,866 such rows in the
extract, and estimated underserved population is unavailable for that category.

The missingness changes the meaning of the statistic. A median FTE among rows
that report FTE is not the capacity of all designated facilities. Overlapping
components cannot be added into a national or county total without double
counting people, sites, or designated populations.

The component comparison adds another warning. Counties with population-based,
low-income, facility/site, geographic, tract, or migrant/seasonal components
have different PLACES medians, but the categories overlap and the PLACES
denominator is usually the county, not the designated population. A lower
county median for one category does not mean that the designated population
has better access.

The next care test must preserve the component object and add provider
locations, active hours, specialty, insurance acceptance, appointment wait,
travel time, and neighboring alternatives. Until then, HRSA is an
institutional designation surface—not a patient episode.

Read the [component finding](findings/us-local-business-place-009.md) and the
[operational-field audit](findings/us-local-business-place-010.md).

## 5. The newer PLACES release is a measurement check, not a clean trend

The 2024 and 2025 PLACES releases can be compared for common county FIPS, but
they use different BRFSS inputs, population and ACS inputs, and release
construction. In the common 2,885 counties, routine-checkup prevalence rises,
lack of insurance rises, mental distress is nearly flat, transportation
insecurity falls modestly, and food, housing, and utility measures move by
group rather than in one direction.

This is useful because it prevents the program from turning a release-to-release
difference into a single story of local improvement or decline. Same county
does not mean same respondents. Same measure name does not guarantee identical
model inputs or availability. The 2025 values are a newer estimate surface,
not a clean before/after measurement of the same residents.

Read the [PLACES vintage finding](findings/us-local-business-place-008.md).

## 6. Where culture, consumption, and politics enter

The measurable place layers stop before meaning. They do not tell us whether
residents describe a closure as corporate extraction, government failure,
unfair neglect, demographic change, ordinary market churn, or a chance to
rebuild. They do not tell us whether people organize, switch providers, leave,
stay, vote, or withdraw.

The existing CES place-context comparisons show why this final arrow must be
handled carefully. Trust and civic-action shares are not monotonic across
population-growth or capacity/mobility cells, and broad party identity can
explain more variation than the place cell itself. The local immigration survey
also shows that support for legal status can coexist with conditional views on
immigration levels, border policy, services, and fiscal responsibility.

The cultural and political question is therefore not simply:

> Does declining capacity cause distrust?

It is:

> Which material change did people encounter, how did they interpret its cause,
> what substitute or collective response was available, and what did an
> institution do afterward?

That requires a matched place/event design with direct measures of exposure,
attribution, belonging, action, and institutional response. The current
cross-source work identifies the missing links; it does not fill them by
assumption.

## The end-to-end research program from here

The next durable build is a common-geography, dated place panel. For selected
counties or tracts, it should align:

1. business applications, openings, closures, employer stock, jobs, payroll,
   ownership, and survival;
2. sector-specific services and provider locations, hours, staffing, prices,
   insurance or eligibility, and quality signals;
3. roads, transit, vehicle access, travel time, neighboring supply, and route
   reliability;
4. household use, delayed or foregone care, food and housing strain, unpaid
   care, missed work, and consumer substitution;
5. public attitudes, local narratives, attribution, trust, belonging, civic
   action, voting, complaints, organizing, and institutional response; and
6. a dated event such as a closure, opening, designation change, policy shift,
   disaster, financing shock, or service interruption.

The panel must contain counterexamples: places where nominal capacity is low
but neighboring access is strong; places where applications rise but durable
firms do not; places where health establishments are numerous but shortage
components remain; and places where material strain is high but trust or civic
action does not move in the expected direction.

## What this page is—and is not

This is a synthesis of separate official and survey-based evidence layers. It
is designed to make the long-term research program legible to a reader, not to
claim that the current files form one person-level panel. The results are
descriptive and bounded by their units, dates, geographies, denominators,
missingness, and release methods.

The program's central discipline is simple: every arrow from material change to
meaning or politics must either be measured in a compatible design or remain
explicitly open.

## Source trail

- [Census Business Formation Statistics](https://www.census.gov/econ/bfs/data.html) and [Business Dynamics Statistics](https://www.census.gov/programs-surveys/bds.html)
- [Census County Business Patterns](https://www.census.gov/programs-surveys/cbp.html)
- [HRSA shortage-area downloads](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas)
- [CDC PLACES](https://www.cdc.gov/places/)
- [National Household Travel Survey](https://nhts.ornl.gov/)
- [Project findings 007–011](findings/us-local-business-place-007.md)

**Evidence status:** cross-source synthesis of compared national and county
layers. It does not estimate a causal effect, resident-level access, firm
survival, health outcome, cultural change, trust change, or political response.
