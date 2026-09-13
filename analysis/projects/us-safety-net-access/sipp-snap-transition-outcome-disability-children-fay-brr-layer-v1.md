# SIPP SNAP transition × work limitation × children: following hardship v1

**Checked:** 2026-09-13  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file; 2024 reference year  
**Unit:** identified person, adjacent reference-month pair  
**Weight:** `WPFINWGT` from month *t*; `REPWGT1`–`REPWGT240` for variance  
**Method:** Fay BRR with `G=240` and perturbation factor `0.5`; descriptive only

## Why this comparison matters

The public-system question is not simply whether SNAP receipt changes. The same
transition can occur for people with different work capacity and household
responsibilities, and the material result may remain different afterward.

```text
SNAP state at t -> SNAP state at t+1
  + work-limiting condition + children under 18 in household
  -> rent/mortgage or utility hardship reported in t+1
  -> notice, effort, amount, remedy, trust, and later action remain separate
```

`EDISABL` identifies a reported condition that limits the kind or amount of
work a person can do. `RHNUMU18` identifies one or more household members under
18; it is not a parenthood or caregiving-hours measure. The grouping variables
are taken from month *t*. The transition is still only a descriptive receipt
change, not a treatment assignment.

## Verified calculation

- 379,215 primary person-month rows were read.
- 294,814 adjacent transition pairs matched the replicate file and had valid
  work-limitation, children, and age/group status fields.
- All 16 transition × work-limitation × children cells were produced.
- Outcomes are valid code-1 reports in month *t+1*; each outcome has its own
  universe and valid denominator.
- Percentages below are weighted shares; parentheses are Fay-BRR standard
  errors in percentage points. `n` is the valid pair count for that outcome.

## Results

| SNAP transition | Work-limiting condition | Children under 18 | Rent/mortgage hardship | Utility hardship |
|---|---|---|---:|---:|
| No → No | Yes | None | 4.94% (0.44), n=37,336 | 7.77% (0.59), n=37,336 |
| No → No | Yes | 1+ | 9.18% (1.85), n=6,758 | 16.78% (2.29), n=6,758 |
| No → No | No | None | 2.74% (0.22), n=151,890 | 3.72% (0.25), n=151,890 |
| No → No | No | 1+ | 4.34% (0.40), n=72,898 | 6.67% (0.56), n=72,898 |
| No → Yes | Yes | None | 18.50% (6.94), n=68 | 28.91% (7.91), n=68 |
| No → Yes | Yes | 1+ | 20.23% (10.65), n=21 | 20.23% (10.65), n=21 |
| No → Yes | No | None | 13.83% (5.54), n=89 | 20.64% (5.97), n=89 |
| No → Yes | No | 1+ | 17.20% (5.45), n=124 | 20.91% (5.43), n=124 |
| Yes → No | Yes | None | 7.98% (3.73), n=65 | 12.10% (4.53), n=65 |
| Yes → No | Yes | 1+ | 26.11% (12.80), n=17 | 47.07% (18.05), n=17 |
| Yes → No | No | None | 10.72% (5.64), n=81 | 7.94% (2.88), n=81 |
| Yes → No | No | 1+ | 17.02% (6.10), n=120 | 28.57% (7.25), n=120 |
| Yes → Yes | Yes | None | 9.31% (1.26), n=10,465 | 16.79% (1.43), n=10,465 |
| Yes → Yes | Yes | 1+ | 17.85% (3.75), n=2,111 | 31.57% (4.49), n=2,111 |
| Yes → Yes | No | None | 7.77% (1.60), n=6,050 | 11.60% (1.76), n=6,050 |
| Yes → Yes | No | 1+ | 11.56% (1.84), n=6,721 | 16.47% (2.28), n=6,721 |

## What the comparison supports

### 1. The aggregate SNAP pattern is not socially uniform

