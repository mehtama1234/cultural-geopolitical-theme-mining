# Federal Reserve income volatility, support, and budget margin 2025 layer v1

**Checked:** 2026-09-13 · **Status:** official SHED published-table extraction

## Why this layer matters

The existing SHED price-adaptation record shows what adults say they do when prices rise. This layer adds the household room around those adaptations: where income comes from, how variable it is, whether outside support enters, whether spending is outrunning income, and which groups have month-end margin. It is a context layer, not a causal household panel.

The Federal Reserve's 2025 SHED report records 68% of adults and partners receiving labor income, 57% receiving non-labor income, 16% receiving food assistance, 3% receiving housing assistance, and 23% receiving help from someone outside the household for a listed expense. The [machine-readable record](../../records/us-federal-reserve-income-volatility-support-2025.json) preserves the distinct universes and official-page hash.

## Direct evidence

Thirty percent of adults reported income varying at least occasionally through the year, up from 28% in 2023; 11% said that income variation caused difficulty paying bills. The employment contrast is large: 58% of self-employed adults reported variability and 22% reported bill difficulty, versus 28% and 10% among adults working for someone else. This is a descriptive association, not an estimate of the causal effect of self-employment.

In 2025, 32% reported higher monthly income than a year earlier while 35% reported higher monthly spending. Forty-one percent said they always or often had money left at the end of the month, but the figure was 19% below $25,000 family income and 59% at $100,000 or more. These measures describe budget margin and direction, not balances or durable security.

Price adaptation remains widespread: 62% switched to cheaper products, 60% used less or stopped using products, 46% delayed a major purchase, 41% reduced saving, 16% increased borrowing, and 17% worked more or got another job. Eighteen percent made a major purchase earlier than planned because they expected prices to rise. Actions could be strategic, protective, or constrained, and respondents could select multiple actions.

## Mechanism under test

```text
income timing, support, and budget margin
  -> available options under price or care pressure
  -> substitution, delay, borrowing, work, or reduced saving
  -> protected or sacrificed needs and time
  -> recovery, trust, political judgment, or exit
```

The layer measures the first two stages at population level. It does not link one dated event to one respondent's action or later meaning.

## Interpretation and limits

Outside support and multiple income sources are part of household resilience, but they can also mask dependence and shift burdens across family networks. Income variability is not automatically hardship; hardship depends on buffers, timing, obligations, and alternatives. The report's percentages are not interchangeable with the 2024–2025 SHED panel or with ATUS, SIPP, CFPB, or NBER units.

The next test is a valid same-respondent or same-family design joining dated income/price/care exposure to time allocation, need protection, recovery, and attribution. Until then, this layer supports a distributional account of room and adaptation, not a full material-to-political chain.

## Reproducibility

- [Federal Reserve income and expenses report](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-income-and-expenses.htm)
- [Federal Reserve overall financial well-being report](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-overall-financial-well-being.htm)
- Local accessible HTML snapshot SHA-256: `5c62390731246d73c45cc8b5582c3ca0c05ed51a83a4bca90025e3925784902e`
