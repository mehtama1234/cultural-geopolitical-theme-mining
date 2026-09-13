# SHED 2024 care, health, and price-adaptation layer v1

**Checked:** 2026-09-12
**Unit:** US adult respondent; 2024 Federal Reserve SHED
**Method:** weighted descriptive percentages using `weight`; each measure uses its own nonmissing denominator; no design-based standard errors or causal estimate

## Why add a second survey year

The 2025 care/health layer shows that medical-cost concern, unpaid adult care,
and poorer self-rated health align with different financial adaptation menus.
This pass runs the same available fields in the 2024 SHED file. It tests
whether the broad distributional shape is visible in another survey year; it
does not create a panel link between 2024 and 2025 respondents.

```text
medical concern, care responsibility, or health limitation
  -> different money and work responses
  -> different buffers and displaced needs
  -> possible care, trust, institutional, and political consequences
```

## Selected 2024 results

| Group comparison | Price worsened finances | Used less/stopped | Increased borrowing | Reduced savings | Worked more/got job | Three-month funds |
|---|---:|---:|---:|---:|---:|---:|
| Medical cost: not a concern | 45.6% | 48.0% | 9.2% | 30.2% | 11.3% | 65.1% |
| Medical cost: major concern | 77.4% | 78.7% | 25.1% | 60.3% | 28.7% | 38.7% |
| Unpaid adult care: no | 58.1% | 59.6% | 14.5% | 40.5% | 16.8% | 55.9% |
| Unpaid adult care: yes | 67.0% | 69.9% | 22.2% | 53.7% | 21.9% | 51.0% |
| Health: excellent | 48.8% | 53.4% | 10.3% | 37.1% | 20.1% | 65.7% |
| Health: poor | 72.1% | 71.0% | 27.6% | 48.0% | 16.8% | 21.5% |

The 2024 gradients broadly match the 2025 layer: major medical-cost concern,
regular unpaid adult care, and poorer health coincide with more reduced use,
borrowing, and saving cuts and with less emergency capacity. The labor response
is not monotonic: people reporting poor health worked more in neither year,
which is consistent with a constrained adaptation menu rather than lower
pressure. The comparison is descriptive and the samples are not treated as the
same respondents.

## What this adds to the societal trend map

1. **The care-cost pattern is not limited to one annual release.** The same
   directional structure appears in 2024 and 2025 cross-sectional SHED layers.
2. **Adaptation is behavior-specific.** Borrowing, reduced use, saving cuts,
   extra work, and emergency funds do not form one interchangeable stress
   measure.
3. **Care and health alter the available response menu.** A person may protect
   care or consumption by borrowing or cutting savings, while poor health may
   limit the ability to respond through paid work.
4. **The cultural and political arrows remain open.** Repeated adaptation does
   not by itself establish blame, dignity, trust, public demand, or political
   action.

## Boundaries and counterexamples

The 2024 and 2025 layers use different cross-sectional samples and do not
support a year-over-year causal claim. Medical-cost concern, care, and health
are self-reported group variables; they do not identify a dated bill, care
hours, coverage rule, recipient, family transfer, or which need was displaced.
Outside-help field `FS21_c` was not present in the 2024 file, so it is excluded
rather than imputed or silently compared.

A necessary counterexample is a respondent with major medical concern or poor
health whose emergency capacity and use do not deteriorate, because insurance,
cash, family support, public assistance, or job control protected them. A
second is someone whose emergency funds fall without a medical or care concern.

## Reproduction

```text
python3 scripts/analyze_shed_care_health_year.py \
  --input /path/to/SHED_2024.csv.zip \
  --output /tmp/shed-2024-care-health.json
```

The raw 2024 file contains 12,295 rows after reading the official CSV. The
analysis uses the official [Federal Reserve SHED data release](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
Raw files and generated JSON are not committed.

Related: [2025 care, health, and price-adaptation layer](shed-2025-care-health-price-adaptation-layer-v1.md),
[care cost, work, family time, and security layer](care-cost-work-family-security-layer-v1.md),
and the [broad trend register](../../US-PROVISIONAL-SOCIETAL-TRENDS_V1.md).
