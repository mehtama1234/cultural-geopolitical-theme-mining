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
| Care channel → event payment | [MEPS bounded episode surface](meps-2024-bounded-episode-surface-v1.md) | Observed / estimated | Office, ER, inpatient, and prescription event records carry dates or bounded timing and payment fields | Non-users, delayed care, payment timing, or a household total | Add a bill/claim identifier and payment/obligation timing |
| Event payment → annual bill problem | [MEPS event-payment/bill-context layer](meps-2024-event-payment-bill-context-v1.md) | Compared / Taylor-estimated | Observed payment is not monotonic with annual bill-problem status; coverage and poverty conditioning change the pattern | That the displayed event caused the bill problem or was unaffordable | Link the specific event to an amount owed, balance, due date, and remedy |
| Coverage/resources → practical room | [MEPS coverage/resource conditioning](meps-2024-event-payment-bill-context-v1.md) and [SHED adaptation layers](shed-2025-care-health-price-adaptation-layer-v1.md) | Compared / reported | Coverage, annual resources, liquidity, and adaptations describe different response menus | Liquid cash at the event, deductible exposure, alternatives, or ability to exit | Observe benefit design, cash/credit room, and alternatives in the same episode |
| Health direction → financial adaptation | [SHED panel adaptation-health layer](../us-household-financial-pressure/shed-panel-adaptation-health-path-layer-v1.md) | Longitudinal descriptive | Improved health does not automatically reverse borrowing or delayed purchases; adaptation types differ in persistence | Whether health caused adaptation or recovery, or which need was protected | Add dated health/cost trigger and adaptation timing |
| Need/payment → care delay or foregoing | [SHED 2025 care-skipping layer](shed-2025-care-skipping-choice-layer-v1.md) and [care-cost/work/family-security layer](care-cost-work-family-security-layer-v1.md) | Reported / compared | Cost-related care skipping is a measurable population route: 26% overall, 38% below $25,000 income, 13% at $100,000+, and 45% uninsured versus 24% insured | Exact bill, condition, alternative, treatment outcome, or non-user counterfactual | Join reported unmet need to event, reason, coverage, and later treatment continuity |
| Care → work/time/family substitution | [Care-cost/work/family-security layer](care-cost-work-family-security-layer-v1.md), [ATUS layers](../us-aging-care-strain/atus-2023-2024-published-care-work-layer-v1.md), and SIPP layers | Compared across sources | Care can be paid through unpaid time, work constraint, family labor, or money | Same-person dated substitution after the medical event | Same-family panel with care hours, schedule control, work, and resources |
| Cost/health → recovery | MEPS Panel 27 and SHED 2024→2025 panels | Longitudinal descriptive | Health, money, care, and adaptation can recover or persist on different clocks | Recovery from a specific bill, debt, treatment, or household sacrifice | Follow balance, treatment continuity, work, health, and adaptation after an episode |
| Institutional route → remedy | [Consumer recourse and public-system lanes](../us-customer-automation-recourse/README.md) and related health findings | Separate institutional evidence | Complaints, policy routes, and remedies are measurable as distinct stages | The provider/insurer response to the same health-cost episode | Preserve case ID, effort, response, correction, repeat contact, and exit |
| Household burden → trust/action/exit | [Health-cost matched finding](../../findings/us-health-cost-household-choice-matched-evidence-001.md) and [material-to-trust/action bridge](../../records/us-material-to-trust-action-bridge-2022-2025.json) | Inferred across sources / open | Financial judgment, trust, action, and exit are separately observable research endpoints | That a medical cost caused distrust, voting, switching, or collective action | Timed panel with attribution, prior identity, institutional response, and later action |
| Household episode → state/geopolitical consequence | [Broad end-to-end goal](../../../END_TO_END_GOAL_V1.md) and program atlas | Open | Health and household systems can be situated within public capacity and institutional power | Any direct geopolitical effect from current health-cost evidence | Trace a policy/provider/technology dependency through realized capacity and external response |

## Current strongest findings

1. **Observed care payment is not household burden.** Event payment differs by
   channel and by coverage/resource context, but the annual bill-problem field
   is not an event-specific obligation.
2. **Recovery is multidimensional.** Improved self-rated health does not
   automatically reverse borrowing or delayed purchases in the SHED panel.
3. **The missing middle is now specified.** A defensible next episode needs a
   dated bill or need, coverage and alternatives, payment obligation, care
   decision, money/time substitution, protected and sacrificed outcomes, and
   follow-up remedy or recovery.

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
