# Public record map: housing and insurance v1

**Checked:** 2026-09-12  
**Purpose:** identify the records needed to test the cost-of-staying chain without claiming that one public file contains it all.

## The records and their jobs

| Record | Unit and time | Can measure | Cannot measure alone |
|---|---|---|---|
| [Federal Reserve SHED 2025](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-housing.htm) | Adult or homeowner; 2025 survey | Insurance status, affordability trouble, housing cost, income, mortgage, and reported hardship | Exact bill, policy terms, claim, property risk, or later move |
| [Treasury FIO homeowners report and supporting metrics](https://home.treasury.gov/system/files/311/Analyses_of_US_Homeowners_Insurance_Markets_2018-2022_Climate-Related_Risks_and_Other_Factors_0.pdf) | ZIP code and year; 2018–2022 | Premiums, claims, nonrenewals, coverage measures, insurer concentration, and climate-risk comparisons for a large share of private policies | A named household’s payment, deductible, coverage quality, claim recovery, or move |
| [FEMA National Risk Index](https://hazards.fema.gov/nri/data-resources) | Census tract/county and hazard; current releases | Modeled hazard exposure and expected annual loss across perils | Whether a property is insured, the premium charged, mitigation work, or actual damage |
| [OpenFEMA NFIP data](https://www.fema.gov/about/openfema/data-sets/national-flood-insurance-program-nfip-data) | Flood policy and claim records; release-specific periods | Flood policies, premiums, claims, payments, and mapped risk fields where publicly released | Private coverage, non-flood perils, full household finances, and unobserved uninsured losses |
| [FHFA House Price Index](https://www.fhfa.gov/data/hpi/datasets) | Geography and period; repeat-sales index | Change in home prices by state, metro, county, ZIP, or tract where available | One property’s sale reason, insurance terms, repair quality, or buyer financing |
| [HMDA public data](https://www.consumerfinance.gov/data-research/hmda/) | Mortgage application and loan; year and geography | Applications, approvals, loan purpose, property type, income, lender, and action | Insurance premium, claim, property hazard, and the household’s later payment or move |
| [Census ACS](https://www.census.gov/programs-surveys/acs/data.html) | Household, housing unit, and geography; annual or multi-year estimates | Tenure, mortgage, income, rent, race, age, disability, commuting, and local housing conditions | Policy terms, claim outcomes, exact premium, or causal response |

## The safe join

The useful public join is geographic and time-based:

```text
property area + year
  -> hazard measure and insurance market measure
  -> home-price and mortgage-market measure
  -> household composition and housing-cost measure
```

That join can show whether places with different risk and insurance conditions also have different prices, lending, tenure, or household hardship. It cannot be called a property-level causal chain unless the same property and household are observed through the change.

## The missing link

The hardest gap is between a ZIP-code market signal and a household action. Public records usually do not show all of these together:

- the renewal notice and exact premium;
- the deductible and excluded loss;
- the mortgage escrow change;
- the repair or mitigation choice;
- the claim payment and delay;
- the food, care, transport, or debt tradeoff;
- the decision to stay, sell, move, or go without coverage.

This is why the household-calendar project needs a consent-based property event ledger. The public files set the place and market context; the household record carries the dated choice and recovery.

## First local comparison

Choose one high-risk and one lower-risk US area with enough public data. For each area, compare:

1. FIO premium, claim, and nonrenewal measures;
2. FEMA modeled hazard and expected loss;
3. FHFA home-price change;
4. HMDA mortgage applications and action rates;
5. ACS tenure, income, mortgage, rent, and disability distributions;
6. SHED household reports as a national reference, not a local estimate.

Keep the comparison descriptive. The first output should identify where the signals line up and where they do not. A mismatch is useful: it may show that prices changed without coverage loss, or that households stayed despite a higher cost because moving was worse.

## What would change the working idea

The cost-of-staying idea would weaken if higher-risk places did not show higher protection costs or weaker availability; if those changes did not line up with home prices, lending, or household hardship; or if dated property records showed that households usually recovered without sacrificing protection, repairs, work, care, or mobility.
