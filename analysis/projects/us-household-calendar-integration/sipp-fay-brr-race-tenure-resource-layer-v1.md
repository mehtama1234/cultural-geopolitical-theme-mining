# SIPP Fay-BRR race × tenure × resource layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`; replicate weights `REPWGT1`–`REPWGT240`  
**Method:** Fay BRR, `G=240`, perturbation factor `0.5`

This is a three-way population comparison inside the broad societal program.
It asks whether the race × monthly resource pattern looks the same for people
in owned, rented, and rent-free housing. It is not a household-count table and
not a causal explanation.

## Selected estimates

Values are percentages; parentheses are Fay-BRR standard errors in percentage
points. `n` is the number of valid person-month records contributing to that
cell and outcome. The table shows White-alone and Black-alone groups at the
two resource endpoints; the full machine-readable output contains all 48
race × tenure × resource cells.

| Race | Tenure | Resource band | Utility difficulty | Hunger | High/marginal food security | One job |
|---|---|---|---:|---:|---:|---:|
| White alone | Owner | Below 1.00x | 11.82 (1.60), n=13,003 | 30.20 (5.04), n=3,814 | 79.36 (2.04), n=10,815 | 26.44 (1.54), n=10,815 |
| White alone | Renter | Below 1.00x | 17.53 (2.08), n=12,367 | 34.31 (3.55), n=5,019 | 67.47 (2.08), n=9,864 | 25.11 (1.62), n=9,864 |
| White alone | Owner | 4.00x or more | 1.97 (0.29), n=119,621 | 13.65 (2.77), n=5,631 | 97.12 (0.37), n=105,737 | 62.88 (0.60), n=105,737 |
| White alone | Renter | 4.00x or more | 4.80 (0.88), n=19,263 | 28.44 (5.31), n=2,828 | 91.82 (1.23), n=17,782 | 75.30 (1.21), n=17,782 |
| Black alone | Owner | Below 1.00x | 21.65 (6.64), n=2,054 | 25.14 (9.56), n=899 | 66.99 (7.13), n=1,691 | 17.17 (2.87), n=1,691 |
| Black alone | Renter | Below 1.00x | 18.46 (4.20), n=4,824 | 28.27 (6.44), n=1,991 | 61.98 (4.02), n=3,609 | 17.89 (2.29), n=3,609 |
| Black alone | Owner | 4.00x or more | 4.93 (1.37), n=8,408 | 20.14 (6.88), n=826 | 94.91 (1.50), n=7,621 | 66.46 (1.85), n=7,621 |
| Black alone | Renter | 4.00x or more | 10.34 (2.83), n=3,231 | 25.92 (9.74), n=712 | 89.07 (2.81), n=2,935 | 74.52 (2.88), n=2,935 |

## What this adds

The resource gradient remains visible within the larger White and Black
groups, but tenure changes the level and sometimes the apparent ordering. For
example, White renters report more utility difficulty and lower food security
than White owners at both resource endpoints. Among Black respondents, the
owner/renter differences are less stable and several hunger cells are
imprecise. This is evidence for intersectional distribution, not evidence
that race or tenure independently causes the outcome.

The three-way result also prevents a misleading two-way summary. A race gap at
one resource level can partly reflect the housing positions within that group;
the housing position itself can carry payment, security, mobility, and control
conditions that the SIPP fields do not fully explain.

## Verification and limits

- 379,215 primary person-month rows were read.
- 378,291 positive-weight rows matched to replicate records; no unmatched
  positive-weight rows remained.
- The selected field universes and status flags were applied: interviewed
  households for rent/mortgage and utility difficulty; the documented food
  screen for hunger; age 15+ for food-security status and job count; and valid
  poverty/race status for the grouping.
- Household outcomes repeat across people. The estimates are person-weighted,
  not household-weighted.
- `ERACE` is the four-category SIPP recode and does not replace detailed
  ethnicity or multiracial analysis.
- The three-way cells include sparse combinations. Large standard errors and
  small `n` cells should not be used for fine ranking.
- The result does not measure why a person rents, owns, or lives rent-free; it
  does not identify a particular price or policy shock; and it does not connect
  the material condition to repair, move, health, trust, political action, or
  firm response.

## Reproduction

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_fay_brr.py --group-by ERACE_ETENURE_THINCPOV --official-universes
```

The raw files, derived CSV, and three-way JSON output are not committed. The
calculation output was `/tmp/us-broad-sipp-2025/full-v8/fay-brr-race-tenure-resource-v2.json`.

## Next test

Use the same pre-registered cells to add household composition and disability,
then compare whether tenure differences persist after those measured
conditions. Keep repair, insurance, benefit access, work schedule, health,
trust, and political action as separate downstream outcomes until a valid
same-unit design measures them.

Related records: [SIPP Fay-BRR race × resource layer](sipp-fay-brr-race-resource-layer-v1.md),
[unequal exposure and status layer](../../US-UNEQUAL-EXPOSURE-STATUS-LAYER_V1.md),
and [SIPP Fay-BRR tenure × resource layer](sipp-fay-brr-tenure-resource-estimates-v1.md).
