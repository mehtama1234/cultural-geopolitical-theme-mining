# IBM Germany works-council AI framework governance record v1

**Status:** archived agreement and representative implementation account;
pre-deployment governance and formal controls observed; live worker outcome
not observed
**Checked:** 2026-09-15

## Why this record matters

The platform-deactivation cases ask whether a worker can recover after an
adverse decision. The IBM Germany record tests an earlier point in the chain:
whether worker representatives can shape the conditions under which AI enters
the workplace at all.

It is therefore an anticipatory-control case, not evidence of a successful
individual appeal or a measured productivity effect.

## Source and scope

The archived text of the IBM Central Holding GmbH / Group Works Council
agreement identifies a signature date of 30 July 2020. The agreement governs
the introduction and use of AI systems within its stated scope. A 2022 BTQ
Kassel interview with an IBM Group Works Council representative describes the
framework as created early, before AI applications had affected employees'
daily work, and reports examples of systems in use or not used in Germany.

The agreement text is available through [WageIndicator's archived
transcription](https://wageindicator.org/de-de/arbeiten-in-deutschland/tarifvertrag/konzernbetriebsvereinbarung-uber-die-einfuhrung-und-den-einsatz-von-systemen-der-kunstlichen-intelligenz-artificial-intelligence).
The implementation account is the [BTQ Kassel interview with Frank
Remers](https://www.btq-kassel.de/interview_frank_remers/). The local
[German works-council source record](german-ai-works-council-source-record-v1.md)
preserves acquisition details and hashes.

A peer-reviewed comparative article independently describes the 2020 IBM
agreement as a joint works-council, HR, and expert project and identifies its
human-final-decision principle and AI Ethics Council. This corroborates the
governance architecture, while still not supplying a live intervention or
worker outcome.

## Governance matrix

| Control stage | What the record provides | What remains open |
|---|---|---|
| Before deployment | Group Works Council agreement and stated early framework | Whether every covered system was actually submitted before use |
| Risk classification | Categories of AI use, including a highest-risk category | Classification record for a named live system |
| Transparency | Explainability, information, and inspection language | Worker receipt, comprehension, and response time |
| Human authority | Principle that AI supports decisions and a human makes the final decision | Whether the human could reject the output and how often that occurred |
| Data and quality | Data-quality, bias-analysis, and algorithm-quality checks | Completed audit, error rate, and remediation log |
| Correction | Correction process for false recommendations; rapid correction route for higher-risk systems | A named false recommendation corrected in practice |
| Collective escalation | AI Ethics Council and works-council inspection rights | An intervention, decision, or deployment changed by those bodies |
| Personnel effects | Category-5 restriction on recommendations or automatic personnel measures without substantial workforce benefit or harm reduction; retraining/equivalent-job language | Coverage, enforcement, and actual effect on job security or mobility |

## Named implementation signals

The source packet identifies a “Skill Recommendation” tool that uses workplace
data to suggest development options while retaining a human decision-maker.
The BTQ interview reports internal call-center and training/career
recommendation systems in use, while a manager salary-increase recommender and
a voluntary-resignation probability system were not used in Germany at that
time.

These details are valuable because they distinguish system functions and
deployment decisions. They remain reported practice, not an independently
audited inventory of all IBM systems.

## Mechanism

```text
works-council bargaining
  -> risk classification and inspection rights
  -> limits on data use and automatic personnel action
  -> correction / escalation / retraining routes
  -> possible worker influence before adverse output
```

The strongest observed link is from collective representation to written
governance conditions. The missing links begin at actual system submission and
continue through worker use, correction, changed workflow, and material
outcome.

## Remedy and control coding

```text
intervention timing              observed_ex_ante_and_ongoing_rule
worker representation            observed_group_works_council
explanation / transparency       observed_rule
human review                     observed_rule
correction                       observed_rule
collective escalation            observed_rule_and_reported_institution
deployment exclusion            observed_rule; high-risk non-use reported by representative
worker-level correction          not_observed
pay / time / stress outcome      not_observed
anti-retaliation                 not_observed
```

## Comparison with post-harm platform remedies

```text
IBM Germany:  representation -> rules before deployment -> outcome open
Bandameeda:   deactivation -> external review -> reactivation + pay order
Kumar:        rating-based deactivation -> compliant review -> dismissal
```

The IBM case expands the meaning of worker control. Control is not only the
ability to appeal an individual decision; it can also be the ability to inspect
the system, set risk boundaries, require human authority, and exclude a class
of personnel decisions before they become routine. But a written ex-ante rule
should not be counted as a worker outcome without a live intervention record.

## Decisive next acquisition

Find one named IBM Germany deployment covered by the agreement and recover:
its risk classification, notice, works-council review, data-quality or bias
assessment, worker challenge, correction or non-deployment decision, and any
measured effect on work, pay, mobility, or stress.

## Sources

- [WageIndicator transcription of the IBM AI framework](https://wageindicator.org/de-de/arbeiten-in-deutschland/tarifvertrag/konzernbetriebsvereinbarung-uber-die-einfuhrung-und-den-einsatz-von-systemen-der-kunstlichen-intelligenz-artificial-intelligence)
- [BTQ Kassel interview with IBM Group Works Council representative](https://www.btq-kassel.de/interview_frank_remers/)
- [Peer-reviewed study on German union strategies for workplace AI](https://doi.org/10.1177/10242589221142273)
- [German works-council AI source record](german-ai-works-council-source-record-v1.md)
- [AIM-WORK exposure to institutional safeguard crosswalk](aim-work-institutional-safeguard-crosswalk-v1.md)

## Boundary

The agreement and interview establish a documented governance architecture and
reported implementation signals. They do not establish complete coverage,
compliance, enforcement, worker-level benefit, or prevention of all monitoring
or adverse personnel decisions.
