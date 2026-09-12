# SIPP Fay-BRR race × resource layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`; replicate weights `REPWGT1`–`REPWGT240`  
**Method:** Fay BRR, `G=240`, perturbation factor `0.5`

This is the first completed intersectional diagnostic in the broad program. It
compares race categories across monthly income-to-poverty bands. It is a
population distribution, not a one-household story and not a causal estimate.
The second calculation applies the documented status flags for the selected
fields, so the estimates below are status-flag-filtered rather than simple
nonblank diagnostics.

## Estimates

Values are percentages among nonblank selected records; parentheses are
Fay-BRR standard errors in percentage points.

| Race category | Resource band | Unable to pay utility bills | Hungry but did not eat because of money | One job |
|---|---|---:|---:|---:|
| White alone | Below 1.00x | 14.60 (1.26) | 33.48 (3.00) | 25.81 (1.04) |
| White alone | 1.00–1.99x | 13.88 (1.19) | 27.65 (2.73) | 35.82 (0.85) |
| White alone | 2.00–3.99x | 6.61 (0.56) | 23.85 (2.31) | 52.07 (0.67) |
| White alone | 4.00x or more | 2.44 (0.27) | 18.98 (2.57) | 64.50 (0.54) |
| Black alone | Below 1.00x | 19.11 (3.36) | 26.89 (5.29) | 17.65 (1.85) |
| Black alone | 1.00–1.99x | 17.32 (2.95) | 24.56 (4.74) | 41.85 (2.04) |
| Black alone | 2.00–3.99x | 11.29 (2.01) | 22.67 (4.40) | 59.57 (2.00) |
| Black alone | 4.00x or more | 6.43 (1.29) | 22.25 (5.49) | 68.17 (1.64) |
| Asian alone | Below 1.00x | 7.79 (3.85) | 17.69 (7.80) | 24.11 (3.53) |
| Asian alone | 1.00–1.99x | 3.78 (2.56) | 9.71 (6.98) | 38.58 (3.27) |
| Asian alone | 2.00–3.99x | 3.01 (1.33) | 5.92 (4.63) | 49.17 (2.35) |
| Asian alone | 4.00x or more | 1.27 (0.60) | 24.50 (12.62) | 68.68 (1.55) |
| Residual race category | Below 1.00x | 28.47 (4.72) | 57.31 (8.10) | 24.53 (3.10) |
| Residual race category | 1.00–1.99x | 26.06 (5.73) | 38.19 (6.98) | 37.99 (3.97) |
| Residual race category | 2.00–3.99x | 12.16 (2.81) | 22.03 (6.29) | 50.36 (2.76) |
| Residual race category | 4.00x or more | 2.03 (0.68) | 15.36 (5.69) | 65.06 (2.37) |

## What the table shows

The resource gradient is visible within every race category for utility-payment
difficulty: the reported share is lower in the highest resource band than in
the below-poverty band. The same broad gradient appears for the hunger
diagnostic, although several cells are imprecise. The one-job measure changes
with resource band too, but it is a work-status measure, not proof of security
or hardship.

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
- The selected outcomes use nonblank denominators after excluding records with
  status flag `0` (not in universe) for that field. This is a status-aware
  calculation, but it has not independently reconstructed every domain rule
  from the dictionary; `official_universes_constructed` therefore remains
  false in the machine-readable output.
- Standard errors are a first design-based check and do not establish cause.
- The results do not connect race/resource status to a particular bill, price,
  repair, benefit decision, health event, move, trust judgment, vote, or firm
  response.

## Reproduction command

The extraction and calculation use the repository scripts:

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_fay_brr.py --group-by ERACE_THINCPOV
```

The raw files and derived CSV are not committed. The status-aware temporary
calculation output was `/tmp/us-broad-sipp-2025/full-v6/fay-brr-race-resource-official-v2.json`.

## Next test

Reconstruct the remaining variable-specific domain rules, then add tenure and
household composition to a small pre-registered set. Pair the intersection with a valid
measure of benefit access, local prices, housing quality, health, or mobility.
Keep the downstream links—repair, food recovery, work change, trust, political
action, and institutional response—separate until they are measured in the
same source or a defensible linked design.

Related records: [SIPP Fay-BRR tenure × resource layer](sipp-fay-brr-tenure-resource-estimates-v1.md),
[unequal exposure and status layer](../../US-UNEQUAL-EXPOSURE-STATUS-LAYER_V1.md),
and [2025 SIPP broad-bridge crosswalk](sipp-broad-bridge-crosswalk-v1.md).
