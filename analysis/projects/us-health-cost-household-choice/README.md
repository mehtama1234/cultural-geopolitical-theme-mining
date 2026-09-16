# Project: US health costs and the choices people give up

## Question

When medical care costs more than a family can pay, what do people stop doing first—and how does that private choice affect work, debt, trust, and public policy?

## Short end-to-end goal

Follow a health cost from the bill or coverage rule to the care a person delays, then to the household's work and money choices, and finally to the response of providers, insurers, regulators, and voters.

```text
price, bill, coverage, or payment rule
  -> care is delayed, changed, or refused
  -> debt, missed work, worse health, or family strain
  -> trust and political pressure
  -> provider, insurer, regulator, or court response
  -> who carries the cost and who can avoid it
```

This is one durable lane in the long-term atlas. Its next sources should progressively connect reported choices to later household and institutional outcomes.

## Matched evidence pass

- [A medical cost can change care, work, and debt in different ways](../../findings/us-health-cost-household-choice-matched-evidence-001.md)
- [Reader-friendly HTML](../../../site/us-health-cost-household-choice-matched-evidence-001.html)

## Population depth

The [end-to-end status matrix](end-to-end-status-matrix-v1.md) is the current
control surface for this lane. It maps each stage from system scale and
observed payment through care choice, household substitution, recovery,
institutional remedy, and trust/action, while naming the evidence and the next
required join.

The [SHED 2025 care-skipping and medical-debt layer](shed-2025-care-skipping-choice-layer-v1.md)
adds the reported population-level care-choice stage that observed MEPS event
files cannot see: going without treatment because of cost, the types of care
skipped, income and insurance differences, and medical debt.

The [SHED care-skipping/adaptation association](shed-2025-care-skipping-adaptation-association-v1.md)
now joins those care decisions to same-respondent medical debt, unexpected
medical expenses, emergency funds, borrowing, savings, consumption, purchase,
and work adaptations. It is a weighted cross-sectional bridge, not a dated
bill or causal outcome.

The associated [coverage-conditioned layer](shed-2025-care-skipping-adaptation-association-v1.md)
tests insured and uninsured routes within the same respondent architecture.
It preserves the counterexample that coverage lowers reported care foregoing
overall but does not eliminate medical debt among people who still skip care.
The same layer now records outside-household help for medical expenses, debt,
or health insurance as a possible support route; it does not show transfer
size, timing, conditions, or whether help prevented foregoing or resolved debt.

The [unexpected-expense amount and care-choice association](shed-2025-unexpected-expense-amount-care-choice-association-v1.md)
then conditions that bridge on reported expense amount. It shows that smaller
expense bands can coincide with more care foregoing, while the largest band
has the highest medical-debt share; amount alone does not identify the route.

The [SHED panel care-foregoing persistence layer](shed-panel-care-foregoing-persistence-v1.md)
links the same respondents across 2024 and 2025. Entry and persistence of
reported care foregoing coincide with higher 2025 debt and adaptation, while
exit still carries residual financial strain; this is longitudinal description,
not proof of recovery or causation.

The companion [health/work path layer](shed-panel-care-foregoing-health-work-paths-v1.md)
shows that persistent foregoing also aligns with a higher fair/poor-health
surface, while employment status moves differently and cannot serve as a single
burden proxy.

The [CFPB medical-collections credit-response layer](cfpb-medical-collections-credit-response-layer-v1.md)
extends the chain into institutional visibility and remedy. It records how
medical debt becomes a credit signal, how reporting changes remove or delay
some signals, and how the 2025 federal rule was vacated; credit visibility is
not the same as bill resolution or restored care.

The [health-cost institutional-legitimacy bridge](health-cost-institutional-legitimacy-bridge-v1.md)
places those household and institutional surfaces beside a Census
expense-difficulty/confidence contrast. It labels the final legitimacy arrow
as inferred across sources and open, because no source yet follows one health
bill through remedy to a later trust or political-action judgment.

The [coverage-transition care-foregoing layer](shed-panel-coverage-care-foregoing-paths-v1.md)
tests the institutional alternative itself. Stable insured respondents have the
largest no-foregoing share, while persistent uninsured respondents have the
largest persistence share; the small transition cells remain descriptive.

The [randomized medical-debt relief layer](medical-debt-relief-randomized-response-layer-v1.md)
tests whether downstream debt relief repairs the next outcomes. It finds
modest credit-access effects in the reporting subexperiment, but no detected
average health, care-utilization, or financial-wellness effects, keeping credit
repair separate from health and household recovery.

The companion [RCT outcome-separation layer](medical-debt-relief-rct-outcome-separation-v1.md)
preserves the causal estimates and repayment counter-result directly from the
study rather than treating “relief” as one undifferentiated success measure.

The [Oregon Medicaid lottery coverage route](oregon-medicaid-lottery-coverage-route-v1.md)
provides the coverage-side causal counterexample: randomized access reduced
financial exposure and expanded care use, while depression, self-reported
health, objective physical health, and labor outcomes moved on different
scales.

