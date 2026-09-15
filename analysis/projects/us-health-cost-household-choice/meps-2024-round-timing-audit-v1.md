# MEPS 2024 round timing does not yet create event follow-up

**Checked:** 2026-09-15  
**Status:** timing audit complete; bounded temporal context only  
**Machine record:** [MEPS round timing audit](data/us-meps-2024-round-timing-audit.json)

**Official timing reference:** [AHRQ HC-256 documentation](https://meps.ahrq.gov/data_stats/download_data/pufs/h256/h256doc.shtml)

## Result

HC-256 has round reference-period end fields for R3/1, R4/2, R5/3, and the
full-year file. AHRQ states that, for most sample members, the round interview
date is the reference-period end date. The public-use file supplies only
month/year, and AHRQ notes exceptions for people who died, left the reporting
unit, became institutionalized, joined the military, or had a confidentiality
recoding. R3/1 and R4/2 end in 2024 for nearly all people, while R5/3 can end
in 2025. The full-year reference period ends in December 2024 for everyone.

All 145,818 office events, 4,351 emergency-room events, and 1,912 inpatient
events have valid event dates and unique event keys. Their person-panel keys
match HC-256 exactly. The round reference dates are also largely available:
98.22% for R3/1, 98.98% for R4/2, 99.16% for R5/3, and 100% for the full-year
endpoint.

## What timing can and cannot establish

For most people, comparing event month with a round endpoint gives a bounded
month-level ordering. It does not reveal the interview day, and a same-month
event and endpoint may occur in either order. It also does not show whether the
event was the trigger for a later reported outcome or whether a round field
summarizes a post-event state.
For example, office events occur both before and after the R4/2 endpoint, but
that does not identify a treatment window; R5/3 often ends after the 2024
event, but its employment and health values still cannot be called recovery.

The full-year endpoint is especially unsuitable for causal ordering: every
2024 event is before or in the same month as December 2024, while the annual
fields summarize the year rather than a post-event period.

## What the audit enables

The round fields can support a carefully labeled month-ordered candidate
surface:

```text
dated event month
  -> person-panel key
  -> month-level round reference-period boundary
  -> round employment / perceived-health value
```

This can help select candidate cases for a later analysis, preserve the
available timing information, and expose where a valid pre/post design might
exist. It can support a month-ordered descriptive transition analysis for the
majority of records, with same-month and exceptional cases flagged. It cannot
promote `EMPST31`, `EMPST42`, `EMPST53`, or `RTHLTH31/42/53` to exact event
outcomes or causal recovery measures.

## Next decisive test

The next pass should use the documented month-level ordering for one event
family, flag same-month and exceptional cases, and compare round employment or
health status only as a descriptive transition. If a stronger day-level or
event-trigger design is required, the correct finding is that MEPS supports
exact event linkage and month-level round context but not the complete
health-cost episode. The missing stages remain care delay or substitution,
alternatives, unpaid care, work-time or debt response, recovery, remedy, trust,
and action.
