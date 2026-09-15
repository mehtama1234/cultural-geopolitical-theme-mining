# NBER W35067 payment-incidence layer v1

**Checked:** 2026-09-13 · **Status:** full-paper descriptive extraction
completed; household incidence and welfare follow-up remain open

**Source:** [Who Pays for Payments?](https://www.nber.org/papers/w35067), NBER
Working Paper 35067, April 2026

## What changed from the earlier source note

The earlier project record relied on the HBS explanation and correctly marked
the paper as needing review. The official NBER page and downloaded paper are
now reviewed. The paper uses two Fiserv data surfaces: a 2022 merchant
settlement cross-section of approximately one million merchants, covering
around one-fifth of US card payments, and Clover transaction data covering
approximately 800,000 merchants from 2019 through 2022, with cash and card
payments observed together. The committed PDF hash is
`sha256:bc2acfe5dbfb82a063122ae4b22192a50e44b7ebe28641f0a4d8606fe2ccd52b`.

## Direct paper findings

Cards charge interchange fees to merchants and use those fees to fund rewards.
If a merchant raises one common price for customers using different payment
methods, cash and debit users can subsidize credit-card users at the same
merchant. The paper argues that this standard story is incomplete because
consumer payment choices sort across merchants and interchange fees differ by
sector, size, and negotiated contract.

The authors estimate approximately $30 billion in annual redistribution from
cash and debit users to credit-card users. They estimate that consumer sorting
and merchant fee heterogeneity reduce the transfer by 25%, but do not
eliminate it. Because credit-card use rises with income, the paper reports an
estimated $9.2 billion annual transfer from households earning under $150,000
to households earning above that threshold. The paper also reports an effective
sales-tax-equivalent burden 26% higher for cash users than for premium
credit-card users. These are model-based incidence estimates, not observed
payments or measured household welfare changes.

The paper reports several institutional and policy contrasts. Large grocery
stores are an example where payment methods overlap but fees are lower through
sector discounts and private negotiation. The paper also reports that the
Durbin Amendment and the rise of premium credit cards were regressive within
its framework. Those results describe the paper's modeled incidence, not a
complete evaluation of those policies or a claim about current political
beliefs.

## Mechanism

```text
payment method and network rule
  -> interchange fee and reward structure
  -> merchant cost and common or differentiated price
  -> consumer sorting across merchants and payment rails
  -> different net reward, price, and liquidity outcome
  -> possible difference in household buffer or future choice
```

The paper directly measures merchant payment composition, fees, and the
modeled redistribution. It does not observe the same household's full basket,
cash balance, credit access, reward redemption, later debt, or political
response. The connection to household financial pressure therefore remains a
testable bridge. The [machine-readable record](../../records/us-nber-payment-rewards-redistribution-2026.json)
preserves the units, coverage, estimates, counterinterpretations, and PDF
hash.

## What the evidence supports

The strongest supported proposition is institutional and distributional: a
payment system can redistribute value through a shared merchant price while
payment users receive different rewards and face different fees. The paper's
main contribution is that the direction and size of this redistribution depend
on the joint distribution of payment choices and merchant characteristics,
not on average card fees alone.

This sharpens the project's earlier language. “A common checkout price can
hide different net outcomes” is supported as a mechanism under the paper's
pass-through framework. “The payment system caused broad household financial
stress” is not supported. The Federal Reserve SHED measures price pressure,
emergency capacity, BNPL use, and bill payment, but those data do not identify
payment-reward exposure as the cause. The [existing project claims ledger](claims-ledger-v1.md)
should continue to keep those layers separate.

## Counterexamples and limits

- Consumers do not all shop at the same merchants; sorting limits exposure to
  high-fee merchants.
- Large chains and sectors may negotiate lower fees, so an average fee cannot
  be assigned to every purchase.
- Rewards may compensate for credit, convenience, fraud protection, or other
  services; the estimate is not automatically a welfare loss.
- Fiserv and Clover platform coverage is extensive but is not a complete
  nationally representative household panel.
- The $30 billion and $9.2 billion figures depend on sufficient-statistics and
  pass-through assumptions and should not be mixed with observed household
  dollar outcomes.
- The paper is circulated as an NBER working paper and has not undergone the
  review attached to an official NBER publication.

## What would change the finding

The distributional finding would weaken if merchant-level payment overlap,
fee heterogeneity, and pass-through produced little net incidence after
sorting and negotiated contracts were incorporated. The household-pressure
extension would weaken if transaction-level exposure did not predict net
prices, liquidity, debt, or financial adaptation after household resources,
merchant choice, and credit access were measured.

It would strengthen if a linked design observed the same household's payment
mix, merchant prices, rewards, income/liquidity, and later financial outcomes,
with a merchant or policy comparator that changes payment costs without the
same household selection.

## Next test

Pair the paper's merchant incidence estimates with CFPB credit-card market
data, Federal Reserve SHED payment and liquidity measures, and BLS or CEX
spending data. Keep merchant, payment transaction, household, and survey
adult as separate units. The first safe output is a matched exposure design,
not a claim that the modeled transfer equals a household's annual loss.

## Reading rule

The paper establishes a modeled payment-system redistribution mechanism. It
does not by itself establish a household welfare loss, a change in consumer
trust, or a political consequence. Those arrows remain open until a same-unit
or defensible matched design measures them.

