# CFPB published complaint-response trend, 2020–2025 v1

**Checked:** 2026-09-13  
**Status:** annual aggregate trend in a complaint institution; not a consumer
harm, remedy, or trust trend

## Question

Did the recorded endpoint of CFPB complaints change over time, and what can
that tell us about consumer recourse?

## Method and unit

The [official CFPB complaint API](https://www.consumerfinance.gov/data-research/consumer-complaints/)
was queried separately for each calendar year received, using the documented
trailing-slash endpoint and `size=0`. Each response retained aggregate facets
for company response, timeliness, narrative presence, product, and the API's
current metadata. The reusable fetcher is
[fetch_cfpb_complaint_aggregation.py](../../../scripts/fetch_cfpb_complaint_aggregation.py);
the trend summarizer is
[analyze_cfpb_annual_response_trend.py](../../../scripts/analyze_cfpb_annual_response_trend.py).

The unit is a **published complaint record**, not a customer, account, harmed
household, or representative marketplace experience. Shares use all published
records received in the year as the denominator.

## Recorded annual response endpoints

| Year | Published records | Explanation | Non-monetary relief | Monetary relief | Untimely response | Narrative present |
|---|---:|---:|---:|---:|---:|---:|
| 2020 | 444,837 | 90.714% | 6.185% | 2.910% | 0.192% | 39.238% |
| 2021 | 496,474 | 88.071% | 8.897% | 2.859% | 0.173% | 41.049% |
| 2022 | 801,453 | 65.161% | 32.662% | 2.105% | 0.072% | 42.141% |
| 2023 | 1,293,802 | 56.227% | 42.143% | 1.575% | 0.055% | 37.713% |
| 2024 | 2,739,722 | 49.014% | 50.062% | 0.869% | 0.055% | 29.778% |

The annual counts and shares are reproducible from the five aggregate JSON
snapshots. Retrieval hashes are retained in the generated output rather than
treated as permanent facts; the 2024 snapshot hash is
`e8a179e7c2ed21936d61725ce38466495d661265eb59fccca758b903ff994f8c`.
The machine-readable observation record is [here](../../records/us-cfpb-annual-response-trend-2020-2025.json)
and is checked by `validate_trend_observation_records.py`.

## What the pattern supports

The complaint system's visible endpoint mix changed substantially. By 2024,
non-monetary relief was the largest recorded response category, while the
share marked explanation was lower than in 2020. The visible institution is
therefore not static: its product labels, response coding, routing, and
publication environment need to be tracked as part of any consumer-power
trend.

The pattern does **not** establish that consumers received better remedies.
“Non-monetary relief” can contain different actions, “explanation” can be
appropriate or inadequate, and neither category verifies restoration of money,
time, access, or trust. The falling monetary-relief share cannot be read as a
fall in recovery probability because the denominator is published complaints,
not eligible losses or accounts.

## Measurement breaks and counterexamples

The product taxonomy changed across the period: older years combine labels such
as credit card or prepaid card, 2023 contains both older and newer credit-
reporting labels, and 2024 uses the current labels. The CFPB also states that
complaints are published after a response, confirmation of a commercial
relationship, or 15 days, and that recent records can be incomplete while the
company-response window runs. These changes make a simple year-over-year
behavioral interpretation unsafe.

A genuine improvement in remedy could coexist with a lower monetary-relief
share if non-monetary correction became more effective. Conversely, a larger
non-monetary category could reflect coding or product-mix change without better
consumer outcomes. Those are required counterinterpretations, not edge cases.

## Program connection and next test

This advances themes 3, 9, and 12: consumer recourse, cultural meaning and
trust, and firm/market power. It adds time to the institutional-response arrow
without closing the customer outcome arrow.

The next valid test is a product-stable, case-level or panel design that follows
first contact, prior attempts, company response, verified remedy, repeat effort,
dependence or switching, and later trust. Preserve publication eligibility,
product taxonomy, company mix, narrative opt-in, and account denominators as
separate controls.

## Official references

- [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [CFPB complaint database API documentation](https://cfpb.github.io/api/ccdb/api.html)
- [CFPB database changes and field reference](https://cfpb.github.io/api/ccdb/fields.html)
