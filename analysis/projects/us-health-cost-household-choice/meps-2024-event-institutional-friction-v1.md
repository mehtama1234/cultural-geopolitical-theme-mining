# MEPS event channels and institutional friction v1

**Checked:** 2026-09-15  
**Status:** same-round descriptive event-family comparison; no causal claim  
**Machine output:** [event/institutional-friction data](data/us-meps-2024-event-institutional-friction.json)

## Question

Does the association between reported insurance denial or prior-authorization
delay and household health-cost context appear only in one care channel, or
does it remain visible among people with dated office, emergency-room, and
inpatient events?

## Method

The script selects the first dated event per person within each event family,
joins it exactly to HC-256 by `DUPERSID + PANEL`, and compares `EQDENY53=1`
(insurance denied or prior approval delayed) with `EQDENY53=2` (no denial or
delay). Positive `PERWT24F` supplies the descriptive weight. The event date
establishes an observed event-family universe; it does not establish when the
denial occurred relative to that event.

| Event family | Denial/delay n | No denial/delay n | Cost-related care delay | Medical debt | Collector contact | Bill problem |
|---|---:|---:|---:|---:|---:|---:|
| Office | 1,452 | 7,249 | 15.59% vs 5.75% | 24.87% vs 13.34% | 20.35% vs 9.27% | 16.21% vs 5.89% |
| Emergency room | 389 | 1,408 | 18.99% vs 7.67% | 27.10% vs 19.06% | 25.68% vs 15.25% | 25.24% vs 9.16% |
| Inpatient | 201 | 728 | 15.31% vs 5.09% | 26.91% vs 13.86% | 18.79% vs 11.68% | 21.93% vs 5.17% |

Each pair is denial/delay versus no denial/delay. These are weighted shares;
the displayed record counts are unweighted and outcome-specific valid rows
can differ. The pattern remains visible across all three event families, but
the absolute levels differ by event channel and selected universe.

## Interpretation boundary

```text
observed care channel
  + reported institutional friction
  -> different same-round care, debt, collection, and bill context
```

This is a stratified descriptive cross-check, not evidence that a denial
caused the event, delayed care, produced debt, or triggered collection. The
denial field is annual and contains no claim identifier, decision date, appeal,
response, correction, or remedy. Event presence is also selected: people with
no event in a file are outside these event-family rows.

The useful result is persistence of the friction association across care
channels, alongside channel-specific levels. It does not show that the same
claim, bill, or household choice is being followed. The next decisive source
must connect claim-level denial to a dated need, alternative, care decision,
payment obligation, remedy effort, and later household or legitimacy outcome.

## Reproduction

```text
python3 scripts/analyze_meps_event_institutional_friction.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  --office-file /tmp/cgtm-meps-2024/events/h254g.dta \
  --emergency-room-file /tmp/cgtm-meps-2024/events/h254e.dta \
  --inpatient-file /tmp/cgtm-meps-2024/events/h254d.dta \
  --output analysis/projects/us-health-cost-household-choice/data/us-meps-2024-event-institutional-friction.json
```

The output records input hashes and the analyst-script hash. No person-level
identifiers are written to the committed output.
