# CFPB consumer-outcome field audit v1

**Checked:** 2026-09-14  
**Status:** public API field gap recorded; no remedy estimate promoted

## Purpose

The CFPB complaint database exposes a useful institutional route from complaint
receipt to company response, but the end-to-end program needs to distinguish a
response label from an actual consumer outcome. This audit tests whether the
current public API supplies fields for dispute, correction, repeat effort, or
verified resolution.

## Probe

The public API was queried for three 2024 mortgage complaint records using the
documented endpoint and a fixed retrieval-order request:

```text
https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/
  ?date_received_min=2024-01-01
  &date_received_max=2025-01-01
  &product=Mortgage
  &size=3
```

The three returned records exposed these fields:

`company`, `company_public_response`, `company_response`, `complaint_id`,
`complaint_what_happened`, `date_received`, `date_sent_to_company`,
`has_narrative`, `issue`, `product`, `state`, `sub_issue`, `sub_product`,
`submitted_via`, `tags`, `timely`, and `zip_code`.

The probe did not expose a usable `consumer_disputed` value. In the returned
records the key was absent rather than a documented yes/no outcome. It also did
not expose a verified correction, amount returned, repeat contact, account
change, switching event, or post-response consumer assessment.

## Interpretation

The current public data can support:

- access and submission channel;
- CFPB receipt-to-company routing time;
- company response category;
- the database's timely-response field;
- narrative visibility;
- public company-response visibility;
- product, issue, company, and place context.

It cannot support a verified remedy rate or a same-case sequence of response,
correction, repeat effort, recovery, trust, switching, or exit. “Closed with
non-monetary relief,” “closed with explanation,” and “timely” remain
institutional record labels, not independently verified consumer outcomes.

## What would close the gap

The next consumer-power acquisition should seek one of the following:

1. a version of the complaint record containing a documented consumer-dispute or
   post-response field;
2. a repeat complaint or complaint-history identifier that permits same-consumer
   route analysis without exposing direct identifiers;
3. a consented consumer panel linked to product use, complaint effort, response,
   correction, financial recovery, switching, trust, or non-use;
4. firm or regulator administrative records verifying account correction,
   monetary payment, or other remedy.

Until one exists, the project should retain the current route and visibility
findings but should not convert response categories into remedy, trust, or exit
claims.

## Sources and reproducibility

- [CFPB complaint database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [CFPB API documentation](https://cfpb.github.io/api/ccdb/api.html)
- [CFPB field reference](https://cfpb.github.io/api/ccdb/fields.html)
- [Existing recourse visibility layer](cfpb-recourse-visibility-remedy-layer-v1.md)
- [Existing case-route sample](cfpb-case-route-sample-2024-v1.md)
- [Consumer recourse bridge](consumer-recourse-power-exit-cross-source-bridge-v1.md)

