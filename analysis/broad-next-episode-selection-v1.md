# Broad next-episode selection v1

**Status:** ranked route decision; promotion gate applied; no qualifying local end-to-end route
**Checked:** 2026-10-20
**Machine record:** [next-episode selection](data/broad-next-episode-selection-v1.json)

## Decision

The existing MEPS 2024 staged event ledger was the primary local depth route.
Its 18,457 privacy-minimized person/event rows provide a dated first
event-family scaffold with payment, coverage, health, employment, and bill
context. A strict event-window follow-up also carries the same person to R5/3
health and employment transitions. The completed stage audit shows that the
local representation still lacks the initiating need, usable alternatives,
event-specific response, verified remedy, and meaning/action endpoint.

The [MEPS 2024 episode closure audit](projects/us-health-cost-household-choice/meps-2024-episode-closure-audit-2026-10-20.md)
now closes repetitive MEPS payment/event refinement as a route decision: the
committed bounded outputs remain the primary public comparator, but no further
MEPS cross-tab should be promoted unless a newly available file adds an
episode-level field. The next primary route is therefore the registration-gated UAS acquisition
specified in the [UAS health-cost episode audit](projects/us-health-cost-household-choice/uas-health-cost-legitimacy-acquisition-audit-v1.md).
UAS is the smallest identified candidate that could connect a reported
medical-expense event to later health/work/well-being measures and, through
UAS 537 or 698, add care choice, bill, provider-experience, and
institution-specific trust fields. No UAS respondent files are currently
retained or acquired.

The route is authorization-gated in two senses. The current UAS terms require
registration and expressly restrict automated access and LLM management,
processing, or analysis of distributed respondent data without written
authorization. Therefore UAS is a human/account-holder handoff candidate, not
an autonomous next execution lane. The required file, overlap, timing, weight,
missingness, and remedy gates remain unchanged if compliant access is supplied.

Keep the CFPB/platform records and the named Cash App, BrightSpeed, and
Navient redress records as storage-light remedy counterexamples and fallback,
not as a substitute for the missing UAS/MEPS middle. They provide stronger
institutional response and partial remedy or distribution evidence, but sparse
alternatives, receipt, durability, trust, and exit. Keep SHED and HTOPS as
panel context; do not join any of these sources into one person or household
story.

## Promotion-gate result

No currently retained route qualifies for promotion to a new end-to-end
finding. The governing gate requires both (a) an episode-level alternative or
non-use observation and (b) a receipt or outcome follow-up. MEPS fails both
requirements in its staged rows. The CFPB/platform route supplies formal
response and redress comparators, but not recipient-level receipt or a defined
post-remedy outcome. SHED/HTOPS supply persistence or adaptation context, but
not a dated actor-linked remedy episode. UAS is the best next acquisition
candidate for a same-respondent health-cost route, but its files are not yet
available and its documentation does not establish a verified remedy field.

The next pass may be promoted only after an acquired or lawfully linked source
demonstrates both gate fields, reports their denominators and missingness, and
preserves the distinction between institutional response and lived outcome.
Until then, the correct output is an acquisition boundary or route-specific
comparator—not a new causal or pooled trend claim.

The retained bridge matrix now also includes the April-to-June HTOPS
material-pressure-to-option-search route. It strengthens the navigation stage:
people under expense pressure search for work, food, benefits, credit, housing,
and medical options. It does not add a usable alternative, completed
application or transaction, remedy receipt, recovery, trust, or exit, so it
does not change the `qualifying_local_route: false` decision.

The machine record cross-checks this decision against the [authoritative
same-case gate](data/broad-same-case-episode-availability-audit-v1.json): 41
local surfaces, nine observed alternative/non-use surfaces, three observed
verified-remedy or outcome-follow-up surfaces, one observed meaning/action
surface, and `qualifies: false`.

## Required MEPS depth test

Before promoting another finding, inspect whether the staged MEPS rows contain:

```text
dated event
  -> initiating need and usable alternative
  -> care choice/delay and payment timing
  -> work, unpaid-care, food, housing, or debt trade-off
  -> provider/insurer/employer response and verified remedy
  -> later health, security, trust, action, switching, or exit
```

