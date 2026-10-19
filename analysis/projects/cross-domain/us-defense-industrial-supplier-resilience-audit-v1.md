# U.S. defense-industrial supplier resilience and replaceability audit v1

Date: 2026-10-18  
Status: active U.S. industrial/geopolitical rotation; bounded JASSM/LRASM case

## Research question

When a U.S. defense program reports many suppliers, a higher production rate,
and allied procurement, does that create replaceable and delivered capability—or
only a broad contract surface whose concentration, facility assignment, and
fielded output remain uncertain?

The chain under test is:

`strategic requirement -> prime award and supplier network -> production and
integration -> accepted delivery and inventory -> substitute/repair capacity ->
allied resilience, deterrence, and public-industrial legitimacy`.

## Evidence ledger

| Stage | Evidence | What it supports | Boundary |
|---|---|---|---|
| Supplier surface | [USAspending concentration record](../../records/usaspending-jassm-lrasm-supplier-concentration-2024-2025.json): 74 returned subaward records totaling $1.1427B, 51 reported recipient names, top five representing 49.5004% and top ten 74.595% of returned amount; extract HHI 0.077644. | The bounded award extract has both recipient breadth and financial concentration. | One parent award/page; names are not reconciled to legal entities/ownership; subaward visibility, locations, amendments, and production are incomplete. |
| Component diversity | [USAspending subaward structure](../../records/usaspending-jassm-lrasm-subaward-structure-2024-2025.json) reports component/assembly descriptions across all 74 records, including engines, processors, antennas, warheads, wings, tails, optics, power, and connectors. | The reported network spans multiple system elements. | Free-text descriptions are not a bill of materials, quantities, manufacture, integration, delivery, or competition measure. |
| Corporate footprint | [Multi-facility recipient route](../../records/usaspending-jassm-lrasm-multi-facility-recipient-route-2024-2025.json) maps one General Dynamics OTS recipient name and $80.5508M reported amount to three active CAGE facilities in Hampton AR, Colchester VT, and Saco ME under parent CAGE 95403. | A corporate recipient can have geographically distributed registered facilities. | The subaward lacks the identifier needed to assign the work to a facility; footprint is not redundancy or replaceability. |
| Production capacity | [Air Force production/integration record](../../records/us-jassm-lrasm-production-integration-realization-2024-2025.json) reports Lockheed Martin in Troy, Alabama and a FY2026 combined minimum sustained rate of 396 missiles/year: 336 JASSM and 60 LRASM. | A government exhibit reports a defined production-rate target and a capacity expansion rationale. | Minimum sustained rate is not realized throughput, accepted output, inventory, staffing, yield, or delivery. |
| Production investment | The same record cites a 225,000-square-foot facility brought online in 2022 and a corporate claim to accelerate deliveries. | Capacity investment and management claims are observable intermediate stages. | No quantity, delivery, acceptance, uptime, or customer-allocation evidence is supplied. |
| Integration | The record reports an initial LRASM/F-35B flight test on March 4, 2025 at Naval Air Station Patuxent River, with an independent F-35C loaded-missile test context. | Integration testing moved beyond a plan into dated events. | A flight test is not certification, operational fielding, accepted inventory, combat performance, or adversary response. |
| Allied demand | [Polish JASSM-ER procurement record](../../records/us-jassm-er-poland-external-procurement-response-2024-2030.json) reports a May 28, 2024 agreement worth about $735M with deliveries scheduled for 2026–2030 and a stated aim to increase inventory. | Allied procurement converts strategic concern into a contracted demand signal. | Quantity, delivery, acceptance, training, inventory, industrial participation, and operational availability are not stated. |
| Delivery non-observation | [Polish delivery recheck](../../records/us-poland-jassm-er-delivery-nonobservation-2026.json) found no delivery, acceptance, or fielding/training notice in the reviewed official source set; another official briefing used a different 2028–2030 schedule. | The missing delivery endpoint and schedule conflict are themselves auditable findings. | Absence from the reviewed pages does not prove no delivery; variant, lot, or planning-stage differences may explain the conflict. |
| Procurement control | [Polish NIK audit](../../records/us-poland-jassm-er-audit-control-2022.json) reviewed nine settlement forms totaling PLN 210,543.7 thousand and found no numeric value tied to the JASSM-ER settlement line; a separate 32-unit comparator is explicitly not assigned to JASSM-ER. | Auditability and accounting evidence can be a separate bottleneck from production. | The audit passage does not identify JASSM-ER delivered quantity or absence of delivery. |

