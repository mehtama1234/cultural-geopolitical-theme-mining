# Month-ordered MEPS events sharpen—but do not close—the follow-up link

**Checked:** 2026-09-15  
**Status:** month-ordered descriptive transition screen; no causal claim  
**Machine record:** [MEPS month-ordered event follow-up](data/us-meps-2024-month-ordered-event-followup.json)

## Result

Using AHRQ’s documented relationship between round reference-period end dates
and interview dates for most people, each person’s first dated event was
classified relative to the R4/2 endpoint month. Acute events occurring before
the endpoint are associated with higher R4/2 fair/poor health, medical-bill
problems, and nonemployment than people without that event family. Inpatient
events show the strongest health and employment gradients. Same-month groups
are retained but are inherently ambiguous because the event day is not public.

| First event timing | ER bill problem | ER fair/poor health | Inpatient fair/poor health | Inpatient not employed |
|---|---:|---:|---:|---:|
| Before R4/2 endpoint month | 14.50% (SE 1.10 pp) | 26.53% (1.18 pp) | 34.61% (2.28 pp) | 58.29% (2.24 pp) |
| Same endpoint month | 14.73% (3.00 pp) | 20.31% (3.41 pp) | 41.19% (5.56 pp) | 73.55% (5.43 pp) |
| No event | 6.68% (0.46 pp) | 8.26% (0.32 pp) | 9.07% (0.31 pp) | 31.99% (0.55 pp) |

For office events, the bill-problem comparison is a counterexample: 7.74%
before the endpoint versus 7.47% with no office event. Office-event presence
still has a health and employment gradient, but utilization does not map
uniformly onto reported payment difficulty.

## What the ordering adds

This pass is stronger than an unconditioned annual event cross-tab because it
uses the first event month and a person-specific round endpoint. It identifies
candidate temporal ordering and separates before, same-month, after, and no-
event groups. It does not convert the outcome into a post-event measure. A
round field may summarize a reference period that includes the event, and the
event may be a consequence of pre-existing health or work conditions.

The safe interpretation is therefore:

```text
month-ordered event presence
  -> different same-round health, work, and bill-problem context
  -> candidate cases for a stronger event study
```

The arrows from event to outcome remain observational. Acute care can be a
marker of prior need, severity, age, employment selection, or access rather
than the cause of the later-looking status.

## Remaining end-to-end gap

The data still do not identify the bill or care decision, available
alternative, delay or foregoing, borrowing, savings draw, unpaid care,
work-time sacrifice, recovery, institutional remedy, trust, switching, or
political action. Same-month records cannot be ordered at the day level, and
the after-event group is not a causal control group.

The next test should add a documented pre-round value where the event occurs
strictly before the endpoint and report a transition only when the field’s
universe and timing support it. If no stronger window is available, this
month-ordered surface is the correct MEPS endpoint and the missing household
adaptation stages must be pursued through compatible SHED, SIPP, PSID, or
administrative evidence without pretending those records are the same people.
