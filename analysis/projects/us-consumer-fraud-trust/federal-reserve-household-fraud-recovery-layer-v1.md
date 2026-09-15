# Federal Reserve household fraud and recovery layer v1

**Question:** When fraud reaches a US household, how much exposure becomes
direct loss, unrecovered money, and time spent seeking recovery?

**Source:** [Federal Reserve, Economic Well-Being of US Households in 2024:
Banking and Credit](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm)
and its [accessible tables](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-accessibility-tables.htm).

## What the source directly reports

The 2024 SHED asked adults about financial fraud for the first time. Twenty-one
percent reported experiencing financial fraud or scams involving their money;
17% reported credit-card fraud and 8% another type of financial fraud. These
categories can overlap, so they must not be added into a single prevalence
estimate.

Among adults experiencing non-credit-card fraud, 63% lost money and 32% said
at least some of that money was not recovered. The Federal Reserve estimates
$84 billion in non-credit-card losses, $21 billion recovered, and $63 billion
in net losses borne directly by consumers. About three in ten people in this
group spent at least ten hours trying to recover funds or dealing with other
consequences from their most recent fraud.

Age differences separate incidence from severity: any reported financial fraud
was 14% among adults ages 18–29 and 26% among adults 60+, while the median
pre-recovery loss among people with non-credit-card losses was $423 for ages
18–44 and $600 for ages 60+.

## Interpretation boundary

This is a weighted household-survey layer, not a verified fraud database. It
measures self-reported exposure, loss, recovery, and time for the most recent
non-credit-card incident; it does not identify the firm, payment rail, account
decision, complaint outcome, or later trust and financial behavior. The $63B
estimate is not directly comparable to FTC reported-loss totals because the
populations, definitions, underreporting assumptions, and measurement frames
differ.

The useful end-to-end arrow is currently:

```text
fraud/scam exposure -> direct loss -> recovery and unrecovered loss -> time cost
  -> institutional response, later trust, financial use, or political action
```

The first three stages have direct survey evidence here. The final stage
remains open and requires same-person follow-up or a valid linked design.

## Reproduction and next test

The fetched Federal Reserve HTML and accessible tables are retained under
`data/` with SHA-256 hashes. The next pass should condition the loss and
recovery path on payment/account type, age, income, disability, language,
digital access, and whether a dispute or firm response occurred. It should
then be compared with the FTC report frame and CFPB case-route frame without
treating any of them as the same denominator.

