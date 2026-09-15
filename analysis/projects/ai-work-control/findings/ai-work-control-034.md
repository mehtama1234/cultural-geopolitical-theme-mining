# Sector mobility, representation, and pay describe different workplace conditions

**Status:** provisional BLS cross-source work-control finding · **Checked:** 2026-09-14

## The bounded finding

The 2025 BLS context map shows that sector mobility, formal union membership,
and average hourly earnings do not form one workplace-quality scale. Across
four selected industries:

| Industry | JOLTS quits rate | CPS union membership | CES average hourly earnings |
|---|---:|---:|---:|
| Manufacturing | 1.39% | 7.7% | $35.45/hour |
| Professional and business services | 2.34% | 2.1% | $44.26/hour |
| Education and health services | 1.93% | 8.2% | $35.59/hour |
| Leisure and hospitality | 3.93% | 3.0% | $22.84/hour |

The contrast is descriptive, not causal. Leisure and hospitality has the
highest establishment quits rate and lowest average pay of these four sectors,
but that does not identify why workers leave or whether low pay caused the
movement. Education and health services has the highest formal membership rate
and a relatively low quits rate, but the aggregate comparison cannot attribute
that pattern to representation.

## What each source actually measures

- **JOLTS:** seasonally adjusted establishment-level monthly rates, summarized
  here as a 12-month 2025 arithmetic mean. It does not follow unique workers,
  identify reasons, or measure job quality or control.
- **CPS Union Members:** annual industry membership share among employed wage
  and salary workers. Membership is not contract coverage, grievance success,
  practical schedule control, or worker voice in a particular workplace.
- **CES:** establishment average hourly earnings for all employees in the
  selected industry series. It is not a worker-level wage trajectory and does
  not capture hours, benefits, scheduling, or within-sector inequality.

The denominators and sampling frames are intentionally retained as separate
objects. The comparison is a conditioning map for where a worker-level study
should look, not a joined worker dataset.

## The mechanism under test

```text
sector demand and job mobility
  + formal representation
  + pay context
  -> worker schedule, discretion, grievance, health, and exit
  -> household time/security and collective or political action
```

Only the first three context layers are measured here. The worker, household,
institutional-response, and political stages remain open.

## Counterexamples and safeguards

- High pay does not imply high worker control: professional/business services
  has the highest average pay but low formal membership and higher quits than
  manufacturing or education/health services.
- Formal membership does not guarantee low mobility or good lived conditions;
  membership rates do not observe contract enforcement, grievance resolution,
  or schedule autonomy.
- Low quits can reflect weak outside options, delayed exits, staffing needs,
  or composition rather than worker satisfaction or bargaining power.
- JOLTS rates describe establishments, while CPS and CES use different worker
  or establishment frames; rankings are not individual trajectories.
- BLS notes that 2025 CPS annual estimates exclude October and are not
  strictly comparable with earlier annual averages.

## Next end-to-end test

The next worker-power pass should match a defined worker or workplace unit to
a dated change in tool use, schedule, safety, pay, benefit, or grievance
route. It should observe notice, discretion, appeal, health/time response,
household security, retention or exit, and collective action. The comparison
must include workers in similar sectors with different representation or
workplace rules, and preserve firms where high mobility coexists with higher
pay or where representation coexists with high burden.

Until that design exists, the safe claim is that sector context identifies
different exposure and bargaining environments—not that unions reduce quits,
pay buys autonomy, or mobility measures worker power.

## Reproduction and sources

- [JOLTS/union industry context record](../../../records/us-bls-jolts-union-industry-context-2025.json)
- [JOLTS/union/earnings context record](../../../records/us-bls-jolts-union-earnings-industry-context-2025.json)
- [JOLTS/union context layer](../bls-jolts-union-industry-context-layer-v1.md)
- [JOLTS/union/earnings layer](../bls-jolts-union-earnings-industry-context-layer-v1.md)
- [BLS JOLTS API](https://api.bls.gov/publicAPI/v2/timeseries/data/)
- [BLS Union Members Table 3](https://www.bls.gov/news.release/union2.t03.htm)

**Evidence status:** four-industry descriptive cross-source comparison;
worker-level causation, control, household consequences, trust, collective
action, and geopolitical implications are not established.
