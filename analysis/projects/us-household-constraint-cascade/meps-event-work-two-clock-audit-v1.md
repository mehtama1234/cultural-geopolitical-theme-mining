# MEPS event-to-work two-clock audit v1

**Checked:** 2026-09-16  
**Status:** aligned descriptive synthesis; not a row-level merged panel

## Purpose

The dated MEPS event screen supplies an R4/2 nonemployment level after a first
event in the strict R3/1–R4/2 window. The existing six-month follow-up carries
the same event-family/date rule to R5/3 employment levels and conditional
transitions. This audit puts those clocks next to one another while preserving
that the R5-valid panel is smaller and is not asserted to be the identical row
set used by the R4 screen.

## Results

| Event family | R4/2 nonemployment: event / comparison | R5/3 nonemployment: event / comparison | R4→R5 status change: event / comparison | Nonemployment resolved: event / comparison | Nonemployment onset: event / comparison |
|---|---:|---:|---:|---:|---:|
| Office | 33.35% / 33.91% | 35.24% / 34.59% | 10.07% / 9.35% | 5.41% / 5.35% | 8.99% / 6.91% |
| Emergency room | 47.62% / 32.98% | 49.01% / 33.84% | 11.49% / 9.35% | 3.58% / 5.52% | 6.67% / 7.32% |
| Inpatient | 60.13% / 33.03% | 62.18% / 33.90% | 11.83% / 9.40% | 2.61% / 5.51% | 6.34% / 7.31% |

The event and comparison values are weighted percentages; each outcome has its
own valid denominator and BRR uncertainty in the source outputs. The acute
event groups begin with much higher R4/2 nonemployment, remain higher at R5/3,
and show mixed resolution/onset patterns. The office level is nearly flat at
R4/2, while its onset estimate is higher than the comparison. These are
descriptive persistence and transition surfaces, not evidence that the event
caused employment loss or that later status is recovery.

## What this adds to the broad goal

This is a sharper material → work → later-status arrow than a single
cross-sectional employment tab: it distinguishes an immediate endpoint level
from a later level and from conditional transition directions. It still does
not observe the initiating need, usable alternative, bill obligation, hours or
earnings trade-off, provider/employer response, remedy, household adaptation,
trust, political action, or exit. The next decisive join remains a claim- or
bill-level episode ledger with those fields.

## Reproduction

```text
python3 scripts/build_meps_event_work_two_clock_audit.py \
  --r4 analysis/projects/us-household-constraint-cascade/data-meps-dated-cascade-event-screen-2024.json \
  --r5 analysis/projects/us-household-constraint-cascade/data-meps-event-six-month-followup-2024.json \
  --output analysis/projects/us-household-constraint-cascade/data-meps-event-work-two-clock-audit-2024.json
```

See the [R4/2 event screen](meps-dated-cascade-event-screen-v1.md) and the
[R5/3 follow-up](meps-event-six-month-followup-v1.md) for source hashes,
event-window definitions, and full outcome denominators.
