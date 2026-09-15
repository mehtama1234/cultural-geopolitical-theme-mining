# Regional SIPP differences are sharper for reported work prevention than paid-care use

**Status:** official-universe Fay-BRR regional finding · **Checked:** 2026-09-13

## The bounded finding

Paid child-care use is similar across the four Census regions in the 2024-
reference-year SIPP data: 29.308% in the Midwest, 29.629% in the Northeast,
29.727% in the West, and 30.824% in the South. Reported child-care work
prevention varies more, from 2.990% in the Northeast to 4.813% in the Midwest.

Payment assistance ranges from 5.699% in the West to 7.494% in the Northeast.
Time-lost estimates are conditional, small-cell, and wide; they are not used
for fine regional ranking.

## Estimates

| Region | Paid care | Assistance | Work prevented | Time lost* |
|---|---:|---:|---:|---:|
| Northeast | 29.629% (SE 2.920) | 7.494% (1.843) | 2.990% (0.877) | 15.895% (9.626) |
| Midwest | 29.308% (2.585) | 6.763% (1.640) | 4.813% (1.320) | 19.649% (11.333) |
| South | 30.824% (1.855) | 6.125% (1.074) | 3.797% (0.605) | 16.994% (6.684) |
| West | 29.727% (2.126) | 5.699% (1.078) | 3.831% (0.869) | 14.755% (6.940) |

*Time lost is conditional on reported work prevention; valid records are 132,
228, 447, and 312 respectively. Intervals are wide.

## What this adds

The regional screen is a counterexample to treating paid-care incidence as a
complete place-level care story. Similar paid-care shares coexist with more
regional variation in reported work prevention, which may reflect household
resources, child-care supply, employment, schedule control, housing, or
composition. The SIPP fields cannot identify which mechanism explains the
pattern.

Region is context, not a causal exposure. Local provider adequacy, prices,
travel, employer practices, and household alternatives require place-matched
sources and a stronger design.

## End-to-end route under test

```text
place, resources, and care arrangement
  -> paid care, assistance, or unpaid substitution
  -> work opportunity and time loss
  -> household security, health, recovery, trust, or action
```

This pass strengthens geographic distribution and uncertainty. It does not
observe local provider capacity, a dated care need, employer flexibility,
unpaid substitution, protected outcomes, or later cultural/political meaning.

## Method and limits

The full estimate uses `WPFINWGT`; replicate estimates use `REPWGT1` through
`REPWGT240` under Census’s Fay modified-BRR formula (`G=240`, perturbation
factor `0.5`). Official `TEHC_REGION`, `APAY`, `APAYHELP`, `AWORKMORE`, and
`ATIMELOST` flags and conditional universes were applied. All fields are
person-weighted, and household fields are not household prevalence estimates.

The regional comparison is descriptive, not a provider, price, employer,
housing, or child-care causal estimate. It does not establish recovery, trust,
political action, or cultural change.

## Next test

Join region or more precise place context to provider supply, travel, wages,
housing, and work schedules where compatible dates and units exist. Retain
income, tenure, disability, race, and child-presence moderators rather than
reading the regional average as a local mechanism.

**Evidence status:** reproducible design-based person-weighted regional
comparison with explicit conditional and small-cell boundaries; causal and
complete same-unit arrows remain open.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)
- [Machine-readable result](../../../records/us-sipp-care-work-region-official-variance-2024.json)
