# A broad defense supplier surface can remain financially concentrated

**Status:** bounded USAspending supplier-concentration finding · **Checked:** 2026-09-15

## The short finding

The JASSM/LRASM USAspending subaward extract contains 74 returned records and
51 distinct reported recipient names. That breadth is real as a description of
the returned records, but it does not establish supplier independence or
replaceability. The five largest reported recipients account for 49.50% of the
returned-record amount, and the ten largest account for 74.60%. Seventeen of
the 51 recipient names appear in more than one returned record.

The useful distinction is **component diversity versus bargaining diversity**.
Many names and many component descriptions can coexist with financial and
program dependence on a smaller set of major participants.

| Surface | Result | What it supports | What it does not support |
|---|---:|---|---|
| Returned subaward records | 74 | Observable procurement subaward surface | Complete supply chain or all tiers |
| Distinct reported recipient names | 51 | Multiple named participants | Independent legal entities, competing substitutes, or geographic resilience |
| Five-largest recipient share | 49.50% of returned amount | Material concentration in the extract | Market-power estimate or single-point failure |
| Ten-largest recipient share | 74.60% | A long tail does not mean equal bargaining weight | Replaceability or competition |
| Recipient names repeated across records | 17 of 51 | Some participants receive multiple reported actions/lots | Production continuity, capacity, or output |
| Amount-based HHI | 0.077644 | A reproducible concentration diagnostic for this extract | Defense-industry HHI or program-level resilience |

## Why “51 suppliers” is an incomplete capability claim

The source is a single parent award and one returned subaward response. It
contains reported names, amounts, dates, and free-text descriptions. It does
not provide a reconciled corporate-parent tree, facility location, ownership,
contract tier, production quantity, delivery, acceptance, inventory, workforce,
or substitute supplier. A named recipient may be a component specialist, a
repeat lot recipient, a subsidiary, or a reporting artifact rather than an
independent source of operational capability.

The text descriptions also span different layers of a system. The 74 records
include terms such as covers, wings, hoses, antennas, power components,
connectors, processors, printed wiring, and other parts. The terms overlap and
are not a bill of materials. They show what was written in the returned
subaward descriptions, not what was manufactured, integrated, delivered, or
available at scale.

The concentration result therefore changes the state-capacity question. It is
not enough to ask whether a state has a broad supplier network. The next
questions are:

- Which recipients roll up to the same corporate parent?
- Which facilities actually perform the work, and are they geographically or
  operationally substitutable?
- Which component is single-sourced or difficult to qualify elsewhere?
- Are repeated actions new lots, modifications, testing, maintenance, or
  production?
- What inventory, acceptance, delivery, and sustainment evidence exists?
- Can a buyer switch suppliers without losing schedule, certification, or
  interoperability?

## The state-leverage chain remains open

```text
budget and strategic intent
  -> award and subaward route
  -> supplier and component concentration
  -> production, delivery, acceptance, and sustainment
  -> replaceability and operational option
  -> observed state choice, external response, or leverage
```

This pass strengthens only the concentration stage. It does not show that the
United States or a partner can impose terms, that an adversary changed
behavior, or that a local community gained jobs or resilience. A concentrated
supplier structure could be efficient and well-buffered, or fragile and hard
to replace; the extract cannot distinguish those cases.

## Counterexamples and safeguards

- A broad supplier list can reflect prime-contractor reporting rather than
  genuine competition.
- A concentrated amount share can coexist with many technically substitutable
  suppliers, or with one irreplaceable low-dollar component.
- A repeat recipient can indicate scale, reliability, or dependence; without
  output and contract terms it does not identify which.
- A small supplier can be strategically critical despite a small award amount.
- A domestic recipient name does not establish domestic inputs, facility
  location, workforce benefit, or insulation from foreign dependencies.
- A component description does not prove delivery or integration into an
  accepted weapon system.

## Next decisive test

The next procurement pass should link each reported recipient to a legal parent,
facility, component class, action type, and program milestone. It should then
join award modifications, delivery/acceptance records, production or inventory
evidence, and substitute-supplier or qualification records. A valid leverage
claim requires an observed external decision or changed terms—not merely a
large award, a domestic facility, or a broad recipient list.

## Reproduction and sources

- [Machine-readable concentration record](../../../records/usaspending-jassm-lrasm-supplier-concentration-2024-2025.json)
- [Reproduction script](../../../../scripts/analyze_usaspending_supplier_concentration.py)
- [Committed USAspending subaward response](../data/usaspending-jassm-lrasm-subawards-2026-09-13.json)
- [Prior staged defense-capability finding](ai-work-control-066.md)
- [USAspending subaward acquisition layer](../usaspending-defense-award-acquisition-layer-v1.md)
- [USAspending API documentation](https://api.usaspending.gov/docs/endpoints)

**Evidence status:** inferred concentration metrics from one bounded official
subaward extract. No supplier-market, production, readiness, replaceability,
local-incidence, or geopolitical-leverage estimate is made.
