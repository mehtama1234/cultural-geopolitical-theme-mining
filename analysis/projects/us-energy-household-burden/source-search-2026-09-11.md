# Source search: US household energy burden

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** first matched evidence pass completed; health, work, and later housing links remain open

## Working question

When energy costs take more of a household's income, what other choice becomes harder?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-DOE-LEAD | [DOE Low-Income Energy Affordability Data tool](https://www.energy.gov/cmei/scep/low-income-energy-affordability-data-lead-tool) | The national average energy burden for low-income households is about 6%, compared with about 2% for non-low-income households; some places are higher | Official data tool and definition | Built from modeled and survey-linked data; threshold and income definition matter |
| US-EIA-RECS-2024 | [EIA Residential Energy Consumption Survey](https://www.eia.gov/consumption/residential/) | 2024 household characteristics and energy-insecurity data cover an estimated 132.5 million primary homes, with state-level tables | Official survey and data portal | Initial 2024 releases do not yet include all consumption and expenditure tables |
| US-EIA-SEDS-2024 | [EIA State Energy Data System](https://www.eia.gov/state/seds/seds-data-complete.php) | State-level energy prices, consumption and residential expenditures through 2024 | Official state data | State averages can hide utility, building and income differences |
| US-GAO-HOME-INSURANCE-2026 | [GAO homeowners insurance review](https://www.gao.gov/products/gao-26-107867) | Average premiums rose about 3% after inflation from 2019–2024, while some southern coastal areas rose 25% or more; higher risk can also reduce availability | Official review of premium and risk data | National averages hide local exposure; insurance is state-regulated and the report does not follow household budgets |

## First pattern to test

```text
home, fuel, utility, or weather condition
  -> energy bill or energy insecurity
  -> food, care, rent, debt, work, or comfort choice
  -> public aid, utility response, or political demand
```

The opening sources measure burden and supply context. They do not yet show which household choice changes first.

## Main gaps

- shutoffs, arrears and payment plans by income and place;
- building quality, rent, ownership and utility structure;
- health, school, work and care effects after high bills;
- the effect of weatherization or energy aid on later choices;
- which households can shift fuel use or buy efficient equipment;
- public and utility records on complaints, relief and disconnections.
- whether energy and insurance costs arrive together for the same household.

## Decision rule

Pair one household energy-burden measure with a utility or assistance outcome. If the data only show average bills, record the burden and move on.

## Verification pass: 2026-09-11

DOE's LEAD tool defines energy burden as the share of gross household income spent on household energy. Its current summary puts the national average at 6% for low-income households and 2% for non-low-income households; some areas are above 30%. The tool can separate renters and owners, building age, building type, heating fuel, income and race, but it does not include transportation costs.

LEAD also estimates that 52% of low-income households are renters. That matters because a renter may pay the energy bill without being able to change insulation, windows or equipment. The tool identifies this as a split between who pays and who can make the improvement; it does not show which household later cuts food, care, debt or work.

EIA's 2024 RECS has preliminary housing and energy-insecurity data for an estimated 132.5 million primary homes and nearly 17,000 responding households. Consumption and expenditure data are not all in the first release, so the current evidence is strongest on housing conditions and insecurity, not the full bill-to-choice path.

[DOE LEAD tool definitions and data](https://www.energy.gov/cmei/scep/low-income-energy-affordability-data-lead-tool)

[EIA 2024 Residential Energy Consumption Survey](https://www.eia.gov/consumption/residential/)

## Matched evidence result

The 2024 EIA table gives a direct household-pressure measure: 32.89 million primary homes reported reducing or forgoing food or medicine to pay energy costs; 16.19 million received a disconnect or delivery-stop notice; 17.55 million kept the home at an unhealthy temperature; and 6.83 million could not use heating equipment. These are separate reported conditions, and households may report more than one.

The next finding therefore treats energy burden as a control problem as well as a price problem. Renters may pay the bill without controlling the building, and assisted households may face a gap between a utility allowance and actual expense. The full later outcome is still open.
