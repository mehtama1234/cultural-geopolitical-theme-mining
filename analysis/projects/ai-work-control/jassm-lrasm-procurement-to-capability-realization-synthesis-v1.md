# Procurement is not capability: the JASSM/LRASM realization clock

**Checked:** 2026-09-15  
**Status:** bounded procurement-to-capability synthesis; no leverage claim

## The question

A large defense award can be described as strategic capability long before the
system is produced, accepted, delivered, integrated, maintained, or usable by
the customer. This case asks how far the public record can currently travel
from a JASSM/LRASM procurement decision to realized capability and geopolitical
leverage.

The evidence supports a staged clock:

```text
possible sale / procurement agreement
  -> award and supplier structure
  -> facility and production-capacity investment
  -> production support and integration testing
  -> accepted quantity
  -> shipment, delivery, fielding, and training
  -> inventory, maintenance, and operational use
  -> replaceability and an observed external response
```

Only the earlier and middle stages are currently visible for the selected
case. The missing later stages are not clerical details: they determine
whether an announced investment has become an option that a state can use.

## What the evidence currently establishes

| Stage | Current evidence | Safe interpretation |
|---|---|---|
| Procurement | US award and Polish JASSM-ER agreement/schedule | Demand, commitment, and planning are visible |
| Supplier structure | 74 subaward rows, 51 reported recipients, selected UEIs and reported locations | A traceable supplier/reporting network exists |
| Facility context | BAE and General Dynamics-OTS facility/capability records | Relevant industrial capability is documented at selected locations |
| Production support | DoD's $999 million JASSM/LRASM production-support IDIQ | A formal support route exists; award ceiling is not delivered output |
| Capacity investment | Lockheed reports large-lot and factory-capacity investment | Intended or built capacity is visible; actual throughput remains open |
| Integration testing | Lockheed reports completion of an LRASM F-35C flight-science phase | A technical milestone is visible; it is not fielded inventory |
| Customer realization | Polish official sources provide a 2026–2030 or 2028–2030 planning window | Delivery and acceptance of the 2024 JASSM-ER order are not publicly observed in the reviewed record |
| Geopolitical consequence | No dated external behavior change tied to realized inventory was located | Leverage remains open |

The supplier and facility rows should remain separate. A USAspending recipient
location or primary place of performance is not automatically a manufacturing
site. A component description is not a production quantity. The selected BAE
and General Dynamics-OTS UEIs make further reconciliation possible, but they
do not by themselves establish plant assignment or completion.

## The central timing lesson

The NIK FMS comparison shows why a single “delivery” or “status” field is
insufficient. In a separate F-35 case, physical deliveries occurred in
December 2024 and January 2025 while the estimated schedule placed them in
2024's third quarter, and related settlement forms arrived later. This does
not establish anything about Poland's JASSM-ER order; it does establish a
control rule for the acquisition:

```text
schedule -> shipment -> physical delivery -> acceptance -> training/fielding
         -> inventory/maintenance -> accounting settlement
```

These events can occur on different clocks. Missing accounting visibility is
not proof of missing delivery, and delivery is not proof of operational
readiness.

## What “capability” would require

For this atlas, capability is not inferred from contract value, supplier count,
factory size, or a test milestone. A defensible capability observation needs
at least a dated variant/lot, accepted or delivered quantity, customer unit or
location, integration/training status, and a maintenance or inventory signal.
The stronger sovereignty question additionally needs an alternative or
switching route: common inputs, certified substitutes, software/data
dependence, repair capacity, and the time required to replace the supplier.

This distinction matters for both US and allied interpretations. A larger
production-support route may increase future option space without yet changing
what Poland can deploy. A customer agreement may reveal threat assessment and
alliance demand without demonstrating usable inventory. A dispersed supplier
map may look resilient while sharing a parent, input, tooling, certification,
or software dependency.

## Counterexamples and non-observations

- A planned delivery window is not evidence of a delay, acceleration, or
  delivered quantity.
- An IDIQ ceiling and “no funds obligated at award” do not establish output.
- Company-reported capacity is useful industrial evidence but is not a neutral
  production-rate measurement.
- A flight-science or integration test can succeed without operational
  fielding, sustainment, or customer acceptance.
- A public-source non-observation is not evidence that no delivery occurred;
  it means the reviewed public record cannot support promotion to that stage.
- FMS accounting and physical realization can be asynchronous, so settlement
  records must not be used as a substitute for shipment or acceptance records.

## Smallest decisive next test

Retrieve one identifier-bearing, dated realization record tied to a JASSM/LRASM
variant or customer: an accepted lot quantity, shipment, delivery, fielding,
training, inventory, maintenance, or official exercise record. Then reconcile
its variant, customer unit, supplier/facility, and date against the existing
USAspending UEI and DLA CAGE records. Only after that should the atlas test
replaceability or an external actor's response.

The stopping rule is strict: if the next source only repeats procurement
intent, schedule, capacity, or testing, publish it as another realization
stage and do not promote a capability or leverage claim.

## Sources and related records

- [JASSM/LRASM realization-stage finding](findings/ai-work-control-080.md)
- [Subaward-to-UEI and reported-location finding](findings/ai-work-control-078.md)
- [Poland JASSM-ER delivery non-observation](findings/ai-work-control-081.md)
- [FMS timing-asynchrony finding](findings/ai-work-control-083.md)
- [State-leverage control ledger](state-leverage-control-ledger-v1.md)
- [Recipient-identity and facility records](data/usaspending-jassm-lrasm-rich-subaward-search-2026-09-14.json)

