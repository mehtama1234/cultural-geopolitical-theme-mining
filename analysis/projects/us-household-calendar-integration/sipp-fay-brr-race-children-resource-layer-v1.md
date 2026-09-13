# SIPP Fay-BRR race × children × resource layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`; replicate weights `REPWGT1`–`REPWGT240`  
**Method:** Fay BRR, `G=240`, perturbation factor `0.5`

This is a three-way population comparison in the broad unequal-exposure
program. It asks whether the race × monthly resource pattern differs between
households with no members under 18 and households with one or more members
under 18. The children measure is a household-composition measure repeated on
person-month records; it is not an individual parent/child classification.

## Selected estimates

Values are percentages; parentheses are Fay-BRR standard errors in percentage
points. `n` is the number of valid person-month records contributing to that
cell and outcome. The table shows White-alone and Black-alone groups at the
two resource endpoints; the full machine-readable output contains all 32
race × children × resource cells.

| Race | Household members under 18 | Resource band | Utility difficulty | Hunger | High/marginal food security | One job |
|---|---|---|---:|---:|---:|---:|
| White alone | None | Below 1.00x | 11.82 (1.14), n=15,492 | 40.02 (3.42), n=5,186 | 72.99 (1.66), n=15,492 | 21.40 (1.12), n=15,492 |
| White alone | One or more | Below 1.00x | 18.04 (2.43), n=11,298 | 25.83 (5.13), n=4,108 | 72.11 (2.71), n=6,346 | 36.38 (2.06), n=6,346 |
| White alone | None | 4.00x or more | 2.40 (0.31), n=92,985 | 25.69 (3.68), n=5,121 | 96.40 (0.44), n=92,985 | 62.64 (0.65), n=92,985 |
| White alone | One or more | 4.00x or more | 2.61 (0.49), n=47,036 | 9.48 (3.51), n=3,426 | 95.84 (0.79), n=31,630 | 70.80 (0.88), n=31,630 |
| Black alone | None | Below 1.00x | 19.07 (3.22), n=3,839 | 31.02 (5.98), n=1,467 | 65.31 (4.04), n=3,839 | 14.91 (2.40), n=3,839 |
| Black alone | One or more | Below 1.00x | 18.90 (5.44), n=3,197 | 24.44 (7.13), n=1,503 | 60.17 (6.49), n=1,591 | 22.28 (2.88), n=1,591 |
| Black alone | None | 4.00x or more | 4.99 (1.03), n=8,109 | 20.08 (5.28), n=971 | 93.01 (1.49), n=8,109 | 70.40 (1.92), n=8,109 |
| Black alone | One or more | 4.00x or more | 9.02 (2.91), n=3,756 | 25.14 (11.61), n=605 | 92.29 (2.67), n=2,673 | 64.43 (3.22), n=2,673 |

## What this adds

Household composition changes the distribution inside the race × resource
comparison. Among White-alone households below poverty, those with members
under 18 show higher utility difficulty and a higher one-job share, while the
hunger estimate is imprecise and points in the other direction. At the high
resource endpoint, the child-present White group has a lower hunger estimate
but a higher one-job share. These differences demonstrate why “family” cannot
be treated as a simple hardship multiplier; the protected need, work pattern,
and household composition can move together in different ways.

The Black-alone child-present cells are generally less precise. The comparison
does not establish whether children change the outcome. It may reflect family
structure, age, work composition, caregiving, tenure, health, or other
conditions not controlled here.

## Verification and limits

- 379,215 primary person-month rows were read.
- 378,291 positive-weight rows matched to replicate records; no unmatched
  positive-weight rows remained.
- The selected field universes and status flags were applied: interviewed
  households for rent/mortgage and utility difficulty; the documented food
  screen for hunger; age 15+ for food-security status and job count; and valid
  poverty/race/household-composition status for the grouping.
- `RHNUMU18` counts household members under 18 in the month. It does not show
  whether the respondent is a parent, whether a child needs care, or whether
  children were shielded from adult hardship.
- Household outcomes repeat across people. The estimates are person-weighted,
  not household-weighted.
- Some cells are sparse or imprecise. No causal ranking should be made from
  these comparisons.
- The result does not connect composition to childcare, unpaid care, health,
  benefit access, housing stability, political judgment, or firm response.

## Reproduction

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_fay_brr.py --group-by ERACE_RHNUMU18_THINCPOV --official-universes
```

The raw files, derived CSV, and JSON output are not committed. The calculation
output was `/tmp/us-broad-sipp-2025/full-v11/fay-brr-race-children-resource.json`.

## Next test

Combine child presence with tenure and the work-limiting-condition measure in a
small pre-registered subset, then add a direct care or work-schedule outcome.
Keep household composition, caregiving, employment, and food security as
separate variables.

Related records: [SIPP Fay-BRR race × disability × resource layer](sipp-fay-brr-race-disability-resource-layer-v1.md),
[SIPP Fay-BRR race × tenure × resource layer](sipp-fay-brr-race-tenure-resource-layer-v1.md),
and [unequal exposure and status layer](../../US-UNEQUAL-EXPOSURE-STATUS-LAYER_V1.md).
