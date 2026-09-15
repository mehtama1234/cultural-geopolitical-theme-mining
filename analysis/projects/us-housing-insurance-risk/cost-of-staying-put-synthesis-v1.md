# The cost of staying put is more than the monthly payment

**Status:** reader-facing housing, insurance, hazard, and energy synthesis  
**Checked:** 2026-09-15  
**Scope:** US renters, homeowners, climate-risk places, energy-burdened
households, coverage, mobility, and public backstops

## The short answer

Housing security is often described as affordability: can the household pay
the rent or mortgage? The current evidence shows a wider system:

```text
housing payment + energy need + hazard exposure
        ↓
insurance price, coverage gap, nonrenewal, repair, and assistance
        ↓
cash, credit, time, health, work, and care trade-offs
        ↓
stay, move, defer repair, borrow, reduce use, or seek a public backstop
        ↓
place attachment, trust, political demand, and market response
```

The atlas can measure several first- and middle-stage surfaces, but it cannot
yet show one household's complete move-or-stay episode. The central finding is
therefore **housing security has payment, coverage, hazard, and energy layers
that can reinforce one another without being interchangeable.**

## Four pressures that look like one problem from the outside

| Pressure | Current measure | What it tells us | What remains open |
|---|---|---|---|
| Payment | Federal Reserve 2025 housing module | 23% of renters were behind on rent in the prior year; about 33% below $50k | Exact arrears episode, eviction, borrowing, and recovery |
| Coverage | Federal Reserve 2025 homeowner module | 6% reported no homeowners insurance; 20% below $50k | Coverage adequacy, claims, lender response, and repair |
| Hazard/market | Treasury/FIO matched ZIP and FEMA context | Higher-risk places have higher premiums and nonrenewal exposure | Causal hazard pricing, insurer withdrawal, and household mobility |
| Energy | 2020 RECS household estimates | Energy-burden proxy is much higher in lower income bands | Dated bill shock, safe temperature, health, care, and work substitution |

The denominators differ: renters, homeowners, ZIP rows, FEMA-matched places,
and RECS households are not one sample. A combined narrative is useful only if
the units remain visible.

## 1. Payment pressure is uneven before insurance enters

The Federal Reserve's 2025 household housing module reports that **23% of
renters** were behind on rent during the prior year, up from 21% in 2024. The
reported share was approximately 33% among renters with household income below
$50,000 and 5% among those with income of at least $100,000.

This is a reported annual experience, not an eviction rate. It does not show
whether the household borrowed, received help, moved, negotiated, lost
utilities, or recovered. The income gradient establishes unequal exposure; it
does not identify the exact rent, local supply, household composition, or
payment event.

For homeowners, **6%** reported having no homeowners insurance in 2025, down
from 7% in 2024. The uninsured share was approximately 20% among homeowners
with income below $50,000 and 12% among homeowners in low- or moderate-income
neighborhoods. Among uninsured homeowners, 43% said they could not afford the
coverage. Among insured homeowners below $50,000, 30% reported struggling to
afford premiums.

That creates two distinct risks: failing to make the housing payment and
remaining in the home without a financial shock absorber. Insurance absence is
not the same as a claim, loss, or underinsurance, but it changes what the next
event can do.

See the [Federal Reserve housing and insurance record](../../records/us-federal-reserve-housing-insurance-risk-2025.json).

## 2. Hazard exposure can become a price and availability problem

The Treasury/FIO 2022 market-place screen matches **25,084 ZIP rows** to usable
Census ZCTA context, a 98.0% match among considered rows. In the matched rows,
mean premium was $1,630 for places below $50,000 in median household income and
$2,332 for places at or above $100,000. Mean nonrenewal was 1.261% versus
0.909%, respectively, in the unweighted row comparison.

The FEMA-hazard screen assigns **25,330 ZIP rows** to a FEMA National Risk
Index county. Mean premium was $1,564.92 in relatively low expected-loss
places, $2,449.06 in relatively high places, and $1,927.57 in very-high places
under the displayed unweighted classification. Mean nonrenewal was 0.959% in
relatively low places and 1.271% in very-high places.

The non-monotonic very-high premium result is a reminder that hazard ratings,
property mix, insurance markets, geography, regulation, and data coverage all
matter. The pattern is a place-level association, not proof that FEMA risk
caused a household's premium or that an insurer withdrew because of one
property's hazard.

The practical implication is nonetheless important: a household can face a
payment problem and a coverage problem at the same time. The market may price
the risk before the household has a realistic ability to move, repair, or
replace coverage.

