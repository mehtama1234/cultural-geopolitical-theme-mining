# SHED care and work distribution layer v1

**Checked:** 2026-09-12
**Unit:** US adult respondent; 2024 Federal Reserve SHED
**Method:** weighted descriptive cross-tab of regular unpaid adult care and employment status; no variance estimate or causal model

## Why this split matters

Care is not a single household condition. The same care responsibility can be
absorbed while working full-time, working part-time, or not working, and those
positions provide different amounts of income, schedule control, and capacity
to respond to financial pressure. This pass adds the work position to the
existing care/health adaptation layer.

```text
unpaid adult care
  + employment position
  -> different money, time, and adaptation options
  -> different buffers and possible work/care tradeoffs
```

## Selected 2024 results

| Care status | Employment status | Price worsened finances | Used less/stopped | Increased borrowing | Reduced savings | Worked more/got job | Three-month funds |
|---|---|---:|---:|---:|---:|---:|---:|
| No regular unpaid adult care | Not working | 55.6% | 55.1% | 11.3% | 37.6% | 7.5% | 54.8% |
| No regular unpaid adult care | Working part-time | 56.7% | 61.7% | 15.5% | 42.0% | 27.3% | 49.1% |
| No regular unpaid adult care | Working full-time | 60.2% | 62.2% | 16.4% | 42.2% | 20.6% | 58.5% |
| Regular unpaid adult care | Not working | 66.0% | 67.5% | 19.8% | 50.3% | 10.4% | 48.6% |
| Regular unpaid adult care | Working part-time | 67.1% | 72.8% | 21.3% | 51.4% | 26.8% | 49.9% |
| Regular unpaid adult care | Working full-time | 67.8% | 70.7% | 24.4% | 57.4% | 29.7% | 53.5% |

Caregivers report more reduced use, borrowing, and saving cuts than people not
reporting regular unpaid adult care within each employment position. Among
caregivers, full-time workers report the highest borrowing and saving cuts and
the highest share working more or getting a job; nonworking caregivers still
report substantial pressure and the lowest emergency-fund share among the
caregiver cells. These are group alignments, not evidence that care caused the
financial response or that employment protected or harmed a particular person.

## What this adds to the broad societal program

1. **Care and work interact.** Caregiving changes the adaptation menu in every
   employment group, but the available labor response differs.
2. **Employment is not a complete security measure.** Full-time caregivers
   report more borrowing and saving cuts than nonworking caregivers, while
   retaining somewhat more emergency capacity; pay, hours, schedule control,
   leave, and household resources are still missing.
3. **Unpaid labor is part of the economic system.** A person can be working,
   caring, and cutting consumption simultaneously; “employed” does not mean
   care has no cost.
4. **The political and cultural endpoint remains open.** These data do not
   show dignity, family obligation, employer fairness, institutional trust,
   advocacy, or policy action.

## Boundaries and counterexamples

The source is cross-sectional and self-reported. `CG4` does not provide care
hours, recipient condition, task, distance, paid replacement, family division,
or schedule flexibility. `ppemploy` does not provide pay, hours, job control,
leave, or whether work changed because of care. The adaptation questions refer
to a prior period and have their own nonmissing denominators.

Required counterexamples include a caregiver whose work and emergency funds
remain stable because of paid care, leave, family support, or public services,
and a non-caregiver whose borrowing or reduced use is equally severe because of
housing, health, or debt. Those cases prevent a simple “caregiver penalty”
interpretation.

## Reproduction

```text
PYTHONPATH=scripts python3 scripts/analyze_shed_care_work_distribution.py \
  --input /path/to/SHED_2024.csv.zip \
  --output /tmp/shed-care-work.json
```

The analysis uses the official [Federal Reserve SHED data release](https://www.federalreserve.gov/consumerscommunities/shed_data.htm). Raw files and generated JSON are not committed.

Related: [SHED 2024 care/health adaptation layer](shed-2024-care-health-adaptation-layer-v1.md),
[2025 care/health adaptation layer](shed-2025-care-health-price-adaptation-layer-v1.md),
and the [aging, care, and social-capacity bridge](../us-aging-care-strain/aging-care-system-capacity-bridge-v1.md).
