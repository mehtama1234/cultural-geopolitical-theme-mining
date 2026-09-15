# Project: US housing, insurance, and the cost of staying put

## Question

When housing becomes more expensive to own or insure, who can stay, who must sell or go without protection, and who ends up carrying the risk?

## Short end-to-end goal

Trace one housing-risk change from the physical or financial cause to the household bill, then to lending, insurance, local business, public action, and political feeling.

```text
storm, fire, repair cost, rate, rent, or rule
  -> insurer, lender, landlord, builder, or household response
  -> higher cost, less coverage, denial, delay, or exit
  -> change in family security and neighborhood stability
  -> change in home value, local tax base, public aid, or political demand
  -> who owns the risk and who has a way out
```

This is one durable lane in the long-term atlas. It should be revisited as household data, market records, and public action add or weaken the place-risk pattern.

The [Federal Reserve 2025 housing and insurance risk layer](federal-reserve-2025-housing-insurance-risk-layer-v1.md)
adds current renter arrears, homeowner coverage gaps, neighborhood/income
differences, and insurance affordability pressure. It preserves the distinction
between payment stress, no coverage, and underinsurance.

The [Treasury FIO market layer](treasury-fio-homeowners-insurance-market-layer-v1.md)
adds observed ZIP-code premiums, nonrenewals, claim severity, and cancellations
for 2018–2022. It supplies the market-side condition but not household-level
affordability, coverage loss, repairs, or moves.

The [Treasury × Census ZCTA context layer](treasury-fio-census-zcta-context-layer-v1.md)
matches 98.0% of Treasury's 2022 rows to ACS income, poverty, and tenure
context. It finds a non-monotonic place pattern—higher premiums in higher-income
places but somewhat higher nonrenewal in lower-income places—without treating
place context as an individual or causal estimate.

The [Treasury × FEMA NRI hazard layer](treasury-fio-fema-nri-hazard-context-layer-v1.md)
adds county modeled expected-loss context to 99.0% of the 2022 rows. Premiums
and nonrenewals do not move monotonically across FEMA rating bins, so the layer
is a hazard-conditioned screen, not a causal dose-response estimate.

The [GAO 2019–2024 layer](gao-homeowners-insurance-2019-2024-layer-v1.md)
extends the market window through 2024 and adds estimated premiums, risk
associations, rate-filing review time, and state policy context. It shows mild
national real growth alongside sharper local risk and regulatory divergence.

The [California FAIR Plan residual-market layer](california-fair-plan-residual-market-layer-v1.md)
adds a concrete state backstop series: policies in force grew from 242,440 at
September 2021 to 642,010 at September 2025, while reported insured exposure
grew from $160.6 billion to $694.0 billion.
The [FAIR/private-market crosswalk](california-fair-private-market-crosswalk-layer-v1.md)
matches 1,717 of 1,719 2022 FAIR-share ZIP rows to California's voluntary-market
count file. ZIPs in the highest FAIR-share quartile had a 12.40% voluntary
nonrenewal rate among renewal decisions, versus 9.89% in the lowest quartile.
The [wildfire-risk county context layer](california-doi-wildfire-county-context-layer-v1.md)
then joins 56 counties to CDI's modeled high/very-high exposure share. The
highest exposure quartile had an 11.31% voluntary nonrenewal rate versus 9.98%
in the lowest quartile; this is a descriptive gradient with a 2015 exposure
base against 2022 market decisions, not an adjustment or causal test. CDI's
companion insurer workbook adds statewide 2018–2023 coverage and loss measures
by risk score, but has no county or household key and remains separate.
The [ACS context layer](california-fair-market-acs-context-layer-v1.md) matches
1,591 FAIR ZIP rows to 2022 Census ZCTA context. The lowest-income quartile
has a 12.34% voluntary nonrenewal rate versus 9.80% in the highest-income
quartile; the highest detached-home-share quartile has 11.68% versus 10.06% in
the lowest. These are place-composition screens, not adjusted household
estimates.
The [joint context screen](california-fair-joint-context-screen-v1.md) retains
1,570 ZIPs across all dimensions. Low-income/high-risk ZIPs show 12.72%
nonrenewal versus 10.13% in high-income/low-risk ZIPs, with the risk contrast
visible under that definition. The [sensitivity layer](california-fair-joint-sensitivity-layer-v1.md)
shows the ordering changes under other cut points, so this is a stratified
descriptive screen, not a stable risk gradient or causal adjustment.
The [California sensitivity finding](findings/us-housing-insurance-risk-002.md)
promotes that counterexample into the published atlas and keeps the next test
on pre-specified multi-cut-point and property-year validation.
The new [backstop and household-room finding](findings/us-housing-insurance-risk-003.md)
promotes the cross-source record into a plain-language result: household
payment pressure, market nonrenewal, modeled hazard, and FAIR Plan growth are
distinct stages, and a larger public pool does not by itself establish usable
coverage or the ability to remain housed.

## First working idea

Insurance may be turning housing from a long-term asset into a conditionally usable asset: a home can still exist, but the cost or absence of coverage can change whether a family can borrow, sell, repair, or remain. This is a working idea, not a conclusion.

## Scope

- US homeowners, renters, lenders, insurers, local governments, and builders;
- premiums, nonrenewals, coverage gaps, deductibles, mortgage requirements, rents, and repair costs;
- differences by income, race, age, place, tenure, and disaster exposure;
- household security, neighborhood change, home values, public aid, and political response.

Do not treat climate risk as the only cause. Track construction costs, reinsurance, state rules, migration, lending, litigation, and local building decisions separately.

## Required output

- a short source record;
- a claims ledger only for claims that survive the first pass;
- one plain-language finding or a clear decision to move on;
- a list of missing data and the next test.

## Writing rule

Use ordinary words. Say what happened to the bill, the coverage, the home, and the family's choices. Do not use “resilience,” “disruption,” or “market transformation” unless the record shows the exact change.
