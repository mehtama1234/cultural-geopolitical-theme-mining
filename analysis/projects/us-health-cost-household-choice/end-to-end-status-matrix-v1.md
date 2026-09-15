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
| Care channel → event payment | [MEPS bounded episode surface](meps-2024-bounded-episode-surface-v1.md), [first-event ledger](meps-2024-bounded-episode-ledger-v1.md), and [payment-band screen](meps-2024-event-payment-bands-v1.md) | Observed / estimated / compared | Office, ER, and inpatient first-event records carry exact person identity, month-level timing, payment, annual health/work/bill context, and round-level cost-related delay/affordability fields; payment bands expose non-monotonic practical-room, health, and bill context | Non-users, event-specific delayed care, payment timing, or a household total | Add a bill/claim identifier and payment/obligation timing |
| Event payment → annual bill problem | [MEPS event-payment/bill-context layer](meps-2024-event-payment-bill-context-v1.md) | Compared / Taylor-estimated | Observed payment is not monotonic with annual bill-problem status; coverage and poverty conditioning change the pattern | That the displayed event caused the bill problem or was unaffordable | Link the specific event to an amount owed, balance, due date, and remedy |
| Coverage/resources → practical room | [MEPS coverage/resource conditioning](meps-2024-event-payment-bill-context-v1.md), [MEPS event payment-band/financial-room screen](meps-2024-event-payment-bands-v1.md), and [SHED adaptation layers](shed-2025-care-health-price-adaptation-layer-v1.md) | Compared / reported | Coverage, annual resources, round-level financial room, medical debt, and adaptations describe different response menus; event payment and confidence paying an unexpected expense can move in opposite directions | Liquid cash at the event, deductible exposure, alternatives, or ability to exit | Observe benefit design, cash/credit room, and alternatives in the same episode |
| Health direction → financial adaptation | [SHED panel adaptation-health layer](../us-household-financial-pressure/shed-panel-adaptation-health-path-layer-v1.md) | Longitudinal descriptive | Improved health does not automatically reverse borrowing or delayed purchases; adaptation types differ in persistence | Whether health caused adaptation or recovery, or which need was protected | Add dated health/cost trigger and adaptation timing |
| Need/payment → care delay or foregoing | [SHED 2025 care-skipping layer](shed-2025-care-skipping-choice-layer-v1.md), [care-cost/work/family-security layer](care-cost-work-family-security-layer-v1.md), [coverage-transition care-foregoing layer](shed-panel-coverage-care-foregoing-paths-v1.md), and [Oregon Medicaid lottery route](oregon-medicaid-lottery-coverage-route-v1.md) | Reported / compared; longitudinal descriptive; randomized coverage evidence | Cost-related care skipping is a measurable population route: 26% overall, 38% below $25,000 income, 13% at $100,000+, and 45% uninsured versus 24% insured; the panel shows changing coverage states have different care-foregoing paths; the Oregon lottery shows coverage can causally expand use and reduce financial exposure | Exact bill, condition, alternative, treatment outcome, or non-user counterfactual; coverage fields do not measure plan adequacy or access, and Oregon is a historical local experiment | Join reported unmet need to event, reason, coverage, benefit design, and later treatment continuity |
| Care foregoing → household adaptation | [SHED care-skipping/adaptation association](shed-2025-care-skipping-adaptation-association-v1.md); [amount-conditioned care-choice association](shed-2025-unexpected-expense-amount-care-choice-association-v1.md); [SHED panel persistence](shed-panel-care-foregoing-persistence-v1.md); [health/work path layer](shed-panel-care-foregoing-health-work-paths-v1.md) | Same-respondent reported / compared; longitudinal descriptive | Respondents reporting any care skipped also report higher medical debt, unexpected medical expense, borrowing, reduced savings, delayed purchases, work adaptation, and outside-household support; amount bands separate some care-foregoing and debt patterns without producing a monotonic choice gradient; panel entry and persistence align with higher 2025 financial adaptation and fair/poor health, while exit retains residual strain and work status moves differently | Bill identity, timing, causal direction, exact alternative, protected outcome, treatment consequence, and institutional remedy | Separate care need, bill, coverage, amount, support, and adaptation timing in a same-unit episode |
| Care → work/time/family substitution | [Care-cost/work/family-security layer](care-cost-work-family-security-layer-v1.md), [ATUS layers](../us-aging-care-strain/atus-2023-2024-published-care-work-layer-v1.md), and SIPP layers | Compared across sources | Care can be paid through unpaid time, work constraint, family labor, or money | Same-person dated substitution after the medical event | Same-family panel with care hours, schedule control, work, and resources |
| Cost/health → recovery | MEPS Panel 27 and SHED longitudinal/panel layers | Longitudinal descriptive | Health, money, care, and adaptation can recover or persist on different clocks; the SHED care-foregoing panel shows exit can coexist with residual strain, while persistence is associated with the highest 2025 adaptation surface | Recovery from a specific bill, debt, treatment, or household sacrifice | Follow balance, treatment continuity, work, health, and adaptation after an episode |
| Institutional route → remedy | [CFPB medical-collections credit-response layer](cfpb-medical-collections-credit-response-layer-v1.md), [randomized medical-debt relief RCT](medical-debt-relief-rct-outcome-separation-v1.md), [Oregon Medicaid lottery route](oregon-medicaid-lottery-coverage-route-v1.md), and [consumer recourse/public-system lanes](../us-customer-automation-recourse/README.md) | Official institutional record / randomized response evidence | Medical debt can become a credit signal; reporting changes can remove or delay some signals; randomized debt relief produces modest credit-access effects but no detected average health/care/wellness repair, while randomized coverage access reduces financial exposure and expands care use | The provider/insurer/collector response to the same health-cost episode, and whether repair reaches household health, security, trust, or exit | Preserve case ID, effort, response, correction, repeat contact, credit/housing/work effect, and exit |
| Household burden → trust/action/exit | [Health-cost institutional-legitimacy bridge](health-cost-institutional-legitimacy-bridge-v1.md), [health-cost matched finding](../../findings/us-health-cost-household-choice-matched-evidence-001.md), and [material-to-trust/action bridge](../../records/us-material-to-trust-action-bridge-2022-2025.json) | Inferred across sources / open | SHED, CFPB, and Census provide separate household-burden, institutional-response, and expense-difficulty/confidence surfaces; the bridge preserves the final conversion as a hypothesis | That a medical cost caused distrust, voting, switching, or collective action for the same person or episode | Timed panel with attribution, prior identity, institutional response, remedy effort, and later action |
| Household episode → state/geopolitical consequence | [Broad end-to-end goal](../../../END_TO_END_GOAL_V1.md) and program atlas | Open | Health and household systems can be situated within public capacity and institutional power | Any direct geopolitical effect from current health-cost evidence | Trace a policy/provider/technology dependency through realized capacity and external response |

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
