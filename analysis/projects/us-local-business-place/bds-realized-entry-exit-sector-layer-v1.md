# Realized firm entry, exit, and sector turnover layer v1

**Checked:** 2026-09-12  
**Question:** After an application signal, what actually opens, closes, creates jobs, destroys jobs, and changes the sector capacity of the US economy?

## Why this layer matters

Business applications are an early intention signal. County Business Patterns (CBP) is an employer-establishment stock. Neither one is a firm birth or death rate. Census Business Dynamics Statistics (BDS) supplies the missing realized-dynamics layer: annual establishment openings and closings, firm deaths, job creation and destruction, and net employment change.

This matters for the broad program because sectors are not interchangeable. A change in retail, care, transport, manufacturing, or food service can redistribute everyday access, work, prices, time, and local dependence differently. The BDS layer measures the firm and job movement first; services, culture, politics, and belonging remain later arrows requiring their own evidence.

## Source and reproducibility

- [Census BDS program](https://www.census.gov/programs-surveys/bds.html): describes annual measures of job creation/destruction, establishment births/deaths, and firm startups/shutdowns.
- [2023 BDS sector CSV directory](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/): official downloadable tables.
- [2023 sector CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_sec.csv), SHA-256: `758a263b166167e9557d4fc4ba8cd60229c5e05d341214b7494982c4764cf224`.
- Reproduction: `python3 scripts/analyze_bds_sector_dynamics.py --csv /path/to/bds2023_sec.csv --year 2023`.

The sector file is an annual national aggregate. It is not a panel of identifiable firms and does not say which particular business opened or closed. The BDS program's API and state/county tables can support later geographic passes.

## 2023 national sector baseline

| Sector | Establishments | Employment | Openings | Closings | Jobs created by establishment births | Jobs destroyed by establishment deaths | Net job creation |
|---|---:|---:|---:|---:|---:|---:|---:|
| Construction | 703,433 | 7,614,745 | 90,679 | 77,211 | 348,581 | 319,204 | 242,798 |
| Manufacturing | 268,269 | 12,293,106 | 18,443 | 18,782 | 262,904 | 235,498 | 154,526 |
| Retail trade | 980,272 | 16,068,436 | 77,369 | 69,636 | 479,805 | 377,117 | 52,232 |
| Transportation and warehousing | 254,427 | 6,450,641 | 37,750 | 37,291 | 289,723 | 227,346 | 128,978 |
| Finance and insurance | 438,240 | 6,912,028 | 35,830 | 42,421 | 307,479 | 301,423 | 126,469 |
| Professional/scientific/technical services | 838,248 | 10,364,674 | 103,804 | 91,802 | 466,244 | 478,417 | 249,750 |
| Health care and social assistance | 925,453 | 21,997,571 | 98,281 | 70,254 | 872,304 | 654,668 | 881,400 |
| Accommodation and food services | 714,803 | 14,565,278 | 78,150 | 64,285 | 976,486 | 638,129 | 791,588 |
| Other services | 742,030 | 5,677,219 | 73,476 | 59,894 | 296,271 | 218,055 | 202,396 |

These are descriptive sector flows. Net job creation is not the same as net firm formation: jobs can change within continuing establishments, and establishment openings/closings are not identical to firm startups/shutdowns.

## Broad societal readings to test

1. **Capacity is sector-shaped.** A place with more entry is not necessarily gaining the services people need; entry in construction, care, food, or transport has different consequences.
2. **Turnover can coexist with expansion.** Health care and food services show substantial birth and death flows alongside positive net job creation. Growth therefore does not mean stability for workers, owners, or customers.
3. **Exit and entry redistribute dependence.** A closing establishment can move travel, waiting, price, care, or employment burdens even when the national sector grows.
4. **The application-to-life bridge remains open.** The next test should compare BFS applications with BDS/CBP realized dynamics by state, county, sector, and time, then attach service-access and political evidence where available.

## What this does not establish

This layer does not prove that applications caused openings, that a closing establishment caused household hardship, that sector turnover changed local identity, or that any economic movement caused a political choice. It also cannot identify consumer quality, ownership concentration, informal activity, or whether a new establishment replaced the lost service in the same location.

## Next bounded pass

Use BDS state/county-sector tables to test whether high-application places have realized entry, exit, and net-job patterns that differ by sector and rural/urban context. Keep a counterexample: a place with applications but no corresponding employer-stage growth, and a place with stable stocks but high turnover. Then connect only measured service, work, price, or civic outcomes.
