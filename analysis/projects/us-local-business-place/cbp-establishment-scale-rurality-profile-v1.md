# CBP establishment scale by sector and rurality v1

**Checked:** 2026-09-12
**Status:** descriptive firm-size profile; not a concentration, productivity, or service-adequacy estimate

## Why this dimension matters

An establishment count describes presence, while employment describes the
labor footprint attached to that presence. Their ratio provides a rough scale
diagnostic: whether the typical county-sector establishment is relatively
small or large. It helps prevent “more establishments” from being treated as
more jobs, more service hours, or more bargaining power.

```text
sector/place conditions
  -> number of employer establishments and employees
  -> establishment scale and labor footprint
  -> work options, service capacity, local dependence, and bargaining questions
```

## Method

The analysis uses numeric 2023 CBP `est` and `emp` values for each county and
2-digit sector, retaining only positive establishment counts and a numeric
employment value. It reports the county-level median of `emp / est`, not a
population-weighted national average. USDA 2023 RUCC codes divide counties
into metro (1–3) and nonmetro (4–9). Suppressed or absent values are excluded,
not treated as zero.

Reproduce with:

```text
PYTHONPATH=scripts python3 scripts/analyze_cbp_sector_establishment_scale.py \
  --cbp /path/to/cbp23co.zip \
  --rucc /path/to/rucc2023.csv
```

## Selected 2023 results

| Sector | All counties median employees/establishment | Metro | Nonmetro |
|---|---:|---:|---:|
| Manufacturing | 37.54 | 39.05 | 35.12 |
| Retail trade | 11.86 | 14.61 | 10.62 |
| Health care and social assistance | 18.53 | 19.16 | 18.19 |
| Accommodation and food | 14.07 | 17.48 | 12.03 |
| Transportation and warehousing | 8.90 | 14.47 | 6.96 |
| Professional, scientific, technical | 4.73 | 5.97 | 4.19 |

The scale distribution is sector-specific. Manufacturing establishments have a
much larger typical employment footprint than retail, food, or professional
services. Within the selected sectors, metro establishments are generally
slightly larger than nonmetro establishments, but this is not a universal
rule and the county medians conceal substantial within-sector variation.

## What this adds to the broad program

1. **Presence and labor scale are separate.** A county can have many small
   establishments or fewer larger employers, with different implications for
   jobs, schedules, service continuity, and bargaining.
2. **“Business dynamism” needs a scale lens.** Applications and openings do not
   reveal whether the resulting local economy is made of one-person or
   labor-intensive establishments.
3. **Sector labels carry different social meanings.** A health establishment
   and a manufacturing establishment cannot be compared by count alone; their
   staffing, dependence, and local work effects differ.
4. **Rurality conditions firm structure.** The metro/nonmetro contrast is a
   useful conditioning variable, not an explanation of wages, access, or local
   power.

## Limits and counterexamples

Employees are an establishment-level CBP measure, not full-time-equivalent
work, pay, schedule quality, ownership, productivity, or service delivered.
County medians give each county equal weight. CBP does not show whether jobs
are held by residents, whether customers can use the service, or whether a
firm has market power. A necessary counterexample is a county where a larger
establishment footprint coexists with poor wages, weak worker control, high
prices, or inaccessible service; another is a place with many small firms and
strong practical alternatives.

Related: [all-sector county capacity profile](cbp-all-sector-county-capacity-profile-v1.md),
[rural/urban capacity profile](cbp-capacity-rural-urban-profile-v1.md),
[complete BFS–BDS sector profile](bfs-bds-complete-sector-profile-v1.md),
and the [firm and market power distribution layer](firm-market-power-distribution-layer-v1.md).
