# CFPB public administrative event-ledger acquisition audit

**Checked:** 2026-09-14  
**Status:** bounded acquisition complete; no consumer-outcome trend promoted

## What this pass tested

The project needs an episode-level administrative layer between household
burden and later remedy. This pass tested whether the public CFPB complaint API
contains enough fields to build a de-identified event ledger for a small,
reproducible sample without inventing remedy, trust, or exit outcomes.

The answer is yes for complaint receipt, agency-to-company routing, submission
channel, narrative visibility, timeliness, and published company-response
labels. The answer is no for verified correction, money recovered, repeat
effort, switching, trust, or exit.

## Extract and reproduction

- Endpoint: CFPB Consumer Complaint Database public API
- Filter: `product=Student loan`, `date_received_min=2024-01-01`,
  `date_received_max=2025-01-01`, `size=25`
- Returned records: 25 of 14,685 matching records reported by the API
- Retrieval design: first 25 records returned by the public API; not a random
  sample and not population weighted
- Input SHA-256:
  `4695d731bf3fb27bbf043742d2bf720b48d54c672877d6fb6ade0752ea3814cc`
- Reproduction command:

  ```bash
  curl --get 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/' \
    --data-urlencode 'date_received_min=2024-01-01' \
    --data-urlencode 'date_received_max=2025-01-01' \
    --data-urlencode 'product=Student loan' \
    --data-urlencode 'size=25' \
    -o /tmp/cfpb-student-loan-2024-25.json
  python3 scripts/build_cfpb_event_ledger_sample.py \
    /tmp/cfpb-student-loan-2024-25.json \
    /tmp/cfpb-student-loan-event-ledger-2024-25.json
  python3 scripts/validate_us_broad_event_ledger.py \
    /tmp/cfpb-student-loan-event-ledger-2024-25.json
  ```

The reusable builder is [build_cfpb_event_ledger_sample.py](../../../scripts/build_cfpb_event_ledger_sample.py).
The committed [de-identified event-ledger extract](data/cfpb-student-loan-event-ledger-2024-25.json)
passed the broad event-ledger contract with 25 events and 2 arrows. Its
SHA-256 is `5f01d7ad212f87e98bb4d70cb89cdf06aadaf577580aef5f2fffc3701e02715f`.
It is a reproducible administrative sample extract, not a promoted trend
record.

## Fields that are directly usable

The public records support the following bounded observations:

- complaint receipt date, product, coarse state, and de-identified case key;
- date sent to company and derived receipt-to-send lag;
- submission channel and whether a narrative was present;
- `timely` label;
- company-response label and whether a public response was present.

The derived ledger also carries `protected_outcome` and `sacrificed_outcome`
for every case. Both are explicitly marked unobserved in this public extract;
the fields are present to prevent a future route label from being mistaken for
either preserved security or an inferred customer loss.

In this extract, all 25 records were submitted through the Web; 24 were
labelled timely and 1 untimely; 23 had “Closed with explanation” and 2 had
“Closed with non-monetary relief.” These counts describe this capped retrieval
sample only.

## Fields intentionally not claimed

The ledger does not treat a company-response label as a verified remedy. The
public route does not establish whether the customer received money, obtained
the requested correction, regained access, avoided repeat contact, changed
provider, continued using the service out of necessity, trusted the firm, or
exited. It also does not establish what the episode protected or sacrificed;
those two outcome fields remain unknown rather than being inferred from the
complaint or response label. Narrative presence is not narrative meaning, and a published complaint
is not a population incidence rate.

Direct identifiers, ZIP codes, company names, and narrative text are omitted
from the derived ledger. Complaint IDs are hashed only to provide stable keys
within this extract. No linkage to SHED, SIPP, ANES, FTC, or other sources is
claimed.

## 2025 retrieval-order comparison: diagnostic only

The same bounded query was fetched for `product=Student loan`,
`date_received_min=2025-01-01`, `date_received_max=2026-01-01`, and `size=25`.
The reusable builder now derives the sample year from the observed records
rather than embedding the 2024 label in every event. The 2025 input hash is
`365ae6ebc2d7020eeb2bcd3fd47d92785b82bc7f6a6d184a946fb9a9c1c0805c`.
The resulting 25-event ledger passed the broad event-ledger validator.

| Field in first 25 returned records | 2024 sample | 2025 sample |
|---|---:|---:|
| Timely = Yes | 24 | 15 |
| Timely = No | 1 | 10 |
| Closed with explanation | 23 | 16 |
| Closed with non-monetary relief | 2 | 0 |
| Untimely response label | 0 | 9 |
| Narrative present | 14 | 0 |
| Web submission | 25 | 23 |
| Phone/referral submissions | 0 | 2 |

These differences are not promoted as a 2024–2025 route trend. Both samples
are the first 25 API records returned, are not random or weighted, and can be
affected by API ordering, product composition, missingness, and publication
workflow. The sharp narrative difference is a useful counterexample: a change
in public visibility in a capped retrieval sample can reflect record ordering
or field availability rather than a change in consumer experience. A valid
time comparison requires a documented full query universe, stable fields,
product/sub-product conditioning, and a design that does not rely on the first
page of results.

## End-to-end implication

This pass strengthens the institutional middle of the atlas:

```text
household problem or loss
  -> complaint becomes visible
  -> CFPB routes it to a company
  -> company response label is published
  -> verified correction, recovery, repeat effort, trust, or exit
```

The first three arrows can be observed in public administrative records. The
last arrow remains an acquisition gap. The next substantive test is therefore
not another complaint aggregate; it is a lawful same-case or linked follow-up
design that adds attempted-but-unsubmitted contact, effort, authority to
change the decision, verified remedy, repeat contact, switching, dependence,
trust, and exit.

## Source

- [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [CFPB public complaint API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/)

The reusable [event-ledger builder](../../../scripts/build_cfpb_event_ledger_sample.py)
derives its period label from `date_received` so future samples cannot silently
inherit the wrong year.
