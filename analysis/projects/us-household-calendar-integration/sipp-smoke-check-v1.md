# SIPP smoke check v1

**Run date:** 2026-09-12  
**Source:** [2025 SIPP public-use pipe file](https://cdn.www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)  
**Reference period:** 2024  
**Rows read:** first 10,000 rows from the archive stream

## What was verified

The extractor read 10,000 rows without loading the full file and wrote the selected 31 fields to a temporary CSV. The rows contained:

- all 12 `MONTHCODE` values;
- 362 distinct `SSUID` sample units;
- 367 distinct `SSUID:SHHADID` household-at-interview combinations;
- four panel-year/wave combinations in the first slice;
- usable values for income, rent/mortgage difficulty, utility difficulty, food recodes, and household poverty-ratio fields;
- commute-mode values where a person had a qualifying job record.

## What the missingness check showed

Several fields are conditional rather than universally filled. Utility-assistance, savings value, child-care, commute, and other job fields are blank for many rows because the question does not apply to every person or household, or because the value is not reported in that record. `ETIMELOST` had only 12 non-special values in this smoke slice.

This is a design warning. A blank field cannot be read as zero, no care problem, no commute cost, or no hardship. The extractor must keep the source status flags and the research layer must preserve `unknown`.

## What this does not prove

The first 10,000 rows are an engineering smoke sample, not a weighted estimate and not a random sample. The counts above prove that the fields and month codes can be read together; they do not describe US households. A population result requires the full file, the correct survey weights, variance method, and source-accuracy review.

## Reproduction

The raw archive can be streamed without a full expansion:

```bash
unzip -p /path/to/pu2025_csv.zip pu2025.csv \
  | head -n 10001 \
  | python3 scripts/extract_sipp_household_calendar_slice.py \
      --input - \
      --output /tmp/sipp-smoke/sipp-household-slice.csv \
      --report /tmp/sipp-smoke/sipp-household-slice-report.json \
      --max-rows 10000
```

The smoke output was removed after inspection. No raw SIPP data or derived row file is committed.

