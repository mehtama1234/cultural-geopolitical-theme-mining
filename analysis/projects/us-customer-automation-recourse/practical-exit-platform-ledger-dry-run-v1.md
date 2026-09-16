# Practical-exit contract dry-run: platform-remedy ledger v1

**Status:** coverage audit only; no new trend record or exit estimate  
**Checked:** 2026-09-16  
**Source:** 27 records in the local platform-remedy case ledger  
**Contract:** [practical-exit observation contract](../../../manifests/practical-exit-observation-contract-v1.json)  
**Machine-readable audit:** [dry-run JSON](practical-exit-platform-ledger-dry-run-v1.json)

## Result

The ledger can populate trigger, route, decision, and some adjudicated remedy
fields. It cannot currently establish practical exit. The dry-run assigns only
`access_restored` where the source explicitly records access resumption or a
reactivation order; all other post-event statuses are `unknown`. An order is
not receipt, restoration is not durable continued use, and a case outcome is
not worker switching or exit.

| Contract layer | Coverage in source ledger | Treatment |
|---|---|---|
| Trigger / threatened resource | decision surface and boundary usually present | mapped with evidence labels; threatened resource remains partly inferred |
| Attempted route | worker route present for all 27 records | mapped as observed; effort is unknown |
| Decision | implementation stage or boundary present for most records | mapped as observed |
| Alternatives | no reusable same-unit alternative inventory | unknown; no exit promotion |
| Money, time, access constraints | not consistently recorded | unknown |
| Remedy | adjudicated order, rule, or reported practice is often present | order/offer/observation kept separate from receipt |
| Follow-up / durability | not established in the ledger | unknown |
| Post-event status | 9 restoration/access-resumption cases in the broader synthesis, but durable use is not shown | `access_restored` only when explicit; otherwise `unknown` |
| Protected / sacrificed outcome | not coded at same-unit follow-up | unknown |
| Meaning / action | not coded | unknown |
| Counterexample | no paired alternative-constraint comparison | open |

## What this changes in the broader program

This dry-run makes the platform family usable as a boundary-tested input to the
broader American trend map without overstating it. The family currently shows
that algorithmic or platform-controlled access can produce formal review,
dismissal, reactivation orders, and lost-remuneration orders. It does **not**
show what the affected worker did next, whether another platform was reachable,
whether payment was received, whether access lasted, or whether a worker
stayed, switched, refused, stopped using the platform, or left the labor market.

The highest-value next collection is therefore a small same-unit follow-up
module for already identified cases: event date, actual access after the order,
payment receipt, recurrence, alternative work used, time and money spent, and
the protected or sacrificed household outcome. Until that exists, this family
should support institutional-remedy and recourse themes, not a practical-exit
claim.

## Reproduction

```text
python3 scripts/audit_platform_ledger_practical_exit.py
```

The audit uses only the existing local JSON ledger and writes a compact
machine-readable coverage report. It downloads no data and does not perform
person-level linkage.
