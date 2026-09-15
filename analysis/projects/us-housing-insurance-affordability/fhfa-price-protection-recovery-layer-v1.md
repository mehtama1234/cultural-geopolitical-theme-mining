# House price, protection cost, and recovery capacity are different currencies

**Checked:** 2026-09-15  
**Source:** [FHFA HPI summary tables](https://www.fhfa.gov/data/hpi/summary-tables) and [FHFA HPI datasets](https://www.fhfa.gov/data/hpi/datasets)  
**Machine record:** [FHFA HPI 2026Q2 record](../../records/us-fhfa-house-price-index-2026q2.json)

## The bounded finding

The latest FHFA summary creates an important counterweight to any story that treats housing value, insurance, and household security as one measure. In 2026Q2, the national seasonally adjusted purchase-only FHFA index was up 2.13% over one year and 33.41% over five years. But the one-year state movement ranged from +8.30% in Alaska to −1.25% in New Mexico, a 9.55 percentage-point spread. California was −0.20%, Florida +0.96%, and Texas +0.45% in the same table.

Those are price-index movements, not household welfare results. They do not tell us whether an owner can afford insurance, produce a deductible, refinance, repair a damaged home, sell, or move. Their value for this program is diagnostic: the asset-price clock can move differently from the protection-cost clock and the recovery clock.

## What the FHFA layer measures

| Evidence unit | Current observation | What it makes visible | What remains open |
|---|---:|---|---|
| National purchase-only HPI, 2026Q2 | +0.35% quarter over quarter; +2.13% year over year; +33.41% over five years | Aggregate movement in covered single-family property values | Household equity, liquidity, affordability, insurance, debt, or realized sale |
| State purchase-only HPI, 2026Q2 | +8.30% Alaska to −1.25% New Mexico over one year | Geographic divergence inside the national result | Local hazard, insurance terms, income, migration, supply, and who owns or can enter the market |
| Selected insurance-relevant states | California −0.20%; Florida +0.96%; Texas +0.45% one year | Price movement does not have one obvious direction across high-attention insurance markets | Whether the price move reflects insurance pressure, rate conditions, composition, supply, demand, or other mechanisms |
| FHFA data architecture | Repeat-sales indexes across national, state, metro, county, ZIP, and tract-related datasets | A potential geographic bridge to hazard, insurance, and public records | A valid person/property join, consistent vintage, and comparable denominator across sources |

FHFA describes the HPI as a weighted repeat-sales measure based on repeat mortgage transactions for single-family properties whose mortgages have been purchased or securitized by Fannie Mae or Freddie Mac. That gives it broad and useful market coverage, but it also defines its boundary. This is not a survey of all owners, renters, homes, or transactions.

## The important split

The housing lane now has three separate currencies:

```text
asset value
  -> equity, collateral, sale price, or market entry condition

protection cost
  -> premium, deductible, exclusion, nonrenewal, public backstop, or uninsured loss

recovery capacity
  -> cash, credit, repair speed, temporary housing, work continuity, and ability to stay or move
```

An owner can have an appreciating home and still face a protection problem. A flat or falling local index can coexist with adequate insurance and strong household liquidity. A high asset value can be unusable if the owner cannot borrow, sell without disrupting care, or fund the deductible. The index cannot choose among these mechanisms; it tells us where a property-market comparison can begin.

## What this changes in the CBO and Federal Reserve comparison

CBO supplies the national disaster-loss and federally connected mortgage-exposure layer. The Federal Reserve supplies reported household insurance gaps and affordability pressure. FHFA supplies an observed price-market layer. They should be read together as a staged architecture:

| Stage | Best current source | Safe claim |
|---|---|---|
| Market value movement | FHFA HPI | Covered single-family property prices moved differently across places and periods |
| Disaster-loss and public exposure | CBO | Uncovered loss and federally connected mortgage exposure can be large at national/model scales |
| Household protection | Federal Reserve SHED | Some owners report no insurance, inadequate desired coverage, or premium strain |
| Same-property consequence | Not yet acquired | Need premium, deductible, mortgage, claim, repair, sale, move, and recovery records with aligned dates |

The central interpretation is deliberately modest: market value and protection are connected through housing finance but are not interchangeable. A rising HPI does not refute insurance stress. Insurance stress does not by itself predict a price decline. The open research question is where the two clocks reinforce one another and where households, lenders, insurers, or public programs absorb the divergence.

## What this does not prove

- It does not show that insurance pressure caused the state-level price differences.
- It does not estimate the price of a particular home or the equity available to a particular owner.
- It does not include renters’ housing security, landlord insurance, or displacement directly.
- It does not establish that a national or state price change produced a move, default, repair delay, or political response.
- It does not make FHFA, CBO, Federal Reserve, and NBER observations one pooled household dataset.

## The next test

The next housing-property join should preserve the separate clocks and units:

1. property location and FHFA-compatible geography;
2. HPI vintage and local price movement;
3. hazard exposure and mitigation;
4. premium, deductible, limit, exclusion, renewal, and insurer availability;
5. mortgage balance, escrow, payment trouble, modification, and sale;
6. disaster date, claim, payment, repair, temporary housing, work disruption, and move;
7. household income, liquid resources, care obligations, and alternative housing.

The useful result would not be a single “housing stress” score. It would show which households or properties experienced asset appreciation, protection strain, and recovery difficulty together or separately—and who had the option to wait, switch, borrow, repair, sell, or leave.

## What would change the finding

The working picture would weaken if price movement closely tracked adequate protection and recovery for the same properties and households, with no meaningful divergence by hazard, income, tenure, or place. It would strengthen if matched property episodes showed that insurance strain or coverage loss persisted despite stable or rising asset values, or if falling price movement magnified already unequal recovery constraints.

## Reading rule

When a source says a home “gained value,” ask: for whom, on which index, with what debt and protection cost, and could the owner actually use that value when a loss or move arrived?
