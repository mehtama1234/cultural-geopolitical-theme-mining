# Source record: payment rewards and household distribution

**Record ID:** US-HBS-PAYMENT-REWARDS-2026  
**Accessed:** 2026-09-11  
**Primary page:** [HBS Working Knowledge](https://www.library.hbs.edu/working-knowledge/how-credit-card-rewards-became-multibillion-dollar-wealth-transfer)  
**Underlying paper named by the story:** [NBER Working Paper 35067](https://www.nber.org/papers/w35067)  
**Status:** HBS story and underlying NBER Working Paper 35067 reviewed; the
paper's merchant-level data are not public in this workspace.

## What the source says

The HBS story reports research by Mark Egan, Gregor Matvos, Lulu Wang, Amit Seru, and Vincent Yao on interchange fees and rewards. It says the researchers used payment data covering about one million merchants and cash data from about 800,000 Clover merchants. The story reports differences in rewards and fee burdens by payment method and income, including an estimated annual transfer toward households earning more than $150,000.

The story also reports that the researchers tested the result after relaxing the assumption that merchants pass interchange fees into prices. It says shoppers sort across merchants, and large chains can negotiate lower fees, reducing the estimated transfer.

## Method and population

- **Unit:** payment transactions and merchants, then household income and payment method.
- **Geography:** United States.
- **Data described:** Fiserv/Clover transaction data, including card and cash observations; merchant-level analysis.
- **Comparison:** premium credit cards, basic credit cards, debit cards from large and small banks, and cash.
- **Period:** 2022 merchant settlement cross-section; Clover transaction data
  from 2019–2022; paper dated April 2026.

## What it can support

- Payment design can distribute costs and rewards across people who shop at the same merchants.
- A common posted price can conceal different net outcomes by payment method.
- Merchant size, sector, and customer sorting can change the size of the effect.
- The distribution is not necessarily captured by a simple average card fee.

## What it cannot yet support

- A household-level transfer or welfare estimate: the paper's central dollar
  figures are modeled incidence estimates, not observed household bills.
- A claim that the payment system caused broad political behavior or current inflation.
- A claim about every merchant, card product, household, or state.
- A claim that the policy effect is the same as the researchers' estimated consumer incidence.

## Completed verification

The official NBER page and paper were reviewed. The paper records the two
Fiserv data surfaces, merchant and Clover coverage, consumer sorting, fee
heterogeneity, pass-through framework, and policy comparisons. The committed
PDF retrieval hash is
`sha256:bc2acfe5dbfb82a063122ae4b22192a50e44b7ebe28641f0a4d8606fe2ccd52b`.
The new [NBER payment-incidence layer](nber-w35067-payment-incidence-layer-v1.md)
and [machine-readable record](../../records/us-nber-payment-rewards-redistribution-2026.json)
carry the detailed extraction. The merchant raw data remain unavailable, so
reproduction of every table and household-level matching remain open.
