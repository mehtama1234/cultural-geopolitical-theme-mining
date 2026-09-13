# SIPP SNAP transition × race × work limitation × children: following hardship v1

**Checked:** 2026-09-13  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file; 2024 reference year  
**Unit:** identified person, adjacent reference-month pair  
**Weight:** `WPFINWGT` from month *t*; `REPWGT1`–`REPWGT240` for variance  
**Method:** Fay BRR with `G=240` and perturbation factor `0.5`; descriptive only

## Why this comparison matters

The public-system pattern should not be summarized as “SNAP recipients” or
“people with children.” The same receipt transition can sit inside different
combinations of race, reported work limitation, and household children.

```text
SNAP state at t -> SNAP state at t+1
  + race + work-limiting condition + children under 18
  -> rent/mortgage or utility hardship in t+1
  -> notice, effort, amount, remedy, meaning, and action remain separate
```

`ERACE` is the SIPP race recode used in the public-use slice: White alone,
Black alone, Asian alone, and Residual. `EDISABL` identifies a reported
condition limiting the kind or amount of work a person can do. `RHNUMU18`
identifies one or more household members under 18; it is not parenthood or
caregiving hours.

## Verified calculation

- 379,215 primary person-month rows were read.
- 294,814 adjacent transition pairs matched the replicate file.
- 64 transition × race × work-limitation × children cells were produced.
- Outcomes are valid code-1 reports in month *t+1*; each outcome has its own
  valid universe.
- Percentages below are weighted shares; parentheses are Fay-BRR standard
  errors in percentage points. `n` is the valid pair count for that outcome.

## Stable-state comparison

Rare entry and exit cells are retained in the machine-readable output but are
not ranked here: their estimates are often based on single-digit or low-double-
digit records. The stable states provide the more interpretable distributional
screen.

| SNAP state | Race | Work limitation | Children | Rent/mortgage hardship | Utility hardship | n |
|---|---|---:|---:|---:|---:|---:|
| No → No | White alone | Yes | None | 4.63% (0.48) | 7.11% (0.62) | 31,202 |
| No → No | White alone | Yes | 1+ | 9.56% (2.25) | 16.53% (2.68) | 5,098 |
| No → No | White alone | No | None | 2.51% (0.24) | 3.44% (0.27) | 124,507 |
| No → No | Black alone | Yes | 1+ | 6.02% (2.86) | 16.93% (4.44) | 851 |
| No → No | Black alone | No | 1+ | 8.79% (1.68) | 12.69% (2.15) | 6,323 |
| Yes → Yes | White alone | Yes | None | 8.38% (1.34) | 16.01% (1.72) | 7,179 |
| Yes → Yes | White alone | Yes | 1+ | 22.12% (5.32) | 36.75% (5.56) | 1,324 |
| Yes → Yes | White alone | No | None | 3.58% (1.15) | 10.53% (2.41) | 3,928 |
| Yes → Yes | Black alone | Yes | 1+ | 11.82% (6.19) | 21.27% (7.65) | 494 |
| Yes → Yes | Black alone | No | 1+ | 11.15% (4.11) | 15.33% (4.74) | 1,103 |

## What this adds

### 1. The hardship pattern is intersectional

Within the stable nonrecipient state, the White work-limitation/children cell
has higher utility hardship than the White no-limitation/no-children cell
(16.53% versus 3.44%). Among continued recipients, that comparison is 36.75%
versus 10.53%. The Black cells show a different ordering and wider uncertainty,
which is precisely why a single disability or children average is insufficient.

### 2. Continued receipt is not equivalent to housing or utility security

Among White respondents with a work-limiting condition and children, continued
receipt coexists with 22.12% rent/mortgage hardship and 36.75% utility
hardship. SNAP receipt can protect food access while leaving other budget
obligations exposed. This is a conditional distribution, not evidence that
SNAP caused or failed to cause those outcomes.

### 3. Race does not operate as a universal ranking

The Black continued-recipient work-limitation/children cell has lower point
estimates than the corresponding White cell, but its standard errors are wide
(`n=494`). Other Black cells reverse or narrow that pattern. The safe result is
that the joint distribution differs and requires adequate cell sizes—not that
one racial group has a universal transition or hardship ranking.

### 4. Transition cells are a design signal, not a conclusion

The full output retains `No → Yes` and `Yes → No` cells. Some have only one to
twenty valid records, and their intervals are correspondingly unstable. They
identify where an episode ledger is needed; they do not establish that entry,
exit, or a recorded reason improved or worsened security.

## Arrow status

| Arrow | Status | Safe conclusion |
|---|---|---|
| SNAP transition → following hardship | Time-ordered descriptive association | Hardship shares differ across observed transition states, but selection and field timing prevent a program-effect claim. |
| Race × work limitation × children → hardship pattern | Observed distribution with Fay-BRR uncertainty | The joint social-capacity pattern is not reducible to one demographic or one receipt average. |
| Receipt → restored security | Not established | Continued receipt can coexist with rent, mortgage, or utility hardship. |
| Exit → improved circumstances | Not established | Exit can reflect income, time limits, reporting, family change, or administrative route. |
| Episode → trust, blame, action, or vote | Open | SIPP does not observe the same episode's notice, interpretation, remedy, or political response. |

## Limits

- Person-month records can represent covered members of a SNAP unit; they are
  not household benefit amounts or complete benefit spells.
- “Following month” is record order. Hardship questions have their own
  reference periods and do not prove that a new bill arrived after the SNAP
  transition.
- The work-limitation measure is not a full disability taxonomy, and children
  under 18 are not a care-hours measure.
- Race categories are the SIPP public-use recode and do not replace detailed
  ethnicity or multiracial analysis.
- Fay-BRR intervals describe sampling uncertainty, not causal uncertainty.
- Notice, effort, benefit amount, timing, appeal, correction, food outcome,
  health, debt, dignity, trust, complaint, turnout, vote, and agency response
  remain unmeasured for the same episode.

## Reproduction

```text
python3 scripts/analyze_sipp_snap_transition_outcomes_fay_brr.py \
  --primary /tmp/us-broad-sipp-2025/full-v11/sipp-household-slice.csv \
  --replicate-zip /tmp/us-broad-sipp-2025/rw2025_csv.zip \
  --group-by ERACE_EDISABL_RHNUMU18 \
  --output /tmp/us-broad-sipp-2025/full-v11/snap-transition-outcomes-race-disability-children.json
```

Related: [SNAP transition × work limitation × children](sipp-snap-transition-outcome-disability-children-fay-brr-layer-v1.md),
[SNAP reason × following hardship](sipp-snap-transition-reason-outcome-fay-brr-layer-v1.md),
and the [same-episode implementation specification](same-episode-event-ledger-implementation-v1.md).
