# MEPS 2024 event presence is associated with different household-context surfaces

**Checked:** 2026-09-15  
**Status:** weighted descriptive same-person association; no causal claim  
**Machine record:** [MEPS event-context association](data/us-meps-2024-event-context-association.json)

## Result in one line

In the 2024 HC-256 person file, people with an observed emergency-room or
inpatient event have higher reported shares of medical-bill problems, fair or
poor perceived health, and nonemployment than people without that event type.
Office-visit presence is associated with a much larger health and employment
gradient but almost no difference in reported medical-bill problems. These are
same-year differences shaped by need, age, coverage, selection, and event
intensity—not evidence that the event caused the outcome.

## Bounded comparisons

| Event present? | Medical-bill problem | Fair/poor perceived health | Not employed at R5/3 |
|---|---:|---:|---:|
| Office event present | 7.63% (SE 0.48 pp) | 12.30% (0.70 pp) | 37.72% (0.70 pp) |
| Office event absent | 7.47% (0.73 pp) | 6.35% (0.45 pp) | 25.98% (0.97 pp) |
| ER event present | 13.17% (0.88 pp) | 26.41% (1.10 pp) | 47.67% (1.40 pp) |
| ER event absent | 6.68% (0.46 pp) | 8.27% (0.29 pp) | 32.51% (0.57 pp) |
| Inpatient event present | 10.60% (0.95 pp) | 34.83% (1.79 pp) | 59.54% (2.15 pp) |
| Inpatient event absent | 7.39% (0.49 pp) | 9.23% (0.30 pp) | 32.85% (0.55 pp) |

Shares use the field-specific valid universe and final person weights. Standard
BRR uses the 128 HC-036BRR indicators. Event presence means the annual event
count is greater than zero; it does not mean that the event was unaffordable,
unexpected, or the source of the reported condition.

## What this adds

This is the first same-person context test after the event-linkage work. It
shows that the event surface is not just a payment table: event presence
coexists with different health and employment conditions, and emergency or
inpatient care also coexists with a higher reported medical-bill-problem
share. The office-event comparison is a useful counterexample: care use can
be common without a corresponding difference in the annual bill-problem
measure.

The result therefore supports a segmented interpretation:

```text
observed event type
  -> different need / severity / coverage / selection composition
  -> different same-year health and work context
  -> possible bill pressure signal for acute events
```

The middle arrow is not identified by this cross-tab. Inpatient and ER users
may have been ill before the event, may differ in age and coverage, and may
have received care without paying the full amount themselves. Non-users are
not an equivalent no-need control group.

## What remains open

The annual event indicators do not identify care that was delayed, skipped, or
never sought. The bill-problem item does not identify the bill, amount, date,
actor, or remedy. The employment field is a round-status measure, not a
post-event work-loss record. Nothing here observes borrowing, savings draw,
unpaid care, food or housing tradeoff, recovery, switching, trust, or
political action.

The next decisive test is a field-specific round analysis for the smallest
event family with a defensible reference-period ordering. If the round dates
cannot establish a pre-event and post-event window, this result should remain
the endpoint of the MEPS same-person association lane and be paired with SHED,
SIPP, or administrative records only as separate contextual layers.
