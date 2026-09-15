# Source search: US ACS transportation context

**Search date:** 2026-09-13  
**Geography:** United States  
**Status:** official annual context packet; first national layer completed, subgroup/place extension open

## Working question

Do annual household vehicle availability and commute-time distributions provide
an independent context for the NHTS place/income mobility-pressure findings?

## Official source set

| ID | Source | What it gives us | Evidence status | Immediate limit |
|---|---|---|---|---|
| US-ACS-2023-SF | [2023 ACS table-based 1-year summary files](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/1YRData/) | Official B08201 vehicle-availability and B08303 commute-time tables | Downloaded and hash-identified | Aggregate annual estimates; no respondent matching to NHTS |
| US-ACS-2024-SF | [2024 ACS table-based 1-year summary files](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/1YRData/) | Official B08201 vehicle-availability and B08303 commute-time tables | Downloaded and hash-identified | Aggregate annual estimates; no respondent matching to NHTS |
| US-ACS-DESIGN-2024 | [2024 ACS design and methodology](https://www2.census.gov/programs-surveys/acs/methodology/design_and_methodology/2024/acs_design_methodology_report_2024.pdf) | Sampling, dissemination, and accuracy context | Official documentation | Margin-of-error handling remains to be added to the first layer |

## Current result and next test

The [ACS annual transportation layer](../us-household-calendar-integration/acs-transport-annual-national-layer-v1.md)
shows a modest national movement from 2023 to 2024 in no-vehicle household
share and 30-plus-minute commute share. It is a corroborating context, not a
replication of the NHTS urban/rural or income cells.

The next test is state/place and income-conditioned ACS extraction with
margin-of-error-aware comparisons, followed by a bounded comparison to NHTS.
The two sources must retain their different universes, geography, and units.

The first state-context extension is now complete in the [state income layer](acs-transport-state-income-context-v1.md)
and [trend record](../../records/us-acs-transport-state-income-context-2024.json). It finds a non-monotonic pattern across state median-income quartiles, so the next pass must add explicit household-income and urban-form controls rather than treating state income as household exposure.

The [PUMS subgroup layer](acs-pums-mobility-subgroups-v1.md) now supplies that
household/person conditioning. It confirms a steep income gradient in vehicle
scarcity while showing a separate, higher long-commute pattern among higher-
income households and Black workers. The next test is design-based uncertainty
and interactions with state, urban form, transit mode, disability, and actual
transport costs.
