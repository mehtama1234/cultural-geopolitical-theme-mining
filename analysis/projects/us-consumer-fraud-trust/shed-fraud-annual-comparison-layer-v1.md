# SHED fraud burden annual comparison v1

The 2024 and 2025 Federal Reserve SHED public-use files support the same
codebook-backed fraud definitions across two separate annual respondent
samples. This adds a time comparison to the 2024 age/income screen; it is not
a repeated-person panel and the 2025 public file does not carry the 2024
account-route fields.

| Year | Respondent rows | Age 18–29 exposure | Age 45–59 exposure | Age 60+ exposure | Unrecovered, $10k–$25k | Unrecovered, $100k–$150k |
|---|---:|---:|---:|---:|---:|---:|
| 2024 | 12,295 | 6.85% | 10.25% | 9.31% | 53.78% | 22.57% |
| 2025 | 12,934 | 7.13% | 8.38% | 8.86% | 50.67% | 28.29% |

Exposure is the weighted share reporting another type of financial fraud or
scam. The unrecovered measures condition on reporters on that non-credit-card
path and use the codebook's money-loss/recovery categories. The income pattern
remains nonmonotonic in both annual samples, while the age exposure ordering
changes: ages 45–59 are highest in 2024 but not 2025. This weakens any simple
age trend claim and supports retaining annual variation as part of the atlas.

The annual files use the main survey weight and metric-specific nonmissing
denominators. Cells are descriptive and self-reported; no replicate-weight
variance is reproduced. The 2025 public file lacks `BK51`/`BK52_b`, so the 2024
P2P versus non-P2P recovery comparison is not extended across years.

```text
fraud exposure -> direct loss -> recovery burden
annual subgroup movement -> possible change in exposure/composition (open)
recovery burden -> verified provider remedy, trust, switching, or exit (open)
```

Reproduction: `python3 scripts/analyze_shed_fraud_annual_comparison.py
--input 2024=/tmp/cgm-shed/shed2024.zip --input
2025=/tmp/cgm-shed/shed2025.zip --output
analysis/projects/us-consumer-fraud-trust/data/shed-fraud-annual-comparison-2024-2025.json`.

Sources: [SHED data releases](https://www.federalreserve.gov/consumerscommunities/shed_data.htm),
[2024 codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2024codebook.pdf),
and [2024 household banking report](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm).
