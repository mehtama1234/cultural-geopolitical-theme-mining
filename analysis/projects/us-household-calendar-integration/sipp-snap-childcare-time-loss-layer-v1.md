# SIPP SNAP transition and child-care time-loss layer v1

This layer extends the same-person November-to-December SNAP comparison with
`ETIMELOST` and `ETIMELOST_TP`, which the 2025 SIPP dictionary defines as the
amount and type of time lost from work because child-care arrangements caused a
reference parent to be unable to work or work more during the fall reference
year.

| Stable transition | Child care prevented work/more work | Valid time-loss cases | Hours | Days | Weeks |
|---|---:|---:|---:|---:|---:|
| No SNAP → No SNAP | 3.42% (SE 0.45; 95% CI 2.54–4.30; n=2,295) | 71 | 38.52% (SE 6.78) | 49.94% (SE 6.97) | 11.55% (SE 3.97) |
| SNAP → SNAP | 7.43% (SE 1.88; 95% CI 3.75–11.11; n=351) | 23 | 48.83% (SE 11.82) | 34.95% (SE 11.69) | 16.22% (SE 7.26) |

The stable-SNAP comparison has a higher descriptive share reporting that
child-care arrangements prevented working or working more. Among the small
valid time-loss cells, the type composition also differs, with a larger hours
share and smaller days share in the stable-SNAP cell. The intervals are wide;
this is a bounded comparison, not a causal estimate.

The November-to-December pair supplies a same-person temporal anchor for SNAP
status, but the child-care questions refer to a typical fall week or the fall
reference year and are copied into monthly records. They should not be read as
December care outcomes. The entry and exit transitions have only 4 and 2 valid
EWORKMORE records and no valid time-loss cases, so they are not interpreted.

The flag-inclusive rerun included `AWORKMORE`, `ATIMELOST`, and
`ATIMELOST_TP`. It returned the same point estimates and valid-cell counts as
the original response-code audit, so the result survives that quality gate.
The remaining limitation is substantive: these are annual fall child-care
fields attached to an adjacent-month SNAP bridge, not a dated care episode.

## Current reproducibility audit

On 2026-09-14 the analysis was rerun against the current local `full-v15`
primary slice and the 240-replicate `rw2025.csv` archive. The run read 379,215
rows and matched 31,335 replicate pairs. It reproduced the committed point
estimates and standard errors exactly for all four transition groups and all
reported measures, including the 2,295 stable no-SNAP and 351 stable-SNAP valid
work-prevention denominators. The entry and exit cells remained 4 and 2 valid
work-prevention records, with no valid time-loss cases.

This confirms the computational layer and its denominator/uncertainty controls.
It does not strengthen the causal interpretation: the child-care fields refer
to the fall reference year, while SNAP status supplies an adjacent
November-to-December bridge. Stable SNAP remains a household-state comparison,
not evidence that SNAP caused care-related work loss.

## Reproduction

The primary slice was streamed from the 2025 SIPP public-use file (2024
reference year), retaining 379,215 rows, 13,670 sample units, and 13,910
households. The analysis uses the 240-replicate `rw2025.csv` file with Fay
factor 0.5:

```text
python3 scripts/extract_sipp_household_calendar_slice.py --input - \
  --output /tmp/sipp-household-calendar-slice-2025.csv \
  --report /tmp/sipp-household-calendar-slice-2025.json
python3 scripts/analyze_sipp_snap_childcare_time_loss.py \
  --primary /tmp/sipp-household-calendar-slice-2025.csv \
  --replicate-zip /path/to/rw2025_csv.zip \
  --output /tmp/sipp-snap-childcare-time-loss.json
```

The [machine-readable record](../../records/us-sipp-snap-childcare-time-loss-2024.json)
preserves the separate denominators, replicate-weight uncertainty, flag-aware
rerun, sparse transition cells, and open meaning/action links.

Source: [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
and the [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf).
