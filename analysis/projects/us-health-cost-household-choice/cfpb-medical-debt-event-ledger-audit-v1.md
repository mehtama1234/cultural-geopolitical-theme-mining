# CFPB medical-debt complaint event-ledger audit v1

**Checked:** 2026-09-17  
**Status:** bounded administrative-route acquisition and vintage diagnostic; no prevalence or remedy estimate
**Machine records:** [2024 ledger](data/cfpb-medical-debt-event-ledger-2024.json) and [2025 recheck ledger](data/cfpb-medical-debt-event-ledger-2025.json)

## What this pass establishes

The CFPB Consumer Complaint Database can supply a small, dated institutional
route layer for medical-debt episodes. A query for `product=Debt collection`,
`sub_product=Medical debt`, received from 2024-01-01 through 2024-12-31, with
`size=25`, returned 25 records. The derived ledger retains de-identified case
keys, coarse state, receipt date, routing date, submission channel, narrative
presence, timeliness, and company-response labels.

```text
medical-debt complaint received
  -> CFPB-to-company routing
  -> published response label
  -> verified correction, recovery, trust, or exit [open]
```

The first 25 returned records are not a random or weighted sample. In the
2024 retrieval their dates run from 2024-08-25 through 2024-09-04 and cover 17
states. All 25 were web submissions. Sixteen were labelled `Closed with
explanation` and nine `Closed with non-monetary relief`; six had a public
response flag and 19 did not. These are retrieval-sample and
administrative-field counts only.

## 2025 vintage recheck

The same capped query for received dates in 2025 returned another 25 cases,
spanning 2025-07-18 through 2025-12-02 and 16 states. All 25 were web
submissions. Twenty-four were labelled `Closed with explanation` and one
`Closed with monetary relief`; 24 were timely and one untimely; seven had a
public response flag and 18 did not. None of the fields verifies that the
complainant received money, correction, restored access, or durable relief.

| Field | 2024 first 25 | 2025 first 25 | Interpretation |
|---|---:|---:|---|
| Records | 25 | 25 | Same cap, not the same universe or sampling design |
| States represented | 17 | 16 | Retrieval composition only |
| Closed with explanation | 16 | 24 | Administrative label; not outcome severity |
| Closed with non-monetary relief | 9 | 0 | Administrative label; not verified relief |
| Closed with monetary relief | 0 | 1 | Label does not establish payment receipt or amount |
| Timely = Yes | 25 | 24 | Routing/response field; not customer recovery |
| Public response present | 6 | 7 | Publication visibility; not remedy or trust |

The differences must not be promoted as a 2024–2025 route trend. The API
returns the first 25 records, with no randomization or population weights in
this extract; the observed date spans and ordering differ. A valid vintage
comparison requires a documented full query universe, stable field definitions,
and a design that addresses product mix, publication, missingness, and
ordering.

## Stage coverage and missingness

| Stage | Status | Boundary |
|---|---|---|
| Dated complaint and coarse place | Observed | Complaint-selected cases; non-users and abandoned attempts are outside the denominator |
| Institutional route | Observed | Receipt and company-send dates support a derived routing lag; effort and authority are not measured |
| Response label | Observed | Timeliness and company-response fields are administrative labels |
| Medical bill, care choice, or obligation | Not observed | The public complaint extract does not identify amount owed, due date, treatment continuity, or available alternative |
| Verified remedy or recovery | Not observed | Non-monetary relief is not proof of correction, money recovered, or burden removed |
| Meaning, trust, action, or exit | Not observed | Narrative presence is not coded meaning; no follow-up identifies repeat effort, switching, dependence, or exit |

The 2024 raw API response hash is
`cca7bf4be079a18042f0092d0b35429f929d777891fa5c5462122450f9d8d59c`; its
committed de-identified ledger hash is
`886e0281885370ee923c6805de1c3580bd6098b538f006463434018e62cf7586`. The
2025 raw response hash is
`50175a48dd86ced79469d4522d63739dd544356951c3283155e453057e8b9807`; its
ledger hash is
`308a56c426847ac64632558b2ecbd591ecd9a7c76162a581f518157c01355355`.
Direct identifiers, company names, ZIP codes, and narrative text are omitted.

## Why this advances the broad goal

This is a concrete medical-cost institutional middle, not a claim that
medical debt caused later distrust or political action. It makes the next
missing fields operational: link a lawful complaint or account episode to the
underlying bill or care decision, effort and alternatives, verified correction
or payment, repeat contact, and later recovery or exit. MEPS remains the
person-linked event and health/work context layer; this CFPB ledger remains a
separate administrative-case layer. Their identifiers cannot be merged.

## Reproduction

```text
curl --get 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/' \
  --data-urlencode 'date_received_min=2024-01-01' \
  --data-urlencode 'date_received_max=2025-01-01' \
  --data-urlencode 'product=Debt collection' \
  --data-urlencode 'sub_product=Medical debt' \
  --data-urlencode 'size=25' \
  -o /tmp/cfpb-medical-debt-2024.json
python3 scripts/build_cfpb_event_ledger_sample.py \
  /tmp/cfpb-medical-debt-2024.json \
  /tmp/cfpb-medical-debt-event-ledger-2024.json
python3 scripts/validate_us_broad_event_ledger.py \
  /tmp/cfpb-medical-debt-event-ledger-2024.json
```

The 2025 recheck uses the same command with the received-date bounds changed
to `2025-01-01` and `2026-01-01`, writing
`/tmp/cfpb-medical-debt-event-ledger-2025.json`.

**Evidence status:** public administrative route observed in two bounded
vintages; underlying medical episode, household burden, remedy receipt,
recovery, trust, action, and exit remain unobserved.

**Source:** [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
