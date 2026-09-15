# Real-wage loss and inflation are not interchangeable political signals

**Status:** full-paper-audited county-level political-economy finding · **Checked:** 2026-09-14

## The bounded finding

NBER Working Paper 35301 studies US county-level changes in family-budget
costs, nominal income, real wages, and electoral outcomes from 2021 to 2024.
Its reported design uses within-state cross-county variation in local price
changes and examines presidential and Congressional vote shares, margins, and
turnout.

The paper's central result is a useful separation: real-wage decline, rather
than higher inflation alone, is associated with Republican electoral gains,
while inflation retains an association with presidential vote shares beyond
the real-wage/economic-voting measure.

This gives the atlas a sharper material-to-political distinction. “Prices
rose” and “purchasing power fell” are related but different experiences, and
neither county association tells us exactly what an individual household
noticed, blamed, trusted, or did.

## What the full paper measures

The county estimation sample contains **3,102 counties** observed in both the
2020 and 2024 presidential elections. Local cost changes are built from the
Economic Policy Institute Family Budget Calculator for 2021 and 2024, with
food, housing, childcare, transportation, healthcare, other necessities, and
tax categories. Wage changes come from BLS Quarterly Census of Employment and
Wages data. Election returns come from the MIT Election Data and Science Lab;
controls draw on Census/ACS, USDA, and BEA data.

The category surface is much wider than the total-cost average suggests. Total
family-budget cost growth ranges from near zero to above 57% across counties;
childcare ranges from -63% to 240%, and healthcare from -19% to 115%. In the
paper's baseline category comparisons, transportation and healthcare price
growth have especially large negative associations with Republican vote-share
change. Turnout is less uniform: housing cost growth is positively associated
with turnout change while childcare cost growth is negatively associated, with
some category estimates becoming imprecise under state-cluster inference. These
are category-specific county patterns, not evidence that every household faced
the same basket or that one category caused an individual vote.

The preferred wage–price-gap specification uses state fixed effects and
controls for urbanization, population density, age, education, real GDP, and
demographic composition. Variables are standardized. The paper reports
heteroskedasticity-robust standard errors and 100-replication state-cluster
block-bootstrap standard errors.

## Preferred total-gap estimates

| Outcome change, 2020–2024 | Real-wage-growth coefficient | Inflation coefficient | County observations |
|---|---:|---:|---:|
| Republican two-party vote share | −0.0517 (robust SE 0.0208; bootstrap SE 0.0311) | −0.1205 (0.0275; 0.0386) | 3,102 |
| Republican vote margin | −0.0477 (0.0181; 0.0248) | −0.1104 (0.0248; 0.0325) | 3,102 |
| Presidential turnout | +0.0987 (0.0489; 0.0618) | +0.0703 (0.0406; 0.0516) | 3,102 |

The signs are coefficients on standardized variables, not percentage-point
effects for an ordinary household. The paper also checks Congressional
districts: the turnout sample contains 1,257 district observations, including
227 competitive districts and 1,030 safe districts. The competitive cell is
small and imprecise, so it is not treated as a general electoral estimate.

The paper's baseline and re-parameterized models answer different questions.
The baseline allows nominal wages and each price category to enter separately;
the wage–price-gap model asks whether real purchasing power and nominal price
growth retain distinct associations. A residual inflation association can be
consistent with price salience, perceived unfairness, expectations, or local
demand pressure, but the county design does not distinguish those mechanisms.

## What the source contributes

| Layer | NBER abstract-level evidence | Boundary |
|---|---|---|
| Material condition | County family-budget costs, nominal income, and real wages are separated | County measures are not a household bill, basket, or subjective worry response |
| Political outcome | Presidential and Congressional vote shares, margins, and turnout are examined | County electoral movement is not individual persuasion, vote choice, or civic action |
| Comparison | Within-state cross-county price variation is used to relate inflation and real wages to outcomes | The identifying variation remains county-level and is not an individual shock |
| Main distinction | Real-wage decline and inflation retain different reported associations in the preferred specification | Association is not a causal individual attribution or a universal economic-voting law |

## How it fits the end-to-end atlas

```text
local prices and nominal income
  -> real purchasing power and household room
  -> perceived fairness, blame, and economic judgment
  -> county electoral outcomes and turnout
  -> open individual action, institutional response, and policy feedback
```

The source directly informs the first and third surfaces and uses a design
that is stronger than a simple national time-series correlation. The middle
meaning/attribution stage remains unobserved in this record. The study also
does not tell us whether the relevant route was food, housing, transport,
energy, debt, wages, employment, local industry, partisan information, or a
combination.

## Counterexamples and safeguards

- Inflation can be associated with presidential vote shares even after the
  paper separates real-wage change, so a purchasing-power-only story is too
  narrow.
- The cost basket is not a single national experience: childcare and healthcare
  have especially wide cross-county ranges, and the category pattern for
  turnout differs from the pattern for partisan vote share.
- Real-wage decline is a county-level average; some households in a declining
  county may gain wages or have buffers, while some households in a growing
  county may lose room.
- A county vote shift can reflect turnout, migration, composition, campaign
  exposure, or collective local conditions rather than persuasion by prices.
- A price change does not identify who paid it, whether a firm absorbed it,
  or whether a household substituted, borrowed, delayed, or went without.
- The full paper is now audited through an author-hosted copy, but the paper's
  replication code and county-level analysis file have not been acquired into
  the repository.
- The EPI Family Budget Calculator measures the cost of a defined “modest but
  adequate” family living standard; it is not a CPI basket or each household's
  realized expenditure.

## What this changes in the political lane

The result strengthens the program's measurement specification: political-
economy analysis should preserve at least four distinct objects—price growth,
nominal income, real wage/purchasing power, and political outcome. It should
then add household adaptation, attribution, identity, trust, source
environment, and action rather than treating election results as a direct
readout of hardship.

This complements the ANES panel finding, where financial worry and reported
vote vary with prior party identity. The two studies should not be pooled:
NBER observes county-level economic/electoral variation, while ANES observes
respondents and identity-conditioned worry/trust/vote measures.

## Next acquisition and test

The next upgrade is to acquire replication materials or reconstruct the county
input frame, then compare the paper's category-specific cost measures with
local food, housing, energy, employment, and household-adaptation records.
Preserve the county-to-person ecological boundary. The strongest next design
would combine a dated local purchasing-power shock with repeated respondents
measuring attribution, trust, civic action, and vote or turnout separately.

## Sources and reproducibility

- [NBER Working Paper 35301](https://www.nber.org/papers/w35301)
- [Author-hosted full-paper copy used for the audit](https://ftrebbi.com/research/InflationPocketvotingUS.pdf)
- [NBER DOI 10.3386/w35301](https://doi.org/10.3386/w35301)
- [Machine-readable trend record](../../../records/us-nber-real-wages-inflation-elections-2021-2024.json)
- [Full-paper acquisition audit](../data/nber-w35301-full-paper-acquisition-audit-2026-09-14.json)
- [ANES party-conditioned finding](us-cost-trust-politics-014.md)

**Evidence status:** full-paper-audited county study with reported regression
estimates and uncertainty procedures; individual attribution, causal household
path, and political-action mechanism remain open.
