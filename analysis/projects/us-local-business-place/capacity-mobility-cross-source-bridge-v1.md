# Local capacity and mobility cross-source bridge v1

**Checked:** 2026-09-12  
**Question:** When local sector capacity differs, what transport choices may mediate practical access?

## Why this bridge exists

The county CBP layers measure where employer establishments and employment are located. The NHTS layer measures household vehicles and travel modes. They are not the same sample or geography, so they cannot prove that a county with low capacity caused a particular household's travel burden. Together they define the next societal test:

```text
sector capacity in a place
  + household vehicle and mode options
  -> practical reach, travel time, fare/fuel, and failure risk
  -> work, food, care, shopping, and social participation choices
  -> household security, place attachment, and political demand
```

## Existing evidence layers

| Layer | What it measures | What it does not measure |
|---|---|---|
| [CBP county capacity](cbp-county-essential-capacity-population-layer-v1.md) | Establishments and employment per 10,000 residents in manufacturing, retail, health/social assistance, and accommodation/food | Distance, hours, quality, prices, staffing, use, or neighboring-county access |
| [RUCC capacity profile](cbp-capacity-rural-urban-profile-v1.md) | Metro/nonmetro distribution of sector establishments | Whether residents can reach or afford the capacity |
| [2022 NHTS transport comparison](../us-household-calendar-integration/nhts-transport-comparison-v1.md) | Vehicle ownership, rideshare exposure, and work-trip modes by NHTS urban/rural category | County-sector capacity, exact destination, fare, missed opportunity, or later household recovery |

## 2022 NHTS transport facts to carry forward

The weighted NHTS comparison found zero-vehicle households at 9.73% in urban areas and 2.82% in rural areas. Rideshare use in the prior 30 days was 20.05% for urban respondents and 5.69% for rural respondents. Pickup share of work trips was 12.09% urban and 22.92% rural. These are reported population patterns, not evidence that rideshare or pickup use solved a capacity gap.

The definitions are intentionally kept separate: NHTS urban/rural categories are not interchangeable with USDA RUCC metro/nonmetro codes. A future same-geography file should use one documented classification rather than treating the two comparisons as a direct join.

## What this contributes to the broad societal question

The practical access problem is not simply “how many businesses are nearby?” It is the interaction of local provision and the ability to reach alternatives. A county can have retail establishments but poor vehicle access; a nonmetro county can have more establishments per resident but still require longer trips to specialized care; a metro county can have high care employment while residents face non-car travel or cost constraints. Those are hypotheses to test, not conclusions from the separate layers.

## Next bounded test

Use a common geography and period to combine sector capacity, establishment employment, RUCC or another documented place class, vehicle access, commute/travel time, and service-use or unmet-need measures. Compare low-capacity/high-mobility, low-capacity/low-mobility, and high-capacity/low-mobility places. Include price, hours, quality, public provision, and neighboring-place access before interpreting differences as consumer, cultural, or political trends.
