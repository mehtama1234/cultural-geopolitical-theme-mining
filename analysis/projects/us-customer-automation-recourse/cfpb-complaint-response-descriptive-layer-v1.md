# CFPB complaint → response descriptive layer v1

**Checked:** 2026-09-12  
**Source:** [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)  
**API endpoint:** `https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/`  
**Window:** `date_received_min=2024-01-01` through `date_received_max=2025-01-01`  
**Snapshot metadata:** last updated and indexed 2026-09-12; total database record count 17,712,347  
**Snapshot hash:** `8b772fc111e6a82075a876ecbf0ab78fdeb755a7f6357852c1b570f2b422781a` (API response)

## What was counted

The API returned **2,739,722 published complaint records** received during
calendar year 2024. These are published complaint records, not all consumer
problems or all customers.

| Field | Category | Count | Share |
|---|---|---:|---:|
| Company response | Closed with non-monetary relief | 1,371,550 | 50.062% |
| Company response | Closed with explanation | 1,342,858 | 49.014% |
| Company response | Closed with monetary relief | 23,797 | 0.869% |
| Company response | Untimely response | 1,504 | 0.055% |
| Timely response? | Yes | 2,731,969 | 99.717% |
| Timely response? | No | 7,753 | 0.283% |

The product distribution was highly concentrated:

| Product | Count | Share |
|---|---:|---:|
| Credit reporting or other personal consumer reports | 2,370,336 | 86.519% |
| Debt collection | 156,242 | 5.703% |
| Credit card | 76,109 | 2.778% |
| Checking or savings account | 52,901 | 1.931% |
| Mortgage | 21,474 | 0.784% |
| Money transfer, virtual currency, or money service | 16,772 | 0.612% |
| Student loan | 14,685 | 0.536% |
| Vehicle loan or lease | 13,378 | 0.488% |
| Payday/title/personal/advance loan | 9,052 | 0.330% |
| Prepaid card | 6,341 | 0.231% |
| Debt or credit management | 2,432 | 0.089% |

## What this adds to the broad map

The database makes an institutional sequence visible:

```text
consumer problem
  -> complaint submitted and sent to company
  -> company response category and timing
  -> possible consumer review, dispute, remedy, repeat contact, or exit
```

The 2024 records show a high share marked timely and response categories
dominated by non-monetary relief or explanation. This does **not** mean that
most problems were solved: the response category is not an independently
verified outcome, and “non-monetary relief” can mean different things. This is
evidence about the complaint-and-response institution, not a consumer welfare
rate.

Complaint volume is not harm prevalence. Credit-reporting complaints dominate
this snapshot; complaint propensity, product use, company size, referral rules,
publication rules, and ability to complain shape the counts.

## Product stratification

The same response categories vary substantially by product. Percentages below
are within each product's 2024 published records, not rates among all users of
the product.

| Product | Records | Non-monetary relief | Explanation | Monetary relief | Untimely |
|---|---:|---:|---:|---:|---:|
| Credit reporting | 2,370,336 | 54.816% | 45.132% | 0.034% | 0.017% |
| Debt collection | 156,242 | 29.015% | 70.360% | 0.247% | 0.376% |
| Credit card | 76,109 | 25.753% | 60.957% | 13.257% | 0.033% |
| Checking/savings | 52,901 | 7.125% | 77.827% | 15.007% | 0.042% |
| Mortgage | 21,474 | 2.775% | 94.789% | 2.142% | 0.293% |
| Student loan | 14,685 | 1.662% | 97.208% | 0.797% | 0.334% |

This comparison changes the interpretation of the national totals: the low
overall monetary-relief share is heavily influenced by the volume of credit-
reporting complaints, while banking and credit-card records show higher shares
in that category. The difference is descriptive and may reflect complaint
selection, issue mix, company practice, and publication rules—not different
underlying remedy probabilities.

## Firm visibility

The same API can expose named firms within a product, which adds a firm-level
layer without pretending complaint counts are market shares. In 2024 the five
largest named complaint counts were:

| Product | Largest named firms by published complaint count |
|---|---|
| Credit card | TransUnion 7,535; Equifax 7,385; Experian 7,099; Capital One 7,067; Citibank 6,695 |
| Checking/savings | JPMorgan Chase 7,047; Wells Fargo 6,816; Bank of America 5,003; Citibank 2,941; Chime 2,790 |
| Mortgage | Shellpoint Partners 2,718; Mr. Cooper 2,082; Wells Fargo 1,486; Ocwen 1,001; Freedom Mortgage 956 |

These counts describe visibility in the complaint system. They do not show
which firm has the most customers, the highest complaint rate, the greatest
harm, or the strongest market power. A valid firm comparison requires a
denominator such as accounts or servicing volume, issue mix, company size,
response timing, and independently measured outcomes.

## Limits and next test

CFPB states that complaints are published after a company response confirming a
commercial relationship or after 15 days, whichever comes first, and that the
database is not a statistical sample of marketplace experiences. Referred and
unreported problems are not represented in the same way. Company public
responses are optional, and narratives are opt-in. The data cannot estimate
the share of all customers harmed, the probability of a remedy, or the effect
on trust and switching.

Next, stratify by product, issue, company size or market share where available,
state, submission channel, response category, timeliness, and narrative
presence. Pair the complaint records with a separate survey or transaction
panel to test repeat contact, dispute, exit, trust, and later financial
condition. Do not join complaints to SIPP or ANES as if they identify the same
people. The stratified figures above are reproducible by repeating the same API
query with each `product` value and the stated date bounds; the API's current
field definitions are documented in the [CFPB field reference](https://cfpb.github.io/api/ccdb/fields.html).

Related records: [service/platform recourse bridge](../../bridges/us-service-platform-recourse-trust-v1.md),
[political-response specification](../us-cost-trust-politics/political-response-measurement-spec-v1.md),
and the [broad theme coverage matrix](../../US-BROAD-THEME-COVERAGE-MATRIX_V1.md).