The consolidated [end-to-end finding](findings/us-health-cost-household-choice-end-to-end-001.md)
now carries the evidence chain from care cost and coverage through care choice,
household adaptation, institutional response, remedy, and the still-open
legitimacy endpoint. It is deliberately a layered synthesis rather than a
single causal estimate.

The [MEPS legitimacy-endpoint audit](meps-2024-legitimacy-endpoint-audit-v1.md)
records the structural boundary: HC-256 contains burden, adaptation, and
institutional-friction fields but no trust, attribution, complaint, switching,
vote, or organizing endpoint. The legitimacy arrow therefore remains an
explicit acquisition target.

The [ANES health-cost legitimacy acquisition audit](anes-health-cost-legitimacy-acquisition-audit-v1.md)
narrows that target. ANES supplies repeated political endpoints plus health
insurance status and concern about paying health-care expenses, but it does
not supply a dated bill, care decision, remedy effort, or episode attribution.
It is therefore a promising concern-to-judgment layer, not yet a completed
MEPS/SHED-to-legitimacy join.

The [ANES health-cost concern, trust, and policy-demand layer](anes-health-cost-concern-trust-policy-layer-v1.md)
now executes the first two SDA tests. Health-care payment concern is compared
with federal-government trust and with post-election demand for government help
paying health-insurance costs. These are same-survey descriptive results, not
evidence that a medical bill caused distrust or political action.

The [CES medical-affordability participation audit](politics-personal-crisis-medical-affordability-participation-audit-v1.md)
adds a direct same-respondent action surface. Public 2018 and 2020 crisis
module extracts connect trouble affording medical expenses to validated turnout,
contact, protest, campaign work, signs, meetings, and donations, and include
responsibility attribution. The cross-year screen points more consistently to
targeted official contact than to universal disengagement, but the module
extracts do not provide a dated bill, remedy, or reproduced design-based
medical-specific uncertainty. It is therefore an action benchmark and
acquisition bridge, not a completed health-cost-to-legitimacy effect.

The same audit now records a negative companion-file result: the public
`VOTER_2019vv_crisis.tab` extract contains trust and institutional-confidence
variables but no medical-expense hardship field that can be matched to the CES
exposure. Trust context therefore remains a cross-source layer, not a
same-respondent medical-hardship-to-trust estimate.

The [reader-facing CES finding](../../findings/us-medical-affordability-political-action-matched-evidence-001.md)
promotes that benchmark into the connected atlas. It preserves the adjusted
contact screen, the 2018/2020 attribution-format difference, and the missing
bill-to-remedy-to-legitimacy join.

The [UAS health-cost and legitimacy acquisition audit](uas-health-cost-legitimacy-acquisition-audit-v1.md)
identifies the strongest next route: USC's registration-gated UAS links
health-cost and unmet-care modules, monthly health/financial events, and
institution-specific trust or satisfaction through `uasid`. It is a verified
acquisition design, not yet a result; overlap, timing, weights, and missingness
must be established after access.

The [HRS health-cost and institutional-trust acquisition audit](hrs-health-cost-trust-acquisition-audit-v1.md)
defines a parallel older-adult route. HRS 2020 documents unaffordable delayed
care, non-cost delay reasons, health-care cost satisfaction, and trust in
Medicare/Medicaid and insurance companies. Its module sampling, age-50-plus
universe, timing, identifiers, and weights must be verified before promotion;
it is a replication/counterexample route, not a substitute for the UAS join.

Party identity, insurance status, health-condition status, and household
income are now included as conditioning tests. They show that trust levels
and gradients vary by prior identity and health/coverage composition; annual
income and the high-end cells do not substitute for liquid room or a bill.

The [MEPS event payment-band screen](meps-2024-event-payment-bands-v1.md)
adds a payment-stratified counterexample: self/family payment and later
bill/health/work context do not form a monotonic burden scale within the first
office, emergency-room, or inpatient event universes.

The [health-cost episode acquisition protocol](health-cost-episode-acquisition-protocol-v1.md)
turns the remaining same-unit gap into an executable design: dated exposure,
alternatives, care choice, obligation, protected and sacrificed outcomes,
institutional remedy, and later trust/action with explicit promotion and
failure rules.

The [CFPB event-ledger health-cost bridge](cfpb-event-ledger-health-cost-bridge-v1.md)
maps the public complaint ledger onto that protocol. It demonstrates a usable
receipt-to-response event contract while keeping verified medical remedy,
household recovery, repeat effort, switching, and trust as unobserved fields.

The [MEPS financial-room/care-delay layer](meps-2024-financial-room-care-delay-v1.md)
adds a same-respondent comparison between confidence paying an unexpected
expense or medical debt and cost-related delay or inability to afford care and
prescriptions. It is a stronger practical-room association, but not a dated
bill-level causal result.

The [MEPS event-channel institutional-friction comparison](meps-2024-event-institutional-friction-v1.md)
stratifies the denial/prior-authorization association across first dated
office, emergency-room, and inpatient event people. The pattern persists in
each channel, including within the privately covered stratum. The uninsured
friction cells are small, and annual denial timing and claim-level remedy
remain open.

