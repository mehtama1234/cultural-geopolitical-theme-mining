# SNAP transition reasons point to work and income pressure, but do not close the route

**Status:** reproducible Fay–BRR SIPP reason layer · **Checked:** 2026-09-14

## The bounded finding

The 2025 SIPP public-use file supports a reason-aligned view of adjacent-month
SNAP transitions. Among classified entries, the largest named reason was job
loss, layoff, or reduced wages: **30.10%** (SE 3.94; 95% CI 22.38–37.83; 57
classified pairs). Other income loss or reduction accounted for **15.72%**
(SE 3.13), and becoming disabled or unable to work accounted for **10.67%**
(SE 2.56). The entry denominator was 217 classified pairs out of 437 observed
no-to-yes transitions.

Among classified exits, **32.40%** (SE 4.26; 95% CI 24.04–40.75; 63 pairs)
reported income increased and ineligibility. Nearly half, **49.53%** (SE 4.34;
88 pairs), were recorded as `other`. The exit denominator was 188 classified
pairs out of 387 observed yes-to-no transitions.

## What this adds to the end-to-end program

This strengthens the route from public-system status to reported material and
work context:

```text
monthly SNAP transition
  -> recorded reason category
  -> resource, earnings, hours, job-count, hardship, and care context
  -> later security, interpretation, or action
```

The first two stages are now better resolved, but they are still not a same-
episode causal chain. The reason fields are not administrative case records,
and the resource/work fields have separate valid universes. The “other” share
also shows why a clean story about entry or exit would overstate what the data
measure.

## Limits and counterexamples

- A reported job-loss or wage-reduction reason does not identify the employer,
  date, hours change, benefit amount, or whether SNAP prevented hardship.
- Income-increase/ineligibility is not proof of restored household security;
  the following-context layer still finds resource declines after many exits.
- Requirements, time limits, and “benefits not worth the trouble” are distinct
  recorded categories, but this layer does not observe notice quality, effort,
  appeal, remedy, or administrative responsibility.
- Entry and exit reasons use different response taxonomies and are not symmetric
  outcomes.
- Only 217 of 437 entry pairs and 188 of 387 exit pairs had classified reasons;
  unclassified transitions are not folded into `other`.

## Reproduction and sources

- [Machine-readable reason record](../../../records/us-sipp-snap-transition-reasons-2024.json)
- [Reason-layer methodology](../sipp-snap-transition-reason-layer-v1.md)
- [Reproduction audit](../sipp-snap-transition-reasons-reproduction-audit-2026-09-14.json)
- [SIPP transition context](../findings/us-safety-net-access-007.md)
- [Census SIPP 2025 public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)

The estimates use `WPFINWGT` and 240 replicate weights with Fay factor 0.5.
They are descriptive and do not establish SNAP effects, restored security,
trust, political action, or geopolitical consequence.
