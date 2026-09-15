# Household selection changes the apparent size of SIPP material pressure

**Status:** provisional unit-construction finding · **Checked:** 2026-09-14  
**Project:** Household calendar integration

## The bounded finding

The 2025 SIPP public-use file repeats household conditions on person records.
If those rows are read as household observations, larger households contribute
more records. A deterministic one-record-per-household-month selection changes
the point estimates for the same 2024-reference-year fields. That is not a
substantive household trend by itself; it is evidence that unit construction
must be settled before the program describes a household burden or joins it to
time, care, health, or politics.

## What was compared

The source slice contains 379,215 person-record/month rows, of which 378,291
have a positive final person weight. The selection diagnostic produced 166,706
household-month records by choosing `ERP=1` where available and the lowest
`PNUM` as a deterministic fallback within each
`SSUID/SHHADID/SPANEL/SWAVE/MONTHCODE` group.

| Measure | All person-record view | One selected record per household-month | Difference |
|---|---:|---:|---:|
| Unable to pay rent or mortgage | 4.637% | 4.489% | −0.148 pp |
| Unable to pay utility bills | 7.063% | 6.458% | −0.605 pp |
| High or marginal food security | 88.563% | 88.225% | −0.338 pp |

The selected-record diagnostic attaches pseudo Fay–BRR uncertainty using the
same person's `WPFINWGT` and `REPWGT1`–`REPWGT240`: rent/mortgage difficulty has
an approximate SE of 0.213 percentage points, utility difficulty 0.246 points,
and high/marginal food security 0.349 points. These are sensitivity intervals,
not official household estimates, because the extracted surface does not
provide an official household weight.

## Weight-surface recheck

The current 2025 SIPP schema contains 5,203 variables. A label/name scan found
one weight-related variable, `WPFINWGT`, labeled the final person weight; it did
not find a separately named household weight. This is a schema-surface audit,
not a claim that no household estimator could exist in other Census
documentation. It does, however, confirm that the current extracted surface
cannot silently be described as household-weighted.

The scan is preserved in the [machine-readable selection record](../../../records/us-sipp-reference-household-selection-2024.json), including the schema hash and the exact result. The next valid route is either an official documented household estimator or an explicitly labeled sensitivity analysis using reference-person selection and person-weight reuse.

## The mechanism under test

```text
person rows repeat household fields
  -> household size and respondent selection affect the apparent rate
  -> the material-pressure denominator changes
  -> time/care/work comparisons can be misread as household burden
  -> later claims about adaptation, meaning, or politics inherit the unit error
```

This is a measurement and denominator finding. It does not say that utility
hardship fell, that household conditions differ causally by size, or that the
selected reference person is the household. It says that the program must not
move from repeated household fields to household prevalence without an explicit
selection rule and appropriate weight.

## Why it matters for the end-to-end program

The material/time/care question requires a stable unit before it can ask who
protected food, housing, health, rest, or work and who sacrificed it. A
person-weighted record can be useful for a person-experience question. A
household-context question requires one household rule, and a household
prevalence estimate requires a household weight or a documented estimator that
supports that target. The difference is not cosmetic: the utility-payment
diagnostic moves by more than half a percentage point under the selection
rule.

The selected view also does not close the stronger chain. It has no exact bill
date, detailed minutes, service contact, remedy, attribution, recovery, trust,
or political-action follow-up. It is therefore a gate for the next join, not an
end-to-end cultural or political result.

## Counterexamples and safeguards

- Person-level hardship can be the correct estimand when the question concerns
  people exposed to a household condition; the person-record view is not
  automatically wrong.
- The reference person may be the best available reporter for a household
  field, but preferring `ERP=1` does not prove that this person controls the
  household's money, care, or schedule.
- The point differences may reflect person-weight reuse and respondent
  selection rather than real household-size effects.
- A household-weighted estimate could differ from both views; this diagnostic
  must not be promoted as its substitute.

## Next test

1. Confirm whether the full 2025 SIPP release supplies a household weight or a
   documented household estimator for the target fields.
2. Compare reference-person, lowest-`PNUM`, and any official household route
   under the same field-specific universes and replicate design.
3. Preserve one-record-per-household rules before producing joint outcomes for
   utility, food, child-care, work, health, or recovery.
4. Only then connect the selected material unit to time allocation, dated
   events, institutional routes, interpretation, and later action.

## Sources and reproducibility

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [Machine-readable selection diagnostic](../../../records/us-sipp-reference-household-selection-2024.json)
- [Reproduction script](../../../../scripts/analyze_sipp_reference_household_selection.py)
- [Earlier person-weighted SIPP finding](us-household-calendar-integration-001.md)

**Evidence status:** reproducible unit-construction sensitivity comparison with
explicit selection, replicate matching, and absent-household-weight limits; no
household prevalence, causal effect, recovery, trust, or political action is
established.
