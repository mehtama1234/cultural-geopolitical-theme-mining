# Data portability, practical choice, and remedy

**Status:** eleventh active depth artifact in the ongoing program  
**Checked:** 2026-10-18  
**Scope:** Australian Consumer Data Right, data quality, switching, small-business dependence, error correction, and public trust in digital infrastructure

## The question

When a consumer gets a formal right to move data, does that become a real
ability to compare, switch, save money, avoid harm, and obtain correction?

The relevant chain is:

```text
legal right and consent
  -> data access and transfer
  -> accurate, current, comparable data
  -> product choice or switching
  -> price, service, safety, or productivity result
  -> error detection and remedy
  -> repeat use, trust, or exit
```

The current evidence reaches active use and data-quality governance. It does
not yet prove consumer-level savings, switching, fraud reduction, or durable
choice.

## Evidence packet

The [ACCC 2026 Consumer Data Right record](../../records/comparative-australia-accc-consumer-data-right-data-quality-2026-switching-usability.json)
reports:

- 1.3 million Australians using the CDR as of July 2026;
- a 16-respondent stakeholder survey, with follow-up meetings involving seven
  respondents;
- average overall consumer-data quality of 3.5/5 and product-data quality of
  3.2/5;
- average issue-resolution ratings of 3.1/5 for consumer data and 3.5/5 for
  product data;
- failure modes including stale interest rates, incorrect offer categories,
  invalid links, missing structured fields, contradictory free text, and
  inconsistent loan-to-value tiers; and
- some tickets remaining open for more than six months, with weaker escalation
  routes for participants without Service Management Portal access.

| Stage | What this supports | What it cannot support |
|---|---|---|
| Formal access | A live data-sharing ecosystem has reached substantial administrative use. | That each user actively shared data, compared products, or switched. |
| Data quality | Accuracy, completeness, timeliness, standardization, and error handling are material conditions of choice. | The share of all products or consumers affected, or the size of any price loss. |
| Switching | Poor data can create a hidden comparison and switching tax; workarounds may be needed. | That a particular consumer failed to switch or paid more because of the defect. |
| Remedy | Escalation and resolution pathways affect whether the formal right is usable. | A verified correction, refund, better product, or restored trust. |
| Small business | Accounting and reconciliation tools depend on alignment between CDR data and other digital channels. | Productivity gains, firm survival, or unequal small-business incidence. |

## What connects to the wider program

This is the digital version of the same pattern seen in public systems,
insurance, and local infrastructure:

1. **A formal option is not a practical option.** A portability right requires
   usable data, a receiving service, time to compare, and a route to correct
   mistakes.
2. **Infrastructure quality is experienced through failure handling.** A stale
   field may be invisible until a person relies on it. The legitimacy test is
   then whether the error can be found, escalated, corrected, and explained in
   time.
3. **Choice can be asymmetric.** Large providers may have technical staff and
   portal access; small providers and consumers may carry the workaround cost.
4. **Use is not benefit.** 1.3 million users is an ecosystem scale signal, not
   a consumer-welfare measure.
5. **Exit is not the only outcome.** A person may stay because the service is
   good, because switching is costly, because the error is unresolved, or
   because alternatives are unavailable. These meanings must be separated.

## Comparison with existing remedy evidence

The project’s CFPB layers already distinguish complaint visibility, company
response, explanation, non-monetary relief, monetary relief, and verified
consumer remedy. The CDR record adds an upstream digital-infrastructure stage:
bad or stale shared data can shape the consumer’s option set before a complaint
is even filed.

The comparison fits because both systems ask whether a formal consumer right
can produce a usable correction or alternative. It does not mean the Australian
CDR and U.S. financial complaints share a population, law, product, or outcome
measure. The CDR survey is a small stakeholder sample; CFPB records are
complaint-system outputs. They must remain separate evidence packets.

## Counterexamples and alternative explanations

- A product can be accurately represented and still be unsuitable or too costly
  for a consumer.
- A stale field may be corrected before it changes a purchase or switching
  decision.
- A long ticket may reflect a complex legacy system while bilateral support
  resolves simpler cases quickly.
- Users may value budgeting, account aggregation, or record access without
  switching providers.
- Standardization may improve comparison but remove useful product detail or
  impose disproportionate compliance costs on smaller providers.
- A consumer may not switch because of trust, identity, habit, exit fees, or
  service quality—not because the data were defective.

These alternatives prevent a direct leap from data-quality ratings to consumer
harm.

## Bounded social discussion

- [Telecom switching discussion](../../social-discussions/records/atlas-ofcom-telecom-switching-linkedin-001.json)
  interprets switching as an affordability response shaped by inertia, missed
  bills, downgrades, and cancellations. It does not show whether switchers got
  better outcomes.
- [Platform non-use discussion](../../social-discussions/records/platform-exit-001.json)
  describes exit as nonlinear and reversible under social and platform
  pressure. This helps challenge the idea that “exit” is a simple binary.
- [Reddit quitting discussion](../../social-discussions/records/platform-exit-003.json)
  shows substitution and disagreement about what counts as leaving a platform.
  It is a self-reported anecdote, not a prevalence estimate.
- [X collective-break discussion](../../social-discussions/records/platform-exit-x-001.json)
  shows how a public break can become another platform ritual. Visibility of an
  exit action is not durable non-use.

These discussions add the cultural meaning of choice and exit. They do not
verify data quality, switching, savings, or remedy.

## Stronger next test

The next acquisition should follow a repeated product or account comparison
through a transparent event ledger:

```text
consumer or small business
  -> data-sharing consent
  -> fields received and quality errors
  -> comparison or recommendation
  -> application, switch, stay, or abandonment
  -> price, fee, service, fraud, or productivity result
  -> error report and resolution time
  -> correction, repeat use, trust, or exit
```

Minimum fields are product, date, data-holder, recipient, error type, affected
field, resolution route, time to correction, decision taken, and outcome. If
consumer-level data are unavailable, use repeated product-level audits and
clearly label the result as infrastructure quality rather than consumer welfare.

## Current answer

**Answer state: partly answered.** The CDR has meaningful scale, but the
evidence shows that formal portability can remain a fragile option when data are
stale, incomparable, or difficult to correct. Actual switching, savings,
productivity, and durable trust remain open.

Related project: [US customer service, automation, and the right to reach a
person](README.md). Related operating plan: [ongoing cross-source theme-mining
program](../../ONGOING-GOAL-OPERATING-PLAN_V1.md).
