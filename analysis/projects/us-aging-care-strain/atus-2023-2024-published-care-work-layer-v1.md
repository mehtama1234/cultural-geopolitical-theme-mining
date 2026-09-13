# ATUS 2023–2024 published care, work, and social-availability layer v1

**Checked:** 2026-09-13  
**Status:** official published-table comparison; descriptive population layer, not a causal care-to-work estimate

## Why this layer matters

The broader program treats care as social infrastructure. A care need can be
paid, unpaid, delayed, shared, or transferred into work and family time. This
layer adds an official population-scale estimate to the broader chain:

```text
aging-related care need
  -> unpaid care and coordination time
  -> work, leisure, social, civic, and family-time conditions
  -> household security, employer pressure, service demand, or political meaning
```

The table does not identify which activity was displaced. It tells us how large
the care population is, which groups carry more of the reported care exposure,
and how much time appears on care days.

## Source and unit

The source is the Bureau of Labor Statistics [2023–2024 Unpaid Eldercare in
the United States release](https://www.bls.gov/news.release/elcare.toc.htm),
based on combined American Time Use Survey years 2023 and 2024. An eldercare
provider is a person age 15 or older who, during the prior three to four
months, cared for someone with an aging-related condition; the published
estimates are restricted to people who cared for at least one person age 65 or
older. The population denominator is the civilian noninstitutional population
age 15 and over. This is a respondent-level population layer, not a family
panel or a care-recipient outcome record.

## Population scale and distribution

| Group | Population (thousands) | Eldercare providers (thousands) | Provider rate |
|---|---:|---:|---:|
| Total, 15+ | 272,126 | 38,192 | 14.0% |
| Men | 132,989 | 17,201 | 12.9% |
| Women | 139,137 | 20,990 | 15.1% |
| Age 45–54 | 40,003 | 7,508 | 18.8% |
| Age 55–64 | 41,312 | 9,974 | 24.1% |
| Age 65+ | 58,995 | 9,919 | 16.8% |
| Employed | 174,244 | 23,569 | 13.5% |
| Full-time workers | 138,031 | 18,386 | 13.3% |
| Not employed | 97,882 | 14,622 | 14.9% |
| Parent of a household child under 18 | 66,214 | 7,616 | 11.5% |

The pattern is not simply “retired people provide care.” The provider rate is
highest in the 55–64 group at 24.1%, and 23.6 million providers are employed.
The employed and full-time rates are close to the overall population rate, so
care is simultaneously a labor-market and later-life issue. Women have a
higher provider rate than men in the published table, while the difference is
also conditioned by age, household structure, employment, and relationship to
the recipient.

Source: [BLS Table 1](https://www.bls.gov/news.release/elcare.t01.htm).

## Time on the care day

Across all eldercare providers, 27.6% provided care on an average day. They
spent 1.07 hours per day on average when all providers are included, and 3.88
hours on days on which they actually engaged in eldercare. For employed
providers, 21.3% provided care on an average day, averaging 0.61 hours per day
across all employed providers and 2.84 hours on care days. Full-time workers
averaged 2.81 hours on care days.

This distinction matters. A population estimate averaged over all days and a
care-day estimate answer different questions. The former describes the burden
spread across ordinary time; the latter describes the intensity of a care day.

| Group | Care providers (thousands) | Care on average day | Hours/day, all providers | Hours on care days |
|---|---:|---:|---:|---:|
| Total, 15+ | 38,192 | 27.6% | 1.07 | 3.88 |
| Employed | 23,569 | 21.3% | 0.61 | 2.84 |
| Full-time workers | 18,386 | 20.4% | 0.57 | 2.81 |
| Not employed | 14,622 | 37.8% | 1.82 | 4.83 |
| Age 55–64 | 9,974 | 30.4% | 1.25 | 4.11 |
| Age 65+ | 9,919 | 39.5% | 1.95 | 4.93 |

Source: [BLS Table 4](https://www.bls.gov/news.release/elcare.t04.htm).

## What happens inside the care day

The care day is not only direct physical care. In the published Table 5,
household activities accounted for 22.9% of reported eldercare activity time,
caring for or helping household members 9.0%, caring for or helping
nonhousehold members 8.8%, leisure and sports 33.7%, socializing and
communicating 10.5%, and travel 5.2%. The activity shares can sum to more than
100% across providers because respondents may report more than one activity.

Among providers on care days, 20.9% engaged in caring for or helping household
members and 22.9% engaged in caring for or helping nonhousehold members. Only
2.7% engaged in working or work-related activities on those care days in the
published table. That last figure must not be read as “care caused people to
stop working”: the diary day is not a counterfactual, and workers may provide
care on non-work days or outside reported work activities.

Source: [BLS Table 5](https://www.bls.gov/news.release/elcare.t05.htm).

## Frequency changes the social meaning of the burden

Frequency is a major distributional distinction. On care days, people who
provided care daily averaged 4.98 hours of eldercare, compared with 2.24 hours
among those providing care several times per week and 2.28 hours among those
providing care once a week or less. Daily-care providers were also more likely
to report household care activities: 32.3% cared for or helped household
members, compared with 4.4% among providers caring several times per week and
5.7% among those caring once a week or less.

For nonhousehold adults, the pattern reverses in a useful way: 29.3% of the
several-times-per-week group reported helping nonhousehold adults, compared
with 6.8% of the daily group. This is a counterexample to treating all care as
one household-bound experience. Care frequency and recipient relationship can
change whether the burden is concentrated in household coordination or spread
through kin and community networks.

Source: [BLS Table 7](https://www.bls.gov/news.release/elcare.t07.htm).

## What this adds to the societal program

This layer strengthens three broad observations:

1. **Care is a population institution, not a private anomaly.** Tens of
   millions of people report recent eldercare, and the burden is concentrated
   in working-age later-life groups as well as older adults.
2. **Time is a social currency.** Care appears through direct help, household
   work, travel, purchasing, communication, and coordination—not only through
   a medical bill.
3. **Care can carry cultural and political meaning through unequal capacity.**
   The same care need can be absorbed by a worker, a non-employed person, a
   household member, or a wider kin network. The distribution of that capacity
   is a plausible route into employer demands, public-service demand, family
   norms, dignity, and political judgment.

These are population-level interpretations of separate published tables. They
do not prove a care-induced reduction in work, civic participation, health, or
trust.

## Next linkage

The strongest next test is to combine this population layer with an accessible
ATUS microdata extract or a valid panel that contains the same respondent's
employment schedule, care frequency, household composition, health, and later
wellbeing. The required counterexample is a similar care exposure with stable
work, health, and social availability because paid support, flexible work,
family help, or public services protected the respondent.

The political endpoint remains open: this table measures time and care, not
attribution, fairness, belonging, trust, organizing, turnout, or vote choice.
