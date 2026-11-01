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
| `source_steward` | Source registry, source controls, rights and release boundaries | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | TBD |
| `evidence_analyst` | Capture, normalize, compare, and preserve observation evidence | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | TBD |
| `lineage_reviewer` | Publisher, upstream, host dependence, and independence review | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | TBD |
| `trend_challenger` | Qualification, falsification, counter-signals, and backtests | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | TBD |
| `decision_translator` | Decision narratives and company-pilot gate discipline | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | TBD |
| `release_owner` | Refresh schedule, release manifest, continuity, and escalation | TBD | TBD | ☐ | ☐ | ☐ | TBD | TBD | TBD |

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
