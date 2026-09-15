# CFPB route-vintage recheck: eight product-year extracts reproduced

**Checked:** 2026-09-15  
**Status:** reproducibility/no-change control; no new consumer trend promoted

## What was rerun

The repository comparison script was rerun against the official CFPB Consumer
Complaint Database API for four products and two `date_received` windows:

- 2024: `2024-01-01` through `2025-01-01`
- 2025: `2025-01-01` through `2026-01-01`
- `size=500` retrieval-order records per product-year

The rerun produced eight observations and reproduced the existing route
measures and raw-response hashes. The comparison remains a diagnostic slice,
not a representative complaint rate or remedy estimate.

| Vintage | Product | Records | Timely = Yes | Routing >24 hours | P90 routing hours | Raw-response SHA-256 prefix |
|---|---|---:|---:|---:|---:|---|
| 2024 | Checking/savings | 500 | 99.0% | 3.4% | 1.30 | `803b2a64…` |
| 2024 | Credit reporting | 500 | 99.6% | 0.0% | 0.29 | `02ef7791…` |
| 2024 | Mortgage | 500 | 99.0% | 9.6% | 10.41 | `4b2e3613…` |
| 2024 | Student loan | 500 | 95.2% | 10.0% | 23.72 | `b1f20968…` |
| 2025 | Checking/savings | 500 | 98.4% | 33.4% | 1,342.98 | `19990954…` |
| 2025 | Credit reporting | 500 | 98.6% | 39.0% | 3,008.83 | `ffb1939f…` |
| 2025 | Mortgage | 500 | 97.4% | 30.6% | 2,533.82 | `9ad14c6e…` |
| 2025 | Student loan | 500 | 59.8% | 21.6% | 649.57 | `3ac0f49d…` |

The full hashes and field-level measures remain in the [machine-readable
comparison record](../../records/us-cfpb-case-route-vintage-comparison-2024-2025.json).
The [reproduction script](../../../scripts/analyze_cfpb_case_route_vintage_comparison.py)
performs the eight live requests.

## Interpretation

The unchanged output is a source-control result. It supports reuse of the
existing bounded finding and does not establish that routing, timeliness,
company response, or consumer remedy improved or worsened in the population.
The retrieval-order sample has no population weights, account denominator,
sampling error, verified correction, money recovered, repeat-contact measure,
switching outcome, trust measure, or exit outcome.

The next decisive consumer-power acquisition remains an account- or
consent-linked follow-up that joins the public route to the customer’s
requested outcome, effort, authority to change the decision, correction or
restoration, residual loss, dependence, switching, and trust. Until that
exists, the honest result is a stable diagnostic boundary—not an end-to-end
consumer-outcome trend.

Source: [CFPB Consumer Complaint Database API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/).
