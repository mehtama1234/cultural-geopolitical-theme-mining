# Monthly resources and job counts move on different clocks

**Status:** reproducible SIPP same-person transition diagnostic · **Checked:** 2026-09-14

## The bounded finding

The 2025 SIPP public-use file for the 2024 reference year supports a valid
same-person monthly comparison for two explicitly monthly fields: household
income-to-poverty-ratio band (`THINCPOV`) and number of jobs held in the month
(`RMNUMJOBS`). Across 346,160 valid income-band adjacent-month pairs, 3.67%
changed income band. Across 297,861 valid job-count adjacent-month pairs, 1.70%
changed job-count category.

The figures are not directly comparable prevalence measures because their valid
pair universes differ. They do establish a useful measurement and societal
boundary: monthly material room and job count are related but distinct clocks.
A stable job count does not imply stable monthly resources, and a job-count
change does not identify the direction, size, or cause of a household's
resource change.

## What is measured

| Field | Valid adjacent pairs | Transition result | Unit and method |
|---|---:|---:|---|
| `THINCPOV` | 346,160 | 3.67% changed income-to-poverty band | Weighted pair share using first-month `WPFINWGT`; bands are below 1×, 1–2×, 2–4×, and 4× or more poverty |
| `RMNUMJOBS` | 297,861 | 1.70% changed job-count category | Weighted pair share using first-month `WPFINWGT`; categories retain the recorded monthly job count |

The rerun read 379,215 person-month rows, identified 31,992 people, found
31,090 people with all twelve reference months, and had 346,283 available
adjacent-month pairs before field-specific missingness. The person key is
`SSUID + SHHADID + PNUM`; this prevents unrelated respondents from being
treated as one person.

## The mechanism under test

```text
income, earnings, transfers, hours, and other monthly resources
  -> income-to-poverty position changes
  -> job holding, work intensity, care, consumption, and bill security may respond
  -> health, time, household coordination, trust, or political meaning may change
```

This diagnostic reaches only the monthly resource and job-state stages. It does
not observe hours, pay, schedule control, job quality, job loss reason, care
episode, employer response, exact bill, benefit notice, remedy, recovery,
trust, or political action.

## The critical field boundary

The SIPP file also places annual or reference-period measures on monthly person
records. Rent/mortgage difficulty, utility difficulty, food security, and
hunger therefore cannot automatically be read as newly observed monthly events
just because they appear in twelve rows. The transition layer keeps those
fields separate. A repeated hardship value may reflect survey design or copying
rather than twelve independent episodes.

This distinction is central to the end-to-end program. Person identifiers solve
one linkage problem; they do not solve timing, household-unit, or outcome-
universe problems.

## Counterexamples and safeguards

- A person can remain in the same job-count category while income moves across
  a poverty band through hours, earnings, transfers, household income, or
  other resources.
- A person can change job count without moving income band because a new job,
  lost job, or second job may be small, offset, delayed, or accompanied by
  other income changes.
- Stable monthly categories do not prove stable hours, pay, schedule control,
  health, care, or security.
- The 3.67% and 1.70% figures use different valid-pair universes and do not
  support a claim that income is “more volatile” than employment in a formal
  statistical sense.
- `WPFINWGT`-weighted descriptive transitions are not design-based variance
  estimates and are not causal effects.

## Next test

Extend the same-person monthly design with valid monthly income, earnings,
employment, SNAP status, work hours, and selected household-change fields;
retain status flags and field universes. Then condition transitions on care,
children, disability, tenure, race, region, and resource bands with Fay–BRR
uncertainty where the replicate fields support it. The decisive next link is a
dated resource or work change followed by work loss/gain, care/time loss,
food/housing/utility outcome, and later recovery or institutional action.

Do not promote annual hardship fields into the monthly event ledger until the
SIPP documentation supports that timing interpretation.

## Reproduction and sources

- [SIPP person-transition layer](../sipp-person-transition-layer-v1.md)
- [Reproduction audit](../sipp-person-transition-reproduction-audit-2026-09-14.json)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [240-replicate-weight archive](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip)

**Evidence status:** same-person monthly descriptive diagnostic with explicit
field timing, valid-pair denominators, and reproduction audit; no causal work,
household, health, cultural, political, or geopolitical conclusion is claimed.
