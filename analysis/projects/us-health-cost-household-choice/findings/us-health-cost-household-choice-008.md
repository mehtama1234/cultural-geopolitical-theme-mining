# Prescription purchase records do not represent the full affordability-risk population

**Status:** provisional MEPS 2024 person/event-linked comparison  
**Checked:** 2026-09-16

## Bounded finding

The 2024 MEPS HC-254A prescription event file can be linked exactly to the
HC-256 person file. Among 19,140 HC-256 person records, 12,135 have at least
one matching recorded prescription event. Using the HC-256 person weight and
the released 128 BRR flags, reported prescription delay and inability to afford
prescriptions are higher among people with a recorded purchase event than
among people without one:

| HC-254A event status | Prescription delayed | Could not afford prescription |
|---|---:|---:|
| Recorded purchase | 4.44% (SE 0.21; n=11,979) | 3.70% (SE 0.19; n=11,979) |
| No recorded purchase | 1.34% (SE 0.19; n=6,704) | 0.99% (SE 0.16; n=6,704) |

The interval estimates are 4.02–4.86% and 3.33–4.07% for the recorded-
purchase group, versus 0.98–1.71% and 0.67–1.31% for the no-recorded-purchase
group. These are descriptive person-level comparisons, not a purchase effect.

## What this adds to the health-cost chain

The result makes the event-selection problem measurable:

```text
prescription event observed
  -> payment channel and person context observed
  -> reported affordability delay can still be present
  -> people without an observed purchase are a mixed group
  -> forgone fill, adherence, health recovery, work/time, and remedy remain open
```

An observed purchase can coexist with reported delay or inability to afford a
prescription, potentially because the measures refer to different medicines,
times, or episodes. Conversely, absence of a recorded purchase cannot be
called a forgone fill without a need/intent measure. The comparison therefore
supports selection-aware interpretation, not a conclusion that purchasers are
more financially burdened or that non-purchasers are safer.

## Method and boundaries

The event indicator is whether the person-panel key appears in HC-254A; it does
not count unique medicines or establish a first purchase. `DLAYPM42` and
`AFRDPM42` are HC-256 person-level reported annual fields with their own valid
universes. The estimates use `PERWT24F` and standard MEPS BRR variance from
HC-036BRR (`BRR1`–`BRR128`). Person-level weighting is not household weighting,
and the event group is selected on an observed purchase.

| Arrow | Status | Safe conclusion |
|---|---|---|
| Recorded prescription event → affordability-delay report | Observed descriptive comparison | Delay reports differ between event-selected and no-event groups |
| Prescription need → purchase or forgone fill | Open | No common need/intent denominator is available |
| Payment → adherence or treatment continuity | Open | Purchase and payment do not establish use or continuation |
| Cost/affordability → health, work, debt, or household substitution | Open | No dated episode and downstream follow-up are linked |
| Medication episode → remedy, trust, political action, or exit | Open | Requires same-person event follow-up with those outcomes |

The [machine-readable record](../data/us-meps-2024-prescription-purchase-delay.json)
preserves the hashes, event-selection definition, denominators, estimates, and
uncertainty. The [reproduction script](../../../../scripts/analyze_meps_prescription_purchase_delay.py)
defines the person/event join and BRR calculation. The raw MEPS files remain
outside Git.

## Next decisive test

Acquire a same-person medication episode with intended prescription, fill or
non-fill, reason, payment, adherence, clinical continuity, and follow-up
health/work fields. Until then, keep purchase/payment exposure and
affordability-delay reports as separate but linked surfaces.

## Official sources

- [AHRQ MEPS HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes)
- [AHRQ MEPS HC-254A prescribed-medicine file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254A&prfricon=yes)
- [MEPS prescription reproduction audit](../meps-2024-prescription-reproduction-audit-2026-09-16.md)
