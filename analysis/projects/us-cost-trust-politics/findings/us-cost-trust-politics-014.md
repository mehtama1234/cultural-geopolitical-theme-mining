# Financial worry does not override party identity in the same way for everyone

**Status:** official ANES SDA descriptive controlled cross-tab · **Checked:** 2026-09-14

## The bounded finding

In the retained 2016–2020–2024 ANES panel, pre-election financial worry and
post-election reported presidential vote have different descriptive patterns
inside party-identity groups. Strong partisans' reported votes are highly
concentrated across the worry categories. Independents show more visible
variation by worry level.

This is a controlled descriptive comparison, not an economic-voting estimate.
It does not identify a dated bill, price, job, policy, or household event that
caused worry or vote choice.

## Selected row percentages

The official SDA export uses pre-election financial worry (`V241539`),
post-election presidential vote (`V242067`), pre-election party identity
(`V241227x`), the panel filter (`V240003(1)`), and the post-election panel
weight (`V240106b`). Percentages are within each party-identity and worry
control cell. The export does not include design-based standard errors.

| Party identity | Financial worry | Harris | Trump |
|---|---|---:|---:|
| Strong Democrat | Extremely worried | 94.9% | 5.1% |
| Strong Democrat | Not at all worried | 99.4% | 0.4% |
| Independent | Extremely worried | 24.7% | 13.3% |
| Independent | Very worried | 25.1% | 74.9% |
| Independent | Moderately worried | 46.0% | 54.0% |
| Independent | Not at all worried | 71.6% | 21.5% |
| Strong Republican | Extremely worried | 0.0% | 100.0% |
| Strong Republican | Not at all worried | 2.3% | 97.7% |

The visible independent pattern is not a causal gradient: worry reporting,
candidate evaluation, media, retrospective judgment, prior identity, and
panel selection can all contribute. Rare cells should not be overinterpreted.

## What this adds to the political atlas

```text
material condition or perceived trajectory
  + prior identity and information environment
  -> financial worry and national judgment
  -> candidate preference, civic action, or withdrawal
```

The table measures worry and reported vote with an identity condition. It does
not measure trust change, attribution, fairness, efficacy, turnout mechanism,
direct action, institutional response, or recovery. Party identity is not only
a nuisance control: it is part of the cultural route through which an economic
judgment may be interpreted.

The counterexample is important. A pooled worry/vote association can look like
a broad economic mechanism while strong partisans remain close to their prior
candidate choice across worry categories. Conversely, independents may show
more visible co-movement without proving that worry produced the vote.

## Limits and next test

- The panel is a selected reinterview population, not a simple full-cross-
  section estimate.
- The official controlled export has no reproduced design-based standard
  errors; small worry-by-vote cells require caution.
- Financial worry is broad and not a direct measure of price, income, debt,
  work, housing, or health exposure.
- Reported presidential vote is one political endpoint; it is not trust,
  civic action, turnout mechanism, policy demand, or collective organization.
- A stronger design would add baseline trust, attribution, income, source
  environment, national/personal judgment, direct action, and a dated material
  event, with panel attrition and variance documented.

## Sources and reproduction

The [party-conditioned ANES layer](../anes-panel-worry-vote-party-conditioned-layer-v1.md)
contains the source setup, variable names, panel filter, full boundary, and
parser route. The [broader political-meaning synthesis](us-cost-trust-politics-013.md)
places this controlled comparison beside SHED, GSS, and CCES without pooling
their respondents or estimands.

**Evidence status:** official weighted descriptive controlled cross-tab; no
causal attribution, design-based contrast test, or downstream trust/action
claim.
