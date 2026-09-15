# Finding 008: The newer PLACES vintage moves county measures without producing one local-health trend

**Status:** provisional same-county vintage comparison · **Checked:** 2026-09-15

## The bounded finding

The CDC PLACES 2025 release allows a second county vintage to be aligned with
the 2024 release and the existing CBP capacity screen. Among 2,885 common
county FIPS with 2023 CBP health-establishment capacity, the median measures
move in different directions:

- routine-checkup prevalence rises in the full common set and in both the low-
  and high-capacity groups;
- lack of health insurance rises in both capacity groups;
- frequent mental distress is nearly flat overall, slightly down in the low-
  capacity group, and slightly up in the high-capacity group;
- transportation insecurity falls modestly in both capacity groups where the
  measure is available;
- food insecurity rises in the full common set and high-capacity group but is
  nearly flat in the low-capacity group; and
- housing and utility insecurity move by group rather than in one common
  direction.

The result is a measurement and interpretation finding:

> A newer county estimate can show movement across multiple social and health
> surfaces without establishing a single local-health trend, a capacity effect,
> or improvement for the same residents.

## Same-county comparison

| Group | Counties | Transportation | Food insecurity | Housing insecurity | Utility shut-off threat | Mental distress | Uninsured 18–64 | Routine checkup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| All common counties, 2024 median | 2,885 | 8.8% | 14.4% | 12.5% | 8.5% | 17.9% | 9.2% | 75.5% |
| All common counties, 2025 median | 2,885 | 8.5% | 15.4% | 12.2% | 8.4% | 17.9% | 10.1% | 76.8% |
| Low-capacity, 2024 → 2025 | 722 | 10.2% → 9.5% | 18.1% → 17.9% | 14.8% → 13.85% | 10.0% → 9.6% | 18.8% → 18.6% | 11.5% → 12.4% | 75.7% → 76.8% |
| High-capacity, 2024 → 2025 | 722 | 8.0% → 7.9% | 12.3% → 13.75% | 11.3% → 11.45% | 7.4% → 7.7% | 16.85% → 17.1% | 8.0% → 9.2% | 74.95% → 76.2% |

The capacity groups are defined by 2023 CBP health/social-assistance
establishments per 10,000 residents among the common counties. They are not
provider-quality groups, and the comparison does not adjust for income,
age, race, disability, rurality, insurance, migration, or neighboring-place
access.

## Why the release change matters

CDC documents that the PLACES 2024 release used 2022 BRFSS data for 36 measures
and 2021 BRFSS data for four measures, with 2022 population and ACS 2018–2022
inputs. The current 2025 release uses 2023 BRFSS data for 35 measures and 2022
BRFSS data for five carried-over measures, with 2023 population and ACS
2019–2023 inputs. CDC also documents the transition to 2020 Census geographies
and Connecticut planning regions for county equivalents.

That means the comparison is useful as a vintage check, but not as a clean
before/after estimate. A difference can reflect:

- changed BRFSS responses or sampling;
- updated population and ACS inputs in the small-area model;
- changed geography or county-equivalent construction;
- measure-definition changes, especially among social-needs fields;
- availability differences; or
- an actual change in the underlying local population.

For the selected social-needs measures, only 2,239 of the common counties have
2024 values and 2,255 have 2025 values in the extracted files. The health,
insurance, and routine-checkup measures are available for all 2,885 common
counties. Missingness is therefore part of the result, not a detail to hide
behind a national median.

## What does and does not persist from the capacity finding

The first PLACES/CBP/HRSA screen found higher modeled social need in the lowest
health-establishment-capacity quartile and nearly equal routine-checkup medians.
The vintage comparison preserves the broad level contrast but does not prove
that the contrast is stable because the social-needs universes and available
county sets differ across releases.

The routine-checkup counterexample is more durable: the high-capacity group
does not begin with a higher 2024 routine-checkup median than the low-capacity
group, yet both groups rise in the 2025 release. This weakens a simple claim
that visible local health-sector stock mechanically determines measured
routine-care use.

The insurance result points in another direction: both capacity groups show a
rise in the median modeled share lacking insurance. That movement cannot be
assigned to local establishment capacity because insurance coverage depends on
employment, policy, prices, eligibility, household composition, and survey/model
inputs beyond CBP.

## Counterexamples preserved

- A social-need measure can rise while routine-checkup estimates also rise;
  access, need, and use are distinct surfaces.
- Low-capacity counties do not show a uniform deterioration across the newer
  vintage; transportation, food, housing, utility, and mental-distress medians
  move differently.
- High-capacity counties can show higher food insecurity in the newer vintage;
  nominal provider stock does not eliminate household resource constraints.
- Same county FIPS does not mean the same respondents were measured, and same
  release name does not mean identical model inputs.
- A county with no HPSA component is not necessarily adequately served, and a
  county with one is not uniformly underserved.

## Next decisive test

The place program should now move from vintage comparison to mechanism:

1. harmonize PLACES measure definitions and available county universes across
   releases;
2. carry confidence limits and population weights into the capacity groups;
3. add component-level HRSA geography and designated populations;
4. measure neighboring-county provider access, travel time, appointment wait,
   insurance acceptance, price, and provider workload; and
5. attach a dated closure, expansion, policy, or service event to actual care
   use, delayed care, work/time displacement, or household recovery.

Only after those steps can the program test whether local capacity changes
health access or social reproduction. Trust, belonging, and political response
still require separately measured respondent meaning and action; they cannot be
inferred from the PLACES estimates.

## Reproduction and sources

- [CDC PLACES current release notes](https://www.cdc.gov/places/current-release-notes/index.html)
- [CDC PLACES methodology](https://www.cdc.gov/places/methodology/index.html)
- [2024 county release](https://data.cdc.gov/d/fu4u-a9bh)
- [2025 county release](https://data.cdc.gov/d/swc5-untb)
- [Reproduction script](../../../../scripts/analyze_places_vintage_comparison.py)
- [Committed comparison output](../data/places-vintage-comparison-summary.json)
- [Machine-readable PLACES vintage record](../../../records/us-cdc-places-vintage-comparison-2024-2025.json)
- [Capacity/outcome diagnostic](us-local-business-place-007.md)

**Evidence status:** same-county FIPS vintage comparison of CDC modeled small-
area estimates with a capacity-conditioned descriptive split. No claim of
resident-level change, causal capacity effect, health-policy evaluation,
household outcome, trust, or political response.
