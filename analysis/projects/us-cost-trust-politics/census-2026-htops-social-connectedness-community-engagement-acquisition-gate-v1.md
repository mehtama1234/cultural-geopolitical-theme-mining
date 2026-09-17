# Census HTOPS 2026 social-connectedness and community-engagement acquisition gate v1

**Checked:** 2026-09-17
**Source:** U.S. Census Bureau, March 2026 Household Trends and Outlook Pulse Survey tables
**Field window:** March 13–30, 2026
**Status:** source-discovery and variable-availability gate; no estimates are promoted from the linked spreadsheets

**Access recheck:** 2026-09-17; the canonical Census table URL returned an
official page-not-found response, and the linked `health3a.xlsx` and
`health3c.xlsx` URLs returned 404. The staging copy still exposes the table
names, but it does not provide a usable replacement file. This route remains
unacquired and must be rechecked before any estimate is made.

## Why this source matters

The broad program has separate evidence on material pressure, neighborhood
trust, mental health, civic participation, and informal support. The March 2026
HTOPS release is a promising bridge because one survey release contains tables
for social connectedness and community engagement alongside employment, food
sufficiency, household expenses, energy, transportation, health insurance, and
mental health.

The Census press release describes a sample of about 136,000 households and
coverage of the nation and smaller geographic areas. The detailed table page
lists the following social and cultural modules:

| Candidate table | Potential bridge | What must be checked before use |
|---|---|---|
| Feelings of Loneliness and Frequency of Social and Emotional Support | Need/pressure → perceived social support | Question wording, respondent universe, reference period, subgroup denominators |
| Social Interaction by Telephone, Video, or In-person | Contact mode → connection or substitution | Frequency categories, person versus household unit, missingness |
| Community Engagement in the Last Twelve Months | Community participation → social/civic capacity | Activity definitions, time window, overlap with formal civic action |
| In-person Arts and Entertainment Attendance | Consumer/cultural participation → place and resources | Paid/free status, geography, frequency, selection into attendance |
| Personal Creation, Practice, and Performance of Art | Cultural production → time, identity, and participation | Whether activity is hobby, work, school, or community-based |
| Available Neighborhood or Community Arts and Cultural Activities | Place capacity → practical cultural access | Availability versus use, local geography, transportation and cost |
| Difficulty Paying Usual Household Expenses | Material pressure → social/cultural participation | Same household denominator and alignment with social modules |
| Food sufficiency, employment, energy, and transportation tables | Material constraint and practical access | Whether the public tables permit compatible cross-tabulation |

## What is already established

The page establishes table availability and a common March 2026 release window;
it does not establish the numeric relationships among tables. The release is
an experimental data product. Census also notes that the March and May 2026
public-use files were corrected for a weighting error, so any microdata
acquisition must use the corrected vintage and preserve the user note.

The table page provides detailed tables, standard-error tables, technical
documentation, and data-quality material. Each listed spreadsheet is under
1 MB, but the acquisition policy still requires variable and estimand checks
before retrieval.

## Why this could close an adjacent arrow

If the public-use file or compatible tables support the same respondent or
household universe, the source could connect:

```text
expense/food/employment/energy/transport pressure
  -> loneliness or social/emotional support
  -> interaction or community/arts engagement
  -> subgroup and place differences
```

That would be a stronger same-round bridge than joining separate surveys by
calendar date. It still would not automatically establish causality, help
delivered, provider burden, later trust, political action, or recovery.

## Acquisition gate

Before downloading even the small spreadsheets, confirm:

1. corrected release vintage and table revision status;
2. household versus person respondent unit;
3. exact question wording and reference periods;
4. compatible denominators across social and material tables;
5. available geography and subgroup cells;
6. standard-error or replicate-weight support;
7. whether the PUF contains a lawful same-record cross-tab path; and
8. a pre-specified contrast, such as expense difficulty × loneliness or food
   sufficiency × community engagement.

If only separate aggregate tables are available, retain the result as a
same-release comparison and do not call it a same-household bridge. If the PUF
supports compatible records, acquire only the corrected PUF or the minimum
table files needed for one specified contrast.

## Boundary and storage note

This memo records a source route, not a new estimate. The existence of tables,
a large sample, or a common field window does not prove a relationship among
the measures. HTOPS shifted from longitudinal collection in 2025 to a
cross-sectional design beginning in March 2026. No spreadsheet, PUF, PDF, or
bulk archive was downloaded in this pass.

The current 404 condition is itself part of the provenance record: a source
listing is not equivalent to an accessible data artifact. Do not substitute a
staging URL, stale spreadsheet path, or corrected PUF without revalidating the
release and table contents.

**Official table page:** <https://www.census.gov/data/tables/2026/demo/hhp/2603.html>
**Official release note:** <https://www.census.gov/newsroom/press-releases/2026/htops-data-tables.html>
