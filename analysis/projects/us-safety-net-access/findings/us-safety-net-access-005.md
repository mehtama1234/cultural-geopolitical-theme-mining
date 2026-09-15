# Food hardship stayed high while route exposure remained unequal

## The short finding

The Urban Institute's Well-Being and Basic Needs Survey reports that household
food insecurity among adults ages 18–64 fell from 24.0% in December 2019 to
19.9% in 2021, then rose to 27.2% in 2023 and remained high at 27.7% in 2025.
The finding is useful as a material-security baseline next to the existing SNAP
route evidence, but it is not a causal estimate of SNAP, food prices, or the
2025 policy changes.

## Persistent does not mean uniform

In December 2025, the published working-age rates were 32.0% among adults living
with children and 51.0% among adults in families below 200% of the federal
poverty level. The corresponding rates were 34.2% at 200–<400% FPL and 9.3% at
400% FPL or above. The brief also reports 39.0% among Black adults, 38.8% among
Hispanic adults, and 52.1% among adults with disabilities.

These comparisons identify where exposure is concentrated; they do not identify
the effect of belonging to a subgroup. Income, wealth, health, household size,
work, place, food prices, and public-program access are intertwined.

## The time series has a methodology boundary

WBNS uses a six-item USDA food-security short form with a 12-month reference
period. Its 2025 brief reports unadjusted estimates after a methodology
reassessment; earlier reports used regression adjustment for sample composition
and panel conditioning. The published brief says recent adjusted and unadjusted
patterns are similar but earlier differences are larger. The series can support
a bounded trend statement, not an assumption of a perfectly identical estimator
across all years.

## What it changes in the end-to-end atlas

The public-system chain is now better separated:

`material pressure / policy context → route exposure → reported interruption → household food-security outcome`

The evidence supports each component in a different source or layer. It does
not hold the same household and episode constant from the first condition to the
last outcome. The existing WBNS route layer reports that 24% of SNAP-family
respondents experienced an involuntary stop or interruption in the prior year,
including 13% who could not recertify on time; this new layer shows why the
material endpoint matters, but it cannot assign that endpoint to those route
events.

## Limits and next test

- The exact analytic denominators for the published percentages are not disclosed in the brief.
- The 12-month food-security reference period is not an event date and cannot establish sequence relative to a SNAP notice or interruption.
- The 2025 sample expanded to older adults, so the age comparison is not a continuation of the working-age trend.
- Survey weights reduce but do not eliminate nonresponse and panel-conditioning concerns.
- The report supplies significance annotations and method notes, but not a complete machine-readable variance table in the PDF.

The next test is to acquire the WBNS public-use file and codebook, reproduce
route/outcome cross-tabs with survey design and item-specific universes, and keep
the result separate from USDA administrative universes and SIPP transitions.

## Sources and reproducibility

- [Detailed WBNS persistence layer](../wbns-food-insecurity-persistence-layer-v1.md)
- [Machine-readable observation record](../../../records/us-urban-wbns-food-insecurity-persistence-2019-2025.json)
- [Urban Institute 2025 brief](https://www.urban.org/research/publication/food-insecurity-remained-high-2025-snap-cuts-loom)
- [Urban Institute 2025 brief PDF](https://www.urban.org/sites/default/files/2026-03/Food%20Insecurity%20Remained%20High%20in%202025%2C%20As%20Safety%20Net%20Cuts%20Loom%20.pdf)
- [Existing SNAP route finding](us-safety-net-access-003.md)

