# A shared checkout price can hide different payment-system burdens

**Status:** provisional merchant-to-household mechanism finding · **Checked:** 2026-09-14

## The bounded finding

NBER Working Paper 35067 combines merchant payment data with a payment-system
incidence model. It estimates that common merchant prices can redistribute
value between cash/debit users and credit-card users because interchange fees
fund rewards and payment choices sort across merchants. The paper estimates
roughly $30 billion per year in gross redistribution from cash/debit users to
credit-card users, reduced by about 25% after consumer sorting and merchant fee
heterogeneity. It estimates $9.2 billion per year moving from households below
$150,000 income toward households above that threshold.

These are modeled incidence estimates, not observed losses on household bills.
They identify a payment-system mechanism; they do not show that the mechanism
caused financial stress, lower consumption, debt, distrust, or political action.

## What the NBER evidence measures

| Layer | Direct evidence | Unit and boundary |
|---|---|---|
| Merchant settlement data | Payment composition, counts, fees, and card types across approximately one million merchants, covering roughly one-fifth of US card payments | 2022 Fiserv merchant cross-section; not a household panel |
| Clover transaction data | Cash and card payments observed together across approximately 800,000 merchants | 2019–2022 platform merchants; not all US transactions |
| Modeled redistribution | Approximately $30B annual gross transfer; about 25% reduction after sorting/fee heterogeneity; $9.2B toward households above $150,000 | Sufficient-statistics incidence model; not observed household dollars |
| Relative burden | Cash users’ modeled effective sales-tax-equivalent burden is 26% higher than premium credit-card users | Model comparison; not a measured tax or welfare loss |

The paper also reports sector and merchant differences. Large grocery stores
illustrate negotiated fees and payment overlap, which prevents assigning an
average fee or modeled transfer to every consumer or merchant.

## The cross-source bridge

```text
payment network and merchant pricing rule
  -> interchange fee and reward structure
  -> common or differentiated merchant price
  -> payment choice and consumer sorting
  -> different liquidity, reward, and effective-price position
  -> household adaptation, fairness judgment, or political meaning
```

NBER reaches the merchant and modeled incidence stages. Federal Reserve SHED
measures household price pressure, bill payment, emergency capacity, payment
use, and financial adaptation, but it does not identify whether a respondent's
experience reflects the NBER payment-reward mechanism. The two sources should
be aligned as a future matched exposure design, not pooled as if they shared
households.

## What this changes

The visible checkout price is not always the complete distributional object.
The same nominal price can coexist with different rewards, credit access,
fraud protection, convenience, liquidity, and merchant options. The model's
income gradient makes financial room relevant, but income alone does not fix
payment choice, merchant access, balances, rewards, or welfare.

This is a firm/consumer power question as much as a price question: who can
choose the payment rail, wait for rewards, use a negotiated merchant, or avoid
the common-price system? The current evidence identifies the mechanism and
the likely distributional dimensions, not the lived result for a household.

## Counterexamples and limits

- Consumers sort across merchants, so a high-fee merchant does not expose every
  payment user equally.
- Negotiated contracts and sector differences can reduce or reverse the
  average incidence pattern.
- Rewards may compensate for credit, convenience, fraud protection, or other
  services; a transfer estimate is not automatically a welfare loss.
- Fiserv and Clover platform coverage is extensive but not a representative
  household or national transaction panel.
- The NBER paper is a working paper; modeled dollar figures depend on
  pass-through, matching, and sufficient-statistics assumptions.
- SHED household outcomes have different years, question universes, and
  denominators; no same-household payment mix and later outcome are observed.

## Next end-to-end test

Pair transaction-level payment mix, merchant prices, rewards, fees, income,
liquid assets, credit access, and later spending or debt for the same household
or account. Add a merchant, card-network, or policy comparator that changes
payment costs without changing household selection. Preserve merchant,
transaction, household, and survey-adult units separately until that design
exists.

## Sources and reproduction

The [NBER payment-incidence layer](../nber-w35067-payment-incidence-layer-v1.md)
contains the full paper extraction, coverage, model boundary, and PDF hash.
The [machine-readable record](../../../records/us-nber-payment-rewards-redistribution-2026.json)
preserves the reported merchant surfaces and modeled observations. The [SHED
adaptation layer](../shed-2025-adaptation-distribution-layer-v1.md) supplies
the separate household-response context.

**Evidence status:** merchant/platform evidence plus modeled incidence and
separate household adaptation context; household welfare, causal pass-through,
trust, and political consequences remain open.
