# The month after a SNAP transition, resources still move more than jobs or hours

**Status:** Fay–BRR SIPP following-context finding · **Checked:** 2026-09-14

## The bounded finding

Following a reported SNAP entry, the next observed month still showed a lower
household income-to-poverty ratio in 61.8% of 401 valid transition triples. The
corresponding following-month resource decline after reported exit was 69.5%
of 359 valid triples. These are selected descriptive sequences, not estimates
of SNAP effects or benefit adequacy.

The work measures moved on different clocks. Following entry, job count was
unchanged in 91.9% of 284 valid triples and average hours were unchanged in
79.4% of 108. Following exit, job count was unchanged in 97.2% of 264 and
hours in 94.5% of 122. Person earnings were more mixed: after entry, 32.3%
declined and 45.5% rose among 108 valid triples; after exit, 37.0% declined
and 46.1% rose among 122.

## Direct evidence

| SNAP transition at t → t+1 | Following measure | Down | Same | Up | Valid triples |
|---|---|---:|---:|---:|---:|
| No → Yes | Household resource ratio | 61.78% | 18.28% | 19.94% | 401 |
| No → Yes | Person earnings | 32.30% | 22.20% | 45.50% | 108 |
| No → Yes | Average hours | 12.29% | 79.40% | 8.31% | 108 |
| No → Yes | Job count | 5.86% | 91.89% | 2.25% | 284 |
| Yes → No | Household resource ratio | 69.46% | 10.91% | 19.63% | 359 |
| Yes → No | Person earnings | 37.02% | 16.86% | 46.13% | 122 |
| Yes → No | Average hours | 2.18% | 94.50% | 3.32% | 122 |
| Yes → No | Job count | 0.86% | 97.23% | 1.91% | 264 |

Resource intervals have Fay–BRR standard errors of roughly 3.8–5.0 percentage
points; earnings intervals are roughly 3.8–5.7 points; hours and job-count
intervals are smaller in some cells but retain selected-universe limits.

## What this adds

```text
SNAP transition
  -> following month
  -> household resources, earnings, hours, and job count diverge
  -> recovery, adequacy, notice, effort, trust, and action remain open
```

The following month makes the timing safeguard stronger. A lower resource ratio
can persist after entry or exit even when job count and hours are unchanged.
Conversely, earnings can rise without a corresponding resource recovery. This
is why “exit to work” and “receipt restored security” are both too simple for
these records.

## Limits and counterexamples

- The unit is an identified person and adjacent three-month sequence, not a
  household benefit spell or same-case administrative episode.
- `THINCPOV` is a household income-to-poverty ratio; `TPEARN` is person
  earnings; `TMWKHRS` is average weekly hours among job holders; `RMNUMJOBS`
  is a person job count. Their valid denominators differ.
- A following-month decline can precede the transition, reflect timing,
  household composition, reporting, renewal, or another shock.
- Stable jobs or hours can coexist with lower pay, worse schedules, poor work
  quality, or worsening food/housing security.
- Rising earnings after exit can reflect a partial or temporary change and is
  not restored household security.
- The design does not observe notice, application or renewal effort, benefit
  amount, appeal/correction, care, food, health, trust, or political action.

## Next test

Link this three-month backbone to an administrative or same-episode ledger that
records notice timing, effort, decision, amount, interruption, remedy, food and
housing result, care/time loss, perceived fairness, trust, later recovery, and
political action. Preserve counterexamples where resources improve without
receipt, receipt ends without recovery, or stable work coexists with hardship.

## Sources and reproduction

- [SIPP SNAP transition context layer](../sipp-snap-transition-context-fay-brr-layer-v1.md)
- [Machine-readable following-context record](../../../records/us-sipp-snap-following-resource-work-context-2024.json)
- [Following-context reproduction audit](../sipp-snap-following-context-reproduction-audit-2026-09-14.json)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

**Evidence status:** three-month same-person descriptive sequences with Fay–BRR
uncertainty; no causal, adequacy, recovery, cultural, political, or geopolitical
conclusion is claimed.
