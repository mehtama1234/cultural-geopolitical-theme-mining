# The map of AI work changes with the measurement layer

**Status:** provisional multi-source measurement finding · **Checked:** 2026-09-13

## The bounded finding

The current evidence does not support one thing called “AI exposure.” It
supports a stack of different measurements: O*NET task metadata, NBER worker-
reported adoption, NBER broad activity aggregation, and platform chat-log
classification. These layers overlap enough to be connected, but not enough to
be substituted for one another. The practical consequence is that a claim about
AI and work must state whether it describes task fit, worker use, system
activity, or a change in workplace control.

## What the layers contribute

| Layer | Unit and evidence | What it can establish | What it cannot establish |
|---|---|---|---|
| O*NET 31.0 | US occupation/work-activity metadata; August 2026 release | Stable task and occupation labels for a versioned crosswalk | Actual AI use, access, employer permission, pay, autonomy, or bargaining |
| NBER DWA/IWA/BWA indexes | RPS work-activity observations pooled August 2025–May 2026 | Worker-reported, survey-weighted adoption rates by activity; 682 DWA, 256 IWA, and 9 BWA rated rows | Worker-level subgroup outcomes, workplace rules, productivity, or control |
| NBER worker/task analysis | 13,920 employed respondents and 55,634 worker-task observations | Widespread but shallow adoption and variation among people doing similar work | Why adoption differs or what happens after adoption |
| Platform chat-log comparisons | Three platform activity measures compared with RPS task measures | Different activity classifications have low pairwise agreement; all reported correlations are below 0.4 | Population prevalence, worker experience, or which classification is “true” |

The [O*NET/NBER audit](../onet-release-metadata-gate-v1.md) found that the
hierarchical IDs do not exactly match. After normalization, 1,653 of 1,655 DWA
labels and all 322 IWA labels match uniquely. NBER’s nine BWA IDs can be mapped
to O*NET GWA prefix members, but their broad labels remain an aggregation layer,
not exact O*NET labels. The historical [provisional crosswalk artifact](../data/nber-onet-provisional-label-crosswalk-2026-09-13.json)
has now been superseded for reproducibility by the [acquired-input crosswalk](../data/onet-nber-crosswalk-2026-09-14/provisional-label-crosswalk.json)
and its [identifier reconciliation audit](../data/onet-nber-crosswalk-2026-09-14/onet-nber-identifier-reconciliation-audit-2026-09-14.json).
keeps that distinction explicit.

## The evidence chain

```text
occupation/task metadata
  -> possible task fit and exposure
  -> worker access, permission, training, and perceived usefulness
  -> reported adoption for selected activities
  -> task allocation, discretion, pace, monitoring, and evaluation
  -> pay, security, wellbeing, household room, voice, and political meaning
```

The current sources directly measure the metadata and adoption stages. They
partly compare measurement systems. They do not measure the employer decision,
worker discretion, or downstream household and political endpoints in the same
unit and period.

## Interpretation

The defensible interpretation is that AI adoption is a situated relationship,
not a fixed property of an occupation. A high-exposure occupation can contain
workers with different access or use; a low-adoption task can reflect poor tool
fit, professional norms, privacy, quality concerns, or employer restriction.
Likewise, a platform’s chat activity can reveal a kind of system demand without
showing who performed the work or who gained control over it.

This matters for cultural and political interpretation. “AI-exposed worker” can
become a public identity before people in the category experience the same tool,
rule, risk, or opportunity. That is a hypothesis about meaning and power that
requires worker, workplace, and institutional evidence; it is not a result of
the adoption indexes alone.

## Counterinterpretations

- Label agreement may reflect shared O*NET-derived wording rather than identical
  sampling, taxonomy vintage, or construct validity.
- The two unmatched DWA labels may be genuine naming changes, transcription
  differences, or tasks absent from the current mapping.
- Broad prefix membership provides a transparent aggregation rule but not proof
  that NBER and O*NET assign identical conceptual boundaries.
- Worker-reported adoption can miss informal, unreported, or employer-mediated
  use; platform logs can over-generalize activity.
- Similar adoption does not imply similar training, monitoring, autonomy,
  bargaining power, or benefit.

## What would change the finding

It would weaken if a validated release-matched crosswalk showed that the
measurement differences were only cosmetic and worker access, employer rules,
and adoption were nearly determined by occupation/task exposure. It would
strengthen if adoption differences persisted within matched tasks after access,
training, employer policy, worker characteristics, and workplace outcomes were
measured.

## Next test

Use the provisional crosswalk only as a reproducibility aid. The next empirical
test is a compatible worker or workplace design that joins task adoption to
training, permission, monitoring, discretion, correction, pay, promotion,
health, household security, and worker voice. Keep O*NET metadata, NBER survey
indexes, platform logs, firm disclosures, and field experiments as separate
units until a valid linkage exists.

**Evidence status:** detailed/intermediate label reconciliation and broad-prefix
mapping completed; semantic crosswalk validation and adoption-to-control and
downstream cultural, household, political, and geopolitical links remain open.

## Sources

- [NBER Working Paper 35677](https://www.nber.org/papers/w35677)
- [O*NET 31.0 database](https://www.onetcenter.org/database.html)
- [O*NET release archive](https://www.onetcenter.org/db_releases.html)
