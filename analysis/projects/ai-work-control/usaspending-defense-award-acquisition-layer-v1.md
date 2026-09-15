# USAspending defense-award acquisition layer v1

**Checked:** 2026-09-13  
**Unit:** DoD award- or transaction-level API record  
**Status:** reusable award and transaction acquisition route; no procurement or capability estimate

## Why this is the next gate

SIPRI measures national military-resource allocation but not the procurement
system through which resources become contracts, suppliers, places, workers,
technology, or delivered capability. The official USAspending API exposes a
bounded award-level route filtered to the Department of Defense and fiscal-year
date windows.

The first probe returned award records with award ID, award amount, awarding
agency, and recipient name. A transaction-level probe now returns transaction
amount, action date, description, NAICS, product/service code, and place of
performance state. This makes procurement visibility more useful, but neither
retrieval should be described as total DoD procurement or production.
The verified FY2024 transaction retrieval returned 100 records; its raw
response hash was `sha256:ae538871b6f887ed00b154c040c69bd3b896d4de48d8cb9f66fcac51aaeafe64`.
The exact acquisition output is preserved at
[`data/usaspending-dod-transactions-fy2024-2026-09-13.json`](data/usaspending-dod-transactions-fy2024-2026-09-13.json).

## Reproduction

```text
python3 scripts/fetch_usaspending_defense_awards.py \
  --start-date 2023-10-01 --end-date 2024-09-30 --level transaction --limit 100 \
  --output /tmp/usaspending-dod-awards-fy2024.json
```

The output preserves the request body, endpoint, raw-response SHA-256, page
metadata, returned records, and boundary. The API result is a retrieval page,
not a weighted sample. Transaction obligations are not delivered hardware,
service quality, readiness, jobs, local benefit, or state leverage. Award-level
retrieval remains available with `--level award`.

## Required next fields

1. award type and transaction-level obligations rather than one award-page
   amount;
2. recipient parent, place, product/service code, and small-business status;
3. contract duration, modifications, cancellations, delivery, and performance;
4. supplier concentration and domestic/foreign input or ownership exposure;
5. workforce, production, inventory, and local incidence; and
6. a dated procurement, substitution, refusal, or alliance event showing an
   actual change in capability or external behavior.

This is therefore an acquisition control that connects SIPRI's resource layer
to the next measurable institutional stage. It does not close the geopolitical
leverage arrow.

Official source: [USAspending API](https://api.usaspending.gov/docs/endpoints),
[USAspending](https://www.usaspending.gov/).
