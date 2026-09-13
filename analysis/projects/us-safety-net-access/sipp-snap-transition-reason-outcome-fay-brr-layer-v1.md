# SIPP SNAP transition reason and following hardship v1

**Checked:** 2026-09-13  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** identified person, adjacent reference-month SNAP transition pair  
**Method:** Fay BRR with `G=240` and perturbation factor `0.5`; descriptive only

## What this pass adds

Earlier layers measured recorded transition reasons and following-month
rent/utility hardship separately. This pass keeps them on the same adjacent-
month person record:

```text
SNAP receipt at t -> receipt at t+1
  + recorded reason for entry or exit
  -> valid rent/mortgage or utility hardship report at t+1
```

It is a population-level mechanism comparison, not a one-person case and not
a program-impact estimate.

## Results among classified transitions

There were 217 classified entry pairs and 188 classified exit pairs. The
hardship percentages below use the valid outcome denominator within each
reason category; parentheses give Fay-BRR standard errors in percentage points.

### SNAP entry

| Recorded entry reason | Pairs | Rent/mortgage hardship | Utility hardship |
|---|---:|---:|---:|
| Job loss/layoff or wages reduced | 57 | 16.8% (6.1) | 34.1% (7.8) |
| Loss/reduction of other income | 35 | 16.9% (7.5) | 30.0% (8.6) |
| Became disabled/unable to work | 24 | 28.3% (13.8) | 17.6% (9.9) |
| New child/dependent or pregnancy | 15 | 14.9% (8.3) | 27.6% (10.6) |
| Other | 50 | 8.8% (5.1) | 7.9% (3.9) |

The larger entry groups show different material profiles: job or wage loss and
other income loss are accompanied by higher utility than rent hardship, while
the disability group has the highest point estimate for rent hardship. These
cells are small and uncertain; they describe distinct routes into observed
receipt, not different program effects.

### SNAP exit

| Recorded exit reason | Pairs | Rent/mortgage hardship | Utility hardship |
|---|---:|---:|---:|
| Ineligible because income increased | 63 | 13.7% (4.6) | 27.6% (6.0) |
| Other | 88 | 10.1% (5.0) | 9.9% (3.3) |
| Family change | 8 | 17.3% (12.9) | 27.3% (17.5) |
| Requirements not met | 8 | 10.5% (11.1) | 10.5% (11.1) |
| Time limit reached | 11 | 17.7% (13.0) | 17.7% (13.0) |
| Still eligible but could not/chose not to collect | 6 | 27.3% (23.4) | 27.3% (23.4) |
| Benefits not worth the trouble | 4 | 32.3% (25.7) | 32.3% (25.7) |

The exit table does not support an “exit equals recovery” interpretation. Even
the largest exit groups retain material hardship in the following record, and
the small categories are too uncertain for fine ranking. “Income increased”
is a recorded eligibility reason, not proof that rent or utilities became
secure.

## Missingness and boundaries

The full transition frame contains 437 entry pairs and 387 exit pairs, but
only 217 and 188 respectively have a classified reason. Unknown or unclassified
reason is therefore part of the population boundary, not a nuisance to erase.
The hardship fields have their own valid-code flags, universes, and reference
periods. “At `t+1`” is record order, not proof that a bill arrived after the
transition.

The combined record still does not observe notice comprehension, application
effort, access channel, documents, benefit amount or timing, appeal, correction,
food quantity, health, debt, fairness, trust, complaint, turnout, vote, or
agency response. No causal or policy-effect claim is made.

## What this adds to the broad societal map

1. Public-system participation has multiple material routes: job loss, income
   loss, disability, family change, and administrative or informational paths
   do not share one hardship profile.
2. Receipt and security remain separate stages. A transition reason can be
   recorded while rent or utility hardship remains present.
3. The same public system can be experienced as income protection, disability
   support, family support, or an administrative route, so later trust and
   political meaning should not be inferred from transition status alone.
4. The next missing arrow is the episode ledger: route burden, notice, amount,
   timing, remedy, interpretation, and action.

## Reproduction

```text
python3 scripts/analyze_sipp_snap_reason_outcome_fay_brr.py \
  --primary /tmp/us-broad-sipp-2025/full-v13/sipp-household-slice.csv \
  --replicate-zip /tmp/us-broad-sipp-2025/rw2025_csv.zip \
  --output /tmp/us-broad-sipp-2025/full-v13/sipp-snap-reason-outcome-fay-brr.json
```

The raw files and generated JSON remain outside the repository. The reusable
analysis script is [analyze_sipp_snap_reason_outcome_fay_brr.py](../../../scripts/analyze_sipp_snap_reason_outcome_fay_brr.py).

Related: [SNAP transition hardship](sipp-snap-transition-outcome-fay-brr-layer-v1.md),
[SNAP transition reasons](sipp-snap-transition-reason-fay-brr-layer-v1.md),
and the [same-episode event-ledger design](same-episode-event-ledger-design-v1.md).
