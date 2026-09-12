# SIPP Fay-BRR tenure × resource estimates v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`; replicate weights `REPWGT1`–`REPWGT240`  
**Method:** Fay BRR, `G=240`, perturbation factor `0.5`

This is a population-level distributional layer for the broad US program. It
does not turn the project into a one-household study or establish a causal path
from a bill to a later household, cultural, or political outcome.

## Results

Percentages are among nonblank selected records; parentheses are Fay-BRR
standard errors in percentage points.

| Tenure | Resource band | Unable to pay rent/mortgage | Unable to pay utility bills | Hungry but did not eat because of money |
|---|---|---:|---:|---:|
| Owned/bought | Below 1.00x | 7.02 (1.21) | 13.69 (1.64) | 30.54 (4.35) |
| Owned/bought | 1.00–1.99x | 4.87 (0.71) | 12.01 (1.40) | 24.07 (3.56) |
| Owned/bought | 2.00–3.99x | 2.88 (0.43) | 5.19 (0.56) | 15.43 (2.21) |
| Owned/bought | 4.00x or more | 1.28 (0.20) | 2.10 (0.28) | 15.65 (2.54) |
| Rented | Below 1.00x | 16.29 (1.71) | 18.11 (1.77) | 33.95 (3.15) |
| Rented | 1.00–1.99x | 12.82 (1.32) | 17.08 (1.83) | 29.97 (3.11) |
| Rented | 2.00–3.99x | 8.67 (1.08) | 11.50 (1.20) | 29.44 (2.97) |
| Rented | 4.00x or more | 4.24 (0.69) | 5.31 (0.76) | 27.15 (4.45) |
| Rent-free | Below 1.00x | 3.58 (1.89) | 11.67 (3.88) | 39.97 (11.81) |
| Rent-free | 1.00–1.99x | 3.54 (1.86) | 17.30 (5.94) | 15.14 (7.06) |
| Rent-free | 2.00–3.99x | 1.83 (1.32) | 7.92 (4.52) | 6.09 (4.85) |
| Rent-free | 4.00x or more | 1.99 (1.84) | 3.30 (2.42) | 9.40 (7.56) |

## Interpretation

This is a stratified population pattern, not a one-household story: tenure
and resources jointly organize reported housing, utility, and food pressure.
Renters show higher housing and utility-payment difficulty than owners within
each resource band in this diagnostic. The rent-free cells are imprecise.
These descriptive associations do not show that tenure or income caused the
reported condition.

This layer feeds the household-room, housing/place, unequal-exposure, and
public-systems themes. Other sources are still needed for local prices and
infrastructure, insurance and repairs, health and mobility, service recourse,
work control, interpretation, political response, firm/sector behavior, and
geopolitical consequences.

## Verification and limits

- 379,215 primary rows read; 378,291 positive-weight rows matched to
  replicates; no unmatched positive-weight rows remained.
- Missing resource bands are excluded rather than emitted as a subgroup.
- Person weights do not create a household weight; household fields repeat on
  person records.
- The nonblank denominator is not a substitute for each variable’s official
  universe and status-code rules.
- The result does not connect a person or place to a later repair, move, care
  decision, work change, trust judgment, vote, firm response, or state effect.

The earlier point-only table remains [exploratory](sipp-tenure-resource-two-way-layer-v1.md).
The program-level recovery brief is [here](../../../END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md).
