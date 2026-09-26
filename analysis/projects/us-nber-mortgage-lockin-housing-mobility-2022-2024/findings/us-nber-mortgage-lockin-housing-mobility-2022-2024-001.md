# Finding 001: Mortgage lock-in can turn a rate shock into constrained staying

## The bounded finding

NBER Working Paper 35237 studies mortgage lock-in using individual-level
mortgage data and a spatial housing-ladder model. The authors report that U.S.
existing-home sales fell 40% between 2022 and 2024 and describe a mechanism in
which borrowers with low-rate mortgages do not sell while potential buyers do
not buy elsewhere. Missing downsizers remain in larger homes, especially in
expensive areas.

The individual-mortgage analysis provides causal evidence that lock-in reduces
mobility by 25%, with moves down the housing ladder disproportionately reduced.
In the model, a temporary rate hike raises aggregate house prices 4.4% and
rents 1.5% relative to a no-lock-in counterfactual. A $10,000 starter-home
seller tax credit modestly increases mobility but raises trade-up prices; the
estimated cost per marginal move is $650,000 in the model.

The safe route is:

```text
rate change and existing low-rate mortgage
  -> lock-in and reduced sale/buy option
  -> constrained staying or altered housing-ladder move
  -> rent/price and household cost effect
  -> repair, insurance, care, work, security, and exit (open)
```

## What this adds to the atlas

This complements the flood-buyout record. Buyouts show that an official exit
can move households to different destinations; mortgage lock-in shows that a
financial condition can make staying the adaptive response. “Stayed” therefore
cannot be coded automatically as either security or failure.

## Limits and next test

- The aggregate sales decline is not a household-level causal estimate.
- The 25% mobility result is study-specific and does not reveal every
  household's desired move, alternative, or welfare.
- Modeled price, rent, and marginal-move effects are counterfactual estimates,
  not observed household bills.
- Repair, insurance, health, care, work, trust, and durable housing security
  remain unobserved.

The next decisive artifact is a protected borrower-property panel linking rate,
desired move, transaction, replacement housing, repair/insurance costs,
household needs, destination, and later security.

## Sources

- [NBER Working Paper 35237](https://www.nber.org/papers/w35237)
- [Flood-buyout relocation comparator](../../../records/us-nber-flood-buyouts-race-relocation-neighborhoods-2026.json)

**Evidence status:** individual-mortgage causal mobility evidence plus a
calibrated housing-ladder model; household repair, stay quality, and durable
security remain open.
