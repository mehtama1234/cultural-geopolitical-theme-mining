# Claims ledger: Amazon visibility and customer price

The working chain is `ad-auction charge → seller cost → seller price or margin → product visibility → customer purchase and final price`. Each step needs its own record.

| Claim to test | Needed record | Current basis | Status |
|---|---|---|---|
| Sponsored placement changes what customers see | Search page, keyword, placement, seller, product, timestamp | FTC complaint describes the placement system | Open |
| The auction charge exceeds the next competitive bid | Bid log, auction rule, winning charge, date | FTC complaint alleges hidden surcharge and near-first-price charging | Allegation only |
| Seller cost changes seller behavior | Seller ad spend, margin, price, stock, quality, exit | FTC complaint and NBER advertising model describe possible mechanisms | Open |
| Seller behavior changes customer price | Same product, seller, price, fees, delivery, date | No joined record yet | Missing |
| Placement changes customer choice | Impression, click, purchase, return, repeat purchase | NBER work gives related search mechanisms | Missing |
| The effect differs by seller size or demand | Seller size, category, demand day, auction conditions | FTC complaint identifies small and medium sellers among affected advertisers | Open |

## Data plan

Join, at the smallest useful time unit:

1. auction bids and charged amount;
2. sponsored and organic placement;
3. seller price, stock, margin, and fulfillment terms;
4. customer impression, click, purchase, return, and repeat purchase;
5. product quality and complaint records.

Compare the same seller and product before and after an auction-rule change, and compare high-demand days with ordinary days. Keep the ad charge, seller price, customer price, and customer welfare as separate outcomes.

## Stop rule

Do not turn the FTC complaint into a finding about household prices unless an independent record links the auction charge to the seller's price and the customer's final purchase.
