# NHTS mobility pressure by place and household resources v1

**Run date:** 2026-09-13  
**Source:** [2022 NHTS CSV V2.1 archive](https://nhts.ornl.gov/media/2022/download/csv.zip)  
**Documentation:** [NHTS downloads](https://nhts.ornl.gov/downloads) and [NHTS documentation](https://nhts.ornl.gov/documentation)  
**Extraction:** [extract_nhts_transport_slice.py](../../../scripts/extract_nhts_transport_slice.py)  
**Analysis:** [analyze_nhts_mobility_material_work_care.py](../../../scripts/analyze_nhts_mobility_material_work_care.py)

## The finding

Mobility pressure is not one urban/rural variable. In this descriptive screen, it is patterned by place, household resources, and the kind of trip being recorded.

Among urban households in the lowest grouped income band (NHTS HHFAMINC codes 01-03), 35.23% had zero vehicles; the corresponding share among urban households in codes 06-08 was 3.54%. In rural households, the comparable figures were 12.79% and 0.71%.

The time pattern does not simply reverse. At the high-income end, 40.82% of recorded urban work trips and 53.40% of recorded rural work trips lasted at least 30 minutes. Shopping trips in the low-income urban cell averaged 34.01 minutes, compared with 20.71 minutes in the high-income urban cell. These are weighted travel-day observations, not a household’s complete weekly or annual burden.

| Cell | Zero vehicles | Work trips >=30 min | Shopping-trip mean |
|---|---:|---:|---:|
| Urban, under $35k | 35.23% | 31.46% | 34.01 min |
| Urban, $75k+ | 3.54% | 40.82% | 20.71 min |
| Rural, under $35k | 12.79% | 13.92% | 29.65 min |
| Rural, $75k+ | 0.71% | 53.40% | 26.31 min |

## Interpretation for the long-term program

This creates a useful bridge between the material and cultural/societal layers:

```text
household resources + place
  -> vehicle and mode choice set
  -> time required for work and daily-life trips
  -> different exposure to prices, fatigue, coordination, and failure risk
  -> possible downstream effects on care, consumption, trust, and political judgment
```

NHTS measures the first three arrows partially. It does not establish the downstream effects. Those require the household calendar, expenditure/budget records, health/care modules, and political-attitudes sources already in the wider program.

## Method and boundaries

- Household measures use `WTHHFIN`; recorded trip measures use `WTTRDFIN`.
- Income groups are `HHFAMINC` 01-03, 04-05, and 06-08, described as under $35k, $35k-$74k, and $75k or more. Refusals and unknowns are excluded.
- Work trips use `WHYTRP90=01`; shopping trips use `TRIPPURP=04`. Shopping is a daily-life activity proxy, not a complete care or caregiving measure.
- Household, person, and trip units are joined only by household identifier for stratification. No person-level causal pathway is inferred.
- No survey-design interval is reproduced. Small cells, broad urban/rural categories, travel-day selection, missingness, and extreme trip times can change the descriptive picture.
- The raw archive is not committed to the repository. Retrieval is identified by SHA-256 `64530c396d5f164d2259a22f7042f27bee5147babcd367568ddbfafe6c8bf34c`.

## What would change the finding

The layer would weaken if the resource/place gradients disappeared under design-based inference and richer controls, or if low vehicle access did not correspond to different time, cost, or failed-trip exposure once full household calendars were observed. The next required bridge is a dedicated care/medical/childcare trip and missed-activity module, linked to actual fares, fuel/repair costs, income timing, and household coping.

The bounded results are preserved in the [machine-readable trend record](../../records/us-nhts-mobility-material-work-care-2022.json).
