# Broad AI-work headlines are not simple sums of detailed task rates

**Status:** provisional consistency finding · **Checked:** 2026-09-13

## The bounded finding

The NBER W35677 public release contains both detailed task (DWA) rates and
broad work-activity (BWA) rates. After a versioned, transparent O*NET-prefix
mapping, the broad rates do not reproduce as simple observation-weighted means
of the displayed detailed rates. Eight of nine broad categories have higher
NBER-linked DWA aggregates than the BWA rate; physical/manual work is slightly
lower. This is evidence that the aggregation layer is a distinct measurement
object, not a reason to choose one rate as the “real” adoption rate.

## Diagnostic comparison

| NBER broad category | BWA rate | DWA displayed-rate weighted mean | Difference |
|---|---:|---:|---:|
| Reasoning and Decision Making | 30.0% | 34.411% | +4.411 pp |
| Information and Data Processing | 27.0% | 31.358% | +4.358 pp |
| Coordinating, Developing, Managing, and Advising | 24.2% | 27.903% | +3.703 pp |
| Performing Complex and Technical Activities | 24.0% | 28.965% | +4.965 pp |
| Looking for and Receiving Job-Related Information | 18.3% | 19.900% | +1.600 pp |
| Communicating and Interacting | 17.7% | 20.333% | +2.633 pp |
| Identifying and Evaluating Job-Relevant Information | 15.0% | 17.230% | +2.230 pp |
| Administering | 14.8% | 15.731% | +0.931 pp |
| Performing Physical and Manual Work Activities | 9.6% | 9.085% | −0.515 pp |

The [machine-readable diagnostic](../data/nber-bwa-dwa-consistency-audit-2026-09-13.json)
preserves the detailed-row counts, unweighted observation totals, source
hashes, and calculation method. The [historical provisional crosswalk](../data/nber-onet-provisional-label-crosswalk-2026-09-13.json)
has been superseded for current reproduction by the [acquired-input crosswalk](../data/onet-nber-crosswalk-2026-09-14/provisional-label-crosswalk.json)
and [identifier audit](../data/onet-nber-crosswalk-2026-09-14/onet-nber-identifier-reconciliation-audit-2026-09-14.json).
records how the prefix membership was established.

## What this does and does not show

The calculation uses the NBER-displayed DWA adoption rates, weights each by its
displayed unweighted observation count, groups tasks by O*NET GWA prefix, and
compares the result with NBER’s directly displayed BWA rate. It is a
reproducibility diagnostic. It does not recreate the NBER estimator, because
the two levels may use different valid universes, missingness, weights,
respondent-task structures, or aggregation rules.

The result therefore supports a measurement conclusion: broad-category rates
should not be treated as mechanically interchangeable with detailed-task
aggregates. A difference also does not imply a data error, bias, productivity
change, or difference in workplace control.

## Evidence chain

```text
task labels and taxonomy
  -> detailed adoption rates
  -> broad aggregation rule and valid universe
  -> headline category rate
  -> interpretation of which work is changing
  -> claims about worker control, pay, security, or political meaning
```

Only the first four stages are examined here. The final interpretive arrows
remain open and require worker/workplace evidence.

## Counterinterpretations

- The apparent differences may be produced by different weighting or missing-
  data rules rather than substantive aggregation choices.
- A DWA prefix grouping may not reproduce the NBER authors’ broad-category
  construction even when the identifiers are hierarchically related.
- Displayed DWA rates may have different task-level universes from the BWA
  denominator.
- Adoption is not productivity, discretion, employer permission, bargaining
  power, or worker benefit.

## Next test

Obtain the underlying documentation or code that defines the NBER BWA
aggregation and compare it with the public index. Then, if worker-level data
become available, reproduce both levels from the same records with identical
weights, missingness rules, and task universes before making subgroup or
occupation comparisons.

**Evidence status:** public DWA/BWA consistency diagnostic completed; estimator
reproduction, worker-level determinants, and downstream workplace and social
outcomes remain open.

## Sources

- [NBER Working Paper 35677](https://www.nber.org/papers/w35677)
- [NBER public RPS data page](https://sites.google.com/view/covid-rps/data)
- [O*NET 31.0 database](https://www.onetcenter.org/database.html)
