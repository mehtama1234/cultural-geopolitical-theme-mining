# Institutional response and remedy route v1

**Checked:** 2026-09-16  
**Status:** local evidence map; remedy and recovery remain unobserved  
**Scope:** household constraint, institutional route, response, remedy, and later action

## The missing arrow

The household constraint cascade is not complete when a household reaches an
institution. A complaint, denial, referral, or response label is an
institutional event. It is not yet evidence that the underlying bill, benefit,
coverage decision, account, or care problem was corrected.

```text
household pressure or disputed decision
  -> attempt / complaint / appeal
  -> receipt and routing
  -> response, denial, explanation, or relief label
  -> verified correction, payment, coverage restoration, or no remedy
  -> repeat effort, adaptation, recovery, trust, switching, or exit
```

The current local sources let us observe the middle of this chain. They do not
yet follow the same account or household through the final two arrows.

## What the existing local evidence closes

| Stage | Existing evidence | Narrow claim supported | Boundary |
|---|---|---|---|
| A household has a health-cost pressure | MEPS 2024 event files and person-panel variables | First office, ER, or inpatient event months can be linked to payment, coverage, health, employment, bill-problem, debt, and collector-contact context for the same person | The event is not necessarily the triggering bill or the household's chosen sacrifice |
| A person encounters institutional friction | MEPS `EQDENY53` layer and dated event screens | Annual denial/prior-authorization context and dated event-to-care/debt comparisons are measurable | No claim identifier, exact denial date, appeal, provider response, or resolution |
| A consumer reaches a complaint route | CFPB case-level route sample | Receipt date, CFPB-to-company send date, submission channel, narrative presence, timeliness, and company-response fields are observable | Published complainants are a selected route population; attempted-but-unsubmitted contacts are absent |
| An institution records a response | CFPB annual and case-level response layers | Explanation, non-monetary relief, monetary-relief labels, and public-response visibility can be compared by product and period | A response label is not independently verified money, correction, access restoration, or trust repair |
| A household adapts after burden | SHED, SIPP, and MEPS screens | Borrowing, reduced savings, delayed purchases, care delay, work movement/nonemployment, food insecurity, debt, and collector contact are separate endpoints | They are not linked to one dated institutional case or remedy |

Relevant local writeups are the [MEPS dated event-to-household-response
screen](meps-dated-cascade-event-screen-v1.md), the [MEPS dated episode
spine](meps-dated-event-spine-v1.md), the [CFPB public event-ledger audit](../us-customer-automation-recourse/cfpb-public-event-ledger-acquisition-audit-2026-09-14.md), the [CFPB recourse visibility and remedy layer](../us-customer-automation-recourse/cfpb-recourse-visibility-remedy-layer-v1.md), and the [CFPB case-level route sample](../us-customer-automation-recourse/cfpb-case-route-sample-2024-v1.md).

## Why “closed” is not “resolved”

The CFPB route records an institutional disposition and, in some records, a
company's public position. The local audit explicitly leaves verified
correction, money recovered, repeat effort, switching, trust, and exit
unobserved. The annual response layer similarly shows that timely response and
response category are separate dimensions. A complaint marked closed with an
explanation may represent a satisfactory resolution, an unacceptable denial,
or a consumer who stopped pursuing the matter; the public record cannot
distinguish these cases.

The same caution applies to MEPS. A denial or prior-authorization indicator
can identify institutional friction, and a later bill/debt field can identify
financial context, but without an episode-level claim key and dates we cannot
say that the denial caused the later debt or that a subsequent payment repaired
the problem.

## A bounded causal remedy benchmark

The health-cost lane already contains a randomized downstream remedy result in
the [medical-debt relief response layer](../us-health-cost-household-choice/medical-debt-relief-randomized-response-layer-v1.md).
Two experiments relieved collection-stage medical debt for 83,401 people. The
result is useful here because it tests a remedy, rather than merely recording an
institutional response:

| Remedy outcome | Bounded result | Interpretation for this cascade |
|---|---:|---|
| Credit score where the debt would otherwise be reported | +3.4 points | Relief can restore a credit-access surface when reporting exposure is active |
| Credit-limit change in that reporting subexperiment | +$340 | Access to borrowing can move separately from health or care |
| Another unpaid medical bill sent to collections | +1.1 percentage points | Payment behavior can move in a different direction from credit access |
| Mental/physical health, care utilization, financial wellness | No average effect detected | Debt relief is not evidence of automatic health, care, or broad-room recovery |

