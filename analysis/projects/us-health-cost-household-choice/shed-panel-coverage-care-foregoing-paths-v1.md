# SHED coverage transitions and care-foregoing paths v1

## Question and boundary

Does care-foregoing persistence or entry differ when the same recontacted
respondent remains insured, loses coverage, gains coverage, or remains
uninsured between 2024 and 2025?

This is a weighted descriptive panel cross-tab. Insurance status is defined as
any Yes among the six listed coverage fields in each year, and care foregoing
as any Yes among the five listed E1 fields. It does not identify plan
generosity, network access, a dated bill, or an insurance change caused by a
particular health event.

## Results

| 2024 → 2025 coverage path | Pairs | No→No care | No→Yes entry | Yes→No exit | Yes→Yes persistence | 2025 debt | 2025 fair/poor health |
|---|---:|---:|---:|---:|---:|---:|---:|
| Insured → insured | 3,964 | 69.12% | 6.74% | 9.61% | 14.53% | 15.12% | 16.13% |
| Insured → uninsured | 158 | 41.18% | 13.01% | 26.28% | 19.53% | 18.13% | 20.93% |
| Uninsured → insured | 115 | 48.40% | 17.22% | 11.89% | 22.50% | 20.16% | 19.02% |
| Uninsured → uninsured | 182 | 36.36% | 13.76% | 12.53% | 37.35% | 22.57% | 20.69% |

Stable insurance is associated with the largest no-foregoing share and the
lowest persistent-foregoing share in this selected panel universe. Remaining
uninsured is associated with the highest persistence share. Coverage loss and
gain both have smaller cells and elevated entry or persistence relative to the
insured-to-insured path.

This is evidence that “insured” is not a complete or fixed protection state.
Coverage transitions may mark employment, age, income, eligibility, family,
or health changes, and the coverage fields do not measure deductibles,
networks, prior authorization, provider supply, or affordability. The pattern
therefore supports a route distinction, not an insurance effect estimate.

## End-to-end implication

Coverage belongs between exposure and feasible alternatives. A valid episode
design must retain coverage at the time of the need, benefit design, network
and access constraints, amount owed, care decision, household adaptation, and
later health or remedy outcome. Annual coverage transition alone cannot tell
which part of the route changed.

## Reproduction

```text
python3 scripts/analyze_shed_panel_care_foregoing_paths.py \
  --old /tmp/cgtm-shed/shed2024.zip \
  --new /tmp/cgtm-shed/shed2025.zip \
  --output analysis/projects/us-health-cost-household-choice/data/us-shed-panel-care-foregoing-paths-2024-2025.json
```

## Source

The panel files are maintained on the Federal Reserve [SHED data page](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
Variable definitions are documented in the [2025 SHED codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2025codebook.pdf).
