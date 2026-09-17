# Broad same-case episode availability audit v1

**Status:** stage-availability audit; no synthetic episode or causal estimate
**Checked:** 2026-09-17
**Machine record:** [same-case episode availability audit](data/broad-same-case-episode-availability-audit-v1.json)

## Why this audit matters

The broad program's most important missing middle is not another measure of
pressure. It is the ability to follow one episode through the decision and
consequence chain:

```text
dated exposure
  -> actor and alternatives
  -> effort, money/time trade-off, and adaptation
  -> protected or sacrificed outcome
  -> institutional response and verified remedy
  -> meaning, trust, action, recovery, persistence, or exit
```

This audit tests whether the existing local records can support that route.
It keeps different respondents, complaints, health events, and survey panels
separate.

## Stage coverage

| Local source surface | Strongest stages | Critical missing stages |
|---|---|---|
| CFPB student-loan event ledger (25 rows) | Public route, complaint/event handling | Recipient alternatives, verified remedy, recovery, trust/action, exit |
| CFPB Cash App redress case (1 named enforcement event) | Fraud/dispute-process failure, formal redress ceiling, operational correction requirements | Individual loss, payment/receipt, correction time, repeat effort, alternative provider, trust, switching, exit |
| CFPB BrightSpeed distribution (1 named ongoing distribution) | Eligible class, aggregate compensable harm, named administrator, ongoing distribution status | Issuance, successful receipt, amount, residual loss, repeat effort, trust, switching, exit |
| CFPB Navient compensation (1 named ongoing payment record) | Official check/distribution status, named administrator, explicit non-reduction of underlying loan obligation | Person-level receipt, amount, balance/credit correction, remaining loss, effort, trust, switching, exit |
| Platform remedy dry-run (27 episodes) | Adjudication, reactivation, some lost-remuneration orders | Alternatives, remedy receipt/durability, post-event status, practical exit |
| OpenAI/Statsig PERM settlement (6 recruitment items) | Named recruitment-channel burden, claimant-identification route, potential back-pay, access-restoration controls, oversight | Applicant-level exposure, alternatives/effort, payment receipt, restored opportunity, durable compliance, trust/action, household recovery, exit |
| Apple PERM implementation (1 settlement event) | Named recruitment-channel burden, individualized lost-income review, $18.25m back-pay processing/exhaustion, access-control requirements | Individual payment distribution/timing, restored opportunity, post-monitoring compliance, worker voice, trust/action, household recovery, exit |
| Warraich single-case follow-up (1 episode) | Formal unfairness finding, reactivation order, lost-pay direction, targeted public follow-up search | Actual access restoration, payment/receipt, continued work, alternative work, household recovery, switching/exit |
| Hotak access-restoration follow-up (1 episode) | Voluntary reactivation, more than 150 subsequent trips, formal reactivation order | Payment/receipt, net recovery, durable access, alternatives, household outcome, switching/exit, non-retaliation |
| SHED recontact panel (4,419 respondents) | Adaptation, care/financial persistence, later status | Dated actor/event, institutional response, remedy, meaning/action, exit |
| HTOPS linked panel (6,564 respondents) | Same-ID timing, later material outcomes, institutional confidence | Actor, alternatives, attribution, action, remedy, recovery/exit |
| MEPS bounded event ledger (3 event surfaces) | Person-linked event ordering, payment and later health/work context | Complete route, remedy, trust/action, practical exit |
| CFPB medical-debt route (49 locally filtered cases) | Dated complaint, coarse place, institutional routing, response label | Underlying bill/care choice, alternatives, verified remedy, recovery, trust/action, exit |

## Stage-level coverage count

The 14 surfaces can also be summarized without pooling their units. A status is
classified as **observed** when it begins with `observed`, **partial** when it
begins with `partial`, and **open/unknown** for all other labels (including
reference-period and unknown statuses).

| Required stage | Observed | Partial | Open/unknown |
|---|---:|---:|---:|
| Dated event or exposure | 11 | 1 | 2 |
| Responsible actor | 7 | 5 | 2 |
| Alternative or non-use | 1 | 3 | 10 |
| Effort, money, or time trade-off | 1 | 9 | 4 |
| Adaptation or protected/sacrificed outcome | 2 | 4 | 8 |
| Institutional or firm response | 11 | 1 | 2 |
| Verified remedy | 0 | 8 | 6 |
| Meaning, trust, or action | 0 | 2 | 12 |
| Recovery, persistence, or exit | 0 | 5 | 9 |

This count is a stage-availability diagnostic, not a success rate or a common
denominator. It identifies the sharpest broad-program bottleneck: records can
show that an event occurred and that an institution responded, while they do
not show what alternative the affected unit had, whether the remedy was
received, or what happened to meaning, recovery, or exit.

## Result

No current local source supplies all nine required stages. The platform ledger,
the three CFPB named redress/distribution records,
the OpenAI/Statsig and Apple recruitment-remedy events, and the Hotak follow-up
come closest to a response/remedy/implementation surface;
MEPS, SHED, and HTOPS provide different kinds of person-level timing or
persistence, while Warraich supplies a formal-remedy boundary. These are useful
complements, but they cannot be joined into one consumer or household story.

The safe broad-program conclusion is therefore a measurement result: the atlas
has substantial exposure, adaptation, route, formal remedy, and selected follow-up evidence,
but not a closed same-case event chain. The medical-debt query initially
revealed an API sub-product filtering failure; the corrected local filter now
adds a bounded administrative route sample, but supplies no underlying
household episode or verified remedy. This explains why the program should
prioritize an episode key and stage-specific missingness over additional
cross-sectional pressure measures.

## Next decisive test

Choose one lawful source with a stable episode identifier—consumer complaint,
public-program case, financial account event, health-care episode, or workplace
intervention—and require actor, alternatives, effort, protected/sacrificed
outcome, verified remedy, attributed cause, later trust/action, and exit. A
valid negative result is one that shows which stages remain unavailable.

## Reproduction

```text
python3 scripts/validate_broad_same_case_episode_availability.py
```

The audit uses fourteen committed local records and downloads nothing.
