# CFPB response routes remain product-shaped in 2025

**Status:** checked · **Checked:** 2026-09-13

## One-sentence finding

The 2025 pooled CFPB shift toward “explanation” is not a uniform product
pattern: mortgage and vehicle-loan records remain explanation-dominant,
checking/savings records move sharply toward explanation, and student-loan
records show a large gap between the `timely` and `company_response` fields
that requires taxonomy and route review.

## Product-conditioned recorded endpoints

| Product | Year | Records | Explanation | Non-monetary relief | Monetary relief | Company-response untimely |
|---|---:|---:|---:|---:|---:|---:|
| Checking/savings | 2024 | 52,901 | 77.8% | 7.1% | 15.0% | 0.0% |
| Checking/savings | 2025 | 84,348 | 84.5% | 4.8% | 10.6% | 0.1% |
| Credit card | 2024 | 76,109 | 61.0% | 25.8% | 13.3% | 0.0% |
| Credit card | 2025 | 90,157 | 66.7% | 20.6% | 12.7% | 0.1% |
| Debt collection | 2024 | 156,242 | 70.4% | 29.0% | 0.2% | 0.4% |
| Debt collection | 2025 | 283,828 | 73.3% | 25.6% | 0.2% | 1.0% |
| Mortgage | 2024 | 21,474 | 94.8% | 2.8% | 2.1% | 0.3% |
| Mortgage | 2025 | 24,735 | 94.9% | 2.7% | 1.7% | 0.6% |
| Student loan | 2024 | 14,685 | 97.2% | 1.7% | 0.8% | 0.3% |
| Student loan | 2025 | 21,333 | 81.6% | 1.2% | 0.4% | 15.9% |
| Vehicle loan | 2024 | 13,378 | 89.8% | 6.9% | 2.9% | 0.3% |
| Vehicle loan | 2025 | 20,823 | 91.0% | 6.3% | 2.1% | 0.5% |

Shares are within each product-year’s published records. Categories may not
sum to 100% because the 2025 API includes an in-progress category and displayed
values are rounded. The last column is the `company_response = Untimely
response` category, not the separate `timely = No` field.

## What this changes

The pooled 2025 response shift cannot be read as a single consumer-protection
or consumer-harm trend. Product-specific routes move differently. The sharpest
new signal is student-loan timing: the `timely = No` field is 30.4% in 2025
versus 5.6% in 2024, while the separate company-response untimely category is
15.9% versus 0.3%. That is important institutional evidence, but it may reflect
servicing, routing, field-definition, or taxonomy changes and needs a targeted
data-dictionary and case-level review.

```text
product-specific problem
  -> product/firm complaint route
  -> response category and timing
  -> verified correction, financial recovery, repeat effort, exit, or trust
```

The first three stages are visible in the aggregate. The final outcomes remain
unobserved.

## Limits and counterinterpretations

- Published complaint records are not a representative sample of customers or
  all marketplace harm.
- Product-specific complaint propensity, issue mix, firm mix, and publication
  rules can change across years.
- “Explanation,” “non-monetary relief,” and “monetary relief” are recorded
  categories, not independently verified outcomes.
- The 2025 student-loan untimely result must be checked against field definitions,
  routing, servicing changes, and case-level records before interpretation.
- No account, customer, exposure, repeat-contact, switching, financial-recovery,
  or trust denominator is present.

A stronger result would link product/firm exposure to a repeated case or
consumer panel and observe contact effort, response, correction, repeat effort,
switching or dependence, and later trust. Evidence that the student-loan timing
spike disappears after a field or servicing correction would be a direct
counterexample to interpreting it as worsened recourse.

## Sources

- [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [CFPB API field reference](https://cfpb.github.io/api/ccdb/fields.html)
- [Machine-readable product-year record](../../../records/us-cfpb-product-response-routes-2024-2025.json)
