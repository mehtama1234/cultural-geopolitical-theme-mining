# Matched-place housing, capacity, and access option stack v1

**Checked:** 2026-09-13
**Status:** selected-county descriptive screen; not a migration, housing, or service-access causal estimate

## Why add housing to the place screen

Sector establishments do not tell us whether a place can absorb new or
existing residents. A place can have firms but too little housing, or vacant
units that are unaffordable, distant, seasonal, inaccessible, or disconnected
from jobs and services. The relevant societal question is an option stack:

```text
population change and composition
  -> housing cost, vacancy, crowding, and language-access need
  -> firms, providers, travel, and local capacity
  -> who can reach, afford, use, or leave the place
  -> belonging, trust, conflict, or political demand
```

## Unit and sources

The screen contains six lower-change and six higher-change counties among US
counties above 100,000 residents. It combines:

- 2020 and 2023 Census population estimates;
- 2023 ACS five-year foreign-born share and foreign-born arrival timing;
- 2023 ACS median gross rent, vacant housing units, crowded units, and limited
  English-speaking population;
- 2023 CBP retail, health/social-assistance, and food establishments and
  employees per 10,000 residents;
- 2023 BDS state context and BFS application intensity; and
- RUCC rurality plus a current HRSA primary-care HPSA component flag.

The fields are different units and stages. Vacancy is not available affordable
housing; establishments are not usable care; limited-English share is not an
identity or deficiency measure; and an HPSA component is not a county-wide
shortage estimate.

## Selected place comparison

| Group | County | Population change % | Rent $ | Vacant units % | Crowded units % | Limited-English % | Health establishments/10k | Health employees/10k | HPSA |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Lower change | San Francisco County, CA | -6.36 | 2,419 | 11.88 | 6.51 | 18.95 | 44.19 | 952.13 | Yes |
| Lower change | St. Louis city, MO | -5.84 | 978 | 16.94 | 2.14 | 3.11 | 55.66 | 1,364.53 | Yes |
| Lower change | Bronx County, NY | -5.76 | 1,436 | 4.19 | 12.09 | 25.31 | 21.92 | 896.15 | Yes |
| Lower change | Calcasieu Parish, LA | -5.55 | 1,096 | 18.49 | 2.28 | 1.68 | 29.05 | 683.95 | Yes |
| Lower change | Hinds County, MS | -5.40 | 1,032 | 15.54 | 2.53 | 1.25 | 32.58 | 1,200.04 | Yes |
| Lower change | Terrebonne Parish, LA | -4.91 | 1,010 | 11.42 | 2.53 | 2.13 | 26.72 | 609.02 | Yes |
| Higher change | Kaufman County, TX | 26.87 | 1,408 | 5.77 | 5.41 | 6.18 | 11.62 | 228.32 | No |
| Higher change | Rockwall County, TX | 20.54 | 1,899 | 4.62 | 2.21 | 4.37 | 30.39 | 474.49 | No |
| Higher change | Comal County, TX | 18.61 | 1,460 | 9.17 | 2.03 | 3.37 | 27.31 | 448.18 | No |
| Higher change | Liberty County, TX | 18.01 | 1,038 | 13.68 | 6.91 | 13.51 | 10.99 | 139.05 | Yes |
| Higher change | Sumter County, FL | 16.77 | 1,225 | 16.71 | 1.21 | 1.91 | 19.06 | 471.75 | Yes |
| Higher change | Parker County, TX | 16.05 | 1,440 | 7.74 | 2.35 | 3.10 | 19.93 | 230.00 | Yes |

## What the selected screen shows

The higher-change group has a higher median rent ($1,424 versus $1,064) and a
lower median vacancy rate (8.46% versus 13.71%) than the lower-change group,
but this is a small selected comparison and not a population estimate. Median
crowding is similar (2.28% versus 2.53%), while limited-English shares are
more varied than either group median suggests.

Fast growth is not one housing pattern. Kaufman and Rockwall have low vacancy,
while Sumter has 16.71% vacancy. Liberty combines high growth, 6.91% crowded
units, 13.51% limited-English share, and a HPSA component. Comal has high growth
and no HPSA component but a smaller health employment footprint than the
decline counties. These are counterexamples to both “growth automatically
creates shortage” and “visible capacity means practical access.”

## Societal interpretation

The same population change can redistribute different kinds of pressure:

- renters may face price and crowding pressure without a measured shortage in
  establishments;
- owners or landlords may face vacant units that do not match local wages,
  jobs, or transport;
- clinics may be present while provider adequacy, appointments, price, or
  language access remains weak;
- firms may enter while workers and residents lack bargaining power or a nearby
  alternative;
- residents may interpret the change as opportunity, exclusion, revitalization,
  or loss of control depending on their own ability to stay, move, or use the
  new capacity.

These meanings are not inferred here. Direct belonging, fairness, attribution,
trust, and political-action measures remain a separate required layer.

## Limits and next test

- The twelve counties are a screen, not a representative sample.
- Population change mixes demographic processes and does not identify
  migration.
- ACS medians and shares are place aggregates; they do not show who moved,
  who was displaced, or why a unit is vacant.
- CBP and HRSA are capacity indicators, not service-use, quality, or outcome
  measures.
- State BDS rates are context, not county dynamics.

The next matched-place pass should add vacancy and rent to a larger all-county
conditioning model, then connect similar places to travel time, wages, permits,
provider adequacy, service use, and direct measures of belonging and political
response. Preserve high-growth/high-capacity and low-growth/low-access cases as
counterexamples.

## Reproduction

```text
python3 scripts/analyze_migration_place_capacity_panel.py \
  --cbp /tmp/cbp23co.zip \
  --population /tmp/co-est2024-alldata.csv \
  --hpsa /tmp/BCD_HPSA_FCT_DET_PC.csv \
  --rucc /tmp/rucc2023.csv \
  --nativity /tmp/acsdt5y2023-b05002.dat \
  --arrival /tmp/acsdt5y2023-b05005.dat \
  --rent /tmp/acsdt5y2023-b25064.dat \
  --vacancy /tmp/acsdt5y2023-b25002.dat \
  --crowding /tmp/acsdt5y2023-b25014.dat \
  --language /tmp/acsdt5y2023-c16001.dat \
  --bfs /tmp/bfs_county_apps_annual.xlsx \
  --bds /tmp/bds2023_st.csv --n 6
```
