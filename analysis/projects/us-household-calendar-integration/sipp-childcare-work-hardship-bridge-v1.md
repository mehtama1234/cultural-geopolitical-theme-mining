# SIPP child-care work-prevention and following hardship bridge v1

This layer conditions the same-person November-to-December stable SNAP
comparison on whether child-care arrangements prevented the reference parent
from working or working more, then measures valid rent/mortgage and utility
hardship in the following month.

| SNAP transition | Child-care work prevention | Rent/mortgage hardship | Utility hardship |
|---|---|---:|---:|
| No SNAP → No SNAP | No | 4.94% (SE 0.56; 95% CI 3.85–6.03; n=2,224) | 7.83% (SE 0.75; 95% CI 6.36–9.30; n=2,224) |
| No SNAP → No SNAP | Yes | 7.41% (SE 3.68; 95% CI 0.19–14.62; n=71) | 16.86% (SE 4.74; 95% CI 7.57–26.15; n=71) |
| SNAP → SNAP | No | 12.01% (SE 2.11; 95% CI 7.87–16.16; n=328) | 19.43% (SE 2.38; 95% CI 14.77–24.10; n=328) |
| SNAP → SNAP | Yes | 43.65% (SE 11.18; 95% CI 21.73–65.57; n=23) | 32.39% (SE 10.72; 95% CI 11.39–53.40; n=23) |

Descriptive within-status contrasts (work-prevention minus no-work-prevention)
are +2.46 percentage points for rent/mortgage hardship and +9.03 points for
utility hardship in the stable no-SNAP comparison. In the stable-SNAP
comparison they are +31.64 and +12.96 points, respectively; the corresponding
point-estimate ratios are 3.63 and 1.67. These contrasts inherit the small
cell's wide uncertainty and are not reported as causal or independently
significant effects.

The descriptive ordering is consistent with a constrained-care / constrained-
household-room pattern: work prevention is associated with higher hardship in
both stable-status comparisons, most sharply in the small stable-SNAP cell.
The intervals are wide, and the comparison is not adjusted for household
composition, income, employment, eligibility, or care need. It is therefore a
mechanism signal, not a program-effect estimate.

The child-care variables refer to the annual fall reference period, while
hardship is measured in the following December record. This creates a useful
same-person timing bridge but not a dated care episode. Entry/exit transitions
are not included because their valid work-prevention cells are too sparse.

The [machine-readable record](../../records/us-sipp-childcare-work-hardship-bridge-2024.json)
preserves the separate outcome denominators, status flags, Fay-BRR uncertainty,
and open causal/meaning/action links. Analysis script:
`scripts/analyze_sipp_childcare_work_hardship_bridge.py`.

Source: [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
and the [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf).
