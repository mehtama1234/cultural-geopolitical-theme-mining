# SIPP SNAP transition reason and compound hardship layer v1

**Checked:** 2026-09-13  
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file  
**Unit:** identified person, adjacent reference-month SNAP transition pair  
**Method:** Fay BRR with `G=240` and perturbation factor `0.5`; descriptive only

## What this adds

The existing reason layer kept rent/mortgage hardship and utility hardship as
separate outcomes. This pass adds a stricter compound outcome: a valid report
of being unable to pay **both** rent/mortgage and utility bills in the month
following a recorded SNAP transition.

```text
SNAP receipt at t -> receipt at t+1
  + recorded entry/exit reason
  -> simultaneous rent/mortgage and utility hardship at t+1
```

This is a population-level distributional test. It is not a program-impact
estimate and does not describe one household.

## Results among classified transitions

There were 217 classified entry pairs and 188 classified exit pairs. The
compound percentages below use the valid joint-outcome denominator within each
reason category; parentheses give Fay-BRR standard errors in percentage points.

### SNAP entry

| Recorded entry reason | Pairs | Both hardships |
|---|---:|---:|
| Job loss/layoff or wages reduced | 57 | 15.9% (6.1) |
| Loss/reduction of other income | 35 | 16.9% (7.5) |
| Became disabled/unable to work | 24 | 14.7% (9.8) |
| New child/dependent or pregnancy | 15 | 14.9% (8.3) |
| Needed to recertify | 11 | 8.5% (9.7) |
| Other | 50 | 1.5% (1.6) |

The largest entry categories show that a transition into receipt can coexist
with simultaneous housing and utility insecurity. The point estimates are
uncertain, especially for disability and family categories; they should not be
ranked as program effects.

### SNAP exit

| Recorded exit reason | Pairs | Both hardships |
|---|---:|---:|
| Ineligible because income increased | 63 | 12.1% (4.3) |
| Ineligible because of family changes | 8 | 17.3% (12.9) |
| Still eligible but could not/chose not to collect | 6 | 27.3% (23.4) |
| Requirements not met | 8 | 10.5% (11.1) |
| Time limit reached | 11 | 17.7% (13.0) |
| Benefits not worth the trouble | 4 | 32.3% (25.7) |
| Other | 88 | 5.2% (2.3) |

The exit screen directly weakens the shorthand “benefit exit means recovery.”
Several exit routes retain compound hardship in the following record, although
the smallest categories have very wide uncertainty.

## Interpretation and boundary

The joint outcome is a stronger material-security signal than either bill
field alone, but it still does not observe benefit amount, notice, application
effort, timing of the bills, appeal, remedy, food, health, debt, trust, or
political action. “Following month” is an adjacent SIPP reference-month record;
it does not prove that the SNAP transition caused the hardship.

Recorded reasons remain incomplete: only 217 of 437 entry pairs and 188 of 387
exit pairs had a classified reason. Unknown reasons and invalid joint hardship
reports remain part of the boundary, not observations to be silently removed.

## What this adds to the broad societal map

1. Public assistance receipt and basic security are different stages.
2. Housing and utility insecurity can remain simultaneous after entry and after
   recorded exit, so one benefit status cannot stand in for household security.
3. Administrative, income, disability, family, and employment routes need to
   remain distinct before interpreting trust, fairness, or political meaning.
4. The next missing arrow remains the same-episode ledger: notice, route effort,
   amount, decision, remedy, interpretation, and action.

## Reproduction

```text
python3 scripts/analyze_sipp_snap_reason_outcome_fay_brr.py \
  --primary /tmp/us-broad-sipp-2025/full-v13/sipp-household-slice.csv \
  --replicate-zip /tmp/us-broad-sipp-2025/rw2025_csv.zip \
  --output /tmp/us-broad-sipp-2025/full-v13/sipp-snap-reason-outcome-fay-brr-compound.json
```

The raw files and generated JSON remain outside the repository. The reusable
analysis script is [analyze_sipp_snap_reason_outcome_fay_brr.py](../../../scripts/analyze_sipp_snap_reason_outcome_fay_brr.py).
