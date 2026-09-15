# Household expense difficulty and institutional confidence are linked in the July pulse—but the event is missing

**Status:** replicate-weighted July 2026 cross-sectional association · **Checked:** 2026-09-14

## The bounded finding

In the July 2026 Census HTOPS/HPS public-use file, respondents who reported
some difficulty paying usual household expenses were less likely to report high
confidence in federal statistical agencies and Congress than respondents who
reported no difficulty.

The difference is substantial in the snapshot: high confidence in federal
statistical agencies was 28.8% among the difficulty group versus 43.9% among
the no-difficulty group. High confidence in Congress was 13.8% versus 20.8%.
The result is a same-round association, not evidence that the expense problem
caused distrust or that respondents took a political action.

```text
reported expense difficulty
  ↘ same-round institution-specific confidence
  [open] dated bill, blamed actor, news/source environment, action, recovery
```

## What was measured

| July 2026 respondent group | High confidence in federal statistical agencies | High confidence in Congress |
|---|---:|---:|
| Not at all difficult to pay usual expenses | 43.9% (SE 1.57 pp) | 20.8% (SE 1.26 pp) |
| At least a little difficult | 28.8% (SE 1.32 pp) | 13.8% (SE 1.25 pp) |
| Difference: difficulty minus no difficulty | −15.1 pp (SE 1.95 pp) | −6.9 pp (SE 1.75 pp) |

The approximate 90% replicate-weight intervals for the two differences are
−18.3 to −11.9 percentage points for statistical-agency confidence and −9.8
to −4.1 points for Congress. These are design-based precision diagnostics for
the cross-sectional comparison, not causal-effect intervals.

The file contains 12,755 respondents. The expense comparison classifies
`EXPENSE_DIFFICULT` as no difficulty versus any difficulty, and the confidence
outcomes classify “a great deal” or “quite a lot” as high confidence. Each
outcome has its own valid denominator because item nonresponse and routing
differ.

## Why the two institutions should remain separate

The confidence gap is larger for federal statistical agencies than for
Congress, but the measures are not interchangeable. Statistical-agency trust
can reflect whether people think public numbers describe their lives, while
Congress confidence can reflect representation, partisan identity, legislative
performance, or broader institutional judgment. A single “trust” score would
hide that distinction.

The result also does not mean that every respondent with expense difficulty
lost confidence. Some households may experience pressure while retaining
confidence in public data or legislators; others may distrust an institution
without reporting current financial difficulty. The comparison is a
distributional contrast, not a universal psychological sequence.

## What is still missing from the end-to-end path

The survey asks about recent expense difficulty and confidence in the same
release. It does not identify:

- the specific bill, price, benefit, employer, or service that produced the
  difficulty;
- whether the respondent blamed a firm, local government, Congress, a party,
  foreign actor, or no actor;
- the respondent's prior confidence or party identity before the expense
  episode;
- whether the person complained, contacted an official, organized, voted,
  switched providers, or withdrew; or
- whether the household recovered, remained under pressure, or received a
  remedy later.

The correct interpretation is therefore narrower than “hardship causes
political distrust”: current material pressure and institution-specific
confidence occupy related but separate surfaces that need a timed panel or
event record to connect.

## Reproduction and sources

- [Official July 2026 HTOPS/HPS public-use package](https://www2.census.gov/programs-surveys/demo/datasets/hhp/2026/topical/HTOPS_HPS_2607_CSV.zip)
- [Census HTOPS/HPS data page](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html)
- [Machine-readable observation](../../../records/us-census-htops-july-expense-trust-cross-tab-2026.json)
- [Reproduction audit](../data/htops-july-expense-trust-reproduction-2026-09-14.json)
- [Related three-snapshot comparison](us-cost-trust-politics-017.md)

**Evidence status:** replicate-weighted same-round cross-sectional association;
the material-to-attribution-to-action and recovery arrows remain open.
