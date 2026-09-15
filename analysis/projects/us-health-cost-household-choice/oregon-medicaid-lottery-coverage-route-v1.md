# Oregon Medicaid lottery coverage route v1

## Question and design

What changes when an uninsured, low-income adult receives a randomized chance
to apply for Medicaid? The Oregon Health Insurance Experiment uses the 2008
lottery from a waiting list to separate coverage access from the people’s
pre-existing selection into seeking coverage.

## Causal results

| Outcome | Estimated result |
|---|---:|
| Medicaid coverage during the study period | +24.1 percentage points |
| Any outpatient visit | +21 percentage points (about 35%) |
| Any unpaid medical bill sent to collections | −6.4 percentage points (about 25%) |
| Any out-of-pocket medical expenditure | −20 percentage points (about 35%) |
| Positive depression screen after about two years | −9.15 percentage points; 95% CI −16.70 to −1.60 |
| Self-reported good-to-excellent health | Increased by about 25% relative to the control mean |

The experiment also found higher use of preventive services, prescriptions, and
hospital care, while several measured physical-health outcomes and labor-market
outcomes did not show statistically significant improvement in the reported
follow-up windows. More care use and lower financial exposure therefore do not
collapse into one outcome: coverage can protect household finances and expand
access while objective health or employment responds on a different clock.

## End-to-end implication

```text
randomized coverage opportunity
  -> Medicaid enrollment and care use
  -> lower out-of-pocket exposure, borrowing/other-bill pressure, and collections
  -> lower depression and better self-reported health
  -> no universal objective physical-health or labor-market improvement
```

This is a stronger causal coverage route than the SHED annual status contrast,
but it is not a universal estimate for current US plans or populations. It
begins with an Oregon low-income uninsured waiting-list population and does not
observe a specific bill’s care-foregoing choice, household time trade-off,
provider response, trust, or political action.

## Source

[NBER Oregon Health Insurance Experiment](https://www.nber.org/papers/w17190), [NBER results summary](https://www.nber.org/programs-projects/projects-and-centers/oregon-health-insurance-experiment/oregon-health-insurance-experiment-results), and [clinical-outcomes publication](https://doi.org/10.1056/NEJMsa1212321).
