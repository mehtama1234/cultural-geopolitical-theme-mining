# SIPP Fay-BRR race × resource layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`; replicate weights `REPWGT1`–`REPWGT240`  
**Method:** Fay BRR, `G=240`, perturbation factor `0.5`

This is the first completed intersectional diagnostic in the broad program. It
compares race categories across monthly income-to-poverty bands. It is a
population distribution, not a one-household story and not a causal estimate.
The latest calculation applies the documented status flags and domain
conditions for the selected fields, so the estimates below are universe-aware
rather than simple nonblank diagnostics.

## Estimates

Values are percentages among nonblank selected records; parentheses are
Fay-BRR standard errors in percentage points.

| Race category | Resource band | Unable to pay rent/mortgage | Unable to pay utility bills | Hungry but did not eat because of money | High or marginal food security | One job |
|---|---|---:|---:|---:|---:|---:|
| White alone | Below 1.00x | 10.94 (1.24) | 14.60 (1.26) | 33.48 (3.00) | 72.73 (1.39) | 26.09 (1.05) |
| White alone | 1.00–1.99x | 8.91 (0.91) | 13.88 (1.19) | 27.64 (2.73) | 77.88 (1.20) | 36.24 (0.86) |
| White alone | 2.00–3.99x | 4.11 (0.46) | 6.62 (0.56) | 23.83 (2.31) | 89.54 (0.65) | 52.63 (0.67) |
| White alone | 4.00x or more | 1.51 (0.21) | 2.45 (0.27) | 18.81 (2.56) | 96.20 (0.36) | 65.01 (0.54) |
| Black alone | Below 1.00x | 13.51 (2.78) | 18.98 (3.37) | 26.98 (5.31) | 63.33 (3.48) | 17.75 (1.86) |
| Black alone | 1.00–1.99x | 7.33 (1.71) | 17.33 (2.95) | 24.57 (4.75) | 74.34 (2.95) | 42.22 (2.05) |
| Black alone | 2.00–3.99x | 8.53 (1.81) | 11.33 (2.01) | 22.94 (4.43) | 85.12 (1.92) | 60.24 (2.01) |
| Black alone | 4.00x or more | 4.93 (1.11) | 6.46 (1.30) | 22.28 (5.50) | 92.79 (1.36) | 68.79 (1.58) |
| Asian alone | Below 1.00x | 7.86 (3.78) | 7.79 (3.85) | 17.69 (7.80) | 83.25 (4.29) | 24.42 (3.58) |
| Asian alone | 1.00–1.99x | 3.43 (1.70) | 3.78 (2.56) | 9.71 (6.98) | 82.21 (5.44) | 38.90 (3.37) |
| Asian alone | 2.00–3.99x | 2.08 (1.10) | 3.01 (1.33) | 5.92 (4.63) | 93.13 (2.02) | 49.44 (2.36) |
| Asian alone | 4.00x or more | 0.89 (0.45) | 1.25 (0.60) | 24.50 (12.62) | 97.32 (0.82) | 69.64 (1.56) |
| Residual race category | Below 1.00x | 20.66 (4.13) | 28.47 (4.72) | 57.31 (8.10) | 60.79 (4.60) | 25.51 (3.39) |
| Residual race category | 1.00–1.99x | 12.44 (3.58) | 26.15 (5.75) | 38.31 (7.04) | 64.38 (5.00) | 38.47 (4.03) |
| Residual race category | 2.00–3.99x | 7.50 (2.35) | 12.17 (2.81) | 22.03 (6.29) | 76.97 (3.72) | 51.40 (2.86) |
| Residual race category | 4.00x or more | 2.72 (1.07) | 2.03 (0.68) | 15.36 (5.69) | 92.27 (1.66) | 65.65 (2.39) |

## What the table shows

The resource gradient is visible within every race category for utility-payment
difficulty and high or marginal food security: the reported utility-pressure
share is generally lower, and food-security share higher, in the highest
resource band than in the below-poverty band. The same broad gradient appears
for the hunger diagnostic, although several cells are imprecise. The one-job
measure changes with resource band too, but it is a work-status measure, not
proof of security or hardship.

At comparable resource bands, the size and ordering of gaps differ. Black-alone
respondents have higher utility-payment difficulty than White-alone respondents
in the four displayed resource bands, while the residual category is more
heterogeneous and the Asian-alone food cells are imprecise. This is a reason to
retain intersections and uncertainty, not to assign one universal racial cause.

The table supports a distributional question: how much of observed pressure is
associated with resources, race, tenure, place, household composition, health,
work, or institutional access, and how do those conditions interact? It does
not answer that question by itself.

## Verification and limits

- 379,215 primary person-month rows were read.
- 378,291 positive-weight rows matched to replicate records; no unmatched
  positive-weight rows remained.
- `ERACE` is the SIPP four-category recode: White alone, Black alone, Asian
  alone, and Residual. It is not a full ethnicity or detailed multiracial
  measure.
- `THINCPOV` is a monthly household income-to-poverty ratio; the estimates use
  person records and the final person weight.
- Household fields repeat across people; this is not a household-count table.
- The selected outcomes use nonblank denominators after applying the documented
  field universes and excluding status flag `0` (not in universe). The hunger
  denominator also requires the documented EFOOD1/EFOOD2/EFOOD3 screen; food
  security and job count require age 15+. The machine-readable output records
  `official_universes_constructed: true` for these selected fields.
- Standard errors are a first design-based check and do not establish cause.
- The results do not connect race/resource status to a particular bill, price,
  repair, benefit decision, health event, move, trust judgment, vote, or firm
  response.

## Reproduction command

The extraction and calculation use the repository scripts:

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_fay_brr.py --group-by ERACE_THINCPOV --official-universes
```

The raw files and derived CSV are not committed. The status-aware temporary
calculation output was `/tmp/us-broad-sipp-2025/full-v6/fay-brr-race-resource-official-v2.json`.

## Next test

Add tenure and household composition to a small pre-registered set. Pair the intersection with a valid
measure of benefit access, local prices, housing quality, health, or mobility.
Keep the downstream links—repair, food recovery, work change, trust, political
action, and institutional response—separate until they are measured in the
same source or a defensible linked design.

Related records: [SIPP Fay-BRR tenure × resource layer](sipp-fay-brr-tenure-resource-estimates-v1.md),
[unequal exposure and status layer](../../US-UNEQUAL-EXPOSURE-STATUS-LAYER_V1.md),
and [2025 SIPP broad-bridge crosswalk](sipp-broad-bridge-crosswalk-v1.md).
