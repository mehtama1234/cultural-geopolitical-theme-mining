# California insurance nonrenewal patterns are sensitive to how risk is defined

**Status:** provisional California place-risk sensitivity finding · **Checked:** 2026-09-14

## The bounded finding

The 2022 California ZIP-level screen combines voluntary-market nonrenewal
decisions, ACS income context, and modeled wildfire exposure, with FAIR Plan
share retained as a separate market-backstop dimension. Under the first
pre-specified split—income below $64,000 and CDI high/very-high exposure above
12.1%—the voluntary nonrenewal rate was:

| Income × modeled exposure cell | Nonrenewal rate | ZIP rows |
|---|---:|---:|
| Low income / high risk | 12.72% | 167 |
| Low income / low risk | 12.19% | 225 |
| High income / high risk | 10.77% | 454 |
| High income / low risk | 10.13% | 724 |

That screen suggests a modest descriptive low-income/high-risk gradient, but the
ordering is not robust to the income definition. With a $50,000 income cut and
the same exposure threshold, low-income/high-risk ZIPs had 12.03% nonrenewal
versus 13.16% in low-income/low-risk ZIPs. The sensitivity result is therefore
the stronger finding: the direction and size of the joint pattern depend on
cut points and composition.

## What is measured

- **Market decision unit:** voluntary residential insurance renewed versus
  nonrenewed decisions aggregated to ZIP rows in 2022.
- **Income unit:** ACS five-year ZCTA median-income context, approximated to ZIP
  geography.
- **Risk unit:** CDI modeled high/very-high wildfire exposure, based on a 2015
  dwelling-unit base and assigned through county context.
- **Backstop unit:** FAIR residential-structure share, separate from the
  voluntary decision denominator.

The result is an unweighted stratified screen, not a household or property
panel. The four dimensions do not have identical universes or exact geography.

## Mechanism under test

```text
income and structure mix + modeled hazard
  -> premiums, insurer decisions, and residual-market availability
  -> coverage affordability and ability to remain insured
  -> claims, repairs, move/stay, lending, and local political response
```

Only the place-market pattern is observed here. Premium burden, policy terms,
claims, repairs, household resources, and move/stay outcomes are not linked.

## Counterexamples and safeguards

- The low-income/high-risk ordering changes under a $50,000 rather than $64,000
  income cut; this weakens a universal income-risk gradient.
- High modeled risk does not mechanically produce higher nonrenewal in every
  cell; regulation, mitigation, structure mix, insurer composition, and timing
  can alter the pattern.
- FAIR Plan presence or share is not proof of affordable, adequate, renewable,
  or successfully claimable coverage.
- ZIP-to-ZCTA and ZIP-to-county assignments hide within-place variation.
- Market nonrenewal decisions do not identify a household's ability to pay,
  whether replacement coverage was found, or whether the property was sold or
  abandoned.

## Next empirical test

Pre-specify a multi-cut-point sensitivity design and then estimate a compatible
state/property-year panel with premiums, deductibles, policy status,
nonrenewal, hazards, mitigation, claims, repairs, FAIR enrollment, household
resources, and move/stay outcomes. Retain structure type, mortgage status,
county regulation, and housing supply as conditioning dimensions. A valid
counterexample is a similar hazard/income place where mitigation or market
competition preserves affordable, usable coverage.

Until those links exist, the safe interpretation is “cut-point-sensitive place
market inequality,” not a stable wildfire-causation, displacement, or
insurance-failure claim.

## Reproduction and sources

- [Joint context record](../../../records/us-california-fair-joint-context-2022.json)
- [Sensitivity record](../../../records/us-california-fair-joint-sensitivity-2022.json)
- [Joint context layer](../california-fair-joint-context-screen-v1.md)
- [Sensitivity layer](../california-fair-joint-sensitivity-layer-v1.md)
- [Treasury FIO market record](../../../records/us-treasury-fio-homeowners-insurance-market-2018-2022.json)
- [Machine-readable California wildfire county context](../../../records/us-california-doi-wildfire-county-context-2022.json)
- [Machine-readable California FAIR/ACS market context](../../../records/us-california-fair-market-acs-context-2022.json)
- [Machine-readable California FAIR/private-market crosswalk](../../../records/us-california-fair-private-market-crosswalk-2020-2023.json)
- [California residential insurance market source](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/01-res/)

**Evidence status:** unweighted ZIP-level sensitivity comparison with explicit
geography, temporal, denominator, and composition limits; household coverage,
repair, displacement, health, and political effects remain open.
