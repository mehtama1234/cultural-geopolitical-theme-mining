# Platform-remedy stage coding specification v1

**Status:** reusable coding protocol for cross-country remedy records
**Checked:** 2026-09-15

## Purpose

This specification defines the minimum structure for coding how a
platform-mediated decision becomes, or fails to become, a practical remedy. It
is designed for the Australian case census, the Malaysia Tribunal lane, the
Cambodia diagnostic, and future country inventories.

The protocol is deliberately stage-based. A formal right, a worker's use of a
channel, a review, a correction, and receipt of money are different events and
must not share one “remedy” field.

## Unit of analysis

The preferred unit is **one disputed decision affecting one worker or one
identified claimant**, not one legal instrument or one platform. If a source
only supports an institution, survey, or comparative audit, code that source as
an aggregate or institutional unit and do not infer an individual outcome.

Each record must identify:

```text
record_id
place / jurisdiction
platform and legal entity
worker or population unit
decision surface and date
source packet and access date
```

Multiple documents about the same dispute are linked under one case ID. A
single proceeding can contain multiple decision surfaces, but the ledger must
state whether it is counting a proceeding, an order, or a worker-level event.

## Required stage fields

| Field | Allowed core values | Coding rule |
|---|---|---|
| `exposure` | `observed_adjudicated`, `observed_official`, `observed_case_report`, `observed_self_report`, `observed_rule`, `not_observed` | Code how the adverse decision or system exposure is evidenced, not whether it was lawful |
| `explanation` | `observed_adjudicated`, `observed_official`, `observed_practice`, `observed_self_report`, `observed_rule`, `insufficient`, `not_observed` | “Reason exists” is not enough; record whether the affected person received usable information |
| `worker_route` | `not_observed`, `available`, `requested`, `used`, `institutional_filing`, `collective_action` | Separate a route being available from the worker actually using it |
| `human_review` | `not_observed`, `available`, `requested`, `performed`, `adjudicated_sufficient`, `adjudicated_insufficient`, `self_reported` | A human's title or contact does not prove meaningful review; record authority, inquiry, and response considered |
| `decision_change` | `not_observed`, `correction`, `restoration`, `modification`, `dismissal_upheld`, `settlement_unknown`, `open` | A refusal can be a reasoned outcome; no change is not automatically institutional failure |
| `payment` | `not_observed`, `ordered`, `agreed`, `paid_verified`, `paid_self_reported`, `quantum_open`, `not_applicable` | An order or agreement is not proof of receipt |
| `recurrence_prevention` | `not_observed`, `rule_changed`, `system_changed`, `individual_warning_only`, `collective_protection`, `open` | Require a source showing change beyond the single claimant's immediate remedy |
| `anti_retaliation` | `not_observed`, `protected_observed`, `concern_reported`, `enforced`, `open` | Do not infer safety from silence after a case |
| `outcome` | controlled case-specific label | Must state the strongest verified endpoint and may not collapse mixed stages |

The machine ledger may add more specific values, but every value must map back
to one of these core dimensions.

## Evidence classes

Use the strongest class actually supported by the source:

```text
rule                 statute, directive, policy, or formal institutional design
official_action      ministry, regulator, tribunal, or court action without a full merits finding
case_report           named proceeding reported by a credible source; details may remain incomplete
self_report           worker or respondent reports experience in a survey/interview
adjudicated           court/tribunal finding or order after evidence was considered
verified_implementation payment/access/system change independently documented
inference             interpretation across separate sources; never substitute for a stage field
open                  searched or relevant but not established
```

An evidence class describes provenance, not truth value. A self-report can be
important evidence of lived experience; it is simply not an adjudicated payment
record. An official rule can be authoritative while still lacking exercised
outcomes.

## Explanation and review test

Code explanation as meaningful only when the record answers all applicable
questions:

1. What decision or allegation was at issue?
2. What relevant facts, factors, or data were supplied to the affected person?
3. What could the person do to contest or remedy the issue?
4. Was the response deadline usable and known?
5. Could the reviewer change the decision?

If a source shows only “human review,” “investigation,” or “complaint received,”
code review as `available`, `requested`, or `performed` only as appropriate;
do not code it as sufficient. An adjudicated finding that the process was
adequate or inadequate can upgrade the field to an adjudicated value.

## Outcome ladder

The minimum comparable ladder is:

```text
L0 exposure only
L1 route or right exists
L2 route used / hearing or review reached
L3 reasoned institutional decision
L4 decision, access, rating, or status changed
L5 money or material loss restored
L6 verified implementation and durable prevention
```

The ladder is ordinal for description, not a universal score. A case can reach
L5 for lost remuneration while remaining L0 for anti-retaliation or L1 for
recurrence prevention. Never average dimensions into one effectiveness index
without a theory and compatible denominators.

## Denominator rules

Every comparison must publish:

```text
universe searched
time window
geographic scope
unit counted
inclusion and exclusion rules
duplicate handling
missing-outcome treatment
```

Use separate denominators for separate questions:

- `eligible_cases`: cases reaching the legal or institutional threshold;
- `merits_cases`: cases where the underlying decision was examined;
- `restoration_cases`: merits cases with an adjudicated or documented access
  restoration;
- `payment_order_cases`: cases with an order or agreement for money;
- `payment_verified_cases`: cases with evidence of receipt;
- `durable_change_cases`: cases with evidence of system or collective change.

Do not divide restoration by all records when many records ended at eligibility,
settlement, or missing-publication stages. Report the funnel instead.

## Missingness and negative findings

`not_observed` means the current source packet does not establish the event. It
does not mean the event did not occur. `open` means the field is a decisive
unresolved link with a defined acquisition path. A search failure should record
the source locations searched and the date searched.

Negative findings are legitimate results when supported: no public award found,
no candidate-level correction shown, no reviewer authority identified, or no
payment receipt located. They must include a boundary and must not be converted
into a claim of universal absence.

## Cross-country comparison recipe

1. Build each jurisdiction's source-specific inventory first.
2. Deduplicate by worker/proceeding, not by PDF or news item.
3. Publish the stage funnel and evidence class before interpretation.
4. Compare only shared stages, such as “route used,” “hearing reached,” or
   “adjudicated restoration.”
5. Keep worker-reported resolution separate from verified payment or correction.
6. Add a counterexample and a missing-link acquisition for every strong theme.
7. Re-run the inventory after a defined update window.

For the current program this yields:

```text
Australia  -> case-level adjudicated depth through L5 in selected matters
Malaysia   -> rule/institution plus reported hearing, mostly L1-L2
Cambodia   -> self-reported access and resolution experience, L1-L2 by evidence class
```

This is a measurement map, not a national ranking.

## Quality gates

A record is ready for publication only if:

- every stage has a value or `not_observed`;
- every observed value has a source and evidence class;
- the unit and denominator are explicit;
- settlement, order, payment, and receipt are not merged;
- a platform claim is not treated as an independent adjudicated finding;
- an inference is labeled as an inference;
- local links and machine-readable fields validate;
- the next decisive acquisition is named for every material open link.

## Current application

The [platform-work remedy ledger](platform-remedy-case-ledger-v1.md) is the
current machine-linked application. The [Australian case census](australian-platform-deactivation-case-census-v1.md)
applies the denominator rules, while the [Australia–Malaysia–Cambodia comparison](australia-malaysia-cambodia-stage-compatible-comparison-v1.md)
applies the stage-comparison rules.

## Boundary

This protocol does not establish that any particular legal regime is effective.
It establishes a reproducible way to say exactly which part of an effectiveness
claim is supported, which part is missing, and what evidence would close the
gap.
