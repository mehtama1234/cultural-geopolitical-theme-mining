# CFPB narrative filtering did not expose a narrative-bearing case surface

**Checked:** 2026-09-18  
**Status:** live public-API schema and filter boundary; no consumer outcome promoted

## The bounded probe

The public CFPB complaint API was queried twice with the same narrow route:
`product = Credit card`, `company_response = Closed with monetary relief`,
complaints received from `2025-01-01` through `2026-09-18`, `field = all`, and
`size = 25`. The probe added `has_narrative = true`; the control omitted that
parameter.

Both requests reported 21,425 matching records and returned 25 records. The
returned complaint IDs were identical. Both responses exposed the same 15
administrative fields and neither exposed `complaint_what_happened` or a
usable `has_narrative` field.

This result is stronger than simply observing a missing field in one response:
within this tested query shape, the narrative filter did not change the
retrieval. It still does not prove that narratives are absent from every CFPB
endpoint, vintage, access tier, or administrative system.

## What the API can and cannot establish here

```text
credit-card complaint
  -> public CFPB receipt and company routing
  -> published response category
  -> [not exposed in this route] narrative meaning or alternative decision
  -> [open] verified relief, correction, repeat effort, trust, switching, exit
```

The response category remains a company-reported administrative label. Even a
future narrative-bearing record would be a self-report unless independently
linked to a remedy or account outcome. The current response does not support
coding an alternative, non-use decision, remedy receipt, or exit event.

The test therefore does not qualify the broad same-case promotion gate. It
does, however, close one acquisition ambiguity: repeating the same public API
probe with the tested narrative filter is unlikely to add the missing
consumer-power fields. The next useful route must be a lawful linked,
consented, or account-level follow-up source rather than another parameter
variant of this response slice.

## Counterexamples and missingness discipline

- A missing narrative field is not a zero-narrative finding.
- `has_narrative=true` returning the same IDs is not proof that the filter is
  semantically implemented; it is evidence only about the observed response.
- `Closed with monetary relief` is not proof of amount, issuance, receipt, or
  correction.
- A complaint record is not a measure of all affected consumers, including
  people who could not complain, abandoned the route, or used another channel.

## Reproduction and storage

The [machine-readable probe record](data/cfpb-narrative-filter-probe-2026-09-18.json)
preserves the exact filters, response hashes, field inventory, and bounded
interpretation. Raw responses, direct identifiers, and narrative text were not
retained.

Source: [CFPB Consumer Complaint Database public API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/).
