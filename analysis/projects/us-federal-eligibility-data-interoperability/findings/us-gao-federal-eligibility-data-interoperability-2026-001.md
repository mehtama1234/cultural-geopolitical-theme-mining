# Finding 001: Government can have many eligibility databases without having usable oversight

**Status:** bounded federal-data, payment-integrity, and institutional-accountability finding · **Checked:** 2026-09-22

## The bounded finding

GAO reviewed nine selected federal data sources used to decide whether entities
were eligible for awards or payments. Agencies can draw on more than 100 such
sources across the award life cycle, and 28 sources were in or designated for
the Do Not Pay working system as of September 2025.

The problem was not a lack of data alone. All nine selected sources had some
data-quality issue, such as missing, invalid, duplicate, or otherwise flawed
records. Seven of the nine had cross-source inconsistencies, including overlap
in data that should have been mutually exclusive. GAO found no designated
governmentwide authority for interoperability, and the related congressional
matter remained open as of July 2026.

GAO partially linked SAM entity data, SAM Exclusion records, and
USAspending.gov using unique entity identifiers. The link matched 2,074 awards
to exclusion records, but the match did not establish that any particular award
was improper. Case-level evaluation was still required.

The route is:

```text
eligibility and exclusion records
  -> identifier matching
  -> award or payment decision
  -> investigation and correction
  -> public value and trust [not observed here]
```

## What this adds to the broad atlas

This adds a state-capacity and accountability version of a recurring pattern:

> More data does not automatically create more control. If identities and
> definitions do not line up, oversight can be data-rich but decision-poor.

It also creates an important boundary for automated or AI-assisted oversight:
matching records can surface a lead, but it cannot replace case-level judgment.

## Limits and counterevidence

- GAO selected nine sources judgmentally; this is not a census of all federal
  eligibility systems.
- Data-quality problems and cross-source inconsistencies do not prove a
  particular improper award, payment error, or recipient harm.
- The 2,074 matches are leads for review, not confirmed improper payments.
- Agency-specific systems may serve legitimate program purposes even when they
  were not designed for cross-agency matching.
- The review does not follow a person or entity through correction, repayment,
  future eligibility, trust, or public benefit.

The next decisive artifact is a protected case ledger joining entity identity,
eligibility source, award, exclusion status, human review, correction,
repayment, and later program outcome.

## Sources

- [GAO-26-107466: Federal Award and Payment Eligibility Data](https://www.gao.gov/products/gao-26-107466)

**Evidence status:** official oversight evidence shows fragmented and
inconsistent data infrastructure; it does not establish a national improper-
payment rate or a particular recipient's wrongdoing.
