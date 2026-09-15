# MEPS 2024 round timing does not yet create event follow-up

**Checked:** 2026-09-15  
**Status:** timing audit complete; bounded temporal context only  
**Machine record:** [MEPS round timing audit](data/us-meps-2024-round-timing-audit.json)

## Result

HC-256 has round reference-period end fields for R3/1, R4/2, R5/3, and the
full-year file. These fields can be compared with dated event records, but
they are not a single interview-date clock. R3/1 and R4/2 end in 2024 for
nearly all people, while R5/3 can end in 2025. The full-year reference period
ends in December 2024 for everyone.

All 145,818 office events, 4,351 emergency-room events, and 1,912 inpatient
events have valid event dates and unique event keys. Their person-panel keys
match HC-256 exactly. The round reference dates are also largely available:
98.22% for R3/1, 98.98% for R4/2, 99.16% for R5/3, and 100% for the full-year
endpoint.

## Why this is not a before/after result

Comparing event month with a round endpoint tells us only whether an event
month falls before, in, or after a reference-period boundary. It does not tell
us when the interview occurred, whether the event was the trigger for a later
reported outcome, or whether the round field measures a post-event state.
For example, office events occur both before and after the R4/2 endpoint, but
that does not identify a treatment window; R5/3 often ends after the 2024
event, but its employment and health values still cannot be called recovery.

The full-year endpoint is especially unsuitable for causal ordering: every
2024 event is before or in the same month as December 2024, while the annual
fields summarize the year rather than a post-event period.

## What the audit enables

The round fields can support a carefully labeled temporal-context surface:

```text
dated event
  -> person-panel key
  -> round reference-period boundary
  -> round employment / perceived-health value
```

This can help select candidate cases for a later analysis, preserve the
available timing information, and expose where a valid pre/post design might
exist. It cannot promote `EMPST31`, `EMPST42`, `EMPST53`, or `RTHLTH31/42/53`
to event outcomes without a documented interview or measurement date.

## Next decisive test

The next pass should inspect MEPS documentation and any available round-level
field definitions for interview timing, then test a narrowly defined event
family against a real pre-event and post-event window. If no public-use field
provides that window, the correct finding is that MEPS supports exact event
linkage and annual/round context but not the complete health-cost episode.
The missing stages remain care delay or substitution, alternatives, unpaid
care, work-time or debt response, recovery, remedy, trust, and action.
