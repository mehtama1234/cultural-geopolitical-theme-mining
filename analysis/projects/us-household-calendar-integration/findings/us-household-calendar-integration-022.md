# Material room is patterned by resources, race, and tenure together

**Status:** reproducibility-strengthened descriptive SIPP finding · **Checked:** 2026-09-14

## The bounded finding

Monthly household resource position and housing tenure describe different
parts of material room, and their pattern differs across the White-alone and
Black-alone SIPP recodes. At both the below-1.00x and 4.00x-or-more monthly
income-to-poverty endpoints, renters generally show more utility difficulty
and worse food-security status than owners within the displayed race groups.
The gaps are not uniform, and several Black-alone hunger cells are imprecise.

This is a person-weighted, reference-month comparison. It does not estimate a
race effect, a tenure effect, a household rate, or a causal housing or income
mechanism.

## Selected estimates

Percentages below use `WPFINWGT`; parentheses are Fay–BRR standard errors in
percentage points. `n` is the valid person-month record count for that outcome.
The full 48-cell output remains in the source layer.

| Race recode | Tenure | Resource band | Utility difficulty | Hunger | High/marginal food security | One job |
|---|---|---|---:|---:|---:|---:|
| White alone | Owner | Below 1.00x | 11.82 (1.60), n=13,003 | 30.20 (5.04), n=3,814 | 79.36 (2.04), n=10,815 | 26.44 (1.54), n=10,815 |
| White alone | Renter | Below 1.00x | 17.53 (2.08), n=12,367 | 34.31 (3.55), n=5,019 | 67.47 (2.08), n=9,864 | 25.11 (1.62), n=9,864 |
| White alone | Owner | 4.00x or more | 1.97 (0.29), n=119,621 | 13.65 (2.77), n=5,631 | 97.12 (0.37), n=105,737 | 62.88 (0.60), n=105,737 |
| White alone | Renter | 4.00x or more | 4.80 (0.88), n=19,263 | 28.44 (5.31), n=2,828 | 91.82 (1.23), n=17,782 | 75.30 (1.21), n=17,782 |
| Black alone | Owner | Below 1.00x | 21.65 (6.64), n=2,054 | 25.14 (9.56), n=899 | 66.99 (7.13), n=1,691 | 17.17 (2.87), n=1,691 |
| Black alone | Renter | Below 1.00x | 18.46 (4.20), n=4,824 | 28.27 (6.44), n=1,991 | 61.98 (4.02), n=3,609 | 17.89 (2.29), n=3,609 |
| Black alone | Owner | 4.00x or more | 4.93 (1.37), n=8,408 | 20.14 (6.88), n=826 | 94.91 (1.50), n=7,621 | 66.46 (1.85), n=7,621 |
| Black alone | Renter | 4.00x or more | 10.34 (2.83), n=3,231 | 25.92 (9.74), n=712 | 89.07 (2.81), n=2,935 | 74.52 (2.88), n=2,935 |

## What the intersection adds

The two-way resource gradient is not enough to describe the available room.
For example, White renters report more utility difficulty than White owners at
both resource endpoints, while the Black-alone owner/renter differences are
less stable and have wider intervals. Housing position may carry payment,
security, mobility, family-support, and control conditions that the selected
SIPP fields do not identify.

The comparison therefore supports an intersectional measurement rule:

```text
monthly resources × tenure × race position
  -> observed hardship and food-security distribution
  -> work and housing options that remain unmeasured
  -> possible time, health, institutional, or political consequences
```

Only the first arrow is measured here. Household outcomes repeat across person
records, and one-job status is not a measure of hours, pay, schedule control,
job quality, or voluntary choice.

## Counterexamples and limits

- A higher-resource renter cell can still show more hardship than a lower-risk
  owner cell; resource bands do not erase housing-cost or security differences.
- The Black-alone owner/renter ordering is not a stable ranking for every
  outcome; sparse hunger cells have wide uncertainty intervals.
- Race and tenure are descriptive positions, not independent causes in this
  table. Composition, geography, household structure, disability, prices,
  and access to assistance are not fully controlled.
- The analysis does not observe a dated bill, eviction or move, repair event,
  health change, benefit route, trust judgment, political action, or firm
  response.

## Reproduction and evidence boundary

The calculation uses the 2025 SIPP public-use file, `WPFINWGT`, official
universe/status flags, and 240 Fay–BRR replicate weights with perturbation
factor 0.5. The current v16 rerun reads 379,215 primary rows and matches
378,291 positive-weight rows to replicate records. It reproduces the promoted
estimates from the earlier local extract; the [dated reproduction audit](../sipp-fay-brr-race-tenure-resource-reproduction-audit-2026-09-14.json)
preserves input/output hashes and the exact command.

The [source layer](../sipp-fay-brr-race-tenure-resource-layer-v1.md) contains
the field universes, full cell design, and original table. This finding is a
reader-facing interpretation of that layer, not a new trend observation.

## Next test

Add household composition and disability status to the pre-specified cells,
then test whether tenure differences persist. A later design must connect the
material position to work schedule, care, health, repair, benefit access,
trust, and political action in the same valid unit before making an end-to-end
claim.

**Evidence status:** weighted intersectional person-month comparison with
design-based uncertainty and a reproduction audit; causal, household-weighted,
and downstream cultural or political effects remain open.
