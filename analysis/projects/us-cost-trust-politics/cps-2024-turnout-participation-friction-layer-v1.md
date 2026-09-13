# CPS 2024 turnout and participation friction layer

**Checked:** 2026-09-12  
**Status:** official population-level descriptive result; reasons for nonvoting are self-reported and not causal explanations.

## What this adds

The ANES panel measures political judgment and reported candidate choice. This
CPS Voting and Registration Supplement adds a different endpoint: whether
people participated, and what nonvoters said prevented participation.

```text
material / social / institutional conditions
  -> time, health, transport, registration, interest, or candidate connection
  -> registration and voting behavior
  -> unequal political voice and collective representation
```

The data do not identify which earlier condition produced a reason, and they do
not turn nonvoting into apathy. “Not interested,” schedule conflict,
registration problems, illness, transport, and dislike of candidates are
different reported mechanisms.

## Official 2024 baseline

The [Census Bureau's 2024 voting and registration release](https://www.census.gov/newsroom/press-releases/2025/2024-presidential-election-voting-registration-tables.html)
reports that 73.6% of the citizen voting-age population registered and 65.3%
reported voting. It reports 63.7% voting among men and 66.9% among women; the
educational gap was 82.5% for people with an advanced degree versus 52.5% for
people with a high school education.

The [official detailed table set](https://www.census.gov/data/tables/time-series/demo/voting-and-registration/p20-590.html)
also provides breakdowns by race and Hispanic origin, age, income, tenure,
disability, employment, family status, residence duration, state, and reasons
for not voting. The CPS supplement has collected comparable voting and
registration information across elections since 1964.

## Reasons reported by nonvoters

Table 10 reports 18.161 million people age 18 and over as not voting. The
percent distribution of their stated reason was:

| Reported reason | Percent of nonvoters |
|---|---:|
| Not interested | 19.7% |
| Too busy or conflicting schedule | 17.8% |
| Did not like candidates or campaign issues | 14.7% |
| Illness or disability | 12.4% |
| Other reason | 12.2% |
| Out of town | 7.4% |
| Registration problems | 3.6% |
| Don't know or refused | 3.1% |
| Inconvenient polling place | 2.4% |
| Transportation problems | 2.2% |
| Forgot to vote | 4.1% |
| Bad weather conditions | 0.3% |

These categories describe the participation barrier as experienced or
reported by the respondent. They should not be added into a single “political
disengagement” score. For example, the schedule category points toward time
control and work/care constraints; illness points toward health and access;
registration and polling-place categories point toward administration; and
candidate dissatisfaction points toward political representation and meaning.

## Cross-group signals

The reason mix changes with life position. Among nonvoters age 18–24, 22.3%
reported a conflicting schedule and 20.4% reported not being interested. Among
those age 65 and over, illness or disability was 35.0% and schedule conflict
was 3.5%. Among Hispanic nonvoters, 23.1% reported not being interested and
21.8% a conflicting schedule; among Black nonvoters, the corresponding shares
were 23.8% and 17.1%.

These are descriptive subgroup differences, not evidence that age, race, or
ethnicity caused a participation barrier. The next comparison should use the
official replicate-weight files and a defined intersectional universe rather
than infer mechanisms from percentages alone.

## Registration, resources, place, and work

The same Census release provides additional distributional signals. Among
citizens in families with reported income under $10,000, 59.0% were reported
registered; among those at $150,000 or more, the figure was 86.4%. These income
tables have a restricted family/relationship universe and exclude people who
did not report knowing their income, so they are not a universal individual
income gradient.

By housing tenure, reported registration was 77.4% for citizens in
owner-occupied units and 63.6% for citizens in renter-occupied units. Among
people with any disability, reported registration was 71.8%, compared with
73.9% for people with no disability. In the labor-force table, reported
registration was 66.6% for unemployed citizens, 74.5% for private-industry
workers, and 70.6% for people not in the labor force.

These are not claims that income, renting, disability, or unemployment causes
nonparticipation. They identify where the next mechanism search should look:
time and schedule control, housing stability and address changes, accessible
registration and polling, work interruption, and the material capacity to
follow political information and procedures.

## Place variation

The state table adds a geographic action layer. Among citizens, reported voting
ranged from 52.8% in Arkansas and 57.9% in Texas to 75.9% in Minnesota and
75.3% in Oregon. The District of Columbia is reported separately and is not a
state comparison. The national citizen voting rate was 65.3%.

This range is a place signal, not a place explanation. It may reflect
registration rules, voting methods, local institutions, campaign intensity,
population composition, mobility, work schedules, or differences in survey
response. The next place test should compare similar populations across states
or counties while measuring registration access, residence duration, transport,
work/care time, and information exposure.

## Place × social position

The state-by-race table shows why state averages are not enough. Nationally,
reported voting among citizens was 70.5% for White non-Hispanic people, 59.6%
for Black people, 57.1% for Asian people, and 50.6% for Hispanic people. The
state table makes those groups available within place, but some cells have
large margins of error: for example, the reported Hispanic rate in Vermont was
74.1% with a 22.5-point margin of error, while the reported Black rate in
Oregon was 78.8% with a 15.6-point margin of error.

That uncertainty is part of the result. A place comparison that ignores cell
size and margin of error can turn sampling noise into a story about culture or
political motivation. The next executable version should pre-specify pooled
regions or multi-election cells, use the replicate weights, and report both
the group gap within place and the place gap within group.

## What this means for the broad program

Political participation is not one outcome. The program now has separate
population layers for:

1. material adjustment and financial worry (SHED);
2. institutional trust and political judgment (ANES);
3. candidate choice measured after the election (ANES panel); and
4. voting, registration, and reported participation barriers (CPS).

The missing societal bridge is still attribution: which prices, work rules,
care burdens, public-system experiences, media environments, or local
conditions changed participation for whom? A future linked or quasi-experimental
pass must measure those exposures separately and preserve nonvoters who face
access barriers, not treat turnout as a pure preference signal.

## Limits

The CPS measure is a survey report, not an administrative vote count. The
Census Bureau notes that survey estimates can differ from administrative data
or exit polls because of nonresponse, vote misreporting, question wording, and
survey administration. The table is cross-sectional for the 2024 election;
it does not follow the same respondent from a cost or institutional event to a
later vote.
