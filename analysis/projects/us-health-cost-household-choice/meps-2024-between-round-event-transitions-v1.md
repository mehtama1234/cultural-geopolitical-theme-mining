# MEPS inter-round event windows reveal baseline selection before follow-up

**Checked:** 2026-09-15  
**Status:** month-ordered descriptive transition screen; no causal claim  
**Machine record:** [MEPS inter-round transitions](data/us-meps-2024-between-round-event-transitions.json)

## Result

For people whose first event occurred strictly between their R3/1 and R4/2
reference-period endpoint months, acute-event groups show higher R4/2
fair/poor health, medical-bill problems, and nonemployment than the broad
comparison group without an event in that window. The event groups also show
substantially worse health and employment at R3/1, before the inter-round
event. That baseline difference is direct evidence of selection and prevents
the follow-up contrast from being read as an event effect.

| Inter-round event group | Baseline fair/poor health | R4/2 fair/poor health | Health worsened | R4/2 bill problem |
|---|---:|---:|---:|---:|
| ER event window | 24.29% | 27.05% | 29.02% | 15.14% |
| No ER event in window | 11.01% | 9.66% | 21.92% | 7.19% |
| Inpatient event window | 28.99% | 33.67% | 31.42% | 11.13% |
| No inpatient event in window | 11.27% | 10.00% | 22.06% | 7.52% |

Office events provide a counterexample. The office-event group had 9.34%
fair/poor health at baseline and 9.26% at R4/2, compared with 12.19% and
10.84% in the no-event-window group; its bill-problem shares were 8.01% and
7.52%. Utilization and payment difficulty therefore do not move as one
universal burden measure.

## What this closes

This is the strongest MEPS timing screen completed so far. It preserves a
baseline endpoint before a strictly inter-round event month and a follow-up
endpoint after it, excluding same-month boundary cases. It shows that acute
events are embedded in prior health and employment differences, and that
later bill-problem and health differences persist without pretending the event
created them.

The safe chain is:

```text
pre-existing health/work selection
  -> inter-round observed care event
  -> different R4/2 health, work, and bill-problem context
```

The event-to-outcome arrow remains open because need, severity, access,
coverage, age, and prior conditions are not fully controlled here.

## Remaining end-to-end gap

The public-use extract still does not identify the triggering need or bill,
available alternative, delay or foregoing, borrowing, savings draw, unpaid
care, work-time sacrifice, recovery, verified institutional remedy, trust,
switching, or political action. Event timing is month-level, and the no-event
window group is not a causal control group.

The next step is to use the baseline/follow-up structure for a prespecified
subgroup or event severity comparison, or to pair this MEPS result with SHED
or SIPP evidence on care choices and adaptation as separate source layers.
