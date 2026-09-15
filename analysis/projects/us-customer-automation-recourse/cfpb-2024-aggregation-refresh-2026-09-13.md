# CFPB 2024 complaint aggregation refresh v1

**Checked:** 2026-09-13  
**Status:** current official aggregate snapshot; institutional-response evidence,
not a consumer-outcome estimate

## Acquisition

The official [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
API was queried through its documented trailing-slash endpoint:

`https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/`

The query used `date_received_min=2024-01-01`,
`date_received_max=2025-01-01`, and `size=0`, retaining the API aggregate
facets and metadata without downloading complaint narratives. The reusable
fetcher is [fetch_cfpb_complaint_aggregation.py](../../../scripts/fetch_cfpb_complaint_aggregation.py).

## Current snapshot

| Measure | Value |
|---|---:|
| Published complaint records received in 2024 | 2,739,722 |
| CFPB database records in the current index | 17,729,722 |
| API last updated/indexed | 2026-09-13 12:00 ET |
| Data stale flag | false |
| Data issue flag | false |

The 2024 total reproduces the earlier response-route layer. The current index
metadata changed since the prior snapshot, so future refreshes must preserve
the retrieval hash and metadata rather than treating the record count as
timeless.

## Date-boundary recheck

On 2026-09-14, the exact prior request boundary was rerun. The endpoint with
`date_received_max=2025-01-01` again returned **2,739,722** records, with raw
response hash `7d69a20e59b327e086119e26e06e5d57f2ec9c80d8769d106abe0935fb0266cf`.
A strict `date_received_max=2024-12-31` request returned **2,734,269** records,
with hash `4ebb44832834689ff160161bb0b0a375de955282b539de8904a048ade9b44ebf`.
The difference is **5,453** records. This recheck prevents the difference from
being mislabeled as an index revision: the API's maximum-date boundary is
material to the count and the prior “2024” snapshot includes a boundary
condition that must be preserved in any comparison. Future annual extracts
should use explicit inclusive/exclusive semantics and report the exact request
URL alongside the count.

The same official query for calendar 2025 returns 5,452,107 published records
in the current index. The index metadata remains current and reports 17,729,722
records overall. The 2025 snapshot is preserved separately because its response
mix includes an in-progress category and cannot be treated as a mechanically
identical endpoint without checking the taxonomy.

## Program connection

This advances themes 3, 9, and 12: consumer recourse, cultural meaning and
trust, and firm/market power. The next missing arrow remains a same-case or
linked follow-up from complaint contact through verified remedy, repeat effort,
dependence or exit, and later trust. Complaint aggregates cannot supply that
arrow and must not be joined to SIPP or ANES as if they identify the same
people.

The [2020–2025 annual response record](../../records/us-cfpb-annual-response-trend-2020-2025.json)
now extends the visible institutional trend through 2025. The 2025 share
marked explanation rises to 58.706%, while non-monetary relief falls to 40.633%,
monetary relief to 0.480%, and published narratives to 22.426%. These are
changes in the recorded complaint system, not verified changes in consumer
outcomes; product mix, publication, routing, coding, and index timing remain
possible explanations.
