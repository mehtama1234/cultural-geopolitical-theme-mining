# BFS annual county data-quality boundary

**Checked:** 2026-09-12  
**Source:** [Census Business Formation Statistics annual county data](https://www.census.gov/econ/bfs/data/county.html)  
**Release:** June 10, 2026; annual business applications through 2025  
**Status:** quality-control record; no county trend finding is claimed.

## Why this boundary matters

Business Formation Statistics are useful because they distinguish early EIN
applications from later business formation. But the current annual county
release says that its disclosure-avoidance process uses differentially private
geometric noise for the 2005–2025 county application counts. That makes a raw
county ranking or year-over-year percentage change unsafe without checking the
noise, denominator, and plausibility of the specific cell.

## Reproducibility record

The official workbook was downloaded from:

`https://www.census.gov/econ/bfs/xlsx/bfs_county_apps_annual.xlsx`

It contains one sheet, `County Data`, with state, county, FIPS identifiers, and
`BA2005` through `BA2025`. The values are delivered as text strings in the
workbook, so analysis must parse them explicitly and preserve the original
strings alongside converted numbers.

An exploratory parser found values that require a validation stop before
interpretation. For example, the workbook reports Sheridan County, Wyoming at
38,208 applications in 2024 and 47,787 in 2025, while neighboring county rows
are much smaller. This may reflect the release's noise and disclosure rules,
an identifier or data issue, or a real but unusual application pattern; this
record does not decide among those explanations.

The observation is a data-quality signal, not evidence that Sheridan had that
many durable firms, jobs, services, or entrepreneurs. It is also not evidence
of a statewide trend.

## Required checks before use

1. Read the [BFS methodology](https://www.census.gov/econ/bfs/methodology.html)
   and county data dictionary beside every extracted value.
2. Preserve state FIPS, county FIPS, county name, release date, and raw cell
   text; never match by county name alone.
3. Compare applications with projected or actual formations, employer firms,
   establishments, payroll, population, and tax records where lawful.
4. Treat small-county ratios as especially unstable and use pooled periods or
   larger geographies when the research question permits.
5. Record the disclosure-avoidance version and check whether revisions or a
   future release change the cell.

## What this means for the broad program

The firm/place layer can support a careful question about the stages of local
business entry, but the stages are not interchangeable:

```text
EIN application
  -> projected or actual employer formation
  -> establishment, payroll, service, and local relationship
  -> jobs, prices, access, belonging, and political voice
```

The first arrow is available in the county workbook. The later arrows require
different sources and quality checks. The next valid comparison is therefore a
matched geography pass that joins applications to durable employer and service
measures, with privacy noise and sparse cells made visible.

## Stop rule

Do not publish county application growth as a trend in local entrepreneurship,
small-business survival, employment, service access, community identity, or
political participation until the underlying cell passes the checks above and
the later outcome is measured separately.
