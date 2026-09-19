# Broad same-case episode availability audit v1

**Status:** stage-availability audit; no synthetic episode or causal estimate
**Checked:** 2026-09-19
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
| IER individual remedy follow-ups (5 resolution summaries) | Four agency-reported individual paid-remedy cases, one back-pay offer, and employer training/policy controls | Employer and worker identities, alternatives, payment instruments, restored work, durable compliance, household recovery, trust/action, exit |
| IER individual-remedy event ledger (5 events) | Machine-readable case-level dates, reported individual payments/offers, and employer controls | Episode-level alternatives, independent receipt confirmation, restored work, durable compliance, household recovery, trust/action, exit |
| IER telephone-intervention remedy ledger (4 cases) | Barrier-to-intervention-to-correction sequence, including reported rehire, continued work, and back pay | Worker confirmation, accepted restoration, alternatives, receipt, durable compliance, household recovery, trust/action, exit |
| IER DACA bilateral remedy (1 case) | Lower-wage rehire, worker complaint, signed agreement, restored wage, back pay, seniority, and complaint withdrawal | Payment instrument/date, durable employment, benefit use, household recovery, trust, recurrence, exit |
| OSHA Texas asbestos whistleblower case (2 workers) | Safety/environmental voice, retaliatory termination, OSHA finding, reinstatement order, and ordered back wages/damages | Payment, actual safe return, employer compliance, community protection, household recovery, trust, exit |
| Warraich single-case follow-up (1 episode) | Formal unfairness finding, reactivation order, lost-pay direction, targeted public follow-up search | Actual access restoration, payment/receipt, continued work, alternative work, household recovery, switching/exit |
| Hotak access-restoration follow-up (1 episode) | Voluntary reactivation, more than 150 subsequent trips, formal reactivation order | Payment/receipt, net recovery, durable access, alternatives, household outcome, switching/exit, non-retaliation |
| Rehman lost-remuneration ledger (1 episode) | Worker application, voluntary/formal access restoration, no substitute paid earnings to deduct, and gross lost-remuneration order | Alternative availability or choice, payment receipt, net recovery, durable access, trust/action, switching/exit |
| Mansoor substitute-earnings ledger (1 episode) | $9,000 Baysec earnings, estimated $1,760 Didi increase, reactivation, and $6,073.23 gross lost-pay order | Alternative equivalence/choice, payment receipt, actual access, durable work, household recovery, trust, switching/exit |
| FWC site-clearance alternative-employment ledger (1 episode) | Dismissal after site-clearance loss, lower-paid replacement work, travel-cost trade-off, and compensation order | Payment receipt, equivalence/duration of alternative work, household recovery, trust/action, recurrence, exit |
| FWC Greaves no-alternative-employment ledger (1 episode) | Primary adjudicated dismissal, unsuccessful job search, assessed eight-week loss, and compensation order | Payment receipt, later employment, household recovery, trust/action, recurrence, exit |
| FWC customer-allocation non-return ledger (1 episode) | Eleven job applications, new employment, explicit non-return reasoning, assessed loss, and compensation order | Payment receipt, job duration, standardized trust measure, household recovery, recurrence, switching/exit |
| FWC alternative-work client-redirection ledger (1 episode) | Alternative surf-shop earnings, client redirection, relationship breakdown, and staged compensation order | Instalment receipt, later work, household recovery, standardized trust, recurrence, switching/exit |
| FWC Westrip alternative-employment ledger (1 episode) | Five-week transition to alternative employment, no-income interval, non-return through compensation in lieu of reinstatement, and $3,744 order | Payment receipt, job duration, household recovery, durable trust, recurrence, exit |
| FWC Meadley enforced-payment ledger (1 episode) | Officially reported compensation payment, failed reinstatement, worker enforcement, and further court relief | Alternative/non-use, later employment, household recovery, durable trust, recurrence, exit |
| SHED recontact panel (4,419 respondents) | Adaptation, care/financial persistence, later status | Dated actor/event, institutional response, remedy, meaning/action, exit |
| HTOPS linked panel (6,564 respondents) | Same-ID timing, later material outcomes, institutional confidence | Actor, alternatives, attribution, action, remedy, recovery/exit |
| MEPS bounded event ledger (3 event surfaces) | Person-linked event ordering, payment and later health/work context | Complete route, remedy, trust/action, practical exit |
| CFPB medical-debt route (49 locally filtered cases) | Dated complaint, coarse place, institutional routing, response label | Underlying bill/care choice, alternatives, verified remedy, recovery, trust/action, exit |
| Doxo bill-payment enforcement case (2 observations) | Search-route and official-channel confusion, alleged fees, complaint-level payment-timing/service-risk consequences, order-stage controls | Person-level payment success, bill status or service continuity, remedy receipt, trust, switching/exit |
| Grubhub multisided remedy program (1 reported program) | Aggregate checks/PayPal payments and prospective worker, account, and restaurant controls | Group-specific exposure, individual receipt, restored income/access, alternatives, trust, switching/exit |
| VRURC portable-charger recall bridge (1 recall key) | Dated hazard notice, replacement instruction, later recall-level correction snapshot | Purchaser exposure, notice/replacement receipt, safe restoration, residual cost, trust, switching/exit |
| Honda Talon repair ledger (1 recall key) | Dated vehicle hazard, direct-contact claim, dealer-repair route, later correction snapshot | Purchaser exposure, repair receipt, downtime, safe mobility, residual cost, trust, switching/exit |
| CFPB credit-card monetary-relief ledger (25 cases) | Complaint receipt, routing, timely handling, and monetary-relief response label | Account exposure, alternatives, issuance/receipt, correction, remaining loss, trust, switching/exit |
| FWC Adcon liquidation ledger (1 episode) | Employer shutdown, unpaid notice/redundancy, reported family/financial stress, lower-paid replacement work, $9,584 alternative earnings, liquidation, and $17,531.43 compensation order | Compensation receipt, FEG recovery, job duration, household recovery, durable trust, recurrence, exit |

