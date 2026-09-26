# Finding 042: Expense difficulty carries a later material-pressure gradient without one universal confidence shift

**Status:** bounded same-respondent cross-lagged screen · **Checked:** 2026-09-19

## The bounded finding

The April and June 2025 Census HTOPS public-use files share `SCRAMID`, allowing
a storage-light follow-up of baseline expense difficulty. The exact intersection
contains 6,564 linked respondents. Among the selected linked sample, baseline
expense difficulty is followed by substantially higher June food insufficiency,
energy-bill nonpayment, and recent household job loss. The institutional
pattern is selective rather than universal: high confidence in Congress is
nearly identical across the two baseline groups, while confidence in the
presidency, military, police, Supreme Court, public schools, and statistical
agencies is lower among respondents who reported expense difficulty.

| April baseline group | June food insufficiency | June unable to pay energy bill | June recent household job loss | Congress | Presidency | Military | Police | Supreme Court | Public schools | Statistical agencies |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Expense difficulty | 12.3% (SE 1.43) | 21.4% (SE 1.36) | 11.7% (SE 1.16) | 17.2% (SE 1.38) | 24.3% (SE 1.69) | 57.9% (SE 1.87) | 44.6% (SE 1.94) | 29.2% (SE 1.84) | 42.8% (SE 1.76) | 57.7% (SE 2.23) |
| No expense difficulty | 1.1% (SE 0.42) | 2.2% (SE 0.45) | 2.9% (SE 0.36) | 16.9% (SE 1.03) | 30.8% (SE 1.31) | 71.9% (SE 1.38) | 62.9% (SE 1.42) | 38.3% (SE 1.35) | 52.0% (SE 1.52) | 69.6% (SE 1.25) |

The outcome-specific valid unweighted counts range from 2,574 to 3,961. The
table therefore adds temporal ordering and a distinct institutional-confidence
profile, but it is not a causal estimate or a general population transition
rate. The Congress result is a counterexample to treating the other gradients
as a universal political reaction.

## What the chain establishes

```text
baseline expense difficulty
  -> later household material-pressure context [descriptive same-respondent link]
  -> later institutional confidence [selective gradients, not one common shift]
  -> dated bill, responsible actor, alternative, remedy, recovery, and action [open]
```

The result does not identify whether expense difficulty arose from a bill,
income interruption, health event, housing cost, debt, care, or another shock.
It also does not identify whether later food, energy, or job outcomes were
caused by the baseline condition. The near-equal Congress-confidence shares
are useful precisely because the other institution-specific gaps cannot be
converted into one general political-legitimacy shift without prior trust,
attribution, and a measured action route. Material pressure may relate
differently to executive, coercive, judicial, educational, statistical, and
legislative institutions.

## Limits and next field

- The linked sample is a retained intersection; April weights and replicate
  weights are not documented as attrition-adjusted longitudinal weights.
- Expense difficulty and the June outcomes have item-specific valid universes.
- The public-use linkage does not supply a dated bill, actor, payment route,
  notice, appeal, remedy receipt, durable recovery, or practical alternative.
- These confidence measures are not trust change in a responsible actor and
  are not a vote, complaint, organizing event, or other political action. The
  differences also should not be read as institution-specific causal effects.

The next decisive field is a dated material or service episode joined to the
route taken, effort/cost, response, verified correction or recovery, and later
household and political endpoint. Until then, this is a cross-lagged association
and acquisition boundary, not a causal household-security or political-effect
claim.

## Reproduction boundary

This pass reads the retained [cross-lagged audit](../data/htops-2025-cross-lagged-panel-audit.json)
and does not download new raw files. The [canonical record](../../../records/us-htops-expense-difficulty-cross-lagged-2025.json)
preserves the measures, standard errors, valid counts, public source, and raw-file
hashes. The [panel linkage audit](../htops-2025-panel-linkage-audit-v1.md)
documents the exact-ID and weighting boundary.
