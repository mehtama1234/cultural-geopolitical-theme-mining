# Finding 030: Earnings change is not earnings gain, and hours change is not hours loss

**Status:** reproducible same-person SIPP directional cross-lag · **Checked:** 2026-09-14

## The bounded finding

The prior SIPP cross-lag counted whether earnings or average weekly hours
changed between adjacent months. That was useful but incomplete: a change can
be an increase, decrease, or no change. The directional rerun preserves the
same person key, monthly timing, four resource bands, reported work-limiting
status, and 240-replicate Fay-BRR variance procedure.

Among people reporting a work-limiting condition at month *t*:

| Resource band at *t* | Earnings increase | Earnings decrease | Earnings same | Hours increase | Hours decrease | Hours same |
|---|---:|---:|---:|---:|---:|---:|
| Below 1× poverty | 37.4% | 29.3% | 33.3% | 9.4% | 7.4% | 83.1% |
| 1–1.99× | 36.2% | 35.1% | 28.7% | 4.5% | 5.5% | 90.0% |
| 2–3.99× | 40.3% | 39.8% | 19.9% | 4.4% | 4.9% | 90.7% |
| 4× or more | 41.5% | 44.1% | 14.4% | 2.6% | 5.0% | 92.4% |

For people not reporting a work-limiting condition, the corresponding below-1×
and 4×-or-more cells are:

| Resource band at *t* | Earnings increase | Earnings decrease | Earnings same | Hours increase | Hours decrease | Hours same |
|---|---:|---:|---:|---:|---:|---:|
| Below 1× poverty | 33.3% | 28.0% | 38.7% | 7.6% | 4.4% | 87.9% |
| 4× or more | 43.4% | 42.8% | 13.8% | 1.8% | 2.5% | 95.7% |

The defensible synthesis is: **hours are usually unchanged in the adjacent
month, while earnings movement is more common and can point in either
direction; work-limitation and resource position alter the distribution of
those directions.** This is a sharper description of household/work
instability, not a welfare or causal estimate.

## What this changes from the prior result

The earlier record showed that hours-change shares were higher in lower-resource
and work-limiting cells. The directional result shows why that should not be
called “hours loss”: in the below-1× work-limiting cell, hours increased 9.4%,
decreased 7.4%, and stayed the same 83.1%. At 4× or more, decreases exceeded
increases among work-limited people, but that still does not reveal whether a
reduction was desired, accommodated, or forced.

The earnings surface is different. Among work-limited people at 4× or more,
earnings decreased in 44.1% of valid pairs and increased in 41.5%; among the
below-1× group, increases exceeded decreases. This is not a simple resource
security gradient: earnings levels, jobs, hours, composition, and reporting can
move together in different ways.

## Units and uncertainty

The work-limiting observation contains 11,196 valid earnings pairs and a
separate 11,548-pair hours universe. The no-limitation observation contains
153,759 valid earnings pairs and a separate 154,992-pair hours universe. Each
direction category uses the relevant outcome universe; categories should not
be read as if they share a denominator across earnings and hours.

The person key is `SSUID + SPANEL + SWAVE + PNUM + MONTHCODE`. The month-*t*
`WPFINWGT` weights each adjacent pair, and `REPWGT1` through `REPWGT240` are
used with Census Fay BRR (`G = 240`, perturbation factor `0.5`). These are
person-record transitions, not household prevalence estimates.

## End-to-end implication

```text
resource position + work-limiting status
  -> earnings direction and hours direction
  -> food, housing, utilities, care, and time room
  -> recovery, accommodation, institutional judgment, trust, or action
```

The new result closes only the direction of one middle transition. It still
does not observe the bill, health event, employer decision, care substitution,
desired schedule, benefit notice, remedy, or later meaning/action.

## Counterexamples kept visible

- An earnings increase can reflect more hours, a second job, overtime, or a
  temporary payment rather than improved security.
- An earnings decrease can reflect fewer hours, job exit, timing, reporting, or
  a chosen reduction with adequate support.
- Unchanged hours can coexist with changing pay, prices, care demands, health,
  or job quality.
- More hours can be an opportunity or a constraint; fewer hours can be relief or
  involuntary loss.
- `EDISABL` is a reported work-limiting-condition field, not a diagnosis,
  accommodation, discrimination, or preference measure.

## Next test

The next SIPP pass should condition directional transitions on children, tenure,
SNAP state, food/housing/utility fields, and documented care/work status flags,
then follow a valid transition to a later material or assistance outcome. A
stronger end-to-end result still requires a dated health, employer, bill, or
administrative event and a later recovery, trust, or action measure.

## Reproduction and sources

- [Directional machine-readable record](../../../records/us-sipp-resource-worklimitation-direction-2024.json)
- [Directional analysis script](../../../../scripts/analyze_sipp_resource_worklimitation_direction.py)
- [Prior hours/earnings cross-lag](../../../records/us-sipp-resource-worklimitation-hours-earnings-crosslag-2024.json)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

**Evidence status:** same-person monthly directional cross-lag with design-based
uncertainty; no causal, household, cultural, political, or geopolitical
conclusion is claimed.
