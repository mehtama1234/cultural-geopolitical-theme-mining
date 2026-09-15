# CFPB API vintage refresh: metadata changed, route aggregates unchanged

**Checked:** 2026-09-14  
**Status:** verified no-change check for substantive 2025 route measures

## Query

The official CFPB complaint API was queried with:

```text
date_received_min=2025-01-01
date_received_max=2026-01-01
size=0
```

The committed reproducible snapshot is [cfpb-2025-aggregation-snapshot-2026-09-14.json](data/cfpb-2025-aggregation-snapshot-2026-09-14.json).
Its SHA-256 is
`2b9ddffb9fd3b44afbec0e55f4e233087706bcfa55638c3e17c846aa8b4c9b39`.

## What changed

| Field | 2026-09-13 snapshot | 2026-09-14 refresh |
|---|---:|---:|
| 2025 records received | 5,452,107 | 5,452,107 |
| CFPB index total | 17,729,722 | 17,737,752 |
| API last updated/indexed | 2026-09-13 12:00 ET | 2026-09-14 12:00 ET |
| stale flag | false | false |
| data issue flag | false | false |

The aggregate facets for company response, public response, narrative
presence, product, issue, state, submission channel, tags, and timeliness are
byte-equivalent after comparing the parsed aggregate objects. The raw response
hash changed because the API metadata changed.

## Live reproducibility recheck

The same fetcher was run again against the live API on 2026-09-14. It returned
the same 2025 record count and the same stored raw-response hash:

| Check | Committed snapshot | Live recheck |
|---|---:|---:|
| 2025 records received | 5,452,107 | 5,452,107 |
| CFPB index total | 17,737,752 | 17,737,752 |
| API last updated/indexed | 2026-09-14 12:00 ET | 2026-09-14 12:00 ET |
| Raw API response hash | `4b37229c3cc1a6d3422da03c6ec4fe6550ca2197d570c621c417259f2f3f5b65` | identical |

The committed JSON artifact hash remains
`2b9ddffb9fd3b44afbec0e55f4e233087706bcfa55638c3e17c846aa8b4c9b39`.

## Interpretation

This is a source-vintage control result, not a new consumer trend point. The
2025 product-response record remains numerically unchanged, while the current
index metadata is newer. The record still measures published complaint-system
endpoints, not representative consumer harm, account-denominated incidence,
verified remedy, recovery, trust, switching, or exit.

No existing trend observation was silently rehashed or replaced. Future
reproduction should retain both the earlier observation hashes and this newer
metadata snapshot when explaining the API vintage.

## Reproduction

```bash
python3 scripts/fetch_cfpb_complaint_aggregation.py \
  --date-min 2025-01-01 --date-max 2026-01-01 \
  --output /tmp/cfpb-2025-refresh-2026-09-14.json
```

Source: [CFPB Consumer Complaint Database API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/).
