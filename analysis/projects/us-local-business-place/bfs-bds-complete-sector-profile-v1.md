# BFS–BDS complete sector profile v1

**Checked:** 2026-09-12  
**Question:** How does early business-application activity compare with
realized establishment and job dynamics across the full national sector file?

## Why this matters

“Business activity” is not one societal outcome. Applications are an early
signal; BDS openings, closings, and job creation are realized annual flows.
The full profile makes it possible to see whether the contrast is specific to
retail, care, food, transport, or another sector rather than generalizing from
one selected group.

```text
BFS applications by sector
  -> BDS establishment openings and closings
  -> net job creation or destruction
  -> employer stock, service capacity, work, prices, and local life
```

## Sources and reproduction

- [Census BFS sector CSV](https://www.census.gov/econ/bfs/csv/naics2.csv), weekly national applications summed across 2023.
- [Census BDS 2023 sector table](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_sec.csv), annual national establishment and job dynamics.
- BFS SHA-256: `4f8c6f5b8c56c7b6e856845609e2b9a374db649326f99f897c10160098212f4a`.
- BDS SHA-256: `758a263b166167e9557d4fc4ba8cd60229c5e05d341214b7494982c4764cf224`.
- Reproduction: `python3 scripts/analyze_bfs_bds_sector_bridge.py --bfs /path/to/naics2.csv --bds /path/to/bds2023_sec.csv --year 2023`.

The stage ratio below is `BFS applications / BDS establishment openings`.
It is not a firm-formation, survival, or conversion rate: the files use
different constructions, timing, and disclosure rules.

## Complete 2023 profile

| NAICS sector | Applications | Openings | Closings | Net job creation | Applications per opening |
|---|---:|---:|---:|---:|---:|
| Agriculture, forestry, fishing and hunting | 78,480 | 2,033 | 2,256 | -5,816 | 38.60 |
| Mining, quarrying, and oil and gas extraction | 6,890 | 2,000 | 1,629 | 60,674 | 3.45 |
| Utilities | 8,000 | 1,027 | 1,110 | 15,634 | 7.79 |
| Construction | 546,160 | 90,679 | 77,211 | 242,798 | 6.02 |
| Manufacturing | 95,440 | 18,443 | 18,782 | 154,526 | 5.17 |
| Wholesale trade | 127,500 | 24,035 | 29,486 | 125,518 | 5.30 |
| Retail trade | 971,630 | 77,369 | 69,636 | 52,232 | 12.56 |
| Transportation and warehousing | 393,310 | 37,750 | 37,291 | 128,978 | 10.42 |
| Information | 101,720 | 15,058 | 16,368 | -8,797 | 6.76 |
| Finance and insurance | 218,270 | 35,830 | 42,421 | 126,469 | 6.09 |
| Real estate and rental and leasing | 290,120 | 49,858 | 44,553 | 89,014 | 5.82 |
| Professional, scientific, and technical services | 674,660 | 103,804 | 91,802 | 249,750 | 6.50 |
| Management of companies and enterprises | 48,340 | 2,817 | 4,591 | 115,635 | 17.16 |
| Administrative/support and waste management | 407,790 | 50,123 | 45,959 | -130,391 | 8.14 |
| Educational services | 80,930 | 11,579 | 8,752 | 160,169 | 6.99 |
| Health care and social assistance | 325,200 | 98,281 | 70,254 | 881,400 | 3.31 |
| Arts, entertainment, and recreation | 158,950 | 17,983 | 13,700 | 187,414 | 8.84 |
| Accommodation and food services | 302,250 | 78,150 | 64,285 | 791,588 | 3.87 |
| Other services except public administration | 521,140 | 73,476 | 59,894 | 202,396 | 7.09 |

## What the full profile changes

1. **Application intensity and realized job growth diverge by sector.** Retail
   has the largest application count in this profile, but its net job creation
   is much smaller than health/social assistance or accommodation/food.
2. **Negative net job sectors remain visible.** Agriculture, information, and
   administrative/support services have negative 2023 net job creation in the
   BDS file despite recorded applications. This is a reason to preserve exit
   and job destruction rather than narrating applications as expansion.
3. **Low stage ratios do not prove successful conversion.** Mining and
   health/social assistance have fewer applications per recorded opening than
   retail, but the difference may reflect timing, sector structure, reporting,
   or the construction of the two datasets.
4. **Social importance and application volume are different dimensions.**
   Care, food, utilities, transport, education, and information can affect
   daily life through jobs or services without ranking highest on applications.

## Boundaries and next test

This is a national, one-year, descriptive bridge. It does not identify firms,
owners, workers, customers, wages, prices, quality, concentration, informal
activity, local capacity, or cultural/political response. Net job creation is
not job quality or bargaining power, and an establishment opening is not a
service reaching a resident.

Next, select contrasting sectors and places, join applications to realized
firms and employer stocks, then add service access, prices, wages, ownership,
worker control, and local civic measures. Retain a sector where applications
rise but jobs or access do not, and a sector where stable applications coexist
with strong realized capacity.

Related: [BFS–BDS sector bridge](bfs-bds-sector-bridge-v1.md), [BDS realized
entry, exit, and sector dynamics](bds-realized-entry-exit-sector-layer-v1.md),
and the [broad trend-extraction protocol](../../US-BROAD-TREND-EXTRACTION-PROTOCOL_V1.md).
