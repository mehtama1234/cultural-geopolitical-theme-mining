# Material exposure to political meaning/action: status ledger v1

**Checked:** 2026-09-16  
**Status:** focused program-control synthesis; not a new estimate  
**Purpose:** choose the next broad-program test without collapsing judgment,
trust, action, turnout, and withdrawal into one outcome

## The bridge we are trying to close

The broad program asks how an ordinary material or institutional experience
becomes political meaning or action:

```text
dated exposure or institutional episode
  -> alternatives, effort, money, time, or security change
  -> attribution, identity, fairness, or perceived control
  -> trust, judgment, civic action, turnout, organizing, switching, or exit
  -> institutional, firm, policy, or state response
  -> later security, legitimacy, or power
```

The current atlas has evidence at nearly every stage, but usually in separate
units, waves, or designs. This ledger records the strongest available route and
the missing join instead of presenting those layers as one causal story.

## Current evidence routes

| Route | What is actually measured | Strongest supported link | What remains open |
|---|---|---|---|
| **HTOPS April→June panel** | Same selected respondent; baseline expense difficulty, later food insufficiency, energy-bill inability, job loss, and June congressional confidence | Material condition precedes later material outcomes; political confidence is a useful counterexample to mechanical translation | Dated bill/actor, attribution, remedy, prior identity, action, recovery, and attrition-adjusted inference |
| **CCES material/work proxy screen** | Same post-election respondent; gig work and student-loan responsibility crossed with federal/state trust and six civic actions | Trust and action differ across joint proxy cells and are not monotonic; low trust does not equal withdrawal | Dated shock, burden, reason, schedule control, prior trust, desired action, remedy, and causal uncertainty |
| **CES medical-affordability module** | Same respondent; reported medical-expense hardship, responsibility attribution, and separate political actions in 2018/2020 | Local rerun reproduces the existing hardship → attribution/action screen, including distinct contact/protest patterns | A dated bill or care event, payment/choice, remedy, trust change, recovery, and design-based uncertainty; see the [reproduction audit](projects/us-health-cost-household-choice/cces-medical-affordability-action-reproduction-audit-2026-09-16.md) |
| **ANES 2016–2020–2024 panel subset** | Repeated-panel respondent subset; pre-election financial worry crossed with federal trust and post-election reported vote | Worry is temporally ordered before reported vote, with non-monotonic trust and vote patterns | Direct material exposure, attribution, prior party identity in the causal design, action beyond vote, institutional response, and representative retention |
| **CPS 2024 Voting Supplement** | Person/household survey; registration, voting, and reported participation barriers | Political participation and nonparticipation are distinct observed outcomes with social-position differences | Whether a specific material or administrative burden caused the reported barrier, plus trust, remedy, and later behavior |
| **Public-system and consumer route designs** | Program/complaint/service records and proposed same-episode ledgers | Visibility, route, effort, response, and remedy can be specified as an episode | A linked recipient outcome showing attribution, trust, action, recovery, switching, or exit |
| **Practical-exit contract dry-runs** | 27 platform-remedy cases and 25 CFPB student-loan event-ledger rows, plus SHED same-respondent adaptation | Access restoration, complaint routing, response labels, and repeated consumer adaptation are separately observable | Alternatives, remedy receipt, protected/sacrificed outcome, later trust/action, switching, non-use, and exit remain sparse or unknown; see the [cross-domain observability audit](projects/us-customer-automation-recourse/practical-exit-observability-audit-v1.md) |
| **Capacity/dependence realization lane** | US data-center and Poland JASSM-ER ledgers; 74-row JASSM/LRASM supplier-control surface | Commitment, capacity, governance, supplier identity, planned delivery, and operational-stress stages are visible | Accepted output, replaceability, public/partner incidence, and changed external behavior; see the [realization-stage audit](projects/ai-work-control/capacity-dependence-realization-audit-v1.md) |
| **SIPP material-to-buffer gate** | Existing local SIPP utility condition at month *t* followed by credit-balance and savings-account fields at month *t+1*; 294,145 pair keys matched to 240 replicate weights | The field-timing test found zero valid adjacent-month credit or savings state changes, so these fields cannot supply a monthly borrowing, repayment, or recovery arrow | Dated bill/transaction, shutoff or assistance event, genuine buffer movement, payment success, recovery, and later meaning/action; see the [gate memo](projects/us-household-calendar-integration/sipp-utility-buffer-following-gate-v1.md) |

