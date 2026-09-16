# Reported child-care-related work time loss is measurable only in a selected conditional universe

**Status:** provisional official-universe Fay-BRR finding  
**Checked:** 2026-09-16

## Bounded finding

The SIPP `ETIMELOST` field supplies a direct time-sacrifice amount, but only
for reference parents whose child-care arrangements prevented working or
working more (`EWORKMORE=1`) and whose time-loss status is valid. After applying
the official status gates, 560 person-month records remain from 379,215 rows;
all 560 match the 240-replicate archive.

| Current resource endpoint | Valid records | Mean reported work time lost | Fay-BRR SE | Approx. 95% interval |
|---|---:|---:|---:|---:|
| Below 1× poverty | 170 | 8.43 hours | 1.70 | 5.10–11.75 |
| 4× poverty or more | 390 | 24.40 hours | 7.25 | 10.18–38.62 |

The high-resource point estimate is larger, but this is not a ranking of who
experiences greater care burden. The cells condition on having reported both
care-related work prevention and a valid time-loss amount. Resource groups may
differ in care arrangements, job schedules, reporting, ability to absorb or
avoid time loss, and the type of reference parent represented. The wide
high-resource interval is part of the result.

The reporting type also changes across the two endpoints. The lower-resource
selected records are predominantly reported in days (54.1%), while the
higher-resource selected records are more often reported in hours (55.7%).
Weeks account for 21.0% and 3.9%, respectively. These are shares of the same
conditional time-loss universe, not evidence that one group experienced more
care burden; reporting scale, recall, work arrangements, and selection may all
contribute.

| Resource endpoint | Hours | Days | Weeks |
|---|---:|---:|---:|
| Below 1× poverty | 24.9% (SE 8.4) | 54.1% (SE 10.5) | 21.0% (SE 7.8) |
| 4× poverty or more | 55.7% (SE 9.3) | 40.4% (SE 8.9) | 3.9% (SE 2.8) |

## What this adds

Compared with the binary `EWORKMORE` screen, `ETIMELOST` makes the sacrificed
currency explicit:

```text
child-care arrangement
  -> work prevented
  -> reported hours lost
  -> possible earnings, schedule, household, or care trade-off
  -> later recovery, health, trust, or institutional response
```

The first two arrows are observed only inside the selected reference-parent
universe. The following arrows remain open. In particular, the result cannot
say whether time loss was paid or unpaid, whether another household member
protected work, whether the lost time was later recovered, or whether the
arrangement reflected provider price, availability, schedule mismatch, or
employer policy.

## Universe and timing boundary

`ETIMELOST` describes childcare-related work time lost during the fall
reference year; it is not a monthly diary total. The resource band is attached
to the SIPP person-month record, but that does not turn the care measure into a
dated bill or monthly event. Records without a valid time-loss status are not
recoded as zero, and non-`EWORKMORE` respondents do not provide a valid
no-prevention comparison for this amount.

| Arrow | Status | Safe conclusion |
|---|---|---|
| Resources → reported time-loss amount | Conditional descriptive comparison | Two resource endpoints have different selected conditional means, with uncertainty |
| Child-care constraint → actual care minutes or schedule control | Open | Neither is directly measured here |
| Time loss → earnings, food, housing, health, or work continuity | Open | No same-event downstream outcome is linked |
| Time loss → recovery, remedy, trust, political action, or exit | Open | Requires a dated follow-up design |

The [machine-readable record](../data/sipp-childcare-time-loss-resource-2024.json)
preserves the input hashes, matched counts, estimates, and conditional
boundary. The [analysis script](../../../../scripts/analyze_sipp_childcare_time_loss_resource.py)
defines the official status filtering, resource grouping, and Fay-BRR mean.

## Next decisive test

Pair this direct time-loss amount with desired and actual hours, schedule
control, paid and unpaid care, provider/price information, and a later
earnings, health, food, housing, or work-continuity measure for the same
person/family. Preserve both protected cases and time-loss cases, and retain a
dated event identifier before interpreting the amount as a mechanism.

## Official source

- [Census 2025 SIPP data and documentation](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP childcare time-loss gate](../sipp-utility-time-loss-following-gate-v1.md)
