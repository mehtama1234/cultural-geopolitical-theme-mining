# Medical-debt relief randomized response layer v1

## Question and design

Does removing downstream medical debt repair credit access, payment behavior,
health, care use, or financial wellness?

Kluender, Mahoney, Wong, and Yin study two randomized experiments conducted
with RIP Medical Debt. Between 2018 and 2020, the experiments relieved medical
debt with a face value of $169 million for 83,401 people. The debt had been
sent, or was about to be sent, to collections. One experiment also straddled a
change in industry credit reporting, allowing the authors to distinguish relief
with and without counterfactual reporting exposure.

## Causal results

| Outcome or treatment surface | Estimated result |
|---|---:|
| Credit score when control debt was counterfactually reported | +3.4 points on average |
| Credit-limit change in that reporting subexperiment | +$340 on average |
| Credit-report outcomes when there was no counterfactual reporting | No impact detected |
| Probability of another unpaid medical bill sent to collections | +1.1 percentage points, or 6.6% of the control mean of 16.2% |
| Survey measures of mental/physical health, health-care utilization, and financial wellness | No average effects detected |

The remedy therefore has a sharply bounded result. Debt relief can improve a
credit-access surface when the debt would otherwise be reported, but it does
not automatically restore health, care use, or broad financial wellness. The
increase in unpaid bills sent to collections is consistent with lower repayment
of existing bills after relief; it does not prove intentional nonpayment or
that relief worsened health.

## End-to-end implication

This randomized layer moves the institutional-remedy arrow from correlation to
causally estimated outcomes for a selected downstream debt population:

```text
medical debt sent toward collections
  -> randomized debt relief
  -> modest credit-access improvement when reporting is active
  -> no detected average health/care/wellness repair
```

It also reinforces the project’s multi-currency rule. Credit repair, payment
behavior, health, care utilization, and financial wellness are separate
outcomes. A policy can repair one without repairing the others.

## Boundaries and counterexamples

The experiments concern downstream medical debt associated with a partner’s
collection portfolios, not all medical bills or all people who skip care. They
do not observe the original care-foregoing decision, household food/housing or
unpaid-care trade-off, provider/insurer remedy, trust, political action, or
geopolitical consequence. The average null health result does not rule out
heterogeneous effects, and the credit result depends on whether debt reporting
would otherwise occur.

## Source

[NBER Working Paper 32315: The Effects of Medical Debt Relief: Evidence from Two Randomized Experiments](https://www.nber.org/papers/w32315), also published in the [Quarterly Journal of Economics](https://academic.oup.com/qje/article/140/2/1187/7933321).
