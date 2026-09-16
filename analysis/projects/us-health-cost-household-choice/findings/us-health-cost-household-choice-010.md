# Prescription-delay reporters show both health improvement and worsening at follow-up

**Status:** provisional MEPS 2024 longitudinal descriptive comparison  
**Checked:** 2026-09-16

## Bounded finding

The MEPS 2024 HC-256 file permits a round-ordered screen: prescription delay
reported in round 4/2, followed by the direction of the person’s perceived
health rating between round 4/2 and round 5/3. Among valid records, delay
reporters show both improvement and worsening rather than a single directional
path.

| Round-4/2 prescription-delay report | Health improved | Health worsened | Health unchanged |
|---|---:|---:|---:|
| Yes | 24.6% (SE 2.3; n=674) | 19.1% (SE 2.0; n=674) | 56.3% (SE 2.5; n=674) |
| No | 20.4% (SE 0.4; n=17,683) | 22.1% (SE 0.5; n=17,683) | 57.5% (SE 0.5; n=17,683) |

The next-round improvement share is higher and worsening share lower among
delay reporters in this descriptive screen, but the group is selected by a
reported affordability/access problem and may differ in underlying illness,
medication need, age, coverage, and treatment intensity. This is not evidence
that delay improved health or that non-delay protected it.

## What this adds to the end-to-end chain

```text
prescription affordability-delay report at t
  -> round-to-round perceived-health direction at t+1
  -> adherence, fill/non-fill, clinical continuity, work, and household response
  -> recovery, remedy, trust, or political action
```

The first arrow is a measured temporal association. The remaining links are
open. A perceived-health rating is not a clinical outcome, and “improved” or
“worsened” is based on an ordinal rating change rather than a dated treatment
response. The mixed directions are therefore a reason to preserve individual
health trajectories, not to claim a universal consequence.

## Method and boundaries

Health improvement is a lower numeric `RTHLTH53` rating than `RTHLTH42`,
worsening is higher, and unchanged is equal; valid codes are 1–5. The
prescription-delay exposure is `DLAYPM42=1` versus `2`. Estimates use
`PERWT24F` and standard MEPS BRR variance from 128 `BRR` flags. The two groups
have separate valid denominators, and the design does not identify a clinical
need, intended prescription, fill/non-fill, adherence, payment timing, or
household burden.

| Arrow | Status | Safe conclusion |
|---|---|---|
| Delay report → later perceived-health direction | Longitudinal descriptive association | Both improvement and worsening occur; the delay group’s composition differs |
| Delay → clinical treatment continuity | Open | No fill/use or clinical pathway is observed |
| Health direction → work, debt, care, or household adaptation | Open | No same-episode downstream response is linked |
| Medication episode → recovery, remedy, trust, action, or exit | Open | Requires a richer event/person follow-up |

The [machine-readable record](../data/us-meps-2024-prescription-delay-health-direction.json)
preserves hashes, valid denominators, estimates, intervals, and boundaries. The
[reproduction script](../../../../scripts/analyze_meps_prescription_delay_health_direction.py)
defines the ordinal direction and BRR calculation. It complements, but does
not replace, the purchase-event and same-round outcome comparisons.

## Next decisive test

Link an identified medication need and intended fill to fill/non-fill reason,
payment, adherence, clinical outcome, work/time, and household financial
follow-up. Until then, report prescription delay and later perceived-health
direction as separate, selection-sensitive endpoints.

## Official sources

- [AHRQ MEPS HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes)
- [AHRQ MEPS HC-036BRR variance file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-036BRR&prfricon=yes)
- [Prescription delay and same-round health/work outcomes](us-health-cost-household-choice-009.md)
