# CFPB credit-card monetary-relief response slice recheck

**Checked:** 2026-09-18  
**Status:** current administrative response-category slice; lived remedy open

## What was tested

The CFPB public complaint API was queried for a narrow current response
category: `product = Credit card`, `company_response = Closed with monetary
relief`, and complaints received from 2025-01-01 through 2026-09-19. The API
reported 21,425 matching records. The first 25 returned records were mapped
through the existing de-identified event-ledger builder and passed its broad
event-ledger contract with 25 events and 2 arrows.

This is a response-category-conditioned sample. It is not a monetary-relief
rate, a random sample, a population estimate, or evidence that any consumer
received money.

## Bounded observed surface

| Field | Result in the first 25 returned records | Safe interpretation |
|---|---:|---|
| Company response filter | 25 `Closed with monetary relief` | A published company-response category is selected by design |
| Observed complaint dates | 2026-09-08 to 2026-09-16 | The current retrieval reaches recent records |
| Timely response | 25 Yes | Administrative timeliness label in the selected slice |
| Submission channel | 23 Web; 2 Referral | Route composition of the capped retrieval sample |
| Public company response | 15 present; 10 absent | Public-response availability, not remedy quality |
| Narrative field | 0 present in the returned records | Narrative absence is not absence of harm or explanation |

The current raw API hash is
`75b9ef375a866c22f9a8e225c493a2d6d8d3c4ae688eb5d90c2325cf1029853b`; the
retained de-identified ledger hash is
`ca343abee12c2e4fedb614d245824918e31bdc899eab4511edfb976cc8232be4`. The
compact [machine recheck record](data/cfpb-credit-card-monetary-relief-event-ledger-recheck-2026-09-18.json)
and [event ledger](data/cfpb-credit-card-monetary-relief-event-ledger-v1.json)
preserve the query, hashes, denominator, and field diagnostics without
retaining raw complaint narratives or direct identifiers.

## End-to-end boundary

```text
credit-card complaint
  -> CFPB publication and company routing
  -> company-response label: Closed with monetary relief
  -> [open] relief amount, issuance, receipt, account correction,
           remaining loss, repeat effort, trust, switching, or exit
```

The label advances the formal-response stage beyond an unconditioned complaint
sample, but it remains company-reported administrative metadata. The public
record does not establish whether money was issued, how much was received,
whether an account or credit record was corrected, whether the consumer still
had a loss, or whether the consumer continued, switched, stopped using, or
changed trust.

The 21,425 count is the filtered API universe reported for this query. The
25-row retrieval is not a denominator for the response category because the
query already selects that category and the API ordering is not a sampling
design. The dates also show current publication reach, not the date of the
underlying credit-card problem or payment correction.

## Decision for the broad program

This route is now a reusable formal-remedy comparator: it supplies a current
case date, a product-conditioned route, and a monetary-response label while
preserving the missing lived-outcome fields. It does not qualify the same-case
promotion gate, which still requires episode-level alternatives or non-use plus
verified remedy receipt or outcome follow-up. The next consumer-power test is
a lawful linked or account-level implementation record, not another
response-category slice.

The 25 de-identified events are now retained in the [versioned event ledger](data/cfpb-credit-card-monetary-relief-event-ledger-v1.json)
and indexed with the other real broad ledgers. This preserves administrative
route evidence without changing the lived-remedy boundary.

## Reproduction

```text
curl --get 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/' \
  --data-urlencode 'product=Credit card' \
  --data-urlencode 'company_response=Closed with monetary relief' \
  --data-urlencode 'date_received_min=2025-01-01' \
  --data-urlencode 'date_received_max=2026-09-19' \
  --data-urlencode 'size=25' \
  -o /tmp/cfpb-credit-card-monetary-relief-2025-2026.json
python3 scripts/build_cfpb_event_ledger_sample.py \
  /tmp/cfpb-credit-card-monetary-relief-2025-2026.json \
  /tmp/cfpb-credit-card-monetary-relief-event-ledger.json \
  --require-product 'Credit card'
python3 scripts/validate_us_broad_event_ledger.py \
  /tmp/cfpb-credit-card-monetary-relief-event-ledger.json
```

The raw API JSON was used transiently and is not retained. The derived,
de-identified event ledger is retained for reproducible contract validation.
