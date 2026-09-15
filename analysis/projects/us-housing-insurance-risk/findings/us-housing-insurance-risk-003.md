# A larger insurance backstop does not yet tell us who can stay housed

**Status:** current cross-source housing/insurance finding · **Checked:** 2026-09-14

## The bounded finding

The housing-risk atlas now sees two movements at once:

1. households report rent arrears, missing coverage, and premium pressure; and
2. California's FAIR Plan public/residual-market pool grows while place-level
   voluntary-market nonrenewal varies with income, modeled risk, and the way
   those categories are defined.

Together these establish a layered housing-security problem. They do **not**
establish that insurance withdrawal caused a particular household to move,
lose a home, delay repair, or become politically active.

The strongest safe statement is:

> A public backstop can expand while the underlying question—whether coverage
> is affordable, adequate, renewable, and usable after loss—remains unresolved.

## The four evidence surfaces

| Surface | Current observation | Unit and denominator | What it does not show |
|---|---|---|---|
| Household payment room | 23% of renters reported being behind on rent in 2025; the reported share was 21% in 2024 | Federal Reserve SHED renter population; separate annual cross-sections | Eviction, duration, payment plan, assistance, or move |
| Household coverage room | 6% of homeowners reported no homeowners insurance in 2025; the share was 12% in low/moderate-income neighborhoods | Federal Reserve SHED homeowner population; subgroup frames are separate | Policy adequacy, mortgage status, self-insurance, claim outcome, or insurer action |
| Market exposure | Treasury/FIO ZIP rows show higher broad premiums and nonrenewal exposure in some risk/income comparisons, but FEMA-bin premiums are non-monotonic | ZIP-level market rows joined to ZCTA/county context; not households or properties | Individual affordability, causal hazard pricing, replacement coverage, repair, or move |
| Public backstop | California FAIR Plan policies rose from 242,440 in September 2021 to 642,010 in September 2025; a later June 2026 headline reports 696,562 policies and about $768B exposure | Published FAIR Plan stocks with changing scope and timing | Private-market withdrawal, adequate coverage, affordability, claim success, or displacement |

The denominators are deliberately not combined. A renter's arrears, a
homeowner's insurance status, a ZIP's nonrenewal rate, and FAIR Plan policies
are different objects. Treating them as one national “housing insecurity rate”
would erase the mechanism the program is trying to learn.

## What the California cross-source comparison adds

California provides a useful place case because it contains both a visible
public backstop and a geographically joinable private-market file. The 2022
FAIR/private-market crosswalk matched 1,717 of 1,719 FAIR-share ZIP rows to
voluntary-market data. ZIPs in the highest FAIR-share quartile had a 12.40%
voluntary nonrenewal rate among the relevant renewal decisions, compared with
9.89% in the lowest quartile.

That result is a place-market association, not a household transition. FAIR
share is based on residential structures while the voluntary workbook covers a
broader policy universe. Property type, insurer mix, wildfire exposure,
regulation, prices, and reporting can all shape the ordering.

The joint income/risk screen makes the boundary even more important. Under one
pre-specified split, low-income/high-risk ZIPs had 12.72% nonrenewal versus
10.13% in high-income/low-risk ZIPs. Under a different income cut, the low-
income/low-risk cell exceeded the low-income/high-risk cell. The sensitivity
finding is therefore stronger than a simple gradient: **the apparent pattern
depends on how income and risk are operationalized.**

The public backstop and private-market screens answer different questions:

```text
FAIR growth: how much risk is entering or remaining in the residual pool?
private nonrenewal: where do observed renewal decisions differ?
household survey: who reports payment or coverage difficulty?
property/household panel: who actually loses coverage, repairs, moves, or stays?
```

Only the first three lines are currently observed.

## What the result means for the end-to-end program

The housing chain under test is:

```text
fire, storm, construction cost, reinsurance, rate, rent, mortgage, or rule
  -> premium, deductible, nonrenewal, arrears, or residual-market entry
  -> reduced maintenance, borrowing, delayed repair, underinsurance, move/stay
  -> debt, health, work, neighborhood stability, service exposure
  -> blame, trust, regulatory demand, organizing, or political response
```

The current evidence reaches the exposure and market-administration stages.
The household outcome stages remain open. In particular, an expanding FAIR
Plan may protect a property from being completely uninsured while increasing
premium, assessment, coverage-limit, or claims risk. “Covered” and “secure”
are not synonyms.

## Counterexamples that prevent overclaiming

- A renter can be behind on rent without eviction because family support,
  assistance, or a payment plan preserves the tenancy.
- An uninsured owner may have liquid resources, low perceived hazard, or a
  mortgage-free home; the survey does not identify which explanation applies.
- A high-risk ZIP can retain voluntary coverage through mitigation, regulation,
  insurer competition, or property composition.
- FAIR Plan growth can reflect property values, limits, underwriting, policy
  design, enrollment visibility, or line-of-business changes—not only private
  insurer withdrawal.
- A premium increase can be absorbed without a move; a move can occur for work,
  care, or family reasons without an insurance event.
- A policy can remain active while being inadequate after a loss, and a claim
  can be filed without showing timely repair or household recovery.

## The next decisive test

The next release should build a compatible state/property-year panel with:

1. premium, deductible, policy status, nonrenewal, and replacement coverage;
2. hazard, mitigation, claim, repair, and public-assistance records;
3. property type, mortgage status, value, and local housing supply;
4. household income, savings, debt, health, care, and work conditions; and
5. foreclosure, eviction, move/stay, service access, public comments,
   regulatory action, and political response.

The most informative counterexample would compare similar hazard and income
places where mitigation, public provision, insurance competition, or housing
supply keeps coverage usable and residence stable. Until that design exists,
the safe label is **uneven housing and insurance risk**, not a single
displacement trend.

## Reproduction and sources

- [Machine-readable cross-source record](../../../records/us-housing-insurance-payment-coverage-mobility-crosssource-2021-2026.json)
- [Federal Reserve housing and insurance layer](../federal-reserve-2025-housing-insurance-risk-layer-v1.md)
- [Treasury/FIO market layer](../treasury-fio-homeowners-insurance-market-layer-v1.md)
- [California FAIR Plan layer](../california-fair-plan-residual-market-layer-v1.md)
- [California FAIR/private-market crosswalk](../california-fair-private-market-crosswalk-layer-v1.md)
- [California sensitivity finding](us-housing-insurance-risk-002.md)
- [Federal Reserve 2025 housing report](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-housing.htm)
- [Treasury/FIO homeowners-insurance report](https://home.treasury.gov/news/press-releases/jy2791)

**Evidence status:** non-pooled household, market, modeled-place, and public-
backstop evidence; coverage adequacy, claims, repairs, mobility, health,
political attribution, and causal displacement remain unestablished.
