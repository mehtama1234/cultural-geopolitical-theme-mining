# Resource position is followed by different earnings and hours movement across work-limiting status

**Status:** reproducible same-person SIPP cross-lag with Fay-BRR uncertainty · **Checked:** 2026-09-14

## The bounded finding

The SIPP monthly resource/job analysis can be extended to two work measures:
total person earnings (`TPEARN`) and average weekly hours at all jobs
(`TMWKHRS`). Among pairs with valid nonnegative numeric values, the share that
changed by the following month differs across resource bands and reported
work-limiting status.

The result measures change, not direction or welfare. A changed earnings value
can rise or fall; a changed hours value can be more or less desired.

## Work-limiting condition reported

| Resource band at month t | Earnings changed by t+1 | Hours changed by t+1 |
|---|---:|---:|
| Below 1× poverty | 66.70% (SE 4.93 pp; CI 57.03–76.37) | 16.88% (SE 2.55 pp; CI 11.89–21.87) |
| 1–1.99× | 71.33% (SE 3.64 pp; CI 64.20–78.47) | 10.04% (SE 1.12 pp; CI 7.85–12.23) |
| 2–3.99× | 80.09% (SE 1.57 pp; CI 77.01–83.17) | 9.26% (SE 0.83 pp; CI 7.62–10.89) |
| 4× or more | 85.58% (SE 1.03 pp; CI 83.57–87.60) | 7.61% (SE 0.63 pp; CI 6.38–8.84) |

## No work-limiting condition reported

| Resource band at month t | Earnings changed by t+1 | Hours changed by t+1 |
|---|---:|---:|
| Below 1× poverty | 61.32% (SE 1.94 pp; CI 57.51–65.13) | 12.09% (SE 0.75 pp; CI 10.63–13.55) |
| 1–1.99× | 79.82% (SE 0.90 pp; CI 78.06–81.58) | 7.19% (SE 0.40 pp; CI 6.40–7.98) |
| 2–3.99× | 83.84% (SE 0.55 pp; CI 82.76–84.92) | 5.41% (SE 0.20 pp; CI 5.02–5.79) |
| 4× or more | 86.21% (SE 0.28 pp; CI 85.67–86.75) | 4.28% (SE 0.14 pp; CI 4.01–4.55) |

The descriptive pattern is not a simple “more resources means more stability.”
Earnings changes become more common at higher resource bands, while hours
changes become less common. Among people reporting a work-limiting condition,
hours-change shares are higher at every displayed resource band, but that
does not tell us whether hours were lost, gained, desired, or accommodated.

## What this adds to the end-to-end program

The prior SIPP pass established that resource position and job counts move on
different clocks. This pass adds work intensity and person earnings as separate
outcomes:

```text
work-limiting status
  -> access, accommodation, hours, earnings, or job composition
  -> monthly resource position
  -> food, housing, utilities, care, and time room
  -> recovery, trust, institutional judgment, or political action
```

Only the first two measured transitions are observed. No health event, employer
decision, care response, household outcome, or political meaning is identified.

## Limits and counterexamples

- `TPEARN` and `TMWKHRS` have separate valid pair universes; the denominators
  cannot be treated as identical.
- A changed earnings value may be an increase or decrease, and no sign is
  inferred here.
- A changed hours value does not reveal desired hours, schedule control, job
  quality, or accommodation.
- `EDISABL` is a reported work-limiting-condition field, not a diagnosis,
  complete disability measure, or discrimination measure.
- Resource bands, work status, age, occupation, household composition, and
  selection differ across cells; no causal contrast is claimed.
- Person weights do not create a household estimate, and repeated household
  conditions remain a person-record issue.

## Next test

Add the direction of earnings and hours change, monthly SNAP status, tenure,
children, care/time fields, and documented status flags. Then test whether a
work or resource transition is followed by a valid food, housing, utility, or
benefit outcome. A dated health, employer, or administrative event remains
necessary for a stronger causal or end-to-end interpretation.

## Reproduction

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [Reproduction audit](../sipp-work-limitation-hours-earnings-reproduction-audit-2026-09-14.json)
- [Machine-readable record](../../../records/us-sipp-resource-worklimitation-hours-earnings-crosslag-2024.json)
- [Analysis script](../../../../scripts/analyze_sipp_resource_worklimitation_hours_earnings.py)
- [Related resource/job/work-limitation cross-lag](us-household-calendar-integration-025.md)

**Evidence status:** same-person monthly cross-lag with design-based uncertainty;
no causal, household, cultural, political, or geopolitical conclusion is
claimed.
