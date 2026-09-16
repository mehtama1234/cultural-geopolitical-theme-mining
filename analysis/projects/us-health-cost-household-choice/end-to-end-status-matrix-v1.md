# Health cost to household choice: end-to-end status matrix v1

**Checked:** 2026-09-15  
**Purpose:** operationalize the project’s long-form end-to-end goal without
collapsing incompatible sources into one causal estimate

## Governing chain

```text
health need or system condition
  -> exposure and coverage
  -> observed service and payment
  -> event-specific bill and feasible alternatives
  -> care continuation, delay, substitution, or foregoing
  -> money, time, work, unpaid-care, food, housing, or debt trade-off
  -> health/work/family outcome and recovery
  -> provider, insurer, employer, regulator, or legal response
  -> trust, meaning, collective action, switching, or exit
```

The matrix distinguishes what the current evidence actually measures from the
next join required to close the chain.

| Stage / arrow | Current evidence | Status | What it establishes | What it does not establish | Decisive next test |
|---|---|---|---|---|---|
| System scale → payer architecture | [CMS NHE household layer](cms-national-health-expenditure-system-household-layer-v1.md) | Observed / reported | National spending, sponsor, and payer scale | A typical household bill or welfare effect | Map a defined payer/benefit rule to a person-level episode |
| Person → health-cost exposure | [MEPS Panel 27 longitudinal layer](../us-household-calendar-integration/meps-panel27-health-cost-longitudinal-layer-v1.md) and [2024 HC-256 audit](meps-2024-reproducibility-audit-v1.md) | Longitudinal / estimated | Total and out-of-pocket expenditure, coverage, health, work, and utilization move on person-level annual clocks | A dated bill, choice, debt, or forgone-care event | Preserve a dated need/bill and full-round household context |
| Care channel → event payment | [MEPS bounded episode surface](meps-2024-bounded-episode-surface-v1.md), [first-event ledger](meps-2024-bounded-episode-ledger-v1.md), [payment-band screen](meps-2024-event-payment-bands-v1.md), [prescription episode boundary](meps-2024-prescription-episode-boundary-v1.md), and [strict inter-round payment follow-up](findings/us-health-cost-household-choice-004.md) | Observed / estimated / compared | Office, ER, inpatient, and prescription records carry exact person identity and payment fields; office, ER, and inpatient first-event records additionally carry month-level timing and annual health/work/bill context; prescription purchases add a fourth payment channel but only a restricted medication-start clock; strict inter-round payment bands show that event payment does not form a monotonic later health or bill gradient | Non-users, event-specific delayed care, complete prescription purchase timing, payment obligation timing, or a household total | Add a bill/claim identifier and payment/obligation timing; preserve prescription purchases separately from dated care episodes |
| Event payment → annual bill problem | [MEPS event-payment/bill-context layer](meps-2024-event-payment-bill-context-v1.md) | Compared / Taylor-estimated | Observed payment is not monotonic with annual bill-problem status; coverage and poverty conditioning change the pattern | That the displayed event caused the bill problem or was unaffordable | Link the specific event to an amount owed, balance, due date, and remedy |
| Coverage/resources → practical room | [MEPS coverage/resource conditioning](meps-2024-event-payment-bill-context-v1.md), [MEPS event payment-band/financial-room screen](meps-2024-event-payment-bands-v1.md), [MEPS financial-room/care-delay layer](meps-2024-financial-room-care-delay-v1.md), and [SHED adaptation layers](shed-2025-care-health-price-adaptation-layer-v1.md) | Compared / reported | Coverage, annual resources, round-level financial room, medical debt, and adaptations describe different response menus; even within private coverage and annual income categories, low confidence paying an unexpected expense aligns with much higher care delay; care delayers also report constrained hypothetical $500-bill strategies; event payment and confidence can move in opposite directions | Liquid cash at the event, deductible exposure, alternatives, or ability to exit | Observe benefit design, cash/credit room, and alternatives in the same episode |
| Health direction → financial adaptation | [SHED panel adaptation-health layer](../us-household-financial-pressure/shed-panel-adaptation-health-path-layer-v1.md) | Longitudinal descriptive | Improved health does not automatically reverse borrowing or delayed purchases; adaptation types differ in persistence | Whether health caused adaptation or recovery, or which need was protected | Add dated health/cost trigger and adaptation timing |
| Need/payment → care delay or foregoing | [SHED 2025 care-skipping layer](shed-2025-care-skipping-choice-layer-v1.md), [MEPS financial-room/care-delay layer](meps-2024-financial-room-care-delay-v1.md), [care-cost/work/family-security layer](care-cost-work-family-security-layer-v1.md), [coverage-transition care-foregoing layer](shed-panel-coverage-care-foregoing-paths-v1.md), and [Oregon Medicaid lottery route](oregon-medicaid-lottery-coverage-route-v1.md) | Reported / compared; same-respondent association; longitudinal descriptive; randomized coverage evidence | Cost-related care skipping is a measurable population route: 26% overall, 38% below $25,000 income, 13% at $100,000+, and 45% uninsured versus 24% insured; in MEPS, low financial room, medical debt, and uninsured status align with higher cost-related care delay; the panel shows changing coverage states have different care-foregoing paths; the Oregon lottery shows coverage can causally expand use and reduce financial exposure | Exact bill, condition, alternative, treatment outcome, or non-user counterfactual; MEPS round fields do not establish event timing or causality; coverage fields do not measure plan adequacy or access, and Oregon is a historical local experiment | Join reported unmet need to event, reason, coverage, benefit design, and later treatment continuity |
| Care foregoing → household adaptation | [SHED care-skipping/adaptation association](shed-2025-care-skipping-adaptation-association-v1.md); [MEPS financial-room/care-delay layer](meps-2024-financial-room-care-delay-v1.md); [MEPS care-delay/adaptation layer](meps-2024-care-delay-adaptation-v1.md); [amount-conditioned care-choice association](shed-2025-unexpected-expense-amount-care-choice-association-v1.md); [SHED panel persistence](shed-panel-care-foregoing-persistence-v1.md); [health/work path layer](shed-panel-care-foregoing-health-work-paths-v1.md) | Same-respondent reported / compared; longitudinal descriptive | Respondents reporting any care skipped also report higher medical debt, unexpected medical expense, borrowing, reduced savings, delayed purchases, work adaptation, and outside-household support; MEPS respondents reporting cost-related medical-care delay show higher debt, collections, missed payments, rent, utility difficulty, spending/savings sacrifice, work/time constraint, and family-care substitution; amount bands separate some care-foregoing and debt patterns without producing a monotonic choice gradient; panel entry and persistence align with higher 2025 financial adaptation and fair/poor health, while exit retains residual strain and work status moves differently | Bill identity, timing, causal direction, exact alternative, protected outcome, treatment consequence, and institutional remedy | Separate care need, bill, coverage, amount, support, and adaptation timing in a same-unit episode |
| Care → work/time/family substitution | [Care-cost/work/family-security layer](care-cost-work-family-security-layer-v1.md), [MEPS financial-room/care-delay work split](meps-2024-financial-room-care-delay-v1.md), [ATUS layers](../us-aging-care-strain/atus-2023-2024-published-care-work-layer-v1.md), and [SIPP tenure/work-limitation cross-lags](../us-household-calendar-integration/findings/us-household-calendar-integration-039.md) | Compared across sources; same-respondent descriptive | Care can be paid through unpaid time, work constraint, family labor, or money; within MEPS, low financial room aligns with more care delay among both employed and not-employed respondents; SIPP shows job-count and resource-band transitions differ by work limitation and tenure | Same-person dated substitution after the medical event | Same-family panel with care hours, schedule control, work, and resources |
| Cost/health → recovery | [MEPS financial-room/care-delay layer](meps-2024-financial-room-care-delay-v1.md), [month-ordered event follow-up](findings/us-health-cost-household-choice-005.md), [inter-round event transition](findings/us-health-cost-household-choice-003.md), [payment-band follow-up](findings/us-health-cost-household-choice-004.md), MEPS Panel 27, and SHED longitudinal/panel layers | Same-respondent compared; longitudinal descriptive | MEPS care-delay groups show distinct same-round health and employment surfaces; month-ordered and strictly timed acute-event groups retain baseline selection and later health/bill differences; payment bands do not identify a monotonic recovery or burden path; health, money, care, and adaptation can recover or persist on different clocks | Recovery from a specific bill, debt, treatment, or household sacrifice | Follow balance, treatment continuity, work, health, and adaptation after an episode |
| Institutional route → remedy | [MEPS denial/prior-authorization comparison](meps-2024-financial-room-care-delay-v1.md), [MEPS event-channel friction finding](findings/us-health-cost-household-choice-006.md), [MEPS round-to-round friction follow-up](findings/us-health-cost-household-choice-011.md), [MEPS care-delay/adaptation layer](meps-2024-care-delay-adaptation-v1.md), [CFPB medical-collections credit-response layer](cfpb-medical-collections-credit-response-layer-v1.md), [randomized medical-debt relief RCT](medical-debt-relief-rct-outcome-separation-v1.md), [Oregon Medicaid lottery route](oregon-medicaid-lottery-coverage-route-v1.md), and [consumer recourse/public-system lanes](../us-customer-automation-recourse/README.md) | Same-respondent compared; official institutional record; randomized response evidence | MEPS denial/prior-authorization friction aligns with more care delay, medical debt, collection contact, spending/savings sacrifice, and work constraints across office, ER, and inpatient event-family universes; the round-to-round screen retains a health-direction contrast but similar employment transitions; medical debt can become a credit signal; reporting changes can remove or delay some signals; randomized debt relief produces modest credit-access effects but no detected average health/care/wellness repair, while randomized coverage access reduces financial exposure and expands care use | The provider/insurer/collector response to the same health-cost episode, and whether repair reaches household health, security, trust, or exit | Preserve case ID, effort, response, correction, repeat contact, credit/housing/work effect, and exit |
| Household burden → trust/action/exit | [Health-cost institutional-legitimacy bridge](health-cost-institutional-legitimacy-bridge-v1.md), [ANES health-cost concern/trust/policy layer](anes-health-cost-concern-trust-policy-layer-v1.md), [CES medical-affordability participation audit](politics-personal-crisis-medical-affordability-participation-audit-v1.md), [ANES health-cost legitimacy acquisition audit](anes-health-cost-legitimacy-acquisition-audit-v1.md), [UAS health-cost and legitimacy acquisition audit](uas-health-cost-legitimacy-acquisition-audit-v1.md), [health-cost matched finding](../../findings/us-health-cost-household-choice-matched-evidence-001.md), and [material-to-trust/action bridge](../../records/us-material-to-trust-action-bridge-2022-2025.json) | Same-survey descriptive bridges plus inferred cross-source bridge; stronger episode-level endpoint remains open | ANES compares health-care payment concern with federal trust and post-election health-policy demand using repeated panel respondents, conditioned on party identity, insurance, health-condition status, and household income; CES 2018/2020 module extracts connect reported medical-expense hardship to validated turnout and six political acts, with responsibility attribution and an exploratory adjusted contact screen; the companion VOTER extract has trust variables but no matching medical-hardship exposure; UAS is the strongest registration-gated candidate for linking bounded cost/care experience, later well-being, and institution-specific trust through `uasid`; SHED, CFPB, and Census supply separate burden and institutional-response surfaces | That a medical cost caused distrust, voting, switching, or collective action for the same person or episode; existing CES, ANES, and VOTER boundaries remain, and UAS overlap, timing, weights, and exact trust/cost co-occurrence are not yet verified from microdata | Register/acquire the UAS codebooks and files, test respondent-wave overlap and timing, and promote only a documented same-person sequence; use CES, ANES, and VOTER as complementary benchmarks until then |
| Household episode → state/geopolitical consequence | [Broad end-to-end goal](../../../END_TO_END_GOAL_V1.md) and program atlas | Open | Health and household systems can be situated within public capacity and institutional power | Any direct geopolitical effect from current health-cost evidence | Trace a policy/provider/technology dependency through realized capacity and external response |

