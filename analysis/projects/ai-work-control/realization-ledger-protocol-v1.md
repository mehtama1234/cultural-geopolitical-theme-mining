# Strategic capability realization ledger protocol v1

**Status:** reusable acquisition and promotion protocol  
**Checked:** 2026-09-15  
**Primary case:** Poland JASSM-ER customer-realization watchpoint

## Purpose

This protocol keeps a strategic capability's realization clocks separate. A
budget line, an agreement, a production milestone, a shipment, an acceptance
event, an operational inventory change, and an external response are different
observations. They may refer to the same program, but they cannot be merged
into one “capability exists” field without losing the mechanism the atlas is
trying to measure.

The protocol is reusable for weapon systems, strategic infrastructure,
industrial partnerships, and other dependency cases. It is an event ledger,
not a readiness score or geopolitical-leverage index.

## Event contract

Each row should contain, at minimum:

| Field | Required meaning |
|---|---|
| `case_id` | Stable program/order/project identifier; do not use a headline as the key |
| `object` | Specific item, lot, facility, software, service, or capability being discussed |
| `event_type` | One controlled stage from the table below |
| `event_date` and `date_precision` | Date of the event, with day/month/year precision preserved |
| `actor` and `recipient` | Entity that acted and entity that received, accepted, operated, or responded |
| `place` | Facility, unit, base, country, or jurisdiction named by the source |
| `quantity` and `quantity_unit` | Quantity only when the source states it; never derive it from contract value alone |
| `source_class` | Official record, audit, contract, company report, visual evidence, journalism, or other defined class |
| `source_locator` | Stable URL or local source file plus page, section, table, or paragraph |
| `status` | Observed, planned, estimated, inferred, or not observed |
| `boundary` | What this row does not establish |

### Controlled event types

| Event type | What it can establish | What it cannot establish by itself |
|---|---|---|
| `objective` | Stated threat, mission, or policy purpose | That the objective is achieved |
| `authorization` | Approval or notification for a possible transfer | Signed order, delivery, or use |
| `agreement` | Signed procurement, partnership, or financing commitment | Production, acceptance, or operational availability |
| `budget` / `funding` | Allocated or obligated financial resources | Output, readiness, or local benefit |
| `award` / `modification` | Contract action, recipient, amount, or changed obligation | Completed work or delivered quantity |
| `production_support` | Support, sustainment, tooling, or capacity commitment | Accepted output |
| `capacity` | Named plant, workforce, line, power, or service capability | Case-specific output or customer control |
| `test` / `integration` | A dated test or integration milestone | Fielded readiness or combat availability |
| `audit_control` | An audit finding about documentary, accounting, or implementation control | Production, delivery, or non-delivery of the capability |
| `shipment` / `delivery` | Physical movement or receipt, if the source says so | Formal acceptance, training, or operational use |
| `acceptance` | Customer or authority accepted a specified object or lot | Sustained readiness or external leverage |
| `training` / `fielding` | Personnel or unit preparation and placement | Full inventory, maintenance, or mission performance |
| `maintenance` / `inventory` | Support or recorded stock status | Effective operational availability unless stated |
| `operational_use` | Observed use or exercise by a named operator | General strategic leverage or deterrence |
| `external_response` | Another actor changed a decision, term, posture, or behavior after the capability event | A causal effect unless timing and alternative explanations are documented |
| `non_observation` | A bounded search that did not locate a specified event | Proof that the event did not occur |
| `comparator` | A separately identified case that tests timing, control, or realization interpretation | Evidence about the primary case |

## Promotion rules

1. Preserve the source before extracting the event. Record retrieval date,
   revision, language or translation status, and the exact locator.
2. Treat a planned date as `planned`, a model or estimate as `estimated`, and
   an announcement of intent as `observed agreement`—never as delivery.
3. Do not infer quantity from contract value, capacity from a facility name,
   or operational availability from delivery.
4. Keep accounting settlement separate from physical shipment. A later form
   can document an earlier event; its arrival date is not the delivery date.
5. A recipient or parent-company identifier is not a facility assignment
   unless the source explicitly joins the work package to that site.
6. Promote `external_response` only when the responding actor, response date,
   changed behavior, and plausible link to the preceding event are all named.
7. Record non-observation as a bounded search result: define sources,
   jurisdictions, date window, and event terms searched. It is not proof that
   the event did not occur.

## Required case joins

For a case to move from realization to a capability claim, the ledger should
contain separate evidence for:

```text
program objective
  -> authorization/agreement
  -> award and responsible entities
  -> production or service capacity
  -> shipment/delivery
  -> acceptance
  -> training/integration
  -> inventory/maintenance/operational availability
  -> external response or substitution
```

The strongest missing join is usually not another announcement. It is the
first identifier-bearing record that links the ordered object or lot to a
recipient unit, facility, acceptance authority, or operational inventory.

## Counterexample requirement

Every promoted leverage interpretation needs at least one comparison case:

- similar procurement without observed operational response;
- similar capacity with a successful supplier switch;
- local production with external control of design, software, certification,
  finance, or critical inputs; or
- physical delivery whose settlement or public announcement occurred on a
  different clock.

The counterexample is not a demand for a perfect control group. It prevents a
single visible milestone from carrying more causal meaning than the evidence
supports.

## Current application: Poland JASSM-ER

The current case has observed authorization, agreement, planned delivery
windows, US production-support and integration activity, and comparative FMS
timing evidence. It does **not** yet have a publicly verified 2024-order
shipment, accepted quantity, Polish unit receipt, training event, inventory
change, operational-use record, or external response. The [Poland delivery
watchpoint](findings/ai-work-control-081.md), [NIK control finding](findings/ai-work-control-082.md),
and [FMS timing comparison](findings/ai-work-control-083.md) remain separate
ledger inputs.

The applied machine-readable ledger is the [Poland JASSM-ER realization
ledger](data/poland-jassm-er-realization-ledger-v1.json). It keeps the F-35
timing row marked as a comparator and records the reviewed non-observation
separately from the observed agreement and planned window.

The same contract is also applied to the [US data-center capacity, revenue,
governance, and operational-stress ledger](data/us-data-center-realization-ledger-v1.json).
That second case keeps national modeled demand, county aggregate capacity,
utility policy response, and reported load-drop events as separate stages.

Validate it with:

```text
python3 scripts/validate_realization_ledger.py \
  analysis/projects/ai-work-control/data/poland-jassm-er-realization-ledger-v1.json
```

The next decisive acquisition must therefore identify event type before
content: a delivery notice is not an acceptance record, an acceptance record
is not an operational-use record, and none of these alone is geopolitical
leverage.

## Related methods

- [State-capacity and geopolitical-leverage synthesis](state-capacity-geopolitical-program-v1.md)
- [Defense resource-to-capability finding](findings/ai-work-control-048.md)
- [Realization-stage milestone finding](findings/ai-work-control-080.md)
- [Public event-ledger schema](../../../manifests/us-broad-event-ledger-schema-v1.json)
