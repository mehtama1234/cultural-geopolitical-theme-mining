# A low unemployment rate did not prevent consumer sentiment from falling

**Status:** bounded FRED aggregate time-series finding · **Checked:** 2026-09-15

## The bounded finding

From January 2024 to July 2026, the FRED series used here show three different
stories at once. The University of Michigan consumer-sentiment index fell from
79.0 to 55.2, a decline of 23.8 index points. The CPI for all urban consumers
rose from 309.698 to 332.813, a 7.5% increase in the index level. The civilian
unemployment rate was 3.7% in January 2024 and 4.1% in July 2026.

The useful result is not that prices “caused” sentiment to fall. This simple
aggregate comparison cannot establish that. It is that a relatively low
unemployment rate and a rising aggregate price level did not translate into a
single, stable public feeling about economic life. Employment conditions,
prices, expectations, politics, and household room can move on different
clocks.

| Month | Consumer sentiment | CPI | Unemployment rate |
|---|---:|---:|---:|
| January 2024 | 79.0 | 309.698 | 3.7% |
| December 2024 | 74.0 | 317.604 | 4.1% |
| December 2025 | 52.9 | 326.031 | 4.4% |
| July 2026 | 55.2 | 332.813 | 4.1% |

The December 2025 low and July 2026 partial recovery are especially important.
If sentiment were a simple mechanical reflection of the price index, the
recovery would be difficult to explain. The series instead points to a wider
interpretive field: what people expect next, how they understand political and
economic events, whether their own fixed costs have changed, and whether they
have enough buffer to absorb another shock.

## Why the aggregate comparison matters

Macroeconomic summaries often put employment, prices, and confidence in one
sentence. Households do not experience them as one statistic. A person can be
employed in a labor market with low unemployment and still face a rent reset,
insurance increase, debt payment, care interruption, or food bill that leaves
less room at the end of the month. Another person can face the same national
price level with savings, housing equity, family support, or a flexible job.

The FRED layer therefore acts as a timing screen. It tells us when the national
signals diverge. It does not tell us which people are carrying the adjustment
or what they are doing about it.

## The route into cultural and political meaning

The program’s working route is:

```text
aggregate price and labor conditions
  -> household-specific exposure and expectations
  -> perceived room, fairness, and future security
  -> confidence, blame, identity, and political judgment
  -> action, adaptation, or withdrawal
```

This FRED record reaches only the first stage and a broad public-confidence
signal. The [Federal Reserve SHED layer](../../us-cost-trust-politics/federal-reserve-2025-price-adaptation-judgment-layer-v1.md)
and household financial records are needed to observe exposure, adaptation,
buffers, and institutional judgments. The [BEA macro layer](../../../records/us-macro-price-income-labor-household-room-crosssource-2026.json)
adds income and spending flows, but it also does not identify the same
households. The [Gallup institutional-confidence finding](../../us-cost-trust-politics/findings/us-cost-trust-politics-025.md)
shows why public interpretation must be separated from the economic series:
confidence is institution-specific and politically conditioned.

## What the evidence does not establish

- The three series do not share a household or respondent denominator.
- CPI is an aggregate index, not the cost of a particular household’s basket.
- Consumer sentiment is not spending, hardship, trust, or vote choice.
- Unemployment does not measure wages, hours, job quality, debt, care, or
  whether a worker can leave a bad job.
- The timing does not identify which event, policy, price, or political message
  moved sentiment.
- FRED republishes source series that can be revised; the August 2026 sentiment
  observation was missing in the retrieved file, so July is used as the latest
  comparable sentiment month in this pass.

## Next test

The next pass should use household-level or subgroup data to split the national
screen into different exposure routes:

1. shelter, food, energy, insurance, and debt-payment changes;
2. income, hours, job transitions, and unemployment exposure;
3. liquid savings, credit access, and family or public support;
4. expectations about future prices and employment;
5. institutional blame, trust, and perceived fairness; and
6. the adaptation that followed—cutting consumption, borrowing, delaying care,
   changing work, moving, appealing, voting, organizing, or doing nothing.

The key countercells are households whose costs rose but sentiment or trust did
not fall; households with stable employment but shrinking room; households with
low sentiment but improving material conditions; and households whose confidence
recovers after a concrete improvement rather than after a national index moves.

## Sources and reproduction

- [FRED graph CSV query](https://fred.stlouisfed.org/graph/fredgraph.csv?id=UMCSENT,CPIAUCSL,UNRATE)
- [UMCSENT: University of Michigan consumer sentiment](https://fred.stlouisfed.org/series/UMCSENT)
- [CPIAUCSL: Consumer Price Index for All Urban Consumers](https://fred.stlouisfed.org/series/CPIAUCSL)
- [UNRATE: Civilian unemployment rate](https://fred.stlouisfed.org/series/UNRATE)
- [Machine-readable observation record](../../../records/us-fred-consumer-confidence-price-labor-2024-2026.json)

The record preserves the query URL and SHA-256 hash of the downloaded CSV.
Because FRED is a republisher and the raw CSV is not committed in this pass,
this is a reproducible query specification and captured-input identity, not a
fully versioned local data package.

**Bottom line:** the national labor market can look comparatively strong while
consumer confidence remains weak. That divergence is a prompt to measure
household exposure, expectations, and room to respond—not permission to infer a
single cause from three aggregate series.
