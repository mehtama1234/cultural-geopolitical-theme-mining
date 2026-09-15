# USAspending JASSM/LRASM award-detail case v1

**Checked:** 2026-09-13  
**Unit:** one DoD definitive contract award  
**Status:** case-level procurement/control record; no capability or leverage claim

## Case selected

The top transaction in the persisted FY2024 DoD retrieval is award
`FA868224CB001`, a Lockheed Martin Corporation contract described as large-lot
procurement for the Long Range Anti-Ship Missile / Joint Air-to-Surface
Standoff Missile. The USAspending award-detail response reports:

- total obligation: **$7.202B**;
- 74 subawards and **$1.143B** in total subaward amount;
- period of performance: **2024-09-27 through 2033-01-31**;
- JASSM/LRASM major program;
- NAICS 336414, guided missile and space vehicle manufacturing;
- one offer, not competed, only-one-source procedure;
- firm-fixed-price contract and a DoD comprehensive subcontract plan;
- US-owned business, with recipient and performance location in Orlando,
  Florida.

These fields materially improve the path from aggregate defense resources to a
specific contract, firm, place, program, competition condition, duration, and
subaward structure. They still do not establish that missiles were delivered,
that production capacity increased, that subcontractors benefited locally, or
that the contract changed US bargaining power.

The linked transaction-history retrieval returns **19 transactions** from the
initial September 2024 action through April 2026. Their net transaction amount
is $7.202B; four later actions have zero amount, and later positive
modifications include $1.444B in March 2025, $1.407B in July 2025, and $1.245B
in March 2026. This demonstrates that the initial award page is not the same
thing as the full time-ordered funding history. It still does not establish
delivery, acceptance, production rate, or operational readiness.

## End-to-end position

```text
military allocation
  -> contract obligation and procurement rule
  -> named firm, program, place, duration, and subcontract structure
  -> production, delivery, workforce, inputs, and local incidence
  -> readiness, strategic substitution, alliance behavior, or external response
```

The first three stages are documented for this case. The 74-record subaward
extract now identifies 51 reported subordinate recipients, with a total of
$1.143B; the largest reported recipient is BAE Systems Information and
Electronic Systems Integration Inc. at $210.019M (18.38% of the extract),
followed by L3Harris Cincinnati Electronics at $98.444M (8.62%). This is a
useful supplier-structure lead, but not a complete tier map or supplier-market
share. Delivery, modification history, supplier inputs, workforce, and
observed strategic or external response remain open. “One offer” and
“US-owned” are contract metadata, not proof of effective competition, domestic
self-sufficiency, or geopolitical autonomy.

The exact response is preserved at
[`data/usaspending-jassm-lrasm-award-detail-2026-09-13.json`](data/usaspending-jassm-lrasm-award-detail-2026-09-13.json).
The time-ordered transaction response is preserved at
[`data/usaspending-jassm-lrasm-transactions-2024-2026-09-13.json`](data/usaspending-jassm-lrasm-transactions-2024-2026-09-13.json).
The raw subaward response is preserved at
[`data/usaspending-jassm-lrasm-subawards-2026-09-13.json`](data/usaspending-jassm-lrasm-subawards-2026-09-13.json),
with the reproducible profile at
[`data/usaspending-jassm-lrasm-subaward-profile-2026-09-13.json`](data/usaspending-jassm-lrasm-subaward-profile-2026-09-13.json).
The first corporate ownership reconciliation is documented in the
[subaward ownership route](usaspending-jassm-lrasm-subaward-ownership-route-v1.md).

## Reproduction

```text
python3 scripts/fetch_usaspending_award_detail.py \
  --award-id CONT_AWD_FA868224CB001_9700_-NONE-_-NONE- \
  --output analysis/projects/ai-work-control/data/usaspending-jassm-lrasm-award-detail-2026-09-13.json
```

Official source: [USAspending award API](https://api.usaspending.gov/api/v2/awards/).
Subaward route: [USAspending subawards API](https://api.usaspending.gov/api/v2/subawards/).
