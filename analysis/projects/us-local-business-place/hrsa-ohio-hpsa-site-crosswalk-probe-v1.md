# Ohio HPSA-to-health-center site crosswalk probe v1

**Checked:** 2026-09-19  
**Purpose:** test whether the small coordinate-bearing part of the Ohio HPSA
file can be connected to HRSA health-center site locations. This is a
proximity probe, not a provider-access or completed-care estimate.

## Result

The official HRSA Health Center Service Delivery and Look-Alike Sites file has
676 Ohio rows; all 676 are marked active and have coordinates. A nearest-point
probe against the 94 non-withdrawn Ohio HPSA rows that also have coordinates
found:

| Nearest site distance | HPSA rows |
|---|---:|
| 100 meters or less | 56 |
| 1 kilometer or less | 63 |
| 5 kilometers or less | 79 |
| 10 kilometers or less | 87 |

The median nearest distance is 0 km, the mean is 2.34 km, and the maximum is
20.17 km. Exact or near-exact matches are concentrated in FQHC and look-alike
rows; correctional and rural-health rows show a different pattern. The full
compact output is in the [crosswalk probe JSON](data/hrsa-ohio-hpsa-site-crosswalk-probe-2026-09-19.json).

## What this does and does not show

The result says that a coordinate-based site crosswalk is technically
possible for a subset of HPSA components. It does not prove that the nearest
site is the same organization, that it serves the designated population, that
it accepts a patient's insurance, or that an appointment is available.

```text
HPSA coordinate -> nearby HRSA site record
                -> [open] same organization/service
                -> [open] hours/insurance/wait/travel
                -> [open] attempted and completed care
                -> [open] household, work, health, trust, or action outcome
```

The next valid move is identifier and service-type validation for the candidate
links, followed by hours, insurance acceptance, appointment wait, and a stated
travel-time method. The crosswalk must remain a candidate-link screen until
those fields are observed.

## Source boundary

The HPSA file is the retained HRSA primary-care component CSV. The site file was
downloaded to `/tmp` for this probe from the [official HRSA endpoint](https://data.hrsa.gov/DataDownload/DD_Files/Health_Center_Service_Delivery_and_LookAlike_Sites.csv)
and is not retained in the repository. Its SHA-256 is recorded in the
machine-readable output. No patient, appointment, billing, or outcome data was
used.
