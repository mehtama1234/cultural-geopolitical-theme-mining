# Project: US immigration, local demand and place

## Question

When new residents arrive, how does the added demand for local services change jobs, businesses, prices and the meaning of a place?

## Short first pass

Separate labor supply from local demand. Track services, local jobs, wages, housing costs and business entry rather than treating immigration as one market effect.

## Possible connection

New residents are workers, customers and neighbors at the same time. The customer side can create local jobs and services, while housing and service capacity may adjust more slowly.

## Decision rule

Move on after one source measures local demand and jobs, one source measures business or service change, and one next dataset can follow housing and wages in the same place. Do not turn a local average into a claim about every worker or resident.

The [migration, local demand, and sector capacity bridge](migration-capacity-sector-bridge-v1.md)
adds the first 12-county population-change screening table. The accompanying
[`analyze_migration_place_capacity_panel.py`](../../../scripts/analyze_migration_place_capacity_panel.py)
script is reproducible and explicitly treats total population change as a
proxy while adding the ACS five-year foreign-born share; arrival timing and
local demand remain separate fields to add. The panel now also accepts ACS
housing and C16001 language-access fields, without treating either as a
migrant-specific outcome.

The [all-county capacity profile](migration-capacity-all-counties-profile-v1.md)
extends the selected screen to 620 counties above 100,000 residents. It
compares population-change quartiles with retail, health/social-assistance,
and food establishments and employment, while keeping the result descriptive
and the population-change measure explicitly non-migration-specific.

The [foreign-born share and capacity profile](nativity-capacity-all-counties-profile-v1.md)
adds a separate 2023 ACS foreign-born-share axis to the same 620-county frame.
Its different sector pattern shows why population growth and foreign-born
share cannot be substituted for one another.

The [rurality sensitivity pass](capacity-rurality-sensitivity-v1.md) repeats
both comparisons inside metro and nonmetro groups. It shows that the pooled
negative growth/capacity pattern is concentrated in the metro portion of this
thresholded frame, while preserving the small nonmetro denominator.
