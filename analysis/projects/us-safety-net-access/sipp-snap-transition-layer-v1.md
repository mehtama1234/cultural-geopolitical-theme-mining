# SIPP monthly SNAP transition layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file, 2024 reference year  
**Unit:** identified person, adjacent reference-month pair  
**Weight:** `WPFINWGT` from the first month of each pair  
**Method:** descriptive adjacent-month transition counts; no replicate-weight variance estimate

This layer turns SNAP receipt from a prevalence measure into a limited event
sequence. It asks how often identified people move into, out of, or remain in
SNAP across adjacent months. The transition is a monthly program indicator;
food-security status and poverty bands are included only as reference-period
context unless explicitly documented as monthly.

## SNAP transitions

Among 346,283 adjacent person-month pairs with valid SNAP values:

| Transition | Pairs | Weighted share of all valid pairs |
|---|---:|---:|
| No → No | 312,418 | 90.65% |
| Yes → Yes | 33,041 | 9.11% |
| No → Yes | 437 | 0.13% |
| Yes → No | 387 | 0.12% |

The weighted conditional transition rates are approximately 0.14% from no
receipt into receipt and 1.30% from receipt into no receipt, calculated within
the corresponding prior-state pairs. These are descriptive rates for this
sample and observation design, not national spell hazards or estimates of
program churn.

## What this adds to the broad program

The monthly indicator shows that SNAP receipt is usually stable across adjacent
months in the observed person records, while entry and exit are comparatively
rare in the pair data. This gives the safety-net event ledger a real temporal
anchor: receipt can be treated as a sequence of monthly states rather than
only an annual participation label.

It also establishes the correct next question. A receipt transition should be
paired with the resource band, work status, household child presence, food
security, and income changes around the same person and month. A fall in receipt
could reflect improved resources, an administrative interruption, a move,
voluntary exit, or another reason; the transition alone cannot distinguish
them.

## Verification and limits

- The transition run identified 31,992 people in the selected slice; 31,090
  had all twelve reference months.
- There were 346,283 available adjacent-month pairs for the selected people.
- `RSNAP_MNYN` is the SIPP current-month SNAP receipt recode and uses its
  documented interviewed-household universe and status flag in the related
  weighted layer.
- The transition analyzer uses valid nonblank `1`/`2` codes and the first
  month’s person weight; it does not estimate replicate-weight uncertainty.
- The pair sequence does not identify applications, notices, renewal burden,
  benefit amount, reason for entry/exit, office/channel, or whether food
  security improved.
- The same person identifier does not make food-security responses monthly:
  the SIPP food measures are annual/reference-period measures repeated on
  monthly records.
- Person records may represent covered members of a SNAP unit, so this is not
  a household-level benefit-spell table.

## Reproduction

```text
analyze_sipp_person_transitions.py \
  --fields RSNAP_MNYN RMNUMJOBS THINCPOV
```

The raw files, derived CSV, and JSON output are not committed. The calculation
output was `/tmp/us-broad-sipp-2025/full-v12/sipp-snap-transitions.json`.

## Next test

Use the documented SNAP start/end reason fields and benefit-owner fields to
classify entry, administrative interruption, voluntary exit, improved-income
exit, and unresolved exit. Then compare each transition with monthly resources,
work, child presence, food security, and later re-entry. Keep participation,
food security, employment, debt, health, trust, and political action separate.

Related records: [SIPP SNAP × food-security layer](sipp-snap-food-security-layer-v1.md),
[safety-net access layer](administrative-burden-access-layer-v1.md),
and [US safety-net event ledger](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md).
