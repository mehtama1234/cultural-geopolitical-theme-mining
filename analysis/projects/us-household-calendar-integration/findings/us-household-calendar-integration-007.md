# Work-limiting disability status is associated with less paid care, not clearly less reported work prevention

**Status:** official-universe Fay-BRR disability-status finding · **Checked:** 2026-09-13

## The bounded finding

In the 2024-reference-year SIPP data, records with a reported work-limiting
condition show lower paid-care use than records without one (18.418% versus
31.108%). Their reported child-care work-prevention shares are closer (3.310%
versus 3.927%), while the conditional time-lost estimate is too imprecise for
a stable comparison: 20.354% with 96 valid records versus 16.743% with 1,023.

The calculation uses 379,215 selected person-record/month rows, 378,291
positive-weight rows, official disability and child-care status flags, and 240
Fay-BRR replicate weights. Each measure retains its own universe.

## Estimates

| Released disability status | Paid care | Assistance | Work prevented | Time lost* |
|---|---:|---:|---:|---:|
| Work-limiting condition | 18.418% (SE 3.292) | 5.457% (2.350) | 3.310% (1.148) | 20.354% (14.250) |
| No work-limiting condition | 31.108% (1.231) | 6.460% (0.728) | 3.927% (0.506) | 16.743% (4.470) |

*Time lost is conditional on reported work prevention; the condition group has
only 96 valid records and a very wide interval. It is not suitable for fine
ranking.

## What this adds

The result adds a health-related alternative constraint to the care/work map.
Lower paid-care use among people with a work-limiting condition may reflect
resources, employment, household composition, disability-related care needs,
provider access, or different arrangements. The near-overlap in work
prevention shows why a lower paid-care rate cannot be translated directly into
lower care burden or greater schedule freedom.

The disability recode is not a complete measure of health, accommodation,
dependence, or cultural meaning. The comparison is descriptive and does not
identify an effect of disability, care policy, employer practice, or housing.

## End-to-end route under test

```text
health/work limitation and resources
  -> care arrangement, payment, assistance, or unpaid substitution
  -> work opportunity and time loss
  -> health, security, recovery, trust, or collective action
```

This pass strengthens subgroup distribution and uncertainty. It does not
observe a dated care need, provider route, employer accommodation, unpaid
substitution, protected outcome, or later cultural/political meaning.

## Method and limits

The full estimate uses `WPFINWGT`; replicate estimates use `REPWGT1` through
`REPWGT240` under Census’s Fay modified-BRR formula (`G=240`, perturbation
factor `0.5`). Official `ADISABL`, `APAY`, `APAYHELP`, `AWORKMORE`, and
`ATIMELOST` flags and conditional universes were applied. The work-limiting
condition time-lost cell is sparse; zero-width or wide intervals are not proof
of absence or equivalence.

Disability status is repeated on person records and the final person weight is
not a household weight. The result does not establish care need, inaccessible
services, accommodation, causality, recovery, trust, political action, or
cultural change.

## Next test

Use only sufficiently populated intersections with poverty, tenure, race,
region, and child presence, and test direct work accommodation and health/care
outcomes where available. Then define a one-record-per-household rule and seek
a dated trigger/follow-up design for substitution and recovery.

**Evidence status:** reproducible design-based person-weighted disability-status
comparison with explicit sparse-cell limits; causal and complete same-unit
arrows remain open.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)
- [Machine-readable result](../../../records/us-sipp-care-work-disability-official-variance-2024.json)
