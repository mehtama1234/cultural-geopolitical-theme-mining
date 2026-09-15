# Work limitation changes the relationship between monthly resources and job movement

**Status:** reproducible same-person SIPP cross-lag with Fay-BRR uncertainty · **Checked:** 2026-09-14

## The bounded finding

The 2025 SIPP public-use file supports a same-person monthly comparison of
income-to-poverty-ratio bands and job-count categories, conditioned on whether
the person reports a condition limiting the kind or amount of work they can do.
The two pathways differ:

```text
work-limiting status + monthly resource position
  -> next-month job-count movement

work-limiting status + job count
  -> next-month resource-band movement
  -> possible changes in room, care, food, housing, or benefit security
```

The result is descriptive. It does not identify a health event, employer
decision, accommodation, job quality, pay change, or causal effect.

## Resource band to next-month job-count change

| Resource band at month t | Work-limiting condition | Next-month job-count change | Fay-BRR SE | Approx. 95% interval |
|---|---|---:|---:|---:|
| Below 1× poverty | Yes | 1.07% | 0.21 pp | 0.66–1.47% |
| Below 1× poverty | No | 3.25% | 0.21 pp | 2.84–3.65% |
| 1–1.99× | Yes | 0.97% | 0.14 pp | 0.69–1.24% |
| 1–1.99× | No | 1.91% | 0.13 pp | 1.65–2.17% |
| 2–3.99× | Yes | 1.20% | 0.14 pp | 0.91–1.48% |
| 2–3.99× | No | 1.72% | 0.08 pp | 1.58–1.87% |
| 4× or more | Yes | 1.44% | 0.16 pp | 1.13–1.76% |
| 4× or more | No | 1.64% | 0.06 pp | 1.52–1.75% |

Within the selected pair universes, people reporting a work-limiting condition
show lower job-count movement than those without one at each displayed resource
band. That is a comparison of observed transitions, not evidence that the
condition reduced mobility. Health, age, occupation, household composition,
employer access, and reporting can all contribute.

## Job count to next-month resource-band change

| Job count at month t | Work-limiting condition | Next-month resource-band change | Fay-BRR SE | Approx. 95% interval |
|---|---|---:|---:|---:|
| Zero jobs | Yes | 2.38% | 0.13 pp | 2.13–2.63% |
| Zero jobs | No | 3.24% | 0.13 pp | 3.00–3.49% |
| One job | Yes | 5.27% | 0.35 pp | 4.58–5.96% |
| One job | No | 3.62% | 0.12 pp | 3.38–3.87% |
| Two jobs | Yes | 5.74% | 1.17 pp | 3.45–8.02% |
| Two jobs | No | 4.94% | 0.34 pp | 4.27–5.61% |
| Three or more jobs | Yes | 9.93% | 4.05 pp | 1.99–17.86% |
| Three or more jobs | No | 4.93% | 1.22 pp | 2.54–7.32% |

The reverse path is not monotonic in a simple security direction. Among people
with one or more jobs, resource-band movement is higher in the work-limiting
group, but the three-or-more-job condition cell is sparse and imprecise. A
resource-band change is not necessarily a loss: it can reflect earnings,
transfers, household composition, costs, or movement in either direction.

## What this adds to the end-to-end program

Earlier SIPP layers showed that resource position and job count have distinct
monthly clocks. This pass adds a status moderator: the same observed job or
resource transition can mean different things for people with different work
capacity and alternatives.

It therefore sharpens the next chain:

```text
health or work-limiting condition
  -> accommodation, job access, hours, pay, care, or benefit route
  -> monthly resources and job holding
  -> food, housing, utility, and time trade-offs
  -> recovery, trust, complaint, political judgment, or exit
```

Only the status, resource band, and job-count stages are measured here.

## Counterexamples and limits

- `EDISABL` is a reported work-limiting-condition field, not a diagnosis,
  disability taxonomy, accommodation measure, or discrimination measure.
- Fewer job-count changes can mean stability, constrained access, or missing
  opportunity; the field cannot distinguish them.
- More resource movement after multiple jobs can reflect volatile earnings or
  transfers rather than improved room.
- Person replicate weights support person-level estimates, not household rates.
- Monthly fields are not a dated bill, care onset, employer event, benefit
  notice, remedy, trust judgment, or political action.
- Sparse three-or-more-job condition cells should not be generalized from the
  point estimate.

## Next test

Add monthly earnings, hours, SNAP status, tenure, children, and care/time fields
with documented status flags. Estimate pre-specified transitions within work-
limitation and resource cells, then test whether changes are followed by valid
food, housing, utility, care, or benefit outcomes. A stronger result requires a
dated event or a valid longitudinal design, not just more cross-tabs.

## Reproduction

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP work-limitation/resource reproduction audit](../sipp-work-limitation-resource-job-crosslag-reproduction-audit-2026-09-14.json)
- [Machine-readable record](../../../records/us-sipp-resource-job-worklimitation-crosslag-2024.json)
- [Analysis script](../../../../scripts/analyze_sipp_resource_job_worklimitation_crosslag.py)
- [Related SIPP work-limitation/resource layer](../sipp-fay-brr-disability-children-resource-layer-v1.md)

**Evidence status:** same-person monthly cross-lag with design-based uncertainty;
no causal, household, cultural, political, or geopolitical conclusion is
claimed.
