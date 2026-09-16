# Utility difficulty, care-related work prevention, and housing hardship: a three-way SIPP diagnostic

**Checked:** 2026-09-15  
**Status:** same-record replicate-weighted diagnostic; not a promoted trend estimate

## Why this diagnostic exists

The current SIPP option-stack synthesis places utility difficulty, child-care
work prevention, tenure, and hardship beside one another. This pass checks how
far those fields can be placed on the **same identified December person
record**, rather than only compared in separate component tables.

The resulting diagnostic is deliberately narrow. It asks whether a December
record with reported utility-payment difficulty and an annual fall report that
child-care arrangements prevented work or more work also differs in reported
rent/mortgage hardship by tenure. It does not identify a bill shock, a care
episode, or a causal sequence.

```text
December utility difficulty
  + annual fall child-care work-prevention status
  + housing tenure
  -> same-record December rent/mortgage hardship
```

The utility and mortgage fields are December person-month measures. The
child-care field is an annual fall reference-parent measure attached to that
December record. That mixed clock is the central interpretation boundary.

## Same-record result

The table uses the 2025 SIPP public-use full-file slice for the 2024 reference
period. It retains `WPFINWGT` for weighted descriptive shares, matches all
identified records to the official `rw2025.csv` archive, and uses the 240
replicate weights for Fay-BRR uncertainty. Valid status flags are required for
utility difficulty, child-care work prevention, tenure, and rent/mortgage
hardship. The displayed `n` is the unweighted identified record count; the
weighted denominator is the denominator for the conditional person-record
estimate, not a household count.

| Utility condition | Child-care work prevention | Tenure | n | Weighted denominator | Rent/mortgage hardship |
|---|---|---|---:|---:|---:|
| Difficulty | No | Owner/buyer | 95 | 1,040,358.0 | 38.057% (SE 5.766; 95% CI 26.757–49.358) |
| Difficulty | No | Renter | 134 | 1,632,259.2 | 58.580% (SE 5.047; 95% CI 48.688–68.472) |
| Difficulty | Yes | Owner/buyer | 10 | 107,295.1 | 25.165% (SE 16.045; 95% CI 0–56.613) |
| Difficulty | Yes | Renter | 12 | 144,442.4 | 72.807% (SE 13.300; 95% CI 46.739–98.875) |
| No difficulty | No | Owner/buyer | 1,635 | 18,558,810.2 | 0.781% (SE 0.192; 95% CI 0.404–1.157) |
| No difficulty | No | Renter | 643 | 8,255,253.5 | 2.959% (SE 0.707; 95% CI 1.574–4.344) |
| No difficulty | Yes | Owner/buyer | 42 | 541,758.5 | 2.180% (SE 2.229; 95% CI 0–6.548) |
| No difficulty | Yes | Renter | 30 | 435,375.7 | 12.016% (SE 7.228; 95% CI 0–26.182) |

The sharpest descriptive pattern is not a single care effect. Within the
utility-difficulty records, renters with reported child-care work prevention
have a higher weighted mortgage-hardship share than renters without that
report (72.807% versus 58.580%), but the difference is imprecise: the
approximate intervals are 46.739–98.875% and 48.688–68.472%, respectively. The
corresponding owner/buyer cells are small and move in the opposite direction
(25.165% versus 38.057%), with very wide intervals. The child-care-prevention
cells contain only 10 owner/buyer and 12 renter records, so their point
estimates must not be ranked or generalized.

The no-utility-difficulty rows provide a useful counter-surface: mortgage
hardship is low but not absent, and the renter child-care-prevention cell is
higher than the renter no-prevention cell (12.016% versus 2.959%). This is
consistent with care constraints and housing exposure being related without
utility difficulty being the sole route.

## What this adds to the end-to-end map

The earlier component analyses established four separate facts:

1. utility difficulty has a next-month work-transition surface;
2. utility difficulty and tenure condition an annual child-care work-
   prevention measure;
