# MEPS prescription events add a dated medication-to-household-response layer v1

**Checked:** 2026-09-16  
**Status:** same-person month-ordered descriptive comparison; not causal

## Bounded finding

Using the already-local MEPS 2024 files, the existing dated event screen now
includes prescriptions. It selects each person's first valid HC-254A
prescription event strictly between the person's R3/1 and R4/2 endpoint
months, then compares that event-window group with the complementary
round-order-valid group.

Of 18,723 round-order-valid person records, 1,773 had an in-window prescription
event. The event-window group had a weighted mean self/family payment of
$12.76 for the first recorded event; 28.8% of those event-window events had
zero recorded self/family payment.

| R4/2 outcome | Prescription event window | Complementary round-valid group |
|---|---:|---:|
| Cost-related care delay | 8.09% (SE 0.73; n=1,755) | 6.45% (SE 0.29; n=16,633) |
| Medical bill problem | 8.82% (SE 0.74; n=1,758) | 7.48% (SE 0.49; n=16,657) |
| Medical debt | 19.45% (SE 1.14; n=1,743) | 15.17% (SE 0.68; n=16,471) |
| Debt collector contact | 15.03% (SE 1.24; n=1,750) | 13.08% (SE 0.67; n=16,609) |
| Not employed at R4/2 | 37.53% (SE 1.78; n=1,523) | 33.42% (SE 0.59; n=13,740) |

The screen places a dated prescription event before a later round-level
household context. It does not establish that the prescription caused the
displayed burden: the event may follow a pre-existing need, and the
complementary group may contain events outside the window or no observed
event. The payment field is an event payment component, not the amount owed,
deductible, total household burden, or forgone-care cost.

## What this adds to the broad end-to-end goal

```text
dated prescription event
  -> observed event payment component
  -> later care-delay, bill, debt, collection, and work-status context
  -> [open] fill/adherence and treatment continuity
  -> [open] household time/money substitution and recovery
  -> [open] remedy, trust, political action, switching, or exit
```

This is a stronger dated event spine than an annual purchase-presence flag,
and it adds another health-cost route to the atlas. It still stops before the
claim-level mechanism: intended medication, fill or non-fill, dose, coverage
rule, payment obligation, adherence, clinical outcome, household alternative,
and remedy are not linked here.

## Interpretation boundaries

- `RXBEGYRX` and `RXBEGMM` provide month-level timing; the first event is not
  necessarily the triggering need or the most consequential prescription.
- `RXSF24X` is self/family payment for the recorded event, not total price,
  balance, insurance liability, or unpaid obligation.
- R4/2 outcomes are round-level person measures and do not identify the event's
  claim, medication, bill, or treatment continuation.
- The comparison group is not a no-need or no-prescription counterfactual.
- Employment status is a level indicator, not job loss, hours, earnings,
  schedule control, or work causation.
- No remedy, recovery, trust, attribution, political action, switching, or exit
  outcome is measured.

## Next decisive join

The next record should link intended prescription need to fill/non-fill reason,
coverage and payment obligation, adherence or treatment continuity, a dated
household money/time response, and later remedy or recovery. Until then, the
safe claim is a month-ordered event-to-context comparison with selection and
timing limits.

## Reproduction

Run the existing event-screen script with the already-local prescription file:

```text
python3 scripts/analyze_meps_dated_cascade_event_screen.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  /tmp/cgtm-meps-2024/h36brr/h36brr24.dta \
  --office-file /tmp/cgtm-meps-2024/events/h254g.dta \
  --emergency-room-file /tmp/cgtm-meps-2024/events/h254e.dta \
  --inpatient-file /tmp/cgtm-meps-2024/events/h254d.dta \
  --prescription-file /tmp/cgtm-meps-2024/events/h254a.dta \
  --output /tmp/meps-dated-cascade-prescription.json
```

The compact committed result is [the machine-readable prescription layer](data-meps-prescription-event-cascade-2024.json).
The extended script is [the dated event-screen implementation](../../../scripts/analyze_meps_dated_cascade_event_screen.py).

**Evidence status:** reproduced month-ordered prescription-event-to-household
context screen; no causal, claim-level, recovery, trust, political-action, or
exit result.
