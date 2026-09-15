# BLS JOLTS national mobility layer v1

**Question:** How did the US national balance between open jobs, hiring,
voluntary quits, layoffs, and total separations change from 2020 through 2025?

The [BLS Job Openings and Labor Turnover Survey](https://www.bls.gov/jlt/)
publishes monthly national estimates of openings, hires, and separations. This
layer retrieves the seasonally adjusted total-nonfarm rates through the BLS
public API and computes transparent calendar-year arithmetic means. BLS defines
the job-openings rate using openings divided by employment plus openings, while
hires and separation rates use their respective published employment-based
denominators; the rates are therefore not interchangeable probabilities.

## Observed pattern

The annual mean job-openings rate rose from 4.28% in 2020 to 6.85% in 2022,
then fell to 4.28% in 2025. The quits rate rose from 2.08% to 2.76% between
2020 and 2022, then declined to 2.02% in 2025. The hires rate also declined
from 4.34% in 2021 to 3.32% in 2025, while the layoffs-and-discharges rate
remained near 1.0–1.1% in 2021–2025 after the 2020 shock.

This is consistent with a cooling labor-market mobility context after 2022:
fewer openings and voluntary quits coexist with lower hiring. It does not say
whether workers lost bargaining power, whether pay or schedules worsened, or
whether employers substituted monitoring or technology.

## Boundary and next test

JOLTS is an establishment survey with national aggregate rates. It does not
follow people, identify who quits or is laid off, measure job quality, wages,
training, schedule control, union coverage, household effects, or political
meaning. Revisions and seasonal-adjustment updates can change recent values.

The next work/control test is to condition labor-market churn on occupation,
industry, establishment size, worker demographics, and union or AI exposure,
then connect a defined worker event to pay, schedule discretion, household
room, voice, and exit.

