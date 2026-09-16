# Platform-remedy field-availability audit v1

**Status:** verified same-case field boundary; no remedy or exit rate
**Checked:** 2026-09-16
**Machine record:** [platform-remedy field availability](data/platform-remedy-field-availability-2026-09-16.json)

## Result

The local practical-exit dry-run contains 27 platform-work episodes. Every
episode has an observed attempted route and an observed decision. Ten episodes
have an observed remedy-related record, and eight have an `access_restored`
post-event label.

That does not close the lived remedy or exit chain. Across all 27 episodes, the
following fields are explicitly unknown:

| Field | Available rows | Boundary |
|---|---:|---|
| Alternatives | 0 | No documented usable alternative, affordability, replaceability, or exit route |
| Effort | 0 | No verified waiting, documents, cost, missed work, or repeat-attempt measure |
| Follow-up window | 0 | No defined observation window after the decision |
| Remedy receipt | 0 | An order or restoration is not verified as received by the affected worker |
| Remedy durability | 0 | Recurrence prevention and lasting access are not measured |
| Protected/sacrificed outcome | 0 | Lost income, work continuity, care, health, or security are not linked to the episode |
| Meaning/action | 0 | No same-unit trust, attribution, organizing, switching, non-use, or exit |

## Why this matters to the broad goal

This is the counterexample to a common institutional inference:

```text
formal route -> decision/order -> remedy -> recovery/exit
```

The local evidence supports only the first two arrows and selected parts of the
third. `access_restored` is a source-coded status, not proof of remedy receipt,
durability, free choice, or improved security. The result complements the MEPS
field audit: MEPS has a larger person/event scaffold but lacks remedy and
meaning/action; the platform ledger has route and remedy proceedings but lacks
alternatives and lived follow-up. Neither fills the other's missing fields.

## Next decisive test

For one small case family, obtain a defined post-decision window and document
the alternative actually available, effort and cost, remedy offer versus
receipt, recurrence, protected/sacrificed outcome, and reason for continued use,
switching, non-use, or exit. Keep worker-reported, adjudicated, and
administrative evidence separate.

## Reproduction

```text
python3 scripts/audit_platform_remedy_field_availability.py
```

The script reads the committed 27-episode dry-run and writes aggregate counts;
no new data are downloaded.
