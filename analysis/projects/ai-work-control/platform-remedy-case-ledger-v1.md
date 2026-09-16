# Platform-work remedy case ledger v1

**Status:** initial cross-source ledger; designed for case-level expansion

**Checked:** 2026-09-15

## Purpose

This ledger prevents unlike evidence from being collapsed into a single
“remedy” indicator. Each row identifies the decision surface, the worker's
route, the institutional response, and the strongest outcome actually shown.

The same rows are preserved in the machine-readable [platform-remedy case
ledger JSON](data/platform-remedy-case-ledger-v1.json), which is the expansion
surface for future cases and keeps the stage vocabulary stable.

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
| PR-008 | UK jobseekers in automated recruitment | ICO regulator review and guidance | CV scoring, ranking, filtering, and possible pre-human rejection | Notice, contest, and request for meaningful human review | `observed_rule_or_expectation` | `observed_rule_or_expectation` | `not_observed` | `not_observed` | `not_observed` | High for regulator action; low for individual remedy | More than 30 employers reviewed; 16 organizations committed to recommendations; no candidate-level correction shown |
| PR-009 | Kuching, Malaysia; e-hailing worker and GrabCar Sdn Bhd | Media reports attributing facts to KESUMA / Gig Workers Tribunal | Saver trips, cashback incentives, and advance booking | Tribunal hearing; matter reportedly returned for evidence and witness examination | `observed_case_report` | `observed_case_report` | `not_observed` | `not_observed` | `not_observed` | Medium for existence and subject of first hearing; low for outcome | A first hearing is reported; no award, correction, payment, or final finding located |
| PR-010 | Philippines platform economy | Oxford/De La Salle Fairwork comparative audit | Platform management, contracts, conditions, and worker representation | Formal appeal process evidenced at 2 of 9 assessed platforms | `observed_comparative_audit` | `not_observed` as exercised review | `not_observed` | `not_observed` | `not_observed_as_platform_evidence` | High for published assessment; low for individual remedy | Assessment found formal appeal evidence at GrabCar and GrabFood/Express; no appeal outcome or collective representation evidenced |
| PR-011 | Philippines platform economy | Official DOLE dialogue, complaint-capacity, and inspection releases | Platform labor standards, algorithmic-management policy, data privacy, safety, and complaint access | Government–platform dialogue, requested position papers, 24/7 complaint unit directive, and bounded safety inspection action | `not_observed` as automated-decision review | `not_observed` | `not_observed` | `observed_official_action` only in separate safety episode; not an ADM remedy | High for official actions; low for algorithmic-remedy outcome | Algorithmic-management and remedy issues entered the official agenda; no binding rule or corrected automated decision shown |
| PR-012 | Cambodia platform economy | Official ILO mixed-method diagnostic | Ratings, allocation, refusal penalties, temporary suspension, complaints, classification, social security, and injury | Platform complaint channel; state dispute authority named in Notification No. 1107 | `observed_self_report` for platform complaint access; specific explanation `not_observed` | `not_observed` | `not_observed` | `not_observed` | Medium for survey findings; high for publication and reported notification; low for individual outcome | Most complainants reported seldom-resolved issues; no verified correction, restoration, payment, or state case outcome located |
| PR-013 | Melbourne, Australia; Amazon Flex and Gopal Bandameeda | Fair Work Commission primary decision and lost-remuneration order (UDE2025/62) | Customer complaint, platform suspension, permanent deactivation, and conflicting delivery rules | Worker response; request for human discussion; statutory unfair-deactivation application | `observed_adjudicated` including finding that platform process lacked meaningful consideration and further inquiry | `observed_adjudicated` as external review; platform human review found absent | `observed_adjudicated` — reactivation on prior terms ordered | `observed_adjudicated` — $12,126.31 lost remuneration ordered; restoration, not compensation | `not_observed` | High for decision and order; low for payment receipt, durability, and generalization | One complete individual remedy chain is visible; recurrence prevention, receipt, and anti-retaliation remain open |
| PR-014 | Australia; Uber App, Mian Abu Bakar, and Rasier Pacific | Fair Work Commission eligibility decision and revocation decision | Uber/Uber Eats deactivation; six-month protection threshold; platform-operator identity | Unfair-deactivation application; threshold adjudication; settlement and discontinuance | `observed_adjudicated_then_revoked` at eligibility stage | `not_observed` on merits | `not_observed` | `not_observed` — settlement terms unavailable | `not_observed` | High for revocation and corporate-identity concern; low for settlement outcome | Eligibility finding was revoked by consent; no public merits decision or remedy; operator identity and enforceability remained open |
| PR-015 | Brisbane, Australia; Uber Eats and Rahul Kumar | Fair Work Commission primary merits decision | Customer-satisfaction rating threshold and continued app access | Written response; platform review; unfair-deactivation application | `observed_adjudicated` — written warnings and reasoned notice found compliant | `observed_adjudicated` — human Community Operations review found performed and sufficient | `not_observed` | `not_observed` | `not_observed` | High for decision and process findings; low for rating-system generalization and downstream effects | Protected worker's application dismissed because the Commission found the rating rule and Code process compliant |
| PR-016 | Perth, Australia; Sajid Saleem Warraich and Uber | Fair Work Commission primary merits decision | Five rider complaints, suspension, and complaint-based deactivation | Worker responses, requested discussion, statutory unfair-deactivation application | `observed_adjudicated` — warning and complaint particulars found insufficient | `observed_adjudicated` — nominal internal review did not establish meaningful inquiry | `observed_adjudicated` — reactivation ordered | `open` — parties directed to confer; amount and payment not observed | `not_observed` | High for decision and reactivation; low for later pay and implementation | Commission found Code non-compliance, no valid reason, and unfair deactivation; lost remuneration was left for later determination |
| PR-017 | Sydney, Australia; Zeeshan Aslam Khan and Uber Eats | Fair Work Commission primary merits decision (UDE2025/185) | Repeated sexual-misconduct complaints, temporary holds, warnings, and final deactivation | Written response, support calls, statutory unfair-deactivation application | `observed_adjudicated` — warning particulars and substantive explanation found insufficient | `observed_adjudicated` — platform contacts occurred but did not establish adequate inquiry | `observed_adjudicated` — reactivation ordered | `open` — parties directed to confer on quantum | `not_observed` | High for decision and reactivation; low for later pay and implementation | Commission found the 2025 allegation unproven, the process Code-inconsistent, and deactivation unfair; payment amount and receipt remain open |

