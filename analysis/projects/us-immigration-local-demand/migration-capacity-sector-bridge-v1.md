# Migration, local demand, and sector capacity bridge v1

**Checked:** 2026-09-12  
**Status:** descriptive cross-source bridge; not a migration causal estimate

## Result in plain words

The existing place evidence shows why migration cannot be summarized as either
an economic gain or a service burden. Counties have different sector capacity
before any migration explanation is added. In 2023, population-weighted
nonmetro counties had more retail and manufacturing establishments per resident,
while metro counties had more health/social-assistance establishments; food
service was nearly equal. Separately, 2,785 of 3,072 matched counties with a
usable health-sector row were represented by at least one HRSA primary-care
shortage component, despite similar establishment counts between the groups.

These are not migration effects. They establish the baseline that a migration
comparison must condition on: sector mix, rurality, employer scale, shortage
status, and the difference between presence and adequacy.

## First place table: population-change proxy

The first reproducible cut uses 2020–2023 total population change as a proxy
for local demographic pressure or release. It selects the six lowest- and six
highest-change counties among counties above 100,000 residents, then attaches
2023 CBP establishment presence per 10,000 residents, 2023 RUCC, and whether a
current HRSA primary-care HPSA component carries the county FIPS. This is a
descriptive screening table, not a matched causal comparison and not an
international-migration estimate.

| Group | County | 2020→23 population % | Foreign-born % | Entered 2010+ % | Median rent $ | Crowded units % | Limited-English % | RUCC | HPSA | Retail/10k | Health/10k | Food/10k |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| Lower change | San Francisco County, CA | -6.36 | 34.22 | 24.49 | 2419 | 6.51 | 18.95 | 1 | yes | 35.50 | 44.19 | 51.53 |
| Lower change | St. Louis city, MO | -5.84 | 6.61 | 42.95 | 978 | 2.14 | 3.11 | 1 | yes | 27.51 | 55.66 | 37.20 |
| Lower change | Bronx County, NY | -5.76 | 34.21 | 26.60 | 1436 | 12.09 | 25.31 | 1 | yes | 28.26 | 21.92 | 14.51 |
| Lower change | Calcasieu Parish, LA | -5.55 | 3.29 | 36.81 | 1096 | 2.28 | 1.68 | 2 | yes | 38.05 | 29.05 | 22.69 |
| Lower change | Hinds County, MS | -5.40 | 1.86 | 43.01 | 1032 | 2.53 | 1.25 | 2 | yes | 34.36 | 32.58 | 22.33 |
| Lower change | Terrebonne Parish, LA | -4.91 | 3.16 | 37.62 | 1010 | 2.53 | 2.13 | 3 | yes | 41.81 | 26.72 | 21.72 |
| Higher change | Kaufman County, TX | 26.87 | 10.84 | 23.57 | 1408 | 5.41 | 6.18 | 1 | no | 18.10 | 11.62 | 13.07 |
| Higher change | Rockwall County, TX | 20.54 | 8.70 | 21.84 | 1899 | 2.21 | 4.37 | 1 | no | 24.39 | 30.39 | 21.04 |
| Higher change | Comal County, TX | 18.61 | 6.64 | 18.84 | 1460 | 2.03 | 3.37 | 1 | no | 26.53 | 27.31 | 24.42 |
| Higher change | Liberty County, TX | 18.01 | 13.79 | 23.25 | 1038 | 6.91 | 13.51 | 1 | yes | 18.78 | 10.99 | 10.99 |
| Higher change | Sumter County, FL | 16.77 | 5.85 | 11.13 | 1225 | 1.21 | 1.91 | 3 | yes | 18.86 | 19.06 | 13.08 |
| Higher change | Parker County, TX | 16.05 | 5.16 | 20.85 | 1440 | 2.35 | 3.10 | 1 | yes | 23.97 | 19.93 | 16.31 |

The contrast is a diagnostic, not a conclusion. Several fast-growth counties
have lower establishment presence than the decline group, especially in health
and food; some high-growth counties also have an HPSA component. That pattern
supports the next test of capacity lag, but it does not show that population
growth caused a shortage, nor that a county without a matched component has
adequate care.

### Reproduction

