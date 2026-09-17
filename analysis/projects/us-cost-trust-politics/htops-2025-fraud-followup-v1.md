# HTOPS 2025 fraud-to-follow-up screen v1

**Status:** exploratory same-respondent follow-up; no causal or practical-exit finding
**Checked:** 2026-09-16
**Machine record:** [fraud follow-up screen](data/htops-2025-fraud-followup-2025-04-to-06.json)
**Acquisition gate:** [fraud/recovery/trust gate](htops-2025-fraud-recovery-trust-acquisition-gate-v1.md)

## Question

Can the April 2025 HTOPS fraud module be linked to later June material and
institutional outcomes for the same public-use respondent?

```text
April retrospective scam exposure
  -> loss, reporting, and agency recovery
  -> June food, energy, work-loss, and trust responses
```

The linkage is technically possible through `SCRAMID`. The April person
weight and 80 replicate-weight schema were checked; April replicate variance
is not used because the public files do not document an attrition-adjusted
longitudinal weight.

## Linkage and groups

The April PUF has 8,850 rows and the June PUF has 8,850 rows. The exact-ID
intersection contains 6,564 respondents. Within that linked intersection, the
unweighted group counts are:

| April group | Linked respondents |
|---|---:|
| No reported scam exposure | 751 |
| Reported scam exposure | 5,798 |
| Exposure and money loss | 184 |
| Exposure and government/law-enforcement report | 539 |
| Money loss and report | 51 |
| Money loss, report, and reported agency recovery | 11 |

Groups are constructed only where the relevant April answer is valid. The
small recovery group is retained as a boundary signal, not a stable estimate.

## Descriptive follow-up

The screen applies April `PWEIGHT` to linked respondents and reports weighted
shares among respondents with valid June outcomes:

| April group | June food insufficiency | June unable to pay energy bill | June recent household job loss |
|---|---:|---:|---:|
| No reported exposure (`n=751`) | 9.37% | 16.84% | 9.22% |
| Exposure (`n=5,798`) | 6.12% | 10.66% | 6.86% |
| Exposure + loss (`n=184`) | 23.82% | 43.81% | 8.31% |
| Loss + report (`n=51`) | 12.22% | 44.86% | 11.56% |
| Loss + report + recovery (`n=11`) | 26.57% | 78.80% | 26.03% |

The screen also retains June `TRUST1`, `TRUST2_CONGRESS`, and
`FEDSTAT_TRUST` code-1 shares. Those values are reported in the machine
record as coding screens and are not translated into “high trust” without
preserving the dictionary labels. The pattern is not monotonic across fraud,
loss, reporting, and recovery groups.

## Interpretation boundary

This is stronger than a cross-sectional co-occurrence table because the same
`SCRAMID` is observed in April and June. It is still not a causal fraud
effect. The April fraud questions refer to the prior 12 months rather than a
dated incident; the actor, alternatives, effort, remedy timing, prior trust,
and reason for any June change are not measured. Linked retention is selective,
and April weights are not documented as attrition-adjusted longitudinal
weights. The recovery cell has only 11 linked respondents.

Therefore the safe conclusion is narrow: a public HTOPS respondent-level key
permits an exploratory comparison of later household and institutional
responses across retrospective fraud/loss/reporting groups. It does not show
that fraud caused energy insecurity, food insufficiency, job loss, trust
change, or exit.

## What this closes and what remains open

| Arrow | Status |
|---|---|
| Same respondent across April and June | Observed through exact `SCRAMID` intersection |
| Retrospective exposure → loss/report/recovery | Reported and conditionally coded in April |
| Later material context | Longitudinally associated June outcomes |
| Later trust/meaning | Later coded responses available, but not prior-to-later trust change |
| Incident date, actor, alternative, effort | Open |
| Remedy receipt and durability | Open |
| Causal attribution or practical exit | Open |

## Reproduction

```text
python3 scripts/analyze_htops_2025_fraud_followup.py \
  --april /tmp/cgtm-htops-followup/2504/TOPICAL_2504_PUF.csv \
  --april-replicates /tmp/cgtm-htops-followup/2504/HTOPS_2504_repwgt_puf.csv \
  --june /tmp/cgtm-htops-followup/HTOPS_HPS_2506_PUF.csv \
  --output analysis/projects/us-cost-trust-politics/data/htops-2025-fraud-followup-2025-04-to-06.json
```

The raw PUFs and temporary extracts are not retained in the repository. Input
hashes are recorded in the machine-readable output.