## Finding

The current evidence supports a **network-to-capability gap**. The JASSM/LRASM
case has a broad reported supplier surface, substantial financial concentration,
distributed corporate registrations, a stated production rate, new-facility
investment, integration tests, and allied procurement demand.

None of those stages alone establishes replaceable, delivered capability. The
most important open links are: which legal entity and facility performed which
component work; whether the 396-per-year rate became accepted inventory; whether
integration tests became certification and fielding; whether Poland received and
trained on the ordered missiles; and whether another supplier, facility, or
allied route could substitute after disruption.

The case is therefore neither “resilient” nor “fragile” on the current evidence.
It is a measurable production-and-governance chain with a missing operational
endpoint. Supplier-name breadth should not be mistaken for competition or
replaceability, and a scheduled allied order should not be mistaken for fielded
deterrence.

## Counterexamples and disconfirmation checks

- Financial concentration can coexist with resilience if the largest suppliers
  have validated surge capacity, interchangeable tooling, inventory, or multiple
  qualified facilities.
- A three-facility corporate footprint may provide geographic redundancy, but it
  may also be registration structure with no substitutable production.
- A higher minimum sustained rate can increase replenishment capacity even if
  accepted output lags temporarily; the two stages must remain separate.
- A delayed or unreported delivery may still be operationally complete; public
  non-observation is not non-delivery.
- Allied procurement can improve security and industrial scale while creating
  dependence on a single U.S. prime, export approval, or specialized input.
- Concentration may reflect efficient quality assurance and integration rather
  than harmful lack of competition; resilience requires a performance test.

The interpretation would strengthen toward resilience if a dated disruption or
surge episode showed qualified substitute production, delivery continuity,
accepted inventory, and allied fielding. It would weaken if supplier failure,
test failure, delivery delay, single-facility dependence, or export/licensing
constraints caused a measurable operational gap.

## Bounded public discussion

The [SupplyChainLogistics Reddit discussion](../../social-discussions/records/geopolitical-state-reddit-001.json)
connects geopolitical tension to nearshoring, procurement, shipping, and the
security-versus-efficiency trade-off; a counterclaim says firms may invoke
geopolitics to justify margin increases. This is useful framing for attribution
and incidence, but it provides no missile shipment, price, supplier, or facility
panel and is not representative public opinion.

## Next test

Build an identifier-bearing capability ledger:

```text
parent award and component
  -> recipient legal entity, UEI/CAGE, and facility
  -> contract/subaward action, quantity, and date
  -> production, test, acceptance, shipment, and inventory
  -> supplier failure, surge, substitute, or repair route
  -> allied delivery/training/fielding and operational availability
  -> disruption response, cost, schedule, and strategic effect
```

The first decisive acquisition is to match USAspending recipient names to UEI,
CAGE, facility, and subaward identifiers, then connect those records to Air
Force acceptance/delivery and Polish lot or training records. Preserve the
current source conflict and non-observation rather than selecting the more
favorable schedule. Add worker, community, and public-spending incidence only
after the component/facility unit is resolved.

## Stopping rule

Do not call the JASSM/LRASM network resilient, replaceable, domestically
independent, delivered, or strategically effective from supplier counts,
concentration, a production-rate exhibit, a flight test, an allied agreement,
an audit gap, or a social discussion alone. Close this bounded case only when a
named component/facility route connects production to accepted delivery,
substitution or surge, and allied/operational consequence—or when USAspending,
DoD/Air Force, Polish MOD, audit, and related public records have been checked
and the missing link is documented. Then rotate to the next U.S. industrial or
consumer chain; the broader fourteen-theme program remains active.

