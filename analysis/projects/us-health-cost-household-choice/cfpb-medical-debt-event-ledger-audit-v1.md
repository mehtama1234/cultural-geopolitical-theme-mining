# CFPB medical-debt complaint event-ledger audit v1

**Checked:** 2026-09-17  
**Status:** bounded administrative-route acquisition; no prevalence or remedy estimate  
**Machine record:** [de-identified medical-debt event ledger](data/cfpb-medical-debt-event-ledger-2024.json)

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

The first 25 returned records are not a random or weighted sample. Their dates
run from 2024-08-25 through 2024-09-04 and cover 17 states. All 25 were web
submissions. Nineteen were labelled `Closed with explanation` and six
`Closed with non-monetary relief`; 22 had a public response flag and three did
not. These are retrieval-sample and administrative-field counts only.

## Stage coverage and missingness

| Stage | Status | Boundary |
|---|---|---|
| Dated complaint and coarse place | Observed | Complaint-selected cases; non-users and abandoned attempts are outside the denominator |
| Institutional route | Observed | Receipt and company-send dates support a derived routing lag; effort and authority are not measured |
| Response label | Observed | Timeliness and company-response fields are administrative labels |
| Medical bill, care choice, or obligation | Not observed | The public complaint extract does not identify amount owed, due date, treatment continuity, or available alternative |
| Verified remedy or recovery | Not observed | Non-monetary relief is not proof of correction, money recovered, or burden removed |
| Meaning, trust, action, or exit | Not observed | Narrative presence is not coded meaning; no follow-up identifies repeat effort, switching, dependence, or exit |

The raw API response hash is `cca7bf4be079a18042f0092d0b35429f929d777891fa5c5462122450f9d8d59c`.
The committed de-identified ledger hash is
`886e0281885370ee923c6805de1c3580bd6098b538f006463434018e62cf7586`.
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

**Evidence status:** public administrative route observed; underlying medical
episode, household burden, remedy receipt, recovery, trust, action, and exit
remain unobserved.

**Source:** [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
