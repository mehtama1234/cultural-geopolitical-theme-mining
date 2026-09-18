# Finding 042: Expense difficulty carries a later material-pressure gradient without a clean confidence shift

**Status:** bounded same-respondent cross-lagged screen · **Checked:** 2026-09-18

## The bounded finding

The April and June 2025 Census HTOPS public-use files share `SCRAMID`, allowing
a storage-light follow-up of baseline expense difficulty. The exact intersection
contains 6,564 linked respondents. Among the selected linked sample, baseline
expense difficulty is followed by substantially higher June food insufficiency,
energy-bill nonpayment, and recent household job loss. High confidence in
Congress is nearly identical across the two baseline groups.

| April baseline group | June food insufficiency | June unable to pay energy bill | June recent household job loss | June high confidence in Congress |
|---|---:|---:|---:|---:|
| Expense difficulty | 12.3% (SE 1.43) | 21.4% (SE 1.36) | 11.7% (SE 1.16) | 17.2% (SE 1.38) |
| No expense difficulty | 1.1% (SE 0.42) | 2.2% (SE 0.45) | 2.9% (SE 0.36) | 16.9% (SE 1.03) |

The outcome-specific valid unweighted counts range from 2,574 to 3,961. The
table therefore adds temporal ordering and a distinct political-confidence
counterexample, but it is not a causal estimate or a general population
transition rate.

## What the chain establishes

```text
baseline expense difficulty
  -> later household material-pressure context [descriptive same-respondent link]
  -> later institutional confidence [near-flat comparison]
  -> dated bill, responsible actor, alternative, remedy, recovery, and action [open]
```

The result does not identify whether expense difficulty arose from a bill,
income interruption, health event, housing cost, debt, care, or another shock.
It also does not identify whether later food, energy, or job outcomes were
caused by the baseline condition. The near-equal Congress-confidence shares
are useful precisely because material pressure cannot be converted into a
political-legitimacy shift without attribution and a measured action route.

## Limits and next field

- The linked sample is a retained intersection; April weights and replicate
  weights are not documented as attrition-adjusted longitudinal weights.
- Expense difficulty and the June outcomes have item-specific valid universes.
- The public-use linkage does not supply a dated bill, actor, payment route,
  notice, appeal, remedy receipt, durable recovery, or practical alternative.
- Confidence in Congress is not trust in a responsible actor and is not a vote,
  complaint, organizing event, or other political action.

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
