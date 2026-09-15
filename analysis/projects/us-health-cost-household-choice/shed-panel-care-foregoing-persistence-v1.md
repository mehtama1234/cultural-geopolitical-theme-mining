# SHED 2024–2025 care-foregoing persistence and adaptation v1

## Question and boundary

Among the same recontacted respondents, does reported cost-related care
foregoing persist, exit, or newly appear between 2024 and 2025, and what is
visible in the 2025 financial and support context for each path?

This is a weighted longitudinal descriptive transition. It uses the public-use
`shedid` link and the 2025 `panel_weight`, requiring complete Yes/No answers for
all five listed care-foregoing fields in both years. It does not identify a
dated bill, diagnosis, treatment episode, or causal order.

## Results

| 2024 → 2025 care path | Paired respondents | 2025 medical debt | 2025 unexpected expense | 2025 outside help | 2025 reduced savings | 2025 borrowing | 2025 delayed purchase | 2025 insured |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| No → No | 2,976 | 7.19% | 15.20% | 3.21% | 28.73% | 7.52% | 31.96% | 95.28% |
| No → Yes (entry) | 327 | 30.37% | 34.33% | 6.46% | 59.67% | 22.75% | 62.95% | 85.74% |
| Yes → No (exit) | 444 | 19.12% | 17.77% | 7.05% | 44.50% | 20.25% | 51.99% | 85.22% |
| Yes → Yes (persistence) | 672 | 41.78% | 35.56% | 14.30% | 65.33% | 36.39% | 76.44% | 85.41% |

The persistent-foregoing group has the highest 2025 rates on every listed
financial/adaptation outcome. The entry group is also materially more exposed
than the no-foregoing group, while the exit group retains elevated debt,
savings, borrowing, and delayed-purchase shares. Exiting reported foregoing
therefore does not equal financial recovery; persistence and residual burden
can separate.

Coverage is also part of the route. The 2025 insured share is about 95% among
the no-to-no group but about 85% in each group that either entered, exited, or
persisted in care foregoing. This is descriptive composition, not an insurance
effect: coverage, illness, income, access, plan design, and recontact selection
remain entangled.

## What this moves in the end-to-end chain

This layer moves the care-choice persistence arrow from repeated annual
cross-section evidence to a same-respondent reported transition. It supports
the narrower claim that entry and persistence of care foregoing coincide with
different 2025 household adaptation surfaces, and that exit can coexist with
residual financial strain.

It does not show whether a bill caused the transition, whether care was later
obtained, which outcome was protected, or whether outside help changed the
route. The next decisive join remains a dated need/bill with amount, coverage
and alternatives, care continuity, payment timing, household trade-off, and
follow-up health or remedy outcome.

## Reproduction

```text
python3 scripts/analyze_shed_panel_care_foregoing_paths.py \
  --old /tmp/cgtm-shed/shed2024.zip \
  --new /tmp/cgtm-shed/shed2025.zip \
  --output analysis/projects/us-health-cost-household-choice/data/us-shed-panel-care-foregoing-paths-2024-2025.json
```

## Source

The panel files and weight definitions are maintained on the Federal Reserve
[SHED data page](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
The care-foregoing and adaptation variable definitions are in the [2025 SHED codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2025codebook.pdf).
