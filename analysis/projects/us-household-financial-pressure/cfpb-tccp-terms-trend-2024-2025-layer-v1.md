# CFPB TCCP terms trend 2024–2025 layer v1

**Checked:** 2026-09-13 · **Status:** descriptive two-period product-surface
comparison · **Unit:** reported card-plan product row

## Why this comparison matters

The 2025 TCCP file is not a market-share panel. Comparing it with the prior
2024 second-half file can show whether the public offer surface changed, but
it cannot show that the same products changed terms, that more consumers
received those products, or that household costs moved. The files themselves
also changed shape: the 2024 file contains 566 data rows and 149 columns,
while the 2025 file contains 663 rows and 148 columns after the metadata and
header rows.

The reproducible extraction is in
[`scripts/analyze_cfpb_tccp_terms_trend.py`](../../../scripts/analyze_cfpb_tccp_terms_trend.py).
It downloads the two official spreadsheets, records SHA-256 hashes, reads the
common header row, and calculates product-row counts, offer flags, numeric APR
medians, and fee medians. It does not weight products by accounts or volume.

## What changed in the file surface

| Measure | 2024 H2 | 2025 H2 | Reading boundary |
|---|---:|---:|---|
| Product rows | 566 | 663 | More reported rows, not market growth |
| Columns | 149 | 148 | Field surface changed slightly |
| Named institutions | 145 | 195 | Names are not necessarily economic entities or market shares |
| Unique product names | 529 | 602 | Names are not a linked product panel |
| Purchase APR offered | 551 | 625 | Product-row count |
| APR varies by credit tier | 346 | 396 | Product-row count among all rows; not a borrower effect |
| Introductory APR offered | 133 | 149 | Product-row count |
| Balance transfer offered | 210 | 236 | Product-row count |
| Late fees offered | 556 | 654 | Offer flag, not fee payment |
| Cashback rewards text | 227 | 235 | Text-presence count, not reward value or redemption |

The 2025 file therefore exposes a broader reported offer surface than the
2024 file, but the change may reflect issuer participation, product additions,
renaming, reporting rules, or field definitions. It must not be described as
an increase in cards held by consumers.

## Term distributions

Among numeric product rows, the median purchase-APR field declined from 25.74%
in 2024 H2 to 24.49% in 2025 H2. The median minimum APR declined from 19.99%
to 18.49%, and the median maximum declined from 28.99% to 27.49%. The
product-level annual-fee median was $95 in both files, while the number of
numeric annual-fee rows declined from 121 to 113. The median numeric late fee
was $29 in both periods.

These movements are descriptive and should not be read as cheaper credit for
borrowers. The APR fields can vary by credit tier, balance, promotion, and
eligibility. A lower product-level median can coexist with a higher rate for a
particular applicant, and a missing annual fee is not a zero fee.

## Mechanism under test

```text
issuer participation and product design
  -> advertised APR, fee, promotion, rewards, and eligibility surface
  -> approval and assigned terms for a particular applicant
  -> payment choice, balance carrying, or switching
  -> realized household cost and financial room
```

The TCCP comparison measures only the first stage. The CFPB market report
measures aggregate realized market conditions, and NBER W35067 estimates a
merchant-side payment incidence mechanism. The product trend is useful for
conditioning those layers, but it does not connect them to the same account or
household.

## Counterexamples and uncertainty

- A larger public product menu can coexist with tighter approval or geographic
  restrictions.
- A lower advertised APR can be available only to stronger applicants or for
  a limited promotional period.
- Product rows are not account-weighted, so row-count changes cannot establish
  market expansion or consumer exposure.
- The two files have slightly different column surfaces and may include
  reporting or survey changes; field comparability must be checked before
  forming a long time series.
- Reward text does not measure reward generosity, and fee flags do not measure
  assessment, payment, or remedy.

## What would change the finding

The descriptive offer-surface result would weaken if a harmonized product
panel showed that row and field changes were primarily naming or participation
artifacts. It would strengthen if stable products could be followed across
periods and their terms linked to approval, credit tier, account use, balance,
fees, rewards, and repayment outcomes.

## Next test

Harmonize the 2022–2025 TCCP files using field-level definitions and product/
issuer identifiers where possible. Then pair the offer surface with CFPB
account outcomes and Federal Reserve household measures. Preserve product,
issuer, account, transaction, and household units separately.

## Reproducibility

- [CFPB TCCP data page](https://www.consumerfinance.gov/data-research/credit-card-data/terms-credit-card-plans-survey/)
- [2024 H2 spreadsheet](https://files.consumerfinance.gov/f/documents/cfpb_tccp-data_2024-12-31_uYJ9Krf.xlsx)
- [2025 H2 spreadsheet](https://files.consumerfinance.gov/f/documents/cfpb_tccp-data_2025-12-31.xlsx)
- 2024 H2 SHA-256: `4791f20e20ab294fc8ab4588637b74e5e19f7686b419ec2b26122efd777862f1`
- 2025 H2 SHA-256: `44a418a8e520f58150f818890c8e05d4ef02497e6808ad9e274e691d6255db1a`

