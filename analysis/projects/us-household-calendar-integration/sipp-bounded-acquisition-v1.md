# SIPP bounded acquisition v1

**Run date:** 2026-09-12  
**Source:** [2025 SIPP public-use data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)  
**Archive:** `pu2025_csv.zip`  
**Archive SHA-256:** `570798a6f512c8f82af311ee01a1668d178063c9076c18a05bc3a5a0039b67ed`

## What was run

The archive was streamed from `pu2025.csv` into [extract_sipp_household_calendar_slice.py](../../../scripts/extract_sipp_household_calendar_slice.py). The raw archive and derived CSV remain outside Git at `/tmp/us-broad-sipp-2025/`.

| Check | Result |
|---|---:|
| Rows written | 100,000 |
| Distinct sample units | 3,650 |
| Distinct household IDs | 3,714 |
| Reference months present | 1–12 |
| Selected fields | 31 |
| Raw data committed | No |

The selected fields cover household and person identifiers, month, tenure, utilities, energy assistance, mortgage and gas burden, income, poverty, savings, credit-card debt, food security, pay help, extra work, time lost, number of jobs, weeks worked, and selected job coverage fields. The complete field list is preserved in the extractor report outside Git.

## What this proves

The official 2025 SIPP CSV can be acquired and streamed in this environment. The repository extractor can read the selected monthly fields together across all twelve reference months without loading the full 2.96 GB CSV into memory. This gives the broader program a reproducible population-survey backbone for household security, work, benefits, energy, food, and debt questions.

## What this does not prove

This is the first 100,000 streamed rows, not a random sample and not a weighted population estimate. The counts and field presence prove an engineering path only. A substantive result requires the full file, the correct person or household longitudinal weight, special-code decoding, missingness handling, variance method, and a documented comparison design.

SIPP still does not observe every exact bill date, purchase, service contact, remedy, price, trip fare, political interpretation, or final vote. It can support monthly population patterns and some within-sample changes; it cannot be joined to CE, ATUS, NHTS, SHED, MEPS, or RECS by geography and called one household.

## Next bounded analysis

Use the full SIPP file after confirming the survey weights and field universes. Start with descriptive monthly tables stratified by tenure, income or poverty group, number of jobs, food-security status, utility burden, energy assistance, savings, and credit-card debt. Report denominators, special codes, missingness, source unit, reference period, and uncertainty. Treat the result as a population-survey layer for the five broad bridges, not as a complete causal chain.
