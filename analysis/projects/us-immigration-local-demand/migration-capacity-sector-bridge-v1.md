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

| Group | County | 2020→23 population % | ACS 2023 foreign-born % | RUCC | HPSA component | Retail est./10k | Health/social est./10k | Food est./10k |
|---|---|---:|---:|---:|---|---:|---:|---:|
| Lower change | San Francisco County, CA | -6.36 | 34.22 | 1 | yes | 35.50 | 44.19 | 51.53 |
| Lower change | St. Louis city, MO | -5.84 | 6.61 | 1 | yes | 27.51 | 55.66 | 37.20 |
| Lower change | Bronx County, NY | -5.76 | 34.21 | 1 | yes | 28.26 | 21.92 | 14.51 |
| Lower change | Calcasieu Parish, LA | -5.55 | 3.29 | 2 | yes | 38.05 | 29.05 | 22.69 |
| Lower change | Hinds County, MS | -5.40 | 1.86 | 2 | yes | 34.36 | 32.58 | 22.33 |
| Lower change | Terrebonne Parish, LA | -4.91 | 3.16 | 3 | yes | 41.81 | 26.72 | 21.72 |
| Higher change | Kaufman County, TX | 26.87 | 10.84 | 1 | no | 18.10 | 11.62 | 13.07 |
| Higher change | Rockwall County, TX | 20.54 | 8.70 | 1 | no | 24.39 | 30.39 | 21.04 |
| Higher change | Comal County, TX | 18.61 | 6.64 | 1 | no | 26.53 | 27.31 | 24.42 |
| Higher change | Liberty County, TX | 18.01 | 13.79 | 1 | yes | 18.78 | 10.99 | 10.99 |
| Higher change | Sumter County, FL | 16.77 | 5.85 | 3 | yes | 18.86 | 19.06 | 13.08 |
| Higher change | Parker County, TX | 16.05 | 5.16 | 1 | yes | 23.97 | 19.93 | 16.31 |

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
  --nativity /tmp/acsdt5y2023-b05002.dat --n 6
```

The script labels the population measure as a proxy on purpose. The ACS field
is the 2023 five-year foreign-born share, not the number or timing of arrivals.
The next version must add recent-arrival, language, tenure, rent, and crowding
fields before the table is described as a full migration comparison.

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
- BFS applications, BDS openings/closures and job flows, and CBP employment;
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
- [CBP county essential-sector capacity layer](../us-local-business-place/cbp-county-essential-capacity-population-layer-v1.md)
- [CBP rural/urban capacity profile](../us-local-business-place/cbp-capacity-rural-urban-profile-v1.md)
- [CBP–HRSA primary-care shortage bridge](../us-local-business-place/cbp-hrsa-primary-care-shortage-bridge-v1.md)
- [Migration, local demand, housing, services, and belonging layer](migration-demand-housing-services-belonging-layer-v1.md)
- [NBER local-demand study](https://www.nber.org/papers/w21123)
