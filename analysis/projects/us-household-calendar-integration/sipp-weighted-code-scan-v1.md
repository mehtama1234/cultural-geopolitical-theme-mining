# SIPP weighted code scan v1

**Run date:** 2026-09-12  
**Input:** full v2 slice from [SIPP acquisition v1](sipp-bounded-acquisition-v1.md)  
**Analysis:** [analyze_sipp_weighted_codes.py](../../../scripts/analyze_sipp_weighted_codes.py)  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`, final person weight

## What was measured

The scan read 379,215 selected rows. Of these, 378,291 had a positive final person weight. It computes weighted distributions of raw SIPP codes and missingness; it does not infer value labels or treat the person weight as a household weight.

| Field | Weighted share with raw code `1` | Weighted blank share | Raw nonblank codes |
|---|---:|---:|---|
| `ETENURE` | 67.23% | 0.00% | 1, 2, 3 |
| `EUTILITIES` | 2.01% | 97.06% | 1, 2 |
| `EENERGY_ASST` | 3.54% | 44.77% | 1, 2 |
| `EAWBMORT` | 4.64% | 0.00% | 1, 2 |
| `EAWBGAS` | 7.06% | 0.00% | 1, 2 |
| `EOWN_SAV` | 52.08% | 18.26% | 1, 2 |
| `EDEBT_CC` | 22.42% | 18.26% | 1, 2 |
| `RFOODS` | 88.56% | 0.00% | 1, 2, 3 |
| `RFOODR` | 5.51% | 0.00% | 0, 1, 2, 3, 4, 5, 6 |
| `EFOOD1` | 2.98% | 0.00% | 1, 2, 3 |
| `EFOOD3` | 6.55% | 0.00% | 1, 2 |
| `EFOOD6` | 4.34% | 83.05% | 1, 2 |
| `EPAY` | 2.19% | 92.73% | 1, 2 |
| `EPAYHELP` | 0.46% | 92.73% | 1, 2 |
| `EWORKMORE` | 0.36% | 90.70% | 1, 2 |
| `RMNUMJOBS` | 45.06% | 16.85% | 0, 1, 2, 3, 4, 5 |

The raw code-`1` percentage is a distribution check, not a final claim about the meaning of code `1`. The official codebook/value labels must be attached before prose uses labels such as “yes,” “owner,” “food insecure,” or “one job.”

## What this adds

The full selected SIPP file can now support a person-level weighted descriptive layer. The scan also exposes where conditional fields are sparse: energy assistance, separate utilities, food hardship detail, child-care payment, and work-limit questions have substantial blank shares. Those blanks must remain `unknown` or outside the field universe, not be recoded as “no.”

## What it does not add

This is not a household prevalence table. Monthly household fields are repeated on person records, and the final person weight is not silently converted into a household weight. It is not a causal estimate, a full event history, or evidence that utility, food, debt, work, or care pressure occurred in the same household after one shock.

The scan also does not establish a national trend: it covers the 2024 reference year in the 2025 SIPP release. Month-to-month differences require the survey design, variable universes, appropriate weights, and variance estimation.

## Next analysis

Attach verified value labels and status flags from the official SIPP documentation. Then produce person-level weighted tables by month and selected strata, with denominators and missingness. For household-level claims, define and document a household selection or household-weight method before estimating joint outcomes. Use the results as one population layer across the broad research bridges, not as a substitute for CE, ATUS, SHED, MEPS, RECS, administrative records, or a true event panel.
