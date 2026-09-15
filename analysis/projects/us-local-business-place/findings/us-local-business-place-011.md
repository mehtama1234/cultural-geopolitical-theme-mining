# Business applications are an early signal, not realized local capacity

**Status:** provisional Census BFS–BDS firm/place finding · **Checked:** 2026-09-15

## The bounded finding

The 2023 Census Business Formation Statistics and Business Dynamics Statistics
show why “entrepreneurship” cannot be read from application counts alone.
Business applications are an early signal. BDS records realized establishment
openings, closings, and job flows. Across sectors, the relationship between the
two changes sharply.

The safe conclusion is:

> **A sector can attract many business applications without producing the same
> amount of employer capacity or net job growth. Conversely, a sector with
> fewer applications can produce much larger realized job flows.**

The comparison is national and sector-level. It is not an application-to-firm
conversion rate, a survival estimate, a local-service measure, or a worker
quality result.

## What the comparison shows

| Sector | BFS applications | BDS openings per 100 applications | BDS net jobs per 100 applications | Openings minus closings |
|---|---:|---:|---:|---:|
| Retail trade | 971,630 | 8.0 | 5.4 | +7,733 establishments |
| Professional, scientific, and technical services | 674,660 | 15.4 | 37.0 | +12,002 |
| Construction | 546,160 | 16.6 | 44.5 | +13,468 |
| Health care and social assistance | 325,200 | 30.2 | 271.0 | +28,027 |
| Accommodation and food services | 302,250 | 25.9 | 261.9 | +13,865 |
| Administrative/support and waste management | 407,790 | 12.3 | −32.0 | +4,164 |
| Information | 101,720 | 14.8 | −8.6 | −1,310 |
| Agriculture, forestry, fishing, and hunting | 78,480 | 2.6 | −7.4 | −223 |

The ratios are comparison statistics, not conversion rates. BFS applications
and BDS annual flows have different timing, units, definitions, and statistical
constructions. “Net jobs per 100 applications” does not mean that 100
applications created that number of jobs.

## The counterexample that prevents a simple story

Administrative/support and waste-management activity recorded positive net
establishment openings and closings but negative net jobs per 100 applications.
Information and agriculture also show negative net-job intensity. This means
that establishment entry can coexist with job contraction.

Health care/social assistance and accommodation/food services show the other
side: fewer applications than retail but much higher job intensity and positive
establishment differences. That does not mean those sectors necessarily offer
better work or better services. It shows only that application volume is not a
common scale for realized capacity.

Retail is another useful counterexample. It has the largest application count
in this profile but a much lower job-intensity comparison than construction,
care, or food services. A large application stream may reflect many small,
non-employer, repeated, unrealized, or later-forming activities rather than a
large immediate increase in local employer capacity.

## The firm/place chain under test

```text
business application or early intention
  -> projected or realized formation
  -> establishment opening, survival, closure, and job flow
  -> employer stock, service availability, prices, ownership, and local dependence
  -> worker bargaining room, household access, place meaning, and political response
```

The BFS–BDS comparison reaches the first three steps only in separate national
sector aggregates. It does not match the same application to the same firm, and
it does not observe the service or worker downstream effects.

## What this adds to the atlas

### “More businesses” needs a verb

The relevant question is whether a place is seeing applications, projected
formations, realized establishments, surviving employers, jobs, payroll, or
usable services. Each is a different stage. A city may have high formation
interest while employer stock remains flat, or high employer growth while
workers experience high turnover.

### Sector matters because everyday dependence differs

An opening in health care, food, construction, retail, or information does not
change daily life in the same way. Care and food establishments may affect
reaching essential services; construction may affect housing repair or supply;
information may affect digital capability. The BDS layer identifies candidate
systems, not completed social consequences.

### Growth can contain churn

Positive net jobs and positive openings-minus-closings can coexist with many
individual establishments opening and closing. Workers may experience
instability inside a growing sector, and customers may experience changing
prices, hours, quality, or travel even when a national employment total rises.

## Method and boundaries

- Unit: US national sector, 2023.
- BFS denominator: sector business applications.
- BDS measures: establishment openings, closings, and job flows.
- Method: descriptive cross-source sector comparison; no sampling interval is
  reproduced in the committed record.
- The comparison does not identify firm survival, ownership, wages, job
  quality, worker control, local access, informal activity, or causal effects.
- National aggregation hides state, county, rural/urban, firm-size, and
  ownership differences.

## Next test

Use BDS state/county-sector tables and comparable BFS geography to select three
contrasting place types: high applications/high entry, high applications/high
exit, and low applications/high realized job growth. Add employer stock,
survival, payroll, ownership, population, rents, provider capacity, prices,
travel, complaints, and worker outcomes.

Keep two counterexamples in the place panel: a place where applications rise
without durable employer or service growth, and a place where stable employer
stock hides high turnover. Only after the firm stage is measured should the
program connect sector change to local belonging, trust, civic action, or
political response.

## Sources and reproduction

- [Machine-readable BFS–BDS sector record](../../../records/us-bfs-bds-sector-dynamics-2023.json)
- [BFS–BDS sector divergence layer](../bfs-bds-sector-divergence-layer-v1.md)
- [Realized firm entry, exit, and sector turnover layer](../bds-realized-entry-exit-sector-layer-v1.md)
- [Census Business Formation Statistics](https://www.census.gov/econ/bfs/data.html)
- [Census Business Dynamics Statistics](https://www.census.gov/programs-surveys/bds.html)

**Evidence status:** bounded national sector comparison; it establishes
different firm/job stages and a sector counterexample, not local capacity,
worker power, household welfare, cultural meaning, political action, or
geopolitical consequence.
