# Local capacity is only useful when people can reach an alternative

**Status:** provisional cross-source place-access finding · **Checked:** 2026-09-14

## The bounded finding

The current place evidence supports a narrower claim than “more businesses
mean better access.” County Business Patterns (CBP) shows where employer
establishments and employment are located; HRSA designations identify a
different institutional shortage surface; USDA rurality classifies place; and
NHTS shows household vehicle and travel-mode differences. Together they make a
testable option-stack hypothesis, but they do not follow the same resident to a
service, price, trip, missed appointment, or later political response.

```text
employer/service capacity
  + provider adequacy and public designation
  + vehicle, transit, and neighboring-place options
  -> reachable alternative, price, time, and failure risk
  -> work, food, care, shopping, and social participation
  -> household security, place attachment, and political demand
```

The new county four-cell pass measures a bounded option-stack context; the
lived-access and downstream arrows remain open.

## What the source layers show

| Layer | Unit, date, and denominator | Direct result | Boundary |
|---|---|---|---|
| CBP essential-sector capacity | 3,142 US counties matched to 2023 population estimates; county employer stock | Median establishments per 10,000 residents were 33.14 in retail, 22.95 in health/social assistance, 20.74 in accommodation/food, and 8.66 in manufacturing | Presence is not hours, staffing, price, quality, public provision, or use; neighboring counties and informal/mobile providers are not captured |
| CBP employment scale | Numeric employment rows within the same 2023 county file; sector-specific valid rows | Median employees per 10,000 residents were 404.91 in retail, 438.56 in health/social assistance, 290.86 in accommodation/food, and 345.10 in manufacturing | Suppressed small-county employment is not zero; employee stock is not appointment capacity or job quality |
| HRSA primary-care designation | Current primary-care HPSA file joined by county identifier to the CBP frame | 2,785 of 3,072 usable county rows had a represented designated HPSA component; median CBP health establishments were similar with and without a represented component (23.12 versus 23.44 per 10,000) | HPSA components can be geographic, population-, facility-, tract-, or subdivision-based; a county flag cannot be assigned to every resident |
| USDA RUCC context | 2023 Rural-Urban Continuum Codes joined to county records | 63.6% of the represented HPSA counties in the CBP comparison were nonmetro (codes 4–9) | Rurality is not travel time, provider acceptance, affordability, or unmet need |
| NHTS mobility context | 2022 person/household/trip survey, separate urban/rural categories | Zero-vehicle households were 9.73% urban and 2.82% rural; rideshare use was 20.05% versus 5.69%; pickup work-trip share was 12.09% versus 22.92% | NHTS urban/rural categories are not the CBP county/RUCC frame and do not identify destination success or service use |

The figures are deliberately not pooled. The CBP and HRSA layers use county
records, HRSA is a current-vintage designation over a 2023 stock, and NHTS is a
separate national survey with different geography and denominators. Similar
establishment density therefore cannot be read as similar practical access.

## County four-cell pass

The first common-geography comparison uses 3,006 counties with 2023 CBP,
population, 2023 ACS 5-year vehicle/commute, RUCC, and current HPSA context.
Health/social-assistance establishments per 10,000 residents and the share of
households with no vehicle are each split at their unweighted county median
(23.132 establishments and 5.322% zero-vehicle households). The zero-vehicle
axis is named as a constraint context, not “mobility success.”

| County cell | Counties | Population | Median health establishments / 10k | Median zero-vehicle households | Median 30+ minute commute | Median public-transit commute | Median walk commute | Median work from home | Median gross rent | Median household income | Median QCEW weekly wage | Median permitted units / 1k | Median vacancy | Median crowded units | Median limited-English share | Population-weighted HPSA representation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Low capacity / low zero-vehicle share | 839 | 38.4m | 16.43 | 3.80% | 38.31% | 0.12% | 1.56% | 8.09% | $863 | $67,071 | $944 | 2.65 | 14.09% | 1.97% | 1.69% | 84.96% |
| Low capacity / high zero-vehicle share | 664 | 27.1m | 16.85 | 7.11% | 36.59% | 0.17% | 1.68% | 6.20% | $777 | $55,250 | $913 | 1.15 | 17.51% | 2.06% | 1.57% | 95.56% |
| High capacity / low zero-vehicle share | 664 | 91.2m | 29.14 | 4.11% | 29.03% | 0.25% | 2.16% | 9.95% | $915 | $71,017 | $978 | 2.57 | 13.37% | 1.67% | 1.95% | 87.71% |
| High capacity / high zero-vehicle share | 839 | 175.7m | 30.13 | 7.18% | 26.81% | 0.45% | 2.36% | 7.94% | $879 | $61,626 | $998 | 1.51 | 13.13% | 1.84% | 1.93% | 96.91% |

The result is not a ranking of access. The high-capacity/high-zero-vehicle
cell is a useful counterexample: nominal health-sector presence is high, but
the vehicle constraint context and HPSA representation are also high. The
low-capacity/low-zero-vehicle cell is the opposite reminder that fewer visible
providers can coexist with a lower vehicle constraint share. Transit,
neighboring supply, prices, appointment availability, and quality could
reverse the practical implication in either cell.