## Stage-level coverage count

The 32 surfaces can also be summarized without pooling their units. A status is
classified as **observed** when it begins with `observed`, **partial** when it
begins with `partial`, and **open/unknown** for all other labels (including
reference-period and unknown statuses).

| Required stage | Observed | Partial | Open/unknown |
|---|---:|---:|---:|
| Dated event or exposure | 28 | 2 | 2 |
| Responsible actor | 21 | 9 | 2 |
| Alternative or non-use | 8 | 7 | 17 |
| Effort, money, or time trade-off | 7 | 19 | 6 |
| Adaptation or protected/sacrificed outcome | 10 | 11 | 11 |
| Institutional or firm response | 29 | 1 | 2 |
| Verified remedy | 3 | 22 | 7 |
| Meaning, trust, or action | 1 | 9 | 22 |
| Recovery, persistence, or exit | 2 | 11 | 19 |

This count is a stage-availability diagnostic, not a success rate or a common
denominator. It identifies the sharpest broad-program bottleneck: records can
show that an event occurred and that an institution responded, while they do
not show what alternative the affected unit had, whether the remedy was
received, or what happened to meaning, recovery, or exit.

## Result

No current local source supplies all nine required stages. The IER summaries
advance the verified-remedy stage with four agency-reported individual
payments, while the DACA bilateral case adds reported wage and seniority
restoration plus complaint withdrawal, and the OSHA case adds protected safety
voice, retaliation, and an ordered remedy. None supplies durable recovery,
trust, recurrence, or exit. The platform ledger,
the CFPB named redress/distribution records, and the Doxo and Grubhub
consumer-remedy records,
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

The machine record now encodes the promotion decision explicitly: `qualifies`
is `false`, eight retained surfaces observe an alternative or non-use field, and
three retained surfaces observe verified remedy receipt or a defined outcome
follow-up. A future pass must satisfy both gate fields before a new
end-to-end finding is promoted.

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

The audit uses thirty-two committed local source surfaces and downloads nothing.
