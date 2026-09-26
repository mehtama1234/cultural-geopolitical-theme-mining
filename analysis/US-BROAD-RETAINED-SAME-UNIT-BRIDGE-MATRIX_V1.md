# US broad retained same-unit bridge matrix v1

**Checked:** 2026-09-24
**Purpose:** identify what the strongest retained same-unit routes actually
close in the broad end-to-end model. This is a bridge audit, not a pooled
estimate or a claim that the rows describe the same people.

## Required chain

```text
dated condition or event
  -> alternative / non-use
  -> money, time, access, or control trade-off
  -> institutional response
  -> protected or sacrificed outcome
  -> verified remedy / recovery
  -> persistence
  -> meaning, trust, action, or exit
```

| Retained route | Same-unit evidence actually observed | Strongest closed bridge | Still missing or weak |
|---|---|---|---|
| [MEPS dated event → later panel](projects/us-household-constraint-cascade/meps-event-six-month-followup-v1.md) | Person-level event window before R4/2 context, then R5/3 health and employment levels and conditional transitions; BRR-weighted descriptive denominators | Dated event → later health/work status or transition | Event may follow the real need; no alternative, payer/claim identity, treatment continuity, institutional response, verified remedy, trust, action, or exit |
| [HUD assistance entry/exit → LEHD work trajectory](projects/us-census-hud-lehd-assistance-employment-trajectories/findings/us-census-hud-lehd-assistance-employment-trajectories-2026-001.md) | Census links HUD administrative participation records to matched employee-employer earnings records across 14-year windows around entry and exit; entry, exit, and stayer trajectories are compared | Housing-assistance transition → same linked unit's later employment/earnings trajectory | Assistance amount/timing, rent burden, housing quality, alternatives, exit reason, remedy adequacy, work/care trade-off, health, trust, action, and durable security |
| [HUD HEARS exit type → stability/health/wages](projects/us-hud-hears-exit-type-outcomes/findings/us-hud-hears-exit-type-outcomes-2025-001.md) | Two King County PHAs link classified exit reasons to wage, Medicaid, behavioral-health, homelessness-service, and HMIS records for one-year follow-up | Exit type → same linked person's housing stability, health, behavioral-health, and wage outcome | Regional scope, causal exit effect, rent burden and adequacy, alternatives, later trust/action, and durable security |
| [SHED 2024→2025 persistence](projects/us-household-financial-pressure/shed-2024-2025-panel-persistence-layer-v1.md) | Same respondent’s financial condition and reported substitutions, reduced use, borrowing, savings cuts, delayed purchases, and extra work across two waves | Financial pressure/adaptation → persistence or partial reversal | Trigger is not transaction-dated; alternatives, actor, institutional response, protected outcome, remedy, trust, action, and exit are absent |
| [SIPP utility difficulty → following-month care/security screen](projects/us-household-calendar-integration/sipp-utility-care-following-outcomes-bridge-v1.md) | Same person-pair observed in November and December 2024 reference-month records; utility difficulty and tenure at *t* are placed beside childcare-related work prevention, rent/mortgage hardship, food security, and resource-band movement at *t+1*, with Fay-BRR uncertainty | Bounded material/utility pressure → adjacent care/work and household-security surface | Utility field is not a dated bill or shutoff; childcare is an annual fall reference measure copied onto the following record; cells are sparse, no institutional response, remedy, recovery, trust, action, or exit |
| [CCES 2010→2014 job-loss panel](projects/us-cost-trust-politics/cces-panel-job-loss-political-followup-v1.md) | Same panel respondent’s earlier reported job loss/benefit cut, later insurance status, Congress judgment, contact, and local political action | Earlier work disruption → later institutional judgment/action | Separation date, employer, alternatives, trade-off, remedy, recovery, attribution change, and causal interpretation are absent |
| [HTOPS April→June fraud follow-up](projects/us-cost-trust-politics/htops-2025-fraud-followup-v1.md) | 6,564 exact SCRAMID links; retrospective exposure, reported loss, agency/law-enforcement reporting, sparse self-reported recovery, then later food, energy, work-loss, and institutional items | Exposure → realized loss/report/reported recovery → later household context | Incident date, actor, alternatives, effort, verified remedy, prior-to-later trust/action change, and switching/exit are absent; recovery cell has 11 respondents |
| [HTOPS April expense → June burden/confidence](projects/us-cost-trust-politics/data/htops-material-pressure-confidence-event-ledger-v1.json) | 6,564 exact SCRAMID links; April expense difficulty followed by June food insufficiency, energy-bill inability, household job loss, and confidence-in-Congress comparison | Material pressure → later household burden and institutional judgment | Dated bill, actor, alternatives, adaptation, remedy, prior trust, attribution, political action, recovery, and exit are absent |
| [HTOPS April expense → June option-search](projects/us-consumer-culture/findings/us-consumer-culture-004.md) | 6,564 exact SCRAMID links; April expense difficulty followed by June job, food, benefit, credit, housing, and medical search contrasts with replicate-weight uncertainty | Material pressure → later targeted option-search/navigation | Search result quality, usable alternative, application/transaction completion, institutional response, remedy, recovery, trust, and exit are absent |
| [Cash and Counseling randomized care-control](projects/us-aging-care-strain/cash-counseling-multi-currency-realization-synthesis-v1.md) | Separate beneficiary, informal-caregiver, and paid-worker follow-ups after randomized consumer-directed Medicaid assignment; service satisfaction/unmet need, caregiver wellbeing/strain, and worker compensation/experience are observed on their respective units | Implemented care-control route → short-run lived outcomes across three role surfaces | Allowance take-up/spending, completed care, one joined household, recipient health, caregiver earnings, worker retention, long-run security, trust, action, and exit are absent |
| [CFPB Ombudsman redress reissue example](projects/us-customer-automation-recourse/cfpb-ombudsman-redress-reissue-route-v1.md) | One illustrative recipient-side case: expired check → reissue request → difficulty obtaining reissue → Ombudsman-facilitated administrator route | Formal remedy access failure → recipient effort/escalation → facilitated institutional response | Final delivery, cashing, amount, adequacy, residual loss, recovery, trust, switching, and exit are absent; illustrative case is not a population estimate |
| [FWO Atkins reported receipt](projects/ai-work-control/data/fwo-atkins-truck-driver-backpay-receipt-event-ledger-v1.json) | Ten named truck drivers: underpayment → court enforcement and appeal → funds released from trust → institutionally reported back-pay receipts ranging from $8,012 to $91,566 | Formal wage remedy → reported worker-level receipt for every named worker | Independent payment confirmation, adequacy against each worker's loss, household effect, later work, trust, recurrence, and exit are absent |
| [FTC Yellowstone repeat refund](projects/us-customer-automation-recourse/data/ftc-yellowstone-refund-event-ledger-v1.json) | 3,759 small businesses received a third refund distribution after the FTC reported that each had cashed a previous check | Prior refund cashing → eligibility for a repeat consumer-financial remedy | Third-check cashing, account correction, residual loss, business survival, customer continuity, trust, switching, and exit are absent |
| [FTC ACRO repeat refund](projects/us-customer-automation-recourse/data/ftc-acro-second-refund-event-ledger-v1.json) | 5,685 people who accepted a first payment were sent a second refund check; the official route gives a 90-day cashing window but no later cashing result | First-payment acceptance → recipient-conditioned repeat consumer remedy | Second-check cashing, account/debt correction, residual loss, financial recovery, trust, switching, and exit are absent |
| [California wildfire recovery persistence](projects/us-repeat-energy-crises/data/california-la-wildfire-recovery-persistence-event-ledger-v1.json) | Continued FEMA housing support and CalAssist mortgage assistance are linked to residual-need recontact and insurance/lender timing at the program level | Disaster assistance → extended housing/financial-control route | Named household receipt, insurer/lender decision, repair completion, return/stay/move, adequacy, trust, and durable housing are absent |
| [Mudiyanselage worker-remedy episode](projects/ai-work-control/findings/ai-work-control-113.md) | One worker’s persistent underpayment and delayed wages → repeated complaints and Fair Work Ombudsman assistance → forced exit and new employment → documented $4,000 partial payment and $27,424.88 gross compensation order → refusal to return because trust broke down and emotional stress was reported | Work/payment failure → worker action → constrained exit and alternative employment → formal remedy → directly reported trust-linked refusal of return | Final compensation receipt, residual wage/superannuation loss, new-job quality and duration, household recovery, later trust, bargaining, and political action are absent; selected case is not a worker-population rate |
| [Meadley payment-without-reinstatement case](projects/ai-work-control/data/fwc-meadley-enforced-payment-no-reinstatement-event-ledger-v1.json) | Unfair dismissal → reinstatement and compensation order → employer noncompliance → worker court enforcement → officially reported compensation payment without reinstatement → additional court remedy and penalty | Failed employment remedy → worker enforcement → reported monetary receipt while original work access remains lost | Further payment receipt, replacement work, household recovery, durable trust, recurrence, and exit are absent |
| [Kaur pregnancy-linked reinstatement case](projects/ai-work-control/data/fwc-kaur-pregnancy-dismissal-reinstatement-event-ledger-v1.json) | Regular full-time casual work → pregnancy disclosure and lifting restriction → shifts/training withdrawn → two weeks of alternative work and worker challenge → reinstatement, continuity, and $14,830.40 lost-pay order | Work interruption → bounded alternative employment → worker action → quantified formal remedy | Actual reinstatement, payment receipt, later shifts, household recovery, trust, recurrence, and exit are absent |
| [DOJ IER DACA rehire and status repair](projects/ai-work-control/ier-daca-rehire-wage-seniority-record-v1.md) | One agency-reported worker case: document/status problem → termination and lower-wage rehire → worker submission → bilateral agreement → prior wage, $4,712.50 back pay, and seniority restored; complaint withdrawn | Employment-status exposure → worker action → institutional correction → wage and status remedy | Alternatives, independent payment confirmation, benefit use, durable employment, household recovery, trust, recurrence, and exit are absent; selected agency case is not a prevalence estimate |
| [FWC regular-casual dismissal case](projects/ai-work-control/data/fwc-aitken-casual-dismissal-procedural-fairness-event-ledger-v1.json) | 85 payslips establish regular weekly work; disputed service-performance complaints, neurodivergence/masking context, abrupt dismissal, self-represented response, and unfair-dismissal finding | Regular work exposure → worker evidence/action → formal merits correction | Remedy amount/form, payment or reinstatement, replacement work, earnings recovery, trust, and exit are absent |
| [FWC repeated platform-access case](projects/ai-work-control/data/fwc-khan-platform-reactivation-repeat-deactivation-event-ledger-v1.json) | First complaint → temporary block → warning/reactivation; second complaint → repeat block/deactivation; inadequate disclosure finding → reactivation/lost-pay order | Repeated access disruption → worker response → formal platform correction | Final account restoration, lost-pay amount/receipt, continued work, recurrence, switching, trust, and exit are absent |
| [FWC quantified platform-remedy case](projects/ai-work-control/data/fwc-mansoor-platform-lost-earnings-order-event-ledger-v1.json) | Long-term Uber work → complaint-linked deactivation → Baysec/Didi substitute earnings → unfairness finding → reactivation and $6,073.23 gross lost-earnings order | Platform income loss → constrained substitute work → quantified formal remedy | Payment receipt, post-order account activity, durable earnings, household recovery, trust, and exit are absent |

