# Kenya Ziada human-review platform record v1

**Status:** official ILO case-study record; human mediation observed in platform practice

**Checked:** 2026-09-15

## Why this record matters

The Kenya digital-labour study provides a useful counterexample to the idea
that platform ratings must lead directly to automated discipline. It describes
Ziada, a local platform for domestic, beauty, and personal services, as using
staff discussion and mediation when a worker receives a low rating. The study
contrasts this with local taxi and delivery platforms where ratings,
cancellation rates, bonuses, and acceptance rates can feed penalties or account
deactivation.

This is not a verified legal remedy or a representative estimate of Kenyan
platforms. It is an observed organizational design choice: a platform can
insert human interpretation between a rating and a worker consequence.

## Official source

- [ILO PROSPECTS: Digital labour platforms in Kenya](https://www.ilo.org/sites/default/files/2024-06/24004-ILO-Digital-Labour-Kenya-v6%20Final%20May%2031%202024.pdf)
- Relevant discussion: pp. 27–29 (PDF pages 50–51), section 2.4.4–2.4.5

## Evidence matrix

| Stage | What the ILO case study reports | Boundary |
|---|---|---|
| Rating input | Ziada worker ratings are influenced by client experiences | No underlying rating dataset or threshold was acquired |
| Potential adverse signal | A low rating may reflect overall service quality rather than task performance; the study gives a cleanliness example for a plumber | Illustrative case description, not a random sample of disputes |
| Human review | Ziada staff discuss low ratings with workers and clients to understand the reason | The study does not specify a formal appeal deadline, reviewer independence, or written decision |
| Corrective response | Staff advise workers on broader service quality and seek improved outcomes for worker and platform | No individual rating change, account restoration, or payment correction is documented |
| Comparison platform | Little evaluates driver quality using star ratings and cancellation rates; low ratings or acceptance rates may lead to deactivation | The study does not establish that every deactivation is automated or unlawful |
| Governance implication | Human intervention can mediate a rating before it becomes a penalty or deactivation | Whether mediation is accessible, consistent, or free from retaliation remains open |

## Remedy coding

| Remedy field | Code | Reason |
|---|---|---|
| Concrete adverse signal | `observed_case_study` | Low rating and disputed service-quality assessment |
| Worker contest or mediation | `observed_practice` | Staff engage with workers and clients about the rating |
| Human review | `observed_practice` | Human staff interpret the context before disciplining |
| Explanation | `observed_practice` | Discussion identifies why a rating may not measure task performance |
| Rating correction | `not_observed` | No explicit score change is reported |
| Account restoration | `not_observed` | No deactivation reversal is reported for Ziada |
| Payment or compensation | `not_observed` | No payment remedy is reported |
| Anti-retaliation | `not_observed` | No post-review retaliation measure is reported |
| Evidence strength | `medium` | Official institutional case study; not an administrative case file or representative survey |

## Interpretation

Ziada supplies an important design comparator:

```text
client rating
  -> human discussion and contextual interpretation
  -> advice / service improvement [reported]
  -> rating correction or protection from future penalty [open]
```

The case helps separate “human in the loop” as a formal claim from a more
specific question: does a person have authority and time to reinterpret the
signal before it changes access to work? It also shows why a review mechanism
should be coded for authority, timing, and outcome—not merely for the presence
of a human contact.

## Decisive next acquisition

Obtain Ziada worker terms, rating/complaint procedures, or anonymized dispute
records showing whether staff can remove or correct a rating and whether a
worker can challenge a deactivation. Compare those records with Little's
penalty and deactivation rules.

## Boundary

This record supports a documented platform-practice comparison. It does not
establish prevalence across Kenya, causality, legal compliance, or successful
worker remedy.
