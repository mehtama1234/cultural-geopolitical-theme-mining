# Ohio HPSA coordinate-availability audit v1

**Checked:** 2026-09-19  
**Unit:** Ohio primary-care HPSA component row  
**Purpose:** determine whether the retained shortage file can support a bounded
provider/travel follow-up. This is a data-availability audit, not a care-access
estimate.

## Result

The retained HRSA primary-care file contains 1,342 Ohio rows after excluding
withdrawn rows. Only 94 rows (7.0%) contain both latitude and longitude. All
1,081 population-designation rows and all 87 geographic HPSA rows in this
filtered set lack coordinates. Facility-type rows are the coordinate-bearing
part of the file; a county FIPS code on a population or geographic component is
not a provider location.

| Status or designation | Rows | Rows with coordinates |
|---|---:|---:|
| All retained Ohio rows | 1,342 | 94 |
| Designated | 1,139 | 92 |
| Proposed for withdrawal | 203 | 2 |
| HPSA population | 1,081 | 0 |
| Geographic HPSA | 87 | 0 |
| High-needs geographic HPSA | 80 | 0 |
| Facility-type rows combined | 94 | 94 |

The machine-readable result is the [coordinate-availability audit JSON](data/hrsa-ohio-coordinate-availability-audit-2026-09-19.json).

## What this changes

The file supports a small, transparent next step for coordinate-bearing
facility rows: validate facility identity, active status, service type, hours,
insurance acceptance, and a stated travel-time method. It does not support a
county-wide travel-time estimate for population or geographic shortage rows.
The correct interpretation is therefore:

```text
HPSA component -> possible site coordinate for some facility rows
              -> [open] reachable appointment, price, wait, completed use
```

The audit does not establish that a resident is underserved, that a listed
facility accepts a new patient or a given insurance plan, or that a shorter
geographic distance produces completed care. It also does not connect provider
availability to household work, debt, trust, or political action.

The next controlled source route is HRSA's [Health Center Service Delivery and
Look-Alike Sites](https://data.hrsa.gov/topics/health-centers/) dataset. HRSA
describes it as covering more than 16,200 sites, with a daily refresh cycle;
the catalog listed the CSV at approximately 10.5 MB and updated on 26 August
2026. This audit does not download that file. The next acquisition should use
an Ohio-filtered slice or a documented query/export, then test whether site
identity can be joined to the 94 coordinate-bearing HPSA rows. Site presence
would still not prove hours, insurance acceptance, wait, appointment, or use.

## Source and boundary

Source: [HRSA primary-care HPSA component CSV](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv), retained locally as `hrsa-primary-care-hpsa.csv`; the observed data-warehouse create date text is 2026-09-14. The component file is an administrative designation surface. No patient, appointment, billing, or outcome file is used.
