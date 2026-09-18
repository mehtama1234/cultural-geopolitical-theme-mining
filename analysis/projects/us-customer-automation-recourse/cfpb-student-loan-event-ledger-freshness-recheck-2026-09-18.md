# CFPB student-loan event-ledger freshness recheck — 2026-09-18

**Status:** bounded currentness audit; no consumer-outcome trend promoted

## Query and reproducibility

The CFPB Consumer Complaint Database API was queried for `product=Student
loan`, `date_received_min=2026-01-01`, `date_received_max=2026-09-19`, and
`size=25`. The API reported 14,696 matching records, and the first 25 returned
records were mapped with the existing
[`build_cfpb_event_ledger_sample.py`](../../../scripts/build_cfpb_event_ledger_sample.py)
builder. The retrieval-order sample is not random, weighted, or representative.

- Raw API input SHA-256: `3bba34a99b0b59a0ca1104273789a508142300b2bc249536139a945a419da7dc`
- Derived ledger SHA-256: `03ca06416daa5a1908f6206274bffa2b880f86f4a95c9de863d20ed813e2b59f`
- Observed sample dates: 2026-09-12 through 2026-09-16
- All 25 records were submitted through the Web

The derived ledger passed the broad event-ledger validator with 25 events and
2 arrows. The raw query was retrieved from the [CFPB public complaint
API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/).

## Bounded stage observations

| Administrative field | 2026 first-25 sample |
|---|---:|
| Timely = Yes | 25 |
| Timely = No | 0 |
| Company response = In progress | 13 |
| Company response = Closed with explanation | 12 |
| Public company response present | 1 |
| Public company response absent | 24 |
| Narrative present in derived record | 0 |

These are current administrative route labels in a retrieval-order sample.
“In progress,” “Closed with explanation,” and a public-response field do not
establish correction, payment, restored access, reduced obligation, repeat
effort, trust, switching, or exit. The derived ledger keeps alternatives,
effort, protected outcome, sacrificed outcome, and later outcome explicitly
unknown.

## Interpretation boundary

This recheck confirms that the public CFPB route can expose a current dated
complaint, responsible institutional route, and administrative response stage.
It does not close the broad program's end-to-end chain:

```text
complaint or burden
  -> verified correction or remedy receipt
  -> protected/sacrificed household outcome
  -> recovery, trust, action, switching, or exit
```

The 2026 sample must not be compared with the earlier 2024 or 2025 capped
samples as a trend without a stable query universe, field availability,
ordering rule, and denominator. It is a freshness checkpoint and a reusable
administrative counterexample, not a consumer-harm rate or remedy estimate.
