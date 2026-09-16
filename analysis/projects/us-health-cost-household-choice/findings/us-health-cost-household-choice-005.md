# Month-ordered MEPS events sharpen selection without proving recovery

## The finding

The 2024 MEPS public-use files allow a bounded timing screen: classify each
person's first office, emergency-room, or inpatient event as occurring before,
in, or after the person's R4/2 reference-period endpoint month, then compare
R4/2 health, employment, and medical-bill context. This is stronger than an
unconditioned event cross-tab because it preserves a person-specific month
ordering. It still does not establish that the event caused the later-looking
outcome.

## Before-endpoint event groups

| First event family before endpoint | Bill problem | Fair/poor health | Not employed | No-event bill problem |
|---|---:|---:|---:|---:|
| Office (n=13,002) | 7.74% | 12.26% | 37.39% | 7.47% |
| Emergency room (n=2,165) | 14.50% | 26.53% | 46.66% | 6.68% |
| Inpatient (n=1,004) | 11.96% | 34.61% | 58.29% | 7.39% |

Percentages are weighted shares; outcome-specific valid denominators differ.
The no-event column is a broad comparison group, not a causal counterfactual.
The acute-event groups show markedly worse health and employment context, while
the office-event bill contrast is nearly flat. That office counterexample is
important: utilization does not map uniformly onto household payment trouble.

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
