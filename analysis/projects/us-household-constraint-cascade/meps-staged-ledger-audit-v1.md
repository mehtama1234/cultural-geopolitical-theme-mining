# MEPS staged household-cascade ledger audit v1

**Checked:** 2026-09-16  
**Status:** local staging only; not a promoted finding  
**Source location:** existing local MEPS 2024 files under `/tmp`; no new acquisition

## What was staged

The [staging adapter](../../../scripts/stage_meps_constraint_cascade_ledger.py)
reads the existing HC-256 person file and HC-254 office, emergency-room, and
inpatient files. It keeps one first valid event per positive-weight person and
event family, joins round context exactly by `DUPERSID + PANEL`, replaces the
person key with a keyed hash, and writes JSONL outside Git.

The staged row is deliberately broader than the evidence currently supports:
observed event month, event family, self/family payment, coverage/poverty
context, employment, perceived health, bill-problem, care-delay, medical-debt,
collector-contact, and denial/prior-authorization context are retained;
event-specific care choice, alternatives, household trade-off, institutional
response, verified remedy, trust, action, and recovery remain explicit unknowns
or contextual fields.

## Local run result

The run used the existing local files and produced 18,457 privacy-minimized
rows:

| Event family | First valid positive-weight people |
|---|---:|
| Office | 14,198 |
| Emergency room | 2,868 |
| Inpatient | 1,391 |
| **Total** | **18,457** |

The output was written to `/tmp/cgtm-meps-2024/household-constraint-cascade-staged-ledger.jsonl`
and passed the ledger validator in events-only mode. The exact local output
hash was `9f19ddcb2234890ecfa6cf7ebba5960225fccaa397c09fc44e4c53217527fa88`.
The keyed salt is intentionally not committed or recorded, so a rerun with a
different ephemeral salt will have a different row hash.

## Reproduction

```bash
python3 scripts/stage_meps_constraint_cascade_ledger.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  --office-file /tmp/cgtm-meps-2024/events/h254g.dta \
  --emergency-room-file /tmp/cgtm-meps-2024/events/h254e.dta \
  --inpatient-file /tmp/cgtm-meps-2024/events/h254d.dta \
  --output-jsonl /tmp/cgtm-meps-2024/household-constraint-cascade-staged-ledger.jsonl \
  --audit-output /tmp/cgtm-meps-2024/household-constraint-cascade-staged-ledger-audit.json \
  --salt '<ephemeral-local-salt>'

python3 scripts/validate_household_constraint_cascade_ledger.py \
  /tmp/cgtm-meps-2024/household-constraint-cascade-staged-ledger.jsonl \
  --events-only
```

## What this changes

This is the first real local population of the new contract. It proves that a
large existing event/person frame can be transformed into the project’s
privacy and stage vocabulary without storing direct identifiers in the
repository. It does **not** close the end-to-end goal: the event is not
necessarily the initiating need or bill, the payment is not the household
obligation, and the round fields are not event-specific follow-up. The next
real acquisition must add dated care choice/alternative, obligation, route,
verified remedy, and later household recovery/action while preserving the same
case or person key under approved linkage rules.
