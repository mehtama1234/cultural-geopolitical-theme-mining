# Full-atlas social augmentation program

This is the execution control for the long-term goal. The atlas contains 2,014
machine-readable research records. The existing 402 social records are topic
waves and calibration evidence; they are not a record-level completion count.
The active operating scope is the United States, prioritizing industrial and
consumer consequences and using public discussion as bounded context around
the research evidence.

## Record-level contract

For every atlas record, the pipeline creates one manifest row containing:

- the exact atlas record path and `trend_id`;
- the mapped canonical theme and social question;
- query terms derived from the title, source unit, geography, and theme;
- four platform attempts: YouTube, Reddit, LinkedIn, and X;
- acquisition status for each platform;
- retained social record IDs, if any;
- access gaps, duplicate decisions, or not-applicable decisions;
- the next action and batch identifier.

The row is not terminal until it is `augmented`, `documented_access_gap`, or
`not_socially_applicable`. `queued` and `in_review` are work states only.

## Batch order

The worker processes deterministic batches of 25 atlas records. Each batch
must preserve a manifest snapshot, acquisition log, normalized records, and a
validator result. The first execution batch is `atlas-batch-0001`, records
1–25 in stable path order. Subsequent batches continue from the last terminal
row; rerunning a batch must not duplicate social record IDs.

## Acquisition rule

Use an authorized Creator/API integration when configured. Otherwise use
public, reproducible search only. Do not bypass login, private groups,
robots, rate limits, or platform safeguards. Search results are discovery
signals, not prevalence estimates. A platform gap is a valid result when the
attempt and boundary are recorded.

## Completion audit

The full-corpus validator must report:

- exactly the current atlas record count;
- zero duplicate atlas record IDs;
- zero rows without a terminal state at final completion;
- every retained item linked to an exact atlas record ID;
- every platform attempt carrying a query, retrieval date, and result or gap;
- social schema validation and the existing research-signals validators.

Until those checks pass, the long-term goal remains active.
