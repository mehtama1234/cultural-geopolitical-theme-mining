# SIPP SNAP transition × recorded reason layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file, 2024 reference year  
**Unit:** identified person, adjacent reference-month pair  
**Weight:** `WPFINWGT` from the first month of each pair  
**Method:** weighted descriptive transition/reason comparison; no replicate-weight variance estimate

This layer connects the monthly SNAP transition result to the reason recorded
on the relevant owner record. For a no-to-yes transition, it reads the start
reason on the new receipt month; for a yes-to-no transition, it reads the end
reason on the last receipt month. It is a mechanism-oriented descriptive
layer, not a causal estimate.

## Coverage

| Transition | Valid transitions | Transitions with a recorded reason |
|---|---:|---:|
| No → Yes | 437 | 217 (49.7%) |
| Yes → No | 387 | 188 (48.6%) |

The reason distributions below use only the transitions with a valid recorded
reason, not all transitions.

## Entry reasons among classified entries

| Recorded reason | Weighted share |
|---|---:|
| Job loss/layoff or wages reduced | 30.10% |
| Other | 23.33% |
| Loss or reduction of other income | 15.72% |
| Became disabled or otherwise unable to work | 10.67% |
| New child/dependent or pregnancy | 6.41% |
| No change—decided it was time | 6.01% |
| No change—heard about the program | 3.49% |
| Needed to recertify | 3.21% |
| Separation, divorce, or widowhood | 1.05% |

## Exit reasons among classified exits

| Recorded reason | Weighted share |
|---|---:|
| Other | 49.53% |
| Ineligible because income increased | 32.40% |
| Time limit reached | 6.21% |
| Ineligible because of family changes | 3.67% |
| Requirements not met | 3.52% |
| Still eligible but could not/chose not to collect | 2.53% |
| Benefits not worth the trouble | 2.15% |

## What this adds

The transition-aligned records give entry and exit different social meanings.
Among classified entries, job loss or reduced wages is the largest named
reason. Among classified exits, increased income is the largest named reason,
but “other” is larger and nearly half of the classified weighted exits. The
result therefore supports a more precise event-ledger rule: entry and exit
must be classified before they are interpreted as improvement, failure,
administrative loss, or choice.

The reason coverage is only about half of the observed transitions. The
classified cases may differ systematically from unclassified cases, and the
recorded reason does not reveal the notice, documents, effort, appeal, benefit
amount, or household outcome. It also does not prove that the cited event was
the sole cause of the transition.

## Context check

The transition-aligned reason script also groups events by child presence and
resource band. The variation is a useful hypothesis signal, not a precise
subgroup estimate:

| Context | No → Yes transitions | Classified entries | Job-loss share among classified entries | Yes → No transitions | Classified exits | Income-increase share among classified exits |
|---|---:|---:|---:|---:|---:|---:|
| No children, below 1.00x | 47 | 40 | 47.1% | 31 | 29 | 10.5% |
| Children present, below 1.00x | 96 | 24 | 14.5% | 35 | 8 | 21.8% |
| No children, 1.00–1.99x | 45 | 39 | 17.4% | 38 | 27 | 55.9% |
| Children present, 1.00–1.99x | 77 | 22 | 20.8% | 78 | 27 | 40.6% |
| No children, 2.00–3.99x | 42 | 36 | 36.9% | 37 | 29 | 41.3% |
| Children present, 2.00–3.99x | 79 | 27 | 41.0% | 93 | 26 | 39.2% |

These differences could reflect transition composition, measurement coverage,
work and family changes, or actual institutional processes. The run does not
estimate subgroup standard errors and should not be used to rank contexts. It
does establish which comparisons a larger, reason-complete event design should
pre-register.

## Verification and limits

- 379,215 primary person-month rows were read.
- 31,992 people were identified; 31,090 had all twelve reference months.
- There were 346,283 valid adjacent-month SNAP pairs in the transition run,
  including 437 no-to-yes and 387 yes-to-no transitions.
- Reasons were restricted to the person identified by `ESNAP_OWN = PNUM` and
  to nonblank valid status-coded reason fields.
- The weights come from the first month of each pair. No Fay-BRR variance was
  estimated for these reason distributions.
- The public-use fields do not provide the complete administrative episode:
  application, notice, channel, renewal effort, decision timing, appeal,
  benefit amount, food outcome, work outcome, health, debt, trust, or politics
  after the transition remain open.

## Reproduction

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_snap_transition_reasons.py
```

The raw files, derived CSV, and JSON output are not committed. The calculation
output was `/tmp/us-broad-sipp-2025/full-v13/sipp-snap-transition-reasons-v3.json`.

## Next test

Use resource band, child presence, race, disability, work status, and food
security at the transition to compare classified and unclassified events.
Then add the SIPP spell start/end fields and reason categories to a design that
can observe notice, burden, interruption, and re-entry over time.

Related records: [SIPP SNAP reason layer](sipp-snap-reason-layer-v1.md),
[SIPP SNAP transition layer](sipp-snap-transition-layer-v1.md),
[SIPP SNAP × food-security layer](sipp-snap-food-security-layer-v1.md),
and [safety-net event ledger](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md).
