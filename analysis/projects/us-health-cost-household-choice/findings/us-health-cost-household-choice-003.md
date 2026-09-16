# Finding 003: Acute MEPS events remain selected before the later bill and health surface

**Status:** month-ordered descriptive transition record · **Checked:** 2026-09-15

## Bounded result

The MEPS 2024 public-use files support a strict month-ordering screen. A
person's first emergency-room or inpatient event is required to fall after
that person's R3/1 reference-period endpoint and before the R4/2 endpoint.
Same-month boundary cases are excluded. The event-window groups already had
worse health before the event, and they retained higher R4/2 fair/poor health,
health worsening, and medical-bill problems afterward.

| First event in the inter-round window | Baseline fair/poor health | R4/2 fair/poor health | Health worsened | R4/2 bill problem |
|---|---:|---:|---:|---:|
| Emergency-room event | 24.29% | 27.05% | 29.02% | 15.14% |
| No emergency-room event in window | 11.01% | 9.66% | 21.92% | 7.19% |
| Inpatient event | 28.99% | 33.67% | 31.42% | 11.13% |
| No inpatient event in window | 11.27% | 10.00% | 22.06% | 7.52% |

The office-event layer is a counterexample: baseline fair/poor health was
9.34% in the event group and 12.19% in the no-event group, while follow-up
fair/poor health was 9.26% and 10.84%; follow-up bill-problem shares were
8.01% and 7.52%. Utilization therefore does not map to one universal burden
gradient.

## What the timing screen establishes

~~~text
pre-existing health/work selection
  -> month-ordered observed care event
  -> different later health, employment, and bill context
~~~

The baseline comparison is the important result. It prevents the later
contrast from being described as an event effect. A utilization event can mark
prior need, severity, age, coverage, access, or employment selection.

## What remains open

The MEPS public-use linkage still does not identify the triggering need or
bill, the feasible alternative, care delay or abandonment, borrowing or
savings use, unpaid care, work-time trade-off, recovery from the episode,
verified institutional remedy, trust, switching, or political action.
Month-level ordering is stronger than an unconditioned annual cross-tab but
is not day-level ordering.

The next decisive join is an episode record containing a dated obligation or
need, payment timing, care decision, alternative, protected and sacrificed
household outcome, and follow-up remedy or recovery. This record should remain
a bounded MEPS layer while SHED, SIPP, PSID, UAS, or administrative sources
address the missing household-choice stages.

## Reproduction

- [Canonical machine record](../../../records/us-meps-2024-between-round-event-transitions.json)
- [MEPS inter-round machine output](../data/us-meps-2024-between-round-event-transitions.json)
- [Method note](../meps-2024-between-round-event-transitions-v1.md)
- [Analysis script](../../../../scripts/analyze_meps_between_round_event_transitions.py)
- [AHRQ MEPS HC-256 download page](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256)

**Evidence status:** same-person month-ordered descriptive comparison with
baseline selection explicitly shown; no causal, household-adaptation,
legitimacy, political, or geopolitical conclusion is claimed.
