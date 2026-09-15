# Housing and insurance risk: paper scan v1

**Checked:** 2026-09-15
**Question:** When does a house remain standing but become harder to keep, finance, insure, or sell?

## What the reading adds

| Source | What it studied | Reported result | Limit | Use for the project |
|---|---|---|---|---|
| [HBS: Navigating climate risk after LA’s wildfires](https://www.library.hbs.edu/working-knowledge/navigating-climate-risk-after-los-angeles-wildfires-experts-weigh-in) | Experts’ analysis of insurance, mortgages, and disaster risk after the Los Angeles fires | Insurance and mortgage prices can signal risk, but insurance is a short-term transfer that may not provide enough money or speed after a loss. Weak insurers can fail, withdraw, and leave owners or taxpayers with the loss. | This is an expert discussion, not a household panel or a test of one policy. | Record premium, coverage, deductible, claim timing, temporary housing, and who carries the unpaid part. |
| [HBS: Who pays for wildfire and hurricane damage?](https://www.library.hbs.edu/working-knowledge/who-pays-for-wildfire-and-hurricane-damage-everyone) | Research on regulation, insurer exit, and cross-state pricing | Rules that hold prices below risk can protect owners in the short run but may push costs across places or encourage insurers to leave high-risk areas. | The discussion does not tell us what happened to each homeowner’s bill, claim, or move. | Keep price relief, availability, and public subsidy as separate outcomes. |
| [NBER: Property Insurance and Disaster Risk](https://www.nber.org/papers/w32579) | Millions of mortgage-escrow observations, property risk, premiums, and home prices | The paper reports sharply higher property-insurance premiums from 2020 to 2023, stronger risk pricing, and slower home-price growth in the most exposed ZIP codes. | Premium and price records do not show the same owner’s coverage quality, payment trouble, or decision to move. | Test whether the cost of protection changes borrowing, selling, repair, or staying. |
| [NBER: Pricing Protection](https://www.nber.org/papers/w34848) | About 70 million policies linked to mortgages and property risk | The paper reports that credit scores affect homeowners-insurance premiums alongside disaster risk; a policy change in Washington weakened that link. | A score does not explain itself. The study does not show whether the score changed, whether the premium was paid, or what the household did. | Separate risk in the property from risk assigned to the person’s financial record. |
| [NBER: Housing, Climate Risk, and Insurance](https://www.nber.org/reporter/2025number2/housing-climate-risk-and-insurance) | Research overview of housing, lenders, builders, and insurers | Climate risk affects not just insurance but housing finance, construction, values, and the wider economy. | An overview points to a field; it is not one causal estimate. | Build a connected source map without treating “climate risk” as one single cause. |
| [FHFA: House Price Index summary tables](https://www.fhfa.gov/data/hpi/summary-tables) | Weighted repeat-sales house-price indexes across national, state, metro, county, ZIP, and related geographies | In 2026Q2, the national purchase-only index was up 2.13% year over year and state one-year changes ranged from +8.30% in Alaska to −1.25% in New Mexico. | The HPI is a covered property/transaction index, not a household affordability, insurance, equity, or recovery measure. | Keep asset value, protection cost, and recovery capacity as separate clocks. |
| [CBO: Climate Change, Disaster Risk, and Homeowner’s Insurance](https://www.cbo.gov/publication/60674) | Federal insurance, flood coverage, disclosure, and housing-market evidence | Disclosure and insurance arrangements can affect home prices and federal exposure; the federal government supplies much flood coverage through NFIP. | Federal analysis does not reveal each household’s actual recovery or the full cost of staying. | Include public insurance and disclosure rules in the same chain as private premiums and mortgages. |

The CBO layer is now recorded separately in the [machine-readable CBO record](../../records/us-cbo-climate-disaster-homeowners-insurance-2024.json) and the [full federal-exposure finding](cbo-climate-insurance-federal-exposure-layer-v1.md). Its quantitative anchor is useful because it keeps three scales apart: about $80 billion of $114 billion in 2023 disaster losses was covered by insurers; about $9 trillion of federally guaranteed mortgages and mortgage securities sits in the housing-finance exposure frame; and modeled expected flood damage for homes with federally backed mortgages rises from about $190 billion under 2020 climate conditions to $258 billion under 2050 climate conditions over a 30-year present-value horizon. These are national aggregate and model results, not a household premium, claim, repair, or move estimate.

The FHFA layer is recorded in the [machine-readable HPI record](../../records/us-fhfa-house-price-index-2026q2.json) and [full price/protection/recovery finding](fhfa-price-protection-recovery-layer-v1.md). It adds the asset-value clock without turning price appreciation into household security: the national purchase-only index rose 2.13% over one year in 2026Q2, while state movement ranged from +8.30% to −1.25%. A home can gain value while insurance is unaffordable or inadequate, and a flat price index does not by itself establish a recovery problem.

## The connected picture

The deeper pattern is a change in the cost of staying put:

```text
physical risk or financial history
  -> premium, deductible, exclusion, or loss of coverage
  -> mortgage, repair, sale, or move becomes harder
  -> risk moves to the household, lender, insurer, public plan, buyer, or taxpayer
```

The house may still be there. The usable home can become smaller: less protected, harder to borrow against, harder to sell, or too costly to repair.

## Three prices that must not be merged

1. **Price of protection:** premium and deductible.
2. **Price of the asset:** home value, financing, and sale loss.
3. **Price of recovery:** uncovered damage, temporary housing, transport, storage, lost work, and delay.

A family can afford the premium but not the deductible. It can have insurance but not enough coverage. It can sell but only at a loss. It can stay by accepting more risk. “Insured” does not mean “financially safe.”

## The next bounded data test

Use the existing home-insurance source set to build a property-year ledger with:

- premium, deductible, exclusions, coverage limit, insurer, and renewal status;
- mortgage escrow, payment trouble, and required coverage;
- claim date, payment date, amount, temporary housing, repair completion, and days displaced;
- credit record before and after the premium change;
- mitigation work, public aid, sale, move, and next-home insurance cost.

Compare similar properties across risk zones and credit profiles. Keep renters in a separate path: their risk may appear through rent, landlord coverage, displacement, and contents loss rather than a homeowners premium.

## What would change the working picture

The working idea would weaken if higher risk did not raise the full cost of staying; if coverage remained available and adequate without shifting cost to households or taxpayers; or if premium changes did not affect repairs, financing, sale, moves, or the quality of protection.

## Reading rule

When a source says insurance is “available,” ask: at what price, with what deductible, for which loss, paid how quickly, and with what happens to the household afterward?
