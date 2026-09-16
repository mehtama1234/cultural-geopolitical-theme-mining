# Practical-exit contract dry-run: CFPB student-loan event ledger

**Status:** coverage audit only; no consumer-harm, remedy, trust, or exit rate  
**Checked:** 2026-09-16  
**Source:** 25-record capped retrieval-order student-loan complaint ledger, received in 2024  
**Contract:** [practical-exit observation contract](../../../manifests/practical-exit-observation-contract-v1.json)  
**Machine-readable audit:** [dry-run JSON](cfpb-practical-exit-contract-dry-run-v1.json)

## Result

This ledger is a good route-and-visibility record, not a same-customer exit
record. All 25 rows have an observed trigger/exposure, complaint route,
administrative response label, denominator, and counterexample field. None has
a documented same-customer post-event status. Alternatives, actual effort,
remedy receipt, durability, switching, non-use, trust, and political action
therefore remain unknown. No row is promoted to practical exit.

| Layer | Current evidence | Boundary |
|---|---|---|
| Problem and exposure | service-failure condition and student-loan complaint exposure | complaint records select visible participants |
| Route | web submission, narrative presence, and receipt-to-company-send lag | routing is not completed resolution |
| Burden | customer effort, financial loss, and time are named as unmeasured | no amount, hours, or constraint is observed |
| Response | company response category and timeliness are recorded | response label is not verified correction or payment |
| Alternatives | explicitly “not observed” in the public record | no provider/account substitute or reachable route |
| Follow-up | later outcome explicitly unknown | no same-customer recovery, repeat contact, switch, or exit |
| Meaning/action | meaning, attribution, trust, and civic response unknown | narrative presence is not a meaning measure |

## Broader-program implication

The CFPB lane now cleanly supports a societal trend about institutional
visibility: consumer problems enter a measured route, are screened into
response categories, and become more or less publicly legible depending on
product and record fields. It does not yet support the stronger claim that
customers recovered, stayed, switched, stopped using the service, or left
because of the encounter.

The smallest decisive next test is not a larger complaint download. It is a
lawful, de-identified follow-up sample that links a complaint episode to the
same account or consumer at a defined date: actual correction/payment, repeat
contact and effort, available substitute, whether the substitute was usable,
continued use or non-use, and the protected or sacrificed financial outcome.
Until then, keep complaint visibility, company response, remedy, and practical
exit as separate arrows in the atlas.

## Reproduction

```text
python3 scripts/audit_cfpb_event_ledger_practical_exit.py
```

The audit reads the existing local event ledger only and downloads no data.
