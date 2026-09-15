# New York Fed Economic Heterogeneity Indicators: distribution before interpretation

**Checked:** 2026-09-13  
**Status:** official December 2025 national indicator extraction · descriptive and derived

## What this layer adds

The New York Fed's Economic Heterogeneity Indicators place demographic and
regional exposure between a national macro statistic and a household's own
price experience. The December 2025 release reports constructed inflation gaps,
earnings ratios, employment outcomes, retail spending, wealth, and small-
business conditions. This matters for the broader program because a public
economic message may be heard against different baskets, earnings positions,
and spending capacity.

## Directly recorded results

The national release reports that, in December 2025, Hispanic households had an
estimated inflation rate 0.39 percentage points below the national average,
households headed by someone under 25 were 0.29 points below, and the South
was 0.51 points below. The Northeast was 0.57 points above and the West 0.23
points above. These are demographic-CPI estimates, not official demographic
CPIs published by BLS.

The same release reports December earnings ratios of 78.7% for Black workers
relative to white workers, 77.5% for Hispanic workers relative to white
workers, 57.4% for workers without a college degree relative to workers with a
degree, 81.1% for women relative to men, and 86.7% for rural relative to urban
workers. These ratios describe workers who are employed; they do not measure
employment access, hours, occupations, or bargaining power by themselves.

For retail consumption, the release reports that since 2023 real consumption
among high-income households increased, middle-income consumption remained
flat, and low-income consumption decreased by November 2025. The indicator is
based on receipt-level Numerator data from a balanced panel of about 200,000
households and demographic-specific deflators. It is an aggregate panel trend,
not a same-household causal estimate of inflation, income, or policy exposure.

## Method and limits

Demographic inflation combines prior-year Consumer Expenditure Survey budget
shares with category and metro CPI inflation. It uses 23 major metropolitan
areas plus regional assignments for smaller places. The method assumes that
people within a metro area face the same category prices and uses urban prices
for the rural comparison. The New York Fed explicitly describes these as
constructed indicators rather than official estimates of the Federal Reserve
System or FOMC.

The spending series uses Numerator receipts and permissioned email data. It can
show group-level spending direction, but not cash-flow stress, product-level
substitution for a given family, debt service, or why a household changed its
spending.

## End-to-end connection

```text
different basket / earnings position / wealth
  -> different experienced pressure and room
  -> different interpretation of a rate or price message
  -> different expectation, substitution, delay, or spending response
  -> possible trust, blame, or political judgment
```

The first two arrows are supported as distributional measurement and method.
The New York Fed indicators do not measure the messenger, trust, attribution,
or later politics. The NBER Federal Reserve trust experiment supplies a
separate information-processing layer, and the SHED supplies separate
household adaptation measures. Combining them produces a testable hypothesis,
not a pooled estimate.

## Next test

Join a dated public communication or rate announcement to household-level
prices, debt and deposit exposure, financial margin, source receipt, trust,
expectations, and realized spending. Compare groups with different baskets and
earnings positions, and retain cases where the same message did not change
behavior. A valid join must separate assigned demographic inflation from the
actual price paid by a specific household.

## Sources

- [New York Fed Economic Heterogeneity Indicators](https://www.newyorkfed.org/research/economic-heterogeneity-indicators)
- [December 2025 national EHI report](https://www.newyorkfed.org/medialibrary/research/interactives/data/economic-heterogeneity-indicators/downloads/12-2025_ehi_national_full.pdf?hash=9ED1DF9F83095FAE63BA1946341924C9&sc_lang=en)
- [New York Fed EHI methodology FAQ](https://www.newyorkfed.org/research/economic-heterogeneity-indicators/ehi-faq)
