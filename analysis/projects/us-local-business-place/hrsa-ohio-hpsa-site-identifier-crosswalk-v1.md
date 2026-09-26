# Ohio HPSA-to-site identifier crosswalk v1

**Checked:** 2026-09-19  
**Unit:** Ohio HPSA coordinate row and HRSA service-delivery site
organization identifier  
**Purpose:** strengthen the proximity probe with an administrative identifier
join. This is still not a completed-care estimate.

## Result

Of the 94 Ohio HPSA rows with coordinates, 61 also have a
`BHCMIS Organization Identification Number` that appears in the official Ohio
health-center service-site file. For those 61 shared-identifier rows, the
nearest site belonging to the same organization is:

| Same-organization distance | Rows |
|---|---:|
| 100 meters or less | 56 |
| 1 kilometer or less | 57 |
| 5 kilometers or less | 59 |
| 10 kilometers or less | 60 |

The median distance is 0 km, the mean is 0.43 km, and the maximum is 15.02 km.
All shared-identifier rows are FQHC or FQHC look-alike HPSA rows in this
filtered file. See the [machine-readable crosswalk](data/hrsa-ohio-hpsa-site-identifier-crosswalk-2026-09-19.json).

## Why this is stronger—and still limited

The BHCMIS join is stronger than simply finding a nearby site: it ties the HPSA
row and site record to the same HRSA organization identifier. But it still does
not establish that the site is the designated HPSA component, offers the
relevant service, accepts the person or their insurance, has open appointments,
or was used.

```text
HPSA row -> shared organization identifier -> candidate site
         -> [open] designated service/site identity
         -> [open] hours, acceptance, wait, travel cost
         -> [open] attempted/completed care and household outcome
```

The 33 coordinate-bearing HPSA rows without a shared identifier, plus all
population/geographic HPSA rows without coordinates, remain explicit missing
parts of the access map.

## Source boundary

The site file was downloaded temporarily from the [official HRSA endpoint](https://data.hrsa.gov/DataDownload/DD_Files/Health_Center_Service_Delivery_and_LookAlike_Sites.csv)
and removed from the repository scope; its SHA-256 is recorded in the JSON.
No patient, appointment, billing, or outcome data was used.