## Minimum usable-option promotion gate

The existing [broad event-ledger contract](../manifests/us-broad-event-ledger-schema-v1.json)
already defines the fields needed to test whether a formal route became usable.
For a route to be promoted as an end-to-end episode, the retained unit must
show, with dates and evidence status:

1. the initiating condition or decision and the actor with control;
2. alternatives before action, including non-use or inability to switch;
3. the immediate money, time, access, health, status, or control trade-off;
4. the institutional or firm response and the person's actual receipt or use;
5. a protected outcome and a sacrificed or residual-risk outcome;
6. later persistence, recurrence, continued use, switching, or exit; and
7. the person's meaning, attribution, trust, collective response, or action.

An announcement, eligibility record, complaint closure, payment order, or
aggregate population change may be a valid stage, but it cannot substitute for
the missing stages. Unknown fields remain explicitly unknown; they are not
filled by inference from a nearby aggregate or a different population.

## What this proves

The broad program has real bridges at twenty-two different points in
the chain:

1. **MEPS** supplies event-to-later-outcome timing.
2. **SHED** supplies adaptation persistence and reversal.
3. **CCES** supplies later judgment and action after a prior disruption.
4. **HTOPS** separates exposure, realized loss, reporting, self-reported recovery, and later household context for linked respondents.
5. **CFPB Ombudsman** follows a recipient-side remedy-access failure into effort, escalation, and facilitated reissuance without pretending that facilitation equals receipt.
6. **Cash and Counseling** supplies a randomized care-control bridge from an implemented consumer-directed route to beneficiary, caregiver, and paid-worker outcomes, while keeping those role-specific units separate and leaving long-run household continuity open.
7. **FWO Atkins** supplies a positive receipt comparator: the official record reports that all ten named drivers received court-released back pay, while adequacy and later security remain unobserved.
8. **FTC Yellowstone** supplies a consumer-financial receipt comparator: 3,759 businesses were eligible for a third distribution because the official record says they had cashed a prior check, while the new check and business recovery remain open.
9. **FTC ACRO** supplies a second consumer-financial comparator: 5,685 people who accepted a first payment were sent a second check, while the second-check cashing and account correction remain open.
10. **California wildfire recovery** supplies a disaster/housing bridge from continued assistance and mortgage/insurance timing to a longer recovery clock, while named-household receipt, repair, and stay/move remain open.
11. **Mudiyanselage** supplies the closest retained worker route to the lived
   chain: payment failure, complaint, forced exit, alternative work, partial
   payment, formal compensation, and directly reported broken trust. It still
   stops before final receipt and durable security.
