# EIA 2024 household energy-insecurity consequence layer v1

**Checked:** 2026-09-17
**Source:** US Energy Information Administration, 2024 Residential Energy Consumption Survey, Table HC11.1
**Field period:** late 2024 through early 2025; estimates describe 2024 primary-residence housing units
**Status:** infrastructure-to-household-consequence layer; not a utility shutoff administrative count, causal price estimate, or repeated-event panel

## Why this update matters

The atlas has measured prices, household financial room, food insecurity,
housing, and public-system access as separate surfaces. EIA’s new RECS table
adds a concrete infrastructure consequence: energy payment pressure can be
converted into food or medicine sacrifice, unhealthy temperatures,
disconnect/delivery-stop notices, or unusable equipment. This is a useful
bridge because it identifies the protected and sacrificed goods in the same
household-energy frame.

## Recorded findings

| Surface | Result | Boundary |
|---|---:|---|
| Any reported energy insecurity | 43.56 million of 132.54 million primary-residence homes | The table’s composite includes overlapping conditions and is not a single severity scale |
| Food or medicine tradeoff | 32.89 million homes reported reducing or forgoing food or medicine to pay energy costs | The table does not identify which item was sacrificed, duration, or whether energy service was preserved |
| Unhealthy temperature | 17.55 million homes reported leaving home at an unhealthy temperature | Temperature is self-reported and does not identify medical harm or the reason for leaving |
| Disconnect or delivery-stop notice | 16.19 million homes reported receiving one | A notice is not a completed shutoff, service loss, reconnection, or assistance outcome |
| Unusable equipment | 6.83 million homes could not use heating equipment and 8.16 million could not use air-conditioning equipment | Equipment failure and fuel/electric disruption are combined in the table definitions |
| Household income gradient | Homes below $30,000 income report 14.48 million any-insecurity homes across the published income bands; homes at $200,000 or more report 1.07 million | Published cells are counts in millions, not person-level rates; income is not liquid resources or energy burden |
| Children present | Homes with children under 18: 14.96 million any-insecurity, 11.89 million food/medicine tradeoff, and 7.25 million notice homes | The child-present and all-homes universes are not a causal comparison and conditions can overlap |
| Renting and ownership | Owned homes: 23.01 million any-insecurity; rented homes: 20.55 million | Tenure categories and payment arrangements differ; renters may have energy costs included in rent |
| Age of householder | Homes with a householder under 60: 29.88 million any-insecurity; homes with a householder 60 or older: 13.67 million | Age groups have different housing, income, health, and equipment profiles |
| Race and ethnicity | Black-alone householders: 7.46 million any-insecurity; Hispanic/Latino householders: 8.16 million; Asian-alone householders: 2.16 million | These are published housing-unit counts, not adjusted risk ratios and not causal racial effects |

## The central tension

The table shows that energy insecurity is not only an energy-market outcome.
It is a household allocation problem: a bill or service problem can be
experienced as food or medicine reduction, temperature exposure, equipment
failure, or a threat of disconnection. These are distinct consequences and
should not be averaged into a single hardship score.

The scale is also large enough to change how consumer and political trends
should be interpreted. A household that appears to maintain energy service may
be doing so by reducing food or medicine; a household that receives a notice
may still avoid an actual shutoff; and a household with unusable equipment may
face an infrastructure repair problem rather than a simple payment problem.
The evidence therefore supports a consequence map, not a claim about one
dominant mechanism.

This adds five currencies to the atlas:

1. **Service continuity:** whether heating, cooling, electricity, or fuel was
   available.
2. **Payment threat:** notice or delivery-stop exposure before confirmed loss.
3. **Substitution:** food, medicine, temperature, or other household needs
   sacrificed to preserve energy access.
4. **Equipment capacity:** whether the home could use its heating or cooling
   system.
5. **Repair and remedy:** assistance, reconnection, equipment repair, and
   later stability—which this table does not observe.

## What this changes in the broader trend map

This layer connects infrastructure dependence to consumer and health behavior
without treating energy as merely another price index. It gives the program a
concrete reason to keep housing tenure, income, children, age, fuel/payment
arrangement, and equipment capacity separate. It also creates a counterexample
to a purely market-based reading of inflation: the same nominal energy cost can
produce different consequences depending on housing, service design, and
available alternatives.

The categories also expose a measurement boundary. Food/medicine sacrifice,
unhealthy temperature, notices, and unusable equipment are not sequentially
ordered in this release. They may be different routes, simultaneous states,
or repeated events for the same home.

## Open arrows and next test

The next stronger design would join a dated bill or fuel-price exposure to
notice, shutoff, reconnection, assistance contact, equipment repair, food or
medicine tradeoff, health/work disruption, and later trust or political action.
It should identify the payer, landlord or utility responsibility, alternative
energy source, and whether help arrived before or after the sacrifice.

Until then, this is a nationally representative housing-unit consequence
surface. It does not establish that a specific price increase caused a listed
tradeoff, that all categories occurred in the same homes, or that any remedy
was received.

## Provenance and storage

No local PDF, XLSX, microdata, or bulk archive was downloaded. This memo retains
the official table URL and the reported housing-unit counts. EIA notes that
respondents may report more than one insecurity issue and that the table’s
composite does not include every possible energy-insecurity measure.

**Official table:** <https://www.eia.gov/consumption/residential/data/2024/hc/pdf/HC11.1_2024.pdf>
