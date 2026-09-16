# Health-cost friction does not produce one uniform health-direction pattern

**Status:** bounded MEPS route-comparison finding  
**Checked:** 2026-09-16

## Bounded finding

Two existing MEPS 2024 longitudinal screens point in different directions.
Among people reporting a prescription affordability/access delay in round 4/2,
perceived health improved for 24.62% and worsened for 19.12%. Among people
reporting no such delay, improvement was 20.42% and worsening was 22.11%.

The denial/prior-authorization screen has the opposite descriptive pattern:
among round-5/3 reporters, perceived health improved for 19.04% and worsened
for 25.11%, compared with 20.29% and 21.74% among non-reporters.

| Existing screen | Friction group | Health improved | Health worsened | Valid records |
|---|---|---:|---:|---:|
| Prescription delay at round 4/2 | Yes | 24.62% | 19.12% | 674 |
| Prescription delay at round 4/2 | No | 20.42% | 22.11% | 17,683 |
| Denial/prior authorization at round 5/3 | Yes | 19.04% | 25.11% | 1,574 |
| Denial/prior authorization at round 5/3 | No | 20.29% | 21.74% | 8,591 |

## What this adds to the end-to-end chain

```text
health-cost or coverage friction
  -> care/medication route and treatment continuity
  -> perceived-health direction
  -> payment, work, unpaid care, recovery, remedy, trust, or action
```

The new result is not that one kind of friction is beneficial and another is
harmful. It is that “institutional friction” is too broad a mechanism label:
the observed direction depends on which route, round, question, and selected
population is being measured. That is a useful counterexample to a uniform
friction-to-health story.

## Interpretation boundary

These are two separate, non-pooled screens. Prescription delay is a round-4/2
reported affordability/access condition. Denial or prior-authorization delay
is a round-5/3 reported insurance condition. The latter is not proven to occur
after the round-4/2 health endpoint, and neither screen contains a claim ID,
decision date, appeal, treatment completion, or household alternative.

Underlying illness, medication need, severity, coverage, age, employment,
selection, and regression toward the mean can affect both the reported
friction and later perceived-health direction. Perceived health is ordinal and
is not a clinical recovery measure.

| Arrow | Status | Safe conclusion |
|---|---|---|
| Route-specific friction → perceived-health direction | Separate longitudinal descriptive screens | The two route definitions do not share one direction; improvement and worsening coexist in each |
| Friction → treatment continuity or payment | Open | No fill, adherence, claim resolution, balance, or due date is observed |
| Friction → household substitution or recovery | Open | Work, food, housing, care-time, debt, and later reversal are not linked |
| Friction → trust, action, switching, or exit | Open | Requires a same-person episode with attribution and follow-up |

## Reproduction and next test

The [machine-readable comparison](../data/us-meps-2024-friction-route-direction-comparison.json)
preserves the rounded source-screen values and input-record hashes. Reproduce
the underlying screens with the [prescription-delay script](../../../../scripts/analyze_meps_prescription_delay_health_direction.py)
and [institutional-friction script](../../../../scripts/analyze_meps_institutional_friction_followup.py).

The next decisive test is a single medication or authorization episode with a
dated need, intended treatment, denial or delay reason, payment obligation,
fill/adherence or treatment-continuity outcome, household money/time response,
and later remedy or recovery. Until then, keep prescription delay and
authorization friction as distinct route-specific mechanisms.

## Official sources

- [AHRQ MEPS HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes)
- [AHRQ MEPS HC-036BRR variance file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-036BRR&prfricon=yes)
- [Prescription-delay health-direction finding](us-health-cost-household-choice-010.md)
- [Institutional-friction health/work finding](us-health-cost-household-choice-011.md)
