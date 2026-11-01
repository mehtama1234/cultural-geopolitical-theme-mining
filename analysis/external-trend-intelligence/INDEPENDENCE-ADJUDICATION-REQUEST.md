# Candidate independence adjudication request

This is the human handoff for the five candidate rows in
`candidate-independence-adjudication-queue.json`. Distinct hosts or URLs are
not independent confirmation by themselves. This form does not qualify a
trend, clear rights, or authorize a company bridge.

## Instructions

Assign one reviewer per candidate. For every unresolved record, identify the
canonical publisher, exact artifact, upstream dataset or event, population,
geography, period, unit, denominator, outcome, rights boundary, and dependence
relationship. Record one disposition: `independent`, `dependent`,
`non_comparable`, or `insufficient_evidence`.

Stop if any comparator lacks a canonical publisher, underlying artifact,
compatible unit, or rights evidence. A pending row remains excluded from
independent confirmation.

## Review table

| Candidate | Priority | Reviewer | Due date | Publisher/upstream review | Unit/period/outcome review | Rights review | Dependence disposition | Final disposition | Evidence link / sign-off |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `candidate-formal-response-before-recovery` | high | TBD | TBD | ☐ | ☐ | ☐ | TBD | pending | `candidate-lineage-dependency-review.json`; resolve 3 unclassified records |
| `candidate-time-financial-pressure-practical-room` | high | TBD | TBD | ☐ | ☐ | ☐ | TBD | pending | `candidate-lineage-dependency-review.json`; resolve 6 unclassified records |
| `candidate-digital-capability-control-trust` | high | TBD | TBD | ☐ | ☐ | ☐ | TBD | pending | `candidate-lineage-dependency-review.json`; resolve 5 unclassified records |
| `candidate-infrastructure-dependency-power` | high | TBD | TBD | ☐ | ☐ | ☐ | TBD | pending | `candidate-lineage-dependency-review.json`; resolve 6 unclassified records |
| `candidate-us-food-insecurity-persistence` | standard | TBD | TBD | ☐ | ☐ | ☐ | TBD | pending | `food-security-independence-review-packet.json`; sign disposition |

## Required evidence checklist

- canonical publisher and source-family identity;
- underlying dataset or event, not only a summary or citation;
- population, geography, period, unit, denominator, and outcome;
- method overlap or non-overlap with every comparator;
- rights and redistribution boundary for the exact artifact; and
- explicit reason the comparison is independent, dependent, or non-comparable.

## Acceptance and escalation

- Reviewer acknowledgement: TBD
- Second-reviewer check: TBD
- Final disposition recorded in the machine-readable queue: TBD
- Open-gate and next-review update: TBD

The queue remains open until every candidate has an explicit disposition. The
escalation path is `lineage_reviewer` → `trend_challenger` → `program_sponsor`.

The machine-readable queue now records the first review action, evidence
artifacts, and sign-off requirements for every candidate. A distinct host or
URL is never treated as independent without the artifact-level review.