## Cross-row findings

### The strongest verified remedy is still procedural

PR-001 establishes an adjudicated information remedy. PR-003 establishes a
statutory review and explanation architecture. Neither establishes that a
worker's access, rating, or pay was corrected. PR-002 supplies the first
worker-level positive-resolution signal, but its survey design does not identify
what changed.

PR-009 now adds the first exercised Malaysian Tribunal proceeding to the map.
It closes the “institution created -> case reached a hearing” link, but not the
“hearing -> award or worker outcome” link. It is intentionally coded as a
reported proceeding rather than an adjudicated remedy because the available
report describes an evidentiary hearing still in progress.

PR-012 adds an official Cambodia diagnostic with a worker-level resolution
signal: complaint access is widely reported, but approximately two-thirds of
workers who complained said their issue was seldom resolved. This is stronger
than a generic statement that recourse is weak, but it remains survey evidence,
not a verified correction or adjudicated refusal. The report also links the
remedy gap to independent-contractor classification, social-security coverage,
and occupational risk.

PR-013 supplies the first complete individual remedy chain in the current
packet. The Fair Work Commission found that Amazon's deactivation process did
not provide a real representative discussion, did not establish that a human
representative considered the worker's response, and did not make necessary
further inquiries. It ordered reactivation on the prior terms and a separate
$12,126.31 order restoring lost remuneration. The amount is not coded as
compensation, and payment receipt, continued access, recurrence prevention,
and retaliation remain unverified.

PR-014 supplies the contrasting procedural boundary. The Commission initially
found that an Uber/Uber Eats worker met the six-month protection threshold, but
later revoked that decision by consent after settlement and discontinuance.
The public record raises whether the named respondent or Uber Technologies
was the platform operator and leaves settlement terms, payment, reinstatement,
and merits fairness unobserved. This is not coded as either a worker win or a
worker loss on the underlying deactivation.

PR-015 supplies a merits-level negative outcome. The Commission found Uber's
written warnings and preliminary notice sufficient, identified a human
Community Operations review of the worker's response, accepted the 85 percent
rating threshold as reasonable, and dismissed the unfair-deactivation claim.
The record shows that review can produce a reasoned refusal; it does not prove
that individual ratings were accurate in every case or that no later appeal or
correction occurred.

PR-016 adds a second merits-level Australian contrast. In Warraich, the
Commission found that a generic complaint notice, limited particulars, and an
inadequately evidenced internal review did not satisfy the Code or procedural
fairness. Reactivation was ordered, but the lost-pay amount was deferred.

PR-017 adds a 2026 Uber Eats case with an escalation pattern: an earlier
temporary hold and warning was followed by a second complaint, another hold,
and final deactivation. The Commission found the warning and explanation
insufficient, distinguished partly corroborated earlier conduct from the
conduct supplying a valid current reason, ordered reactivation, and directed
the parties to calculate lost pay.

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
- [UK ICO automated-recruitment remedy record](uk-ico-automated-recruitment-remedy-record-v1.md)
- [Malaysia Act 872 algorithmic-remedy record](malaysia-gig-workers-act-algorithmic-remedy-record-v1.md)
- [Malaysia GrabCar first-hearing case record](malaysia-grabcar-tribunal-first-hearing-case-record-v1.md)
- [Philippines Fairwork platform-management record](philippines-fairwork-platform-management-record-v1.md)
- [Philippines DOLE platform-governance record](philippines-dole-platform-governance-record-v1.md)
- [Cambodia platform-work diagnostic record](cambodia-platform-work-diagnostic-record-v1.md)
- [Amazon Flex / Bandameeda deactivation remedy record](amazon-bandameeda-deactivation-remedy-record-v1.md)
- [Uber / Bakar deactivation-jurisdiction record](uber-bakar-revoked-deactivation-record-v1.md)
- [Uber Eats / Kumar merits-dismissal record](uber-kumar-merits-dismissal-record-v1.md)
- [Uber / Warraich unfair-deactivation record](uber-warraich-unfair-deactivation-record-v1.md)
- [Uber Eats / Khan reactivation and lost-pay record](uber-khan-reactivation-lost-pay-record-v1.md)

## Boundary

This is a research ledger, not a legal database or estimate of the prevalence
of effective remedies. The rows have different units and evidence designs and
must not be pooled without a compatible denominator, time window, and outcome
definition.

The [platform-remedy stage coding specification](platform-remedy-stage-coding-spec-v1.md)
defines the shared fields and denominator discipline used for future expansion.
