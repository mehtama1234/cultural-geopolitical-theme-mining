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

The [inter-round MEPS transition screen](meps-2024-between-round-event-transitions-v1.md)
uses events strictly between R3/1 and R4/2 endpoints, retaining baseline
selection differences before interpreting the R4/2 context.

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
