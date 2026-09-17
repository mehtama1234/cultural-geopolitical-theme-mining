# Finding 045: Stable hours hide different earnings movement across household contexts

**Status:** provisional subgroup-conditioned SIPP finding · **Checked:** 2026-09-17

## The bounded finding

The retained 2025 SIPP slice follows the same person from month *t* to month
*t+1* and uses 240 Fay–BRR replicate weights. Conditioning the directional
earnings/hours screen on children under 18 and SNAP receipt produces a useful
reversal of a simple “work is stable” story:

- hours are mostly unchanged in every displayed resource band and subgroup;
- earnings move in both directions much more often than hours do;
- the low-resource earnings pattern differs by household context, while the
  high-resource pattern converges more closely; and
- SNAP receipt is associated with a different descriptive composition of
  earnings direction than no receipt, but this is not a SNAP effect.

The contribution is a subgroup boundary. Resource gradients in earnings and
hours should not be read as one universal worker or household trajectory.

```text
resource context + children/SNAP status at month t
  -> earnings direction and hours direction at month t+1
  -> [open] job quality, care mechanism, household protection, remedy, trust, action, exit
```

## Evidence comparison

| Subgroup | Low-resource earnings direction | High-resource earnings direction | Low-resource hours direction | High-resource hours direction |
|---|---|---|---|---|
| Children present | Increase 36.6%, decrease 30.1%, same 33.3% (n=2,760) | Increase 43.7%, decrease 43.0%, same 13.3% (n=28,310) | Increase 9.0%, decrease 4.4%, same 86.6% (n=2,859) | Increase 2.1%, decrease 2.6%, same 95.4% (n=28,424) |
| No children recorded | Increase 31.4%, decrease 26.6%, same 42.1% (n=3,126) | Increase 43.1%, decrease 42.9%, same 14.1% (n=65,016) | Increase 7.0%, decrease 5.2%, same 87.8% (n=3,565) | Increase 1.7%, decrease 2.6%, same 95.6% (n=65,395) |
| SNAP receipt | Increase 32.8%, decrease 26.4%, same 40.8% (n=1,123) | Increase 40.8%, decrease 42.0%, same 17.2% (n=1,196) | Increase 9.6%, decrease 5.2%, same 85.2% (n=1,167) | Increase 2.1%, decrease 3.9%, same 94.0% (n=1,203) |
| No SNAP receipt | Increase 34.1%, decrease 28.6%, same 37.3% (n=4,763) | Increase 43.3%, decrease 42.9%, same 13.8% (n=92,130) | Increase 7.5%, decrease 4.7%, same 87.7% (n=5,257) | Increase 1.8%, decrease 2.6%, same 95.6% (n=92,616) |

The table reports weighted directional shares; the displayed `n` is the
unweighted valid pair count for the relevant outcome universe. Earnings and
hours counts differ. Standard errors and approximate 95% Fay–BRR intervals for
all four resource bands are preserved in the [machine-readable record](../../../records/us-sipp-resource-work-direction-subgroups-2024.json).

## What the subgroup reversal changes

At below 1× the poverty threshold, children-present pairs show a lower
same-earnings share than no-children-recorded pairs (33.3% versus 42.1%), with
more earnings increases and decreases. Among SNAP recipients, the comparable
same-earnings share is 40.8%, versus 37.3% among no-SNAP pairs. These patterns
do not identify why earnings moved. They show that the low-resource surface is
not homogeneous and that program-status context changes the composition of
the observed transition.

At 4× and above, the groups are more similar: earnings increases and decreases
are both about 43% for children-present and no-children pairs, while hours are
unchanged for about 95%. The convergence is a descriptive counterexample to a
simple claim that household composition produces the same resource gradient at
every income level.

The sharper recurring split is between earnings and hours. In the low-resource
children-present cell, hours are unchanged for 86.6% while earnings are
unchanged for 33.3%. In the high-resource children-present cell, the analogous
figures are 95.4% and 13.3%. Stable hours therefore leave room for changing
pay, job mix, days worked, reporting, schedule quality, or household members'
unpaid substitution.

## Counterexamples and limits

- Children present is a household-composition marker, not a dated child-care
  failure, care intensity measure, or causal exposure.
- No SNAP receipt is not absence of need, and SNAP receipt is not benefit
  adequacy or a treatment assignment.
- “Same” earnings or hours means equal recorded values across adjacent months;
  it does not mean adequate pay, desired schedule, security, or control.
- The resource band is measured at month *t* and is not a complete household
  balance sheet. Person weights are not household weights.
- Earnings and hours have separate valid-pair universes; small cells carry
  wider uncertainty than the large high-resource cells.
- The panel does not identify a bill, care episode, employer decision,
  institutional remedy, trust change, political action, or later exit.

## Broad-program implication

This result strengthens the atlas's larger claim that money, time, care, and
control are different currencies. A household can show stable recorded hours
while earnings move, or show unchanged earnings while care, schedule, and
security change elsewhere. The subgroup split also warns against assigning a
single cultural or political meaning to “economic stability”: different
household contexts can sit behind the same hours statistic.

The next stronger step remains a dated work/care or payment event with actual
alternatives, schedule control, employer or agency response, and later
household, trust, action, or exit outcomes. This SIPP layer is a subgroup
reversal and timing refinement, not that event.

## Reproduction and storage boundary

- [Machine-readable subgroup record](../../../records/us-sipp-resource-work-direction-subgroups-2024.json)
- [Analysis script](../../../../scripts/analyze_sipp_resource_work_direction_subgroups.py)
- [Prior directional SIPP finding](us-household-calendar-integration-037.md)
- [SIPP 2025 public-use data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)

The analysis read the existing local 379,215-row slice and the retained 240-
replicate archive. No new archive was downloaded. The output preserves the
input, script, replicate, and result hashes.

**Evidence status:** same-person, subgroup-conditioned descriptive transition
with Fay–BRR uncertainty. No causal resource, child, SNAP, care, earnings,
hours, recovery, trust, political-action, or exit claim is made.
