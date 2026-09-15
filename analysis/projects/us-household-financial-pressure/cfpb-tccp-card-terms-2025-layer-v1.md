# CFPB Terms of Credit Card Plans 2025 product layer v1

**Checked:** 2026-09-13 · **Status:** public spreadsheet extracted and hash-
identified · **Unit:** product offer and institution, not cardholder

## Why this layer matters

The 2025 CFPB market report describes realized balances, assessed costs, and
disputes. The Terms of Credit Card Plans (TCCP) survey supplies the upstream
offer surface: what issuers publicly report about APRs, credit-tier pricing,
promotions, fees, and rewards. It therefore helps test whether a household's
visible access to a card can coexist with differentiated future terms. It
cannot show which offer a person received, accepted, or used.

The CFPB says it collects and publishes card-plan data every six months from
over 150 issuers, and that the data are public. The current spreadsheet covers
the July 1–December 31, 2025 reporting period and says it was collected
January–April 2026. The [machine-readable record](../../records/us-cfpb-tccp-card-terms-2025.json)
preserves the 663 product rows, 195 unique institution names, field universes,
derived calculations, and spreadsheet hash.

## Direct file audit

After the metadata rows, the spreadsheet contains 663 product rows and 148
fields. There are 602 unique product-name values and 195 unique institution
names. 410 rows are marked as issued by a top-25 institution. These counts
describe the file, not the number of cards in circulation or issuer market
share.

Purchase APR is offered in 625 rows. Among those rows, 396 report that the
purchase APR varies by credit tier. The median of the numeric product-level
purchase-APR median field is 24.49%; the corresponding medians of the minimum
and maximum fields are 18.49% and 27.49%. These are spreadsheet terms, not
borrower-weighted realized rates. The range can reflect different applicants,
balance tiers, or conditions within a product; it is not a price change for
one person.

The file reports introductory APR offers on 149 rows and balance-transfer
offers on 236 rows. Late fees are marked on 654 rows. 113 rows contain a
numeric annual-fee value, with a product-row median of $95 among those
nonmissing values. The Rewards field is missing on 177 rows; 217 rows include
the text “cashback rewards,” including rows that may also list travel or other
rewards. This is a presence count, not a value, rate, eligibility, or
redemption estimate.

## Mechanism under test

```text
issuer/product offer
  -> eligibility, credit-tier pricing, promotion, fee, or reward
  -> available credit and expected future cost
  -> payment choice, balance carrying, switching, or dispute route
  -> household liquidity and later room to absorb a shock
```

The TCCP file measures the first stage. The CFPB 2025 market report measures
parts of the realized cost and dispute environment. The NBER W35067 paper
measures a separate merchant-side modeled transfer through interchange fees and
rewards. The three surfaces can be ordered as an institutional chain, but
they cannot be collapsed into one household-level causal estimate.

## Counterexamples and limits

- Product availability is not approval or actual access; eligibility,
  geography, underwriting, income, and credit score can narrow the menu.
- A lower introductory APR can provide useful temporary liquidity, while a
  later balance can increase; the sign of the household effect depends on the
  repayment path.
- An annual fee or late-fee field does not show that a fee was assessed or
  paid, and a rewards label does not show reward value.
- Product rows are not market-weighted. A small issuer and a large issuer can
  each contribute one row or many rows without those rows representing equal
  numbers of accounts.
- Missing or textual fields are part of the reporting surface and must not be
  silently treated as zero or no offer.

## What would change the finding

The offer-surface interpretation would weaken if product terms showed little
credit-tier or issuer differentiation after conditioning on actual eligibility
and use, or if realized cardholder outcomes were unrelated to the offered
terms after account selection and liquidity were measured. It would strengthen
if the same account could be followed from available offers through approval,
APR assignment, balance carrying, rewards, fees, disputes, and later financial
adaptation.

## Next test

Compare the 2022–2025 TCCP files field by field, preserving survey redesign and
missingness, then join product terms to issuer/account or consumer records
where lawful and available. The first output should be a product-term
taxonomy and eligibility map, not a household cost estimate. Use the market
report and NBER layer as separate downstream and merchant-side comparators.

## Reproducibility

- [CFPB TCCP data page](https://www.consumerfinance.gov/data-research/credit-card-data/terms-credit-card-plans-survey/)
- [2025-12-31 spreadsheet](https://files.consumerfinance.gov/f/documents/cfpb_tccp-data_2025-12-31.xlsx)
- [CFPB data dictionary](https://www.consumerfinance.gov/data-research/credit-card-data/terms-credit-card-plans-survey/data-dictionary/)
- Retrieval SHA-256: `44a418a8e520f58150f818890c8e05d4ef02497e6808ad9e274e691d6255db1a`

