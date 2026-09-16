# Prescription delay coexists with poorer perceived health, while employment moves differently

**Status:** provisional MEPS 2024 same-respondent comparison  
**Checked:** 2026-09-16

## Bounded finding

The 2024 MEPS HC-256 person file provides a same-respondent outcome surface for
reported prescription delay. Among valid records, people who reported delaying
a prescription had a higher weighted share reporting poor or fair perceived
health than people reporting no delay:

| Prescription-delay report | Poor/fair perceived health | Employed at final observed round |
|---|---:|---:|
| Yes | 31.8% (SE 2.0; n=675) | 55.1% (SE 2.2; n=675) |
| No | 10.0% (SE 0.3; n=17,799) | 49.3% (SE 0.5; n=17,799) |

The health contrast is substantial descriptively, while the employment
contrast is smaller and points in a different direction. That divergence is
important: prescription delay is not a complete proxy for work incapacity or
one universal household-burden scale.

## Interpretation boundary

This is a same-round association, not a causal prescription-delay effect.
Underlying illness, medication need, insurance, income, age, employment
selection, and other factors may influence both the delay report and the
outcomes. The health field is perceived health at the final observed round;
it is not a clinical recovery measure. Employment at that round is not an
estimate of lost work or restored work.

```text
prescription affordability delay report
  -> same-round health/work outcome surface
  -> treatment continuity, adherence, household substitution, recovery, and remedy remain open
```

The result does not establish that a delayed prescription caused poor health,
that employment protected health, or that a non-delayer obtained needed care.
It does establish a measurable downstream surface that should be preserved
when the atlas describes medication affordability.

## Arrow status

| Arrow | Status | Safe conclusion |
|---|---|---|
| Prescription delay → perceived health | Same-round descriptive association | Delay reporters have a higher poor/fair-health share, with BRR uncertainty |
| Prescription delay → employment | Same-round descriptive association | Employment shares differ modestly and require selection interpretation |
| Delay → clinical adherence or recovery | Open | No fill/use/clinical-follow-up measure is linked |
| Delay → household money/time substitution | Open | No same-episode debt, care, food, housing, or time response is observed |
| Delay → institutional remedy, trust, political action, or exit | Open | Requires later person-level follow-up |

The [machine-readable record](../data/us-meps-2024-prescription-delay-outcomes.json)
preserves the source and script hashes, denominators, estimates, and BRR
intervals. The [reproduction script](../../../../scripts/analyze_meps_prescription_delay_outcomes.py)
defines the valid fields and standard BRR calculation. This record remains
separate from the prescription purchase-event comparison because delay and
purchase are different observation surfaces.

## Next decisive test

Use a longitudinal or event-linked medication file that identifies need,
intended fill, fill/non-fill, reason, adherence, and later clinical and work
continuity. Add household payment, debt, time, and institutional-response
fields before interpreting prescription delay as a mechanism of health or
legitimacy.

## Official sources

- [AHRQ MEPS HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes)
- [AHRQ MEPS HC-036BRR variance file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-036BRR&prfricon=yes)
- [MEPS prescription purchase versus delay comparison](../findings/us-health-cost-household-choice-008.md)
