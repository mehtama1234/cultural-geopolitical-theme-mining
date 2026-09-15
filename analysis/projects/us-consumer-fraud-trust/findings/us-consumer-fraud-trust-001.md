# Fraud recovery burden is shaped by income and payment route, not exposure alone

**Status:** weighted SHED subgroup finding · **Checked:** 2026-09-14

## The bounded finding

The 2024 Federal Reserve SHED public-use file shows that fraud exposure,
unrecovered money, and recovery time occupy different conditional stages. The
share reporting another type of fraud or scam is not monotonic across age or
income. Among account-involved cases, respondents whose incident involved a
peer-to-peer payment route report more unrecovered money and more recovery or
consequence time than the selected non-P2P comparison.

These are weighted self-reports. They do not establish payment-route
causation, verified loss, provider responsibility, or later trust and exit.

## What the subgroup layer measures

| Stage | Estimate | Denominator and boundary |
|---|---:|---|
| Other-fraud exposure, ages 18–29 | 6.85% | Adults in age group |
| Other-fraud exposure, ages 45–59 | 10.25% | Adults in age group |
| Unrecovered money, income $10,000–$24,999 | 53.78% | Respondents reporting other-fraud exposure, conditional subgroup |
| Unrecovered money, income $100,000–$149,999 | 22.57% | Respondents reporting other-fraud exposure, conditional subgroup |
| Some/all unrecovered money, P2P account cases | 46.13% | Account-involved other-fraud cases marked P2P |
| Some/all unrecovered money, non-P2P account cases | 28.83% | Account-involved other-fraud cases marked non-P2P |
| Ten or more recovery/consequence hours, P2P account cases | 43.76% | Account-involved other-fraud cases marked P2P |
| Ten or more recovery/consequence hours, non-P2P account cases | 30.93% | Account-involved other-fraud cases marked non-P2P |

The overall extraction contains 12,295 public-use adult rows. Conditional
outcomes use the relevant fraud or account-involved subsets, not all adults.
The public-use file has no replicate weights or design-based variance fields;
the displayed percentages should not be read as precision-ranked estimates.

## What this adds to the end-to-end atlas

```text
fraud encounter
  -> direct financial loss
  -> unrecovered money and recovery time
  -> payment-provider or firm response
  -> trust, switching, continued use, or exit
```

The survey measures the first three stages with different conditional bases.
It does not identify the specific provider's decision, whether a complaint was
filed, whether a reversal was technically possible, whether the respondent
received a verified remedy, or whether trust or payment behavior changed
later.

The income pattern is a useful counterexample to a simple “higher income means
lower recovery burden” story: the selected income groups are not a monotonic
scale, and account balances, fraud type, reporting, resources, and selection
may all contribute. The P2P contrast is a route-conditioned comparison, not a
payment-method effect.

## Safeguards and limits

- The SHED public-use file is a household-survey respondent source, not a
  verified account or transaction file.
- Fraud, loss, unrecovered money, and time are self-reported and affected by
  recall, wording, nonresponse, and skip patterns.
- The P2P cells are selected account-involved cases and are smaller than the
  adult exposure universe.
- The available language fields are limited to a Hispanic module/oversample;
  they do not support a general language comparison here.
- A conditional work-limitation item is not relabeled as a general disability
  measure, and the public file does not supply a clean all-adult digital-access
  gradient for this path.
- No inference is made about CFPB complaint response, bank liability, or
  verified recovery from these household estimates.

## Next end-to-end test

Link a defined payment-route incident to a case-level ledger containing first
notice, contact attempts, provider response, reversal/claim decision, hours,
verified recovery, repeat effort, and later account use or exit. Preserve the
SHED survey as the household-burden frame rather than treating it as a
substitute for provider records.

**Evidence status:** weighted conditional subgroup comparison with explicit
denominators and counterinterpretations; no design-based variance, causal
payment-route effect, verified remedy, trust change, or exit outcome.

## Sources

- [SHED fraud subgroup layer](../shed-fraud-subgroup-layer-v1.md)
- [Machine-readable subgroup record](../../../records/us-shed-fraud-recovery-subgroups-2024.json)
- [Federal Reserve 2024 banking and credit report](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm)
