# SIPP acquisition v1

**Run date:** 2026-09-12  
**Source:** [2025 SIPP public-use data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)  
**Archive:** `pu2025_csv.zip`  
**Archive SHA-256:** `570798a6f512c8f82af311ee01a1668d178063c9076c18a05bc3a5a0039b67ed`

## What was run

The archive was streamed from `pu2025.csv` into [extract_sipp_household_calendar_slice.py](../../../scripts/extract_sipp_household_calendar_slice.py). The raw archive and derived CSV remain outside Git at `/tmp/us-broad-sipp-2025/`.

The first bounded run was followed by a full-file run using the same extractor and selected fields. The bounded result predates the addition of `PNUM` and `TAGE_EHC`; the full-file result below is the authoritative current extraction.

| Check | Result |
|---|---:|
| Rows written | 100,000 |
| Distinct sample units | 3,650 |
| Distinct household IDs | 3,714 |
| Reference months present | 1–12 |
| Selected fields | 35 |
| Raw data committed | No |

The selected fields cover household and person identifiers, month, final person weight, tenure, utilities, energy assistance, mortgage and gas burden, income, poverty, savings, credit-card debt, food security, pay help, extra work, time lost, number of jobs, weeks worked, and selected job coverage fields. The complete field list is preserved in the extractor report outside Git.

## Full-file run

| Check | Result |
|---|---:|
| Rows written | 379,215 |
| Distinct sample units | 13,670 |
| Distinct household IDs | 13,910 |
| Reference months present | 1–12 |
| Selected fields | 35 |
| Derived CSV SHA-256 | `ac7cf95ba404d4a4a99f7061e9dce31db12c77cd3612920ac7ff906c76d68497` |
| Raw and derived data committed | No |

The full run completed with `max_rows` unset and returned `evidence_status: observed_source_rows`. The final person weight is present for a later person-level weighted analysis. The selected identifiers now include `PNUM` (person number), `TAGE_EHC` (monthly age during the reference period), and `TEHC_REGION` (monthly region of residence), which support same-person and place-stratified comparisons.

## What this proves

The official 2025 SIPP CSV can be acquired and streamed in this environment. The repository extractor can read the selected monthly fields together across all twelve reference months without loading the full 2.96 GB CSV into memory. With `PNUM` and `TAGE_EHC`, it gives the broader program a reproducible population-survey backbone for household security, work, benefits, energy, food, debt, and same-person month-to-month questions.

## What this does not prove

The bounded run was the first 100,000 streamed rows, not a random sample and not a weighted population estimate. The full extraction proves that the selected source rows are available for analysis, but it is still not a weighted population estimate. A substantive result requires use of the final person weight for person-level estimates—or a documented household-weight rule for household estimates—plus special-code decoding, missingness handling, variance method, and a documented comparison design.

SIPP still does not observe every exact bill date, purchase, service contact, remedy, price, trip fare, political interpretation, or final vote. It can support monthly population patterns and some within-sample changes; it cannot be joined to CE, ATUS, NHTS, SHED, MEPS, or RECS by geography and called one household.

## Current analysis boundary

The first descriptive and stratified tables are recorded in the [population layer](sipp-population-layer-v1.md), [tenure layer](sipp-tenure-stratified-layer-v1.md), [resource layer](sipp-resource-stratified-layer-v1.md), and [person-transition layer](sipp-person-transition-layer-v1.md). The variance gate is recorded in the [SIPP variance and weighting plan](sipp-variance-and-weighting-plan-v1.md). Continue with field-specific universes, status flags, replicate-weight variance, and monthly fields explicitly defined as monthly. Treat the result as a population-survey layer for the five broad bridges, not as a complete causal chain.