The [HRS acquisition audit](hrs-health-cost-trust-acquisition-audit-v1.md)
adds an age-50-plus parallel to the trust/action row: its 2020 documentation
contains unaffordable delayed-care and non-cost reason fields alongside
Medicare/Medicaid and insurer-trust targets. It remains an acquisition and
replication route until module overlap, timing, weights, and identifiers are
verified in the released files.

The [CFPB event-ledger health-cost bridge](cfpb-event-ledger-health-cost-bridge-v1.md)
adds an implementation-level institutional route: complaint receipt, routing,
and response can be structured as events, but the public administrative record
does not verify medical remedy, household recovery, repeat effort, switching,
or trust. It is therefore a contract for the missing middle, not a completed
health-cost result.

The [CFPB 2025 medical-debt visibility layer](cfpb-2025-medical-debt-visibility-v1.md)
adds a bounded observed category within that route: 8,861 published records
are coded `Debt collection -> Medical debt` in the 2025 aggregate snapshot.
The count is not a debt prevalence, complaint incidence, or remedy estimate.

## Current strongest findings

The consolidated [end-to-end finding](findings/us-health-cost-household-choice-end-to-end-001.md)
is the current handoff artifact for this lane. It makes the supported,
compared, randomized, inferred, and open arrows explicit without pooling
incompatible denominators.

