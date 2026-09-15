# Mobility burden is split between vehicle scarcity, distance, and time

**Status:** provisional cross-source mobility synthesis · **Checked:** 2026-09-13  
**Project:** Household calendar integration

## The bounded finding

The existing NHTS and ACS layers do not support one national “mobility
burden” score. They show three distinct currencies:

1. whether a household has a vehicle;
2. how long recorded work or shopping trips take; and
3. the income, race, and place conditions around those measures.

These currencies can move in opposite directions. Lower-income households are
more likely to lack a vehicle, while higher-income workers can have longer
recorded commutes. Rural households can have fewer zero-vehicle records but
longer high-income work trips. The safe synthesis is that mobility options are
distributed through resources and geography, but time exposure is not a simple
inverse of income or vehicle ownership.

## What the source families show

| Source and unit | Comparison | Result | Boundary |
|---|---|---|---|
| 2022 NHTS urban household/travel-day cells | Urban income under $35k versus $75k+ | Zero-vehicle households: 35.23% versus 3.54%; 30+ minute work trips: 31.46% versus 40.82%; shopping-trip mean: 34.01 versus 20.71 minutes | Household and trip denominators differ; recorded trips omit missed or substituted trips |
| 2022 NHTS rural household/travel-day cells | Rural income under $35k versus $75k+ | Zero-vehicle households: 12.79% versus 0.71%; 30+ minute work trips: 13.92% versus 53.40%; shopping-trip mean: 29.65 versus 26.31 minutes | Small cells; rural classification does not measure service reach or trip necessity |
| 2024 ACS PUMS housing/person records | Household income under $35k versus $75k+ | Zero-vehicle households: 22.25% versus 3.74%; 30+ minute worker commutes: 32.30% versus 40.98% | Past-year household income; commute excludes work-from-home and does not measure fares, reliability, or care travel |
| 2024 ACS PUMS person records | Black versus White workers with positive commute minutes | 30+ minute commute: 42.64% versus 36.64% | Unadjusted race classification; geography, occupation, household income, transit quality, and mechanism remain open |
| 2024 ACS state aggregates | State median-income quartiles | Zero-vehicle households: 6.90%, 6.77%, 11.52%, 8.16%; 30+ minute commutes: 33.43%, 35.48%, 41.22%, 42.31% | State context is not household income; no margin-of-error propagation in the quartile pooling |

## The mechanism under test

```text
money, housing location, vehicle ownership, and local form
  -> available modes and distance
  -> money cost, travel time, waiting, reliability, and schedule flexibility
  -> ability to reach work, shopping, care, health, and civic activity
  -> household adaptation, missed activity, trust, or political meaning
```

The current evidence reaches the first three arrows only partially. It shows
that a vehicle can be absent while a trip is short, or present while a commute
is long. It does not show whether a trip was chosen, required, affordable,
reliable, safe, or successfully completed. “No vehicle” is therefore not a
synonym for exclusion, and “long commute” is not a synonym for deprivation.

## Why the counter-pattern matters

The high-income NHTS urban cell has far more vehicles but longer work trips
than the low-income urban cell. In rural areas, the contrast is even sharper:
the high-income cell has only 0.71% zero-vehicle households but 53.40% of
recorded work trips lasting at least 30 minutes. This may reflect job and
housing sorting, longer distances, or greater ability to choose where to live;
the source does not distinguish those explanations.

The ACS state context supplies a second counterexample. The third median-income
quartile has the highest pooled no-vehicle share (11.52%), plausibly reflecting
dense, transit-served states, while the highest-income quartile has the longest
pooled 30-plus-minute commute share (42.31%). State income is not a household
resource measure, so this is a place-context warning rather than a household
inequality estimate.

The PUMS race comparison adds an exposure difference without a mechanism:
Black workers have a higher 30-plus-minute commute share than White workers in
the unadjusted positive-commute universe. It cannot be translated into a claim
about discrimination or unequal access without conditioning on place,
occupation, income, vehicle access, transit, and care obligations.

## What this contributes to the end-to-end atlas

This synthesis prevents the material/time lane from collapsing transport into
one scarcity measure. A household may have a vehicle but spend substantial
time reaching work; another may lack a vehicle but use transit, walking,
rideshare, or nearby services; a rural household may have vehicles while
bearing long distances. The relevant downstream outcome is not vehicle
ownership alone but whether a person can complete required work, care, medical,
shopping, and civic activities without shifting cost into money, waiting,
unpaid help, or lost opportunity.

No cultural, political, or geopolitical conclusion is promoted here. Those
arrows require a same-place or same-household design with fares/fuel/repair
costs, travel time and reliability, care or medical purpose, missed or delayed
activity, alternatives, and later interpretation or action.

## Method and limits

- NHTS uses `WTHHFIN` for household measures and `WTTRDFIN` for travel-day
  trip measures; its income bands and urban/rural cells are not ACS PUMS cells.
- ACS PUMS housing measures use `WGTP`; worker commute measures use `PWGTP`
  after a `SERIALNO` household-person join.
- ACS aggregate state tables pool B08201 vehicle totals and B08303 commute
  totals within B19013 median-income quartiles; the quartiles are geographic
  contexts, not household-income strata.
- The layers are cross-sectional and use different years, universes, weights,
  and geographies. They are compared as complementary frames, not merged as
  respondent-level evidence.

## Next test

1. Add state/place-level fares, fuel and repair costs, transit and provider
   capacity, travel-time reliability, and care/medical trip measures.
2. Match compatible place-year exposure to work, service use, missed activity,
   move/stay, or household adaptation outcomes.
3. Preserve urban/rural, income, race, disability, tenure, and household-child
   differences with uncertainty and a substitute-access counterexample.
4. Add direct belonging, trust, civic action, or institutional response only
   after the mobility encounter and attribution are measured.

## Sources and related layers

- [2022 NHTS mobility/material/work/care record](../../../records/us-nhts-mobility-material-work-care-2022.json)
- [2024 ACS PUMS mobility subgroup record](../../../records/us-acs-pums-mobility-subgroups-2024.json)
- [2024 ACS state-income transportation record](../../../records/us-acs-transport-state-income-context-2024.json)
- [2022 NHTS urban/rural mobility-options record](../../../records/us-nhts-urban-rural-mobility-options-2022.json)
- [2024 ACS annual transport layer](../acs-transport-annual-national-layer-v1.md)
- [Machine-readable 2023–2024 ACS annual transport record](../../../records/us-acs-transport-annual-national-2023-2024.json)

**Evidence status:** cross-source descriptive synthesis with explicit unit and
denominator separation; no transport-affordability, missed-activity, care,
causal, cultural, political, or geopolitical outcome is established.
