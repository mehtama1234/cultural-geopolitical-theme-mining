# Utility difficulty, care-related work prevention, and housing hardship: a three-way SIPP diagnostic

**Checked:** 2026-09-15  
**Status:** same-record weighted diagnostic; not a promoted trend estimate

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
period. It retains `WPFINWGT` for weighted descriptive shares and requires
valid status flags for utility difficulty, child-care work prevention, tenure,
and rent/mortgage hardship. The displayed `n` is the unweighted identified
record count; the weighted denominator is not a population estimate because
the slice has no locally available replicate-weight archive for this new
three-way cross-tab.

| Utility condition | Child-care work prevention | Tenure | n | Weighted denominator | Rent/mortgage hardship |
|---|---|---|---:|---:|---:|
| Difficulty | No | Owner/buyer | 95 | 1,040,358.0 | 38.057% |
| Difficulty | No | Renter | 134 | 1,632,259.2 | 58.580% |
| Difficulty | Yes | Owner/buyer | 10 | 107,295.1 | 25.165% |
| Difficulty | Yes | Renter | 12 | 144,442.4 | 72.807% |
| No difficulty | No | Owner/buyer | 1,635 | 18,558,810.2 | 0.781% |
| No difficulty | No | Renter | 643 | 8,255,253.5 | 2.959% |
| No difficulty | Yes | Owner/buyer | 42 | 541,758.5 | 2.180% |
| No difficulty | Yes | Renter | 30 | 435,375.7 | 12.016% |

The sharpest descriptive pattern is not a single care effect. Within the
utility-difficulty records, renters with reported child-care work prevention
have a higher weighted mortgage-hardship share than renters without that
report (72.807% versus 58.580%), while the corresponding owner/buyer cells are
small and move in the opposite direction (25.165% versus 38.057%). The
child-care-prevention cells contain only 10 owner/buyer and 12 renter records,
so their point estimates must not be ranked or generalized.

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
- The work-prevention cells are sparse. The weighted percentages have no
  replicate-weight standard errors in this diagnostic and must not be used to
  fine-rank groups or claim population precision.
- A household with no reported utility difficulty can still report care
  constraints and mortgage hardship. Conversely, reported utility difficulty
  need not produce care-related work prevention when savings, assistance,
  flexible work, family support, or another provider protects the household.

## Decisive next test

The next defensible version should rerun this exact cross-tab with the
official 240 replicate-weight archive and preserve Fay-BRR uncertainty. The
stronger design would then identify a dated bill, shutoff warning, payment
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
The raw slice is not committed to the repository. This memo is a diagnostic
extension of the [utility/tenure/care/work option-stack synthesis](sipp-utility-tenure-care-work-option-stack-synthesis-v1.md),
not a replacement for its design-based component outputs.

**Evidence status:** same-record weighted descriptive diagnostic with sparse
cells and no replicate-weight uncertainty; no causal, population-trend,
recovery, trust, political-action, or exit claim.
