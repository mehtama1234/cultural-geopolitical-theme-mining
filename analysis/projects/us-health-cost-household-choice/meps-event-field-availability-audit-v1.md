# MEPS event-field availability audit v1

**Status:** verified staged-field boundary; no new estimate
**Checked:** 2026-09-16
**Machine record:** [MEPS event-field availability](data/meps-event-field-availability-2024.json)

## Result

The privacy-minimized MEPS 2024 staged ledger contains 18,457 rows. Every row
has a hashed episode identifier and a month-precision event date. The staged
record also retains payment and round-level health, employment, bill, debt,
collector, denial, and care-delay context.

The open middle is not merely “not yet analyzed.” The staged rows explicitly
stop at the following fields:

| Required episode stage | Availability in staged rows | Interpretation |
|---|---|---|
| Event identity/date | Present for all rows | First event-family record with month precision; day and initiating need are not identified |
| Payment/context | Present as round-level context | Payment is not an event-specific affordability or household trade-off measure |
| Alternatives | Missing | No usable provider, coverage, travel, time, or payment alternative is recorded |
| Event-specific choice | Missing | Round care-delay fields do not identify what this event caused or displaced |
| Institutional response | Partial | Denial/prior-authorization context is present, but response, appeal, authority, and effort are not |
| Remedy | Missing/unknown | No verified correction, payment arrangement, coverage restoration, or non-remedy |
| Follow-up | Partial context | Later round fields are not event-specific recovery outcomes |
| Meaning/action/exit | Missing | No attribution, trust, civic action, switching, non-use, or exit |

## Broad-program meaning

MEPS is still the strongest local primary route because it supplies a large
same-person event scaffold across health, payment, work, and later context. But
the field audit prevents that scaffold from being promoted into a medical-bill
to-household-recovery story. The correct next move is targeted acquisition or
linkage for need, alternatives, response, remedy, and meaning/action—not a
larger cross-tab of the existing event rows.

The result also clarifies the role of the other broad lanes. SHED can supply
reported care-forgoing and adaptation; CFPB/platform records can supply route
and remedy examples; HTOPS can supply selected material-to-confidence timing.
None can be silently merged with MEPS to fill the missing fields for the same
person.

## Next decisive test

Seek a privacy-approved same-unit source that records the initiating need or
bill, usable alternatives, care/payment choice, provider or insurer response,
verified remedy, and later household/work/health recovery. If such fields are
not obtainable, keep the MEPS result as an event-scaffold boundary and rotate
to the next broad theme.

## Reproduction

```text
python3 scripts/audit_meps_event_field_availability.py \
  --input /tmp/cgtm-meps-2024/household-constraint-cascade-staged-ledger.jsonl \
  --output analysis/projects/us-health-cost-household-choice/data/meps-event-field-availability-2024.json
```

The script streams the existing local 54 MB JSONL and writes only aggregate
availability counts; no raw event rows are copied into Git.
