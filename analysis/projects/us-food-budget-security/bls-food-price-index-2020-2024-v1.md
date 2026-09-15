# BLS food-at-home price index layer v1

**Checked:** 2026-09-13  
**Status:** official national price-pressure series; no household or causal
claim

The BLS CPI-U food-at-home series provides the material-price side of the food
security lane. Using the official Public Data API, this pass summarizes the 12
monthly unadjusted index observations in each calendar year. The food-at-home
annual-average index rose from 250.233 in 2020 to 306.536 in 2024. Annual
food-at-home inflation was 3.46% in 2021, 11.42% in 2022, 5.02% in 2023, and
1.19% in 2024. The 2024 value therefore indicates slower inflation, not a
return to the earlier price level.

For context, the all-items CPI-U annual-average index rose from 258.811 in
2020 to 313.689 in 2024, with annual changes of 4.70%, 8.00%, 4.12%, and
2.95% from 2021 through 2024. Food-at-home inflation exceeded all-items
inflation in 2022 and 2023, then was lower in 2024.

The values and the source response hash are preserved in the
[machine-readable trend record](../../records/us-bls-food-price-index-2020-2024.json).
The source series is [BLS CPI-U food at home, CUUR0000SAF11](https://data.bls.gov/timeseries/CUUR0000SAF11);
the API endpoint used was
`https://api.bls.gov/publicAPI/v2/timeseries/data/` with series
`CUUR0000SAF11` and `CUUR0000SA0`, years 2020–2024.

## Interpretation boundary

This series measures national price levels, not the basket or resources of a
particular household. It does not establish that price movement caused the
USDA's 2024 food-insecurity outcomes, that assistance offset the increase, or
that a lower inflation rate restored security. The next valid comparison is to
align the dated price series with food-security, earnings, SNAP timing, care,
health, local access, and recovery measures while retaining their different
units and universes.
