# Remedy-stage coverage audit

**Checked:** 2026-09-18  
**Status:** explicit-field audit; no inferred remedy stages

The 34-ledger portfolio contains 206 event rows. Only 15 rows across 11 ledgers
explicitly use the new remedy-stage vocabulary. The remaining 197 rows are not
treated as “no remedy”; their stage is simply not recorded in the standardized
field.

| Explicit stage | Rows |
|---|---:|
| Remedy offered | 3 |
| Remedy ordered | 7 |
| Remedy implemented | 3 |
| Remedy reportedly received | 1 |
| Remedy verified received | 0 |
| Durability failed | 1 |
| Durability verified | 0 |
| Later outcome follow-up | 0 |
| Stage not explicitly recorded | 191 |

The calibrated rows include six additional Fair Work Commission employment
cases alongside Meadley, Apple PERM, VRURC, Honda Talon, and Sauna360. They show
why the distinction matters: a reported payment can coexist with
failed reinstatement; a firm-reported correction can coexist with unknown
purchaser receipt; and a repair can later be described as ineffective.

This audit does not estimate remedy success or failure. It measures only the
coverage of explicit stage fields in retained ledgers. The source records and
machine-readable counts are in the [audit JSON](../../data/us-broad-remedy-stage-coverage-audit-2026-09-18.json).

The next evidence target is not another generic response record. It is a
recipient- or user-linked follow-up with remedy receipt, protected outcome,
repeat-harm or durability status, and later continued use, switching, trust,
or exit.
