# NHTS field audit v1

**Checked:** 2026-09-12  
**Source:** [2022 NHTS downloads](https://nhts.ornl.gov/downloads)  
**Documentation:** [2022 NHTS documentation](https://nhts.ornl.gov/documentation)

The 2022 NHTS is not one flat table. It has household, person, vehicle, and trip files. The official user guide says they link through `HOUSEID`, with `PERSONID` and `TRIPID` added for person and trip records. That structure matters: household resources, a person’s rideshare use, and a trip’s purpose are different records and must be joined deliberately.

## Verified field groups

| Question | File and fields | What it can show |
|---|---|---|
| Does the household have a car or driver? | Household: `HHVEHCNT`, `DRVRCNT`, `HHSIZE`, `WRKCOUNT`, `URBRUR` | Vehicle access, household size, workers, and urban/rural setting |
| Who uses or lacks transit? | Person: `USEPUBTR`, `WRKTRANS`, `GCDWORK`, `CONDTRAV`, `CONDPUB` | Public-transport use, commute mode, commute distance, and reported travel limits |
| Who used rideshare? | Person: `LAST30_RDSHR`, `RIDESHARE22`, `CONDRIDE` | Recent rideshare use, rideshare measure, and travel limitation connected to ride access |
| What was the trip for? | Trip: `TRIPPURP`, `WHYTRP90`, `TRPTRANS` | Trip purpose and transportation mode |
| How much time did it take? | Trip: `TRVLCMIN`, `STRTTIME`, `ENDTIME`, `TRPMILES` | Travel time, start/end time, and miles |
| What vehicle burden is visible? | Vehicle: `ANNMILES`, `VEHAGE`, `VEHFUEL`, `VEHOWNED` | Annual miles, age, fuel, and ownership |
| Can results be expanded to population estimates? | Household/person/trip weights: `WTHHFIN`, `WTPERFIN`, `WTTRDFIN` | Survey-weighted household, person, and travel-day estimates |

## What this adds to the project

NHTS can make the transportation part of HC-002 concrete at the level of trip need, mode, time, vehicle access, and rideshare exposure. It can compare households and people across urban, suburban, and rural settings. It can also show whether a person reports a travel limitation connected to rideshare or transit.

It cannot connect a trip to the household’s exact fare, paycheck date, missed shift, debt, safety experience, failed service contact, or next-month recovery. Those remain missing fields for the calendar panel.

## Extractor

The bounded extractor is [extract_nhts_transport_slice.py](../../../scripts/extract_nhts_transport_slice.py). It checks all four archive members, selects the fields above, writes temporary per-file CSVs, and records row counts and value counts. It supports `--max-rows` so a smoke test does not become a full analysis.

## Reproducibility boundary checked 2026-09-12

The checkout contains the extractor and the recorded comparison, but not the raw NHTS archive or derived CSVs. A fresh request to the official downloads site reached the NHTS application shell; the apparent `assets/datasets/2022` JSON and CSV paths did not return the archive in this environment. The recorded NHTS percentages therefore remain prior-run evidence, not a newly reproduced result in this checkout. Re-run the extractor only after retaining the official archive outside Git and recording its exact URL, checksum, archive members, and download date.

The first bounded run is recorded in the [NHTS smoke check](nhts-smoke-check-v1.md). It verified the four-file hierarchy and showed why special survey codes must be decoded before interpretation.

## Interpretation rule

Do not call rideshare use “dependence” from one rideshare field. Dependence requires a need, a real alternative, a price or time comparison, and the result when the ride is unavailable. NHTS supplies some of the first two pieces. The household calendar must record the rest.
