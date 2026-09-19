# Remedy-stage coverage audit

**Checked:** 2026-09-18  
**Status:** explicit-field audit; no inferred remedy stages

The 34-ledger portfolio contains 206 event rows. Only 32 rows across 19 ledgers
explicitly use the new remedy-stage vocabulary. The remaining 197 rows are not
treated as “no remedy”; their stage is simply not recorded in the standardized
field.

| Explicit stage | Rows |
|---|---:|
| Remedy offered | 4 |
| Remedy ordered | 9 |
| Remedy implemented | 9 |
| Remedy reportedly received | 9 |
| Remedy verified received | 0 |
| Durability failed | 1 |
| Durability verified | 0 |
| Later outcome follow-up | 0 |
| Stage not explicitly recorded | 174 |

The calibrated rows now also include named CFPB redress and Ombudsman reissue
routes, alongside IER intervention cases, platform reactivation and refund
cases, and six additional Fair Work Commission employment cases. They show why
the distinction matters: a reported payment can coexist with
failed reinstatement; a firm-reported correction can coexist with unknown
purchaser receipt; and a repair can later be described as ineffective.

This audit does not estimate remedy success or failure. It measures only the
coverage of explicit stage fields in retained ledgers. The source records and
machine-readable counts are in the [audit JSON](../../data/us-broad-remedy-stage-coverage-audit-2026-09-18.json).

The next evidence target is not another generic response record. It is a
recipient- or user-linked follow-up with remedy receipt, protected outcome,
repeat-harm or durability status, and later continued use, switching, trust,
or exit.
