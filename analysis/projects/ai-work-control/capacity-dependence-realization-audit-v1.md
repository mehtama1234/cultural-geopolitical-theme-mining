# Capacity and dependence realization-stage audit v1

**Status:** stage-coverage audit; no capability, autonomy, or leverage estimate  
**Checked:** 2026-09-16  
**Cases:** US data-center capacity/governance and Poland JASSM-ER procurement  
**Machine-readable audit:** [capacity/dependence realization audit](data/capacity-dependence-realization-audit-v1.json)

## Question

The broader program asks when an announced strategic objective becomes usable
capacity, who controls it, who bears its costs, and whether another actor's
options actually change:

```text
objective or demand
  -> authorization/agreement
  -> named capacity and place
  -> delivery, operation, or accepted output
  -> control, maintenance, and replaceability
  -> public/partner outcome
  -> changed external behavior or leverage
```

The local ledgers allow this chain to be audited without treating every dated
record as the same kind of realization.

## Cross-case result

| Case | Observed or planned stages | Still not established |
|---|---|---|
| US data centers | Modeled national demand; local capacity/revenue; utility governance; two large-load drop events; customer-response records; comparator and non-observation records | Facility-level operating load tied to public cost, household/business incidence, ownership, replaceability, reliable service outcome, and public legitimacy |
| Poland JASSM-ER | Possible-sale authorization; procurement agreement; planned 2026–2030 delivery; technology-sensitivity modification; audit/control comparator | Specific-order production, shipment, acceptance, Polish unit receipt, training/fielding, inventory, operational availability, substitution, and external response |

The shared pattern is not “capacity failed” or “capacity succeeded.” It is
that commitments and some intermediate realization signals are visible before
the endpoints that make capacity politically meaningful: accepted output,
replaceability, distributional incidence, and changed behavior.

## Stage counts from the local ledgers

The machine audit classifies event types into comparable analytical stages;
this classification is a reading aid, not a new source claim.

| Case | Events | Commitment | Capacity/operation | Delivery/operation | Governance/external response | Missing-stage record |
|---|---:|---:|---:|---:|---:|---:|
| US data centers | 13 | 0 | 5 | 2 | 4 | 1 |
| Poland JASSM-ER | 7 | 3 | 0 | 1 planned | 0 | 1 |

The counts are not quantities, readiness scores, or comparable performance
rates. The data-center ledger has operating-stress and customer-response
events without a complete named-facility service outcome. The JASSM-ER ledger
has an authorization/agreement and planned delivery but no public record in
this packet proving shipment or acceptance of the specific 2024 order.

## Mechanism boundary

The most defensible current finding is:

> Strategic capacity becomes institutionally visible before its public,
> replaceability, and geopolitical consequences are fully observable.

For the data-center case, the next decisive join is facility or large-load
account → actual energized load → utility cost and reliability → affected
customer/public outcome → alternative or renegotiation. For the defense case,
it is order identifier → production/shipment → acceptance/training/fielding →
maintenance and inventory → substitution or partner/external response.

Neither chain should borrow evidence from the other. County revenue is not
missile delivery; a procurement agreement is not local operating load.

## Reproduction and storage boundary

```text
python3 scripts/audit_capacity_dependence_realization_ledgers.py
```

The audit reads the two existing local JSON ledgers, downloads nothing, and
does not infer household incidence, operational readiness, replaceability,
strategic autonomy, or geopolitical leverage.
