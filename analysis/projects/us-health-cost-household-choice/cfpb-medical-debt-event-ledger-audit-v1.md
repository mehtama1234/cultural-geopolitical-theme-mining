# CFPB medical-debt event-ledger acquisition boundary v2

**Checked:** 2026-09-17  
**Status:** failed sub-product filtering check; no medical-debt event ledger promoted

## Result

The CFPB complaint API accepts a `sub_product=Medical debt` parameter but does
not apply it to the returned record rows in this route. A 2024 request for
`product=Debt collection`, `sub_product=Medical debt`, and `size=25` returned
25 `Debt collection` cases with an API total of 156,242. Only 1 of the 25
rows had `sub_product=Medical debt`; the remainder were other debt categories.

The matched 2025 request returned 25 `Debt collection` cases with an API total
of 283,828. Only 1 of those rows had `sub_product=Medical debt`. The returned
2025 rows included `I do not know`, `Other debt`, `Payday loan debt`, `Credit
card debt`, `Rental debt`, and one Medical debt row.

This is an acquisition and API-behavior finding, not medical-debt evidence.
The two temporary derived ledgers were removed because labeling the full
returned samples as medical debt would be invalid. No new medical-debt trend
record or event ledger is promoted.

## What remains usable

The nested aggregate snapshot still reports a Medical debt bucket under the
Debt collection parent for the visibility-only record. It does not supply
case-level response rates. The existing student-loan CFPB ledger remains the
valid demonstration of the general public administrative route contract.

```text
medical-debt category in aggregate snapshot
  -> visibility signal only
  -> exact record-level sub-product filter [not validated]
  -> response, remedy, recovery, trust, or exit [open]
```

## Correct next acquisition design

Do not use the API’s returned `hits.total` or first-page rows as a medical-debt
denominator when the sub-product constraint is ignored. A valid record-level
medical-debt sample must:

1. retrieve a bounded parent-product response;
2. locally verify every returned row’s `product` and `sub_product` fields;
3. report the number of qualifying rows and discarded rows;
4. preserve the raw-response hash, ordering, date span, and missingness; and
5. retain only a de-identified derived ledger after the filter passes.

If the bounded response contains too few qualifying cases, increase the page
cap only after measuring storage, or use a documented pagination strategy.
The route must still be treated as complaint-selected administrative evidence,
not a population sample or verified remedy dataset.

## Reproduction and hashes

The failed 2024 response was 5,673 bytes in the empty top-level query and
140,740 bytes in the returned parent-product query; its response hash was
`cca7bf4be079a18042f0092d0b35429f929d777891fa5c5462122450f9d8d59c`.
The 2025 parent-product response was 160,846 bytes with hash
`50175a48dd86ced79469d4522d63739dd544356951c3283155e453057e8b9807`.
The corresponding temporary derived ledgers were not retained after the
filter failure.

```text
curl --get 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/' \
  --data-urlencode 'date_received_min=2024-01-01' \
  --data-urlencode 'date_received_max=2025-01-01' \
  --data-urlencode 'product=Debt collection' \
  --data-urlencode 'sub_product=Medical debt' \
  --data-urlencode 'size=25'
```

**Evidence status:** official API behavior and returned-row mismatch observed;
case-level medical-debt route, underlying bill, remedy, recovery, trust,
action, and exit remain unobserved.

**Source:** [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
