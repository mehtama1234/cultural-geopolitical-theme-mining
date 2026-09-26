# Source search: transit service realization and usable mobility

**Search date:** 2026-09-22  
**Geography:** United States public transportation  
**Status:** bounded pass complete; national service output is not the same as usable household access

**Acquisition note:** the official FTA landing page and published summary were
reviewed. The direct PDF endpoint returned an access-denied response to the
local downloader, so the record preserves the official web source and does not
claim a locally downloaded copy of the report.

## Working question

What did the 2024 National Transit Database show about transit service that was
actually operated and consumed?

## Opening source

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-FTA-NTD-2024 | [FTA National Transit Database](https://www.transit.dot.gov/ntd) and [2024 National Transit Summaries and Trends](https://www.transit.dot.gov/sites/fta.dot.gov/files/2026-04/2024%20National%20Transit%20Summaries%20and%20Trends_1.2.pdf) | Aggregates agency-reported service, passenger trips, passenger miles, operating resources, funding, safety, assets, and workforce. | Official FTA/NTD source | It does not show a particular household's reachable route, wait, fare burden, reliability, completed trip, or later economic outcome. |

## First pattern

```text
public transit investment and agency operation
  -> vehicles, workers, revenue miles, and scheduled service
  -> passenger trips and passenger miles
  -> reachable, affordable, reliable household mobility [open]
```

FTA reports that nearly 3,000 agencies provided 7.6 billion passenger trips
in 2024, up 9.8% from 2023, and carried passengers about 38.1 billion miles,
up 8.7%. The system operated in 502 urbanized areas and involved more than
380,000 workers each day with a national fleet of more than 177,000 vehicles.

## Counterpoint to keep visible

The ridership increase is a real operating and use signal, but it is not a
national access or welfare rate. Trips can be concentrated in large systems,
travel purposes differ, and the aggregate does not show people who could not
travel, missed a trip, faced a fare barrier, or used transit because no better
option existed.

## Decision rule

Use NTD for reported operating scale and service consumed. Do not convert
passenger trips or vehicle counts into equitable access, reliability,
affordability, safety, or household mobility without place- and person-linked
evidence.
