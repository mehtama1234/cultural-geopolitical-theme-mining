# Work-limiting conditions change material room inside the resource gradient

**Status:** current-vintage descriptive SIPP refresh · **Checked:** 2026-09-14

## The bounded finding

Within the current 2025 SIPP v16 extract, people reporting a condition that
limits the kind or amount of work they can do show more utility difficulty,
lower high/marginal food security, and fewer people with one job than people
without that condition in the displayed White-alone and Black-alone groups.
The resource gradient remains visible within both status groups. This is a
distributional pattern, not evidence that disability, race, or income caused
the outcome.

`EDISABL` is a work-limiting-condition measure. It is not a full disability
taxonomy, an accommodation measure, a health diagnosis, or a direct measure of
work choice.

## Current-vintage estimates

Percentages use `WPFINWGT`; parentheses are Fay–BRR standard errors in
percentage points. `n` is the valid person-month record count for that outcome.

| Race | Work-limiting condition | Resource band | Utility difficulty | Hunger | High/marginal food security | One job |
|---|---|---|---:|---:|---:|---:|
| White alone | Yes | Below 1.00x | 17.39 (1.73), n=7,557 | 39.52 (3.33), n=3,607 | 60.62 (2.43), n=7,557 | 9.61 (1.21), n=7,557 |
| White alone | No | Below 1.00x | 12.28 (1.28), n=14,281 | 31.24 (4.01), n=3,852 | 78.85 (1.66), n=14,281 | 34.41 (1.41), n=14,281 |
| White alone | Yes | 4.00x or more | 4.10 (0.65), n=14,615 | 33.90 (5.39), n=1,388 | 92.97 (1.02), n=14,615 | 32.43 (1.53), n=14,615 |
| White alone | No | 4.00x or more | 2.23 (0.26), n=110,000 | 18.09 (2.81), n=6,063 | 96.56 (0.35), n=110,000 | 68.68 (0.55), n=110,000 |
| Black alone | Yes | Below 1.00x | 22.28 (4.18), n=2,301 | 35.29 (7.36), n=1,038 | 56.24 (4.65), n=2,301 | 8.78 (2.61), n=2,301 |
| Black alone | No | Below 1.00x | 16.12 (3.51), n=3,129 | 24.46 (5.93), n=1,215 | 67.45 (4.25), n=3,129 | 22.97 (2.62), n=3,129 |
| Black alone | Yes | 4.00x or more | 12.11 (3.42), n=1,552 | 28.45 (12.33), n=261 | 86.92 (5.01), n=1,552 | 40.66 (5.36), n=1,552 |
| Black alone | No | 4.00x or more | 5.37 (1.08), n=9,230 | 21.51 (4.71), n=1,130 | 93.48 (1.18), n=9,230 | 72.11 (1.63), n=9,230 |

## What this adds

The strongest separation is in one-job status. At the below-1.00x resource
endpoint, one-job status is 9.61% for White respondents with the work-limiting
condition versus 34.41% without it, and 8.78% versus 22.97% for Black
respondents. At 4.00x or more, the corresponding comparisons are 32.43% versus
68.68% and 40.66% versus 72.11%.

The material measures move with that work-status separation, but they do not
tell us why. A condition may alter hours, occupation, employer access,
accommodation, care needs, or earnings; the table cannot distinguish those
routes. Nor does it show whether a household buffer, public benefit, family
support, or accessible job protected the person.

## Counterexamples and uncertainty

- Higher resources improve the measured distribution within both status
  groups, but do not eliminate hardship among people reporting a work-limiting
  condition.
- Black-alone high-resource hunger cells are imprecise: the yes-condition cell
  has `n=261` and a 12.33-point standard error.
- The race comparison is not a ranking of groups or a discrimination estimate;
  the recode and composition are limited.
- Household outcomes repeat across person records, so these are not household
  rates. Job count does not measure hours, pay, schedule control, job quality,
  or voluntary choice.
- Current-v16 estimates are directionally consistent with the earlier v10
  layer but not identical in every cell. The refresh therefore supplements the
  earlier result rather than silently replacing it.

## Reproduction and open arrows

The calculation reads 379,215 primary person-month rows and matches 378,291
positive-weight rows to the 240 replicate records. It applies documented
official universes and Fay–BRR with perturbation factor 0.5. The [refresh
audit](../sipp-fay-brr-race-disability-resource-refresh-audit-2026-09-14.json)
preserves the input/output hashes and exact command; the [original layer](../sipp-fay-brr-race-disability-resource-layer-v1.md)
preserves the earlier v10 table.

The current evidence measures resource position, work-limiting status, and
selected hardship/work outcomes. It does not observe a dated health event,
accommodation, employer decision, care-time change, benefit route, housing
move, repair, trust judgment, political action, or firm response.

## Next test

Add tenure and household composition to a pre-specified subset, then connect
the status/resource cells to work hours, care time, health, benefits, or
housing stability in a valid longitudinal or same-unit design. Preserve the
work-limitation definition and do not infer disability, discrimination, or
political meaning from this table alone.

**Evidence status:** current-vintage weighted intersectional comparison with
design-based uncertainty; causal and downstream institutional, cultural, and
political consequences remain open.
