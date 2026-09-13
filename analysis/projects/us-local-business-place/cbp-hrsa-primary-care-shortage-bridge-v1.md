# CBP health capacity and HRSA primary-care shortage bridge v1

**Checked:** 2026-09-12  
**Question:** Does a county having health-sector establishments mean it has adequate primary-care capacity?

## Result in plain words

No. The 2023 CBP and current HRSA primary-care HPSA files show that a county can have health/social-assistance establishments and still contain a designated primary-care shortage component. Among 3,072 counties with a usable CBP health-sector row and population estimate, 2,785 had at least one designated HPSA component with a county FIPS identifier in the HRSA file. The HPSA designation is therefore not a zero-establishment flag, and CBP capacity cannot substitute for provider adequacy.

The near-universality of a county appearing in the HPSA component file should not be read as “all residents of 2,852 counties lack care.” HPSAs can cover geographic areas, population groups, facilities, census tracts, or county subdivisions. This pass uses county identifiers to establish overlap and measurement limits, not to assign the entire county the same shortage.

## Sources and method

- [HRSA shortage-area data downloads](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas): primary-care HPSA data and definitions.
- [HRSA primary-care all-HPSA CSV](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv), SHA-256: `721ede7da4d4ea579d7fd54bfe705ebde3a2adfa988276e03fc2abf5ef3e66bd`.
- [Census CBP 2023 county file](https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip), SHA-256: `e9539e96ceb91608ad44ab1cfc651d7c1ff9b88bddfe7a8ff64134ccde6e9603`.
- [Census 2023 county population estimates](https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/totals/co-est2024-alldata.csv), SHA-256: `abcc8720d669e793bbfdcd440eeec37a78db3b452adbe4ccd1eadf7c72b522b9`.
- Reproduction: `python3 scripts/analyze_cbp_hrsa_primary_care_bridge.py --cbp /path/to/cbp23co.zip --population /path/to/co-est2024-alldata.csv --hpsa /path/to/BCD_HPSA_FCT_DET_PC.csv`.

The HRSA file was refreshed daily and contains current designations; it is not a frozen 2023 snapshot. The CBP stock is from 2023, so this is a cross-vintage bridge. The exact HRSA download date and checksum should be refreshed for a time-aligned study.

## Capacity overlap diagnostic

| County group | Counties | Median CBP health/social-assistance establishments per 10,000 residents | Population-weighted establishments per 10,000 |
|---|---:|---:|---:|
| County represented by a designated primary-care HPSA component | 2,785 | 23.12 | 29.87 |
| No designated primary-care HPSA component represented | 287 | 23.44 | 28.45 |

The similar CBP counts are the point: establishment presence alone does not distinguish adequate from inadequate primary-care supply. The HPSA designation adds a different institutional measurement of shortage, but its geographic components and population coverage must be inspected before making county-wide claims.

## What this contributes to the broad societal program

1. **Presence is not adequacy.** A visible health-sector stock can coexist with a formal shortage designation.
2. **Institutional classifications carry policy meaning.** HPSA designations are used across federal programs, so shortage status can affect resource allocation and political demands; that downstream effect needs separate evidence.
3. **Care access is a capacity–mobility–cost problem.** Provider supply interacts with travel, insurance, appointment availability, price, unpaid family time, and work schedules.
4. **The same pattern is socially distributed.** HPSA components can be geographic, population-based, facility-based, rural, or urban; the relevant exposed population must be identified rather than inferred from a county label.

## Boundaries and next test

This bridge does not measure appointment wait, quality, accepted insurance, clinician workload, patient travel, unmet need, or health outcomes. It does not establish that HPSA status caused a household's delayed care, work loss, debt, trust, or political action. The next test should use HRSA component boundaries and populations, provider counts, travel time, insurance, care use, and a dated household or place outcome.
