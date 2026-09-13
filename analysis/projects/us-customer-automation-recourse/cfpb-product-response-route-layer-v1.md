# CFPB product-conditioned response-route layer v1

**Checked:** 2026-09-13  
**Status:** published complaint-system aggregation; not a consumer outcome or remedy estimate

## Question

When a consumer reaches the CFPB complaint system, what kind of institutional
endpoint is recorded, and does that route differ by product?

```text
consumer problem or dispute
  -> complaint reaches a financial firm through the CFPB system
  -> explanation, monetary relief, non-monetary relief, or untimely response
  -> verified adequacy, repeat effort, exit, trust, or dependence
```

This pass measures the middle arrow for six product slices. It does not observe
the full consumer population or the later outcomes.

## Source and method

The inputs are product-filtered 2024 CFPB Consumer Complaint Database API
aggregations already used for the product/state visibility layer. The script
extracts company-response, timeliness, narrative, and submission-channel
counts and calculates shares within each product slice. The six filtered
totals are:

| Product slice | Published complaint records |
|---|---:|
| Credit card | 76,109 |
| Checking or savings | 52,901 |
| Mortgage | 21,474 |
| Debt collection | 156,242 |
| Student loan | 14,685 |
| Vehicle loan | 13,378 |

The reusable script is [analyze_cfpb_product_response_routes.py](../../../scripts/analyze_cfpb_product_response_routes.py).
The raw API JSON and generated output remain outside the repository.

## Recorded response routes

| Product | Monetary relief | Non-monetary relief | Explanation | Untimely response |
|---|---:|---:|---:|---:|
| Credit card | 13.3% | 25.8% | 61.0% | 0.2% |
| Checking/savings | 15.0% | 7.1% | 77.8% | 0.6% |
| Mortgage | 2.1% | 2.8% | 94.8% | 1.1% |
| Debt collection | 0.2% | 29.0% | 70.4% | 1.7% |
| Student loan | 0.8% | 1.7% | 97.2% | 5.6% |
| Vehicle loan | 2.9% | 6.9% | 89.8% | 1.2% |

The category pattern is strongly product-shaped. Credit card and checking/
savings complaints have the highest recorded monetary-relief shares in this
screen. Debt collection has a high non-monetary-relief share but almost no
monetary relief. Mortgage and student-loan complaints are overwhelmingly
recorded as explanations, with student loans also showing the highest
untimely-response share.

These are differences in recorded institutional response categories, not proof
that one product causes worse consumer outcomes. Complaint mix, firm practices,
product rules, case complexity, and the population able or willing to complain
can all differ.

## Societal interpretation

The comparison supports a broad consumer-power pattern: access to a formal
route does not mean access to the same kind of remedy. A system may be highly
responsive in the administrative sense while most cases close through an
explanation; another product may record non-monetary adjustment without
recording financial restoration. The meaning of “resolved” therefore depends
on the product, the original loss, the timing, and the consumer's ability to
contest or leave.

The result strengthens the distinction between:

- complaint visibility;
- institutional response;
- monetary or non-monetary relief;
- adequate remedy;
- repeat effort or abandonment; and
- later switching, dependence, trust, or political demand.

Only the first three are partly visible here. The final three remain open.

## What this changes in the broad program

This adds product-conditioned depth to themes 3, 9, and 12: consumer recourse,
cultural meaning/trust, and firm/sector power. It also supplies a counterexample
to treating a high response rate as a uniform consumer-protection result.

The next valid test is a same-case or linked follow-up design with account
exposure, prior firm contact, verified remedy, repeat effort, switching or
continued dependence, and later trust. Complaint counts and response categories
cannot supply those outcomes by themselves.
