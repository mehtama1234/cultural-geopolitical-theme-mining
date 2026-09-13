# SIPP SNAP receipt × food security layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`; replicate weights `REPWGT1`–`REPWGT240`  
**Method:** Fay BRR, `G=240`, perturbation factor `0.5`

This layer adds a public-program outcome to the broad material-security map.
It compares current-month SNAP receipt with hunger, food security, work status,
race, child presence, and monthly income-resource bands. It is a population
comparison, not a test that SNAP receipt caused or solved food insecurity.

## Selected estimates

Values are percentages; parentheses are Fay-BRR standard errors in percentage
points. `n` is the number of valid person-month records for that outcome. The
table shows White-alone and Black-alone groups at the two resource endpoints;
the full machine-readable output contains all 32 race × child-presence ×
resource cells.

| Race | Household members under 18 | Resource band | Received SNAP this month | Hungry but did not eat | High/marginal food security | One job |
|---|---|---|---:|---:|---:|---:|
| White alone | None | Below 1.00x | 29.07 (1.54), n=15,492 | 40.02 (3.42), n=5,186 | 72.99 (1.66), n=15,492 | 21.40 (1.12), n=15,492 |
| White alone | One or more | Below 1.00x | 33.59 (2.76), n=11,298 | 25.83 (5.13), n=4,108 | 72.11 (2.71), n=6,346 | 36.38 (2.06), n=6,346 |
| White alone | None | 4.00x or more | 1.62 (0.19), n=92,985 | 25.69 (3.68), n=5,121 | 96.40 (0.44), n=92,985 | 62.64 (0.65), n=92,985 |
| White alone | One or more | 4.00x or more | 2.02 (0.37), n=47,036 | 9.48 (3.51), n=3,426 | 95.84 (0.79), n=31,630 | 70.80 (0.88), n=31,630 |
| Black alone | None | Below 1.00x | 48.54 (3.62), n=3,839 | 31.02 (5.98), n=1,467 | 65.31 (4.04), n=3,839 | 14.91 (2.40), n=3,839 |
| Black alone | One or more | Below 1.00x | 53.96 (5.17), n=3,197 | 24.44 (7.13), n=1,503 | 60.17 (6.49), n=1,591 | 22.28 (2.88), n=1,591 |
| Black alone | None | 4.00x or more | 2.91 (0.77), n=8,109 | 20.08 (5.28), n=971 | 93.01 (1.49), n=8,109 | 70.40 (1.92), n=8,109 |
| Black alone | One or more | 4.00x or more | 7.10 (2.09), n=3,756 | 25.14 (11.61), n=605 | 92.29 (2.67), n=2,673 | 64.43 (3.22), n=2,673 |

## What this adds

SNAP receipt is concentrated in the below-poverty groups and is much lower in
the highest resource groups. Yet receipt and food security are not the same
outcome: below-poverty SNAP-recipient groups still include substantial hunger
and low food security. This is consistent with the program’s role as one part
of a wider security system, while the cross-sectional comparison cannot show
whether benefits reduced hardship, reached the people at greatest risk, or
arrived after hardship had already occurred.

The race and child-presence differences are also descriptive. Black-alone
groups show higher receipt at both endpoints than White-alone groups in the
displayed cells, but the data do not establish differences in eligibility,
take-up, benefit amount, administrative burden, need, or program treatment.

## Verification and limits

- 379,215 primary person-month rows were read.
- 378,291 positive-weight rows matched to replicate records; no unmatched
  positive-weight rows remained.
- `RSNAP_MNYN` is the documented current-month SNAP receipt recode for all
  persons in interviewed households; its status flag `ASNAP_MNYN` was applied.
- Food-security status uses its documented age-15+ universe; hunger uses the
  documented food-screen universe; poverty, race, and child-presence grouping
  uses their documented status conditions.
- SNAP receipt is represented on person-month records and may reflect a SNAP
  unit or covered household member; this is not a household benefit amount
  table. It does not measure application, denial, renewal, interruption,
  benefit amount, or route-to-help effort.
- Food security is an annual/reference-period measure in this SIPP file, while
  SNAP receipt is monthly. Their co-occurrence is informative but not a dated
  before/after event.
- The result does not establish causal program impact, downstream work or
  health effects, trust, political action, or institutional response.

## Reproduction

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_fay_brr.py --fields RSNAP_MNYN EFOOD6 RFOODS RMNUMJOBS \
       --group-by ERACE_RHNUMU18_THINCPOV --official-universes
```

The raw files, derived CSV, and JSON output are not committed. The calculation
output was `/tmp/us-broad-sipp-2025/full-v12/fay-brr-snap-children-resource.json`.

## Next test

Use SIPP’s SNAP spell and reason fields to separate receipt, start, end,
interruption, and reason for exit. Pair that with a longitudinal food,
earnings, work, debt, and care design. Keep participation, food security,
employment, and trust as separate outcomes.

Related records: [safety-net access layer](administrative-burden-access-layer-v1.md),
[SIPP race × children × resource layer](../us-household-calendar-integration/sipp-fay-brr-race-children-resource-layer-v1.md),
and [US safety-net event ledger](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md).
