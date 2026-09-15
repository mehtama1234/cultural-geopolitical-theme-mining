# Material pressure, care, and work appear as different SIPP constraints

**Status:** provisional population-layer finding · **Checked:** 2026-09-13

## The bounded finding

The 2025 SIPP public-use file, covering the 2024 reference year, provides a
monthly person-record backbone for material pressure, food security, savings,
debt, child-care payment, child-care work constraints, tenure, and job count.
The first weighted scan shows these conditions are not one composite state:
utility-payment difficulty, food security, savings, child-care payment, and
work-prevention fields have different definitions and different missing or
restricted universes.

This makes SIPP useful for the long-term program's material/time/care lane, but
the result is a measurement layer—not a claim that one household experienced
every listed condition or that one condition caused another.

## Selected scan results

| Field | Conditional weighted result | Unit boundary |
|---|---:|---|
| Owned or being bought | 67.23% | Selected nonblank person-weighted records with `ETENURE` code 1 |
| Unable to pay utility bills | 7.06% | Selected nonblank records with `EAWBGAS` code 1 |
| High or marginal food security | 88.56% | Selected records with `RFOODS` code 1 |
| Owned a savings account | 63.72% | Selected nonblank records with `EOWN_SAV` code 1 |
| Carried a credit/store-card balance | 27.43% | Selected nonblank records with `EDEBT_CC` code 1 |
| Paid for child care | 30.08% | Selected nonblank records with `EPAY` code 1 |
| Child care prevented working or working more | 3.88% | Selected nonblank records with `EWORKMORE` code 1 |
| One job | 54.20% | Selected nonblank records with `RMNUMJOBS` code 1 |

The scan read 379,215 selected person-record/month rows and retained 378,291
with a positive final person weight. Household fields are repeated on person
records, so these percentages must not be paraphrased as household prevalence
without an explicit household selection and weight method.

## What the monthly view adds

Across the twelve 2024 reference months, the descriptive ranges were 4.61%–
4.69% for rent/mortgage payment difficulty, 7.03%–7.09% for utility-payment
difficulty, 88.45%–88.63% for high or marginal food security, and 54.05%–54.32%
for one job. These narrow ranges are not evidence of true stability: no
design-based variance was computed, and field universes and person/household
roles differ.

## End-to-end route under test

```text
bill, income, care, or work condition
  -> monthly household/person adjustment
  -> food, housing, health, time, debt, or employment outcome
  -> recovery, trust, political judgment, or institutional response
```

SIPP supports the first two stages for selected monthly variables. It does not
record every exact bill, price, service contact, remedy, daily minute, firm
decision, attribution, or political response. Those arrows require additional
sources or a lawful same-unit design.

## Method and counterexamples

The scan uses `WPFINWGT`, the final person weight, and preserves field-specific
nonblank shares. The official 240-replicate file is available for subsequent
variance work, but this initial layer does not compute design-based standard
errors. Child-care payment and work-prevention variables are not all-adult
measures; utility and energy-assistance fields have restricted universes; and
person weights do not turn repeated household fields into household counts.

The counterexample is central: a person can have food security but little
savings, a household can have utility difficulty without rent difficulty, and
child-care payment can coexist with no reported work prevention. The program
must preserve these combinations rather than collapse them into “household
stress.”

## Next test

Use the SIPP monthly spine with field-specific universes and replicate-weight
variance. Define household selection before estimating joint outcomes, then
compare income/work/benefit transitions with care, food, utility, health, and
recovery outcomes. Keep ATUS, MEPS, RECS, SHED, and firm records as separate
layers unless a documented person or household join exists.

**Evidence status:** reproducible person-weighted population diagnostic with
explicit missingness and universe limits; no causal or same-household
material-to-time-to-politics chain is claimed.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP acquisition and weighting notes](../sipp-bounded-acquisition-v1.md)
- [Machine-readable SIPP material/time/care population record](../../../records/us-sipp-material-time-care-population-2024.json)
