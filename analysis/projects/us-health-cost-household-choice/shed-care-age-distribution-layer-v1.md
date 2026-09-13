# SHED care and age distribution layer v1

**Checked:** 2026-09-12
**Unit:** US adult respondent; 2024 Federal Reserve SHED
**Method:** weighted descriptive cross-tab of regular unpaid adult care and age; no variance estimate or causal model

## Why add life stage

Care responsibility is a societal role distributed across the life course. A
single caregiver average can hide whether younger adults have less cash room,
whether midlife caregivers face a work-and-care squeeze, or whether older
caregivers have different buffers and adaptation options.

## Selected results

| Age | Care status | Used less/stopped | Increased borrowing | Reduced savings | Worked more/got job | Three-month funds |
|---|---|---:|---:|---:|---:|---:|
| 18–24 | No care | 59.7% | 14.5% | 38.9% | 28.8% | 30.7% |
| 18–24 | Regular care | 71.2% | 29.3% | 51.5% | 37.7% | 29.7% |
| 25–34 | No care | 64.3% | 19.0% | 43.5% | 23.2% | 48.2% |
| 25–34 | Regular care | 72.6% | 31.0% | 57.4% | 34.9% | 32.6% |
| 35–44 | No care | 65.2% | 20.3% | 46.2% | 21.8% | 51.4% |
| 35–44 | Regular care | 72.3% | 29.4% | 61.6% | 29.0% | 40.6% |
| 45–54 | No care | 65.1% | 17.5% | 45.1% | 19.3% | 52.7% |
| 45–54 | Regular care | 75.8% | 26.8% | 58.8% | 22.0% | 47.6% |
| 55–64 | No care | 60.6% | 11.9% | 41.2% | 12.8% | 61.8% |
| 55–64 | Regular care | 68.6% | 16.7% | 50.1% | 16.2% | 62.2% |
| 65–74 | No care | 49.8% | 6.7% | 31.9% | 4.9% | 73.1% |
| 65–74 | Regular care | 64.0% | 10.5% | 48.7% | 10.2% | 67.4% |
| 75+ | No care | 42.7% | 4.9% | 29.8% | 1.6% | 77.1% |
| 75+ | Regular care | 57.1% | 8.0% | 39.0% | 1.0% | 77.8% |

Regular caregivers report more reduced use, borrowing, and savings cuts than
non-caregivers in every age group. The gap is especially visible among younger
adults: at ages 25–34, regular caregivers report 31.0% borrowing versus 19.0%
without care and 32.6% emergency funds versus 48.2%. At older ages, emergency
capacity is higher overall, but caregiving remains associated with more
reduced use and savings cuts. Extra work is concentrated among younger adults
and does not rise monotonically with care.

## What this adds to the broad societal program

1. **Care is life-stage structured.** The same unpaid-care role sits inside
   different labor-market, savings, and family positions.
2. **Age does not explain the mechanism by itself.** Income, employment,
   recipient relationship, disability, housing, and social support may produce
   the observed differences.
3. **Buffers and burden can coexist.** Older groups report more emergency funds
   while still reporting care-linked reductions in use and savings.
4. **The cultural/political endpoint remains open.** These measures do not show
   family obligation, dignity, employer fairness, trust, advocacy, or policy
   action.

## Boundaries and counterexamples

The source is cross-sectional and self-reported. `CG4` does not measure care
hours, recipient need, task, distance, paid replacement, or who else helped;
age is not a causal exposure. A necessary counterexample is a young caregiver
whose work and emergency capacity remain stable through paid care, leave,
family support, or public services. Another is an older non-caregiver with
severe borrowing or reduced use from housing, debt, or health costs.

## Reproduction

```text
PYTHONPATH=scripts python3 scripts/analyze_shed_care_age_distribution.py \
  --input /path/to/SHED_2024.csv.zip \
  --output /tmp/shed-care-age.json
```

The analysis uses the official [Federal Reserve SHED data release](https://www.federalreserve.gov/consumerscommunities/shed_data.htm). Raw files and generated JSON are not committed.

Related: [care and work distribution layer](shed-care-work-distribution-layer-v1.md),
[SHED 2024 care/health adaptation layer](shed-2024-care-health-adaptation-layer-v1.md),
and the [aging, care, and social-capacity bridge](../us-aging-care-strain/aging-care-system-capacity-bridge-v1.md).
