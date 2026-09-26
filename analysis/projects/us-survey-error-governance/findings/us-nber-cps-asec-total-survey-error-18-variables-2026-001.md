# Finding 001: A high response rate does not guarantee accurate public data

**Status:** bounded survey-governance and administrative-measurement finding · **Checked:** 2026-09-23

## The finding in plain language

Improving the number of people who answer a survey may not fix the biggest error
if people who do answer fail to report benefits or income they actually received.

NBER Working Paper 35680 applies a Total Survey Error framework to eighteen CPS
ASEC income and program-receipt variables linked to administrative records over
more than two decades. For nearly half the variables, reported bias exceeded 40%.
The dominant source was measurement error among respondents who failed to report
receipt, rather than nonresponse alone. Absolute error also tended to rise over
time even when net bias looked stable.

The practical chain is:

```text
household income or program receipt
  -> survey contact and response
  -> reporting, item nonresponse, or imputation
  -> published estimate
  -> policy, research, public belief, and trust [partly open]
```

The broader institutional insight is:

> A number can look stable on average while becoming less accurate for the
> underlying people and records it is supposed to describe.

## What this adds to the atlas

This extends the existing CPS nonresponse and Medicaid-question findings. It
separates response rate, question design, imputation, respondent reporting,
administrative definitions, net bias, and absolute error instead of treating
“better measurement” as one intervention.

## Limits and next test

- This is a working paper, and administrative benchmarks are not automatically
  complete or conceptually identical to survey measures.
- The study does not identify each respondent's reason for misreporting.
- Net bias can hide offsetting positive and negative errors.
- A data-quality problem does not mean every CPS trend is unusable.

The next decisive artifact is a source-by-year audit joining survey question,
response, contact and paradata, imputation, administrative definition, match
quality, correction, subgroup error, published estimate, and downstream policy
use.

## Source

- [NBER Working Paper 35680: The Anatomy and Evolution of Survey Error](https://www.nber.org/papers/w35680)
- [NBER DOI record](https://doi.org/10.3386/w35680)

**Evidence status:** the linked-record decomposition identifies respondent
measurement error as a major source of CPS income and receipt bias; exact error
mechanisms and downstream consequences remain open.
