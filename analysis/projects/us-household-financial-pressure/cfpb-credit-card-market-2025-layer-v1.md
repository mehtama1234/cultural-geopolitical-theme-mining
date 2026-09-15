# CFPB 2025 credit-card market layer v1

**Checked:** 2026-09-13 · **Source:** [The Consumer Credit Card Market,
2025](https://www.consumerfinance.gov/data-research/research-reports/the-consumer-credit-card-market-2025/)
· **Status:** official market-report extraction

## Why this layer is added

The NBER payment-incidence paper estimates how interchange fees can redistribute
value through merchant prices and rewards. The CFPB report supplies the
adjacent market conditions: outstanding balances, APRs, fees, credit-tier
access, promotional borrowing, and disputes. These sources answer different
questions. The CFPB report does not validate the NBER dollar transfer, and the
NBER paper does not measure the later household cost of carrying a balance or
seeking a remedy.

## Direct evidence

The CFPB report uses multiple data sources as of the end of 2024, including a
sample of de-identified credit records and issuer-reported information. It
reports credit-card balances above $1.2 trillion, an approximate average
monthly balance per cardholder of $5,300, and an average APR of 25.2%. It
reports $160 billion in interest charges assessed, up from $105 billion in
2022, and $31.3 billion in fees assessed, up 23% from 2022. “Assessed” is
important: the report defines interest and fees assessed as accrued or
calculated amounts, which do not necessarily mean they were paid.

The report says 2024 credit-card purchase volume was about $3.6 trillion and
grew about 5%. Virtually all of that growth was attributable to cardholders
with prime-plus scores or higher, while purchase-volume growth for prime or
lower score cardholders was about zero since late 2023. Cards with a zero-
percent introductory APR promotion represented $899 billion in purchase
volume and $352 billion in balances at year-end; roughly one-third of purchase
volume and outstanding balances were on cards with an introductory
promotional rate. The report notes that promotional rates temporarily lower
the cost of revolving balances, while promotional accounts exhibit higher
longer-term balances than cards without the promotion.

The report also measures voice and recourse. Consumers disputed $9.8 billion
in credit-card charges in 2024. Cancelled recurring transactions—including
subscriptions, memberships, and utility bills—made up 40% of disputes. This
is an administrative dispute measure, not a verified-error, refund, or
consumer-loss rate. The report additionally says about 56% of below-prime
balances are held by issuers with less than $100 billion in assets, placing
credit-tier exposure and issuer structure in the same market map without
claiming that issuer size caused the consumer outcome.

The [machine-readable record](../../records/us-cfpb-credit-card-market-2025.json)
preserves the distinct market, purchase-volume, credit-tier, and dispute
denominators, along with the PDF hash.

## Combined evidence chain

```text
payment method / card product / credit tier
  -> merchant fee, reward, APR, promotion, or account access
  -> common price, revolving balance, fee, or deferred cost
  -> household liquidity and ability to dispute or switch
  -> later financial room, repayment, and trust
```

The NBER paper supplies the merchant-side modeled transfer mechanism. CFPB
supplies the market-side cost, product, credit-tier, and dispute environment.
Together they support a stronger institutional proposition: payment access is
not one uniform consumer experience, and visible purchase access can coexist
with differentiated future cost and recourse. They still do not identify the
same household's net benefit, its merchant choices, or whether a dispute was
resolved.

## Counterexamples and limits

- A high APR or assessed fee is not the same as an amount paid or a welfare
  loss; some accounts do not revolve and some fees are avoided.
- A promotional APR can protect liquidity during a temporary shock, even if a
  later balance is higher; its value depends on repayment and income paths.
- Prime-plus spending growth may reflect credit access and account composition,
  not the NBER reward mechanism.
- Disputing a recurring charge may demonstrate an available recourse route;
  the report does not show effort, response time, refund adequacy, or exit.
- The CFPB market report uses multiple internal and issuer data surfaces with
  metric-specific universes. Its aggregate totals cannot be joined directly
  to SHED adults or the NBER merchant sample.

## What would change the finding

The combined interpretation would weaken if payment method and credit-product
differences disappeared after merchant sorting, household liquidity, credit
need, and product selection were controlled, or if higher assessed costs did
not translate into different repayment, buffer, or dispute experiences. It
would strengthen if a matched design observed payment method, merchant price,
rewards, APR, balance, income, and later remedy or household adaptation for
the same consumers.

## Next test

Use the CFPB Terms of Credit Card Plans data and report figure data to create a
time-ordered product surface for APR, annual fee, rewards, promotional period,
and credit-tier availability. Pair that with NBER merchant-incidence
estimates and Federal Reserve SHED measures of payment, liquidity, and
financial adaptation. Keep issuer/account, merchant/transaction, and
household/respondent units separate; treat the matched household exposure as
an acquisition target rather than an inference.

## Reading rule

The CFPB report establishes market conditions and administrative dispute
exposure. It does not establish a causal household burden or remedy. The NBER
estimate establishes a modeled merchant-incidence mechanism. The two layers
can be connected as a testable institutional chain, not collapsed into one
observed transfer or one measure of financial stress.

