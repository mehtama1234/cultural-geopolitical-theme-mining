# Capacity and mobility cells do not carry one political response

**Status:** provisional same-county context comparison · **Checked:** 2026-09-14

## The bounded finding

The county-capacity screen can now be placed beside county-keyed 2024 CES trust,
civic-action, and reported-voting fields. In a frame of 620 counties with at
least 100,000 residents, the four capacity/mobility cells show different
political-context patterns, but no simple gradient from nominal health capacity
or zero-vehicle share to trust or action.

The join is at county context, not at the respondent's service experience:

```text
county capacity + mobility context
  -> county-keyed respondent sample
  -> trust, action, reported vote

respondent service use, local meaning, attribution, and causal response remain open
```

## Results

| Capacity/mobility cell | Counties | CES respondents | Median population change | Federal trust | State trust | Civic action | Reported voted |
|---|---:|---:|---:|---:|---:|---:|---:|
| High capacity / high zero-vehicle share | 188 | 16,262 | 0.540% | 41.385% | 55.539% | 38.616% | 97.003% |
| High capacity / low zero-vehicle share | 122 | 7,720 | 2.602% | 34.771% | 54.048% | 40.896% | 97.585% |
| Low capacity / high zero-vehicle share | 122 | 6,655 | 0.339% | 39.886% | 51.573% | 33.992% | 96.059% |
| Low capacity / low zero-vehicle share | 188 | 7,980 | 4.483% | 36.515% | 56.101% | 35.446% | 97.290% |

The high-capacity/low-zero-vehicle cell has the lowest federal-trust share
(34.77%) but the highest civic-action share (40.90%). The low-capacity/high-
zero-vehicle cell has the lowest civic-action share (33.99%), while the
high-capacity/high-zero-vehicle cell has higher federal trust (41.39%) and
similar civic action (38.62%). Reported voting is high in every cell. These
counterpatterns weaken a simple story in which visible capacity automatically
creates trust or mobility constraint automatically creates withdrawal.

## What this changes in the end-to-end program

This is the first same-county bridge from the local option-stack context to
political endpoints. It makes the next empirical question more precise: two
places with similar nominal capacity may differ in political context because
population change, party composition, housing, service quality, local history,
or respondent selection differ. Conversely, similar civic action can coexist
with different trust levels.

The comparison does not yet close the arrow. The county cell does not observe
which business, clinic, store, or public service a respondent used; whether a
trip succeeded; what cost, delay, or shortage they experienced; who they blamed;
or whether they acted because of that experience. The CES common-post weight
also does not make each county representative, and this pass does not estimate
complex-survey standard errors.

## Required next design

Use this result to select matched places rather than to rank counties. The next
design should add a defined local period and measure:

1. service availability, price, hours, wait, and neighboring alternatives;
2. respondent or household exposure and actual use;
3. local belonging, fairness, attribution, and perceived efficacy; and
4. contact, organizing, switching, turnout, or institutional response.

The capacity cells are useful sampling strata. They are not outcomes and should
not be interpreted as county-level political causes.

The [machine-readable record](../../../records/us-cces-local-capacity-trust-action-2024.json)
preserves cell denominators, valid respondent universes, weights, county
thresholds, hashes, and open arrows. The [reproduction script](../../../../scripts/analyze_ces_local_capacity_trust_action.py)
preserves the county assignment and weighted endpoint definitions.

**Evidence status:** compared. The same-county join strengthens the
capacity-to-political-context stage while leaving direct service experience,
meaning, attribution, causality, and institutional response open.
