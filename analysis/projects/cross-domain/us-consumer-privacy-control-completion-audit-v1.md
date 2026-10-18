# U.S. consumer privacy control and completion audit v1

Date: 2026-10-18  
Status: active U.S. consumer rotation; named retailer administrative episode

## Research question

When a U.S. consumer uses a privacy right, does a company’s reported completion
become actual, durable control over personal data—or does the chain stop at
identity verification, category closure, or a status label?

The chain under test is:

`consumer request -> verification and routing -> access, deletion, or sale
opt-out -> data removed or use constrained -> residual exposure/re-collection ->
trust, switching, fraud protection, and practical agency`.

## Evidence ledger

| Stage | Evidence | What it supports | Boundary |
|---|---|---|---|
| Request universe | [Walmart CCPA metrics](../../records/us-walmart-ccpa-privacy-request-completion-2025-2026.json) report 22,480 request rows across access, deletion, and sale-opt-out categories for calendar 2025; categories are not a unique-person denominator. | A large U.S. retailer exposes administrative control activity at category level. | Rows are not people, and the categories should not be pooled as one consumer population. |
| Access route | Walmart reports 1,914 access requests, 1,588 completed, 326 denied, and a 42-day median completion time. | Access requests have visible receipt, disposition, and timing stages. | The data do not show whether disclosures were complete, understandable, useful, or followed by correction. |
| Deletion route | Walmart reports 3,199 deletion requests, 1,962 completed, 1,237 denied, and a 22-day median completion time. | Deletion is materially more contested than sale opt-out in this reported universe. | Denial reasons, identity failures, exemptions, residual data, re-collection, and individual outcomes are not published. |
| Sale opt-out route | Walmart reports 17,367 sale/ sharing opt-out requests, 17,276 completed, and 91 denied. | A restriction on a specified use can have a much higher reported completion rate than deletion. | Opting out of sale is not deleting data; downstream use, inference, internal access, and re-collection remain unobserved. |
| Administrative condition | Walmart states identity or authorization verification is required and valid exemptions may produce denial. | Practical privacy control depends on the request route and eligibility rules, not only the legal right. | The aggregate metrics do not show verification burden, language/access differences, repeat requests, or appeal success. |
| External mechanism | [NBER tracking and fraud paper](../../records/us-nber-privacy-tracking-fraud-2026.json) reports that Apple’s App Tracking Transparency natural experiment reduced consumer fraud complaints, with larger decreases for personal-information misuse and in places exposed to riskier data practices. | Data-flow restrictions can have downstream consumer-protection effects beyond a company’s privacy dashboard. | The working paper is observational around a policy shock; complaint reductions do not measure all fraud, reimbursement, restored accounts, or trust. |
| Governance context | [GAO AI privacy guidance record](../../records/us-gao-ai-privacy-guidance-gaps-2026.json) distinguishes federal AI use from incomplete guidance, risk identification, oversight, transparency, metrics, and agency capacity. | Consumer privacy control sits inside a wider governance-capacity problem as data-intensive systems expand. | Federal guidance gaps do not evaluate Walmart’s CCPA operations or prove a company failure. |

## Finding

The evidence supports a **completion-to-control gap**. Walmart’s reporting shows
real administrative capacity: requests are received, classified, completed or
denied, and assigned median times. It also shows that the type of control matters.
Sale opt-outs have a reported completion rate of about 99.5% in this request-row
universe, while deletion is about 61.3% completed, with different rights,
verification, and exemption conditions.

Those rates are not a measure of privacy protection by themselves. A completed
request can mean that a process reached its company-defined endpoint; it does not
show that every relevant record was removed, that an inference disappeared, that
data were not re-collected, that a consumer understood the result, or that the
consumer changed behavior. The NBER result supplies a counter-mechanism: changing
the data-resale/tracking environment can reduce fraud complaints, suggesting that
privacy controls may matter downstream, but it does not identify which individual
requests produced which protection.

## Counterexamples and disconfirmation checks

- High sale-opt-out completion can represent meaningful risk reduction even when
  deletion is denied or unavailable.
- A deletion denial can be legally valid, correctly verified, and transparently
  explained; denial is not automatically institutional failure.
- A 42-day access median may be acceptable for a complex data inventory, while
  still being unusable for a time-sensitive consumer decision.
- Data restrictions may reduce one fraud channel while shifting activity to
  another, imposing matching costs, or affecting consumers differently by device
  and platform.
- Privacy action may reflect concern and agency, but non-use or continued use can
  reflect convenience, dependence, or lack of alternatives rather than trust.

The interpretation would strengthen toward durable control if a repeated,
consumer-linked audit showed request completion, verified deletion or constrained
use, no unauthorized reappearance, understandable explanation, and lower later
fraud or unwanted targeting. It would weaken if completed requests left material
data in scope, required repeated effort, reappeared, or produced no practical
change for consumers with different verification, language, disability, or
account conditions.

## Bounded public discussion

The [LinkedIn discussion of GAO’s AI/privacy findings](../../social-discussions/records/atlas-batch-0054-ai-privacy-linkedin-001.json)
frames privacy as a governance-capacity issue involving risk identification,
oversight, transparency, metrics, and institutional accountability. This adds a
public policy interpretation to the administrative record, but it is advocacy-
oriented professional discussion, not a Walmart customer sample or independent
evaluation.

## Next test

Build a same-request or repeat-consumer control ledger:

```text
request type and purpose
  -> verification effort, access route, and wait
  -> completed/denied/partial result and explanation
  -> data fields actually delivered, removed, or restricted
  -> residual data, inference, re-collection, or repeat request
  -> fraud/targeting exposure, trust, continued use, switching, or exit
```

Seek regulator filings, company transparency detail, consumer-request samples,
appeal/complaint outcomes, and—where legally available—de-identified repeated
request or data-residency audits. Compare access, deletion, and sale opt-out
routes without treating them as interchangeable. Preserve consumers who stay,
repeat requests, or abandon the process as distinct outcomes.

## Stopping rule

Do not call a privacy right effective, ineffective, or equitable from request
counts, completion rates, median days, a legal policy, a natural experiment, or
public discussion alone. Close this named consumer episode only when an observed
request can be linked to what data/use changed and at least one later exposure,
fraud, trust, switching, or repeat-request outcome—or when company, regulator,
and available consumer records have been checked and the missing link is
documented. Then rotate to the next U.S. industrial or consumer chain; the
broader fourteen-theme program remains active.

