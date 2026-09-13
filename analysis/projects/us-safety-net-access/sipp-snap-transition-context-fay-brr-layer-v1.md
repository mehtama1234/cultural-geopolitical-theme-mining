# SIPP SNAP transition context Fay-BRR layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file; 2024 reference year  
**Unit:** identified person, adjacent reference-month pair  
**Weight:** `WPFINWGT` from the first month; `REPWGT1`–`REPWGT240` for variance  
**Method:** Fay BRR with `G = 240` and perturbation factor `0.5`; descriptive only

## Why this layer was added

The original transition-context comparison showed resource-ratio and job-count
changes around SNAP entry and exit but had no replicate-weight uncertainty. This
pass adds design-based standard errors and approximate 95% intervals to the
conditional distributions. It tests precision around the descriptive pattern;
it does not identify why a transition occurred or estimate program impact.

## Resource-ratio change around transitions

The denominator is the valid context subset within each transition: both
adjacent months have a numeric `THINCPOV` value. Percentages are weighted
shares; intervals are approximate 95% Fay-BRR intervals.

| Transition | Resource ratio down | Same | Up | Valid records |
|---|---:|---:|---:|---:|
| No → Yes | 58.57% (49.75–67.39) | 14.18% (8.45–19.92) | 27.25% (19.09–35.41) | 435 |
| Yes → No | 76.37% (67.80–84.94) | 12.28% (3.86–20.70) | 11.35% (6.51–16.19) | 386 |

The weighted resource-context denominators were approximately 4.62 million for
entry and 4.35 million for exit. In this sample, exit is more often accompanied
by a lower adjacent income-to-poverty ratio than by an increase. That is a
descriptive warning against treating program exit as automatic evidence of
improved resources.

## Job-count change around transitions

The job denominator is smaller because both months must have a valid numeric
`RMNUMJOBS` value. The missing job comparison is not silently assigned to
“same.”

| Transition | Jobs down | Same | Up | Valid records |
|---|---:|---:|---:|---:|
| No → Yes | 2.60% (0.96–4.24) | 92.84% (88.86–96.82) | 4.56% (0.85–8.27) | 309 |
| Yes → No | 3.28% (0.63–5.92) | 95.57% (92.46–98.68) | 1.15% (0.00–2.86) | 287 |

These job results describe a selected valid subset, not employment quality,
earnings, hours, schedule, or work freedom. They do not show that SNAP changed
job counts.

## What this adds to the public-systems picture

The resource context strengthens the claim that receipt exit cannot be read as
a simple success indicator. A lower measured resource ratio around many exits
could reflect timing, household composition, reporting, administrative process,
non-collection, benefit-owner differences, or an unmeasured shock. It does not
by itself show that the program caused the resource decline.

The job context shows why “exit to work” is also too strong for these records:
among valid job comparisons, job count is usually unchanged around both entry
and exit. Missing job values and the coarse job-count measure prevent a stronger
interpretation.

## Verification and limits

- The primary slice contained 379,215 person-month rows.
- The replicate file contained 378,291 positive-weight matched rows.
- All 824 no-to-yes and yes-to-no transition pairs matched replicate records.
- Resource context was valid for 435 entry pairs and 386 exit pairs.
- Job context was valid for 309 entry pairs and 287 exit pairs; the remainder
  had at least one missing/invalid adjacent job-count value.
- `THINCPOV` is a monthly income-to-poverty ratio; `RMNUMJOBS` is a monthly
  job-count recode. Neither is a complete household security measure.
- Person records may represent covered members of a SNAP unit; this is not a
  household-count or benefit-spell table.
- No notice, application, renewal effort, benefit amount, food quantity,
  health, debt, trust, or political action is observed in this calculation.
- Fay-BRR intervals describe sampling uncertainty and do not establish cause.

## Reproduction

```text
python3 scripts/analyze_sipp_snap_transition_context_fay_brr.py \
  --primary /path/to/sipp-household-slice.csv \
  --replicate-zip /path/to/rw2025_csv.zip \
  --output /tmp/sipp-snap-transition-context-fay-brr.json
```

The raw files and derived JSON are not committed. The verified calculation was
run against the 2025 SIPP slice and `/tmp/us-broad-sipp-2025/rw2025_csv.zip`.

## Next test

Add replicate-weight uncertainty to the reason-aligned transition categories,
then connect reasons and context to benefit amount, notice, effort, food
security, household composition, and re-entry. Use the broad event ledger for
the missing same-episode interpretation, trust, and political-action fields.

Related records: [SIPP SNAP transition layer](sipp-snap-transition-layer-v1.md),
[transition Fay-BRR uncertainty layer](sipp-snap-transition-fay-brr-layer-v1.md),
[transition × recorded reason layer](sipp-snap-transition-reason-layer-v1.md),
and [public administration, take-up, security, and political feedback layer](public-administration-takeup-security-trust-action-layer-v1.md).