12. **Meadley** supplies a payment-without-reinstatement bridge: enforcement
   produces a reported compensation payment and further court remedy, while
   the original job remains unrecovered. It shows why monetary receipt cannot
   be used as a proxy for restored access.
13. **Kaur** supplies a pregnancy-linked work-interruption bridge: regular work,
   a bounded alternative job, worker challenge, and a quantified reinstatement
   and lost-pay order are visible, while actual return and payment remain open.
14. **DOJ IER** supplies a compact remedy-stage case in which worker action is
   followed by restored wage and seniority, while durable employment and later
   meaning remain unobserved.
15. **FWC Aitken** supplies a regular-work and procedural-fairness bridge in a
   small-firm casual setting, while the practical remedy remains unresolved.
16. **FWC Khan** supplies a repeated platform-access bridge: one worker is
   observed through temporary block, reactivation, repeat block, adjudication,
   and a reactivation/lost-pay order, while durable access and receipt remain
   open.
17. **FWC Mansoor** supplies a quantified platform-remedy bridge: one long-term
    driver is observed through deactivation, substitute earnings, a finding of
    unfairness, reactivation, and a specific lost-earnings order, while payment,
    durable earning capacity, household recovery, trust, and exit remain open.
18. **HTOPS expense-to-burden** supplies a same-respondent material-pressure
    bridge: April expense difficulty precedes June food insufficiency,
    energy-bill inability, household job loss, and confidence-in-Congress
    comparisons, while the dated bill, alternative, remedy, recovery, and
    action remain open.
