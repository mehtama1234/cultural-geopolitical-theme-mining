# MEPS 2024 first-event ledger joins payment to bounded round context

**Checked:** 2026-09-15  
**Status:** weighted descriptive episode screen; no causal claim  
**Machine record:** [bounded episode ledger](data/us-meps-2024-bounded-episode-ledger.json)

## Result

The first valid dated office, emergency-room, or inpatient event for each
person/event family can be joined exactly to HC-256 payment, insurance,
employment, perceived-health, and medical-bill-problem fields. This creates a
more useful bounded episode screen than either event payment or annual health
context alone. It still does not identify the triggering need, care decision,
available alternative, debt, unpaid care, or remedy.

The extract keeps one first event per person within each event family. This
prevents people with many encounters from being counted as many independent
persons, while retaining separate event-family universes. Event months are
classified against the R4/2 reference-period endpoint as before, the same
month, or after. The after group is not a post-event outcome group: it is an
event that occurs after the R4/2 reference boundary.

## First-event summaries

| Event family / timing | First-event people | Self/family payment mean | Zero self/family payment | Fair/poor health baseline → follow-up | Bill problem at follow-up |
|---|---:|---:|---:|---:|---:|
| Office, before R4/2 | 12,865 | $65.41 | 48.52% | 13.74% → 12.22% | 7.73% |
| Office, same month | 506 | $38.80 | 64.52% | 10.03% → 8.66% | 4.42% |
| Office, after R4/2 | 614 | $64.04 | 61.29% | 6.79% → 5.57% | 6.26% |
| Emergency room, before R4/2 | 2,128 | $148.87 | 73.06% | 27.49% → 26.15% | 14.40% |
| Emergency room, same month | 204 | $104.23 | 71.61% | 21.26% → 19.59% | 14.73% |
| Emergency room, after R4/2 | 340 | $90.58 | 71.80% | 19.27% → 14.47% | 6.44% |
| Inpatient, before R4/2 | 988 | $838.09 | 68.95% | 35.36% → 33.80% | 11.87% |
| Inpatient, same month | 101 | $597.26 | 67.36% | 27.82% → 36.92% | 9.89% |
| Inpatient, after R4/2 | 226 | $796.48 | 66.31% | 20.30% → 24.09% | 3.91% |

All payment means are weighted by the event/person `PERWT24F` after the
positive-weight and valid-date/payment filters. The health, employment, and
bill-problem percentages are weighted descriptive context. No standard error
is reported by this screen, and the rows are not adjusted for severity,
coverage design, age, access, or prior health.

## What this closes

```text
first observed event
  -> exact person-panel identity
  -> self/family payment
  -> month-level relation to R4/2
  -> baseline/follow-up health and employment context
  -> follow-up bill-problem context
```

The result makes two boundaries more visible. First, acute events are
associated with a different health and employment context even before any
possible follow-up comparison; this is selection, not an event effect.
Second, payment and bill-problem context do not move monotonically across
timing groups. A zero self/family payment can coexist with illness, time,
transport, premiums, deductibles, or unpaid-care burden, while a positive
payment does not establish unaffordability or a later household sacrifice.

The same-month rows are retained for completeness but are intrinsically
ambiguous because public-use data provide month-level, not day-level,
ordering. The after rows are useful for describing the event surface but
cannot be interpreted as a recovery or post-event outcome.

## What remains open

This ledger still does not observe whether care was sought, delayed,
substituted, or forgone; what alternative was available; how the household
paid; whether work, food, housing, or unpaid care changed; whether treatment
continued; or whether a provider, insurer, employer, regulator, or court
responded. It also does not observe trust, switching, political action, or
geopolitical consequence. The first event may be a consequence of a prior
need rather than the beginning of the episode.

The strongest safe interpretation is therefore:

```text
pre-existing person context
  -> first observed care event and payment channel
  -> bounded month-level context around R4/2
```

It is not:

```text
medical bill -> household choice -> sacrificed outcome -> recovery
```

## Reproduction and next test

Reproduce the aggregate artifact with:

```text
python3 scripts/analyze_meps_bounded_episode_ledger.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  --office-file /tmp/cgtm-meps-2024/events/h254g.dta \
  --emergency-room-file /tmp/cgtm-meps-2024/events/h254e.dta \
  --inpatient-file /tmp/cgtm-meps-2024/events/h254d.dta \
  --output analysis/projects/us-health-cost-household-choice/data/us-meps-2024-bounded-episode-ledger.json
```

The next decisive acquisition remains a same-unit need/bill and choice
measure: a dated reason for seeking or not seeking care, alternatives,
amount owed and payment timing, and a household money/time response. Until
those fields are linked, the ledger should be used as a bounded bridge to the
SHED care-foregoing and adaptation layers, not as a completed affordability
or recovery result.

## Source and method boundary

The person and event files are the AHRQ [MEPS 2024 HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256), [office file HC-254G](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254G&prfricon=yes), [emergency-room file HC-254E](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254E&prfricon=yes), and [inpatient file HC-254D](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254D&prfricon=yes). Exact linkage uses `DUPERSID + PANEL`; event payment uses the event-family self/family payment field; timing uses event month against `ENDRFY42`/`ENDRFM42`.
