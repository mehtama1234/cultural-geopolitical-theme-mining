# Finding 018: The same SNAP transition leaves a different material footprint when work capacity and children differ

**Status:** bounded same-person subgroup finding · **Checked:** 2026-09-19

## The bounded finding

The 2025 SIPP public-use file follows identified people across adjacent 2024
reference months. The retained analysis compares SNAP entry, exit, and stable
status while conditioning on two social-capacity markers recorded in the first
month: a reported condition limiting the kind or amount of work, and one or
more children under 18 in the household.

Among people who remained on SNAP, those with a work-limiting condition and
children reported following-month rent/mortgage hardship at 17.85% and utility
hardship at 31.57%. The comparable stable-SNAP group with neither marker was at
7.77% and 11.60%. Among stable nonrecipients, the corresponding comparison was
9.18% and 16.78% versus 2.74% and 3.72%.

The result is not that SNAP caused the hardship or that the subgroup contrast
is a national rate. It is a same-person, time-ordered descriptive signal that
formal receipt and remaining household exposure can coexist, and that the
conversion depends on work capacity and household responsibility.

## The chain

```text
SNAP status or transition
  -> work-limiting condition and children present
  -> different following-month rent/utility hardship pattern
  -> remaining care, work, bill, and security burden [partial]
  -> notice, benefit amount, remedy, trust, action, and recovery [open]
```

## What it adds to the broad atlas

This is a useful correction to an overly simple “benefit received → household
secured” story. A food-support status can coexist with housing or utility
exposure, especially where work capacity and household demands narrow the
available alternatives. The two hardship currencies also diverge: utility
hardship is not interchangeable with rent or mortgage hardship.

The finding therefore adds a social-capacity modifier to the main route:

```text
institutional response × usable alternatives × household capacity
  -> practical protection, not formal participation alone
```

## Limits

- The work-limitation field is not a complete disability measure, and children
  under 18 are not a measure of parenthood or caregiving hours.
- “Following month” is adjacent record order; hardship questions have their own
  reference periods and do not prove that a new bill followed a SNAP decision.
- Transition groups are selected and sparse. For example, the work-limiting,
  children-present SNAP-exit cell has only 17 valid pairs for the hardship
  outcome, with a 18.05-point standard error for utility hardship.
- SIPP does not identify notice, effort, benefit amount, appeal, correction,
  food quantity, care obtained, trust, political action, or later recovery for
  the same episode.
- The comparison is descriptive and does not estimate a SNAP effect.

## Next decisive test

The next valid upgrade is an authorized episode-compatible file that records
notice and route effort, benefit amount and timing, care/work trade-offs,
household bills, correction or appeal, and later security or trust. Until then,
receipt, exit, and hardship remain separate stages.

## Reproduction and provenance

The underlying calculation is documented in the [SIPP transition × work
limitation × children layer](../sipp-snap-transition-outcome-disability-children-fay-brr-layer-v1.md).
It reads 379,215 primary person-month rows and produces 294,814 adjacent pairs
matched to the official 240-replicate-weight file. Percentages use the first
month's final weight and Fay-BRR uncertainty; no raw person-level file is
retained in the repository.