```text
python3 scripts/analyze_migration_place_capacity_panel.py \
  --cbp /tmp/cbp23co.zip \
  --population /tmp/co-est2024-alldata.csv \
  --hpsa /tmp/BCD_HPSA_FCT_DET_PC.csv \
  --rucc /tmp/rucc2023.csv \
  --nativity /tmp/acsdt5y2023-b05002.dat \
  --arrival /tmp/acsdt5y2023-b05005.dat \
  --rent /tmp/acsdt5y2023-b25064.dat \
  --crowding /tmp/acsdt5y2023-b25014.dat \
  --language /tmp/acsdt5y2023-c16001.dat \
  --bfs /tmp/bfs_county_apps_annual.xlsx \
  --bds /tmp/bds2023_st.csv --n 6
```

The script labels the population measure as a proxy on purpose. The ACS field
is the 2023 five-year foreign-born share. The 2010-plus field is the share of
the ACS B05005 foreign-born universe entered in 2010 or later; it is not a
2020–2023 flow or a count of new residents. The limited-English field is the
share of the C16001 population speaking a non-English language at home and
reporting English less than “very well.” It signals language-access workload
or need, not low ability, identity, legal status, or a cultural problem.

The housing fields are also descriptive: median gross rent is a place-level
median, and crowded units are occupied units with more than one person per
room. Neither field identifies a migrant household, displacement, or whether
housing supply caused the population change.

## Firm-stage diagnostic

The same selected counties can also be linked to Census Business Formation
Statistics (BFS) applications and the CBP employer-establishment stock. The
figures below are applications per 100 2023 employer establishments; they are
not conversion rates, firm births, or jobs.

| Group | County | BFS 2023 / 100 CBP establishments | BFS 2025 / 100 CBP establishments |
|---|---|---:|---:|
| Lower change | San Francisco County, CA | 52.93 | 61.96 |
| Lower change | St. Louis city, MO | 81.58 | 80.37 |
| Lower change | Bronx County, NY | 94.58 | 81.65 |
| Lower change | Calcasieu Parish, LA | 63.70 | 60.89 |
| Lower change | Hinds County, MS | 119.93 | 115.25 |
| Lower change | Terrebonne Parish, LA | 52.69 | 49.31 |
| Higher change | Kaufman County, TX | 123.68 | 146.08 |
| Higher change | Rockwall County, TX | 77.49 | 84.83 |
| Higher change | Comal County, TX | 60.07 | 66.43 |
| Higher change | Liberty County, TX | 108.46 | 134.49 |
| Higher change | Sumter County, FL | 73.14 | 79.05 |
| Higher change | Parker County, TX | 75.46 | 82.62 |

The diagnostic suggests that population growth and business-application
intensity are not interchangeable. Some high-growth counties show high
application intensity, while others do not; some declining counties also show
high intensity. The next step is to attach realized BDS openings, closures,
employment, and survival before interpreting applications as local economic
capacity.

## Realized firm dynamics at state context

County-level BDS dynamics are not available in the current release used here,
so the selected counties are attached to their state's 2023 BDS rates. This is
context, not a county estimate and not a county causal effect.

| State represented in screen | BDS entry rate % | BDS exit rate % | BDS net job creation rate % |
|---|---:|---:|---:|
| California | 11.401 | 10.256 | 1.440 |
| Missouri | 10.032 | 9.576 | 2.578 |
| New York | 10.530 | 9.691 | 3.341 |
| Louisiana | 8.934 | 8.056 | 3.170 |
| Mississippi | 9.077 | 8.544 | 1.460 |
| Texas | 11.850 | 9.394 | 3.815 |
| Florida | 13.105 | 10.909 | 3.784 |

The state context adds a realized stage to the story: entry, exit, and net job
creation are distinct from applications and from county establishment stocks.
It still cannot tell us which counties, sectors, owners, workers, or residents
received the gains or absorbed the churn. The next firm pass should use BDS
metro/sector data or a later county-capable release, then add wages, survival,
ownership, and service outcomes.

## The bridge

```text
population change and composition
  -> workers, customers, and service needs
  -> sector-specific establishment and employment capacity
  -> travel, wait, price, job, and ownership differences
  -> unequal exposure and adaptation
  -> belonging, trust, and political demand (direct measures required)
```

