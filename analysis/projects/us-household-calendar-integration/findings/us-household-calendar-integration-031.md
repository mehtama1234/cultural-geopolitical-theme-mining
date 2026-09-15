# Tenure and resources jointly shape household pressure, but neither is the whole story

**Status:** official-universe Fay-BRR SIPP distributional finding · **Checked:** 2026-09-15

## The bounded finding

The 2025 Census SIPP public-use file, covering the 2024 reference year, shows
that housing tenure and monthly income-to-poverty position jointly organize
reported housing, utility, and food pressure. In the selected person-record
universes, renters report more difficulty paying rent or mortgage and more
utility-payment difficulty than owners within every displayed resource band.
The pattern is strongest below the poverty line, but it remains visible among
renters at four times the poverty line or more.

| Tenure × monthly resource band | Rent/mortgage difficulty | Utility-payment difficulty | Hungry but did not eat because of money |
|---|---:|---:|---:|
| Owned/bought · below 1.00× | 7.02% (SE 1.21) | 13.69% (1.64) | 30.54% (4.35) |
| Rented · below 1.00× | 16.30% (1.70) | 18.06% (1.77) | 34.00% (3.15) |
| Owned/bought · 4.00× or more | 1.28% (0.20) | 2.10% (0.28) | 15.65% (2.54) |
| Rented · 4.00× or more | 4.20% (0.69) | 5.31% (0.76) | 26.86% (4.41) |

The table is more informative than either a tenure-only or income-only
comparison because it shows that “higher resources” do not erase the exposure
associated with renting. It also shows that the three outcomes do not move as
one: the housing and utility gaps are different from the food-hardship gap.

## Care and work extension

The same official-universe Fay-BRR run adds a bounded care/work layer. The
percentages below are separate field-specific estimates, not a combined care
burden measure.

| Tenure × monthly resource band | Paid child care | Child-care payment assistance | Care prevented work/more | Time lost from work |
|---|---:|---:|---:|---:|
| Owned/bought · below 1.00× | 19.02% (SE 4.01), n=1,002 | 7.60%, n=1,002 | 3.85%, n=1,405 | 13.75%, n=32 |
| Rented · below 1.00× | 23.85% (3.85), n=1,568 | 13.47%, n=1,568 | 6.80%, n=2,218 | 20.73%, n=138 |
| Owned/bought · 4.00× or more | 38.41% (1.93), n=8,945 | 3.86%, n=8,945 | 3.10%, n=10,878 | 24.90%, n=334 |
| Rented · 4.00× or more | 43.47% (5.18), n=1,342 | 5.44%, n=1,342 | 4.45%, n=1,733 | 0.00%, n=56 |

Renters have higher point estimates for paid care, assistance, and work
prevention at both displayed resource endpoints. The time-loss cells are too
sparse for a stable tenure interpretation, especially the high-resource
renter cell; the zero estimate is not evidence of no time loss. These fields
refer to the SIPP fall/reference-parent care universe and do not measure a
dated monthly care episode, price, provider choice, or employer response.

## What the source and estimator support

- **Source and period:** 2025 SIPP public-use file, 2024 reference year.
- **Unit:** person record by reference month; household fields can repeat for
  several people in the same household and are not household-prevalence
  estimates here.
- **Weight and uncertainty:** `WPFINWGT` with `REPWGT1`–`REPWGT240`, Fay BRR,
  240 replicates, perturbation factor 0.5.
- **Denominator:** positive-weight selected records within each outcome’s
  documented official universe and status-code rules.
- **Audit:** 379,215 primary rows were read; 378,291 positive-weight rows
  matched to replicate weights, with no unmatched positive-weight rows.

The 2026-09-15 rerun applies the official status flags and field-specific
universes to the three displayed outcomes. The renter cells update slightly
from the earlier nonblank-denominator layer: below 1.00×, rent/mortgage
difficulty is 16.30%, utility difficulty 18.06%, and hunger 34.00%; at 4.00×
or more, the corresponding values are 4.20%, 5.31%, and 26.86%.

## Why it matters for the end-to-end program

```text
resources and tenure
  -> exposure to rent, utilities, and food trade-offs
  -> payment difficulty or going without
  -> repair, mobility, health, work, care, and household adaptation
  -> trust, political interpretation, institutional response, or exit
```

This result closes only the distributional middle of that chain. It gives the
program a sharper exposure surface for the next test: a renter and an owner at
the same resource position may face different fixed costs, payment schedules,
repair obligations, insurance exposure, or alternatives. But the SIPP table
does not identify which of those mechanisms produced the difference.

The result also prevents an overly simple “income is the pressure” story. A
resource band is not a complete measure of room when tenure, local prices,
family support, debt, health, transportation, and housing quality differ. At
the same time, tenure is not a pure cause: people select into or are sorted
across housing arrangements, and ownership can carry mortgage, repair,
insurance, and energy costs that this table does not capture.

## Counterexamples and boundaries

- High-resource renters still report more food hardship than high-resource
  owners in this selected comparison; the pattern is not only a low-income
  phenomenon.
- Rent-free households do not form a simple secure category. Their arrangement
  may involve family dependence, crowding, informal exchange, or unmeasured
  housing quality; several cells are imprecise.
- A reported inability to pay does not reveal the bill amount, due date,
  arrears, shutoff, eviction threat, repair, or later recovery.
- “Hungry but did not eat because of money” is not the same universe or outcome
  as rent or utility difficulty; the percentages must not be combined into a
  burden index without a field-level universe audit.
- Person weighting represents people living in the tenure/resource cell, not
  independent households. It cannot establish how many households were
  affected or how burden was distributed within a household.

## Next test

The next material/time/care pass should hold resource position and broad place
comparable while adding housing payment, utility amount, insurance, repair,
vehicle access, health, care, work hours, and mobility fields. The strongest
design would follow the same household through a dated bill or housing event
and record whether the response was payment, borrowing, assistance, moving,
care substitution, work change, or going without. A later trust or political
measure should be treated as a separate endpoint with attribution and timing,
not inferred from hardship alone.

## Reproduction and related records

- [Fay-BRR tenure × resource estimates](../sipp-fay-brr-tenure-resource-estimates-v1.md)
- [Official-universe reproduction audit](../sipp-tenure-resource-official-reproduction-audit-2026-09-15.json)
- [Official-universe care/work reproduction audit](../sipp-tenure-resource-care-official-reproduction-audit-2026-09-15.json)
- [SIPP tenure × resource two-way layer](../sipp-tenure-resource-two-way-layer-v1.md)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP replicate-weight archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)
- [Material/time/care program route](../material-time-care-program-v1.md)

**Evidence status:** replicate-weighted descriptive distribution; no causal
tenure effect, household-level prevalence, dated bill response, health effect,
political meaning, or recovery claim is made.
