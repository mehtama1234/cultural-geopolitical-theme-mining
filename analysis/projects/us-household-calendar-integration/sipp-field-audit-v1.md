# SIPP field audit v1

**Checked:** 2026-09-12  
**File checked:** [2025 SIPP public-use data page](https://cdn.www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)  
**Schema checked:** [2025 SIPP pipe-file schema](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/pu2025_schema.json)

The 2025 SIPP release covers the January–December 2024 reference period. The official page offers a pipe-delimited file and a JSON schema. The schema confirms that the public file has the identifiers, reference-month fields, and outcome fields needed for a first household-calendar slice.

## Verified fields

| Calendar need | Verified SIPP fields | What they give us |
|---|---|---|
| Stable source key | `SSUID`, `SHHADID`, `SPANEL`, `SWAVE` | Sample unit, household-at-interview, panel year, and wave |
| Time | `MONTHCODE`, `RWKSPERM` | Reference month and weeks in that month |
| Housing and utilities | `ETENURE`, `EUTILITIES`, `EAWBMORT`, `EAWBGAS` | Tenure, separate utility payment, and inability to pay rent/mortgage or utility bills |
| Income and work | `THTOTINC`, `TPEARN`, `THTOTINCT2`, `THINCPOV`, `RMNUMJOBS`, `RWKSPERM` | Household monthly income, earnings, poverty ratio, jobs, and weeks |
| Room and debt | `EOWN_SAV`, `TOSAVVAL`, `THDEBT_CC`, `EDEBT_CC` | Savings ownership/value and credit-card or store-bill debt indicators |
| Food pressure | `RFOODS`, `RFOODR`, `EFOOD1`, `EFOOD3`, `EFOOD6` | Food-security recodes and several reported food-shortage conditions |
| Care and work tradeoff | `EPAY`, `EPAYHELP`, `EWORKMORE`, `ETIMELOST` | Child-care payment/help, whether care prevented more work, and time lost from work |
| Transport baseline | `EJB1_PVTRPRM`, `TJB1_PVOTHRC` | Primary commute mode and other commuting expense for job 1 |

These fields can test pieces of HC-001, HC-003, HC-004, and HC-005. They can also set a baseline for HC-002, but they do not record every trip, rideshare fare, warning date, substitute, remedy, or next-month recovery.

## What the file does not give us

- exact pay dates and bill due dates;
- a complete purchase or trip diary;
- rideshare use and fare for every trip;
- the warning, contact attempt, decision-maker, or remedy for a failed service;
- a linked helper household when family support crosses homes;
- a month-by-month measure of trust, blame, or political action.

Those are `missing`, not zero. They remain fields for the proposed calendar panel or a separate permitted record link.

## Reproducible slice

The streaming extractor is [extract_sipp_household_calendar_slice.py](../../../scripts/extract_sipp_household_calendar_slice.py). It selects the fields above, writes a small CSV and JSON report, and supports `--max-rows` for a smoke test. A typical run is:

```bash
python3 scripts/extract_sipp_household_calendar_slice.py \
  --input /path/to/pu2025.csv \
  --output /tmp/sipp-calendar/sipp-household-slice.csv \
  --report /tmp/sipp-calendar/sipp-household-slice-report.json \
  --max-rows 10000
```

The raw file and extracted data belong outside Git. Only the field list, method, and coverage report should be committed unless a later decision approves a de-identified derived table.

The first run is recorded in the [SIPP smoke check](sipp-smoke-check-v1.md). It verified all twelve reference months and the selected keys, while showing that many useful fields are conditional and must not be treated as zeros when blank.

## First questions this can answer

1. How often do rent/mortgage difficulty, utility-payment difficulty, food pressure, and credit-card debt appear in the same source households?
2. Do households with lower monthly income or poverty ratios show different savings and debt patterns?
3. Are child-care limits and lost work recorded alongside different job counts or earnings?
4. Which transport fields are present often enough to support a separate commute-access comparison?

These are descriptive checks. They do not prove that one pressure caused another. The next layer is to use the SIPP longitudinal weights and source-accuracy guidance before making population estimates.