| Existing evidence | What it establishes | What it does not establish |
|---|---|---|
| CBP county sector stock + population | Rough place capacity differs by sector and county | Access, quality, staffing, price, or migration cause |
| CBP employment + population | Establishment count and employment scale are different measures | Job quality, hours, wages, or worker power |
| CBP + RUCC | Metro/nonmetro capacity profiles are sector-specific | Rural or urban residents' actual reachable service |
| CBP + HRSA HPSA | Establishment presence can coexist with a formal primary-care shortage component | County-wide shortage, unmet need, or patient outcome |
| NBER local-demand evidence | Immigrant demand can be associated with local job creation in the studied period | Current place effect, housing response, or political meaning |

## Why this changes the next question

The right comparison is not “more immigrants versus fewer immigrants.” It is:

1. Did population and resident composition change?
2. Did customer-facing demand, labor supply, and firm entry change separately?
3. Did the relevant sector's employment and establishment capacity keep pace?
4. Did housing, travel, prices, and public-service workload keep pace?
5. Which residents received jobs or services, and which absorbed cost or time?
6. Did people interpret the change as opportunity, revitalization, competition,
   exclusion, loss of control, or fair adaptation?

The same place can answer “yes” to several apparently conflicting statements:
new residents can add customers; businesses can expand; care can remain
inadequate; rents can rise; and belonging can become contested.

## Next empirical join

Use the matched-place design with a pre/post window and add, in order:

- Census population estimates and ACS population composition, nativity,
  language, tenure, rent, crowding, and commuting;
- QCEW or ACS labor and wage measures by sector;
- BDS openings/closures, job flows, and survival to follow the BFS application
  diagnostic, with CBP employment;
- HRSA component-level shortage and provider measures;
- permits, vacancy, travel, school, and local administrative workload where
  available;
- direct survey or local-record measures of belonging, trust, blame, and
  political response.

Use capacity-keeping-pace and capacity-lagging places as the primary contrast,
with a counterexample. Keep county, person, household, firm, institution, and
opinion records separate; a cross-source bridge supplies context, not a hidden
individual-level causal join.

## Source anchors

- [Census ACS 2023 five-year table-based B05002 data](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b05002.dat), SHA-256: `48bbc708638cc7d83d63bd003f6c0517d75888c16a47c8248e737ce5fcb02ceb`
- [Census ACS 2023 five-year table-based B05005 data](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b05005.dat), SHA-256: `58897ce0329c1b9d5b89ff20a7e61ff1c461d451678133b74155170d83c806e6`
- [Census ACS 2023 five-year table-based B25064 data](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b25064.dat), SHA-256: `8b887d1e102916ef12718e51a29ae303a562a1d7ac545756bfb6a76e3d7b96b7`
- [Census ACS 2023 five-year table-based B25014 data](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-b25014.dat), SHA-256: `6c7b5b56a5b0cabb44c99ca48c9bc7961f6ff347bc658f18eef9212aaee3c8ba`
- [Census ACS 2023 five-year table-based C16001 data](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/5YRData/acsdt5y2023-c16001.dat), SHA-256: `895422f304c56dde8038269259ebe03bb28407be325adfa48d7e5e2292b055fe`
- [Census Business Formation Statistics county applications](https://www.census.gov/econ/bfs/xlsx/bfs_county_apps_annual.xlsx), SHA-256: `327cd7fb8877da4e8d6e82bbe5737c2c78138ff03bd8cd0e68d7707ec3451f5e`
- [Census Business Dynamics Statistics 2023 state CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st.csv), SHA-256: `9e0c86610ee685c2f7c8c4dec60bd213177cd8644fe539e5f66457efc8ef603c`
- [CBP county essential-sector capacity layer](../us-local-business-place/cbp-county-essential-capacity-population-layer-v1.md)
- [CBP rural/urban capacity profile](../us-local-business-place/cbp-capacity-rural-urban-profile-v1.md)
- [CBP–HRSA primary-care shortage bridge](../us-local-business-place/cbp-hrsa-primary-care-shortage-bridge-v1.md)
- [Migration, local demand, housing, services, and belonging layer](migration-demand-housing-services-belonging-layer-v1.md)
- [NBER local-demand study](https://www.nber.org/papers/w21123)
