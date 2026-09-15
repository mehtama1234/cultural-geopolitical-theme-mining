# Work limitation changes the monthly resource-and-job transition surface

**Status:** corrected-v18 same-person SIPP cross-lag diagnostic · **Checked:** 2026-09-15

## The bounded finding

The corrected 2025 SIPP slice supports a same-person monthly comparison of
income-to-poverty position and job count, conditioned on whether the person
reported a work-limiting condition in the first month. The two transition
directions do not move identically.

| Transition and first-month cell | Work-limited | Not work-limited |
|---|---:|---:|
| Below 1× poverty → next-month job-count change | 1.07% (SE 0.21), n=10,096 | 3.25% (0.21), n=18,687 |
| 4× poverty or more → next-month job-count change | 1.44% (0.16), n=16,121 | 1.64% (0.06), n=124,301 |
| Zero jobs → next-month resource-band change | 2.38% (0.13), n=45,094 | 3.24% (0.13), n=93,835 |
| One job → next-month resource-band change | 5.27% (0.35), n=10,888 | 3.62% (0.12), n=134,144 |
| Two jobs → next-month resource-band change | 5.74% (1.17), n=834 | 4.94% (0.34), n=11,074 |

Among people in the lowest resource band, work-limited respondents show less
job-count movement than respondents without the reported limitation. In the
reverse direction, people with one or two jobs show more following-month
resource-band movement when they are work-limited. The high-resource job-change
difference is small relative to the low-resource contrast, while the two-job
work-limited estimate is imprecise.

This is a conditional transition surface, not a claim that work limitation
causes job stability or income volatility. A limitation may reflect health,
disability, age, job type, household composition, or reporting differences;
job count and resource bands can change through hours, earnings, transfers,
prices, or other household changes.

## What this adds to the end-to-end chain

```text
monthly resource position and work-limiting status
  -> job-count or resource-band transition in the next month
  -> potentially different room for care, consumption, and bill payment
  -> later health, work, institutional, or political consequence
```

The new evidence closes only the adjacent-month transition segment. It does
not identify a dated bill, care need, employer decision, accommodation,
protected or sacrificed outcome, remedy, trust judgment, or recovery.

## Counterexamples and limits

- Lower job movement among work-limited people can mean constrained entry or
  stable employment; the data do not distinguish those mechanisms.
- More resource-band movement among work-limited people with one or two jobs
  does not establish worsening or improvement; the direction of the band
  change is not summarized by the change indicator.
- The two-job work-limited cell is small and should not be generalized.
- Person-record weights support person transitions, not household prevalence.
- Annual hardship and care fields are not treated as monthly outcomes merely
  because they repeat on person records.

## Reproduction

```text
python3 scripts/analyze_sipp_resource_job_worklimitation_crosslag.py \
  --primary /tmp/us-broad-sipp-2025/full-v18/sipp-household-slice.csv \
  --replicate-zip /tmp/rw2025_csv.zip \
  --output /tmp/us-broad-sipp-2025/full-v18/resource-job-worklimitation-crosslag.json
```

- [Machine-readable record](../../../records/us-sipp-resource-job-worklimitation-crosslag-2024.json)
- [Analysis script](../../../../scripts/analyze_sipp_resource_job_worklimitation_crosslag.py)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

**Evidence status:** same-person monthly cross-lag with Fay-BRR uncertainty;
descriptive and selection-sensitive, with no causal, household, cultural,
political, or geopolitical conclusion.
