# ANES panel: economic judgment, institutional trust, and political action

**Checked:** 2026-09-12  
**Status:** official SDA descriptive cross-tabs recorded; causal interpretation explicitly out of scope.

## Why this layer matters

The broader question is how material conditions become political and cultural meaning at population scale. The ANES panel gives one bounded bridge:

```text
reported financial worry
  -> judgment about federal government
  -> reported presidential vote choice
```

This is not a claim that a particular bill, price, or household hardship caused a vote. Worry is a political-attitude measure, not a direct measure of a price or expense. Party identity, information, retrospective judgment, candidate preference, and other conditions may shape every link.

## Source and population

The [official 2016–2020–2024 ANES Panel Merged Study](https://electionstudies.org/data-center/2016-2020-2024-panel-merged-study/) contains nine waves. The 2024 panel includes 2,171 pre-election interviews and 2,070 post-election reinterviews. The official [2024 Time Series Study page](https://electionstudies.org/data-center/2024-time-series-study/) identifies the panel weights used for the pre- and post-election interviews.

The estimates below use the official [ANES 2024 Full Release SDA interface](https://sda.berkeley.edu/sdaweb/analysis/?dataset=anes2024full), filtered to `V240003(1)`, the 2016–2020–2024 panel subset. They are weighted descriptive cross-tabs with complex-design standard errors. The panel is not the full 2024 cross-section: it represents respondents who remained in the multi-election panel.

## Recorded descriptive comparisons

### Pre-election financial worry × pre-election trust in the federal government

Valid weighted observations: 2,154. Rows are levels of worry; columns are trust responses. Percentages are row percentages, with complex-design standard errors in parentheses.

| Financial worry | Always | Most of the time | About half | Some of the time | Never |
|---|---:|---:|---:|---:|---:|
| Extremely worried | 0.9 (0.71) | 8.9 (2.94) | 19.8 (4.64) | 37.2 (5.26) | 33.1 (5.61) |
| Very worried | 0.0 | 11.5 (2.94) | 26.3 (4.04) | 42.4 (5.38) | 19.8 (4.10) |
| Moderately worried | 1.5 (0.68) | 7.6 (1.33) | 29.2 (2.98) | 43.3 (3.24) | 18.3 (2.32) |
| A little worried | 1.5 (0.99) | 10.8 (1.29) | 34.0 (2.43) | 42.9 (2.61) | 10.8 (1.38) |
| Not at all worried | 1.4 (0.69) | 20.6 (2.27) | 26.0 (2.30) | 39.3 (2.98) | 12.6 (1.98) |

The descriptive pattern is non-monotonic rather than a simple “more worry, less trust” result. The extremely worried group has 70.3% in “some” or “never” trusting categories; the not-at-all worried group has 51.9%. This is a signal for further modeling, not a finished explanation.

### Pre-election financial worry × post-election presidential vote

Valid weighted observations: 1,699. Rows are pre-election worry; columns are the candidate reported in the post-election interview. Percentages are row percentages, with complex-design standard errors in parentheses.

| Financial worry | Harris | Trump | West | Stein | Other |
|---|---:|---:|---:|---:|---:|
| Extremely worried | 36.9 (8.50) | 55.4 (8.23) | 1.6 (1.59) | 0.7 (0.69) | 5.3 (3.78) |
| Very worried | 29.9 (4.75) | 68.9 (4.89) | 0.0 | 0.0 | 1.3 (0.94) |
| Moderately worried | 44.7 (3.23) | 51.8 (3.27) | 0.0 | 1.6 (1.30) | 1.9 (1.32) |
| A little worried | 56.2 (2.88) | 41.5 (2.91) | 0.9 (0.53) | 0.5 (0.40) | 0.9 (0.56) |
| Not at all worried | 66.5 (3.25) | 32.0 (3.19) | 0.2 (0.20) | 0.3 (0.33) | 0.9 (0.42) |

Because worry is measured before the election and vote is reported after it, this is a temporal descriptive layer. It still does not identify a causal effect. Candidate self-report is not independently validated here, and the comparison remains confounded by political identity and prior beliefs.

## What this adds to the larger program

This layer helps distinguish four population-level questions that are often collapsed:

1. Are people experiencing material worry?
2. Do they interpret institutions as trustworthy or untrustworthy?
3. Do they translate that interpretation into a political choice?
4. Which cultural narratives, identities, and organized actors make that translation plausible?

The ANES cross-tabs address only the first three, and only descriptively. The next breadth/depth pass should connect them to SHED adaptation paths, inflation and housing/insurance exposure, media and platform environments, turnout/participation, and policy or firm decisions. That is how this remains a societal trend-mining program rather than a household case study.

## Reproduction boundary

The underlying panel download endpoint returned the publisher’s web-challenge HTML in this environment, so these estimates were obtained through the official SDA interface rather than a locally reproduced microdata script. Preserve the SDA query settings and archive the panel file when direct retrieval is available. Until then, treat this as a recorded official descriptive result, not a fully auditable local replication.

The two panel comparisons are preserved in the machine-readable [trend
record](../../records/us-anes-panel-worry-trust-vote-2024.json), retaining the
valid cross-tab denominators and the non-monotonic/counteridentity boundaries.
