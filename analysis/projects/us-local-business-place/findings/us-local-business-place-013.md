# Finding 013: Marketplace visibility can become seller cost before any consumer pass-through is observed

**Status:** provisional named marketplace-power finding · **Checked:** 2026-09-17

## The bounded finding

The Federal Trade Commission and 22 state attorneys general sued Amazon in
August 2026, alleging that Amazon used undisclosed surcharges in Sponsored
Products auctions. The complaint describes more than 1 million brands and
sellers, including more than 500,000 small and medium-sized businesses, as
within the alleged scope, and alleges tens of billions of dollars in extracted
advertising revenue. It also alleges that advertisers paid their own winning
bid close to 80% of the time by 2024, despite representations about second-price
auctions.

The FTC further alleges that higher advertising costs were largely passed on
to American consumers. That is a claimed mechanism, not a measured product-
level price or household outcome in the public release.

The safe interpretation is:

> A platform can make marketplace visibility a cost-bearing dependency for
> sellers while the downstream distribution of that cost remains unmeasured.
> The complaint identifies a possible route from auction design to seller
> expense and consumer prices, but does not adjudicate the conduct or establish
> pass-through, product choice, small-business exit, or household harm.

## Event chain

```text
seller dependence on marketplace visibility
  -> sponsored-placement auction and alleged hidden surcharge
  -> seller advertising cost / bid strategy / assortment response
  -> [alleged] consumer-price pass-through
  -> [open] purchase, quality, margin, firm survival, and exit outcomes
```

## What the public record supplies

| Stage | Reported case evidence | Still open |
|---|---|---|
| Institutional action | FTC plus 22 states filed a federal complaint on August 31, 2026; legal result remained pending at the September 17 check | Adjudicated liability, remedy, and implementation |
| Advertiser scope | Complaint alleges more than 1,000,000 brands and sellers, including more than 500,000 small and medium-sized businesses | Complete affected denominator, exposure by seller, and feasible alternative channels |
| Auction mechanism | Complaint alleges advertisers paid their own winning bid close to 80% of the time in 2024, versus approximately 30–40% in 2021 and 70% in 2022 | Auction logs, seller-level charge history, bid strategy, placement, and counterfactual price |
| Revenue and incidence | FTC alleges tens of billions in advertising revenue and largely consumer-borne higher costs | Seller margins, retail prices, quantities, quality, returns, and household incidence |

These are allegations from an institutional enforcement record, not a
representative seller or consumer sample. Advertiser, seller, product, and
consumer units must not be pooled.

## Why it matters to the broader atlas

This case adds a platform-control route between firm dependence and household
cost. A seller may absorb a charge, reduce bids, change assortment, use another
channel, or continue because sponsored visibility produces enough value. A
higher advertising charge therefore does not mechanically imply a higher price
for every product or a firm exit. The unresolved question is who bears the
cost, who can switch, and whether the platform controls the visibility needed
to make switching meaningful.

Keep these states separate:

```text
alleged surcharge != adjudicated unlawful charge
advertiser scope   != measured seller incidence
seller cost        != consumer price change
price change       != household burden
continued selling  != unconstrained choice
```

## Next decisive test

The smallest useful follow-up is an identifier-bearing seller/product ledger
that preserves auction bids, charges, placement, product price, margin,
quality, purchase, return, alternative-channel use, and firm continuation or
exit. A valid design must also retain sellers that changed bids, shifted
channels, absorbed the cost, or did not advertise, and must not infer household
pass-through from the complaint's alleged mechanism alone.

## Sources and storage boundary

- [FTC and states' Amazon advertising-auction announcement](https://www.ftc.gov/news-events/news/press-releases/2026/08/ftc-states-sue-amazon-over-secret-ad-surcharge-scheme)
- [FTC Amazon marketplace case record](https://www.ftc.gov/legal-library/browse/cases-proceedings/1910129-1910130-amazoncom-inc-amazon-ecommerce)
- [NBER field-experiment comparator](https://www.nber.org/papers/w34135)
- [Structured source record](../../../records/us-ftc-amazon-ad-auction-surcharge-2026.json)

No seller, auction-log, product, purchase, or household microdata were added.