3. child-care work prevention co-occurs with higher following hardship in a
   separate stable-SNAP bridge; and
4. renters and owners/buyers occupy different resource and work-transition
   surfaces.

This cross-tab adds a same-record **joint-constraint screen**. It shows why a
household can occupy several constrained positions at once: utility payment
difficulty, limited care alternatives, rental exposure, and housing hardship.
It still cannot tell us which constraint came first, whether a care problem
caused the hardship, whether hardship caused the utility difficulty, or whether
an unmeasured resource protected or destabilized the household.

| Arrow | Status in this diagnostic | Reason |
|---|---|---|
| Utility difficulty + care constraint coexist on one record | Observed/weighted descriptive | Fields are present on the same identified December record |
| Tenure conditions the joint surface | Compared descriptively | Owner/renter cells have different composition and no adjustment |
| Utility difficulty causes care-related work prevention | Open | Annual care field is not time-ordered to a utility event |
| Care-related work prevention causes mortgage hardship | Open | Same-record co-occurrence is not temporal or causal |
| Household recovers, trusts, acts, switches, or exits | Open | No follow-up outcome or meaning/action measure exists here |

## Boundaries and counterexamples

- `EAWBGAS` is the utility-payment-difficulty condition, not a dated bill,
  arrears balance, shutoff, reconnection, or assistance decision.
- `EWORKMORE` describes whether fall child-care arrangements prevented work or
  more work. It is not monthly care hours, provider quality, missed shifts, or
  a measured loss caused by utilities.
- `EAWBMORT` is a separate rent/mortgage-hardship field. It is not a complete
  housing-cost burden, eviction risk, or wealth measure.
- Tenure is an arrangement, not a treatment. Renters and owners/buyers may
  differ in income, family structure, geography, health, employment, and
  access to help.
- The work-prevention cells are sparse. Replicate-weight intervals are
  reported, but their width means the cells must not be fine-ranked or treated
  as precise population differences.
- A household with no reported utility difficulty can still report care
  constraints and mortgage hardship. Conversely, reported utility difficulty
  need not produce care-related work prevention when savings, assistance,
  flexible work, family support, or another provider protects the household.

## Decisive next test

The stronger design would identify a dated bill, shutoff warning, payment
plan, or assistance decision and follow the same person/family at one-,
three-, and six-month windows. It should add care hours and provider/payment
fields, work schedule and earnings, food and housing outcomes, health, and a
verified recovery or institutional-response endpoint.

The essential counterexample is a household with comparable utility exposure
whose care and housing outcomes remain protected because of a documented
payment intervention, flexible schedule, nearby care, family support, or
provider substitute.

## Reproduction boundary

The calculation was run over the locally available slice:

`/tmp/us-broad-sipp-2025/full-v18/sipp-household-slice.csv`

The slice contains 379,215 rows and 13,670 distinct sample units. Its SHA-256
is `4fe7395d4ecdb2f1a3f2879a394f47d1e809c9bdef3960b60543919b79a61eda`.
The calculation retains the fields `MONTHCODE`, `WPFINWGT`, `ETENURE`,
`EAWBGAS`, `AAWBGAS`, `EWORKMORE`, `AWORKMORE`, `EAWBMORT`, and `AAWBMORT`.
All 2,601 identified records matched the replicate archive. The archive is
not committed to the repository. The [machine-readable output](data/sipp-utility-care-mortgage-three-way-2024.json)
and [reproduction script](../../../scripts/analyze_sipp_utility_care_mortgage_three_way.py)
preserve the estimator inputs and result. This memo is a diagnostic extension
of the [utility/tenure/care/work option-stack synthesis](sipp-utility-tenure-care-work-option-stack-synthesis-v1.md),
not a replacement for its component outputs.

**Evidence status:** same-record Fay-BRR descriptive diagnostic with sparse
cells and wide uncertainty; no causal, population-trend,
recovery, trust, political-action, or exit claim.
