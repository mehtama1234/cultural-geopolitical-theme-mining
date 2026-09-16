# Platform-work remedy case ledger v1

**Status:** initial cross-source ledger; designed for case-level expansion

**Checked:** 2026-09-15

## Purpose

This ledger prevents unlike evidence from being collapsed into a single
“remedy” indicator. Each row identifies the decision surface, the worker's
route, the institutional response, and the strongest outcome actually shown.

`observed_rule` means a legal or formal rule exists. `observed_self_report`
means workers reported an experience or outcome. `observed_adjudicated` means a
court or tribunal made a finding or order. `not_observed` means the current
source packet does not establish the event; it does not mean the event never
occurred.

## Ledger

| ID | Place / unit | Source type | Decision surface | Worker request or route | Explanation | Human review | Correction / restoration | Payment / compensation | Anti-retaliation | Evidence strength | Current boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PR-001 | London Uber drivers; Uber/Ola proceedings in Amsterdam Court of Appeal | Court record | Account deactivation, trip allocation, fares, fraud-probability and other scores | GDPR information request and court application | `observed_adjudicated` | `not_observed` after the appellate information order | `not_observed` | `not_observed` | `not_observed` | High for the court order; medium for downstream worker outcome | Information was ordered; no public follow-on correction or reinstatement record located |
| PR-002 | Uganda taxi and delivery platform workers | ILO–Makerere cross-sectional survey | Ratings, allocation, refusal penalties, GPS/call monitoring, deactivation | Platform appeal or complaint | `not_observed` as a formal model explanation | `observed_self_report` as favorable appeal resolution, review content unspecified | `not_observed` | `not_observed` as a specific payment/compensation event | `not_observed` | Medium for reported experience; low for independently verified remedy content | About 75% of affected workers reported appealing; more than 90% of appellants reported favorable resolution, but the action is not itemized |
| PR-003 | Malaysia gig workers under Act 872 | Enacted statute and implementation materials | Automated monitoring/decision systems, service assignment, working conditions, deactivation | Non-automated review, hearing, internal grievance, conciliation, Tribunal | `observed_rule` | `observed_rule` | `not_observed` in a worker case | `observed_rule` for conditional interim payment; actual payment `not_observed` | `not_observed` | High for statutory architecture; low for exercised outcome | Act is in force and complaint infrastructure is visible; no public automated-decision case outcome located |
| PR-004 | EU platform workers under Directive 2024/2831 | EU directive and national preparation records | Algorithmic management and high-impact decisions | Explanation, human oversight, review, correction/compensation, dispute route | `observed_rule` | `observed_rule` | `observed_rule` | `observed_rule` | `observed_rule` | High for EU rule; low for national exercise in current packet | Transposition deadline is 2 December 2026; national implementation and use remain staged |
| PR-005 | Dutch Deliveroo couriers | Civil court record | Algorithmic allocation and platform control considered in employment-status analysis | Collective status litigation | `not_observed` as a decision-specific explanation | `not_observed` | `not_observed` | `not_observed` | `not_observed` | High for status outcome; low for algorithmic-remedy outcome | Employment relationship recognized; no Directive-style automated-decision remedy shown |
| PR-006 | Finnish Wolt couriers | Administrative court and tax-administration record | Platform data used to direct, supervise, monitor, and control work | Status and tax treatment challenge | `not_observed` as a decision-specific explanation | `not_observed` | `not_observed` | `observed` as wage-treatment consequence, not compensation for an automated decision | `not_observed` | High for status/tax consequence; low for automated-remedy outcome | Employment relationship and wage treatment recognized; working-time and automated-remedy dimensions remain separate |
| PR-007 | Kenya Ziada platform workers | ILO institutional case study | Client ratings and service-quality assessments in domestic, beauty, and personal services | Staff mediation and discussion after a low rating | `observed_practice` | `observed_practice` | `not_observed` | `not_observed` | `not_observed` | Medium; official case study, not a case file | Human mediation is reported; score correction, restoration, payment, and consistency remain open |

## Cross-row findings

### The strongest verified remedy is still procedural

PR-001 establishes an adjudicated information remedy. PR-003 establishes a
statutory review and explanation architecture. Neither establishes that a
worker's access, rating, or pay was corrected. PR-002 supplies the first
worker-level positive-resolution signal, but its survey design does not identify
what changed.

### Formal remedy and practical remedy are separate variables

The ledger deliberately keeps these columns separate:

```text
right or route exists
  != request made
  != review occurred
  != decision corrected
  != loss repaid
  != recurrence prevented
```

This is the central measurement discipline for the broader cultural and
geopolitical comparison.

### Status recognition is not automated-decision correction

PR-005 and PR-006 show that a court or administration can recognize platform
control and produce employment or tax consequences without examining whether a
specific automated decision was explained, reviewed, corrected, or reversed.
Those cases belong in the atlas, but they must not be coded as algorithmic
remedy outcomes.

## Next acquisition fields

For each new case, add:

1. platform and legal entity;
2. worker or representative and jurisdiction;
3. exact decision, date, and stated reason;
4. automated function alleged or documented;
5. request channel and response deadline;
6. explanation content and whether relevant factors were supplied;
7. reviewer identity, authority, and independence;
8. correction, account restoration, rating change, or payment result;
9. compensation, recurrence prevention, and retaliation evidence;
10. source type, access date, identifier, and verification strength.

## Linked records

- [Global platform-work remedy comparison](global-platform-remedy-comparison-v1.md)
- [Uber/Ola automated-decision remedy case](uber-ola-automated-decision-remedy-case-record-v1.md)
- [Uganda platform-work algorithmic remedy record](uganda-platform-work-algorithmic-remedy-record-v1.md)
- [Malaysia Gig Workers Act algorithmic-remedy record](malaysia-gig-workers-act-algorithmic-remedy-record-v1.md)
- [Platform-work court comparator](platform-work-court-comparator-v1.md)
- [Kenya Ziada human-review platform record](kenya-ziada-human-review-record-v1.md)

## Boundary

This is a research ledger, not a legal database or estimate of the prevalence
of effective remedies. The rows have different units and evidence designs and
must not be pooled without a compatible denominator, time window, and outcome
definition.
