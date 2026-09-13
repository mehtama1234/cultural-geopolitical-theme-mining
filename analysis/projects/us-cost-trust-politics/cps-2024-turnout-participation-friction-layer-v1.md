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
