# A prescription event can be followed by mixed health and work transitions

**Status:** bounded same-person MEPS follow-up comparison  
**Checked:** 2026-09-20

## The bounded finding

Among 18,691 MEPS person records with valid three-round ordering, 724 had a
first prescription event strictly inside the R3/1-to-R4/2 window and 17,967
formed the complementary comparison group. In the later R4/2-to-R5/3 clock,
the prescription-event group did not show one simple trajectory:

| Later measure | Prescription event | No event in window |
|---|---:|---:|
| Health worsened | 19.62% (SE 1.79; n=684) | 22.16% (SE 0.46; n=17,553) |
| Fair/poor health at follow-up | 9.47% (SE 1.34; n=684) | 10.85% (SE 0.34; n=17,584) |
| Employment status changed | 13.15% (SE 1.68; n=493) | 9.32% (SE 0.24; n=14,499) |
| Nonemployment onset | 12.81% (SE 3.65; n=140) | 7.11% (SE 0.41; n=6,089) |
| Nonemployment resolved | 11.43% (SE 3.13; n=143) | 5.19% (SE 0.40; n=5,986) |

The later health measures are not higher in this descriptive comparison, while
employment movement and both entry into and exit from nonemployment are more
common in the event group. The small transition cells have wide uncertainty.

## Why it matters

This adds a second clock to the health-cost chain:

```text
prescription event
  -> later health and work status
  -> [open] fill, adherence, treatment continuity, and payment burden
  -> [open] household adaptation, remedy, trust, action, or exit
```

A later health or employment value is an outcome surface, not automatically
recovery. The mixed directions are useful because they resist the easy story
that a prescription event must produce either straightforward deterioration or
straightforward improvement.

## Do not overread

This is a month-ordered descriptive follow-up, not a causal treatment effect.
The prescription event may be downstream of an earlier health need, and the
comparison group may contain events outside the selected window. The data do
not identify prescription fill or non-fill, adherence, treatment completion,
payment or coverage obligation, hours or earnings, household care/time, or
an event-specific institutional remedy. Employment status change is not job
loss, and nonemployment resolution is not restored security.

Read the [prescription-event follow-up method note](../meps-prescription-event-six-month-followup-v1.md)
and [machine-readable record](../../../records/us-meps-prescription-event-six-month-followup-2024.json).
