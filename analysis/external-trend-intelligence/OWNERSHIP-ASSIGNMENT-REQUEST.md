# Observatory ownership assignment request

This is the human handoff for assigning accountable owners to the six roles in
`ownership-assignment-queue.json`. It does not infer identity, authorize
company-data access, grant source rights, or close any qualification gate.

## Instructions

Complete one row for every role. Record a primary and backup, obtain both
acknowledgements, disclose conflicts, and attach the signed acknowledgement or
decision note. The queue remains `assignment_required` until the machine-readable
queue is updated and a second analyst independently reviews the handoff.

Required fields for every role:

- person or team;
- primary acknowledgement;
- backup person or team;
- scope acknowledgement;
- conflict declaration; and
- effective date.

The assignment SLA is 10 business days. Activate the backup after two missed
review cycles, an unacknowledged release hold, or a primary conflict declaration.

## Assignment table

| Role | Scope/evidence | Primary owner | Backup owner | Primary acknowledgement | Backup acknowledgement | Scope acknowledgement | Conflict declaration | Effective date | Acceptance evidence / link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `source_steward` | Source registry, rights and release boundaries; review one rights question | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | `acquired-source-register.json` + signed rights decision |
| `evidence_analyst` | Capture, normalize, compare, and preserve evidence; reproduce one snapshot | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | `refresh-history.json` + reconciled rows |
| `lineage_reviewer` | Publisher/upstream/host dependence; adjudicate one question | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | `rights-review-queue.json` + boundary note |
| `trend_challenger` | Qualification and falsification; challenge one held candidate | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | `candidate-qualification-matrix.json` + challenge note |
| `decision_translator` | Decision narratives and pilot gate discipline; frame one bounded question | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | `PILOT-VALIDATION-PROTOCOL.md` + decision note |
| `release_owner` | Refresh, release manifest, continuity, escalation; run release controls | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | `release-manifest.json` + smoke-test output |

## Handoff acceptance

- Signed role acknowledgement: TBD
- Independently reviewable run or decision note: TBD
- Open-gate and next-review update: TBD
- Second-analyst review: TBD
- Program sponsor acceptance: TBD

The escalation path is `release_owner` → `program_sponsor` →
`rights_and_privacy_owner`. Until this handoff is complete, the observatory
remains operational with open ownership gates and must not treat an unassigned
role as an implicit approval.

The machine-readable queue carries each role's full first-30-day action and
required-evidence set. A role is not accepted by filling in a name alone: the
primary and backup must acknowledge scope, disclose conflicts, and attach the
first independently reviewable evidence.
