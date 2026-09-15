# Utility hardship is associated with more balance carrying and less savings, but credit access is unequal

**Status:** provisional same-month SIPP joint diagnostic · **Checked:** 2026-09-14

## The bounded finding

The 2025 Census SIPP public-use file makes it possible to place three household
finance signals in the same person-record/month extraction: reported inability
to pay utility bills, carrying a credit/store-card balance, and owning a
savings account.

Among 377,945 valid person-record/month rows in the official utility-question
universe, 35.21% (Fay-BRR SE 1.51 percentage points) of rows reporting
utility-payment difficulty carried a credit or store-card balance among rows
with a nonblank credit field. The corresponding share was 26.90% (SE 0.36)
among rows not reporting utility-payment difficulty.

Savings moves in the opposite direction: 46.44% (SE 1.60) of
utility-difficulty rows with a nonblank savings field reported owning a savings
account, versus 64.90% (SE 0.42) of rows without utility difficulty. Intervals
are approximate 95% Fay-BRR intervals from the 240-replicate SIPP file.

This supports a narrow same-month co-occurrence finding: utility pressure sits
alongside lower savings access and greater balance carrying. It does not tell
us whether a utility bill caused borrowing, whether borrowing prevented
shutoff, or whether the same household later recovered.

## The resource counterexample

The joint pattern is not a simple “poorer means more revolving credit” scale.
Within the utility-difficulty subgroup, carried-balance shares increased across
the monthly income-to-poverty bands:

| Monthly income-to-poverty band | Carried credit/store-card balance | Owned savings account |
|---|---:|---:|
| Below 1.00x | 22.35% (17.35–27.36) | 29.33% (24.38–34.29) |
| 1.00–1.99x | 35.09% (29.99–40.19) | 42.18% (36.80–47.56) |
| 2.00–3.99x | 38.02% (32.31–43.73) | 52.48% (47.08–57.88) |
| 4.00x or more | 44.75% (39.09–50.42) | 61.34% (54.93–67.74) |

Parentheses are approximate 95% Fay-BRR intervals in percentage points.

The higher balance-carrying share at higher resources within the hardship group
may indicate greater access to revolving credit, different debt portfolios,
different bill or household composition, or different strategies for preserving
cash. It should not be interpreted as lower-resource households experiencing
less pressure. The savings gradient points in the opposite direction and shows
why access to a financial instrument and financial security are not the same
thing.

## What this adds to the end-to-end program

The result fills a missing middle layer between a material condition and a
financial response:

```text
monthly resources / bill pressure
  -> utility-payment difficulty
  -> savings preservation or credit balance carrying
  -> service continuity, food/housing/work trade-off, or later repayment
  -> institutional judgment, trust, or political action
```

SIPP observes the first three states only as cross-sectional monthly fields.
The final service, repayment, meaning, and political stages require separate
records or a lawful same-unit linkage.

## Denominator and method rules

The analysis uses the final person weight (`WPFINWGT`) and valid household-status
and utility-field flags. Utility difficulty is code 1 and no difficulty is code
2. Credit-card balance and savings-account shares use their own nonblank
denominators. Household fields repeat on person records; the estimates are not
household prevalence figures.

The joint script applies the 240 Fay-BRR replicate weights using the Census
formula with `G = 240` and perturbation factor `0.5`. The intervals quantify
sampling-design uncertainty for the person-record diagnostic; they do not fix
the household-field repetition or establish causal ordering.

## Counterexamples kept visible

- A household can report utility difficulty without carrying a credit balance,
  and a household without utility difficulty can still carry one.
- Carrying a balance can smooth a payment shock, reflect ordinary credit use,
  or indicate repayment strain; the field does not distinguish those paths.
- Owning a savings account does not reveal its balance, liquidity, or whether it
  can cover the utility bill.
- Lower-resource households may face stronger pressure while carrying less
  credit because they have less access to revolving credit.
- The same monthly row does not establish which event came first or whether
  utility payment was restored.

## Next test

Define a household selection rule and use SIPP adjacent-month identifiers to
test whether utility difficulty is
followed by credit balance carrying, savings changes, food/housing hardship,
work changes, or exit from assistance. Keep the result descriptive until the
timing and field universes are audited. Then seek a matched utility-account or
credit-record design for bill amount, notice, service status, payment, and
remedy.

## Sources and reproducibility

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [Machine-readable joint record](../../../records/us-sipp-utility-credit-savings-joint-2024.json)
- [Joint diagnostic script](../../../../scripts/analyze_sipp_utility_credit_savings_joint.py)
- [SIPP Fay-BRR estimator](../../../../scripts/analyze_sipp_fay_brr.py)
- [Existing SIPP material/variance record](../../../records/us-sipp-material-time-care-official-variance-2024.json)

**Evidence status:** reproducible person-weighted same-month joint diagnostic
with explicit field universes and a strong access counterexample; replicate
variance, household weighting, temporal ordering, causality, remedy, trust,
and political action remain open.
