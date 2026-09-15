# ACS annual national transportation layer v1

**Checked:** 2026-09-13  
**Source:** [2023 ACS B08201](https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/1YRData/acsdt1y2023-b08201.dat), [2024 ACS B08201](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/1YRData/acsdt1y2024-b08201.dat), and corresponding B08303 travel-time tables  
**Analysis:** [analyze_acs_transport_annual.py](../../../scripts/analyze_acs_transport_annual.py)

## Result

An independent annual household source shows modest national movement in two mobility indicators:

| Measure | 2023 | 2024 | Change |
|---|---:|---:|---:|
| Households with no vehicle, B08201 | 8.44% | 8.52% | +0.08 pp |
| Workers not working from home with commute 30+ minutes, B08303 | 37.97% | 38.69% | +0.72 pp |

The ACS layer does not confirm the richer NHTS gradients by itself. It supplies an annual national anchor with a different unit and universe. NHTS observes sampled household, person, and travel-day trip records; ACS publishes annual aggregate household and worker estimates. The two should be compared as complementary frames, not merged as if they were the same respondents.

## Why this matters for the atlas

```text
annual household vehicle access and commute exposure
  -> national mobility/time context
  -> condition for place, income, care, work, and consumer-access analysis
  -> targeted subgroup and matched-place tests
```

The annual national result is intentionally modest. It prevents the atlas from treating a single NHTS year as the whole mobility story while also preventing a small national change from being inflated into a societal transformation.

## Method and limits

- B08201 uses all US households; the no-vehicle estimate is `B08201_E002 / B08201_E001`.
- B08303 uses workers age 16+ who did not work from home; 30+ minutes sums `B08303_E008` through `B08303_E013` divided by `B08303_E001`.
- The direct national rows were read from the official table-based summary files. File hashes are preserved in the [machine-readable record](../../records/us-acs-transport-annual-national-2023-2024.json).
- ACS sampling and nonsampling error apply; this first layer does not calculate margins of error or cross-year significance.
- Vehicle availability is not affordability or reliability. Commute time is not total travel, care travel, shopping travel, or missed activity.

## Next test

Extend the same tables to states and selected places, add B08203 worker/vehicle cross-tabs and ACS income/race/disability dimensions, calculate margin-of-error-aware comparisons, and compare those distributions with NHTS urban/rural and income cells. The remaining end-to-end bridge is actual transport cost, care/medical reachability, household adaptation, and later trust or political action.
