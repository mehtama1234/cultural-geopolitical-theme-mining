# Rotation AA: Food security, benefit access and the reliable retail route

**Date:** 2026-10-29  
**Lane:** household food security / public benefits / retail geography / health  
**Status:** Tier 1 bounded finding plus Tier 2 household-route question

## Research question

When public data show food insecurity, SNAP or WIC participation, or proximity to a food retailer, what later stages remain unobserved before the atlas can claim a reliable nutritious food route for a household?

## Conversion chain

```text
food-price/income/health/transport pressure
  -> eligibility or application
  -> benefit receipt and redemption
  -> reachable retailer and usable selection
  -> adequate nutritious food acquisition
  -> stable household food security and health
```

The key audit rule is that each arrow has a different unit and clock. A household can be eligible without participating, participate without redeeming, redeem without reaching a large retailer, and reach a store without obtaining adequate food at an affordable price.

## Evidence packet

| ID | Source and direct observation | Stage closed | Stage still open |
|---|---|---|---|
| AA1 | [USDA ERS 2024 food-security report](https://ers.usda.gov/publications/113622) estimates 86.3% of U.S. households were food secure throughout 2024; 13.7% were food insecure and 5.4% had very low food security. | Annual household-reported food-security status | Same household’s benefit, retailer, diet quality, health and later recovery route |
| AA2 | [USDA ERS statistical tables](https://ers.usda.gov/sites/default/files/_laserfiche/publications/113623/ERR-358.pdf) report 18.34 million food-insecure households and 7.202 million with very low food security in 2024. | National prevalence and severity measure | Place-specific causal route and household-level intervention effect |
| AA3 | [USDA FNS SNAP benefit-redemption analysis](https://www.fns.usda.gov/print/pdf/node/22062) reports that in FY2022 households redeemed 79.5% of benefits within two weeks and 94.4% by month end; 5.2% had at least one month with no use. | Aggregate redemption timing and retailer category | Whether redemption produced sufficient, nutritious and stable food for the same household |
| AA4 | [USDA FNS WIC coverage report](https://www.fns.usda.gov/research/wic/eer/2023) estimates WIC reached 56.1% of eligible people in an average month in 2023. | Eligibility-to-participation coverage estimate | Eligibility barriers, transaction usability, food acquisition, continuity and child health |
| AA5 | [USDA ERS Food Access Research Atlas](https://ers.usda.gov/data-products/food-access-research-atlas) separates SNAP-authorized retailer access from large-retailer access and supports straight-line and driving-distance measures. | Census-tract access indicators and method distinction | Actual trip completion, store affordability, inventory, culturally acceptable food and household purchase |

## Stage audit

| Observed signal | What it can safely establish | What it cannot establish |
|---|---|---|
| Food insecurity prevalence | A household experienced difficulty obtaining enough food at some time in the year | Which program, store, price, transport or health pathway caused or resolved it |
| SNAP redemption | Benefits were used at some point and in some retailer categories | Adequacy, nutritional quality, repeat security or absence of trade-offs |
| WIC coverage | A share of eligible people participated | That eligible nonparticipants lacked access for one reason, or that participants completed every purchase |
| Retailer distance | A modeled geographic access condition exists | Open hours, stock, price, safety, disability access, transit and actual trip completion |
| Food assistance policy | Formal eligibility and delivery rules exist | Same-household receipt, acceptance, substitution, diet quality and health outcome |

## Bounded finding

> Food insecurity, benefit participation/redemption and retailer proximity are separate measurable stages; a benefit record or a mapped retailer does not by itself establish a reliable, affordable and culturally acceptable nutritious food route for a household.

This is not a claim that SNAP, WIC or retailers are ineffective. It is a measurement and conversion claim: the public record closes aggregate or modeled stages earlier than it closes same-household acquisition, adequacy and durable security.

## Named-case refresh

These cases test whether benefit and retail mechanisms become an actual food
route in different geographies and formats:

### AA6 — Adelante Mujeres, Forest Grove, Oregon

USDA describes [Adelante Mujeres’ market model](https://www.usda.gov/sites/default/files/documents/7-Healthyfoodaccess.pdf) in Forest Grove, a community with a 27% poverty rate. The programme supported Latino and immigrant farmers, guaranteed market outlets through the farmers’ market and three apartment complexes, introduced EBT and secured a $5 SNAP match. During the grant period, weekly market foot traffic nearly doubled from 800 to 1,500 and EBT redemption rose 422%. This closes a culturally and geographically tailored benefit-to-fresh-produce route. The source does not establish household diet quality, affordability after incentives, health, repeat participation or whether the gains persisted after grant funding.

### AA7 — Tipped Trailer Co., Newport, Maine

USDA’s [Maine SNAP-Ed impact report](https://snaped.fns.usda.gov/sites/default/files/documents/FY-2024-Maine-SNAPEd-Impact-Report.pdf) describes Tipped Trailer Co., a discount grocery store in rural Newport, partnering with Bangor Public Health to use recipe-ingredient bundles and point-of-decision prompts. Penobscot County had low access to grocery stores and elevated food insecurity; the store’s local knowledge and discounted inventory were used to make healthy choices more visible and actionable. This closes part of the retailer-to-usable-choice route, not merely retailer presence. The report does not provide a randomized purchase or health outcome, nor does it establish long-run store viability, transport access or household food security.

### AA8 — USDA SNAP Online Purchasing Pilot

USDA ERS reports that the [online SNAP purchasing pilot](https://ers.usda.gov/amber-waves/2024/april/snap-online-purchasing-pilot-reduced-food-insufficiency-among-low-income-households-during-early-pandemic) reduced food insufficiency among low-income households during the early-pandemic study period, potentially helping people with disabilities or high transportation costs. Online redemption expanded from six authorized retailers in July 2020 to 341 in September 2023, and represented 8.8% of total SNAP redemptions by September 2023. This closes a digital-shopping and transportation-barrier route. It does not show that online users received affordable delivery, culturally acceptable selection, reliable substitutions or durable food security after the pandemic period.

### AA9 — Food on the Move, Rhode Island

USDA’s [project account](https://training-portal.nifa.usda.gov/web/crisprojectpages/1024568-increasing-fruit-and-vegetable-consumption-and-improving-health-status-with-food-on-the-move.html) describes Food on the Move’s SNAP incentive model and longitudinal customer surveys. The programme reported an 11% decline from baseline to 12 months in people saying they could not afford balanced healthy meals; 77% reported shopping at the market multiple times per month and 88% reported a positive or very positive experience. The work helped support Rhode Island’s statewide Eat Well, Be Well pilot. These are useful evidence of repeat use, affordability perception and policy translation. They remain programme-evaluation results, with self-selection and no complete household health or food-security counterfactual.

### AA10 — Price-over-access counterexample for SNAP households

An [ERS analysis of 882 SNAP households](https://www.ers.usda.gov/amber-waves/2015/january-february/prices-play-greater-role-than-access-in-food-purchase-decisions-for-snap-households) found that price and demographic factors were more influential than modeled food-access categories in purchase decisions; when prices were controlled, difficult access had small or negligible effects for most food groups, while a 10% price increase predicted meaningful declines in quantities purchased across all 13 groups. This is a critical counterexample to the idea that placing or mapping a retailer solves food access. The analysis is older and observational, and it does not make geography irrelevant: it shows that price, household resources and access interact and must be measured together.

### Case-ledger conclusion

The refresh closes portions of culturally targeted fresh-food production,
rural retailer choice, digital benefit redemption, repeat incentive use and
price-sensitive acquisition. It does not close the same-household chain:

`eligibility → receipt → redemption → completed trip/order → acceptable and affordable basket → diet/health → repeated food security`

Retailer presence and benefit redemption remain upstream unless the household’s
actual acquisition, substitutions, burden and later security are observed.

## Cultural and geographical interpretation

Food access is lived through the route between a household and a usable food source: time, vehicle or transit, store choice, price, identity and trust, child-care constraints, disability access, language, refrigeration and the ability to return. A national participation rate can therefore coexist with very different meanings in a rural county, a transit-poor suburb, a dense neighborhood with high prices, or a Tribal and culturally specific food system.

The cultural question is not only whether assistance exists. It is whether the household can preserve dignity, choice and continuity without converting food needs into debt, missed care, unhealthy substitution or dependence on emergency food routes.

## Counterexamples and limits

- High redemption can coexist with food insecurity; redemption is not a household food-security outcome.
- A low-access tract is a screening indicator, not proof that every resident lacks food or that every retailer is unusable.
- WIC coverage is not a simple failure score because eligibility, take-up, benefit design and household preference differ by participant category.
- ERS notes that the newer retailer-access and older large-retailer layers use different source years and methods; rapid retail change can make a map stale.
- The sources are primarily U.S. aggregate, survey, administrative and modeled evidence. They do not close a named household’s full food-to-health chain.

## Promotion decision

Promote the bounded finding to Tier 1. Keep the mechanism “benefit-to-food security conversion” in Tier 2 until a named place or panel links eligibility, receipt, redemption, completed food acquisition, affordability/quality and a later food-security or health measure for the same household or a defensible cohort.

## Next test

Build a place-based ledger combining ERS tract access, SNAP/WIC participation, retailer/trip data, prices, transit or vehicle access and repeated household food-security measures. Preserve separate columns for eligibility, receipt, redemption, acquisition, adequacy, culturally acceptable choice and later security.
