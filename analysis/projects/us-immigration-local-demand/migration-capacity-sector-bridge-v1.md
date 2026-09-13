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

- [CBP county essential-sector capacity layer](../us-local-business-place/cbp-county-essential-capacity-population-layer-v1.md)
- [CBP rural/urban capacity profile](../us-local-business-place/cbp-capacity-rural-urban-profile-v1.md)
- [CBP–HRSA primary-care shortage bridge](../us-local-business-place/cbp-hrsa-primary-care-shortage-bridge-v1.md)
- [Migration, local demand, housing, services, and belonging layer](migration-demand-housing-services-belonging-layer-v1.md)
- [NBER local-demand study](https://www.nber.org/papers/w21123)

