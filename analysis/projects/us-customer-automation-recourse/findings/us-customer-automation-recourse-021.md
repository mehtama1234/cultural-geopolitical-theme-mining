# CFPB “timely” is not elapsed routing time, and the public field surface changes by vintage

**Status:** live CFPB API vintage and field-schema audit · **Checked:** 2026-09-15

## The bounded finding

The same CFPB complaint API exposes at least two different clocks:

- `timely`, an administrative response label; and
- the elapsed time between `date_received` and `date_sent_to_company`, a
  derived routing interval.

In a capped retrieval-order sample of 500 complaints per product, those clocks
do not always agree. In 2025, 59.8% of sampled student-loan records were
labelled `timely = Yes`, while 21.6% had a receipt-to-company-send interval
longer than 24 hours. The 90th-percentile routing interval was 649.6 hours,
about 27 days. A label that says “timely” therefore cannot be substituted for
elapsed routing time, let alone company resolution or consumer remedy.

The audit also found a vintage/schema boundary. The live API response returned
no `has_narrative` field in the 2024 or 2025 re-queries, even though the
committed earlier 2024 case-route record contains a narrative-presence measure.
The missing field must be treated as **unavailable**, not as 0% narrative
presence. A response-field change can look like a social or service trend if
the schema is not audited first.

## Product and vintage comparison

| Product | Year | Median routing hours | P90 routing hours | >24-hour routing | Timely = Yes | Public response present | Closed with explanation |
|---|---:|---:|---:|---:|---:|---:|---:|
| Checking/savings | 2024 | 0.29 | 1.30 | 3.4% | 99.0% | 47.6% | 77.4% |
| Checking/savings | 2025 | 0.43 | 1,342.98 | 33.4% | 98.4% | 33.2% | 86.2% |
| Credit reporting | 2024 | 0.06 | 0.29 | 0.0% | 99.6% | 31.4% | 44.2% |
| Credit reporting | 2025 | 0.17 | 3,008.83 | 39.0% | 98.6% | 68.0% | 87.8% |
| Mortgage | 2024 | 0.47 | 10.41 | 9.6% | 99.0% | 51.8% | 95.2% |
| Mortgage | 2025 | 0.59 | 2,533.82 | 30.6% | 97.4% | 35.2% | 94.6% |
| Student loan | 2024 | 0.30 | 23.72 | 10.0% | 95.2% | 46.6% | 97.4% |
| Student loan | 2025 | 0.36 | 649.57 | 21.6% | 59.8% | 9.2% | 61.0% |

The exact 2024 and 2025 rows are not a population trend estimate. Each is a
500-record retrieval-order sample, and the API's ordering and indexed fields
may change. The table is useful as a measurement audit and a product-specific
route comparison, not as an annual service-quality ranking.

The student-loan contrast is especially important. Its 2025 sample has the
lowest timely share and a long routing tail, but the same sample also has a
much lower public-response share and a different response mix. That could
reflect servicing, product events, API indexing, publication rules, issue mix,
or changes in how the records were returned. The public record does not tell
which explanation is correct.

## What changed in the evidence architecture

The earlier route layer treated `timely`, narrative presence, public response,
and routing lag as adjacent fields. This audit tightens the design:

| Field or measure | Safe interpretation | Unsafe substitution |
|---|---|---|
| `timely` | Published administrative label | Elapsed days, resolution, or remedy |
| Receipt-to-company-send lag | CFPB handoff interval where both timestamps exist | Company response time or consumer waiting time |
| `company_response` | Published response category | Verified correction, refund, restored access, or satisfaction |
| `company_public_response` | Public response field present | Proof of substantive engagement or success |
| `has_narrative` | Narrative-presence field only when returned and documented | Zero when the field is absent |
| 500-record API sample | Reproducible diagnostic slice | Representative customer population or incidence rate |

This distinction matters for the larger consumer-power theme. A customer may
receive a fast administrative handoff, an explanation, and no verified repair.
Another may wait longer in the public route but receive an effective correction.
The missing customer-side fields are effort, account exposure, requested
outcome, correction, money or access restored, repeat contact, dependence,
switching, trust, and exit.

## Counterexamples and boundaries

- A long routing interval can reflect an API timestamp, weekend/holiday timing,
  index behavior, or a real handoff delay; it is not automatically customer
  waiting time.
- A `timely = Yes` record can have a long derived lag because the fields encode
  different administrative concepts or coding rules.
- A high public-response share can coexist with lower narrative visibility, and
  neither establishes remedy.
- A response-label shift between vintages may reflect product mix, case mix,
  publication, servicing, or API changes rather than consumer welfare.
- The absence of `has_narrative` is missingness, not evidence that customers
  stopped writing narratives.
- The retrieval-order sample excludes customers who did not complain, could
  not reach the channel, abandoned the route, used another regulator, or were
  not published.

## The next decisive consumer-power test

The public API can now support a stronger field-stable route contract, but it
cannot close the customer outcome arrow. The next design should hold one
product and time window constant and capture:

```text
account exposure / problem
  -> attempted contacts and channel accessibility
  -> CFPB receipt and handoff
  -> company decision and authority to change it
  -> correction, payment, restored access, or denial
  -> repeat effort and residual loss
  -> continued dependence, switching, trust, or exit
```

The case ledger should record API field presence and definitions at every
vintage, preserve raw hashes, and refuse to convert omitted fields into zeros.
A consented account-level follow-up or lawful administrative linkage remains
the route to verified remedy and practical exit.

## Reproduction and sources

- [Machine-readable vintage record](../../../records/us-cfpb-case-route-vintage-comparison-2024-2025.json)
- [Reproduction script](../../../../scripts/analyze_cfpb_case_route_vintage_comparison.py)
- [Prior CFPB case-route finding](us-customer-automation-recourse-019.md)
- [2025 aggregate API vintage refresh](../cfpb-api-vintage-refresh-2026-09-14.md)
- [CFPB API field reference](https://cfpb.github.io/api/ccdb/fields.html)
- [CFPB complaint database](https://www.consumerfinance.gov/data-research/consumer-complaints/)

**Evidence status:** live, capped, product-stratified API vintage/schema audit.
No population complaint rate, consumer-harm rate, verified remedy, trust
change, switching rate, or political consequence is estimated.
