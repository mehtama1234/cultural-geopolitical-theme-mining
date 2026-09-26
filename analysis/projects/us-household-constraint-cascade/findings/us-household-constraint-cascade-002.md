# A prescription event can sit beside payment, debt, and work pressure

**Status:** bounded month-ordered MEPS event-to-household-context comparison  
**Checked:** 2026-09-20

## The bounded finding

Using MEPS 2024 person records with valid round ordering, 1,773 people had a
first prescription event strictly between their R3/1 and R4/2 endpoint months;
16,950 formed the complementary round-valid group. The first recorded event's
weighted mean self/family payment was $12.76, and 28.8% of event-window events
had zero recorded self/family payment.

At the later R4/2 round, the event-window group also showed higher contextual
rates of cost-related care delay, medical debt, debt-collector contact, and
nonemployment:

| Later/context measure | Prescription event | Complementary group |
|---|---:|---:|
| Cost-related care delay | 8.09% (SE 0.73; n=1,755) | 6.45% (SE 0.29; n=16,633) |
| Medical bill problem | 8.82% (SE 0.74; n=1,758) | 7.48% (SE 0.49; n=16,657) |
| Medical debt | 19.45% (SE 1.14; n=1,743) | 15.17% (SE 0.68; n=16,471) |
| Debt-collector contact | 15.03% (SE 1.24; n=1,750) | 13.08% (SE 0.67; n=16,609) |
| Not employed at R4/2 | 37.53% (SE 1.78; n=1,523) | 33.42% (SE 0.59; n=13,740) |

## Why it matters

This gives the health-cost route a dated material-pressure layer:

```text
prescription event
  -> recorded event payment component
  -> care delay, bill, debt, collector, and work-status context
  -> [open] fill, adherence, treatment continuity, and household substitution
  -> [open] remedy, recovery, trust, action, switching, or exit
```

The key insight is not that a prescription caused debt. It is that a health
event can appear alongside several different household currencies at once:
cash payment, delayed care, debt, collection pressure, and employment status.
Those currencies should not be collapsed into one “medical burden” measure.

## Do not overread

This is a selected, month-ordered descriptive comparison, not a causal effect.
The prescription may follow an earlier health need, and the complementary
group is not a no-need or no-prescription control. The payment field is not the
total price, deductible, insurance liability, unpaid balance, or forgone-care
cost. Round-level outcomes are not claim-specific, and the data do not show
fill/non-fill, adherence, treatment continuity, household time substitution,
remedy receipt, recovery, trust, political action, switching, or exit.

Read the [prescription cascade method note](../meps-prescription-event-cascade-v1.md),
[combined event/work record](../../../records/us-meps-dated-medical-event-household-work-2024.json),
and [machine-readable cascade output](../data-meps-prescription-event-cascade-2024.json).
