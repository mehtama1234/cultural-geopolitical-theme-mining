# Institutional friction persists across MEPS care channels

## The finding

The MEPS 2024 person file contains an annual indicator of whether insurance
denied or delayed prior approval (`EQDENY53`). When people with a first dated
office, emergency-room, or inpatient event are stratified by that indicator,
the association with care delay, medical debt, and bill problems remains
visible in every event family.

| First event family | Denial/delay n | No denial/delay n | Care delay | Medical debt | Bill problem |
|---|---:|---:|---:|---:|---:|
| Office | 1,452 | 7,249 | 15.59% vs 5.75% | 24.87% vs 13.34% | 16.21% vs 5.89% |
| Emergency room | 389 | 1,408 | 18.99% vs 7.67% | 27.10% vs 19.06% | 25.24% vs 9.16% |
| Inpatient | 201 | 728 | 15.31% vs 5.09% | 26.91% vs 13.86% | 21.93% vs 5.17% |

Each pair is denial/delay versus no denial/delay. Percentages are weighted
shares; counts are unweighted and outcome-specific valid rows can differ.
Debt-collector contact follows the same direction: 20.35% versus 9.27% for
office, 25.68% versus 15.25% for ER, and 18.79% versus 11.68% for inpatient.

The contrast also survives a private-coverage check. Among privately covered
first-event people, care delay was 15.79% versus 6.01% for office events,
23.77% versus 8.67% for ER events, and 15.41% versus 4.39% for inpatient
events, comparing denial/delay with no denial/delay. Medical debt was
25.01% versus 14.18%, 31.09% versus 22.22%, and 30.31% versus 16.66% in the
same three channels. This is a practical-room robustness screen, not a plan-
adequacy or insurance effect estimate. Uninsured friction cells are small and
are not interpreted as stable subgroup estimates.

## What this adds

```text
observed care channel
  + reported denial or prior-authorization delay
  -> different same-round care, debt, collection, and bill context
```

The persistence across channels makes the institutional-friction signal less
dependent on one utilization family. The levels still differ: ER respondents
with denial/delay have the highest bill-problem share, while inpatient and
office groups show different debt and collection surfaces. Channel is therefore
part of the practical burden context, not merely a control label.

## Boundary

This is a descriptive cross-check, not a causal claim. `EQDENY53` is annual and
does not identify the claim, decision date, appeal, response, correction, or
resolution. It is not shown to precede the observed event. Event presence is
selected, and the outcomes are same-round context rather than post-event
effects. A denial may be a marker of complex care or prior severity rather than
the source of the later context.

Coverage and financial-room intersections do not solve those boundaries. The
annual coverage field is not plan generosity, and confidence paying an
unexpected expense is not liquid cash or deductible exposure.

The result does not connect one claim to a care decision, available alternative,
amount owed, payment timing, household substitution, remedy, trust, political
action, or exit. The next decisive test remains a claim- or case-level ledger
with dates for denial, appeal, response, payment, care completion, and later
household and institutional outcomes.

## Reproduction

See the [method note](../meps-2024-event-institutional-friction-v1.md),
[machine output](../data/us-meps-2024-event-institutional-friction.json), and
[canonical trend record](../../../records/us-meps-2024-event-institutional-friction.json).
The analysis uses the AHRQ HC-256 person file, HC-254 event files, exact
`DUPERSID + PANEL` linkage, positive `PERWT24F`, and the script
`scripts/analyze_meps_event_institutional_friction.py`.

## Reading rule

Read the cross-channel persistence as evidence of a recurring institutional-
friction association, not as proof that a denial caused a household loss or
that a remedy failed. Keep claim timing and response unobserved.
