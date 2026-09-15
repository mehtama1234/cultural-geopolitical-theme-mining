# SIPP care and work measures differ by race group, but the recode is not cultural meaning

**Status:** official-universe Fay-BRR race-group finding · **Checked:** 2026-09-13

## The bounded finding

In the 2024-reference-year SIPP data, Black-alone records show higher reported
child-care assistance (10.734%) and work prevention (5.156%) than White-alone
records (5.029% and 3.702%), while White-alone records show higher paid-care
use (30.275% versus 24.216%). Asian-alone and residual-category estimates are
less precise, especially for reported time lost.

The calculation uses 379,215 selected person-record/month rows, 378,291
positive-weight rows, official race and child-care status flags, and 240
Fay-BRR replicate weights. Payment and assistance retain the child-care-use
universe; work prevention and time lost retain their own conditional universes.

## Estimates

| Released race group | Paid care | Assistance | Work prevented | Time lost* |
|---|---:|---:|---:|---:|
| White alone | 30.275% (SE 1.268) | 5.029% (0.600) | 3.702% (0.511) | 19.501% (5.744) |
| Black alone | 24.216% (3.459) | 10.734% (2.789) | 5.156% (1.393) | 9.988% (6.541) |
| Asian alone | 38.938% (4.254) | 7.022% (2.509) | 3.237% (1.465) | 6.224% (7.166) |
| Residual category | 28.709% (5.524) | 14.000% (4.568) | 3.880% (1.830) | 30.254% (20.054) |

*Time lost is conditional on work prevention; valid records are 783, 204, 72,
and 60 respectively. Intervals are wide and the residual category is
heterogeneous; do not use these rows for fine ranking.

## What this adds

The result adds a subgroup distribution to the broader care/work map. Paid
care, assistance, and foregone work do not move as one bundle across the
released race groups. That is consistent with different resources, employment,
family composition, care arrangements, eligibility, or institutional
experiences, but this comparison cannot determine which mechanism explains the
pattern.

The race recode is not a measure of culture, identity meaning, discrimination,
or political interpretation. Those are separate arrows requiring direct
respondent measures and appropriately designed evidence.

## End-to-end route under test

```text
status, resources, and care arrangement
  -> paid care, assistance, or unpaid substitution
  -> work opportunity and time loss
  -> health, family routine, recovery, trust, or collective action
```

This pass strengthens subgroup distribution and uncertainty. It does not
observe a dated care need, provider route, employer flexibility, unpaid
substitution, protected outcome, or later cultural/political meaning.

## Method and limits

The full estimate uses `WPFINWGT`; replicate estimates use `REPWGT1` through
`REPWGT240` under Census’s Fay modified-BRR formula (`G=240`, perturbation
factor `0.5`). Official race status and child-care status flags were applied.
The no-rent-like sparse-cell rule is retained: estimates with small valid
records are reported with their uncertainty and not treated as stable ranks.

Race-group estimates are person-weighted and descriptive. They do not establish
household prevalence, discrimination, causal care or housing effects, provider
access, employer control, health, recovery, trust, political action, or
cultural change.

## Next test

Test only sufficiently precise intersections with poverty, tenure, disability,
region, and child presence, and use interaction estimates rather than a series
of unadjusted rankings. Then define a one-record-per-household rule and seek a
dated trigger/follow-up design for care, work, time substitution, and meaning.

**Evidence status:** reproducible design-based person-weighted race-group
comparison with explicit sparse-cell boundaries; causal and complete same-unit
arrows remain open.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)
- [Machine-readable result](../../../records/us-sipp-care-work-race-official-variance-2024.json)
