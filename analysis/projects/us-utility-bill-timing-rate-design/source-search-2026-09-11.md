# Source search: US utility bill timing and rate design

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** matched evidence pass complete; household-level bill timing and arrears history remains open

## Working question

Can a household manage an energy cost over a year and still fail when seasonal use, fixed charges, or the due date creates a large monthly bill?

## Sources

| ID | Source | What it tells us | Limit |
|---|---|---|---|
| EIA-2024-BILLS | [EIA: Electric sales, revenue, and average price data](https://www.eia.gov/electricity/sales_revenue_price/) | EIA publishes 2024 residential average monthly bills by state and Census division, making place-level bill comparison possible. | Average bills do not show the spread across households, due dates, arrears, or the income available when the bill arrives. |
| EIA-SEASONAL-BILLS | [EIA: Prices and factors affecting prices](https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php) | Residential electricity use and bills vary with weather and season; most consumers pay rates based on an average cost rather than each day's price. | A national explanation does not show the exact rate schedule or cash stress for a particular customer. |
| EIA-FIXED-COMPONENT | [EIA: Annual Energy Outlook weather assumptions and bill components](https://www.eia.gov/outlooks/aeo/IIF_weather/) | EIA describes a fixed component in residential natural-gas bills: when use falls, the fixed part makes up a larger share of the bill and the per-unit cost can look higher. | This is a model description and example, not a complete national record of electric customer charges. |
| GAO-HUD-UTILITY-ALLOWANCE | [GAO: HUD rental assistance and utility allowances](https://www.gao.gov/products/gao-24-105532) | Utility costs can leave assisted households rent-burdened when allowances do not fully cover reasonable costs. | It does not measure every utility customer or show how a particular due date becomes arrears. |
| EIA-RECS-2024-HC11.1 | [EIA: Household energy insecurity, 2024](https://www.eia.gov/consumption/residential/data/2024/hc/pdf/HC11.1_2024.pdf) | Households report disconnect notices and inability to use heating or cooling equipment, showing that bill pressure can become loss of service. | The table does not contain each household's rate design, due date, income timing, or bill history. |

## First pattern to test

```text
rate design and seasonal use
  -> monthly bill and due date
  -> cash gap, arrears, or payment choice
  -> shutoff risk, unsafe temperature, aid, or debt
```

The annual average hides the timing question. The next test needs monthly bills and income dates for the same household.
