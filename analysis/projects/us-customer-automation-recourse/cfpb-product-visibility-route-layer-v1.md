# CFPB product-conditioned visibility and submission-route layer v1

**Checked:** 2026-09-13  
**Unit:** published CFPB complaint record, product-filtered 2024 API
aggregation  
**Status:** descriptive institutional-visibility comparison; not a harm,
access, remedy, or consumer-population rate

## The question

The complaint system does not only record what a company did. It also filters
which problems become visible and how consumers' accounts enter the system.
This pass separates narrative presence from submission channel across six
products.

```text
problem or dispute
  -> route into complaint system
  -> account becomes narratable and publicly recordable
  -> company response and possible remedy
  -> trust, repeat effort, switching, or dependence
```

The first three stages are only partially visible here. The final outcomes are
not measured.

## Product-conditioned visibility

| Product | Published records | Narrative present | Web | Phone | Referral | Postal mail |
|---|---:|---:|---:|---:|---:|---:|
| Credit card | 76,109 | 46.7% | 91.9% | 3.9% | 3.3% | 0.9% |
| Checking/savings | 52,901 | 55.8% | 82.8% | 7.7% | 8.7% | 0.8% |
| Mortgage | 21,474 | 57.0% | 85.5% | 7.7% | 5.4% | 1.4% |
| Debt collection | 156,242 | 45.1% | 98.5% | 1.1% | 0.2% | 0.2% |
| Student loan | 14,685 | 54.8% | 94.5% | 2.5% | 2.7% | 0.2% |
| Vehicle loan/lease | 13,378 | 56.5% | 90.0% | 6.2% | 3.0% | 0.7% |

The route is strongly web-dominant in every product, but not uniformly so.
Debt-collection records are the most web-concentrated and have the lowest
narrative-present share in this comparison. Checking/savings and mortgage
records show more phone and referral submissions and higher narrative presence.
These differences are product-conditioned features of the recorded complaint
population, not estimates that one product's customers are more articulate or
that a channel caused a better response.

## What this adds to the broad societal map

1. **Consumer voice is institutionally filtered.** The public record reflects
   the route a person used, whether a narrative was present, and whether the
   record passed publication rules—not just the underlying problem.
2. **Digital participation is not one uniform consumer condition.** A nearly
   all-web product route and a route with more phone/referral use may imply
   different practical access, assistance, or problem types, but the database
   cannot identify which explanation is correct.
3. **Product rules shape cultural visibility.** A debt-collection dispute,
   mortgage problem, and checking-account problem may reach the same agency
   through different narrative and channel mixes. “Consumer experience” must
   retain product and route context.
4. **Voice is separate from remedy.** A narrative can be present without a
   monetary correction; a record without a narrative can still receive a
   response. The response-route layer and this visibility layer should not be
   collapsed.

## Arrow status

| Arrow | Status | Safe conclusion | Missing evidence |
|---|---|---|---|
| Product → submission route | Compared | Web, phone, referral, and postal shares differ by product | User access, assistance, account exposure, and failed attempts |
| Route → narrative visibility | Compared at product level | Narrative presence varies across product slices | Case-level route/narrative joint records and reasons for missing narratives |
| Narrative/route → response | Open in this aggregate | Response categories can be measured separately | Joint case-level response, issue, route, and narrative analysis |
| Response → remedy/trust/exit | Open | A recorded response is not verified recovery | Repeat contact, correction, switching, dependence, and later trust |

## Boundaries and counterexamples

- These are published complaint records, not all consumers, complaints, or
  failed attempts.
- “Narrative absent” does not mean the consumer had no account or no reason;
  it may reflect field choice, publication, redaction, or workflow.
- Submission channel is not a direct measure of digital access or demographic
  status.
- Product slices differ in issue mix, firm practices, customer population, and
  complaint propensity. The comparison does not estimate a channel effect.
- The counterexample is built into the data: products with higher narrative
  presence do not necessarily have lower web dependence or more recorded
  monetary relief.

## Reproduction

```text
python3 scripts/analyze_cfpb_product_visibility_routes.py \
  --slice credit-card=/path/to/cfpb-credit-card-2024.json \
  --slice checking-savings=/path/to/cfpb-checking-savings-2024.json \
  --slice mortgage=/path/to/cfpb-mortgage-2024.json \
  --slice debt-collection=/path/to/cfpb-debt-collection-2024.json \
  --slice student-loan=/path/to/cfpb-student-loan-2024.json \
  --slice vehicle-loan=/path/to/cfpb-vehicle-loan-2024.json \
  --output /tmp/cfpb-product-visibility-routes.json
```

The reusable analysis is [analyze_cfpb_product_visibility_routes.py](../../../scripts/analyze_cfpb_product_visibility_routes.py).
Raw API JSON and generated output remain outside the repository.

Related: [CFPB product response-route layer](cfpb-product-response-route-layer-v1.md),
[recourse visibility and remedy layer](cfpb-recourse-visibility-remedy-layer-v1.md),
and the [consumer recourse/power/exit bridge](consumer-recourse-power-exit-cross-source-bridge-v1.md).