The [MEPS care-delay/adaptation layer](meps-2024-care-delay-adaptation-v1.md)
adds ESAQ payment strategies, sacrificed spending and savings, work/leave
constraints, and family-care substitution to the care-delay pathway. It is the
strongest current same-respondent money/time/work bridge, while its cross-round
ordering remains explicitly open.

The [2025 care, health, and price-adaptation layer](shed-2025-care-health-price-adaptation-layer-v1.md)
is now paired with a [2024 comparison layer](shed-2024-care-health-adaptation-layer-v1.md).
Both are cross-sectional weighted descriptions; they test directional
stability across releases without treating the samples as a panel.

The [care and work distribution layer](shed-care-work-distribution-layer-v1.md)
adds employment status to the 2024 care comparison, showing how unpaid care
and work position combine into different adaptation menus.

The [care and age distribution layer](shed-care-age-distribution-layer-v1.md)
adds life-stage structure, showing that the care pattern is distributed across
younger, midlife, and older respondents rather than being one age-neutral mean.

The [care-cost, time, work, and family-security cross-source finding](../../findings/us-care-cost-time-work-currency-cross-source-001.md)
now places the MEPS longitudinal layer beside the SIPP child-care/work
constraint layer and the SHED unpaid-care adaptation layer. It treats money,
time, work capacity, and family security as separate currencies and keeps the
same-event household pathway open rather than pooling non-comparable samples.

The [MEPS 2024 reproducibility audit](meps-2024-reproducibility-audit-v1.md)
re-acquires the official HC-256 and HC-036BRR archives, reproduces the
headline person-level estimates, and records the remaining event-linkage gap.

The [MEPS 2024 event-linkage audit](meps-2024-event-linkage-audit-v1.md)
confirms exact person/event keys across four files and identifies the
prescription timing limitation that must remain visible in any episode result.

The [bounded MEPS episode surface](meps-2024-bounded-episode-surface-v1.md)
now joins dated office, emergency-room, and inpatient events to annual
coverage, resource, work, health, and bill-problem context in an aggregate-only
record.

The [first-event MEPS ledger](meps-2024-bounded-episode-ledger-v1.md) now
combines one first dated event per person/event family with weighted
self/family payment and month-level baseline/follow-up context. It closes the
identity/payment/context bridge while preserving the missing care-choice and
household-adaptation fields.

The [MEPS round-timing audit](meps-2024-round-timing-audit-v1.md) tests the
available R3/1, R4/2, R5/3, and full-year reference boundaries and keeps them
as temporal context rather than incorrectly calling them event follow-up.

The [MEPS event-context association](meps-2024-event-context-association-v1.md)
adds weighted same-person comparisons of event presence with medical-bill
problems, health, and employment while retaining the non-causal boundary.

The [coverage-conditioned MEPS comparison](meps-2024-event-context-by-coverage-v1.md)
tests whether the acute-event pattern persists within private, public-only,
and uninsured under-65 groups, retaining small-cell and selection limits.

The [month-ordered MEPS follow-up screen](meps-2024-month-ordered-event-followup-v1.md)
uses each person’s first event month relative to the R4/2 endpoint and reports
the resulting health, employment, and bill-problem associations as bounded
temporal context.

The [month-ordered MEPS finding](findings/us-health-cost-household-choice-005.md)
promotes that screen into the reader-facing atlas while retaining the office-
visit counterexample, same-month ambiguity, and selection boundary.

The [inter-round MEPS transition screen](meps-2024-between-round-event-transitions-v1.md)
uses events strictly between R3/1 and R4/2 endpoints, retaining baseline
selection differences before interpreting the R4/2 context.

The [strict inter-round event transition finding](findings/us-health-cost-household-choice-003.md)
promotes that timing screen into the atlas: acute-event groups were already
different before the event, so later health and bill contrasts remain selected
descriptive context rather than event effects.

The [strict inter-round payment-band follow-up](findings/us-health-cost-household-choice-004.md)
conditions that window on event-level family payment. It shows why a recorded
payment cannot stand in for the household obligation: zero-payment acute events
can have worse health context, while higher-payment ER events can have more
reported bill problems. This remains a selected descriptive transition, not a
causal affordability or recovery estimate.

The [MEPS event-payment and bill-context layer](meps-2024-event-payment-bill-context-v1.md)
conditions event-level payments on the linked person's annual bill-problem
report. It demonstrates why observed payment is not interchangeable with
household burden or affordability.

## First working idea

Health costs may act like a quiet income cut: people can protect the bill today by giving up care, savings, work time, or another household need. The burden may be hard to see because the choice happens inside the family before it appears in spending or employment data. This is a working idea, not a conclusion.

## Scope

- US households, patients, workers, providers, insurers, employers, and public programs;
- out-of-pocket spending, medical debt, skipped care, coverage, billing, and credit records;
- differences by income, race, age, disability, family type, insurance status, and place;
- firm and public responses only where they can be tied to household experience.

Do not treat total national health spending as the same thing as what a family can afford. Do not treat having insurance as proof that care is affordable.

## Writing rule

Use everyday words. Say what care was missed, what bill was paid, what work or saving changed, and who had a choice. Avoid broad claims about “the health care system” unless the record shows the exact actor and action.