## What the evidence says now

1. Material pressure can persist into later material hardship for the same
   selected respondents, but it does not automatically produce low confidence
   or one political response.
2. Trust, judgment, action, turnout, and withdrawal are different outcomes.
   They can coexist, diverge, or move through different institutions.
3. Joint conditions and social position matter. A pooled hardship-to-distrust
   rule hides counterexamples and interaction patterns.
4. The decisive missing variables are not another generic sentiment measure;
   they are the event, responsible actor, alternative, attribution, action
   route, response, and later recovery or exit.

## Quantitative checkpoint from existing local records

The current numbers sharpen the boundary without creating a pooled effect:

- In the linked April→June 2025 HTOPS respondents, 41.8% remained in the
  baseline “any expense difficulty” state and 7.5% moved from difficulty to no
  difficulty. Among the same linked frame, 5.2% moved into high confidence in
  Congress while 5.3% moved out of it. The panel demonstrates persistence and
  change on different clocks; it does not identify the bill, actor, remedy, or
  political cause.
- In the ANES 2024 panel subset, 70.3% of the extremely worried row reported
  some or never trusting the federal government versus 51.9% of the not-at-all
  worried row. Reported presidential vote also differed: 68.9% of the very
  worried row reported Trump versus 32.0% of the not-at-all worried row. These
  are temporally ordered descriptive contrasts, not a causal economic-voting
  estimate; worry is not a dated bill or payment shock.
- In the CCES 2024 material/work proxy screen, federal trust plus any selected
  civic action was 30.32% among respondents reporting both gig work and student
  debt, compared with 16.42% among respondents reporting neither. Federal low
  trust plus action was 16.11% in the former cell versus 18.66% in the latter.
  The non-monotonic pattern is precisely why low trust cannot be equated with
  withdrawal or proxy conditions with causation.

These figures are intentionally reported by source and denominator. Their
convergence supports prioritizing an event-compatible design; it does not
support adding them into a material-to-action score.

The current rotation has also tested the endpoint definition outside survey
attitudes. Platform and CFPB records show that institutional visibility can be
measured without same-unit exit, while infrastructure/procurement records show
that capacity and supplier identity can be measured without accepted output or
changed external behavior. These are parallel boundary findings, not one
material-to-action dataset.

## Next decisive test

Prioritize one existing panel or event-compatible source that can observe a
dated episode. The minimum record is:

```text
event date and actor
  -> attempted use, alternative, effort, payment/time trade-off
  -> attributed cause and perceived fairness/control
  -> distinct action (complaint, contact, vote, organizing, switching,
     non-use, or withdrawal)
  -> institutional or firm response
  -> remedy, persistence, recovery, trust, or exit
```

The first executable option is a same-respondent panel with a defined event
and repeated meaning/action measures. If that is unavailable, use a
same-case public, consumer, financial, or workplace episode ledger. A matched
place or policy design is a third option, provided it measures action and
attribution separately from aggregate turnout or sentiment.

The immediate local test is to use the retained HTOPS panel output as a
measurement audit: identify whether any shared respondent has a valid dated
exposure, attributed actor, or action field before attempting another estimate.
The raw PUFs are not currently retained locally, so no rerun or new panel
estimate is claimed in this pass.

## Promotion rule

Do not promote a material-to-action claim unless the writeup states which of
the following it has established:

- **Observed:** the same unit reports or records the exposure and outcome;
- **Reported:** the source reports an experience, judgment, or action but not
  the underlying mechanism;
- **Compared:** groups, periods, places, or source layers differ on aligned
  measures;
- **Estimated/identified:** a stated design supports an association or causal
  estimate with valid uncertainty; or
- **Open:** the link is a hypothesis or requires a new event-compatible test.

Cross-source convergence can justify prioritizing a trend. It cannot, by
itself, establish that one household's material experience caused one person's
political meaning or action.

Related evidence: [material pressure and political meaning](projects/us-cost-trust-politics/material-pressure-to-political-meaning-synthesis-v1.md),
[material-to-participation bridge](projects/us-cost-trust-politics/material-to-participation-cross-source-bridge-v1.md),
[CCES material/work layer](projects/us-cost-trust-politics/cces-material-proxy-trust-action-layer-v1.md),
[ANES panel layer](projects/us-cost-trust-politics/anes-2024-panel-judgment-action-layer-v1.md),
and the [broad next-pass queue](US-BROAD-NEXT-PASS-QUEUE_V1.md).