The added ACS, QCEW, and Census Building Permits context shows that the cells also differ in the material
conditions around access: county-median household income ranges from $55,352
to $71,033, gross rent from $778 to $921, vacancy from 13.10% to 17.51%,
crowded housing from 1.67% to 2.06%, and limited-English household share from
1.57% to 1.95%; median QCEW weekly wages range from $908 to $991. QCEW is an
establishment-based average, not a median worker wage or household income. The
permit column measures authorized 2023 housing units per resident, not units
completed, occupied, affordable, or available to the households in the cell.
These are place-level economic, housing, affordability, and language
contexts—not resident service-use or interpretation measures—and they should be
carried into the next matched-place design rather than treated as outcomes.
The lower-income/lower-wage/high-zero-vehicle cell is therefore a more exposed
context than its capacity label alone would show, while the high-capacity/high-
zero-vehicle cell remains a counterexample to equating provider presence with
usable access.

The ACS mode measures add a reachability distinction: the high-capacity/high-
zero-vehicle cell has the highest county-median public-transit commute share
(0.45%) and walking share (2.36%), but not the highest work-from-home share
(7.94%). This does not mean that non-car residents can reach care or shopping;
it only shows that vehicle ownership sits inside different commuting systems.
The mode categories are work-commute measures, not destination-level service
trips, transit reliability, fare burden, or care travel.

The cell summaries use county medians for the splits and population weighting
only for HPSA and RUCC shares. ACS margins of error are not propagated in this
first pass, and the source files do not identify the same resident's service
attempt or outcome. The [machine-readable cell record](../../../records/us-cbp-acs-transport-capacity-cells-2023.json)
and [reproduction script](../../../../scripts/analyze_cbp_transport_capacity_cells.py)
preserve the thresholds, hashes, denominators, and boundary.

## What the comparison changes

### Presence and adequacy can diverge

The near similarity in CBP health-establishment density between counties with
and without a represented HPSA component is a useful counterexample to a simple
capacity story. A visible health-sector stock does not settle primary-care
adequacy. Conversely, a shortage designation does not prove that every person
in the county lacks care. The relevant exposed population and component
boundary must be recovered before assigning a household outcome.

### Capacity and mobility are different currencies

A county may have retail or health establishments while a resident lacks a
vehicle, cannot afford a trip, cannot take time away from work or care, or must
cross a county line. A rural county may have more establishments per resident
in one sector but fewer specialized alternatives; an urban county may have more
health employment while non-car travel, price, or appointment availability
still constrains use. The separate NHTS figures establish why mobility belongs
in the design, not which county is accessible.

### The firm-to-household arrow is still open

CBP and BDS can describe employer stocks and realized openings/closings, while
the New York Fed small-business layer describes firm profitability, revenue
expectations, employment, pricing power, and debt. None of those firm outcomes
alone establishes that a service stayed open, reached residents, improved
worker security, or changed local meaning. The firm/place program must keep
business health, service availability, and household access as separate
endpoints until a common geography and time window can support a join.

## Counterexamples retained

- Similar visible health capacity can coexist with different formal shortage
  designations.
- A place with low nominal capacity can be protected by neighboring supply,
  transit, telehealth, public provision, or flexible scheduling.
- A place with high establishment density can still have high prices, long
  waits, poor quality, weak insurance acceptance, or inaccessible hours.
- More vehicle access can expand reach but also reflect longer distances,
  higher fuel costs, or required travel; less vehicle ownership can coexist
  with strong transit or dense nearby services.
- More establishments do not imply more locally owned firms, good jobs,
  affordable services, or greater political voice.

These are required comparison cells, not claims that the current data have
already measured each protection.

## Next matched-place test

The four-cell screen is now complete as a context diagnostic. The next stage
must add outcomes rather than simply repeat the split. Use one common
geography and period, preferably county or commuting zone, and retain the four
pre-specified cells:

1. low nominal capacity / high mobility options;
2. low nominal capacity / low mobility options;
3. high nominal capacity / low mobility options; and
4. high nominal capacity / high mobility options.

For each cell, align sector-specific establishment and employment stock,
openings/closures, HPSA component and population boundaries, vehicle/transit
access, travel time, rents and prices, insurance/eligibility, provider hours,
appointment availability, service use, unmet need, work/care displacement,
and a direct local meaning or civic-action measure. Preserve neighboring-place
access and public provision as alternatives rather than treating local stock
as a complete supply measure.

The decisive outcome is not whether a county has more businesses. It is whether
the measured option stack changes what residents can actually reach, afford,
and rely on—and whether that experience is then associated with local trust,
belonging, organizing, or political response under a valid time and place
design.

## Sources and reproduction

- [CBP county essential-capacity layer](../cbp-county-essential-capacity-population-layer-v1.md)
- [CBP–HRSA primary-care shortage bridge](../cbp-hrsa-primary-care-shortage-bridge-v1.md)
- [Capacity and mobility cross-source bridge](../capacity-mobility-cross-source-bridge-v1.md)
- [Local capacity, practical access, care adequacy, and mobility bridge](../local-capacity-practical-access-care-mobility-bridge-v1.md)
- [2023 County Business Patterns](https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip)
- [HRSA primary-care shortage data](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas)
- [USDA Rural-Urban Continuum Codes](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes)
- [2022 National Household Travel Survey](https://nhts.ornl.gov/)

**Evidence status:** bounded cross-source place comparison. It measures
nominal capacity, institutional shortage context, rurality, and mobility
distributions in separate units; it does not estimate resident access, firm
causality, household welfare, cultural meaning, or political action.