See the [Treasury/Census place context](../../records/us-treasury-fio-census-zcta-housing-context-2022.json)
and [Treasury/FEMA hazard context](../../records/us-treasury-fio-fema-nri-hazard-context-2022.json).

## 3. Energy burden changes the room left after housing costs

The 2020 RECS layer estimates annual household energy expenditure and a
midpoint-of-income-band burden proxy. Mean annual energy expenditure rises from
$1,439.58 in the lowest displayed income band to $2,255.28 in the highest, but
the burden proxy falls sharply from **28.73%** to **1.74%** because the same
energy cost occupies very different income room.

This is a modeled annual cross-section, not an observed monthly bill. It does
not show whether a household reduced heating or cooling, missed medicine,
delayed care, borrowed, worked more, or used assistance. It does show why a
single dollar expenditure can represent radically different household
security.

Energy is also a housing-quality and equipment question. High expenditure can
reflect a larger home, inefficient equipment, climate, fuel type, or needed
comfort; low expenditure can reflect efficiency—or under-consumption and an
unsafe temperature. Expenditure alone cannot distinguish those routes.

See the [RECS energy-burden record](../../records/us-recs-energy-burden-income-assistance-2020.json).

## 4. Public backstops can grow while the private problem remains visible

California's FAIR Plan illustrates the public-backstop stage. Policies in
force rose from 242,440 in September 2021 to 642,010 in 2025 and 696,562 by
June 2026; reported insured exposure rose from approximately $160.6 billion to
$768 billion. This is a growth in residual-market stock and exposure, not a
measure of affordable, adequate, or easy-to-claim coverage.

A public backstop can keep a property technically insurable while leaving
premiums, deductibles, exclusions, repair capacity, and disaster recovery
unresolved. It may protect market continuity without restoring the household's
financial room. It may also redistribute risk across policyholders and public
institutions.

See the [housing payment/coverage/mobility record](../../records/us-housing-insurance-payment-coverage-mobility-crosssource-2021-2026.json)
and [California residual-market layers](../us-housing-insurance-risk/california-fair-plan-residual-market-layer-v1.md).

## What the combined evidence supports

- Staying housed requires more than meeting the rent or mortgage.
- Rent arrears, insurance gaps, premiums, nonrenewals, hazard, and energy
  burden are separate but potentially compounding exposures.
- Income and place condition the room left after a fixed cost.
- Market and public backstops can preserve nominal access without guaranteeing
  affordability, adequacy, repair, or recovery.
- The relevant social question is who absorbs the next loss: the household,
  insurer, lender, family, employer, public program, or future resident.

## What it does not support

- that hazard ratings caused a particular premium or nonrenewal;
- that an uninsured homeowner is underinsured in the same way as every other
  uninsured homeowner;
- that rent arrears caused a move, eviction, health outcome, or political view;
- that low energy expenditure means efficiency or comfort;
- that a growing residual market proves either insurance failure or successful
  public protection;
- that payment and coverage risk produce the same household response.

## The next decisive housing episode

The strongest next record would follow a property or household over time:

```text
rent, mortgage, premium, hazard, repair, or energy trigger
  -> notice, renewal, claim, shutoff, or assistance route
  -> payment, borrowing, reduced use, unpaid care, or work response
  -> repair, coverage, health, mobility, and housing result
  -> insurer, lender, utility, employer, family, or public response
  -> stay, move, re-enter, recover, or remain exposed
```

It should preserve property type, tenure, income, hazard, geography, claims,
coverage terms, assistance, repair time, transportation, health/care use, and
the household's stated alternative. A matched property/household-year panel is
more valuable than another national average because the open question is not
whether pressure exists; it is how the pressure changes the feasible option
set.

## Source trail

- [Federal Reserve housing and insurance risk](../../records/us-federal-reserve-housing-insurance-risk-2025.json)
- [Housing payment, coverage, hazard, and backstop bridge](../../records/us-housing-insurance-payment-coverage-mobility-crosssource-2021-2026.json)
- [Treasury/FIO Census place context](../../records/us-treasury-fio-census-zcta-housing-context-2022.json)
- [Treasury/FEMA hazard context](../../records/us-treasury-fio-fema-nri-hazard-context-2022.json)
- [RECS energy-burden layer](../../records/us-recs-energy-burden-income-assistance-2020.json)
- [Housing/insurance project route](README.md)

**Evidence status:** non-pooled survey, market-place, hazard-context, and
household-energy synthesis. Payment, coverage, hazard, energy, mobility,
health, and political-response arrows remain distinct and partly open.
