# Local capacity and immigration meaning do not move on one automatic axis

**Status:** provisional place/culture cross-source finding · **Checked:** 2026-09-14

## The bounded finding

The current place evidence separates local capacity from local meaning:

1. In a 620-county frame of places above 100,000 residents, 2020–2023
   population growth and 2023 foreign-born share are distinct axes. The highest
   growth quartile has lower health/social-assistance employment per 10,000
   residents than the lowest-growth quartile in every foreign-born-share
   quartile shown. The low-growth/high-foreign-born cell has 663.49 health/
   social-assistance employees per 10,000 residents, compared with 436.23 in
   the high-growth/high-foreign-born cell.
2. The foreign-born-share axis is not monotonic within growth groups. The
   third foreign-born quartile is often higher-capacity than the highest-share
   quartile, and sector patterns differ between health, retail, and food.
3. A separate 2026 Chicagoland survey reports support for a conditional
   citizenship pathway at 66% in Chicago, 52% in suburban Cook County, and 61%
   in Lake County. These are local respondent meaning measures, not outcomes
   derived from the county capacity screen.

The safe conclusion is that place capacity and immigration meaning must be
measured as separate but potentially interacting layers. Neither population
growth nor foreign-born share is a sufficient proxy for service access,
belonging, trust, or political action.

## What the sources measure

| Layer | Unit and denominator | What it adds | Boundary |
|---|---|---|---|
| Joint capacity screen | 620 US counties above 100,000 residents; quartile cells | CBP health/social-assistance, retail, and food establishments/employment per resident | Population growth is a mixed demographic proxy; foreign-born share is a stock; capacity is employer presence, not lived access |
| Rurality sensitivity | 593 metro and 27 nonmetro counties | Shows the pooled growth/capacity pattern is concentrated in the metro part of the thresholded frame | Nonmetro cell is small; RUCC is not access or service quality |
| Chicagoland survey | 758 Chicago, 742 suburban Cook, and 400 Lake County respondents for the citizenship item | Direct local policy meaning with reported margins of error | Cross-sectional opinion; no respondent-level join to county capacity, material exposure, or later action |

The county measures and respondent measures are not pooled. A county stock
cannot be assigned to a respondent's service experience, and a survey attitude
cannot be used as proof of a capacity bottleneck.

## Mechanism under test

```text
resident growth and population composition
  -> customers, workers, service demand, and housing pressure
  -> provider/employer capacity, travel, wait, price, and quality
  -> different exposure for new and existing residents
  -> belonging, fairness, trust, attribution, and political action
```

The current evidence reaches population/capacity context and direct local
meaning separately. It does not establish the middle lived-access link or a
causal path to attitude.

## Counterexamples and safeguards

- High foreign-born share does not uniformly correspond to low health-service
  capacity; the joint cells are non-monotonic.
- High population growth can coexist with lower per-capita provider employment,
  but the timing and mechanism are not established and growth is not migration.
- Chicago's higher reported support than suburban Cook County does not show
  that capacity differences caused the opinion gap.
- Employer presence and employment per resident do not measure appointment
  availability, language access, price, quality, travel, or unmet need.
- Support for a citizenship pathway is not support for every immigration level,
  admission rule, or local enforcement policy, and is not political action.

## Next end-to-end test

Build a matched local-place panel with a defined population/arrival window and
align county or commuting-zone measures for housing supply, rents, wages,
travel, provider capacity, language access, school/clinic workload, business
formation, and public-agency response. Then collect respondent-level local
meaning/action measures with place identifiers and exposure questions. Compare
places where demand rose while capacity expanded against places where capacity
lagged, retaining high-capacity/high-pressure and low-capacity/low-pressure
countercells.

The decisive outcome is not whether a place has more residents or a more
favorable attitude. It is whether measured exposure, alternatives, and service
experience explain differences in belonging, fairness, trust, participation,
or policy response after timing and place are aligned.

## Reproduction and sources

- [Joint growth/nativity/capacity layer](../migration-growth-nativity-joint-capacity-layer-v1.md)
- [Rurality sensitivity layer](../capacity-rurality-sensitivity-v1.md)
- [Chicagoland local meaning source record](../chicagoland-local-immigration-attitude-case-v1.md)
- [Machine-readable Chicagoland record](../../../records/us-chicagoland-immigration-belonging-action-2026.json)
- [Global Affairs Chicago immigration survey](https://globalaffairs.org/research/public-opinion-survey/chicagoland-immigration-survey)
- [American Community Survey](https://www.census.gov/programs-surveys/acs)

**Evidence status:** county capacity and local respondent-attitude layers
compared without pooling; no migration causal estimate, lived-access estimate,
belonging mechanism, or political-action effect is claimed.
