# Ohio HPSA-linked site operating-fields audit v1

**Checked:** 2026-09-19  
**Unit:** service-site records under the 61 organizations shared by the Ohio
HPSA and HRSA service-site files  
**Purpose:** measure whether the administrative crosswalk carries operating
fields. This is not an appointment or completed-care estimate.

## Result

The 61 shared organization identifiers cover 662 Ohio service-site rows. All
662 are marked active. Of those, 641 list positive operating hours, with a
median of 40 hours per week. But schedule information is much thinner:

| Field | Observed values |
|---|---:|
| Positive operating hours | 641 of 662 rows |
| Missing operating hours | 21 of 662 rows |
| Full-time schedule | 137 rows |
| Part-time schedule | 15 rows |
| Unknown schedule | 510 rows |
| Year-round calendar | 128 rows |
| Seasonal calendar | 9 rows |
| Unknown calendar | 525 rows |

At the organization level, all 61 shared organizations have at least one site
with positive hours, while only 36 have at least one site with a known
full-/part-time schedule. The machine-readable output is the [operating-fields
audit JSON](data/hrsa-ohio-hpsa-site-operating-fields-audit-2026-09-19.json).

## What this means

This advances the route from organization identity to nominal operating fields:

```text
shared organization -> active site -> listed hours
                    -> [open] designated service identity
                    -> [open] new-patient/insurance acceptance and wait
                    -> [open] appointment, completed use, and outcome
```

The hours belong to service-site records under an organization, not necessarily
to the exact HPSA component. They do not show whether a resident can book an
appointment, afford it, use their insurance, or complete care. The next stage
requires service type, patient/insurance acceptance, wait, travel cost, and a
defined exposed population.

## Source boundary

The site file was downloaded temporarily from the [official HRSA endpoint](https://data.hrsa.gov/DataDownload/DD_Files/Health_Center_Service_Delivery_and_LookAlike_Sites.csv)
and is not retained in the repository. No patient, appointment, billing, or
health-outcome data was used.
