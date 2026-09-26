# Finding 001: Housing-assistance entry and exit are followed by different employment and earnings trajectories

**Status:** bounded linked housing-and-work trajectory finding · **Checked:** 2026-09-24

## The bounded finding

The Census CES study links HUD administrative records from 2005–2022 to
matched employee-employer earnings records from 2000–2023 through the LEHD
infrastructure. It follows working-age adults through 16 quarters before and
40 quarters after housing-assistance entry or exit.

For 2.086 million first-time entrants, earnings declined by an average of $112
per year in the four years before entry and rose by $174 per year in the ten
years after entry. The resulting $286-per-year slope change exceeded the
adjusted low-income ACS comparison by $228 per year. The employment slope rose
1.45 percentage points per year, 2.33 points more than the adjusted comparison.

For 1.233 million final leavers, the employment slope fell 1.05 percentage
points per year and the earnings slope fell $244 per year after exit. Relative
to adjusted HUD stayers, the trend breaks were 2.06 percentage points and $268
per year lower. The paper explicitly cautions that pre-existing differences
make a causal counterfactual difficult.

The practical route is:

```text
housing-assistance entry or exit
  -> linked employment and earnings trajectory
  -> possible change in household room and work capacity
  -> housing stability, alternatives, health, trust, and durable security [open]
```

This is a meaningful advance over a simple participation count because the
same linked administrative units are observed across time. It also supplies a
counterexample to simplistic interpretation: entry and exit are selected
events, and exits can reflect higher income, homeownership, relocation, health,
disability, or loss of support. A trajectory around a transition is not
automatically a causal effect of receiving or losing assistance.

## Limits and next test

- Counts and trend magnitudes are rounded for disclosure avoidance, and the
  linked HUD/LEHD data are restricted.
- The comparison balances only observed characteristics available to the study;
  education, occupation, transportation, and detailed family or disability
  measures remain limited or unavailable.
- Employment and earnings do not establish rent burden, housing quality,
  benefit adequacy, alternatives, or household recovery.
- Exit is not necessarily loss: it may reflect improvement, eligibility change,
  relocation, or another unobserved transition.
- The next decisive evidence would link the same participant to assistance
  amount/timing, rent burden, housing quality, work and care changes, exit
  reason, health, appeal or correction, and later security or trust.

## Source

- [Census CES profile for CES-26-31](https://lehd.ces.census.gov/applications/creat/paper-profile/1419)
- [Official Census working paper PDF](https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-31.pdf)

**Evidence status:** official linked administrative research establishes
longitudinal entry/exit and labor-outcome patterns; causal housing, remedy,
health, trust, and durable-security links remain open.
