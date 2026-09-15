# Child-care work prevention can coexist with following housing and utility hardship

## The bounded finding

The same SIPP person-level bridge conditions the November-to-December stable
SNAP comparison on whether child-care arrangements prevented a reference parent
from working or working more, then measures rent/mortgage and utility hardship in
the following December record.

| Status and child-care condition | Rent/mortgage hardship | Utility hardship | Valid pairs |
|---|---:|---:|---:|
| Stable no SNAP; no work prevention | 4.94% (SE 0.56) | 7.83% (SE 0.75) | 2,224 |
| Stable no SNAP; work prevention | 7.41% (SE 3.68) | 16.86% (SE 4.74) | 71 |
| Stable SNAP; no work prevention | 12.01% (SE 2.11) | 19.43% (SE 2.38) | 328 |
| Stable SNAP; work prevention | 43.65% (SE 11.18) | 32.39% (SE 10.72) | 23 |

Within the stable-SNAP comparison, the descriptive work-prevention contrast is
31.64 percentage points for rent/mortgage hardship and 12.96 points for utility
hardship. The stable no-SNAP contrasts are 2.46 and 9.03 points. The stable-SNAP
work-prevention cell is only 23 records, so its intervals are wide and it should
not be ranked as a precise effect.

## What this adds to the chain

The bridge preserves a sequence across the same identified person:

`annual child-care work constraint → following-month housing/utility hardship`

This makes the material-time connection more concrete than separate annual
averages. It shows that child-care work prevention and household bill hardship
can appear together, including among respondents with stable SNAP receipt.

The finding does not establish that care caused hardship. The child-care fields
refer to the annual fall reference period, while the hardship fields refer to
the following December record. The timing is useful but is not a dated care
episode. Household composition, employment, income, eligibility, care need, and
unmeasured resources may explain the contrast.

## Why this is not a benefit-effect result

Stable SNAP status is a conditioning state, not randomized treatment. The layer
does not observe SNAP amount or timing, notice, route effort, provider price or
availability, schedule control, employer response, exact care date, debt, food,
health, recovery, trust, or political action. Rent/mortgage and utility hardship
also have separate valid universes.

The entry and exit groups are too sparse to carry this work-prevention × hardship
comparison. Their absence is retained as a design limitation rather than treated
as zero hardship or zero effect.

## What this contributes to the end-to-end atlas

The result strengthens the middle of the program chain:

`public support / material conditions → care and schedule constraint → work capacity → housing and utility security`

It does not close the institutional or political arrows. The next test needs a
dated care/provider episode with alternatives, schedule control, benefit notice
and amount, work outcome, hardship timing, and later recovery or interpretation.

## Reproduction and sources

- [Machine-readable record](../../../records/us-sipp-childcare-work-hardship-bridge-2024.json)
- [Detailed layer](../sipp-childcare-work-hardship-bridge-v1.md)
- [Related child-care time-loss finding](us-household-calendar-integration-018.md)
- [SIPP 2025 public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP 2025 data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

The estimates use 240 Fay-BRR replicate weights with perturbation factor 0.5.
They are descriptive, retain separate denominators and uncertainty, and should
not be presented as a SNAP or child-care causal estimate.
