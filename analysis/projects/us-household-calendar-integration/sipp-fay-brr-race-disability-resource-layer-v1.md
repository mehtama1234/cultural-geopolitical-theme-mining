# SIPP Fay-BRR race × disability × resource layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`; replicate weights `REPWGT1`–`REPWGT240`  
**Method:** Fay BRR, `G=240`, perturbation factor `0.5`

This is a three-way population comparison in the broad unequal-exposure
program. It asks whether the race × monthly resource pattern differs for
people with and without a condition that limits the kind or amount of work
they can do. It is not a household-count table and not a causal explanation.

## Selected estimates

Values are percentages; parentheses are Fay-BRR standard errors in percentage
points. `n` is the number of valid person-month records contributing to that
cell and outcome. The table shows White-alone and Black-alone groups at the
two resource endpoints; the full machine-readable output contains all 32
race × disability × resource cells.

| Race | SIPP work-limiting condition | Resource band | Utility difficulty | Hunger | High/marginal food security | One job |
|---|---|---|---:|---:|---:|---:|
| White alone | Yes | Below 1.00x | 17.42 (1.71), n=7,557 | 39.52 (3.31), n=3,607 | 60.57 (2.40), n=7,557 | 9.58 (1.20), n=7,557 |
| White alone | No | Below 1.00x | 12.33 (1.32), n=14,281 | 31.17 (4.00), n=3,852 | 78.75 (1.67), n=14,281 | 34.40 (1.43), n=14,281 |
| White alone | Yes | 4.00x or more | 4.08 (0.67), n=14,615 | 33.89 (5.36), n=1,388 | 92.98 (0.96), n=14,615 | 32.44 (1.54), n=14,615 |
| White alone | No | 4.00x or more | 2.17 (0.30), n=110,000 | 18.14 (2.78), n=6,063 | 96.63 (0.43), n=110,000 | 68.68 (0.59), n=110,000 |
| Black alone | Yes | Below 1.00x | 22.31 (4.20), n=2,301 | 35.28 (7.41), n=1,038 | 56.16 (4.55), n=2,301 | 8.81 (2.63), n=2,301 |
| Black alone | No | Below 1.00x | 16.07 (3.49), n=3,129 | 24.54 (5.91), n=1,215 | 67.41 (4.16), n=3,129 | 23.03 (2.60), n=3,129 |
| Black alone | Yes | 4.00x or more | 12.13 (3.37), n=1,552 | 28.46 (12.29), n=261 | 86.92 (5.03), n=1,552 | 40.67 (5.38), n=1,552 |
| Black alone | No | 4.00x or more | 5.41 (1.07), n=9,230 | 21.52 (4.71), n=1,130 | 93.49 (1.17), n=9,230 | 72.06 (1.56), n=9,230 |

## What this adds

Within the displayed White and Black groups, people reporting a work-limiting
condition show more utility difficulty, lower high/marginal food security, and
fewer people with one job than people without that condition at both resource
endpoints. The gaps are especially large for one-job status. This is a
distributional pattern: `EDISABL` describes a work-limiting condition, not all
disability, and the table does not identify whether health, discrimination,
care, job availability, or another mechanism produced the difference.

The resource gradient also remains visible inside both disability categories,
but it is not identical across race. Hunger estimates are notably less precise
than the utility and food-security estimates, especially in Black high-resource
cells. The standard errors and record counts are therefore part of the result,
not an afterthought.

## Verification and limits

- 379,215 primary person-month rows were read.
- 378,291 positive-weight rows matched to replicate records; no unmatched
  positive-weight rows remained.
- The selected field universes and status flags were applied: interviewed
  households for rent/mortgage and utility difficulty; the documented food
  screen for hunger; age 15+ for food-security status, job count, and the
  work-limiting condition; and valid poverty/race/disability status for the
  grouping.
- Household outcomes repeat across people. The estimates are person-weighted,
  not household-weighted.
- The SIPP race recode does not replace detailed ethnicity or multiracial
  analysis. The disability measure is a work-limitation measure, not a full
  disability taxonomy.
- The three-way cells are descriptive and some are sparse or imprecise. No
  causal ranking should be made from them.
- The result does not connect the material condition to a particular health
  event, employer decision, accommodation, repair, move, benefit, trust
  judgment, political action, or firm response.

## Reproduction

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_fay_brr.py --group-by ERACE_EDISABL_THINCPOV --official-universes
```

The raw files, derived CSV, and JSON output are not committed. The calculation
output was `/tmp/us-broad-sipp-2025/full-v10/fay-brr-race-disability-resource.json`.

## Next test

Add household composition and tenure to a pre-registered subset, then test a
defined downstream outcome—benefit access, work schedule, care time, housing
stability, or health—using a same-unit or defensible longitudinal design.

Related records: [SIPP Fay-BRR race × resource layer](sipp-fay-brr-race-resource-layer-v1.md),
[SIPP Fay-BRR race × tenure × resource layer](sipp-fay-brr-race-tenure-resource-layer-v1.md),
and [unequal exposure and status layer](../../US-UNEQUAL-EXPOSURE-STATUS-LAYER_V1.md).
