# USAspending defense transaction profile v1

**Checked:** 2026-09-13  
**Unit:** transaction in a bounded USAspending FY2024 DoD retrieval page  
**Status:** descriptive procurement-concentration diagnostic

## What this pass adds

The acquisition gate now moves from “transactions exist” to “which visible
recipients, places, and industrial codes carry the page.” The profile is run
over the persisted 100-row transaction artifact, which is sorted by transaction
amount. It is therefore useful for selecting cases, not for estimating DoD
supplier shares or total procurement.

The page total is **$69.67 billion** across 100 transactions and **34 named
recipients**. Lockheed Martin Corporation carries the largest page total at
about $15.28 billion, including a
$2.423-billion transaction for a long-range anti-ship/joint air-to-surface
standoff missile large-lot procurement. The next visible transactions include
Boeing aircraft work, Humana managed-care support, Northrop Grumman strategic
systems, and shipbuilding awards. This mixes weapons, engineering/manufacturing,
health services, and construction: transaction amount is not a capability
measure.

## Interpretation boundary

The profile identifies candidate firms, states, NAICS codes, and product/service
codes for the next case audit. It does not show parent ownership, domestic or
foreign inputs, small-business status, subcontracting, delivery, performance,
jobs, wages, industrial bottlenecks, or actual strategic output. A large
transaction can be an advance procurement, modification, funding action, or
multi-year contract rather than delivered equipment.

```text
military budget
  -> transaction and recipient visibility
  -> contract/product/place case selection
  -> delivery, supplier, workforce, and ownership audit
  -> realized capability and domestic/alliance incidence
  -> observed state or external response
```

The exact machine-readable profile is
[`data/usaspending-defense-transaction-profile-fy2024-2026-09-13.json`](data/usaspending-defense-transaction-profile-fy2024-2026-09-13.json).
Its input is the [persisted transaction artifact](data/usaspending-dod-transactions-fy2024-2026-09-13.json).

## Reproduction

```text
python3 scripts/analyze_usaspending_defense_transactions.py \
  --input analysis/projects/ai-work-control/data/usaspending-dod-transactions-fy2024-2026-09-13.json \
  --output analysis/projects/ai-work-control/data/usaspending-defense-transaction-profile-fy2024-2026-09-13.json
```

Next test: select a weapon-system and a service/health transaction, then inspect
recipient ownership, contract modifications, performance, place, workforce,
inputs, and delivery records. Keep the two cases separate until a shared unit
supports a stronger industrial or geopolitical conclusion.