1. **Observed care payment is not household burden.** Event payment differs by
   channel and by coverage/resource context, but the annual bill-problem field
   is not an event-specific obligation.
2. **Recovery is multidimensional.** Improved self-rated health does not
   automatically reverse borrowing or delayed purchases in the SHED panel.
3. **The missing middle is now specified.** A defensible next episode needs a
   dated bill or need, coverage and alternatives, payment obligation, care
   decision, money/time substitution, protected and sacrificed outcomes, and
   follow-up remedy or recovery.
4. **The bounded event bridge is now assembled.** The first-event ledger joins
   exact person-panel identity, event payment, month-level timing, and annual
   health/work/bill context; it still does not observe the household choice or
   adaptation that follows.
5. **Payment is not the missing household burden variable.** The strict
   inter-round payment screen preserves a pre-event health check and shows
   non-monotonic later health and bill context across event-payment bands; the
   next join must capture the full obligation, alternatives, and household
   response.

## Stopping rule for the next pass

Do not promote a new end-to-end claim unless one source or a valid matched
design supplies, at minimum:

- a defined person or household unit;
- a dated need, bill, rule, or service event;
- event-specific coverage/payment or obligation fields;
- a reported or observed care decision and feasible alternative;
- at least one money, time, work, care, health, food, housing, or debt outcome;
- a follow-up window with recovery, persistence, remedy, switching, trust, or
  action; and
- denominator, missingness, weighting, uncertainty, counterexample, and source
  retrieval evidence.

Until those conditions are met, publish the result as a layered bridge,
comparison, or acquisition gap—not as a completed causal chain.