19. **HTOPS option-search** supplies a same-respondent navigation bridge:
    expense difficulty precedes targeted job, food, benefit, credit, housing,
    and medical searching, while the search result, usable alternative, and
    recovery remain open.
20. **HUD–LEHD** supplies a linked housing-assistance transition to employment
    and earnings trajectories around entry and exit, while housing conditions,
    alternatives, adequacy, exit reason, and durable security remain open.
21. **HUD HEARS** supplies a regional classified-exit bridge to same-linked-person
    housing stability, health, behavioral-health, and wage outcomes, while
    national generalization, causal effect, and later meaning/action remain open.
22. **SIPP utility/care screen** supplies a public person-month bridge that
    places utility difficulty and tenure before following-record care/work and
    household-security surfaces with replicate-weight uncertainty, while the
    annual-reference timing, sparse cells, dated institutional response, remedy,
    and durable recovery remain open.

Together they support a structured research model. They do **not** support
joining medical events, financial adaptation, and job loss into one household
or one population pathway. The missing middle is not merely “more data”; it is
specific fields: usable alternatives, event-specific institutional response,
verified remedy or recovery, and direct meaning/action after the episode.

## Cross-route cultural reading

The twenty-two bridges also reject a simple hardship-to-backlash story. MEPS shows
that later health and work movement can run in mixed directions after a dated
medical event. SHED shows that people can improve in broad financial condition
while continuing some substitutions, borrowing, or reduced use. CCES shows
that earlier job loss or insurance insecurity can coexist with different
levels of institutional approval, contact, and local political action. HTOPS
shows that exposure, realized loss, reporting, and reported recovery can be
separated from later food, energy, and work-loss conditions. In
the CFPB Ombudsman example, a formal redress route exists but is not immediately
usable: the recipient must spend effort and escalate before a reissuance route is
facilitated, and the public record still ends before receipt. In
the Cash and Counseling comparison, control over care can improve short-run
beneficiary, caregiver, or worker outcomes without showing one household's
long-run security or continuity. In
the Atkins case, reported payment reaches all ten named workers but does not
show adequacy or later security. In the Yellowstone case, prior check cashing
qualifies 3,759 businesses for another distribution without proving that the
new check arrived or corrected the underlying account harm. The ACRO case adds
a parallel recipient-conditioned route: first-payment acceptance is enough to
trigger a second check, but the public record still ends before second-check
cashing or account correction. In the California wildfire route, extended aid
and mortgage/insurance timing can prolong the
recovery clock without showing repair or stable housing. In the HUD–LEHD route,
entry and exit have different labor clocks, but the public study does not show
whether employment changes preserved housing, care, health, or dignity. HUD
HEARS supplies the missing exit-type distinction in a regional linked sample:
positive and negative exits have sharply different one-year stability and
behavioral-health profiles, but the study cannot establish that the exit caused
those differences or generalize them nationally. In the
SIPP utility/care screen, a bounded person-month ordering can put utility
difficulty before a following-record care/work and food or housing-hardship
surface, but the reference-period fields do not identify a bill, shutoff,
provider response, or care decision. Its sparse cells and non-monotonic
tenure comparisons are therefore a useful counterexample to treating one
material-pressure measure as a universal pathway. In the
DOJ IER case,
complaint withdrawal follows a reported wage and status
repair, but does not establish durable trust or security. Meadley shows that
reported compensation can coexist with failed reinstatement and further legal
enforcement. Kaur adds that a formal order can quantify lost pay and promise
continuity while still leaving actual work restoration unobserved. The FWC platform case
adds that one restoration can be followed by a second access failure, while the
FWC casual-work case shows that legal recognition can precede, rather than
complete, practical remedy. The Mansoor case adds that even a quantified order
with a payment deadline is not the same as verified receipt or durable recovery.
In plain terms: people
do not respond to pressure with one universal sequence.

They may conserve, delay, borrow, work more, stay attached to an institution,
contact it, withdraw from it, or act politically—and these choices are not
interchangeable measures of trust or resistance. The missing same-episode
fields are therefore culturally important: they would show whether a response
was experienced as necessity, dignity-preserving adaptation, resignation,
fairness, betrayal, efficacy, or collective opportunity. The current evidence
supports that as a testable proposition, not as a measured universal meaning.

## Acquisition consequence

The next high-value route must preserve a same-unit key and add at least:

- a dated or bounded trigger and responsible actor;
- the alternative, non-use, or refusal decision;
- money, time, access, or control cost;
- institutional response and remedy receipt or defined outcome follow-up;
- later persistence, trust, action, switching, or exit.

An aggregate exposure, complaint, settlement, or sentiment cross-tab does not
fill these fields. The authorized UAS/PSID/HRS routes remain the strongest
documented acquisition candidates; the retained MEPS, SHED, CCES, HTOPS, and CFPB
Ombudsman routes
remain the comparison anchors and counterexamples.

## Interpretation boundary

All listed routes are descriptive or compared designs with source-specific
weights, missingness, selection, and timing limits. A bridge status means the
specified adjacent stages are observed for the same unit; it does not mean the
upstream condition caused the downstream result.
