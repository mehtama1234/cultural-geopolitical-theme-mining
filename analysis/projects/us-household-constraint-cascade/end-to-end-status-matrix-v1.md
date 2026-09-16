# Household constraint cascade: end-to-end status matrix v1

**Checked:** 2026-09-16  
**Purpose:** completion audit for the governing household cascade; no
synthetic causal estimate

## Governing chain

```text
housing / coverage / utility pressure
  -> care foregone, reduced room, or borrowing
  -> work, childcare, food, or time adaptation
  -> persistence or recovery
  -> institutional response and verified remedy
  -> trust, legitimacy, collective action, switching, or exit
```

| Stage / arrow | Current evidence | Status | What it establishes | Decisive missing evidence |
|---|---|---|---|---|
| Pressure → reduced room | SHED coverage/insurance layers; SIPP utility/tenure layers | Observed, compared | Coverage transitions, premium difficulty, and utility-payment difficulty define distinct constraint surfaces | Dated bill/renewal, amount owed, deductible, shutoff/repair rule, and liquid room for the same episode |
| Reduced room → care choice | SHED care-foregoing panel; MEPS care-delay and denial screens | Reported, compared, longitudinal descriptive | Cost-related delay/foregoing and coverage paths coexist with debt, borrowing, reduced savings, and outside help | Same-unit reason, urgency, alternatives, treatment continuation, and event-specific obligation |
| Dated event + friction → burden context | [MEPS dated friction cascade](meps-dated-friction-cascade-v1.md) | Strict-window descriptive comparison | Denial/prior-authorization reporters show higher weighted care-delay, bill-problem, debt, and collector-contact context across office, ER, and inpatient event families | Claim-level denial date, causal direction, alternative, remedy, and recovery |
| Reduced room → work/childcare/food/time | Unified SIPP adjacent-month screen | Same-person adjacent-month comparison | Utility, tenure, childcare prevention, work movement, housing hardship, food insecurity, and resource movement can be retained in one frame | Monthly care hours, desired/involuntary work change, exact bill response, and household-level weight/choice mechanism |
| Adaptation → persistence/recovery | SHED 2024–2025 recontact panel; MEPS round context | Longitudinal descriptive | Adaptations may persist when broad financial condition improves, and some adaptations end without proving the need was repaired | Dated trigger, same adaptation, remedy date, and material recovery from that episode |
| Health event → payment/context | MEPS dated event spine and staged ledger | Observed bounded event frame | 18,457 positive-weight keyed-hash first-event rows populate event month, payment, coverage/poverty, employment, perceived health, and bill context without direct identifiers in Git | Claim/bill identity, household payer, exact obligation, care choice, and event-specific follow-up |
| Burden → institutional route | MEPS denial/prior authorization; CFPB receipt/routing/response layers | Institutional visibility, not remedy | Denial context, complaint receipt, routing lag, timeliness, response category, and public-response visibility are measurable | Same case/account effort, authority, appeal, correction, refund, coverage/service restoration, and repeat contact |
| Remedy → household recovery | Randomized medical-debt-relief benchmark | Causal but downstream and remedy-specific | Debt relief can improve selected credit access while health, care use, and broad financial wellness show no detected average repair | Remedy linked to the original household trigger, protected/sacrificed needs, work/food/housing outcomes, and heterogeneous effects |
| Recovery → trust/action/exit | ANES/CES/VOTER benchmarks; UAS acquisition route | Cross-source benchmark; open same-case arrow | Trust, attribution, policy demand, turnout, and civic actions are separately measurable | Post-episode trust/action with prior trust/identity, attribution, remedy, switching, dependence, and non-use |

## Requirement audit

The project’s definition of done requires the following fields in one dated
person/household episode. The current status is explicit:

| Required field | Current status | Authoritative evidence |
|---|---|---|
| Trigger | Partial: first observed MEPS event or survey condition, not necessarily initiating need | [MEPS staged-ledger audit](meps-staged-ledger-audit-v1.md) |
| Amount/obligation/rule | Partial: observed event self/family payment and coverage context; obligation and due date absent | [MEPS event spine](meps-dated-event-spine-v1.md) |
| Feasible alternatives | Missing | [Ledger contract](../../../manifests/us-household-constraint-cascade-ledger-v1.json) defines the field; current data mark it unknown |
| Protected/sacrificed need | Missing for same dated episode | [Institutional remedy route](institutional-response-remedy-route-v1.md) |
| Work, care, food, housing, debt | Partial: separate same-person or panel surfaces, not one episode | [Cross-source bridge](constraint-cascade-cross-source-bridge-v1.md) |
| Institutional response | Partial: denial, complaint, routing, and labels; no same-case authority or correction | [CFPB route audit](../us-customer-automation-recourse/cfpb-public-event-ledger-acquisition-audit-2026-09-14.md) |
| Remedy | Benchmark only: randomized downstream debt relief; not linked to current episodes | [Causal remedy benchmark](../us-health-cost-household-choice/medical-debt-relief-randomized-response-layer-v1.md) |
| Persistence/recovery | Partial longitudinal context; no verified episode recovery | [SHED persistence route](../us-household-financial-pressure/shed-2024-2025-panel-persistence-layer-v1.md) |
| Trust/action/switching/exit | Separate survey benchmarks and acquisition target; same-episode result missing | [Next acquisition decision](next-acquisition-decision-v1.md) |
| Denominator/weights/uncertainty/counterexample/source hashes | Present by source layer and staged-ledger contract; not yet a complete same-case package | [Ledger manifest](../../../manifests/us-household-constraint-cascade-ledger-v1.json) |

## Completion verdict

**Not complete.** The project has a reproducible layered bridge, a validated
machine-readable contract, a local privacy-minimized MEPS staging population,
and a causal downstream remedy benchmark. It does not yet have the decisive
same-case fields that connect a dated household trigger to alternatives,
protected and sacrificed needs, verified remedy, and later recovery or action.

The next legitimate promotion requires either an approved compatible panel
such as the UAS route or a consented/matched episode design that satisfies the
ledger contract. Until then, any end-to-end language must remain a hypothesis,
bridge, or acquisition boundary.
