# A cooling labor market does not have one meaning of worker power

**Status:** provisional multi-measure work and voice finding · **Checked:** 2026-09-13

## The bounded finding

BLS data show a cooling national labor-market mobility environment after the
2022 peak, but the meaning of that cooling differs by industry and cannot be
read as a single change in worker power. In 2025, quits, formal union
membership, and average hourly earnings occupied different positions across
manufacturing, professional and business services, education and health
services, and leisure and hospitality.

The evidence supports a measurement rule:

> Worker optionality has at least three distinct observable surfaces—ability to
> leave or move, formal representation, and pay—and none is a substitute for
> schedule control, grievance success, job quality, or household security.

This is a descriptive sector comparison, not a causal estimate of union effects
or a worker-level account of why anyone stayed or left.

## National context

BLS JOLTS annual means show national job openings falling from 6.85% in 2022
to 4.275% in 2025, hires from 4.20% to 3.3167%, and quits from 2.7583% to
2.0167%. Total separations also fell from 3.9583% to 3.2917%, while layoffs
and discharges rose from 0.9583% to 1.1167%.

These are annual arithmetic means of monthly seasonally adjusted establishment
rates. They summarize establishment reports, not unique workers. The sequence
is consistent with fewer openings and voluntary moves after the reopening
period, but it does not identify whether outside options, job quality, worker
preferences, retirement, or industry composition caused the change.

## 2025 sector comparison

| Industry | JOLTS quits rate | CPS union membership | CES average hourly earnings |
|---|---:|---:|---:|
| Manufacturing | 1.3917% | 7.7% | $35.45/hour |
| Professional and business services | 2.3417% | 2.1% | $44.26/hour |
| Education and health services | 1.9333% | 8.2% | $35.59/hour |
| Leisure and hospitality | 3.9250% | 3.0% | $22.84/hour |

The numbers do not form a ranking of good and bad work. Leisure and
hospitality combines the highest quits rate in this comparison with low
average pay and low formal membership. Professional and business services
combines higher pay with higher quits and low formal membership. Education and
health services combines comparatively lower quits with the highest membership
share and near-manufacturing average pay. Manufacturing has the lowest quits
rate in the comparison but a different representation/pay context.

Those patterns demonstrate why a lower quits rate cannot automatically mean
less power, and a higher quits rate cannot automatically mean more power. A
high quits rate may reflect churn, unstable jobs, or abundant alternatives; a
low rate may reflect retention, preference, institutional voice, or the cost of
leaving.

## What each measure can and cannot say

| Measure | Direct object | Useful question | Missing outcome |
|---|---|---|---|
| JOLTS quits | Establishment-reported voluntary separations | How much voluntary movement is occurring in the sector? | Who moved, why, to what job, and with what result? |
| JOLTS openings/hires | Establishment-reported recruiting and hiring rates | How many opportunities and transitions are visible to establishments? | Whether opportunities were accessible, stable, or well paid |
| CPS union membership | Employed wage-and-salary workers reporting membership | Where is formal representation present? | Contract coverage, grievance success, worker control, or bargaining outcome |
| CES average hourly earnings | Establishment average for all employees | What is the sector-level pay context? | Distribution, hours, benefits, schedules, prices, and household room |

The denominators are intentionally not collapsed. JOLTS is an establishment
survey, CPS is a household survey, and CES is an establishment earnings
series. BLS also notes that 2025 annual CPS union estimates exclude October
and are not strictly comparable with earlier annual averages.

## The mechanism under test

```text
sector demand and job structure
  -> openings, hiring, quits, layoffs, pay, and representation
  -> practical ability to stay, leave, complain, bargain, or absorb a shock
  -> household income, time, health, security, and status
  -> trust, identity, collective action, and political meaning
```

The BLS records reach the first two lines only in aggregate. They do not show
the same worker's decision, employer rule, household consequence, or political
interpretation.

## Counterexamples that keep the finding honest

- A sector can have high quits because jobs are poor and workers are cycling
  through instability rather than exercising choice.
- A sector can have low quits because work is secure and well supported, or
  because leaving is expensive and alternatives are weak.
- Union membership can be high while practical grievance access is weak, or
  low while workers have other forms of voice and mobility.
- High average pay can coexist with long hours, poor schedules, high injury
  risk, or unequal pay within the sector.
- A national cooling pattern can hide stronger mobility for a subgroup or a
  place, and a sector average can hide firm-level concentration.

## What the next test requires

The next compatible design should link workers or workplaces over time to:

1. job changes, openings, layoffs, and reasons for movement;
2. pay, hours, schedules, benefits, training, and task/control changes;
3. union coverage, grievance route, contract terms, and actual remedy;
4. household income, debt, care, health, commute, and time room; and
5. trust, attribution, organizing, civic action, or vote after a defined
   workplace or sector event.

Use a sector or firm where mobility and formal representation point in
different directions as a counterexample. The decisive question is not whether
the aggregate quits rate rose or fell, but whether a worker could make a
meaningful move, contest a decision, and protect household security.

## Sources

- [BLS JOLTS API](https://api.bls.gov/publicAPI/v2/timeseries/data/)
- [BLS Union Members 2025, Table 3](https://www.bls.gov/news.release/union2.t03.htm)
- [BLS CES average hourly earnings](https://www.bls.gov/ces/)
- [National JOLTS trend record](../../../records/us-bls-jolts-national-mobility-2020-2025.json)
- [Selected-industry mobility record](../../../records/us-bls-jolts-selected-industry-mobility-2022-2025.json)
- [Mobility and union context record](../../../records/us-bls-jolts-union-industry-context-2025.json)
- [Mobility, representation, and earnings record](../../../records/us-bls-jolts-union-earnings-industry-context-2025.json)

**Evidence status:** observed/estimated descriptive sector context with
different source populations; worker-level control, causal representation
effects, household consequences, and political meaning remain open.
