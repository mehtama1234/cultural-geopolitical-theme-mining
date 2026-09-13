# CFPB complaint visibility × finance-sector state context v1

**Checked:** 2026-09-13  
**Sources:** CFPB 2024 product-filtered published complaints; Census County Business Patterns 2023 state finance-sector establishments/employment; Census 2024 population estimates  
**Unit:** state context, with product-specific published complaint records  
**Status:** time-misaligned contextual comparison; not a harm, access, market-power, or causal estimate

## Why this comparison exists

Complaint visibility is partly shaped by the institutional environment in which
people use and contest financial products. A state with many finance-sector
establishments may have more nearby or employer-linked financial capacity, but
it may also have more product exposure, more complex firms, or different
complaint access. This pass places two separate state-level layers beside one
another:

```text
local finance-sector presence + product exposure/access
  -> consumer problem becomes visible through complaint channels
  -> firm/regulator response and possible remedy
```

Only presence and published visibility are measured. The middle mechanism is
not identified.

## Calculation

- CBP 2023 `NAICS 52----`, all ownership types, supplies finance/insurance
  establishments and employment by state.
- CFPB 2024 product-filtered API slices supply published complaint counts for
  credit cards, checking/savings, mortgages, debt collection, student loans,
  and vehicle loans.
- Census 2024 population supplies the rough per-resident denominator for both
  context layers.
- The years are intentionally retained rather than silently aligned: CBP is a
  2023 stock and CFPB is a 2024 complaint record.

## Selected state context

| State | Finance establishments / 100k | Finance employees / 100k | Debt-collection complaints / 100k | Credit-card complaints / 100k |
|---|---:|---:|---:|---:|
| Georgia | 136.2 | 1,814.0 | 114.6 | 31.1 |
| Texas | 134.9 | 2,057.6 | 83.8 | 32.5 |
| Florida | 155.0 | 2,022.1 | 77.7 | 31.8 |
| District of Columbia | 153.6 | 3,272.2 | 65.2 | 65.4 |
| Delaware | 190.0 | 4,333.6 | 66.9 | 38.5 |
| California | 124.7 | 1,610.1 | 35.3 | 23.6 |
| New York | 122.7 | 2,833.2 | 37.7 | 26.3 |
| North Dakota | 230.1 | 2,275.4 | 20.8 | 10.2 |
| South Dakota | 221.1 | 2,635.5 | 10.8 | 8.0 |

The contrast is deliberately not a ranking. Georgia has a lower finance-
establishment density than North Dakota but a much higher published
debt-collection complaint rate. Delaware combines high finance-sector density
with a high credit-card rate, while South Dakota has high finance-sector
density and low rates for the two displayed products. Those reversals are
counterexamples to a simple “more local finance presence means more or fewer
complaints” story.

## Quartile screen

Dividing the 51 states and D.C. into rough quartiles by finance-establishment
density produces the following unadjusted means across states:

| Establishment-density quartile | States | Mean debt-collection complaints / 100k | Mean credit-card complaints / 100k |
|---|---:|---:|---:|
| Lowest | 13 | 31.8 | 19.0 |
| Lower-middle | 13 | 40.5 | 18.2 |
| Upper-middle | 13 | 43.5 | 23.2 |
| Highest | 12 | 22.1 | 13.8 |

The non-monotonic screen is the substantive result: finance-sector presence
does not act as a one-directional proxy for consumer protection, complaint
access, or harm. The quartiles are exploratory and unweighted by state
population in the mean across states; they are not a regression or causal
estimate.

## What this adds to the broad program

1. **Firm capacity and consumer recourse are connected but not identical.**
   Establishment presence does not reveal whether consumers can switch,
   appeal, or obtain a remedy.
2. **Place context can reverse a national story.** Product-specific complaint
   geography cannot be read from total complaint volume or from finance-sector
   presence alone.
3. **The missing denominator is substantive.** Accounts, product balances,
   customer exposure, branch/digital access, income, language, and firm
   servicing volume are needed before interpreting a rate.
4. **The counterexample is productive.** High finance presence with low
   complaint visibility could mean protection, low harm, low reporting, or
   dependence; each requires a different next measurement.

## Arrow ledger

| Arrow | Status | Safe conclusion | Missing evidence |
|---|---|---|---|
| Finance-sector presence → complaint visibility | Contextual comparison | Product complaint patterns differ across states with different finance-sector stocks | Customer/account denominators, access, issue mix, and timing |
| Complaint visibility → institutional response | Available in CFPB data | Response and timeliness can be stratified by product and state with case-level data | Verified adequacy, repeat effort, and follow-through |
| Local finance capacity → consumer power | Open | Establishment/employment counts do not measure practical exit or appeal | Branch/digital access, switching, prices, terms, and consumer follow-up |
| Place/product → trust or political action | Open | State context defines a sampling frame | Same-case attribution, trust, organizing, and action |

## Limits

- CBP establishments are not branches, lenders, servicers, or consumer access
  points in a uniform sense.
- CFPB complaints are published records, not all harm or all consumers.
- State population is a rough denominator, not product exposure.
- CBP and CFPB are from different years and have different units.
- No causal ranking, market-power claim, or remedy probability is justified.

## Reproduction

```text
python3 scripts/analyze_cfpb_cbp_finance_state_context.py \
  --cbp-state /tmp/cbp23st.zip \
  --population /tmp/census-pop-2024.xlsx \
  --complaints /tmp/cfpb-product-state-rates-2024.json \
  --output /tmp/cfpb-cbp-finance-state-context.json
```

Related: [CFPB product × state complaint-rate layer](cfpb-product-state-rate-layer-v1.md),
[CBP firm/service capacity layer](../us-local-business-place/cbp-2023-sector-service-capacity-layer-v1.md),
and the [firm/market-power distribution layer](../us-local-business-place/firm-market-power-distribution-layer-v1.md).
