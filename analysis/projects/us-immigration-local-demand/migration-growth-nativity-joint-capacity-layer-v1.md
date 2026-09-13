# Migration proxy axes: joint growth, nativity, and local capacity v1

**Checked:** 2026-09-13
**Status:** exploratory joint county comparison; not a migration causal estimate

## Why a joint test is needed

Total population growth and foreign-born share measure different things:

- growth includes births, deaths, domestic moves, and international migration;
- foreign-born share is a population stock, not a recent-arrival flow;
- neither variable identifies a person's reason for moving or a service
  encounter.

If the two axes are collapsed into “migration pressure,” the analysis cannot
show whether capacity patterns are associated more with resident growth,
population composition, or both. This pass ranks counties on both axes and
looks at the intersection.

## Unit and construction

The unit is a US county with at least 100,000 residents, usable 2020 and 2023
population estimates, 2023 ACS foreign-born share, and 2023 CBP sector data.
The run covers 620 counties. Counties are placed into four equal-sized
quartiles on 2020–2023 population change and four equal-sized quartiles on
2023 foreign-born share. Cells are not weighted to a national population; the
cell sizes vary because the two rankings cross.

The capacity measures are 2023 CBP establishments or employees per 10,000
2023 residents in retail, health/social assistance, and accommodation/food.
They measure visible employer presence or employment scale—not service use,
quality, prices, wages, ownership, or unmet need.

## Joint results

The table below shows health/social-assistance employment per 10,000 residents.
Growth quartile 1 is the lowest-growth quarter and quartile 4 the highest;
foreign-born quartile 1 is the lowest-share quarter and quartile 4 the highest.

| Growth quartile | Foreign-born quartile 1 | Quartile 2 | Quartile 3 | Quartile 4 |
|---|---:|---:|---:|---:|
| 1 | 663.49 (n=52) | 725.37 (n=34) | 768.71 (n=23) | 681.45 (n=46) |
| 2 | 595.15 (n=36) | 650.52 (n=32) | 774.17 (n=42) | 684.96 (n=45) |
| 3 | 548.70 (n=43) | 582.68 (n=38) | 685.21 (n=40) | 598.65 (n=34) |
| 4 | 412.10 (n=24) | 429.30 (n=51) | 455.74 (n=50) | 436.23 (n=30) |

The highest-growth quartile has lower health/social-assistance employment per
resident across every foreign-born-share quartile in this screen. Within the
growth quartiles, the foreign-born axis is not monotonic: the highest-share
cell is not always the lowest-capacity cell, and the third foreign-born
quartile is often higher.

The pattern is similar but weaker for retail employment. The low-growth/high-
foreign-born cell has 448.68 employees per 10,000, while the high-growth/high-
foreign-born cell has 444.64. Food employment is more irregular: the
low-growth/high-foreign-born cell has 461.71, while the high-growth/high-
foreign-born cell has 389.37.

Health/social-assistance establishments show the same distinction between the
axes. The low-growth/high-foreign-born cell has 33.34 establishments per
10,000, while the high-growth/high-foreign-born cell has 26.31. The high-
growth/low-foreign-born cell is lower still at 22.88. Presence and employment
therefore move together imperfectly, and neither resolves practical adequacy.

## What this adds to the broader program

This joint screen supports a more precise place hypothesis:

```text
resident growth and composition
  -> demand, workers, and service users
  -> sector capacity and employment scale
  -> travel, wait, price, quality, ownership, and access
  -> unequal exposure, belonging, trust, and political response
```

The observed contrast is more consistent with a growth/capacity relationship
in the health-sector stock than with a simple foreign-born-share gradient. That
is an inference from the joint descriptive pattern, not a causal conclusion.
It also supplies counterexamples to a one-direction narrative: high foreign-
born-share counties do not uniformly have low capacity, and high-growth places
do not all have the same service profile.

## Limits

- 2020–2023 population change is a mixed demographic proxy, not immigration.
- 2023 ACS foreign-born share is a stock; the available arrival field is not a
  2020–2023 flow.
- 2023 CBP capacity is measured after the growth window and cannot establish
  timing or causation.
- County averages conceal within-county inequality, neighboring-place access,
  commuting, and service quality.
- No respondent-level belonging, fairness, blame, trust, turnout, or policy
  response is joined here.

## Reproduction

```text
python3 scripts/analyze_nativity_capacity_all_counties.py \
  --cbp /tmp/cbp23co.zip \
  --population /tmp/co-est2024-alldata.csv \
  --nativity /tmp/acsdt5y2023-b05002.dat \
  --arrival /tmp/acsdt5y2023-b05005.dat \
  --min-population 100000 --joint \
  > /tmp/nativity-joint-capacity.tsv
```

The joint output is an exploratory conditioning layer. The next place pass
should add housing supply, travel, wages, provider adequacy, and direct local
meaning/action measures before interpreting capacity as lived access or
political conflict.
