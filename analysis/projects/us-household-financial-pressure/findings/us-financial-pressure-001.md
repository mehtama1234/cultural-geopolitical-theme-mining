# Finding 001: The checkout price may hide a different deal for each household

**Status:** provisional  
**Date:** 2026-09-11  
**Question:** Do payment and credit products lower the visible barrier to purchase while moving cost and risk toward households with fewer choices?

## Finding

The first evidence suggests that consumer finance does not only decide whether someone can buy. It can also decide who receives a reward, who pays for it through a common price, and who absorbs the next fee or loss of savings. That is a distributional mechanism, not yet a complete explanation of household financial stress.

## What we directly know

- HBS reports research using payment data across roughly one million merchants and cash data from roughly 800,000 Clover merchants. The story reports different shares of rewards and interchange costs by payment method and income, plus an estimated transfer toward higher-income households. [HBS source record](../source-record-hbs-payment-rewards-v1.md)
- The same story says merchant sorting and large-chain bargaining reduce the estimated transfer. This means the effect depends on where people shop and on merchant power.
- The Federal Reserve's 2025 household survey found that prices remained the most common financial concern. It also reported that 58% of adults said price changes had worsened their finances, 16% did not pay all bills in the prior month, and 63% could cover a hypothetical $400 emergency with cash or its equivalent. [Federal Reserve SHED](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-executive-summary.htm)
- The Federal Reserve reported that financial well-being declined for young adults, low-income families, and Black adults, despite relative stability in the overall measure. It also reported BNPL use and overdraft or NSF triggers among BNPL users. [Federal Reserve SHED](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-executive-summary.htm)

## Causal chain under test

```text
payment rule and merchant fee
  -> common posted price plus different rewards or costs
  -> payment choice shaped by income, liquidity, and access to credit
  -> different net household burden and financial buffer
  -> different ability to handle the next shock
  -> different trust in firms, banks, and policy
```

The first two links have evidence in the HBS account. The household-buffer and trust links are not yet established for this mechanism.

## Four maps

| Map | Current reading | Missing evidence |
|---|---|---|
| Material | Fees, rewards, prices, savings, and emergency capacity can differ by payment method. | Full transaction and household incidence; current merchant pass-through. |
| Social | A common checkout price may feel fair while the net deal differs by income and liquidity. | Interviews, repeated survey measures, and behavior after fees or shocks. |
| Institution | Card networks, banks, merchants, regulators, and payment rules shape the terms. | Rulemaking, contracts, enforcement, and changes after the Durbin Amendment. |
| Power | Premium customers and large merchants may have more options; cash and debit users may have less ability to avoid the system. | Direct measures of exit, bargaining, and product substitution. |

## Counterevidence and limits

The HBS story itself reports two mitigating factors: consumers shop at different merchants, and large chains negotiate lower fees. Cash users may also benefit from lower prices at merchants with little card overlap. The evidence currently comes through an HBS summary; the underlying NBER paper and data have not yet been reviewed because the NBER page was inaccessible in this run. The Federal Reserve evidence is descriptive and cannot show that payment rules caused the reported household outcomes.

## What would change our mind

The interpretation would weaken if the underlying data showed little net distribution by payment method after merchant sorting, or if lower-income and debit users consistently received offsetting benefits that exceeded their fee burden. It would also weaken if household financial stress did not differ with payment exposure after income, debt, prices, and local conditions were accounted for.

## Next test

Read NBER Working Paper 35067, reproduce the main incidence table if possible, and join that mechanism to CFPB card-market data, SHED subgroup measures, and BLS price or expenditure series. Then add a case where merchants surcharge, offer cash discounts, or use a different payment structure.

## Claims used

C-001 through C-008 in [claims ledger v1](../claims-ledger-v1.md).
