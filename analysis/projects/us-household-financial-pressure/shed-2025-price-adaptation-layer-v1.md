# SHED 2025 price adaptation layer v1

**Checked:** 2026-09-12  
**Unit:** US adults in the 2025 Federal Reserve Survey of Household Economics and Decisionmaking (SHED)  
**Method:** weighted descriptive percentages using the public-use `weight` field; no causal estimate and no design-based standard errors in this layer.

## Why this layer belongs in the larger program

This is population-level evidence about how people absorb price pressure. It does not describe one household and it does not complete the societal chain by itself. It adds a measured middle section to the wider program:

```text
prices and financial condition
  -> consumer substitution, reduced use, saving cuts, borrowing, delay, or extra work
  -> different room for care, housing, transport, family support, and political judgment
```

The first arrow is measured here. The later cultural, institutional, firm, and political arrows must be tested with their own sources.

## Overall weighted results

| Reported condition or action | Percent |
|---|---:|
| Prices made financial situation somewhat or much worse | 57.6 |
| Switched to cheaper products | 62.2 |
| Used less or stopped using products | 59.7 |
| Reduced savings | 41.0 |
| Delayed a major purchase | 45.6 |
| Increased borrowing | 15.9 |
| Worked more or got another job | 17.0 |
| Made large purchases sooner because prices were expected to rise | 17.6 |
| Had funds set aside for three months of expenses | 54.8 |
| Received outside help for general expenses | 12.9 |
| Received outside help for medical care, debt, or health insurance | 6.3 |
| Received outside help for a car payment, insurance, or repairs | 8.0 |

These are not interchangeable forms of “financial stress.” Substitution, reduced use, lost savings, debt, extra labor, and family assistance are distinct adaptations with different implications for consumption, care, work, and social reproduction.

## Depth: financial-condition gradient

| Current financial condition | Prices worsened finances | Cheaper products | Used less/stopped | Reduced savings | Increased borrowing | Delayed purchase | Worked more/other job | Three-month funds |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Finding it difficult to get by | 86.0 | 83.7 | 82.9 | 66.3 | 48.9 | 72.9 | 32.0 | 9.7 |
| Just getting by | 77.4 | 81.0 | 79.6 | 63.4 | 32.0 | 69.0 | 29.0 | 20.5 |
| Doing okay | 60.6 | 66.1 | 64.2 | 43.9 | 11.8 | 48.9 | 17.3 | 57.8 |
| Living comfortably | 36.2 | 42.2 | 37.9 | 19.2 | 3.6 | 22.1 | 6.5 | 81.2 |

The important societal pattern is not simply that poorer respondents report more pressure. The adaptation menu changes with room: households with less buffer report more substitution, reduced use, saving cuts, borrowing, delayed purchases, and extra work, while households with more buffer retain more emergency capacity. Even people “doing okay” report substantial changes, so pressure is widespread but unequally absorbable.

## A second depth check: change from the prior year

Among respondents who said they were much worse off than a year earlier, 90.7% said prices worsened their finances, 85.7% used less or stopped using products, 70.4% reduced savings, 44.8% increased borrowing, and 76.9% delayed a major purchase. Among those reporting no change, the corresponding figures were 49.9%, 53.1%, 34.3%, 10.7%, and 37.3%.

This is a descriptive alignment between perceived year-over-year decline and reported adaptation, not proof that prices caused every decline. Illness, employment, debt, household composition, and other shocks may also be involved.

## What this adds to the 14-theme map

- **Household room and consumption:** price pressure appears as substitution, reduced use, delay, borrowing, and lost savings—not one “cost” variable.
- **Time as a hidden price / work and bargaining:** some respondents respond with more work or another job; this is a labor adjustment, not just a shopping choice.
- **Care and social reproduction:** outside help for medical or health-insurance costs makes family or social support part of the financial-pressure record.
- **Unequal exposure and status:** the financial-condition gradient and the income, age, ethnicity, and employment cuts provide distributional comparisons.
- **Trust and political judgment:** this layer identifies a material exposure that can be compared with ANES judgment, attribution, trust, and action measures; it does not establish that connection by itself.
- **Firm and market power:** switching or stopping products is evidence of changed consumer behavior, but it does not identify which firms changed terms or who captured the difference.

## Source and limits

The [Federal Reserve SHED data page](https://www.federalreserve.gov/consumerscommunities/shed_data.htm)
describes SHED as a national survey of household economic experiences. The
[2025 public-use codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2025codebook.pdf)
says the file was collected through Ipsos’s probability-based KnowledgePanel
and documents cross-sectional weights plus panel weights for the 2024–2025
panel. This report uses the cross-sectional `weight` and the 2025 file, not
the panel.

The fields are self-reported and several questions are conditional. Each percentage uses the nonmissing weighted denominator for that metric; it should therefore not be read as a share of every respondent when a question applies only to a relevant subpopulation. The analysis does not join respondents to a price series, firm record, later health outcome, move, vote, or policy response.

Reproduction: `python3 scripts/analyze_shed_price_pressure.py --input /path/to/SHED_2025.csv.zip --output /tmp/shed-2025.json`.

## Next bounded tests

1. Align SHED price adaptations with BLS price categories or consumer-expenditure records where the units and dates can be made explicit.
2. Use the SHED panel weights to test whether reported adaptation persists or reverses from 2024 to 2025.
3. Pair the material layer with ANES political judgment variables, preserving separate samples and avoiding a false person-level join.
4. Add firm, complaint, and policy records to test whether changed consumer behavior is followed by remedy, exit, non-use, regulation, or market redesign.
