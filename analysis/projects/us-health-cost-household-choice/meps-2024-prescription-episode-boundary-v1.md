# MEPS 2024 prescriptions add a payment channel, not a complete dated episode

**Checked:** 2026-09-15  
**Status:** bounded event-layer interpretation; no causal claim

## Why this memo exists

Prescription purchases are important to the health-cost pathway because they
sit between a clinical decision and an ordinary household payment. The 2024
HC-254A file can be joined exactly to the HC-256 person file and carries a
self/family payment field. It therefore adds a useful medication-payment
surface to the atlas. It should not, however, be silently folded into the
dated first-event ledger: the available medication start month/year fields
are valid for only 65,563 of 204,550 prescription records (32.05%), and they
do not provide a complete transaction date for every purchase.

## What is directly observed

The 2024 purchase-level layer estimates 3.029 billion prescribed-medicine
purchases, with $233.25 in total payment and $16.95 in self/family payment per
purchase. Among observed under-65 purchases, self/family payment averages
$21.83 for private coverage, $4.12 for public-only coverage, and $55.06 for
uninsured purchases. These estimates use the prescription file's own Taylor
design and keep purchase events separate from person-level prevalence.

The exact join is:

```text
HC-254A purchase record
  -> DUPERSID + PANEL
  -> HC-256 coverage and person context
  -> total payment / self-family payment
```

This directly establishes a purchase/payment channel. It does not establish
that the person needed a medicine but did not obtain it, that the purchase
followed a particular visit, or that the displayed payment was paid at the
time of purchase.

## The timing boundary is substantive

HC-254A's medication start fields can be useful for a restricted dated
subsample, but they are not interchangeable with a purchase date. A start
date may precede the observed purchase, and missing or special-coded dates
are not evidence that the purchase occurred outside the year or that no need
existed. The safe separation is therefore:

| Surface | Safe use | Do not claim |
|---|---|---|
| All HC-254A records | purchase count and payment-channel estimates | complete person prevalence or adherence |
| Records with valid start month/year | restricted timing comparisons | a complete purchase-date episode clock |
| HC-256 cost-delay fields | reported prescription affordability and delay context | that a specific purchase caused or prevented delay |

The same person can appear in multiple purchase records. A first-purchase
extract would answer a different question from the first-care-event ledger,
and a purchase is not necessarily the first medication episode for that
person. The event universe and the person universe must remain visible.

## What this adds to the end-to-end theme

The prescription channel sharpens the distinction between observed access and
unobserved need:

```text
prescription is recorded
  -> payment channel is observed
  -> coverage is observed
  -> cost-related delay or inability to afford medicine is separately reported
  -> forgone fill, substitution, adherence, borrowing, time, and recovery remain open
```

The public-use data can therefore support a layered statement: coverage is
associated with different direct payments where a medicine purchase is
observed, while a separate person-level surface reports whether respondents
delayed or could not afford prescriptions. It cannot identify the missing
counterfactual—who had a prescription need but no purchase—or connect that
choice to a later bill, work adjustment, health recovery, trust judgment, or
political action.

This is not a minor technical caveat. The people most exposed to medication
cost may be underrepresented in a purchase-only denominator precisely because
they delay or forgo the purchase. Treating observed purchases as all medicine
needs would turn a selection boundary into a false access measure.

## Smallest decisive next test

The next defensible extension is a restricted, explicitly two-surface bridge:

1. use valid medication start dates only for a dated subsample;
2. retain all purchase/payment records as a separate event universe;
3. link both to HC-256 coverage, cost-related prescription delay, health,
   work, and financial-room fields;
4. compare observed purchase/payment patterns with reported non-purchase or
   delay, without treating the two as the same person-level outcome;
5. use SHED or another same-respondent source to test borrowing, sacrificed
   essentials, work/time trade-offs, and recovery.

Until a source supplies the need and rejected-alternative fields, the correct
interpretation is **medicine purchase/payment exposure plus a separate
affordability-delay surface**, not a completed prescription affordability
episode.

## Sources and reproduction

The source files are AHRQ's [MEPS 2024 HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes) and [HC-254A prescribed-medicine file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254A&prfricon=yes). The linkage and date audit is documented in [MEPS 2024 event-linkage audit](meps-2024-event-linkage-audit-v1.md). The purchase/payment estimates are reproduced by:

```text
python3 scripts/analyze_meps_hc254a_rx_event_layer.py \
  /tmp/cgtm-meps-2024/events/h254a.dta \
  /tmp/cgtm-meps-2024/h256/h256.dta
```

