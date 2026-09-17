# HTOPS 2025 fraud, recovery, and trust acquisition gate v1

**Status:** metadata-screened acquisition route; no raw file downloaded
**Checked:** 2026-09-16
**Machine record:** [HTOPS endpoint acquisition gate](data/htops-2025-fraud-recovery-trust-acquisition-gate-v1.json)

## Why this route matters

The broad program needs a same-respondent route that reaches beyond material
pressure into institutional response, recovery, meaning, and action. The April
2025 HTOPS public-use questionnaire lists a compact candidate route:

```text
scam exposure -> money lost -> report to government -> funds recovered
  -> life satisfaction, social support, institutional trust
```

This is not yet an end-to-end causal episode. The fraud questions refer to the
prior 12 months, do not identify a dated incident or named actor, and do not
record the alternatives, effort, remedy timing, or later trust change. It is,
however, a stronger small candidate for observed reporting and recovery than
the retained HTOPS panel record currently exposes.

## Metadata result

The official April 2025 user notes list `FRAUD1` through `FRAUD8`, including
scam exposure, reporting to law enforcement or a government agency, reasons for
not reporting, money loss, amount lost before recovery, government/law-
enforcement recovery, scam method, and preferred government warning method.
They also list life satisfaction (`OECD`), social/emotional support and
loneliness (`SOC1_first`–`SOC6`), and institutional-trust fields (`Trust1`–
`Trust3`). The June 2025 notes list material conditions and `Trust1`–`Trust3`
but do not list the fraud module.

The official release page says each release includes a PUF, replicate-weight
file, and data dictionary. The current workspace does not retain the April or
June raw PUFs, so this is a metadata gate rather than a new estimate.

## Proposed bounded acquisition

Acquire only the April 2025 PUF and its dictionary first, subject to a total
compressed-download budget of **20 MB**. Extract only the variables below into
a temporary, non-Git slice and delete the raw archive after hashes and schema
checks are recorded:

| Stage | Candidate fields | Required check |
|---|---|---|
| Exposure | `FRAUD1`, `FRAUD7` | universe, reference period, missing codes |
| Reporting/action | `FRAUD2`, `FRAUD3`, `FRAUD8` | report denominator and response coding |
| Loss | `FRAUD4`, `FRAUD5` | amount units, skip pattern, top-code/interval handling |
| Recovery | `FRAUD6` | whether recovery is any amount, actor, and timing |
| Meaning/context | `OECD`, `SOC1_first`–`SOC6`, `Trust1`–`Trust3` | respondent unit, valid codes, weight and replicate-weight availability |

Do not acquire the June PUF for this route unless the April schema shows a
compatible shared identifier and a specific follow-up variable that changes
the test. Do not interpret April retrospective fraud outcomes as a timed
April-to-June panel effect.

## Promotion and stop rules

Promote a result only if the acquired dictionary and PUF establish the exact
universe, weights, missingness, reference period, and denominator. The first
descriptive screen may report exposure, reporting, loss, and recovery jointly;
it must preserve the distinction between reporting to government, recovery,
trust, and life satisfaction. It may not call reporting “civic action” without
checking the question wording and context.

Stop and record an acquisition gap if the PUF lacks a valid dictionary,
replicate weights, compatible respondent key, interpretable recovery coding,
or a bounded denominator. Stop before any second archive if the April module
cannot support a defensible same-respondent screen.

## Official metadata sources

- [Census 2025 PUF release page](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.2025.html)
- [April 2025 HTOPS user notes](https://www2.census.gov/programs-surveys/demo/technical-documentation/hhp/2504_HTOPS_Household_Pulse_User_Notes.pdf)
- [June 2025 HTOPS user notes](https://www2.census.gov/programs-surveys/demo/technical-documentation/hhp/2506_HTOPS_Household_Pulse_User_Notes_04232026.pdf)

The official notes and release page were inspected as metadata only. No raw
HTOPS archive was downloaded in creating this gate.
