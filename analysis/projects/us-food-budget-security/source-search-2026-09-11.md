# Source search: US food, the household budget, and basic security

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** short discovery pass; no settled finding

## Working question

When money gets tight, what does a household change first to keep food available?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-USDA-ERS-FOOD-2024 | [USDA Household Food Security in the United States in 2024](https://www.ers.usda.gov/publications/113622) | 13.7% of US households, or 18.3 million, were food insecure at some time in 2024; 5.4% had very low food security | Official annual survey and report | It describes prevalence and related conditions; the report does not identify the cause of the trend |
| US-USDA-CHILDREN-2024 | [USDA food-security key statistics](https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-us/key-statistics-graphics) | 18.4% of households with children were food insecure in 2024; 318,000 households had at least one child with very low food security | Official subgroup and state statistics | Household-level categories do not show which adult paid which bill or used credit |
| US-BLS-CPI-FOOD-HOME-2020-2024 | [BLS CPI-U food at home series](https://data.bls.gov/timeseries/CUUR0000SAF11) | The national food-at-home annual-average index rose from 250.233 in 2020 to 306.536 in 2024; annual inflation peaked at 11.42% in 2022 and slowed to 1.19% in 2024 | Official monthly CPI-U series summarized by calendar year | It measures a national price index, not a household basket, local price, income-adjusted burden, or food-security outcome |
| US-FED-SHED-FOOD-2024-2025 | [Federal Reserve income and expenses reports](https://www.federalreserve.gov/publications/2025-economic-well-being-us-households-in-2024-income-and-expenses.htm) | Household food insufficiency was 7% in 2024 and 8% in 2025; the below-$25,000 versus $100,000-or-more gradient was 19% versus 2% in 2024 and 21% versus 1% in 2025, with price-response actions separately reported | Official repeated annual household survey snapshots | Not a linked panel in this layer; one-month self-report and a different measure from USDA's annual food-security scale |
| US-CENSUS-HTOPS-2025 | [Census Household Trends and Outlook Pulse Survey](https://www.census.gov/newsroom/press-releases/2026/household-trends-outlook-pulse-survey.html) | Experimental data include recent food insufficiency, usual expenses, prices, housing, energy and insurance for smaller places and selected groups | Official experimental survey | Different field period and question wording; estimates need care with error and comparability |
| US-CFPB-MEDICAL-2024 | [CFPB medical collections research](https://www.consumerfinance.gov/data-research/research-reports/recent-changes-in-medical-collections-on-consumer-credit-records/) | Medical collections fell on credit records from about 14% to about 5% between March 2022 and June 2023 | Official credit-record analysis | It does not show whether food spending, medical care or borrowing changed |

## First pattern to test

```text
price, income, energy, health, or housing shock
  -> food budget becomes harder to hold
  -> lower-quality food, less food, credit, family help, or public assistance
  -> health, work, school, stress, or political response
```

USDA gives the annual household outcome. The Fed shows a sharp income gradient in a shorter window. The missing link is the order of the household's choices and whether credit or aid prevented a more severe food outcome.

## Counterpoint to keep visible

Food insecurity is not a simple price meter. Income timing, household composition, access to stores, disability, health, school meals and public programs can all matter. A flat national rate can hide a changing mix of families and places.

## Main gaps

- the same-household sequence of food cuts, borrowing, energy payment and skipped care;
- food insecurity by rent, insurance, energy burden and credit status;
- county or state changes tied to benefit rules and food prices;
- differences between household food insecurity and individual food intake;
- whether public assistance prevents debt or only delays another shortfall.

## Decision rule

Pair one food-security measure with one budget or credit measure in the same period and geography. If the sources only show that hardship exists, record it without assigning a cause.