This is the strongest local causal benchmark for the remedy stage, but it does
not complete the household cascade. It begins with selected downstream debt in
collection portfolios, not a dated care need or coverage decision; it does not
measure the original care choice, food/housing/unpaid-care substitution,
provider or insurer response, trust, or political action. Its lesson is
methodological: remedy must be evaluated currency by currency, with the
counterfactual and reporting regime made explicit.

## Smallest decisive ledger

The next useful artifact is a compact, de-identified episode ledger. It should
not attempt to join unrelated survey respondents. Each row should preserve the
same case or account key across the following fields:

The executable contract is the [household cascade ledger manifest](../../../manifests/us-household-constraint-cascade-ledger-v1.json),
and its structural check is [validate_household_constraint_cascade_ledger.py](../../../scripts/validate_household_constraint_cascade_ledger.py).
The [two-episode fixture](data/household-constraint-cascade-ledger-fixture-v1.json)
is simulated test data only: it exercises a lower-room/borrowing case beside a
higher-room/payment case and deliberately leaves remedy and follow-up unknown.

The first local population of the contract is documented in the [MEPS
staged-ledger audit](meps-staged-ledger-audit-v1.md). It supplies 18,457
keyed-hash event rows from existing local files, but deliberately leaves the
same missing remedy and recovery stages open.

1. trigger type and date: bill, renewal, coverage loss, denial, shutoff threat,
   care need, repair, benefit interruption, or disputed account;
2. obligation and rule: amount owed, deductible or balance, due date, benefit
   rule, coverage decision, and feasible alternatives;
3. household response: care continued or delayed, food substitution,
   borrowing, unpaid help, work or childcare change, reduced use, move/stay,
   or repeat contact;
4. institutional route: channel, receipt date, assigned institution,
   escalation, response date, decision, and customer effort;
5. remedy verification: correction, refund, payment plan, coverage restored,
   service restored, denial upheld, partial remedy, or no remedy, with evidence
   source and date; and
6. later outcome: repeat effort, debt/collections, care continuity, work and
   housing stability, recovery or persistence, trust, switching, non-use, or
   exit.

The minimum comparison is a matched counterexample: a similar trigger and
institutional route with a different amount of liquid room, schedule control,
coverage, transportation, language access, or family support. This prevents a
successful remedy from being credited to the institution when the household
simply had enough room to absorb the problem.

## What can be done with current files

Without new acquisition, the project can use the current data to establish
benchmarks and validate the ledger schema:

- MEPS supplies dated event windows, payment bands, coverage context, and
  same-person bill/debt/care outcomes.
- SIPP supplies adjacent-month utility and tenure conditions alongside work,
  housing, food, resource, and childcare endpoints.
- SHED supplies coverage transitions, care foregoing, financial adaptation, and
  persistence/recovery context.
- CFPB supplies the institutional route contract: receipt, routing,
  timeliness, response label, narrative visibility, and public-position fields.

These are benchmark layers, not a synthetic person-level chain. A new source
is justified only if it adds the missing dated obligation, decision, verified
remedy, or later same-case outcome, and only after its acquisition size,
retention, de-identification, and cleanup plan are explicit.

## Falsification and counterexamples

The cascade should be weakened or rejected if any of the following holds in a
proper same-case design:

- households with the same trigger and comparable room do not differ in
  adaptation or recovery by institutional decision;
- verified remedies do not improve the targeted obligation, care continuity,
  debt, work, or housing outcome relative to upheld/no-remedy cases;
- repeated contact and institutional delay are unrelated to later burden once
  trigger severity and household room are controlled;
- apparent remedy effects disappear when nonusers, abandoned cases, and
  offline channels are included in the denominator; or
- trust/action changes are explained by prior institutional orientation or
  broader economic conditions rather than the episode and its resolution.

## End-to-end status

The project now has a bounded bridge from pressure to institutional visibility,
plus dated MEPS and same-person SIPP/SHED benchmark surfaces. It still does not
have a completed causal chain. The decisive remaining work is a small,
lawfully linkable, same-case episode ledger with verified remedy and later
household recovery/action outcomes.
