# Chicagoland local immigration attitude case v1

**Checked:** 2026-09-13  
**Unit:** adults surveyed in Chicago, suburban Cook County, and Lake County  
**Field dates:** April 13–23, 2026  
**Status:** direct local-attitude case; not a national estimate or causal place comparison

## Why this source matters

The national ANES battery measures immigration meaning and political action,
while the CES layer supplies county-keyed trust and civic context. This survey
adds the missing direct local-attitude layer for one large gateway region: it
asks residents what immigrants mean for their own community, local economy,
culture, welcome, legal immigration, citizenship, and refugee admission.

It is a case study of local meaning, not evidence that all US places think the
same way.

## Design and geography

| Area | Unweighted sample | Reported margin of error |
|---|---:|---:|
| Chicago | 758 | ±3.6 percentage points |
| Suburban Cook County | 742 | ±3.6 percentage points |
| Lake County | 400 | ±4.9 percentage points |
| Cook County total | 1,500 | ±2.5 percentage points |

The survey was conducted in English and Spanish using mixed-mode telephone
(landline and cell) and text-to-web invitations with random-digit dialing. The
reported weighting adjusted for gender, age, race/ethnicity, education, PUMA,
and 2024 presidential vote. The smaller Lake County sample is not used for
fine-grained partisan, race, or education subgroup claims.

## Direct local findings reported by the source

- About six in ten residents across Chicago, suburban Cook County, and Lake
  County say immigrants have been good for American culture, the US economy,
  their local economy, and their own communities.
- Roughly eight in ten in each area favor either increasing legal immigration
  or maintaining it at its current level; no more than 21% in any area favor a
  decrease.
- More than nine in ten say Chicago has historically been welcoming to
  immigrants.
- Support for a citizenship path for undocumented immigrants is 66% in
  Chicago, 52% in suburban Cook County, and 61% in Lake County.
- Support for allowing “Dreamers” to gain permanent legal status is 79% in
  Chicago and 72% in both suburban Cook and Lake County.
- Residents distinguish admission criteria: skills needed in the country,
  family/legal sponsors, English, and avoiding social-benefit use are not one
  interchangeable measure of welcome or exclusion.

## Comparable material/place context

The survey geography is not identical to the county panel: Chicago is inside
Cook County, while suburban Cook County is the remainder of that county. The
following county indicators therefore provide context for the survey areas;
they do not describe the city and suburbs separately.

| ACS 2024 5-year context | Cook County | Lake County |
|---|---:|---:|
| Foreign-born share | 21.75% | 19.84% |
| Foreign-born entering 2010 or later | 24.47% | 21.83% |
| Median gross rent | $1,435 | $1,477 |
| Vacant units | 7.74% | 4.49% |
| Crowded units | 3.34% | 2.93% |
| Limited-English share | 14.05% | 10.64% |

| Other dated place context | Cook County | Lake County |
|---|---:|---:|
| Population change, 2020–2023 | -2.36% | 0.11% |
| Health/social-assistance employment per 10,000 | 775.05 | 552.25 |
| Primary-care HPSA component present | Yes | Yes |

The ACS context is now one vintage closer to the April 2026 survey than the
earlier ACS 2023 extraction, but it is still a 2024 five-year estimate rather
than a same-period 2026 measure. Population change, health/social-assistance
employment, and HPSA status remain 2023 context. The two local samples can
report similar broad support for immigrants while sitting in places with
different population trajectories, vacancy, rent, language access, and
visible health employment. Those contextual differences do not explain the
survey answers by themselves. The city/suburb split still requires a
place-level source at the same geography and time.

## What this adds to the broader pattern

The local case shows that a place can hold several views simultaneously:

```text
immigrants seen as economically/culturally positive
  + legal immigration maintained or increased
  + conditional citizenship supported
  + admission criteria still evaluated and ranked
  + partisan differences remain
```

This is why the program keeps capability, distribution, cultural belonging,
fairness, legal inclusion, and political action as separate outcomes. A local
welcoming narrative does not prove that every resident benefits materially,
and support for a citizenship pathway does not imply support for every
immigration level or admission rule.

## Boundaries

1. The survey covers Cook and Lake Counties, not all six collar counties
   sometimes included in the broad Chicagoland definition and not the United
   States as a whole.
2. The published report provides weighted results and margins of error, not a
   public respondent file that can currently be joined to the project’s ACS,
   CBP, HRSA, or CES records.
3. These are reported attitudes, not observed moves, service use, labor
   outcomes, housing costs, or political action.
4. The field period is 2026. The ACS context is 2024 five-year data, while
   population, health/social-assistance employment, and HPSA context are
   2023; timing must be preserved in any comparison.
5. The survey can describe local meaning and subgroup differences; it cannot
   establish that local growth, housing pressure, or migrant arrival caused
   any answer.
6. The contextual county indicators are 2023 measures beside a survey fielded
   in 2026; they are not a same-period event record.

## Valid use in the program

Use this as a direct local counterexample beside the national ANES results and
the county-level CES trust/action context. The valid comparison is:

```text
Chicagoland direct local meaning
  + Chicagoland material/place conditions measured separately
  + national ANES meaning/action layer
  + county-keyed CES political context
```

Do not turn it into a national opinion estimate or use general county growth
as a proxy for what Chicagoland residents believe.

## Source

[Chicago Council on Global Affairs, Built by Immigrants, Shaped by Immigration](https://globalaffairs.org/research/public-opinion-survey/chicagoland-immigration-survey),
published July 13, 2026. The page reports the questionnaire scope, sample
sizes, field method, weighting variables, margins of error, and local findings.
The ACS context comes from the official 2024 table-based five-year files for
[B05002](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b05002.dat),
[B05005](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b05005.dat),
[B25002](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25002.dat),
[B25014](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25014.dat),
[B25064](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25064.dat),
and [C16001](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-c16001.dat).
The other county context comes from the project’s 2020–2023 population,
CBP 2023, and HRSA component files; the extraction is recorded in
`scripts/analyze_migration_place_capacity_panel.py`.
