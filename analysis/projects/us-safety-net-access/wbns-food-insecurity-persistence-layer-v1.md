# WBNS food insecurity persistence and unequal exposure layer v1

**Checked:** 2026-09-14  
**Status:** published-analysis layer; suitable for trend and subgroup context, not causal policy evaluation

## What this layer adds

The Urban Institute's December 2025 Well-Being and Basic Needs Survey keeps a
material-security outcome alongside the existing SNAP route layers. Among
working-age adults, reported household food insecurity was 24.0% in 2019,
fell to 19.9% in 2021, then rose to 27.2% in 2023 and remained high at 27.7%
in 2025. The published series is a population trend, not a same-person record
of a benefit change or food purchase.

The 2025 cross-section shows unequal exposure: 32.0% of working-age adults
living with children reported household food insecurity; the share was 51.0%
below 200% of the federal poverty level, 34.2% at 200–<400% FPL, and 9.3% at
400% FPL or above. Black adults (39.0%), Hispanic adults (38.8%), and adults
with disabilities (52.1%) also had higher published rates. These are overlapping
descriptive cells, not effects of race, disability, children, or income alone.

## Method and comparability

WBNS uses the six-item short form of the USDA Household Food Security Survey
Module with a 12-month reference period. It is a stratified probability sample
from Ipsos's KnowledgePanel, weighted and poststratified to CPS and ACS
benchmarks; participants may answer in English or Spanish. More than 7,500
adults ages 18–64 participated in each round through 2024, and 2025 added about
2,500 adults ages 65 and older.

The 2025 brief reports unadjusted annual trends after a methodology reassessment.
Earlier briefs used regression adjustment for sample composition and panel
conditioning. Urban reports similar recent patterns but explicitly says the
published estimates can differ slightly. The 2025 series therefore preserves
the trend signal while marking a methodology vintage rather than silently
pooling versions.

## Connection to the safety-net route program

The current safety-net evidence now has a bounded three-layer material route:

| Layer | What it observes | What remains open |
|---|---|---|
| USDA/FNA | State-level application and recertification handling | Household notice, effort, amount, and gap days |
| WBNS lived route | Recipient-reported notice, paperwork, interview, and interruption barriers | Verified case episode, remedy, and benefit amount |
| WBNS food-security trend | Household material outcome and subgroup exposure | Same-person route-to-outcome timing and causal effect |

The defensible reading is that food hardship remained elevated while route
friction and unequal exposure were also visible. The sources do not permit the
stronger claim that a reported SNAP interruption caused a particular household's
food insecurity, or that the 2025 policy changes caused the 2025 rate.

## What to test next

The next high-value test remains the public-use WBNS file and codebook: reproduce
the route variables, food-security items, weights, and exact item-specific
universes, then estimate route/outcome cells with design-based uncertainty. That
would strengthen the cross-sectional route-to-security bridge. A linked or
matched administrative episode is still required for notice date, benefit
amount, gap days, correction/appeal, and later outcome timing.

## Sources and reproducibility

- [Machine-readable observation record](../../records/us-urban-wbns-food-insecurity-persistence-2019-2025.json)
- [Urban Institute 2025 WBNS brief](https://www.urban.org/research/publication/food-insecurity-remained-high-2025-snap-cuts-loom)
- [Urban Institute brief PDF](https://www.urban.org/sites/default/files/2026-03/Food%20Insecurity%20Remained%20High%20in%202025%2C%20As%20Safety%20Net%20Cuts%20Loom%20.pdf)
- [WBNS survey program](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey)
- [Existing lived-route layer](urban-wbns-snap-recertification-interruption-layer-v1.md)
- [Existing route-to-security triangulation](public-system-route-to-security-triangulation-v1.md)

