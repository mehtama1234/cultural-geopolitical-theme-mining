# CFPB student-loan timing fields are not interchangeable

**Status:** checked · **Checked:** 2026-09-13

## One-sentence finding

For published student-loan complaints, the API’s separate `timely = No` field
rose from 5.6% in 2024 to 30.4% in 2025, while the
`company_response = Untimely response` category rose from 0.3% to 15.9%; the
fields describe different recorded endpoints and must not be collapsed into a
single remedy or harm measure.

## The field audit

| Year | Records | Company response: untimely | Timely field: no | Company response: in progress |
|---|---:|---:|---:|---:|
| 2024 | 14,685 | 0.3% | 5.6% | 0.0% |
| 2025 | 21,333 | 15.9% | 30.4% | 0.9% |

The CFPB’s 2025 Consumer Response Annual Report provides rounded external
context of roughly 31% of student-loan complaints receiving no timely response
or no response. That is consistent in scale with the API’s `timely = No` field,
not interchangeable with the narrower company-response category.

## Why the distinction matters

```text
complaint enters a product-specific route
  -> timing/status field is recorded
  -> company response category is recorded
  -> correction, payment, restored access, repeat effort, or trust may follow
```

The API exposes two administrative fields at different stages or definitions.
The audit establishes a measurement boundary, not the reason for the gap. A
large `timely = No` share may indicate no timely response, while the company
response category may classify only a subset as an explicitly untimely response.
The exact field semantics and case sequence require targeted documentation and
micro-level review.

## What is still open

- elapsed days from complaint receipt to company response;
- servicing company, transfer date, and borrower notice;
- payment status, deferment/forbearance, credit reporting, or financial loss;
- independently verified correction or remedy;
- repeat contact, abandonment, switching, trust, or political action.

The spike should therefore be treated as an institutional-capacity audit target,
not a causal claim that student-loan borrowers experienced a uniform servicing
failure. A field-definition or servicing correction that removes the gap would
be a direct counterexample to a deterioration interpretation.

## Sources

- [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [CFPB 2025 Consumer Response Annual Report](https://www.consumerfinance.gov/data-research/research-reports/2025-consumer-response-annual-report/)
- [CFPB API field reference](https://cfpb.github.io/api/ccdb/fields.html)
- [Machine-readable field-audit record](../../../records/us-cfpb-student-loan-timing-field-audit-2024-2025.json)
