# Project: US marketplace product safety and counterfeit risk

## Question

When unsafe or counterfeit goods enter an online marketplace, can the customer see the risk and get a remedy?

## Short first pass

Separate seller identity, review signal, product certification, listing visibility, delivery, injury, recall, refund, and enforcement.

## Matched evidence pass

- [A visible listing does not prove a safe product](../../findings/us-marketplace-product-safety-matched-evidence-001.md)
- [Reader-friendly HTML](../../../site/us-marketplace-product-safety-matched-evidence-001.html)
- [Source search record](source-search-2026-09-11.md)

The [current CPSC remedy-design finding](findings/us-product-recall-response-002.md)
adds a live implementation layer: current notices can require registration,
destruction, disposal, photographic proof, or a second repair. These
instructions expose consumer effort and evidence burden, but they do not show
notice reach, completed action, remedy receipt, or safe restoration. The next
storage-light step is one bounded recall family joined to Monthly Progress
Reports, after checking for a recall key, eligible-unit denominator, and
action/receipt fields.

The [bounded Recall API sample](data/cpsc-recall-api-bounded-sample-2026-09-17.json)
confirms that one query exposes product, units, hazard, injury, remedy, and
consumer-instruction fields without requiring the historical export. It does
not expose exposed purchasers, completed repairs, issued payments, or safely
restored units.

## Decision rule

Move on after one product-safety signal, one customer harm or recall measure, and one remedy measure. Do not treat seller verification, reviews, or a safety mark as proof that the product is safe.
