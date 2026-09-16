# Month-ordered MEPS events sharpen selection without proving recovery

## The finding

The 2024 MEPS public-use files allow a bounded timing screen: classify each
person's first office, emergency-room, or inpatient event as occurring before,
in, or after the person's R4/2 reference-period endpoint month, then compare
R4/2 health, employment, and medical-bill context. This is stronger than an
unconditioned event cross-tab because it preserves a person-specific month
ordering. It still does not establish that the event caused the later-looking
outcome.

## Full timing surface

| First event family | Timing | n | Bill problem | Fair/poor health | Not employed |
|---|---|---:|---:|---:|---:|
| Office | Before endpoint | 13,002 | 7.74% | 12.26% | 37.39% |
| Office | Same endpoint month | 533 | 4.44% | 8.68% | 34.45% |
| Office | After endpoint | 867 | 7.88% | 5.77% | 26.54% |
| Emergency room | Before endpoint | 2,165 | 14.50% | 26.53% | 46.66% |
| Emergency room | Same endpoint month | 207 | 14.73% | 20.31% | 45.26% |
| Emergency room | After endpoint | 551 | 6.97% | 19.03% | 47.06% |
| Inpatient | Before endpoint | 1,004 | 11.96% | 34.61% | 58.29% |
| Inpatient | Same endpoint month | 103 | 9.89% | 41.19% | 73.55% |
| Inpatient | After endpoint | 308 | 6.21% | 25.80% | 53.43% |

Percentages are weighted shares; outcome-specific valid denominators differ.
The same-month cells cannot establish event-before-outcome ordering. The
after-event cells describe R4/2 context before the later event, not recovery.
For reference, no-event groups are 7.47% bill-problem/7.07% fair-poor-health
for office, 6.68%/8.26% for emergency-room, and 7.39%/9.07% for inpatient.
The near-flat office bill contrast remains a counterexample: utilization does
not map uniformly onto household payment trouble.

## What the timing adds

```text
event month relative to survey endpoint
  -> distinct health, work, and bill-context surfaces
  -> selected cases for a stronger episode design
```

The event month is not an exact event day, and the R4/2 fields may summarize a
reference period that overlaps the event. Acute utilization may be a marker of
pre-existing need, severity, age, employment selection, access, or coverage.
The result therefore documents temporal ordering and selection, not a treatment
effect, household recovery, or post-event burden.

The same output retains same-month and after-event groups. Same-month records
are inherently ambiguous; after-event records are not a causal control group.
Those groups are kept in the machine output rather than silently discarded so
the boundary remains inspectable.

## What remains open

MEPS still does not link this event to a bill or claim identifier, amount owed,
payment due date, feasible alternative, care delay or substitution, borrowing,
savings draw, unpaid care, work-time sacrifice, remedy, trust, switching, or
political action. The next decisive design needs a dated need or bill, coverage
and alternatives, a care decision, protected and sacrificed outcomes, and a
follow-up remedy or recovery measure.

## Reproduction

The underlying screen and its documented field/timing rules are in the
[month-ordered method note](../meps-2024-month-ordered-event-followup-v1.md).
The machine output is [preserved here](../data/us-meps-2024-month-ordered-event-followup.json),
and the canonical trend record is [here](../../../records/us-meps-2024-month-ordered-event-followup.json).
The result uses positive `PERWT24F` and 128 MEPS BRR replicates; it claims no
design-based causal estimate.

## Reading rule

Read a month-ordered event as evidence that event families occupy different
health, work, and bill contexts—not as evidence that the event caused the
context or that recovery followed. Keep the office counterexample and the
same-month ambiguity visible.
