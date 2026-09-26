# Finding: Privacy protection can change what the public is able to see

**Status:** bounded statistical-privacy and public-information finding · **Checked:** 2026-09-23

## The finding in plain language

This Census working paper proposes a mathematical way to protect confidential
data. The basic idea is to start with the real data, add controlled randomness,
and release a noisy version that is less revealing but still useful.

The paper connects the strength of the privacy protection to a “temperature”
parameter and demonstrates the proposed mechanism on histograms. It proves
formal privacy properties for the proposed process under its stated assumptions.

## What this adds to the atlas

It adds a technical version of the program's control-and-visibility theme:

```text
confidential records
  -> privacy mechanism and controlled noise
  -> public statistic
  -> useful signal and hidden detail
  -> public judgment, research, and policy [open]
```

Privacy is not simply “data available” or “data hidden.” The mechanism decides
how much exactness the public receives and where error enters. That can protect
people while also making small groups, local problems, or unequal outcomes
harder to see.

## Limits and counterexamples

- This is a proposed mathematical framework, not a field test or Census policy
  decision.
- A formal privacy guarantee does not prove the released statistic is useful,
  fast enough, secure in practice, or understandable.
- Noise can protect confidentiality while obscuring small populations or
  changing public interpretation.
- The proof-of-concept uses histograms; it does not establish performance for
  every Census product or administrative decision.
- No public attitude, household, firm, political, or policy outcome is measured.

The next decisive artifact is an operational privacy-utility ledger comparing
privacy loss, error, subgroup accuracy, suppression, runtime, user
understanding, and downstream decisions for the same statistical product.

## Source

- [Census formal-privacy working paper](https://www.census.gov/library/working-papers/2026/adrm/ced-wp-2026-002.html)
- [Census disclosure-avoidance working-paper series](https://www.census.gov/about/policies/privacy/statistical_safeguards/working-papers.html)

**Evidence status:** the paper proposes and mathematically analyzes a privacy
mechanism; operational utility, equitable error, and public trust remain open.
