# Finding 007: County service capacity and lived social need move together descriptively, but capacity is not access

**Status:** provisional place/outcome diagnostic · **Checked:** 2026-09-15

## The bounded finding

The first matched county screen adds a downstream outcome surface to the local
capacity program. It joins:

- 2023 Census County Business Patterns health/social-assistance establishments
  and employment;
- current HRSA primary-care Health Professional Shortage Area component
  presence;
- 2023 county population estimates; and
- CDC PLACES county-level modeled estimates in the 2024 release, whose selected
  measures are based primarily on 2022 BRFSS data.

Across 3,072 matched counties, 2,785 contain at least one designated primary-care
HPSA component. Counties in the lowest quartile of visible health/social-
assistance establishment capacity have higher median modeled transportation,
food, housing, utility, mental-distress, and uninsured measures than counties
in the highest capacity quartile. This is a useful place-level alignment, not a
causal result:

> Nominal local health-sector capacity and lived social need are related
> surfaces, but establishment presence does not establish provider adequacy,
> usable access, or that capacity caused the observed county outcome.

## What the matched screen shows

| County grouping | Counties | Health establishments / 10,000 | Transportation insecurity | Food insecurity | Housing insecurity | Utility shut-off threat | Frequent mental distress | Uninsured adults 18–64 | Routine checkup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Lowest quartile of health-establishment capacity | 768 | 13.854 | 10.2% | 18.1% | 14.7% | 10.0% | 18.7% | 11.0% | 75.8% |
| Highest quartile of health-establishment capacity | 768 | 34.817 | 8.1% | 12.4% | 11.3% | 7.5% | 16.9% | 7.9% | 75.2% |

These are unweighted medians of county estimates. The measures are not one
index: transportation, food, housing, utility, mental distress, insurance, and
routine care have different definitions and populations. The routine-checkup
median is nearly unchanged, which is an important counterexample to a simple
“more capacity means more care” story. A county may have more establishments
and still face price, appointment, transportation, insurance, quality, or
work-schedule barriers.

## HPSA context changes the interpretation

The HPSA split produces a similar warning. Counties with a designated primary-
care HPSA component have a median of 23.119 health establishments per 10,000
residents; counties without a represented component have 23.436. Their modeled
median social-need measures are different:

| HPSA component status | Counties | Transportation insecurity | Food insecurity | Housing insecurity | Utility shut-off threat | Frequent mental distress | Uninsured adults 18–64 | Routine checkup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Designated component present | 2,785 | 9.0% | 15.1% | 12.8% | 8.8% | 18.1% | 9.2% | 75.7% |
| No represented component | 287 | 7.0% | 10.85% | 10.0% | 6.9% | 16.4% | 7.1% | 75.7% |

The HPSA result should not be read as a county-wide shortage estimate. HRSA
components can be geographic, population-based, facility-based, or partial-
county designations. The fact that 2,785 counties appear in the component file
means that a shortage-designation surface overlaps most counties in this
screen; it does not mean every resident lacks primary care.

The similar establishment counts in the earlier CBP–HRSA bridge and the
different PLACES social-need medians show why the program needs both capacity
and outcome measures. Establishments are a stock. HPSA is an institutional
designation. PLACES is a modeled area estimate. None is a patient episode.

## Why the low/high-capacity contrast is not a causal effect

Several explanations remain compatible with the observed ordering:

- Counties with greater need may attract or retain more health/social-
  assistance establishments without eliminating unmet need.
- High-capacity counties may include large hospitals or administrative
  establishments that do not provide accessible primary care.
- Low-capacity counties may use neighboring-county providers, telehealth,
  mobile clinics, family support, or delayed care; the screen cannot observe
  those substitutes.
- Population age, income, race, disability, rurality, insurance, housing,
  transportation, and migration composition can affect both capacity and the
  modeled outcomes.
- PLACES estimates are modeled small-area measures with their own uncertainty;
  the county medians do not provide a person-level or causal standard error for
  the capacity contrast.

The contrast is therefore best treated as a targeting and acquisition signal:
the places that look different in nominal capacity also look different in
social need, so the next study must measure the actual mechanism instead of
assuming it.

## The place-level end-to-end chain now available

```text
population change / local demand / firm and provider stock
  -> HPSA designation, insurance, transport, price, and appointment constraints
  -> actual travel, waiting, delayed care, unpaid care, or substitution
  -> health, work, food, housing, and household-time consequences
  -> trust, local belonging, public demand, provider response, or political action
```

This pass improves the first and second stages and adds a modeled downstream
surface. It does not observe the middle lived-access event or the final meaning
and political stages.

## Counterexamples to preserve

- High visible establishment capacity can coexist with a designated HPSA
  component and higher need.
- Routine-checkup rates are nearly identical across the low/high capacity
  quartiles, despite large differences in social-need measures.
- A designated HPSA component may cover only part of a county or a specific
  population, so a county label is not a resident-level shortage claim.
- A low-capacity county can have access through neighboring places or public
  provision; nominal within-county stock is not the same as practical reach.
- Lower modeled need in a high-capacity county may reflect composition,
  resources, selection, or reporting/modeling differences rather than the
  effect of local providers.

## Next decisive place test

The next place pass should add one of the following observable mechanisms:

1. HRSA component geography and designated population, not just county overlap;
2. travel time or distance to primary-care providers and neighboring-county
   alternatives;
3. insurance acceptance, appointment availability, price, and provider
   workload;
4. MEPS or another compatible health-use source with delayed or foregone care;
5. ACS/NHTS transportation and vehicle constraints with a documented common
   geography; and
6. a dated local service disruption, closure, expansion, or policy event with
   later care, work, household-time, or political outcomes.

The public-data output should remain a matched-place panel and uncertainty
register until a person-, household-, provider-, or event-level design becomes
available. The program should not convert this county screen into a claim about
health inequality, local culture, trust, or political response.

## Reproduction and sources

- [CDC PLACES portal](https://www.cdc.gov/places/)
- [CDC PLACES county data, 2024 release](https://data.cdc.gov/d/fu4u-a9bh)
- [CDC PLACES portal documentation](https://www.cdc.gov/places/tools/explore-places-data-portal.html)
- [HRSA shortage-area downloads](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas)
- [Census CBP 2023 county file](https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip)
- [Census 2023 county population estimates](https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/totals/co-est2024-alldata.csv)
- [Reproduction script](../../../../scripts/analyze_places_hpsa_outcomes.py)
- [Committed summary output](../data/places-hpsa-outcomes-summary.json)
- [Machine-readable county-capacity/outcomes record](../../../records/us-cdc-places-county-capacity-outcomes-2024.json)
- [Earlier CBP–HRSA capacity bridge](../cbp-hrsa-primary-care-shortage-bridge-v1.md)

**Evidence status:** compared ecological place diagnostic using CDC modeled
county estimates, Census employer stock, population estimates, and current HRSA
designations. It does not estimate causal capacity effects, patient access,
health outcomes, household burden, trust, belonging, or political action.
