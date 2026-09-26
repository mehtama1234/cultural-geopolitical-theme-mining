# Finding 001: The family home association is not the same as a causal inheritance

**Status:** bounded intergenerational housing, inequality, and causal-counterexample finding · **Checked:** 2026-09-23

## The finding in plain language

The Census CES study links childhood American Housing Survey records from
1995-2002 to adult tax outcomes from 2016-2019. Children who grew up in a
parent-owned home had, on average, about $2,000 higher adult incomes and were 6
percentage points more likely to own a home later.

But the positive relationship did not survive the study’s causal tests. The
authors find that unobserved differences could drive the coefficients to zero,
and sibling fixed-effects models found no effect of years spent in an owned home
or being born into an owned home.

The practical chain is:

```text
parental resources, tenure, housing quality, and neighborhood
  -> childhood stability, networks, schooling, or selection [not separated]
  -> adult income and ownership association
  -> causal effect or family transmission [not detected in tests]
```

The simple cultural insight is that a family asset can mark advantage without
being the thing that caused the later outcome. “Homeownership helps children”
and “homeowners differ from renters” are different claims.

## What this adds to the atlas

This strengthens the atlas’s counterexample discipline. It links housing wealth,
family status, place, and adult mobility while showing why a compelling
intergenerational pattern must survive stronger comparisons. It also prevents
housing ownership from being treated as a universal cultural pathway to security.

## Limits and counterexamples

- This is a Census CES working paper, not a Census Bureau endorsement.
- The causal null is specific to the study’s linked data, measures, period, and
  identification tests.
- Sibling comparisons remove some shared family factors but not every difference
  or measurement concern.
- Adult income and ownership are not health, happiness, belonging, mobility,
  debt, or durable security.
- A null estimate for parental tenure does not mean housing quality, eviction,
  crowding, neighborhood, or family resources have no effects.

The next decisive artifact is a protected sibling-and-neighborhood panel joining
housing quality, tenure, moves, schooling, family transfers, debt, networks,
adult work and ownership, health, and later household security.

## Sources

- [Census CES working-paper page](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-54.html)
- [Full Census CES paper](https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-54.pdf)

**Evidence status:** the official paper reports positive associations but no
detected causal effect in its stronger tests; mechanisms and broader outcomes
remain open.
