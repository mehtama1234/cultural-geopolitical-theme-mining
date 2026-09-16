# Housing tenure changes the monthly transition surface under work limitation

**Status:** corrected-v18 same-person SIPP conditioning finding · **Checked:** 2026-09-15

## The bounded finding

The corrected 2025 SIPP slice supports a same-person monthly comparison of
resource-band and job-count changes, conditioning on both first-month housing
tenure and a reported work-limiting condition. Tenure changes the transition
surface more clearly in the reverse direction than in low-resource job-count
movement.

| Transition | Owned/bought | Rented |
|---|---:|---:|
| Below 1× poverty → next-month job-count change | 1.11% (SE 0.25), n=3,920 | 0.95% (0.22), n=5,704 |
| 4× poverty or more → next-month job-count change | 1.45% (0.18), n=13,350 | 1.39% (0.31), n=2,542 |
| One job → next-month resource-band change | 4.77% (0.41), n=7,194 | 6.12% (0.58), n=3,485 |
| Two jobs → next-month resource-band change | 3.53% (0.93), n=495 | 7.37% (1.94), n=327 |

Among work-limited respondents, owner/renter job-count movement is close at
both displayed resource endpoints. In contrast, renters with one or two jobs
show higher point estimates for next-month resource-band movement. The two-job
cells are small, so they are a watchpoint rather than a stable ranking.

The result does not identify a housing-tenure effect. Tenure is entangled with
income, mortgage and repair obligations, local prices, household composition,
health, job access, and selection into housing arrangements. A resource-band
change also has no direction here: it may be an improvement, deterioration, or
crossing caused by a transfer or reporting change.

## What this adds to the end-to-end chain

```text
tenure and work-limiting status
  -> monthly resource/job transition
  -> possible room for care, consumption, and bill payment
  -> later health, work, institutional, or political consequence
```

This closes another conditioning segment in the material/time/care lane. It
still does not observe a dated bill, care need, employer decision,
accommodation, protected or sacrificed outcome, remedy, trust judgment, or
recovery.

## Counterexamples and limits

- Similar job-count movement across owner and renter cells shows why tenure
  should not be treated as a universal explanation of job instability.
- Higher resource-band movement among renters with one or two jobs does not
  prove greater hardship or opportunity.
- Rent-free households were retained in the full machine output but are not
  interpreted here because their housing arrangements are heterogeneous and
  their work-limited cells are small.
- Person-record weights support person transitions, not household prevalence.
- The official `ATENURE` universe flag was required and was nonmissing on all
  379,215 rows in the corrected slice.

## Reproduction

```text
python3 scripts/analyze_sipp_resource_job_worklimitation_tenure_crosslag.py \
  --primary /tmp/us-broad-sipp-2025/full-v18/sipp-household-slice.csv \
  --replicate-zip /tmp/rw2025_csv.zip \
  --output /tmp/us-broad-sipp-2025/full-v18/resource-job-worklimitation-tenure-crosslag.json
```

- [Machine-readable record](../../../records/us-sipp-resource-job-worklimitation-tenure-crosslag-2024.json)
- [Analysis script](../../../../scripts/analyze_sipp_resource_job_worklimitation_tenure_crosslag.py)
- [Unconditioned work-limitation finding](us-household-calendar-integration-039.md)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)

**Evidence status:** same-person monthly cross-lag with Fay-BRR uncertainty;
descriptive and selection-sensitive, with no causal, household, cultural,
political, or geopolitical conclusion.
