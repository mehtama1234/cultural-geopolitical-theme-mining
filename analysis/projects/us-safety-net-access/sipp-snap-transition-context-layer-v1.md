# SIPP SNAP transition × material-context layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file, 2024 reference year  
**Unit:** identified person, adjacent reference-month pair  
**Weight:** `WPFINWGT` from the first month of each pair  
**Method:** weighted descriptive transition comparison; no replicate-weight variance estimate

This layer compares the monthly SNAP receipt transition with the change in
monthly household income-to-poverty ratio and job count around the same pair.
It asks whether entry and exit are accompanied by measured resource or work
changes. It does not estimate program impact or explain why the change occurred.

## Material context around transitions

| SNAP transition | Resource ratio down | Same | Resource ratio up | Resource unknown |
|---|---:|---:|---:|---:|
| No → Yes (437 pairs) | 58.13% | 14.08% | 27.05% | 0.75% |
| Yes → No (387 pairs) | 76.20% | 12.25% | 11.32% | 0.23% |

Among pairs with valid job counts, job status was unchanged in 63.29% of
entries and 69.40% of exits. Job count went down in 1.77% of entries and
2.38% of exits, and was unknown in 31.83% and 27.39% respectively because one
or both records lacked a valid job-count value under the selected comparison.

## What this adds

In this descriptive pair sample, both SNAP entry and SNAP exit often occur
alongside a lower next-month income-to-poverty ratio, with the downward share
particularly large for exits. That means a receipt exit should not automatically
be interpreted as improved material circumstances. It may reflect an
administrative or reporting process, a different household threshold or
composition, non-collection, or another unmeasured reason. Conversely, entry is
not itself proof that a household’s resources fell because of the program or
that assistance restored food security.

This result sits beside the recorded-reason layer. The reason field can report
increased income as an exit reason while the adjacent ratio comparison points
down for many exits; the measures refer to different timing, definitions, and
partially overlapping records. That disagreement is a useful warning to keep
reported reason, administrative state, material change, and causal
interpretation separate.

## Verification and limits

- 379,215 primary person-month rows were read.
- 31,992 people were identified; 31,090 had all twelve reference months.
- There were 437 no-to-yes and 387 yes-to-no transitions.
- `THINCPOV` is documented as a monthly household income-to-poverty ratio;
  changes were classified numerically between adjacent months.
- `RMNUMJOBS` is a monthly job-count recode, but 31.83% of entry pairs and
  27.39% of exit pairs had an unknown job comparison in this run.
- The first month’s person weight was used. No Fay-BRR variance was estimated.
- These are adjacent associations, not evidence that SNAP caused a resource
  change, prevented one, or ended because of one.
- The result does not observe application, notice, renewal burden, office or
  channel, benefit amount, food quantity, health, debt, trust, or politics.

## Reproduction

```text
analyze_sipp_snap_transition_context.py
```

The raw files, derived CSV, and JSON output are not committed. The calculation
output was `/tmp/us-broad-sipp-2025/full-v13/sipp-snap-transition-context.json`.

## Next test

Align the transition with the recorded start/end reason, benefit amount,
household composition, work-limiting condition, food-security status, and
re-entry. Use replicate weights or a design-based longitudinal estimator for
the transition-context comparisons, and separate the unclassified events.

Related records: [SIPP SNAP transition × recorded reason layer](sipp-snap-transition-reason-layer-v1.md),
[SIPP SNAP transition layer](sipp-snap-transition-layer-v1.md),
[SIPP SNAP × food-security layer](sipp-snap-food-security-layer-v1.md),
and [safety-net event ledger](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md).
