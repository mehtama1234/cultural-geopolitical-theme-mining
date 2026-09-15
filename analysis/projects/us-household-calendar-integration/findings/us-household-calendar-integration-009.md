# SIPP child-presence comparisons expose a care-universe boundary

**Status:** official-universe Fay-BRR child-presence finding · **Checked:** 2026-09-13

## The bounded finding

Records with one or more household members under 18 show 30.148% paid
child-care use, 6.295% assistance, and 3.843% reported work prevention. The
no-under-18 subgroup has only 405–539 valid records for the first three fields
and 28 for time lost, producing wide or degenerate intervals.

The appearance of valid child-care fields in the no-under-18 subgroup is a
documented timing/universe issue: a follow-up [reference-parent audit](us-household-calendar-integration-010.md)
shows that `RHNUMU18` is a monthly household-member recode, while `ERP` and the
child-care fields use reference-year, fall, December, and child-age universes.
They must not be silently treated as the same universe.

## Estimates

| Child-presence context | Paid care | Assistance | Work prevented | Time lost* |
|---|---:|---:|---:|---:|
| No members under 18 | 25.673% (SE 6.343) | 12.052% (6.284) | 6.063% (3.237) | 0.000% (0.000) |
| One or more members under 18 | 30.148% (1.171) | 6.295% (0.685) | 3.843% (0.462) | 17.420% (4.373) |

*The no-under-18 time-lost cell has only 28 valid records; the zero estimate
is not evidence of no underlying care or work constraint.

## What this adds

The substantive result is a measurement warning before it is a behavioral
finding. Household child presence, reference-parent status, child age, and
fall child-care use are different concepts. The data can support a broad
child-presence screen, but it cannot support an ordinary “parents versus
nonparents” claim without aligning those universes.

Among the well-populated one-or-more-under-18 records, the estimates provide a
calibrated care/work baseline. The sparse no-under-18 cells are retained as a
counterexample and audit target rather than dropped or interpreted.

## End-to-end route under test

```text
household composition and reference-parent universe
  -> paid care, assistance, or unpaid substitution
  -> work opportunity and time loss
  -> household security, health, recovery, trust, or action
```

This pass strengthens universe discipline and subgroup measurement. It does not
observe a dated care need, provider route, employer flexibility, unpaid
substitution, protected outcome, or later cultural/political meaning.

## Method and limits

The full estimate uses `WPFINWGT`; replicate estimates use `REPWGT1` through
`REPWGT240` under Census’s Fay modified-BRR formula (`G=240`, perturbation
factor `0.5`). Official `AHNUMU18`, `APAY`, `APAYHELP`, `AWORKMORE`, and
`ATIMELOST` flags/universes were applied. The result is person-weighted, and
the child-presence context is not a household-weighted parent indicator.

The no-under-18 care records require a follow-up field-level audit against the
full SIPP codebook and reference-parent variables. No causal care, work,
provider, employer, recovery, trust, political, or cultural claim is made.

## Next test

Audit the reference-parent and child-age fields, then construct a valid
parent/child-care universe before estimating intersections with poverty,
tenure, disability, race, and region. Preserve the separate household,
person, and reference-parent units.

**Evidence status:** reproducible design-based person-weighted child-presence
screen with an explicit universe mismatch/audit boundary; causal and complete
same-unit arrows remain open.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)
- [Machine-readable result](../../../records/us-sipp-care-work-children-official-variance-2024.json)
