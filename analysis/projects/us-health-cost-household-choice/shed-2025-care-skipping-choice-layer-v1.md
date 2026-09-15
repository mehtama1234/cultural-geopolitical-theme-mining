# SHED 2025 cost-related care-skipping and medical-debt layer v1

**Checked:** 2026-09-15  
**Unit:** US adult respondent; 2025 Federal Reserve SHED published tables  
**Method:** official report percentages; reported cross-sectional comparisons, not a causal estimate

## What this closes

The MEPS event files show observed care and payment, but exclude people who
delayed or never obtained care. The 2025 SHED report supplies the missing
population-level care-choice surface: adults who went without treatment because
they could not afford it, the type of treatment skipped, differences by income
and insurance, and the prevalence of medical debt.

```text
financial constraint
  -> treatment or follow-up care forgone
  -> unresolved need, debt, or another household trade-off
  -> health, work, time, trust, and institutional consequences
```

The first arrow is reported at the population level. The later arrows remain
open because the report does not follow the same person from a bill to a later
outcome.

## Published results

| Measure | 2025 share | Population / denominator |
|---|---:|---|
| Went without any medical treatment because of cost | 26% | All adults |
| Skipped dental care because of cost | 18% | All adults; overlapping responses |
| Skipped seeing a doctor or specialist because of cost | 15% | All adults; overlapping responses |
| Skipped follow-up care because of cost | 10% | All adults; overlapping responses |
| Skipped mental-health care or counseling because of cost | 10% | All adults; overlapping responses |
| Skipped prescription medicine because of cost | 9% | All adults; overlapping responses |
| Adults with debt from their own or a family member’s medical care | 18% | All adults; debt need not be from the prior year |

Cost-related foregoing is strongly distributed by family income: 38% of adults
with income below $25,000 went without some medical care, compared with 13% of
adults with income of $100,000 or more. Insurance also changes the reported
route: 45% of uninsured adults went without treatment because they could not
afford it, compared with 24% of insured adults.

These figures establish that the care-choice stage is not merely hypothetical
or limited to people observed in utilization files. They do not say whether a
person delayed, substituted, or permanently abandoned treatment, what bill or
condition was involved, what alternative was available, or what outcome
followed.

## Relation to the MEPS and SHED panel layers

| Evidence layer | What it adds | What it cannot supply |
|---|---|---|
| MEPS event files | Observed service channel, event payment, coverage/resource context | People who never reached the observed event; event-specific bill choice |
| SHED 2025 care-skipping tables | Reported cost-related foregoing, income/insurance distribution, medical debt | Dated need, exact price, treatment result, work/time substitution, remedy |
| SHED 2024→2025 panel | Adaptation persistence and health/care direction across respondents | Whether a particular cost caused the adaptation or care decision |

Read together, the layers require a selection-aware interpretation: low
observed MEPS utilization or payment can reflect low need, coverage, completed
treatment, or care that was not obtained. SHED establishes the existence and
distribution of cost-related foregoing but not the household episode that
would connect it to debt, unpaid time, work loss, health recovery, trust, or
action.

## End-to-end status

This layer moves the following arrow from open to reported/compared:

```text
financial constraint or care cost -> care delayed, changed, or forgone
```

The next decisive join is still:

```text
dated need or bill
  -> coverage, price, alternative, and reason
  -> care received/delayed/forgone
  -> debt, time, work, food/housing, or unpaid-care trade-off
  -> health and recovery at a defined follow-up
  -> remedy, trust, switching, exit, or political action
```

## Boundaries and counterexamples

The report uses self-reported annual or prior-12-month measures and published
rounded percentages. Treatment categories overlap. Medical debt may predate
2025 and may concern the respondent or a family member. The income and
insurance comparisons are descriptive; illness severity, local access, provider
availability, plan design, transportation, and household support remain
alternative explanations. A necessary counterexample is an uninsured adult
who obtained needed care, and an insured adult who still went without because
of deductible, network, travel, waiting, or other constraints.

## Source

The official source is the Federal Reserve Board’s [Report on the Economic
Well-Being of U.S. Households in 2025—Economic Hardships](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-economic-hardships.htm),
especially the Health-Care Expenses section and Table 22. The source is a
published report layer; no SHED microdata variable is inferred here.

Related: [MEPS event-payment/bill-context layer](meps-2024-event-payment-bill-context-v1.md),
[SHED panel health/adaptation layer](../us-household-financial-pressure/shed-panel-adaptation-health-path-layer-v1.md),
and the [end-to-end status matrix](end-to-end-status-matrix-v1.md).
