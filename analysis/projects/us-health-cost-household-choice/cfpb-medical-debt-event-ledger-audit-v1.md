# CFPB medical-debt event-ledger acquisition boundary v3

**Checked:** 2026-09-17  
**Status:** bounded locally filtered administrative route; no prevalence or remedy estimate

**Machine records:** [48-row 2024 filtered ledger](data/cfpb-medical-debt-filtered-event-ledger-2024.json) and [49-row 2025 filtered ledger](data/cfpb-medical-debt-filtered-event-ledger-2025.json)

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

The first-page results are an acquisition and API-behavior finding, not valid
medical-debt evidence. The 2025 route was then re-run with a 1,000-record
bounded parent-product response and locally filtered by both returned fields.
That response yielded 49 qualifying Medical debt rows. The same corrected
1,000-row method applied to 2024 yielded 48 qualifying rows. They are retained
in the [2024 ledger](data/cfpb-medical-debt-filtered-event-ledger-2024.json)
and [2025 ledger](data/cfpb-medical-debt-filtered-event-ledger-2025.json).
The earlier unfiltered derived ledgers remain deleted. These corrected ledgers
are administrative route samples, not a medical-debt prevalence or remedy
estimate.

## What remains usable

The nested aggregate snapshot still reports a Medical debt bucket under the
Debt collection parent for the visibility-only record. The corrected 48- and
49-row ledgers supply bounded case-level route fields, but their 1,000-row
retrieval frames are not random or weighted. The existing student-loan CFPB ledger remains
the general public administrative route contract.

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

The corrected 2024 response had dates from 2024-08-28 through 2024-09-04,
covered 26 states, and contained 44 `Closed with explanation` and 4 `Closed
with non-monetary relief` labels. Forty-seven rows were timely and one
untimely; 19 had a public response flag and 29 did not.

The corrected 2025 response had dates from 2025-10-09 through 2026-01-01,
covered 27 states, and contained 43 `Closed with explanation`, 5 `Closed with
non-monetary relief`, and 1 `Untimely response` label. Forty-six rows were
timely and three untimely; 15 had a public response flag and 34 did not. These
counts describe the qualifying rows within the first 1,000 returned parent
records for each year only. If a bounded response contains too few qualifying cases,
increase the page cap only after measuring storage, or use a documented
pagination strategy.

### A narrow year-to-year surface comparison

The retained ledgers permit one bounded comparison of how the administrative
route was coded inside each retrieval frame:

| Surface | 2024 frame | 2025 frame | Safe reading |
|---|---:|---:|---|
| Timely route label | 47/48 (97.9%) | 46/49 (93.9%) | The sampled route labels differ; this is not a response-time trend. |
| Closed with non-monetary relief | 4/48 (8.3%) | 5/49 (10.2%) | Relief labels are administrative categories, not verified consumer recovery. |
| Public response flag present | 19/48 (39.6%) | 15/49 (30.6%) | Publication visibility differs within the capped frames; it is not a remedy or disclosure rate. |

The comparison is interesting because response coding and public visibility do
not move as one surface: the later frame has slightly fewer timely labels and
more non-monetary-relief labels, while its public-response flag is less common.
But the frames cover different dates (a short August–September 2024 window
versus October 2025–January 2026), different returned parent-product orders,
and different state compositions. The denominators are 48 and 49 qualifying
rows after local filtering, not all medical-debt complaints. Nothing here
supports a change in consumer harm, remedy success, bill resolution, or trust.

The route must still be treated as complaint-selected administrative evidence,
not a population sample or verified remedy dataset.

## Reproduction and hashes

The failed 2024 response was 5,673 bytes in the empty top-level query and
140,740 bytes in the returned parent-product query; its response hash was
`cca7bf4be079a18042f0092d0b35429f929d777891fa5c5462122450f9d8d59c`.
The 2025 parent-product response was 160,846 bytes with hash
`50175a48dd86ced79469d4522d63739dd544356951c3283155e453057e8b9807`.
The corrected 2025 1,000-row response was 744,466 bytes with hash
`e20e5908fcfbb3d34b80c32d3785ec9cd6c584513ab04eb2e75aedd0a2374ecd`; its
filtered ledger hash is
`8f9db3c3643a55ce44739a1f8169692ec2621beebdff4827ebcc96f6d415b7176`.
The corrected 2024 1,000-row response was 726,578 bytes with hash
`3108aa5da41c8389aeb3cfd831c946efe79e02cdfeb5fd12951ebc1d4e843f0a`; its
filtered ledger hash is
`fea28b658ac242ff33a40983f5338afdf1f9171acf06ba3631cc69288a21665a`.
The first-page temporary derived ledgers were not retained after the filter
failure.

```text
curl --get 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/' \
  --data-urlencode 'date_received_min=2025-01-01' \
  --data-urlencode 'date_received_max=2026-01-01' \
  --data-urlencode 'product=Debt collection' \
  --data-urlencode 'sub_product=Medical debt' \
  --data-urlencode 'size=1000' \
  -o /tmp/cfpb-debt-collection-2025-page1000.json
python3 scripts/build_cfpb_event_ledger_sample.py \
  /tmp/cfpb-debt-collection-2025-page1000.json \
  /tmp/cfpb-medical-debt-filtered-2025.json \
  --require-product 'Debt collection' \
  --require-sub-product 'Medical debt'
python3 scripts/validate_us_broad_event_ledger.py \
  /tmp/cfpb-medical-debt-filtered-2025.json
```

**Evidence status:** official API behavior and a locally verified bounded
medical-debt route sample observed; underlying bill, remedy, recovery, trust,
action, and exit remain unobserved.

**Source:** [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
