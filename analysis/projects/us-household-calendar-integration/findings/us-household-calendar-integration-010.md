# SIPP’s “no under-18” care records are a timing and universe issue, not a childless-care finding

**Status:** SIPP universe audit · **Checked:** 2026-09-13

## The audit result

The previous child-presence screen showed nonblank care fields among records
with `RHNUMU18=0`. The field-level audit explains why this should not be read as
ordinary care among households without children.

`RHNUMU18` counts household members under 18 in the current reference month.
`ERP` identifies an adult who is a reference parent to household children under
18, while the care variables use additional fall-reference-year, December,
child-age, and reference-parent universes.

Among 225,187 positive-weight person-record/month rows with `RHNUMU18=0`,
568 rows still have `ERP=1`. The same group has 405 nonblank `EPAY` rows, 539
nonblank `EWORKMORE` rows, and 28 nonblank `ETIMELOST` rows. The counts are a
structural diagnostic, not prevalence estimates.

## Month pattern

The overlap is concentrated earlier in the reference year: 93 `ERP=1` rows in
January, 82 in February, and 74 in March among the monthly `RHNUMU18=0`
records, falling to 2 in December. This pattern is consistent with household
composition changing during the year while annual/reference-year parent and
care variables remain attached to the person record.

## What this changes

The prior child-presence comparison remains useful as a screen, but its
no-under-18 subgroup cannot be called “nonparents” or “childless households.”
The correct next step is to construct a reference-parent/child-age universe
using `ERP`, December child counts, and the relevant status flags before
estimating care by parent status.

This is an important program control result: a plausible subgroup label can
silently combine different clocks and units. The atlas now preserves the
timing mismatch instead of turning it into a cultural or behavioral claim.

## End-to-end route under test

```text
household composition over time
  -> reference-parent and care universe
  -> payment, assistance, work prevention, or time loss
  -> protected/sacrificed outcomes and later recovery or meaning
```

The audit strengthens the measurement stage. It does not establish a dated
care need, provider route, employer flexibility, unpaid substitution, health
outcome, trust, political action, or cultural meaning.

## Method and limits

The audit streams the 2025 SIPP public-use file into the established selected
slice, retains positive `WPFINWGT` person-month rows, and cross-tabulates
`MONTHCODE`, `RHNUMU18`, `ERP`, and nonblank care fields. It is not a
household-weighted estimate and does not use replicate-weight variance because
the output is a universe diagnostic.

The official dictionary defines `ERP` as an adult reference parent and
`RHNUMU18` as a monthly household under-18 count. It also defines the care
questions with separate fall/December and child-age conditions. Those are not
interchangeable fields.

## Result of the aligned-universe test

The care extraction was rerun with `ERP` as the grouping field and the official
Fay-BRR replicate-weight method. All valid care records fall in `ERP=1`
(`reference parent`): 24,549 records for `EPAY` and `EPAYHELP`, 31,788 for
`EWORKMORE`, and 1,119 for `ETIMELOST`. The resulting estimates reproduce the
national care screen: 30.083% paid care (SE 1.168 percentage points), 6.379%
payment assistance (0.698), 3.877% work prevention (0.466), and 16.992% time
lost (4.289).

`ERP=2` has zero valid records and zero denominator weight for every care field.
This is the decisive universe result: the care questions in this extraction are
already reference-parent restricted, so `ERP` cannot produce a parent/nonparent
comparison. The earlier `RHNUMU18=0` records with nonblank care fields are
therefore timing/record-structure artifacts, not evidence that nonparents are
being asked the same care questions in the same universe.

The next valid extension is to add the December child-count and child-age
fields as explicit audit columns, then test care intensity, work response, and
resource/health outcomes within the reference-parent universe. Income, tenure,
disability, race, and region remain valid stratifiers only after that aligned
universe is preserved.

**Evidence status:** reproducible source-universe audit; no child-care
prevalence or causal societal claim is made.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [Machine-readable audit result](../../../records/us-sipp-child-presence-reference-parent-audit-2024.json)
