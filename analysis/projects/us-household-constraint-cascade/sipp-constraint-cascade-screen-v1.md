# SIPP same-person constraint-cascade screen v1

**Checked:** 2026-09-16  
**Status:** adjacent-month Fay-BRR descriptive screen; not a causal episode  
**Source:** 2025 SIPP public-use file, 2024 reference year  
**Unit:** identified November-to-December person pair

## What this pass tests

This is the most complete same-person screen currently available locally. It
conditions November utility-payment difficulty and tenure, carries the annual
fall child-care work-prevention report on the December record, and places it
beside December work, housing, food, and resource outcomes.

```text
utility condition + tenure at November
  -> childcare work-prevention status
  -> December work movement, housing hardship, food insecurity,
     and income-to-poverty-band movement
```

It is an ordering in the file, not proof that a bill caused the following
outcome. The annual childcare field and some household fields are reference or
repeated measures rather than newly observed December events.

## Reproduction integrity

- 379,215 primary rows read
- 2,600 November-to-December pairs identified
- 2,600 of 2,600 pair keys matched to the official replicate archive
- 240 Fay-BRR replicate weights; perturbation factor 0.5
- November `WPFINWGT` used for pair estimates
- Separate valid denominators retained for every outcome

## Results

Percentages are person-weighted conditional shares. `n` is the valid pair
count for the subgroup; outcome-specific valid counts can be smaller.

| Utility at November | Tenure | Childcare prevented work | n | Hours changed in December | Mortgage hardship | Food insecure | Resource band changed |
|---|---|---:|---:|---:|---:|---:|---:|
| Difficulty | Owner/buyer | Yes | 10 | 26.15% (n=9) | 25.31% | 77.50% | 8.45% |
| Difficulty | Owner/buyer | No | 95 | 0.93% (n=62) | 38.22% | 49.35% | 2.72% |
| Difficulty | Renter | Yes | 12 | 34.95% (n=10) | 72.80% | 64.64% | 18.96% |
| Difficulty | Renter | No | 134 | 10.36% (n=84) | 57.99% | 50.21% | 5.56% |
| No difficulty | Owner/buyer | Yes | 42 | 3.97% (n=38) | 2.14% | 12.47% | 1.05% |
| No difficulty | Owner/buyer | No | 1,635 | 5.01% (n=1,167) | 0.79% | 4.60% | 4.03% |
| No difficulty | Renter | Yes | 30 | 6.02% (n=21) | 12.10% | 25.75% | 13.42% |
| No difficulty | Renter | No | 642 | 6.21% (n=383) | 2.96% | 18.02% | 5.80% |

The earnings-change endpoint is high across nearly every cell and is not a
work-loss measure. It is retained in the machine-readable output but is less
diagnostic than hours, hardship, food, and resource direction because any
numeric change counts, regardless of size or desirability.

## What the screen supports

1. **A joint constraint surface is measurable.** Utility, tenure, care-related
   work prevention, and several next-month outcomes can be kept on one
   person-pair frame with design-based uncertainty.
2. **Renter utility-difficulty pairs with childcare prevention are a high-risk
   diagnostic cell.** They show higher point estimates for hours movement,
   mortgage hardship, food insecurity, and resource-band movement than the
   corresponding renter/difficulty/no-prevention cell.
3. **The pattern is not universal.** Owner/buyer difficulty cells do not move
   in the same direction as renter cells, and no-difficulty childcare cells
   remain materially different from difficulty cells.
4. **The result identifies a testable cascade hypothesis, not a mechanism.**
   Housing cost, care need, work composition, health, season, family support,
   and selection into utility difficulty remain plausible explanations.

## Sparse-cell and clock limits

- The childcare-prevention cells with utility difficulty contain only 10 owner
  and 12 renter pairs; their estimates are diagnostic and imprecise.
- `EWORKMORE` describes annual fall childcare arrangements and is not care
  hours, a missed shift, or a December utility consequence.
- Utility difficulty is not a bill amount, arrears, shutoff, reconnection, or
  assistance decision.
- Mortgage hardship and food insecurity are separate December fields; neither
  proves which need was protected or sacrificed.
- A resource-band crossing is not continuous income loss, recovery, or a
  household-level poverty transition.
- Person weights and repeated household fields do not yield household
  prevalence without a separate household selection rule.

## Decisive next episode design

The next data object must add a dated bill, shutoff warning, payment plan,
coverage change, childcare disruption, or care need to this kind of person or
household spine. It should record the amount owed, alternatives, paid and
unpaid care, work schedule and earnings, institutional response, and one-,
three-, and six-month recovery or persistence outcomes. A comparable
counterexample with similar exposure but more liquid room, flexible work,
family support, or a functioning assistance route is required.

## Reproduction

- [Machine-readable output](../../records/us-sipp-constraint-cascade-screen-2024.json)
- [Analysis script](../../../scripts/analyze_sipp_constraint_cascade_screen.py)
- [SIPP utility/care reproduction route](../us-household-calendar-integration/sipp-utility-care-following-outcomes-bridge-v1.md)
- [SIPP utility/tenure/childcare audit](../us-household-calendar-integration/sipp-utility-tenure-childcare-reproduction-audit-2026-09-16.json)
- [Official SIPP data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)

Primary input hash: `4fe7395d4ecdb2f1a3f2879a394f47d1e809c9bdef3960b60543919b79a61eda`  
Replicate input hash: `3bf35c17723de10697d581d1122fda4d7cdecb34c6f9e9dfcb18ddc561c7c6b6`  
Script hash: `4ae5fbc993ff8edeb8aff5de4b12ee6f2db8c90f19a1f700b6ee5b59335173a8`

**Evidence status:** reproduced adjacent-month descriptive screen; not a
dated bill event, causal estimate, household prevalence estimate, recovery,
remedy, trust, political-action, or exit result.
