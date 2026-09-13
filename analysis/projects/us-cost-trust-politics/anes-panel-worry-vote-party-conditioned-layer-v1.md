# ANES panel financial worry, vote, and party-identity conditioning v1

**Checked:** 2026-09-13  
**Status:** official SDA weighted descriptive controlled cross-tab; no causal or variance estimate in this export

## Question

The earlier ANES panel table showed a relationship between pre-election
financial worry and post-election presidential vote. This pass conditions the
same comparison on pre-election party identification:

```text
pre-election financial worry
  + pre-election party identity
  -> post-election reported presidential vote
```

This tests whether a pooled worry/vote pattern is actually different inside
political identity groups. It does not identify a price, bill, employer, or
policy event that caused either worry or vote.

## Source and setup

The result comes from the official [ANES 2024 Full Release SDA interface](https://sda.berkeley.edu/sdaweb/analysis/?dataset=anes2024full):

- row: `V241539`, pre-election financial worry;
- column: `V242067`, post-election presidential vote;
- control: `V241227x`, pre-election party identification;
- weight: `V240106b`, post-election raked weight for the panel alone;
- filter: `V240003(1)`, the 2016–2020–2024 panel.

The table reports row percentages within each party-identification control
cell. The controlled export does not include design-based standard errors; rare
worry-by-vote cells must therefore be treated cautiously. The reusable parser
is [parse_anes_sda_worry_vote_party.py](../../../scripts/parse_anes_sda_worry_vote_party.py).
The official SDA HTML export and parsed JSON remain outside the repository.

## Selected result: Harris and Trump row percentages

| Party identity control | Financial worry | Harris | Trump |
|---|---|---:|---:|
| Strong Democrat | Extremely worried | 94.9% | 5.1% |
| Strong Democrat | Not at all worried | 99.4% | 0.4% |
| Independent | Extremely worried | 24.7% | 13.3% |
| Independent | Very worried | 25.1% | 74.9% |
| Independent | Moderately worried | 46.0% | 54.0% |
| Independent | Not at all worried | 71.6% | 21.5% |
| Strong Republican | Extremely worried | 0.0% | 100.0% |
| Strong Republican | Not at all worried | 2.3% | 97.7% |

The controlled pattern is substantively important even before modeling: among
strong partisans, reported vote is highly concentrated within the identity
group across worry categories. Among independents, worry and vote vary more
visibly together, with the very-worried cell leaning Trump and the not-at-all-
worried cell leaning Harris in this descriptive table.

This does not mean financial worry caused independent voters to choose a
candidate. The worry item is broad, identity may shape both worry reporting
and vote, the panel is a selected reinterview population, and the controlled
export lacks variance estimates. Some party/worry cells are small.

## What this adds to the broad program

1. Material concern does not enter politics through one universal channel.
2. Party identity is part of the cultural/political mechanism, not merely a
   nuisance variable to remove.
3. A pooled economic-voting result can conceal different within-identity
   patterns, especially among independents.
4. Trust, attribution, information, policy demand, turnout, and vote remain
   separate outcomes; this table measures only worry and reported vote with an
   identity condition.

The next stronger test is a design-based controlled table or longitudinal
model with financial worry, economic judgment, trust, attribution, income,
information, and prior identity together, with panel attrition and missingness
reported. It still would not substitute for a dated material exposure.
