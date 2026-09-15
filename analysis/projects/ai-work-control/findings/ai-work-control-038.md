# Sector pay context does not restore worker control

**Status:** provisional partial-year work-control context · **Checked:** 2026-09-14

## The bounded finding

The January–August 2026 BLS CES series shows rising establishment average
hourly earnings in four selected private industries, while the companion
January–July 2026 JOLTS series shows openings slightly above the 2025 annual
mean but hires similar and quits lower. The combination is useful context for
the AI/work-control lane:

> Sector pay can rise while worker mobility remains cool, but establishment
> averages and turnover rates do not reveal whether workers gained time,
> discretion, bargaining power, safety, or a practical ability to refuse a
> tool.

This is a partial-year cross-source comparison. CES and JOLTS are establishment
surfaces with different measures and no common worker or workplace key. It is
not a wage-effect estimate, an AI-effect estimate, or a claim that lower quits
were caused by employer power.

## The current comparison

| Sector/context | CES Jan–Aug 2026 average hourly earnings | Jan–Aug movement in CES series | Related JOLTS context | Interpretation boundary |
|---|---:|---:|---:|---|
| Manufacturing | $36.625/hour | $36.20 → $36.92 preliminary | National openings/hiring/quits, not sector-matched in this record | Pay surface and national mobility context are not the same workers |
| Professional and business services | $45.4337/hour | $45.03 → $45.70 preliminary | Same | High average pay does not identify worker discretion, monitoring, or outside options |
| Education and health services | $36.2413/hour | $36.13 → $36.39 preliminary | Same | Sector average can coexist with care burden, staffing pressure, or schedule instability |
| Leisure and hospitality | $23.5413/hour | $23.30 → $23.74 preliminary | Same | Tips, hours, multiple jobs, and within-sector composition are not in the mean |
| Total nonfarm JOLTS | — | — | Openings 4.3714%, hires 3.3143%, quits 1.9571% Jan–Jul 2026; 2025 annual means 4.2750%, 3.3167%, 2.0167% | Establishment rates are not individual transition probabilities |

The CES sector means are arithmetic means of eight monthly seasonally adjusted
observations. July and August are preliminary. The JOLTS means are arithmetic
means of seven monthly seasonally adjusted national rates, with July
preliminary. The two partial-year windows are therefore not identical and must
not be read as a synchronized panel.

## What the comparison adds

The earlier sector bridge placed 2025 mobility, formal union membership, and
average pay beside one another. This 2026 refresh adds time ordering without
claiming a worker result:

```text
sector demand and pay context
  -> worker access, outside options, and retention
  -> task allocation, monitoring, pace, and discretion
  -> pay, health, safety, voice, and household security
```

The new observations reach only the first box and part of the second. CES
shows that the selected sector averages moved upward during the first eight
months of 2026. JOLTS shows that national vacancies remained visible while
hires were nearly unchanged from the 2025 mean and quits were lower. The
combination weakens two shortcuts:

1. **Higher average pay is not the same as higher worker power.** Pay can move
   because of composition, hours, occupation mix, premium pay, or employer
   adjustments without changing decision rights.
2. **Visible openings are not necessarily accessible alternatives.** A worker
   may face geographic, care, credential, health, schedule, immigration,
   transportation, or employer-specific constraints that establishment data
   cannot see.

## Counterexamples and safeguards

- A lower quits rate can reflect worker preference, retirement, sector mix,
  delayed mobility, or reduced outside options; it is not a direct measure of
  coercion or bargaining weakness.
- A rising average hourly earnings series can coexist with falling real wages,
  reduced hours, unstable schedules, benefit loss, or higher household costs.
- A sector with high average pay can contain low-paid occupations and unequal
  access to the gains; the establishment mean has no worker-distribution
  denominator.
- A worker can receive a useful AI tool and retain discretion, or receive the
  same tool under monitoring and pace rules that reduce practical control.
- July and August CES/JOLTS observations are preliminary and may be revised;
  the partial-year means are not annual estimates.

## Next decisive test

The required next design is a worker- or workplace-conditioned panel joining:

`sector and firm exposure -> AI/system function -> training and access -> task/pacing/monitoring rule -> pay/hours/health/safety -> worker voice/appeal -> household and exit outcome`

The design should stratify by sector, occupation, firm size, union status,
age, education, disability, care responsibility, place, and schedule control.
It should retain workers who report higher pay but no greater authority and
workers who report lower mobility despite stable or improving pay. The CES and
JOLTS series remain conditioning context until that common worker or workplace
key exists.

## Sources and reproduction

- [2026 CES machine-readable record](../../../records/us-bls-ces-industry-earnings-2026-ytd.json)
- [2026 CES derived data](../data/bls-ces-industry-earnings-2022-2026-derived.json)
- [2026 JOLTS finding](ai-work-control-037.md)
- [2025 mobility/union/earnings context record](../../../records/us-bls-jolts-union-earnings-industry-context-2025.json)
- [CES manufacturing series](https://data.bls.gov/timeseries/CES3000000003)
- [CES professional/business services series](https://data.bls.gov/timeseries/CES6000000003)
- [CES education/health services series](https://data.bls.gov/timeseries/CES6500000003)
- [CES leisure/hospitality series](https://data.bls.gov/timeseries/CES7000000003)
- [CES reproduction script](../../../../scripts/fetch_bls_ces_industry_earnings.py)

**Evidence status:** official establishment-based partial-year pay and mobility
context; worker-level wage distribution, job quality, control, bargaining,
household security, political meaning, and AI causality remain open.
