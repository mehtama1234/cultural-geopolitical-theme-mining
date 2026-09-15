# CFPB case-level route timing and visibility sample v1

**Checked:** 2026-09-13  
**Unit:** published CFPB complaint record  
**Window:** complaints received during calendar year 2024  
**Status:** capped administrative sample; not a consumer remedy rate

## Why this pass exists

The aggregate CFPB layers show that response categories and complaint
visibility change by product and year. The case-level API also exposes
`date_received` and `date_sent_to_company`, allowing a first audit of the
institutional handoff itself:

```text
consumer/other source reaches CFPB
  -> CFPB receives and sends case to company
  -> company response category and timeliness
  -> optional public response and narrative visibility
```

## Product-stratified sample

The API was queried for 500 records in retrieval order for each product. This
is a capped diagnostic sample, not a random sample or a weighted population
estimate.

| Product | Total matching records | Same-day CFPB→company send | Median hours | P90 hours | Web submission | Narrative present | Public response present |
|---|---:|---:|---:|---:|---:|---:|---:|
| Checking/savings | 52,901 | 96.6% | 0.29 | 1.30 | 90.6% | 59.8% | 47.6% |
| Credit reporting | 2,370,336 | 100.0% | 0.06 | 0.29 | 99.0% | 25.0% | 31.4% |
| Mortgage | 21,474 | 90.4% | 0.47 | 10.41 | 88.4% | 59.2% | 51.8% |
| Student loan | 14,685 | 90.0% | 0.30 | 23.72 | 94.6% | 61.8% | 46.6% |

The first route distinction is therefore not just web versus non-web. Product
systems show different tails between CFPB receipt and company routing, while
the public visibility of narratives and public company responses also differs.
In this sample, student-loan and mortgage cases have much longer routing tails
than credit-reporting cases, even though their medians remain under an hour.

Response categories differ too: checking/savings has 14.4% closed with
monetary relief in the sample, compared with 1.4% for mortgage and 1.2% for
student loans. Credit reporting is dominated by non-monetary relief in this
retrieval slice. These labels describe the published administrative record;
they do not verify that money was restored, an account was corrected, or trust
was repaired.

## Boundaries and counterexamples

- The 500 cases per product were retrieved in API order, not randomly sampled;
  no population standard error is claimed.
- `date_sent_to_company` measures CFPB routing, not company response completion
  or consumer resolution.
- Complaint submitters are not all customers, accounts, or harmed households;
  people unable or unwilling to complain are outside the frame.
- Narratives and company public responses are optional visibility fields.
- Product issue mix, company mix, publication eligibility, weekends, and
  servicing complexity can generate the differences.

A key counterexample is a complaint routed the same day that receives only an
explanation and leaves the underlying financial, time, or access problem
unchanged. Conversely, a delayed route may still precede an effective remedy.

## Reproduction

```text
python3 scripts/analyze_cfpb_case_route_sample.py \
  --date-min 2024-01-01 --date-max 2025-01-01 --sample-size 500 \
  --product "Credit reporting or other personal consumer reports" \
  --product "Mortgage" \
  --product "Student loan" \
  --product "Checking or savings account" \
  --output /tmp/cfpb-case-route-sample-2024.json
```

The [machine-readable record](../../records/us-cfpb-case-route-sample-2024.json)
preserves each product universe, sample design, route timing, visibility,
response fields, API artifact hash, and non-remedy boundary.

Official sources: [CFPB complaint database](https://www.consumerfinance.gov/data-research/consumer-complaints/),
[API documentation](https://cfpb.github.io/api/ccdb/api.html), and [field reference](https://cfpb.github.io/api/ccdb/fields.html).
