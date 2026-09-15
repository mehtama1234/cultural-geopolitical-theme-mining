# Monthly resource and job changes point in different directions across adjacent months

**Status:** reproducible same-person SIPP cross-lag diagnostic · **Checked:** 2026-09-14

## The bounded finding

The 2025 SIPP public-use file supports a same-person monthly comparison using
two fields that are explicitly defined for the reference month: household
income-to-poverty-ratio band (`THINCPOV`) and number of jobs held (`RMNUMJOBS`).

Among valid pairs with a monthly resource band at month *t* and job counts at
months *t* and *t+1*, the share whose job-count category changed at *t+1* was:

| Resource band at month *t* | Next-month job-count change | Fay-BRR SE | Approx. 95% interval |
|---|---:|---:|---:|
| Below 1× poverty | 2.51% | 0.15 pp | 2.21–2.81% |
| 1–1.99× | 1.63% | 0.10 pp | 1.43–1.83% |
| 2–3.99× | 1.62% | 0.07 pp | 1.49–1.75% |
| 4× or more | 1.62% | 0.05 pp | 1.51–1.72% |

The reverse cross-lag also differs by job count. A resource-band change in the
following month occurred for 2.99% of zero-job rows, 3.75% of one-job rows,
and 5.00% of two-job rows. The three-job cell was 5.18%, but its interval was
wide (2.81–7.55%) because the cell is small.

This is not a causal work or poverty result. It is evidence that monthly
resource position and job holding form distinct clocks: the lowest-resource
group has more next-month job-count movement, while people with more jobs have
more resource-band movement in the following month.

## What this adds to the end-to-end program

The cross-lag fills a more precise middle segment:

```text
monthly income / transfers / household resources
  -> resource-band position
  -> job holding changes, or resource-band changes after job status
  -> hours, pay, care, consumption, and bill security
  -> recovery, institutional judgment, trust, or political action
```

Only the first two monthly states are observed here. The dataset does not tell
us why a job count changed, whether a job was good or bad, whether hours or pay
changed, whether care shifted, or whether any institution was blamed.

## Why the direction must remain descriptive

The lower-resource group has a higher point estimate for next-month job-count
change, but that difference can reflect job instability, household composition,
earnings, transfers, reporting, or selection. Conversely, people with two or
more jobs show more resource-band movement, but an additional job may be small,
temporary, or offset by hours, prices, household changes, or benefit changes.

The result should not be translated into “poverty causes job switching” or
“multiple jobs cause income volatility.” It supports a narrower design claim:
monthly material position and job count should be modeled as separate states,
with both directions tested.

## Timing and unit safeguards

The person key is `SSUID + SPANEL + SWAVE + PNUM + MONTHCODE`, and the first
month's `WPFINWGT` weights each adjacent pair. The 240 replicate weights are
used with the Census Fay-BRR formula (`G = 240`, perturbation factor `0.5`).
The estimates are person-record transitions, not household prevalence.

This pass deliberately excludes utility difficulty, food security, and other
annual or reference-period questions from the monthly event chain even though
those fields appear on monthly rows. Repeated values do not automatically mean
new monthly observations.

## Counterexamples kept visible

- A stable job count can coexist with a resource-band change through earnings,
  hours, transfers, household composition, or costs.
- A job-count change can occur without a resource-band change because the job is
  small, delayed, temporary, or offset by other resources.
- A lower-resource person may change job count more often without gaining room;
  a higher-resource person may carry multiple jobs without the same hardship.
- A monthly transition does not identify a bill, employer decision, care event,
  service route, remedy, trust judgment, or political response.
- The small three-, four-, and five-job cells should not be generalized from
  their point estimates.

## Next test

Add monthly income, earnings, employment, SNAP status, and household-change
fields with their official status flags. Then condition the cross-lags on
children, disability, tenure, race, region, and baseline resource band, and
test whether a resource or job transition is followed by a valid food, housing,
utility, care, or assistance outcome. Keep annual hardship fields separate until
their timing can be defended from the SIPP documentation.

## Sources and reproducibility

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [Machine-readable monthly resource/job transition record](../../../records/us-sipp-monthly-resource-job-transition-2024.json)
- [SIPP person-transition reproduction audit](../sipp-person-transition-reproduction-audit-2026-09-14.json)
- [Machine-readable cross-lag record](../../../records/us-sipp-resource-job-crosslag-2024.json)
- [Cross-lag analysis script](../../../../scripts/analyze_sipp_resource_job_crosslag.py)
- [Existing SIPP monthly transition finding](us-household-calendar-integration-021.md)

**Evidence status:** same-person monthly cross-lag with Fay-BRR uncertainty and
explicit timing/unit boundaries; no causal, household, cultural, political, or
geopolitical conclusion is claimed.
