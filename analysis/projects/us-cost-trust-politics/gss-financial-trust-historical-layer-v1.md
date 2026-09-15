# GSS financial satisfaction and trust historical layer v1

The cumulative GSS file supplies a long-run context for the 2024
financial-position/trust screen. Using anchor years with valid financial
satisfaction, trust, and fairness fields, the association between material
satisfaction and social meaning remains visible across the series, but its
level and comparability require caution.

| Year | Not satisfied at all | Trust most people: not satisfied | Trust most people: pretty well satisfied | Fair most people: not satisfied | Fair most people: pretty well satisfied |
|---:|---:|---:|---:|---:|---:|
| 1972 | 21.93% | 39.45% | 49.60% | 53.10% | 63.62% |
| 1980 | 28.28% | 34.83% | 50.69% | 48.28% | 68.78% |
| 1990 | 27.15% | 26.67% | 44.30% | 44.45% | 66.00% |
| 2000 | 22.92% | 23.60% | 42.33% | 37.07% | 62.68% |
| 2010 | 31.31% | 24.23% | 40.54% | 44.70% | 63.92% |
| 2014 | 26.40% | 18.97% | 38.10% | 35.27% | 63.71% |
| 2018 | 21.41% | 25.54% | 44.02% | 37.65% | 65.62% |
| 2022 | 30.16% | 11.53% | 39.78% | 27.99% | 57.00% |
| 2024 | 30.94% | 14.95% | 32.90% | 23.66% | 58.87% |

The repeated contrast is not a simple historical law. In 2024, for example,
trust and fairness expectations are lower among respondents not satisfied with
their finances than among those pretty well satisfied. But generalized trust
also moves across the entire society over time, and the gap changes rather than
remaining constant. Cohort, age, education, race, health, party identity,
survey mode, question administration, and broad institutional conditions may
all contribute.

This is an anchor-year descriptive screen, not an unbroken annual trend or a
causal economic-voting estimate. It uses the cumulative file's `WTSSPS`
person post-stratification weight for a common historical screen. It does not
substitute the 2024 `WTSSNRPS` nonresponse-adjusted weight used in the
single-year layer. Variable availability is incomplete in some intervening
years, and the 2024 multi-mode/design change requires separate harmonization.
Trust and fairness have their own valid-field universes within each year.

The layer strengthens the program's material condition → social meaning arrow
by showing persistence of the comparison across decades while also supplying a
counterexample to treating trust as a direct readout of financial distress.
It does not identify a dated bill, local exposure, institutional remedy,
behavioral adaptation, consumer exit, political action, or geopolitical
consequence.

[Machine-readable record](../../records/us-gss-financial-trust-historical-1972-2024.json)  
Analysis script: `scripts/analyze_gss_financial_trust_historical.py`

Sources: [NORC GSS data downloads](https://gss.norc.org/get-the-data.html),
[cumulative Stata download](https://gss.norc.org/get-the-data/stata.html), and
[2024 codebook](https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook%20R3.pdf).
