# Tenure and resources jointly shape household pressure, but neither is the whole story

**Status:** provisional Fay-BRR SIPP distributional finding · **Checked:** 2026-09-14

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
| Rented · below 1.00× | 16.29% (1.71) | 18.11% (1.77) | 33.95% (3.15) |
| Owned/bought · 4.00× or more | 1.28% (0.20) | 2.10% (0.28) | 15.65% (2.54) |
| Rented · 4.00× or more | 4.24% (0.69) | 5.31% (0.76) | 27.15% (4.45) |

The table is more informative than either a tenure-only or income-only
comparison because it shows that “higher resources” do not erase the exposure
associated with renting. It also shows that the three outcomes do not move as
one: the housing and utility gaps are different from the food-hardship gap.

## What the source and estimator support

- **Source and period:** 2025 SIPP public-use file, 2024 reference year.
- **Unit:** person record by reference month; household fields can repeat for
  several people in the same household and are not household-prevalence
  estimates here.
- **Weight and uncertainty:** `WPFINWGT` with `REPWGT1`–`REPWGT240`, Fay BRR,
  240 replicates, perturbation factor 0.5.
- **Denominator:** positive-weight selected records with a nonblank response
  for each outcome; this is not a replacement for each field’s full official
  universe and status-code rules.
- **Audit:** 379,215 primary rows were read; 378,291 positive-weight rows
  matched to replicate weights, with no unmatched positive-weight rows.

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
- [SIPP tenure × resource two-way layer](../sipp-tenure-resource-two-way-layer-v1.md)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP replicate-weight archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)
- [Material/time/care program route](../material-time-care-program-v1.md)

**Evidence status:** replicate-weighted descriptive distribution; no causal
tenure effect, household-level prevalence, dated bill response, health effect,
political meaning, or recovery claim is made.
