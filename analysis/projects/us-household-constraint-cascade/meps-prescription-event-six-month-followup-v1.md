# Prescription events and the later health/work clock v1

**Checked:** 2026-09-16  
**Status:** same-person month-ordered follow-up comparison; not recovery or causal effect

## Bounded finding

The prescription-event group from the dated MEPS screen can be carried to the
R5/3 follow-up only for people with valid three-round ordering. Of 18,691
round-order-valid people, 724 had a first prescription event strictly inside
the R3/1-to-R4/2 window; 17,967 formed the complementary group.

| Later-clock measure | Prescription event window | No event in window |
|---|---:|---:|
| Health worsened, R4/2→R5/3 | 19.62% (SE 1.79; n=684) | 22.16% (SE 0.46; n=17,553) |
| Fair/poor health at R5/3 | 9.47% (SE 1.34; n=684) | 10.85% (SE 0.34; n=17,584) |
| Employment status changed, R4/2→R5/3 | 13.15% (SE 1.68; n=493) | 9.32% (SE 0.24; n=14,499) |
| Nonemployment onset | 12.81% (SE 3.65; n=140) | 7.11% (SE 0.41; n=6,089) |
| Nonemployment resolved | 11.43% (SE 3.13; n=143) | 5.19% (SE 0.40; n=5,986) |

The event-window group therefore does not have one simple later trajectory:
health worsening is not higher in this descriptive screen, while employment
status movement and both nonemployment entry and resolution are higher. The
small transition cells have wide uncertainty and should not be interpreted as
recovery, harm, or a treatment effect.

## What this adds to the broad goal

```text
dated prescription event
  -> R4/2 care, debt, bill, collection, and work context
  -> R5/3 health and employment level/transition context
  -> [open] adherence and treatment continuity
  -> [open] household adaptation and verified recovery
  -> [open] remedy, trust, political action, switching, or exit
```

This adds a second clock to the prescription route and preserves mixed
directions rather than forcing a single story. R5/3 is a later observation,
not a verified one-, three-, or six-month recovery from the event. The event
may be downstream of an earlier health need, and the comparison group may
contain events outside the window.

## Boundaries

- Prescription timing is month-level and uses the first valid event only.
- The analysis does not identify intended medication need, fill/non-fill,
  adherence, treatment completion, or clinical continuity.
- R4/2 and R5/3 health/work fields are person-round outcomes, not claim-level
  outcomes tied to the prescription.
- Health resolution is defined as fair/poor at R4/2 followed by better-than-
  fair/poor at R5/3; it is not clinical recovery.
- Employment transitions are status changes, onset, and resolution, not job
  loss, hours, earnings, schedule control, or household security.
- No remedy, recovery, trust, attribution, political action, switching, or exit
  endpoint is measured.

## Next decisive join

The next medication record should contain intended need, prescription identity,
fill/non-fill reason, payment and coverage obligation, adherence or treatment
continuity, and an event-specific household money/time and remedy follow-up.
Until then, report the two-clock result as selected descriptive context.

## Reproduction

Use the optional prescription argument in the existing follow-up script:

```text
python3 scripts/analyze_meps_event_six_month_followup.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  /tmp/cgtm-meps-2024/h36brr/h36brr24.dta \
  --office-file /tmp/cgtm-meps-2024/events/h254g.dta \
  --emergency-room-file /tmp/cgtm-meps-2024/events/h254e.dta \
  --inpatient-file /tmp/cgtm-meps-2024/events/h254d.dta \
  --prescription-file /tmp/cgtm-meps-2024/events/h254a.dta \
  --output /tmp/meps-event-six-month-prescription.json
```

The compact committed result is [the machine-readable follow-up layer](data-meps-prescription-event-six-month-followup-2024.json).
The implementation is [the six-month follow-up script](../../../scripts/analyze_meps_event_six_month_followup.py).

**Evidence status:** reproduced later-clock descriptive follow-up; not a
claim-level treatment, recovery, causal, trust, political-action, or exit
result.
