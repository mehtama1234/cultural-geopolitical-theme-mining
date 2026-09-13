# Matched place panel: migration, demand, capacity, and belonging v1

**Checked:** 2026-09-12  
**Status:** measurement design for the next empirical pass; not a causal estimate

## Why this is the next depth pass

The opening scan establishes the broad proposition: new residents can be
workers, customers, neighbors, entrepreneurs, and users of public systems at
the same time. The next step is not another national immigration opinion
source. It is a place-level panel that can observe whether demand, capacity,
cost, ownership, and belonging move together or separate.

## Unit discipline

Do not join unlike records as if they were one observation.

| Level | Record | Questions it can answer |
|---|---|---|
| Person | nativity, arrival, language, work, schooling, health, civic response | Who is exposed, participating, working, or excluded? |
| Household | tenure, rent, crowding, income, commuting, service use | Who absorbs cost, time, or access pressure? |
| Firm/establishment | entry, exit, employment, ownership, sector | Does demand become durable local capacity? |
| Place | population composition, rents, wages, permits, schools, clinics, transit | Does capacity keep pace with population and demand? |
| Institution | caseload, wait, staffing, language access, complaints, budgets | Where does administrative pressure or adaptation appear? |
| Opinion/political event | belonging, blame, trust, protest, vote, policy demand | How does material change acquire cultural and political meaning? |

## Minimum panel fields

Use counties or commuting zones as the starting geography, with a consistent
annual window and a pre-period. Add a small-place sensitivity check only where
the data support it.

1. **Population and movement:** total change, domestic and international
   migration, foreign-born share, recent-arrival share, age, language, and
   household composition.
2. **Labor and demand:** labor-force participation, employment, occupation,
   wages, customer-facing employment, income, retail/service activity, and
   commuting.
3. **Firm capacity:** business applications, employer establishments, openings,
   closures, jobs created/destroyed, sector mix, ownership, and survival.
4. **Housing and mobility:** rent, home prices, vacancy, overcrowding,
   construction/permits, tenure, evictions where available, travel time, and
   transit access.
5. **Public capacity:** school enrollment and staffing, clinic/provider supply,
   shortage designations, emergency/administrative workload, language access,
   and local fiscal capacity.
6. **Distribution and meaning:** outcomes by income, tenure, race/ethnicity,
   nativity, language, age, and industry; then direct measures of belonging,
   perceived fairness, trust, blame, contact, and political response.

## Comparison logic

Select places with similar pre-period size, labor market, housing cost, sector
mix, and region, but different population-change paths. Compare:

```text
population-change path
  -> worker and customer composition
  -> firms, jobs, rents, housing supply, and service workload
  -> unequal cost, access, and opportunity
  -> local adaptation, conflict, trust, belonging, and political demand
```

The primary contrast is **capacity keeping pace** versus **capacity lagging**.
Do not define this from one indicator: use housing supply, employer/service
stocks, staffing or workload, and affordability together. Preserve a
counterexample where population change is high but the predicted cost or
political response does not appear.

## Source routing

| Need | Candidate source family | Keep separate |
|---|---|---|
| population, nativity, language, housing, commuting | Census ACS and population estimates | Stock/estimate is not an arrival event or motive |
| labor and wages | Census ACS, QCEW, BLS | Employment is not job quality or bargaining power |
| applications and realized firms/jobs | Census BFS, BDS, CBP | Application, establishment stock, opening, and survival are different stages |
| rents, prices, construction, eviction | ACS, FHFA, permits, court/administrative records where available | Higher rent is not displacement or voluntary mobility |
| schools, clinics, transit, public workload | NCES, HRSA, NHTS, agency records | Spending or enrollment is not service quality |
| belonging and political interpretation | representative surveys, local records, election/participation data, coded public discourse | Attitude is not proof of a demographic or economic cause |

## What this can and cannot establish

It can establish whether population-change paths coincide with distinct local
labor, demand, firm, housing, service, and distributional patterns, and whether
those patterns are accompanied by measured differences in belonging or policy
response. It cannot, by itself, prove that migration caused a rent increase,
job gain, service failure, or attitude. Timing, selection into places, national
shocks, policy differences, and measurement gaps must remain visible.

The end-to-end claim is therefore conditional: migration may expand capability
and demand while also creating capacity pressure; the societal result depends
on who owns the new activity, who receives the gains, who pays the adjustment
cost, and whether institutions convert change into fair access and belonging.

## Next executable pass

Build a small matched-place table for one period with population change,
foreign-born/recent-arrival change, wages, sector employment, BFS/BDS/CBP firm
measures, ACS rent/overcrowding/vacancy, and one school or health-capacity
measure. Add a second period before interpreting political or cultural meaning.
Label every field as stock, flow, rate, estimate, or reported perception.
