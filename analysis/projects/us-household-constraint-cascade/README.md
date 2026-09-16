# US household constraint cascade

## Governing end-to-end objective

Determine whether housing and coverage instability jointly produce a recurring
household constraint cascade:

```text
housing / coverage / utility pressure
  -> care foregone, reduced room, or borrowing
  -> work, childcare, food, or time adaptation
  -> persistence or recovery on a later clock
  -> firm, agency, insurer, lender, or public-program response
  -> trust, legitimacy, collective action, or exit
```

The project must preserve the unit and clock of every source. It is not allowed
to turn separate population surveys into one synthetic causal estimate.

## Current bounded result

The existing evidence supports a layered cascade hypothesis:

1. Coverage transitions are associated with different care-foregoing paths and
   different 2025 financial-adaptation surfaces in the SHED recontact panel.
2. Utility-payment difficulty sits beside next-month earnings and hours movement
   in SIPP, with tenure producing a useful moderator rather than one universal
   housing mechanism.
3. Utility difficulty also sits beside an annual child-care work-prevention
   measure; the contrast is larger among owners than renters, but the small
   difficulty cells are imprecise and the clock is mixed.
4. Housing insurance pressure adds a second protection problem: ownership does
   not guarantee affordable or adequate coverage, especially for lower-income
   owners.
5. Financial adaptations persist for many SHED respondents even when broad
   financial condition improves, while some improving respondents end an
   adaptation. Recovery therefore has to be measured separately from exposure.

These observations make the cascade a strong research target. They do not show
that a utility bill caused a care decision, that coverage loss caused debt, or
that hardship caused political action.

## Evidence routes

- [Constraint-cascade cross-source bridge](constraint-cascade-cross-source-bridge-v1.md)
- [SIPP same-person constraint-cascade screen](sipp-constraint-cascade-screen-v1.md), with its [machine-readable output](../../records/us-sipp-constraint-cascade-screen-2024.json): utility, tenure, childcare prevention, work, housing, food, and resource endpoints in one adjacent-month frame.
- [SIPP cascade-screen script](../../../scripts/analyze_sipp_constraint_cascade_screen.py)
- [MEPS dated health-cost episode spine](meps-dated-event-spine-v1.md): the existing local event/payment/person-panel route that supplies dated episode context without a new bulk acquisition.
- [MEPS dated event-to-household-response screen](meps-dated-cascade-event-screen-v1.md), with its [compact output](data-meps-dated-cascade-event-screen-2024.json): inter-round event timing beside care delay, bill problems, debt, and collector contact using the valid PERWT/BRR route.
- [MEPS dated event plus institutional-friction cascade](meps-dated-friction-cascade-v1.md), with its [compact output](data-meps-dated-friction-cascade-2024.json): strict-window denial/prior-authorization comparisons against same-person care-delay, bill, debt, and collector context.
- [MEPS friction-cascade regression guard](../../../scripts/test_meps_dated_friction_cascade_guards.py): temporary synthetic test protecting timing, weight, and conditioning invariants.
- [Institutional response and remedy route](institutional-response-remedy-route-v1.md): the evidence map from household pressure through complaint/denial visibility to the still-missing verified remedy and recovery fields.
- [Medical-debt relief causal benchmark](../us-health-cost-household-choice/medical-debt-relief-randomized-response-layer-v1.md): a downstream randomized remedy result that improves selected credit access without establishing health, care, or broad household recovery.
- [Household cascade ledger contract](../../../manifests/us-household-constraint-cascade-ledger-v1.json) and [validator](../../../scripts/validate_household_constraint_cascade_ledger.py): machine-readable stage requirements plus a simulated two-episode fixture for structural testing.
- [MEPS staged-ledger audit](meps-staged-ledger-audit-v1.md): 18,457 local, keyed-hash event rows populate the observed context fields while preserving unknown choice, remedy, and recovery stages outside Git.
- [Next acquisition decision](next-acquisition-decision-v1.md): a storage-conscious UAS go/no-go sequence; no new microdata are downloaded in the current pass.
- [End-to-end status matrix](end-to-end-status-matrix-v1.md): requirement-by-requirement audit showing the current partial arrows and the missing same-case fields.
- [Same-case closure protocol](same-case-closure-protocol-v1.md): explicit promotion gates and the minimum dated episode package required to close the chain.
- [Current themes review brief](current-themes-review-brief-v1.md): a compact reading route through practical room, institutional friction, uneven remedies, and later recovery/legitimacy clocks.
- [SHED coverage-to-care machine record](../../records/us-shed-panel-coverage-care-foregoing-paths-2024-2025.json)
- [SHED coverage-to-care reproduction audit](../us-health-cost-household-choice/shed-panel-coverage-care-foregoing-reproduction-audit-2026-09-16.md)
- [SIPP utility-to-work machine record](../../records/us-sipp-utility-work-following-2024.json)
- [SIPP utility × tenure → work machine record](../../records/us-sipp-utility-work-tenure-following-2024.json)
- [SIPP utility × tenure → childcare machine record](../../records/us-sipp-utility-tenure-childcare-2024.json)
- [SHED financial persistence layer](../us-household-financial-pressure/shed-2024-2025-panel-persistence-layer-v1.md)
- [SHED homeowners-insurance pressure layer](../us-housing-insurance-affordability/shed-2025-home-insurance-pressure-layer-v1.md)

## Definition of done

The project is complete only when a dated person or household episode records:

- the housing, coverage, utility, health, or care trigger;
- the amount, obligation, coverage rule, and feasible alternatives;
- the protected need and the sacrificed, delayed, borrowed, or transferred need;
- paid work, unpaid care, childcare, food, health, housing, and debt outcomes;
- the response from the relevant firm, agency, insurer, lender, employer, or
  family member;
- a later remedy, persistence, recovery, trust, action, switching, or exit
  outcome; and
- denominator, missingness, weights, uncertainty, counterexamples, and source
  hashes sufficient for independent reproduction.

Until then, publish this project as a bridge and acquisition target, not as a
completed causal chain.
