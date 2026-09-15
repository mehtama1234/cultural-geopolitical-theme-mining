# A larger public card-offer surface does not mean cheaper credit for households

**Status:** CFPB TCCP product-surface comparison with household and payment
context · **Checked:** 2026-09-14

## The bounded finding

The CFPB Terms of Credit Card Plans files contain more reported product rows
and named institutions in the second half of 2025 than in the second half of
2024. The median reported purchase APR among numeric product rows fell from
25.74% to 24.49%, while the number of rows marked as having credit-tier APR
variation rose from 346 to 396. The median annual fee remained $95 in both
files.

This is a change in the public offer surface, not evidence that the same
borrower received cheaper credit. The files do not link products over time,
weight offers by accounts or approvals, or measure fees and APR actually paid.

## Direct comparison

| Measure | 2024 H2 | 2025 H2 | What it measures |
|---|---:|---:|---|
| Reported product rows | 566 | 663 | Spreadsheet product rows after metadata/header rows |
| Named institutions | 145 | 195 | Derived count of institution labels |
| Named products | 529 | 602 | Derived count of product labels |
| Rows with purchase APR offered | 551 | 625 | Reported product-field presence |
| Rows with credit-tier APR variation | 346 | 396 | Reported differentiated pricing field |
| Rows with introductory APR | 133 | 149 | Reported offer feature |
| Rows with balance-transfer offer | 210 | 236 | Reported offer feature |
| Rows with late fees | 556 | 654 | Reported product-field presence |
| Median purchase APR | 25.74% | 24.49% | Median of numeric product-level reported fields |
| Median annual fee | $95 | $95 | Median among numeric annual-fee rows only |

The product-row count rose 17.1% and the named-institution count rose 34.5%,
but those changes can reflect participation, entry, exit, naming, missingness,
or file construction. The two files also have slightly different column
counts. No product identifier is used here to claim a linked longitudinal
change.

## The safe end-to-end interpretation

```text
issuer/product offer surface
  -> eligibility and credit-tier assignment
  -> APR, fees, rewards, and account terms actually received
  -> borrowing, payment, balance, and liquidity choices
  -> household room, stress, and use of alternatives
  -> trust, complaint, switching, or exit
```

The TCCP files measure only the first box. The CFPB 2025 credit-card market
report supplies broader market scale and account/transaction context, while
Federal Reserve SHED supplies household reports of price pressure, borrowing,
saving cuts, delayed purchases, and financial margin. The NBER payment-
incidence work supplies a modeled mechanism through which card rewards and
merchant fees can redistribute value across payment groups. None of these
layers identifies the actual terms, payment behavior, or welfare of the same
household.

The apparent median APR decline therefore has multiple possible meanings. It
could reflect a changed product mix, more low-APR promotional products, issuer
participation, or field coverage. It could coexist with high APRs for
credit-constrained borrowers if credit-tier pricing becomes more common. A
larger visible offer set can also increase nominal choice without increasing
practical choice for a rejected applicant or a household that cannot carry a
balance.

## Counterexamples and limits

- A lower product-level median APR is not a lower borrower-weighted APR and
  does not establish cheaper credit for any income or credit-score group.
- More products and institutions can indicate entry and competition, but can
  also reflect survey participation or naming changes without more approvals
  or usable alternatives.
- Credit-tier APR variation rose in row counts, but the file does not show the
  distribution of applicants across tiers or the terms assigned to them.
- A $95 median annual fee among numeric rows does not measure fee incidence,
  waiver conditions, rewards received, or total account cost.
- Household borrowing, delayed purchases, and reduced use in SHED are not
  attributable to TCCP offers without timing, account linkage, and an exposure
  denominator.

## What this adds to the atlas

This finding separates visible choice from practical access. The next empirical
test should:

1. harmonize the 2022–2025 TCCP fields and identify redesign or participation
   changes;
2. join product terms to approval, credit tier, account balances, utilization,
   fees, rewards, and payment behavior where lawful data exist;
3. compare terms and realized cost by income, credit history, geography,
   payment method, and liquidity; and
4. connect the result to household adaptation, complaints, remedy, trust, and
   switching without treating continued card use as satisfaction.

The mechanism would weaken if product-surface changes do not survive field and
participation harmonization, or if realized borrower-weighted costs fall
equally across constrained and unconstrained households. It would strengthen
if differentiated terms and rewards persist after account exposure and are
associated with unequal payment, liquidity, or exit options.

## Sources and reproduction

- [CFPB TCCP trend record](../../../records/us-cfpb-tccp-terms-trend-2024-2025.json)
- [CFPB 2025 single-vintage TCCP product record](../../../records/us-cfpb-tccp-card-terms-2025.json)
- [2024–2025 TCCP comparison layer](../cfpb-tccp-terms-trend-2024-2025-layer-v1.md)
- [CFPB Terms of Credit Card Plans survey](https://www.consumerfinance.gov/data-research/credit-card-data/terms-credit-card-plans-survey/)
- [CFPB 2025 credit-card market layer](../cfpb-credit-card-market-2025-layer-v1.md)
- [Machine-readable CFPB 2025 credit-card market record](../../../records/us-cfpb-credit-card-market-2025.json)
- [NBER payment-incidence finding](us-household-financial-pressure-003.md)
- [Federal Reserve SHED price-adaptation layer](../shed-2025-price-adaptation-layer-v1.md)

**Evidence status:** descriptive product-file comparison with modeled payment
and household context; no borrower-weighted cost, consumer exposure, causal
access, welfare, trust, or exit estimate.