Among stable nonrecipients, the work-limiting/children-present group reports
higher following-month rent/mortgage and utility hardship than the group with
neither condition. Among continued recipients, the same ordering remains: the
work-limiting/children-present cell is 17.85% for rent/mortgage hardship and
31.57% for utility hardship, compared with 7.77% and 11.60% for the
no-work-limitation/no-children cell.

This is a conditional distribution, not evidence that the work-limiting
condition or children caused the hardship. It may reflect resources, housing,
care, health, job access, household composition, eligibility, and other shocks.

### 2. Continued receipt is not the same as security

The continued-receipt cells retain substantial following-month hardship. SNAP
receipt and rent/utility protection are separate stages. A benefit can protect
food access while leaving housing, utilities, disability-related costs, or care
needs unresolved.

### 3. Transition cells are especially selected and uncertain

No→Yes and Yes→No pairs are rare. Their standard errors are wide, especially
for work-limiting people with children: the Yes→No utility estimate is 47.07%
with a 18.05-point standard error from only 17 valid pairs. These cells are
signals for acquisition and design, not reliable rankings of transition
success or failure.

### 4. The outcome must remain bill-specific

Utility hardship and rent/mortgage hardship do not move identically in every
cell. A public program may protect one part of a household budget while a
different bill remains exposed. Collapsing the outcomes into “financial
security” would erase that institutional and household tradeoff.

## Arrow status

| Arrow | Status | Safe conclusion |
|---|---|---|
| SNAP transition → following hardship | Time-ordered descriptive association | Hardship shares differ by observed transition, but selection and field timing prevent a program-effect claim. |
| Work limitation × children → hardship pattern | Observed distribution | The transition pattern differs across the two social-capacity dimensions, with replicate-weight uncertainty. |
| Receipt → restored security | Not established | Continued receipt can coexist with rent, mortgage, or utility hardship. |
| Exit → improved circumstances | Not established | Exit can reflect income, time limits, non-collection, reporting, family change, or administrative route. |
| Episode → trust, blame, action, or vote | Open | SIPP does not observe the same episode's interpretation or political response. |

## Limits

- Person-month records can represent covered members of a SNAP unit; they are
  not household benefit amounts or complete benefit spells.
- “Following month” is record order. The hardship questions have their own
  reference periods and do not prove that a new bill arrived after the SNAP
  transition.
- Work limitation is not a full disability measure; children-under-18 status
  is not care time or parenthood.
- The transition groups differ in need, eligibility, household composition,
  reporting, and other shocks.
- Fay-BRR intervals describe sampling uncertainty, not causal uncertainty.
- Notice, effort, benefit amount, timing, appeal, correction, food outcome,
  health, debt, dignity, trust, complaint, turnout, vote, and agency response
  remain unmeasured for the same episode.

## Next event-level test

Use the same-episode ledger to record notice channel and language, document
requests, effort, deadline, decision, amount and timing, interruption, appeal,
correction, food/housing result, fairness, blame, trust, complaint, contact,
organizing, turnout, and recovery. Compare similar needs across routes and
preserve eligible non-applicants, delayed cases, exits without improvement, and
unknown-reason transitions.

## Reproduction

```text
python3 scripts/analyze_sipp_snap_transition_outcomes_fay_brr.py \
  --primary /tmp/us-broad-sipp-2025/full-v11/sipp-household-slice.csv \
  --replicate-zip /tmp/us-broad-sipp-2025/rw2025_csv.zip \
  --group-by EDISABL_RHNUMU18 \
  --output /tmp/us-broad-sipp-2025/full-v11/snap-transition-outcomes-disability-children.json
```

The raw files and derived JSON remain outside the repository. The reusable
analysis script is [analyze_sipp_snap_transition_outcomes_fay_brr.py](../../../scripts/analyze_sipp_snap_transition_outcomes_fay_brr.py).

Related: [SNAP transition × following hardship](sipp-snap-transition-outcome-fay-brr-layer-v1.md),
[public-system meaning and action gap](public-system-meaning-action-gap-v1.md),
and [same-episode event-ledger design](same-episode-event-ledger-design-v1.md).
