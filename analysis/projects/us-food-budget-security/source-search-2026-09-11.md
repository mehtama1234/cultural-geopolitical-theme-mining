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
| US-FED-SHED-FOOD-2024 | [Federal Reserve income and expenses report](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-income-and-expenses.htm) | 7% of adults said their household sometimes or often did not have enough to eat in the prior month; the rate was 19% under $25,000 income and 2% at $100,000 or more | Official household survey | One-month self-report and a different measure from USDA's annual food insecurity scale |
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
