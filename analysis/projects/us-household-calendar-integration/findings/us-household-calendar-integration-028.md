# Utility difficulty and assistance sit beside, not inside, next-month work change

**Status:** provisional same-person transition screen · **Checked:** 2026-09-14

## The bounded finding

The 2025 SIPP public-use file allows a more direct material-to-work timing
screen than a cross-source comparison: identify a person-month's reported
utility-payment difficulty or energy-assistance status, then inspect whether
that same person's nonnegative earnings or hours value changes in the following
month. Census Fay-BRR replicate weights provide uncertainty for the descriptive
shares.

| Month-*t* screen | Eligible consecutive person-month pairs | Earnings changed at *t+1* | Hours changed at *t+1* |
|---|---:|---:|---:|
| Utility-payment difficulty | 24,289 | 81.68% (n=9,269; SE 2.50 pp) | 7.71% (n=9,474; SE 6.41 pp) |
| No utility-payment difficulty | 321,766 | 84.03% (n=145,626; SE 2.67 pp) | 5.28% (n=147,006; SE 2.23 pp) |
| Energy assistance | 13,389 | 79.59% (n=3,454; SE 2.15 pp) | 7.65% (n=3,513; SE 0.74 pp) |
| No energy assistance | 177,970 | 82.56% (n=70,188; SE 0.41 pp) | 6.71% (n=70,965; SE 0.18 pp) |

The apparent differences are not a simple “utility burden causes work loss”
story. Earnings-change shares are high in every group, while the utility-
difficulty hours estimate is imprecise and its interval includes a wide range.
Energy-assistance recipients show a lower earnings-change share and a somewhat
higher hours-change share than the no-assistance comparison, but eligibility,
need, season, geography, health, and job composition are not controlled here.

## What this adds to the end-to-end program

This is a same-person timing layer between material conditions and work
movement. It does not yet observe the exact utility bill, shutoff threat,
rate, payment, care substitution, desired hours, employer response, or later
recovery. It therefore narrows the missing-arrow question: a valid next step
must distinguish routine monthly work movement from a dated utility event and
must measure whether assistance changes the route, not merely who receives it.

The result also preserves a counterexample to a one-directional hardship model.
The no-difficulty group has a slightly higher earnings-change share, while the
energy-assistance group has a lower one. A work change can therefore coexist
with both material strain and institutional support, and a stable utility
screen cannot be read as stable work.

## Limits and next test

- SIPP person-month rows repeat household utility fields; these are not
  household-prevalence estimates.
- Earnings and hours use separate valid-pair universes and are numeric-value
  changes, not job loss, involuntary reduction, desired-hours mismatch, or
  welfare loss.
- The screen is observational. It does not establish that utility conditions
  or assistance caused the following-month movement.
- The 2024 reference year does not identify a precise bill due date, price,
  weather shock, provider action, or political interpretation.

The next end-to-end test is a dated utility event or administrative episode
linked to payment status, assistance route, work hours/earnings, care or travel
time, and a later hardship or recovery outcome. Until that exists, this record
should remain a conditional transition surface rather than a causal bridge.
The [SIPP utility-to-work time-field gate](../sipp-utility-work-following-time-field-gate-v1.md)
records why the current data do not support promoting `ETIMELOST`, `ATIMELOST`,
or `EWORKMORE` into a generic following-month time-displacement outcome.

## Reproduction

- [Machine-readable record](../../../records/us-sipp-utility-work-following-2024.json)
- [Analysis script](../../../../scripts/analyze_sipp_utility_work_following.py)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [Official SIPP replicate-weight archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)
- [2026-09-14 reproduction audit](../sipp-utility-work-following-reproduction-audit-2026-09-14.json)

**Evidence status:** same-person descriptive monthly transition with Fay-BRR
uncertainty; not a causal utility-to-work estimate.
