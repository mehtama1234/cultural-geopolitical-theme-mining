# SIPP SNAP transition context Fay-BRR layer v1

**Checked:** 2026-09-14
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

## Person-earnings change around transitions

`TPEARN` is monthly earnings for the person, not household income, an hourly
pay rate, or a measure of work quality. Its valid universe is much smaller
because it is not populated for every person-month. Among 119 valid entry
pairs, earnings were down in 48.25% (SE 5.53 pp; 95% CI 37.42–59.08), the
same in 16.75% (SE 4.20 pp; 8.51–24.98), and up in 35.01% (SE 5.78 pp;
23.67–46.34). Among 133 valid exit pairs, earnings were down in 36.68% (SE
5.45 pp; 26.00–47.36), the same in 14.07% (SE 3.43 pp; 7.35–20.79), and up
in 49.25% (SE 5.78 pp; 37.92–60.58).

The earnings context complicates both simple readings: SNAP entry often sits
beside lower person earnings in this selected universe, while exit often sits
beside higher person earnings—but neither pattern establishes program impact,
an exit-to-work pathway, or restored household security. Earnings can change
with days in the month, hours, job composition, reporting, timing, or other
income and work changes.

## Monthly hours around transitions

`TMWKHRS` is average hours per week at all jobs held during the reference month.
It is monthly, but its universe is limited to people with a job in at least one
of the adjacent months. Hours were unchanged for 74.97% of 119 valid entry
pairs (SE 4.68 pp; 95% CI 65.80–84.13), with 15.62% down and 9.41% up. For 133
valid exit pairs, hours were unchanged for 89.77% (SE 3.66 pp; 82.59–96.94),
with 2.23% down and 8.01% up.

This is a sharper work-intensity boundary than job count, but it remains a
selected descriptive context. Stable hours do not establish stable earnings,
schedule control, job quality, or restored household security; people outside
the hours-valid universe can still have job entry or exit.

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
- Person-earnings context was valid for 119 entry pairs and 133 exit pairs; it
  is a selected person-level universe and is not interchangeable with the
  household resource or job-count universes.
- Monthly-hours context was valid for 119 entry pairs and 133 exit pairs; the
  hours universe is job-holder conditioned and has its own missingness.
- `THINCPOV` is a monthly income-to-poverty ratio; `RMNUMJOBS` is a monthly
  job-count recode; `TPEARN` is monthly person earnings; `TMWKHRS` is monthly
  average hours among job holders. None is a complete household security or
  work-quality measure.
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

### Current reproducibility audit

The 2026-09-14 rerun used the same primary slice and replicate-weight archive.
It read 379,215 primary rows and 378,291 replicate rows; all 824 positive-weight
transition pairs matched across the replicate file. The input hashes, script,
and method are preserved in the [reproduction audit](sipp-snap-transition-context-reproduction-audit-2026-09-14.json),
and the promoted estimates are in the [machine-readable transition-context record](../../records/us-sipp-snap-transition-resource-job-context-2024.json)
and [published bounded finding](findings/us-safety-net-access-007.md).

The monthly-hours extension used the complete v16 slice and has a separate
[hours reproduction audit](sipp-snap-transition-hours-reproduction-audit-2026-09-14.json)
because adding `TMWKHRS` changes the primary-slice hash.

## Next test

Add replicate-weight uncertainty to the reason-aligned transition categories,
then connect reasons and context to benefit amount, notice, effort, food
security, household composition, and re-entry. Use the broad event ledger for
the missing same-episode interpretation, trust, and political-action fields.

Related records: [SIPP SNAP transition layer](sipp-snap-transition-layer-v1.md),
[transition Fay-BRR uncertainty layer](sipp-snap-transition-fay-brr-layer-v1.md),
[transition × recorded reason layer](sipp-snap-transition-reason-layer-v1.md),
and [public administration, take-up, security, and political feedback layer](public-administration-takeup-security-trust-action-layer-v1.md).
