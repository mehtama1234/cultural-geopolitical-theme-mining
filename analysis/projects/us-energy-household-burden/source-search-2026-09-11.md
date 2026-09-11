# Source search: US household energy burden

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** short discovery pass; no settled finding

## Working question

When energy costs take more of a household's income, what other choice becomes harder?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-DOE-LEAD | [DOE Low-Income Energy Affordability Data tool](https://www.energy.gov/cmei/scep/low-income-energy-affordability-data-lead-tool) | The national average energy burden for low-income households is about 6%, compared with about 2% for non-low-income households; some places are higher | Official data tool and definition | Built from modeled and survey-linked data; threshold and income definition matter |
| US-EIA-RECS-2024 | [EIA Residential Energy Consumption Survey](https://www.eia.gov/consumption/residential/) | 2024 household characteristics and energy-insecurity data cover an estimated 132.5 million primary homes, with state-level tables | Official survey and data portal | Initial 2024 releases do not yet include all consumption and expenditure tables |
| US-EIA-SEDS-2024 | [EIA State Energy Data System](https://www.eia.gov/state/seds/seds-data-complete.php) | State-level energy prices, consumption and residential expenditures through 2024 | Official state data | State averages can hide utility, building and income differences |

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

## Decision rule

Pair one household energy-burden measure with a utility or assistance outcome. If the data only show average bills, record the burden and move on.
