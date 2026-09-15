# Finding 065: Sector mobility, pay, and representation describe different workplace rooms

**Status:** provisional cross-source sector comparison · **Checked:** 2026-09-14

## The bounded finding

The national JOLTS surface can look relatively cool while sector-level
workplace rooms remain very different. In 2025, four named sectors had
distinct combinations of establishment quits, average hourly earnings, and
CPS union membership:

| Sector | JOLTS quits rate | CES average hourly earnings | CPS union membership |
|---|---:|---:|---:|
| Manufacturing | 1.39% | $35.45 | 7.7% |
| Professional and business services | 2.34% | $44.26 | 2.1% |
| Education and health services | 1.93% | $35.59 | 8.2% |
| Leisure and hospitality | 3.93% | $22.84 | 3.0% |

The defensible synthesis is: **sector labor-market mobility, average pay, and
formal representation form different workplace contexts; none is a direct
measure of worker control, job quality, or the ability to exit.**

## Why the pattern matters

The highest-quits sector in this comparison—leisure and hospitality—also has
the lowest average pay among the four and relatively low formal union
membership. That combination is consistent with a workplace environment in
which movement may be frequent while bargaining room is not necessarily
strong. It is not proof of that mechanism: quits can reflect opportunity,
seasonality, worker composition, job duration, or employer turnover.

Professional and business services show the opposite-looking combination:
the highest average pay, a middle quits rate, and the lowest union-membership
share. Higher pay does not therefore imply formal voice. Education and health
services have relatively high formal membership and moderate pay and quits,
but the aggregate rates do not show whether representation produces schedule
control, grievance success, or protection from workload.

Manufacturing has the lowest quits rate in this four-sector frame, with pay
near education and health services and higher membership than professional
and business services. A low quits rate can mean stable employment, fewer
outside options, worker preference, or sector composition. The rate cannot
select among those interpretations.

## Denominators and methods stay separate

| Surface | Unit | What it measures | What it does not measure |
|---|---|---|---|
| JOLTS | establishment-month | seasonally adjusted quits rate | unique worker transitions, reasons, job quality, or AI exposure |
| CES | establishment-month average | average hourly earnings for employees | individual earnings distribution, benefits, hours, or household room |
| CPS Union Members | employed wage-and-salary worker | annual membership share by industry | bargaining success, grievance remedy, schedule control, or worker discretion |

The 2025 CPS annual estimate excludes October, while JOLTS and CES are
establishment-based series with their own frames and seasonal adjustment. The
figures are therefore a comparison frame, not a pooled regression or a sector
ranking of good and bad work.

## The larger work-control chain

```text
sector pay, mobility, and formal voice context
  -> actual workplace tool/rule/schedule event
  -> worker exposure, pace, discretion, monitoring, and correction
  -> health, household room, grievance, bargaining, or exit
  -> employer response, regulation, political meaning, or institutional change
```

This pass strengthens the context before the event. It does not observe the
same worker across the three BLS surfaces, and it does not identify a dated
workplace decision. The missing unit is a worker or workplace event with
exposure, permission, schedule, pay, monitoring, voice, and follow-up.

## Counterexamples kept visible

- High quits can reflect voluntary opportunity or constrained churn.
- Low quits can reflect good retention or a lack of credible alternatives.
- High average pay can coexist with weak formal representation.
- Formal representation can exist without measured grievance success or
  day-to-day discretion.
- Sector averages can hide large occupation, tenure, demographic, firm-size,
  and geography differences.

## Next decisive test

Use the sector cells to sample or identify a dated workplace implementation
event. The event ledger should retain sector, firm size, worker exposure,
announcement and implementation dates, training, monitoring, schedule change,
pay, representation, correction route, health or household consequence, and
whether the worker could switch or refuse. A successful design would tell us
whether the same surface combination produces different control outcomes
under different workplace institutions or outside options.

## Reproduction and sources

- [Machine-readable BLS sector context record](../../../records/us-bls-jolts-union-earnings-industry-context-2025.json)
- [BLS JOLTS national mobility record](../../../records/us-bls-jolts-national-mobility-2026-ytd.json)
- [BLS JOLTS, union, and earnings layer](../bls-jolts-union-earnings-industry-context-layer-v1.md)
- [BLS JOLTS](https://www.bls.gov/jlt/)
- [BLS union members](https://www.bls.gov/news.release/union2.t03.htm)
- [BLS Current Employment Statistics](https://www.bls.gov/ces/)

**Evidence status:** official BLS cross-source sector comparison; no worker-level
join, causal claim, household estimate, or political/geopolitical conclusion.
