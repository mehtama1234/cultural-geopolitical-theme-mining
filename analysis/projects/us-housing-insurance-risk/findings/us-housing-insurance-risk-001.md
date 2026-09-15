# Housing security is split between making the payment and keeping the risk covered

**Status:** provisional household/place-risk synthesis · **Checked:** 2026-09-13

## The bounded finding

Housing insecurity is not only a rent or mortgage problem. A household can be
exposed through the payment itself, through the cost or availability of
insurance, or through the gap between nominal coverage and what a later loss
requires. The Federal Reserve's 2025 household evidence and Treasury/GAO
market and regulatory evidence support a two-sided risk map, but they do not
follow the same property or household from price to claim, repair, or move.

The defensible statement is:

> Housing room depends on both the ability to keep the home and the ability to
> keep the risk of owning or renting it manageable.

This is a structured hypothesis about household and place exposure, not a
claim that insurance-market change caused a particular eviction or migration.

## Household evidence

The Federal Reserve's 2025 SHED housing module reports:

| Household surface | Published estimate | Conditioning |
|---|---:|---|
| Renters behind on rent at some point in the prior year | 23% | 33% for family income below $50,000; 5% at $100,000 or more |
| Homeowners without homeowners insurance | 6% | 12% in low/moderate-income neighborhoods; 5% in high-income neighborhoods |
| Homeowners below $50,000 without insurance | about 20% | Family-income subgroup |
| Uninsured owners saying they could not afford insurance | 43% | Conditional on being uninsured |
| Insured owners wanting more coverage but unable to afford it | 20% | Conditional on being insured |
| Insured owners struggling with premiums | 14% | About 30% among insured owners below $50,000 |

The annual comparison reports rent arrears rising from 21% in 2024 to 23% in
2025 and the reported uninsured-owner share moving from 7% to 6%. These are
separate cross-sectional surveys, not a panel of the same households. The
one-point insurance movement is not promoted as a substantive trend.

## Market and public-backstop evidence

The Treasury Federal Insurance Office market layer adds ZIP-level 2018–2022
premiums, nonrenewals, claim severity, and cancellations. The linked Census
context covers 98.0% of the intended ZCTA place rows, while the FEMA National
Risk Index join covers 99.0% of county rows. Those joins create a place-level
screen for comparing market conditions with income and modeled hazard.

The California residual-market layer adds a concrete public-backstop sequence:
FAIR Plan policies and insured exposure rise across the 2021–2026 series. The
GAO 2019–2024 review adds later national market and state-regulatory context
and identifies 35 state FAIR or beach plans as of August 2025.

These sources measure different things:

| Layer | Direct object | Boundary |
|---|---|---|
| Federal Reserve SHED | Reported household arrears, insurance status, and affordability | No policy terms, claims, repair, eviction, or move outcome |
| Treasury FIO | ZIP-level premiums, cancellations, nonrenewals, and claim metrics | No identified households, later outcome, or causal hazard effect |
| Census/FEMA context | Place income/property/hazard joins | Modeled hazard, geography/time mismatch, and no lived loss |
| FAIR/residual market | Public or residual-market policies and exposure | Enrollment is not adequate coverage, affordability, claims, or successful repair |
| GAO | Market availability and state regulatory process | Does not provide a universal household/property longitudinal panel |

The layers can be compared as context, but they cannot be pooled into a
household-level rate of “housing risk.”

## The mechanism under test

```text
rent, mortgage, premium, deductible, or nonrenewal condition
  -> cash room and coverage room change
  -> delay, borrowing, reduced maintenance, underinsurance, claim dispute,
     repair delay, move/stay, or public-backstop entry
  -> health, debt, work, neighborhood stability, and local service exposure
  -> trust, blame, political demand, or regulatory response
```

The current evidence reaches the first two lines through separate household,
market, and policy units. The later outcomes remain open.

## What the evidence does and does not imply

First, rent arrears and insurance gaps are not interchangeable. Arrears can
signal a housing-payment problem without eviction; no insurance can reflect
cost, preference, mortgage status, perceived hazard, or self-insurance without
proving insurer withdrawal.

Second, income and neighborhood gradients are not one explanation. Income,
rent, property type, mortgage status, hazard, premiums, savings, assistance,
and local market conditions can all contribute. A place with higher modeled
risk may have lower observed nonrenewal in one screen because product mix,
regulation, timing, or market composition differs.

Third, a residual-market expansion is not automatically market failure or
public success. It may preserve nominal coverage while shifting premium,
assessment, claim, or deficit risk to households, insurers, or the state. The
relevant question is whether coverage is affordable, adequate, renewable, and
usable after loss.

## Counterexamples

- A renter can fall behind without eviction because family support, assistance,
  or a payment plan protects the tenancy.
- An uninsured owner can have substantial liquid assets or low hazard exposure,
  while an insured owner can remain underinsured after a major loss.
- A high-risk place can retain voluntary coverage through regulation, public
  investment, mitigation, or insurer competition.
- A FAIR Plan can prevent an immediate coverage gap while increasing cost or
  leaving exclusions and claims risk unresolved.
- Premium pressure can rise without a move if housing supply is tight; a move
  can occur without insurance pressure because of work, care, or household
  change.

## Next empirical test

Build a state/property-year panel that links:

1. rent, mortgage, premium, deductible, policy status, and nonrenewal;
2. hazard, mitigation, claim, repair, and assistance records;
3. household income, debt, savings, health, care, and work;
4. eviction, foreclosure, move/stay, neighborhood, and service outcomes; and
5. attribution, trust, public comments, regulatory action, or local political
   response.

The key counterexample should compare similar hazard and income places where
public mitigation, insurance competition, housing supply, or assistance keeps
coverage and residence stable. Until that design exists, the atlas should call
this an uneven housing/insurance risk structure—not a single displacement
trend.

## Sources and related records

- [Federal Reserve 2025 housing report](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-housing.htm)
- [Treasury FIO homeowners insurance market report](https://home.treasury.gov/news/press-releases/jy2791)
- [GAO homeowners insurance review](https://www.gao.gov/products/gao-26-107867)
- [Machine-readable GAO premium/availability record](../../../records/us-gao-homeowners-insurance-premium-availability-2019-2024.json)
- [Federal Reserve housing/insurance record](../../../records/us-federal-reserve-housing-insurance-risk-2025.json)
- [Treasury FIO market record](../../../records/us-treasury-fio-homeowners-insurance-market-2018-2022.json)
- [Treasury/Census place context record](../../../records/us-treasury-fio-census-zcta-housing-context-2022.json)
- [Federal Reserve housing/insurance layer](../federal-reserve-2025-housing-insurance-risk-layer-v1.md)
- [GAO layer](../gao-homeowners-insurance-2019-2024-layer-v1.md)

**Evidence status:** household, market, modeled-place, and regulatory evidence
kept as separate layers; causation, coverage adequacy, repair, displacement,
health, and political response remain open.
