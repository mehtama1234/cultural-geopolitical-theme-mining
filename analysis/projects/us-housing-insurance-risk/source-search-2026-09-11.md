# Source search: US housing, insurance, and the cost of staying put

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** short discovery pass; no settled finding

## Working question

Is insurance cost and availability becoming a new limit on who can safely own, finance, and remain in a home?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-FED-HOUSING-2025 | [Federal Reserve housing findings](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-housing.htm) | 6% of homeowners went without homeowners insurance; the share was higher in low- and moderate-income neighborhoods and among lower-income owners; cost was the leading stated reason | Official household survey | Reported answers; not a causal estimate |
| US-FED-SHED-APPENDIX-2025 | [Federal Reserve SHED housing appendix](https://www.federalreserve.gov/publications/2026-supplemental-appendixes-report-economic-well-being-us-households-2025-appendix-b.htm) | Insurance payment amounts, shopping behavior, reasons for no coverage, and survey counts | Official survey appendix | Preserve weights and subgroup definitions |
| US-TREASURY-FIO-2025 | [Treasury report on homeowners insurance](https://home.treasury.gov/news/press-releases/jy2791) | Over 330 insurers and more than 246 million policies were analyzed for 2018–2022; premiums rose faster than inflation and varied sharply by climate-risk ZIP code | Official administrative-data analysis | Historical window; climate risk is one of several possible causes |
| US-TREASURY-FIO-2025-REPORT | [FIO 2025 insurance industry report](https://home.treasury.gov/system/files/311/Final%20FIO%202025%20Annual%20Report.pdf) | Reports higher premiums and nonrenewals in 2024 and explains that cost and availability can affect household coverage | Official report | Needs state-level and household-level checks |
| US-CENSUS-HOUSING-COST-2024 | [Census: cost of homeownership](https://www.census.gov/newsroom/press-releases/2025/acs-1-year-estimates.html) | Median monthly owner costs with a mortgage rose to $2,035 in 2024; insurance fees were among the drivers | Official ACS release | Median values hide major differences by place and household |
| US-CENSUS-RENTER-BURDEN-2023 | [Census: renter cost burden](https://www.census.gov/newsroom/press-releases/2024/renter-households-cost-burdened-race.html) | Nearly half of renter households were cost-burdened in 2023, with differences by race | Official ACS release | Older data than the homeowner release; cost burden does not show cause |
| US-NBER-PROPERTY-INSURANCE-32579 | [Property Insurance and Disaster Risk](https://www.nber.org/papers/w32579) | Uses more than 74 million inferred premiums from 2014–2024 and studies how disaster risk enters premiums and home values | Working paper; revised November 2025 | Working paper; review design, data construction, and alternative explanations |

## Strongest distribution check

The Federal Reserve's 2025 household survey reports that 6% of homeowners went without homeowners insurance. The share was 12% in low- or moderate-income neighborhoods and 5% in high-income neighborhoods. Roughly 2 in 10 homeowners with income below $50,000 went without coverage, and 43% of uninsured homeowners said they could not afford it. Among insured owners with income below $50,000, nearly 30% said they struggled to afford premiums. These are reported household conditions, not proof that climate risk caused the gap.

## First pattern to test

```text
risk or higher replacement cost
  -> premium, deductible, or nonrenewal
  -> coverage gap or higher monthly housing cost
  -> weaker ability to borrow, repair, sell, or stay
  -> lower household security and possible local political pressure
```

The first three links have evidence in the opening sources. The effect on borrowing, selling, staying, and politics is still open.

## Main gaps

- whether households actually leave, delay repairs, or lose mortgage access;
- state rules and insurer behavior after a nonrenewal;
- renters' exposure when landlords pass insurance costs into rent;
- local tax base, public aid, and neighborhood turnover;
- differences by race, income, age, disability, and family type;
- the strongest evidence against the insurance-risk explanation;
- whether the pattern is temporary repricing or a lasting change in where people can live.

## Decision rule

Do one next pass using state insurance filings, mortgage and property records, and one local comparison. If those records cannot connect insurance changes to household or neighborhood choices, record the topic as an important condition and move on.
