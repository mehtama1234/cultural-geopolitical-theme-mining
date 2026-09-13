# SIPP SNAP transition Fay-BRR uncertainty layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file; 2024 reference year  
**Unit:** identified person, adjacent reference-month pair  
**Weight:** `WPFINWGT` from the first month; `REPWGT1`–`REPWGT240` for variance  
**Method:** Fay BRR with `G = 240` and perturbation factor `0.5`; descriptive only

## Why this layer was added

The original SNAP transition layer supplied point estimates but explicitly did
not estimate replicate-weight uncertainty. This pass adds design-based standard
errors and approximate 95% intervals for the distribution of valid adjacent
month transitions. It improves uncertainty, not causality or household-level
interpretation.

## Estimates among all valid transition pairs

| Transition | Pairs | Weighted share | Fay-BRR SE (percentage points) | Approx. 95% interval |
|---|---:|---:|---:|---:|
| No → No | 312,418 | 90.646% | 0.283 | 90.091%–91.202% |
| Yes → Yes | 33,041 | 9.106% | 0.280 | 8.557%–9.655% |
| No → Yes | 437 | 0.128% | 0.012 | 0.104%–0.151% |
| Yes → No | 387 | 0.120% | 0.012 | 0.097%–0.143% |

The denominator is the full weighted set of 346,283 valid adjacent pairs for
each row. The entries and exits are rare in this person-month pair frame. These
are not annual prevalence estimates, national spell hazards, or estimates of
program churn for households.

## What this strengthens

The broad descriptive pattern is precise enough to distinguish the dominant
within-state observations from the rare observed transitions in this selected
sample: most valid adjacent pairs remain in the same recorded SNAP state, while
no-to-yes and yes-to-no transitions each account for roughly one tenth of one
percent of all valid pairs. The intervals quantify sampling uncertainty around
those shares.

This does not change the interpretation limits. A transition can reflect an
application, eligibility change, notice, renewal, non-collection, reporting
state, household composition, or another process. The variance estimate cannot
identify which mechanism occurred or whether a transition improved food,
income, health, work, debt, time, trust, or political action.

## Verification and limits

- The primary slice contained 379,215 person-month rows.
- The replicate file contained 378,291 positive-weight matched rows.
- All 346,283 valid adjacent transition pairs were matched to replicate
  records for this calculation.
- `RSNAP_MNYN` uses the documented SIPP codes: `1 = yes`, `2 = no`.
- The first month’s person weight defines each pair’s point estimate and each
  replicate’s transition weight.
- Person records may represent covered members of a SNAP unit; this is not a
  household-count or benefit-spell table.
- No replicate variance was estimated for the transition-context, reason, or
  downstream food/work comparisons in the related layers.
- Fay-BRR uncertainty does not turn adjacent association into program impact or
  causal evidence.

## Reproduction

```text
python3 scripts/analyze_sipp_snap_transition_fay_brr.py \
  --primary /path/to/sipp-household-slice.csv \
  --replicate-zip /path/to/rw2025_csv.zip \
  --output /tmp/sipp-snap-transition-fay-brr.json
```

The raw files and derived JSON are not committed. The verified calculation was
run against the 2025 SIPP slice and `/tmp/us-broad-sipp-2025/rw2025_csv.zip`.

## Next test

Add replicate-weight uncertainty to the transition-context and reason-aligned
comparisons, then connect the transition to benefit amount, notice, effort,
food-security status, work, resource changes, and later re-entry. Keep the
person-month transition evidence separate from the same-episode ledger needed
to measure interpretation, trust, and political response.

Related records: [SIPP monthly SNAP transition layer](sipp-snap-transition-layer-v1.md),
[transition × recorded reason layer](sipp-snap-transition-reason-layer-v1.md),
[transition × material context layer](sipp-snap-transition-context-layer-v1.md),
and [public administration, take-up, security, and political feedback layer](public-administration-takeup-security-trust-action-layer-v1.md).