If the UAS fields or overlap fail the acquisition gates, the result is a
verified acquisition gap—not a reason to infer a bill-to-recovery chain from
round-level context. The CFPB/platform route remains the next small
remedy-focused comparison, while the broad 14-theme rotation continues through
other lanes.

## Why this is the right broad-program move

The choice preserves breadth and depth simultaneously. MEPS can deepen the
household, care, health, work, financial, and institutional themes; the CFPB
and platform cases preserve consumer power and recourse; SHED/HTOPS preserve
adaptation, persistence, trust, and political context. The sources remain
layered evidence surfaces, not a fabricated end-to-end case.

## Reproduction

```text
python3 scripts/validate_broad_next_episode_selection.py
```

No new raw data are downloaded by this decision artifact.

## Availability recheck — 2026-10-20

The closure audit and current handoff state were rechecked against the local
selection controls. No authorized UAS, PSID, HRS, or raw MEPS respondent file
is present locally; the committed MEPS outputs remain available as bounded
comparators. This is a control-state update, not a new estimate or permission
to retrieve registration-gated data.

## Availability recheck — 2026-09-21

The post-crash local-input recheck still finds no retained `/tmp/cgtm-meps-2024`,
`/tmp/us-broad-sipp-2025`, `/tmp/us-broad-psid`, or `/tmp/cgtm-uas` source
directory. The committed bounded outputs remain usable for synthesis and
validation, but no respondent-level rerun or UAS/PSID promotion is authorized
by the current local state.

The direct script check also confirms that the raw HC-256/BRR and HC-254 event
files required to rerun the dated MEPS event screen are absent. This is the
same acquisition boundary as the health-cost episode protocol, not a new
estimate or a reason to infer the missing middle from committed derivatives.

## Public-only fallback depth selection — 2026-09-20

Because no authorized respondent file is present, the next non-acquisition
depth pass should use the smallest existing recipient-side remedy route: the
[CFPB Ombudsman redress reissue example](projects/us-customer-automation-recourse/cfpb-ombudsman-redress-reissue-route-v1.md).
It is not a population estimate and it does not replace UAS or MEPS. It is the
best public comparator because the record already contains a failed or expired
payment route, recipient effort, escalation, and facilitated institutional
response.

The pass should stop unless it can document the following in the same example
or a clearly bounded comparable set:

```text
redress eligibility
  -> notice and failed/attempted receipt
  -> effort, delay, and escalation
  -> reissue or correction
  -> actual cashing/receipt and amount
  -> adequacy, residual loss, and later account status
  -> continued use, switching, trust, or exit
```

The current public record ends before actual cashing and adequacy. Therefore
the immediate output should be a route-level implementation audit or a
verified acquisition gap, not a new recovery finding. This selection advances
the consumer-power and public-systems lanes while preserving the broader
longitudinal acquisition boundary.

## Fallback audit handoff — 2026-09-20

The public-only CFPB depth pass is complete. The Ombudsman example now has an
explicit stage audit: payment route, failed or incomplete receipt, recipient
effort, and institutional escalation are reported; reissue receipt, cashing,
adequacy, residual loss, trust, and exit remain unreported. Aggregate CFPB
cashing or redistribution figures do not substitute for this recipient's
outcome.

This closes the current consumer recheck. The program should return to the
broader rotation: keep UAS and MEPS as authorization-gated high-value routes,
and use the public-systems/safety-net implementation specification as the next
structural handoff if no compliant respondent file is supplied. No new
consumer recovery claim should be added from the Ombudsman example.

## Public-systems fallback update — 2026-10-19

The public-systems handoff has now been executed through the
[SNAP public-benefit episode acquisition gate](projects/us-safety-net-access/public-benefit-episode-acquisition-gate-2026-10-19.md).
Two official administrative cases add contrasting same-case partial endpoints:
Connecticut records a replacement card and agency-reported $582 credit followed
by residual-claim denial, while New Jersey records investigation, hearing, and
affirmed denial. These cases strengthen the administrative decision and remedy
stages but do not expose food adequacy, later household security, trust, or
exit. The local promotion result therefore remains `false`; the next decisive
route is still authorized UAS/MEPS input or a new identifier-bearing public
episode with downstream outcome evidence.
