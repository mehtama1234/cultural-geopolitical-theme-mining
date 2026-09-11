# Source search: US consumer credit and the shrinking cash buffer

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** verification pass complete; connected memo written, same-household path remains open

## Working question

When a household cannot cover a small surprise with cash, what does credit change—and what does it leave exposed?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-FED-SHED-2024 | [Federal Reserve Economic Well-Being of US Households in 2024](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-overall-financial-well-being.htm) | 63% of adults said they could cover a $400 surprise with cash or its equivalent; 15% said they would use a credit card and pay over time, and 13% could not pay it right away | Official household survey | A stated response is not the same as a later repayment or default |
| US-FED-SHED-EXPENSES | [Federal Reserve 2024 income and expenses](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-income-and-expenses.htm) | 37% said monthly spending rose from a year earlier, compared with 32% reporting higher income; 28% skipped some medical treatment because of cost | Official household survey | Self-reported and descriptive; the figures do not identify which bill came first |
| US-CFPB-MEDICAL-COLLECTIONS | [CFPB recent changes in medical collections](https://www.consumerfinance.gov/data-research/research-reports/recent-changes-in-medical-collections-on-consumer-credit-records/) | The share of consumers with medical collections on credit records fell from about 14% to about 5% between March 2022 and June 2023 | Official credit-record analysis | Credit-record changes do not measure whether the medical bill was paid or whether care changed |
| US-CFPB-MEDICAL-DEBT | [CFPB medical debt and credit reports](https://www.consumerfinance.gov/data-research/research-reports/paid-and-low-balance-medical-collections-on-consumer-credit-reports/) | Medical collections can affect access to housing, car loans, insurance and work, even though they are less predictive of repayment than many other collections | Official research report | It describes possible use of the record; it does not estimate the effect for every person |
| US-NBER-CARD-BANKING | [NBER Credit Card Banking](https://www.nber.org/papers/w35607) | Account-level regulatory data cover 550 million monthly accounts, about 90% of the US card market, and describe how card revenue is made | Working paper abstract | Market revenue facts do not by themselves show whether borrowing helps or harms a household |
| US-FED-BNPL-2024 | [Federal Reserve 2024 banking and credit](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm) | 15% used BNPL; 24% of users paid late, rising to 40% for users with family income under $25,000; 57% of late users said they were charged extra | Official household survey | Self-reported use and late payment; it does not follow balances after the missed payment |
| US-CFPB-BNPL-2025 | [CFPB BNPL market report](https://www.consumerfinance.gov/data-research/research-reports/the-buy-now-pay-later-market/) | Six large providers supplied 2019–2023 market data on users, loan size, late fees and charge-offs; the 2023 loan-level late-fee rate was 4.1% and charge-off rate 1.83% in the report's measures | Official product-market review | Provider data cover a large but selected part of the market; measures are not the same as the Fed's household survey rates |
| US-NYFED-HHDC-2025Q4 | [New York Fed household debt and credit, Q4 2025](https://www.newyorkfed.org/newsevents/news/research/2026/20260210) | Credit-card balances reached $1.28 trillion; 4.8% of all outstanding debt was in some stage of delinquency, and mortgage deterioration was concentrated in lower-income areas and places with falling home prices | Official credit-record panel | Aggregate credit records do not show why a person borrowed or which bill the borrowing covered |

## First pattern to test

```text
bill or income shock
  -> cash buffer is not enough
  -> credit, family help, skipped care, or delayed payment
  -> later balance, fee, credit record, or reduced choice
  -> firm revenue, regulator action, or political demand
```

The Fed shows both the first household choice and a large difference in late payment by income. CFPB supplies product-level measures that are lower because they use different denominators and provider records. The New York Fed shows the broader debt position and place pattern. The missing link is what happened to the same household after it borrowed or delayed payment.

## Counterpoint to keep visible

Credit is not only a trap. It can prevent a missed payment, preserve a needed purchase, or spread a cost across paychecks. The Fed says the leading BNPL reasons were spreading payments and convenience; the CFPB's provider data show that most loans were not charged off. The memo must compare repayment, fees and later access before calling borrowing a transfer of risk.

## Main gaps

- emergency borrowing and repayment by income, race, age and place;
- credit-card, BNPL, overdraft and family-help paths for the same event;
- whether credit preserves housing, energy, food or medical access;
- fees and interest paid after the first borrowing decision;
- how lenders, employers, landlords and insurers use the resulting record;
- evidence that challenges the idea that credit mainly shifts risk to households.

## Decision rule

Pair one household buffer measure with one observed credit outcome and one product term. If the data only show that people would borrow, record the available bridge and move on.
