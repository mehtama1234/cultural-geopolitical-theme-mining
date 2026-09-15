# Finding 038: Food security and children change the work-stability surface under resource pressure

**Status:** provisional SIPP conditioning extension · **Checked:** 2026-09-15

## The bounded finding

The pre-registered conditioning pass shows that the resource-to-work-direction
surface is not one universal gradient. Among people reporting a work-limiting
condition and below 1× poverty, hours were unchanged in the following month
for 84.772% of respondents without children under 18 in the household and
79.000% of those with one or more children. In the corresponding food-security
conditioning, hours were unchanged for 85.039% of the high-or-marginal-food-
security group and 70.770% of the very-low-food-security group.

The child and food contrasts are useful conditioning signals, but their valid
pair counts are 550 versus 244 and 484 versus 132 respectively. The approximate
interval for the very-low-food-security cell is 57.218%–84.322%. The result
therefore supports stratified acquisition and a counterexample to a universal
hours-stability story; it does not establish a food, child, or resource causal
effect.

Tenure is comparatively flat in this same low-resource/work-limited surface:
hours were unchanged for 84.876% of owners or buyers and 83.698% of renters,
with 406 and 348 valid pairs. SNAP recipients were lower at 81.005% versus
84.036% among nonrecipients, but this comparison is also conditional on
reported status and selected valid pairs. The higher-resource cells generally
retain high hours stability, while earnings continue to move in both
directions; stable hours are not stable security.

## Conditioning table

| Condition at month *t* | Below-1×, work-limited: hours same | Valid pairs | 4×+, work-limited: hours same | Valid pairs |
|---|---:|---:|---:|---:|
| No children under 18 | 84.772% | 550 | 92.588% | 4,176 |
| One or more children under 18 | 79.000% | 244 | 91.649% | 1,105 |
| Owner/buyer | 84.876% | 406 | 92.312% | 4,127 |
| Renter | 83.698% | 348 | 92.629% | 1,089 |
| SNAP no | 84.036% | 534 | 92.466% | 5,086 |
| SNAP yes | 81.005% | 260 | 90.483% | 195 |
| High/marginal food security | 85.039% | 484 | 92.603% | 4,757 |
| Very low food security | 70.770% | 132 | 91.617% | 276 |

The table keeps each conditioning dimension separate. It does not compare a
single pooled “pressure score,” and it does not treat all cells as equally
precise. The analysis retained separate earnings and hours universes and
reported all cells, including small or fragile comparisons.

## What this adds to the end-to-end chain

```text
resource position / reported limitation
  -> next-month earnings and hours direction
  -> child, tenure, SNAP, and food-security-conditioned option surface
  -> work stability can coexist with earnings movement and household strain
```

This sharpens the adaptation arrow: the same measured resource band can carry
different work-stability profiles depending on household composition and food
security. It still does not identify the dated price, bill, benefit change,
care event, employer decision, or institutional remedy that produced the
condition. Nor does SIPP here measure trust, meaning, political action, or
recovery after the transition.

## Counterexamples and limits

- Hours unchanged can mean stability, constrained opportunity, an undesirable
  schedule, or offsetting household labor; the measure does not distinguish
  them.
- Earnings increases and decreases coexist within every displayed resource
  and condition group; direction is not welfare.
- Tenure differences are small in the displayed low-resource work-limited
  cell, showing why the child and food contrasts should not be generalized to
  every material dimension.
- The condition fields are observed statuses, not randomized exposures; health,
  composition, job type, and unmeasured shocks can structure every comparison.

## Sources and reproduction

- [Conditioning audit](../sipp-resource-worklimitation-condition-audit-2026-09-15.json)
- [Base directional record](../../../records/us-sipp-resource-worklimitation-direction-2024.json)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP replicate-weight archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)

**Evidence status:** same-person monthly descriptive conditioning with 240
Fay-BRR replicates; not a causal, household-weighted, bill-level, care,
institutional, trust, political-action, or recovery estimate.
