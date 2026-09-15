# Care time is a household price paid in work, money, and reachable places

**Status:** provisional cross-source finding · **Scope:** US care, work, time,
transport, and material adaptation · **Checked:** 2026-09-14

## Short answer

Care is not only a private feeling or a service category. It is a time claim
on a household. When that claim arrives alongside higher prices, limited
transport, or a fixed work schedule, the family has to decide what remains
reachable and what gets deferred. The available evidence shows the pieces of
that trade clearly: care is widespread and uneven; working caregivers report
more price-related adaptation than otherwise similar employment groups; and
low-resource households face a different transport option set. But the
sources are not one longitudinal sample, so this is a bounded mechanism under
test, not proof that care caused a particular loss of work, health, trust, or
political action.

## The deeper finding

The useful unit is not “caregiver” by itself. It is the combination of care
time, schedule control, money available, transport, and the consequence that
the household protects or sacrifices. A person can preserve paid work by
buying replacement care, asking another relative for help, taking a longer
trip, or using savings. Another person can preserve the care obligation by
working less, skipping a purchase, borrowing, or allowing a bill to run late.
The visible outcome may look like a work decision, a financial problem, or a
transport problem even when the underlying scarcity is the same limited week.

This is why an annual care prevalence number cannot be read as a work-loss
estimate. It also explains why a time-use average cannot be treated as a
household burden score. Paid work, household labor, direct care, travel,
social time, and secondary child care are separate currencies. Their
distribution matters precisely because a household may trade one for another.

## What the sources directly show

The 2024 American Time Use Survey (ATUS) merged file contains 7,669 valid
diary respondents age 15+. Its weighted averages are 190.8 minutes of primary
work, 120.7 minutes of household work, 32.8 minutes caring for people, 65.0
minutes traveling, and 273.6 minutes socializing or communicating per diary
day. Secondary child care averages 76.7 minutes and eldercare 11.0 minutes.
These are population time-use estimates, not minutes displaced by a known
care event. [The machine-readable ATUS record](../records/us-atus-time-care-microdata-2024.json)
preserves the diary respondent denominator, standard errors, and the warning
that these currencies must not be added into one burden index.

The distribution is not neutral across people. In the same ATUS layer, women
average 141.0 primary household-work minutes versus 99.4 for men, and 40.5
primary care-for-people minutes versus 24.7. Women also average 91.9 minutes
of secondary child care versus 60.8 for men, while men average more primary
work minutes. Adults age 25–44 average 272.6 work minutes and 56.7 primary
care minutes; adults age 65+ average 44.6 work minutes and 21.6 eldercare
minutes. These comparisons describe allocation, not unequal effort caused by
one institution. The [ATUS annual comparison record](../records/us-atus-time-care-annual-comparison-2024-2025.json)
keeps the year-to-year boundary visible.

The official combined 2023–2024 ATUS eldercare tables estimate that 14.0% of
the civilian noninstitutional population age 15+ provide eldercare—about 38.2
million people. Among employed eldercare providers, 21.3% provide care on an
average day and spend 2.84 hours on care days; among full-time providers the
corresponding figures are 20.4% and 2.81 hours. Care is especially visible in
later working life: 24.1% of people age 55–64 are eldercare providers, and
30.4% of those providers provide care on an average day. The [eldercare record](../records/us-atus-eldercare-work-time-2023-2024.json)
preserves the population and provider denominators. It does not show whether
work was refused, shifted, or lost.

The 2024 Federal Reserve SHED care/work comparison supplies a different but
important angle. Among adults reporting regular unpaid adult care, 67.8% of
full-time workers said price changes worsened their finances, 70.7% used less
or stopped buying something, 24.4% increased borrowing, and 57.4% reduced
savings. The corresponding figures for full-time adults without reported
regular unpaid adult care were 60.2%, 62.2%, 16.4%, and 42.2%. For part-time
workers, the care/no-care contrasts were also visible: 72.8% versus 61.7%
used less or stopped, and 21.3% versus 15.5% increased borrowing. The [SHED
record](../records/us-shed-care-work-adaptation-2024.json) makes clear that
each percentage has its own nonmissing outcome denominator and that the
cross-section cannot establish a care effect or measure care hours.

The transport layer shows why the same care obligation can have different
prices by place and resources. In 2022 NHTS data, 35.2% of urban households
under $35,000 had zero vehicles, compared with 3.5% of urban households at
$75,000 or more. In rural areas the corresponding figures were 12.8% and
0.7%. Yet long recorded work trips were more common among higher-income
rural households: 53.4% of recorded rural work trips lasted at least 30
minutes, compared with 13.9% among lower-income rural work trips. Shopping
trips also differ: the urban low-income mean was 34.0 minutes versus 20.7
minutes for the higher-income group. These are trip and household measures,
not unmet care trips or welfare outcomes. The [NHTS record](../records/us-nhts-mobility-material-work-care-2022.json)
preserves those separate denominators and the urban/rural counterexample.

Finally, the 2024 SIPP bridge provides a narrow same-person follow-up. Among
stable non-SNAP-status pairs, people reporting that child care prevented work
or more work had a December utility-hardship share of 16.9%, versus 7.8% for
those reporting no such prevention. The prevention cell is small (71 valid
pairs), and its approximate 95% interval is 7.6–26.2%; therefore the point
difference is not a population-wide effect estimate. Among stable SNAP pairs,
the child-care-work-prevention cell is smaller still (23 pairs), with a
43.7% rent/mortgage-hardship estimate and a wide 21.7–65.6% interval. The
[SIPP record](../records/us-sipp-childcare-work-hardship-bridge-2024.json)
keeps the transition-pair and weighted denominators visible. It is the
strongest local bridge here, but it still lacks care quality, exact timing,
recovery, and political meaning.

The current-vintage SIPP intersection refreshes add an important distributional
qualification to that bridge. In displayed race-by-tenure-by-resource cells,
renter/owner differences in utility difficulty and food-security measures are
visible at both low and high resource endpoints, although the Black-alone
ordering is not uniform and some hunger cells are imprecise. In the separate
work-limitation-by-resource layer, people reporting a work-limiting condition
show more utility difficulty, lower high/marginal food security, and fewer
one-job records within the displayed race groups. These layers sharpen the
available-room comparison but are person-weighted, not household-weighted;
they do not measure a dated care event, accommodation, hours lost, schedule
control, or the later cultural or political consequences. See the [race,
tenure, and resource finding](../projects/us-household-calendar-integration/findings/us-household-calendar-integration-022.md)
and [work-limitation and resource finding](../projects/us-household-calendar-integration/findings/us-household-calendar-integration-023.md).

## Mechanism under test

```text
care need or care responsibility
  -> available hours, schedule control, and transport options change
  -> paid care, unpaid substitution, longer travel, reduced purchases,
     borrowing, saving cuts, or work change
  -> one obligation is protected while another is delayed or sacrificed
  -> bill, health, work continuity, family routine, and social availability
     may diverge
  -> later recovery, trust, collective action, or exit becomes possible
```

The first arrow is directly measured by ATUS time allocation and the SHED
care grouping. The second is partly measured by SHED adaptation responses and
the SIPP work-prevention item. The transport record supplies a conditioning
factor: the cost of protecting care depends on vehicles, distance, and place.
The protected/sacrificed pairing and later meaning/action remain open. The
2025 SHED price record, for example, reports that 77% of adults took at least
one action after higher prices and 58% said prices worsened their finances,
but it cannot identify whether care was the reason for a particular action.
See the [price-adaptation record](../records/us-federal-reserve-price-adaptation-judgment-2025.json).

## Who gains, loses, adapts, or exits

Households with cash, flexible work, reliable vehicles, nearby services, or
available family support can purchase time or change the order of obligations.
That is an options advantage, not proof that their care load is smaller.
Workers with less schedule control may have to protect paid work by reducing
consumption or savings; workers with less transport access may spend more
time reaching work, shopping, or care. Employers and service providers can
benefit from the hidden substitution when the household absorbs the cost
privately. Public systems can reduce the pressure if assistance is timely and
reachable, but a benefit that arrives after the missed shift or unsafe trip
does not restore the lost option automatically.

The evidence does not yet show who exits a job, care arrangement, provider,
neighborhood, or political institution. Those are the next outcomes to
measure, not conclusions to infer from time allocation.

## Counterexamples and boundaries

Several observations resist a simple “care reduces work” story. Many people
provide care while working full time; the ATUS data show coexisting work and
care rather than a universal substitution. Rural high-income households show
longer recorded work trips than rural low-income households even though they
have greater vehicle access, so time burden is not reducible to vehicle
scarcity. Nonworking caregivers in SHED still report substantial price
adaptation, while some non-caregivers also borrow, reduce savings, or work
more. These are not noise to be averaged away: they indicate that income,
health, family structure, job conditions, place, and available substitutes
modify the mechanism.

## What is observed, inferred, and still open

**Observed or reported:** time-use distributions; eldercare prevalence and
care-day intensity; SHED price-related actions by care/employment group;
vehicle scarcity and recorded trip durations by place/income; and the bounded
SIPP association between child-care work prevention and following-month
hardship.

**Inferred but bounded:** care can operate as a hidden household price because
the sources show its time claim, adaptation correlates, and option-set
differences. The inference is a cross-source mechanism, not a causal estimate.

**Still open:** a dated care or bill event; the exact alternative considered;
who controlled the schedule or could refuse; which outcome was protected;
whether the same household recovered; and whether the experience changed
trust, identity, collective action, voting, provider exit, or institutional
legitimacy.

## What would change the finding

The finding would weaken if a same-unit design showed that care exposure did
not alter time, work, spending, or hardship after accounting for baseline
resources and composition, or if the observed SHED contrasts disappeared when
care intensity and job flexibility were measured. It would strengthen if a
repeated person/family design showed that a dated care change preceded a
specific work, time, or hardship change, with a comparable counterexample and
measured alternatives. A stronger version would then require a defined
follow-up showing recovery, persistence, trust, action, or exit.

## Next test

The immediate next empirical test is the [PSID material/time/care extract
specification](../projects/us-household-calendar-integration/psid-material-time-care-extract-spec-v1.md):
construct repeated family/person waves, verify the candidate fields and
universes, retain weights and attrition, and compare material-room change
with paid hours, care, household labor, perceived rushing, health, and family
routine. PSID access is still an account prerequisite, so no PSID estimate is
claimed here. Until that gate is cleared, the safe output is this bounded
cross-source finding and an explicit acquisition gap.

The full [price-pressure/time-transfer bridge](../projects/us-household-calendar-integration/price-pressure-time-social-participation-cross-source-bridge-v1.md)
is also available as a [published HTML reading page](../../site/price-pressure-time-social-participation-cross-source-bridge-v1.html).

## Reading rule

This page joins evidence with compatible questions, not identical samples.
Percentages, minutes, trip records, and transition pairs retain their own
units and denominators. A connection is a testable mechanism; it is not proof
that one source caused the outcome measured by another.

## Sources and reproducibility

- [ATUS 2024 data files](https://www.bls.gov/tus/data/datafiles-2024.htm)
- [ATUS 2023–2024 eldercare tables](https://www.bls.gov/tus/tables/a4-2023-2024.pdf)
- [Federal Reserve SHED 2024 report](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-income-and-expenses.htm)
- [NHTS 2022](https://nhts.ornl.gov/)
- [Census SIPP](https://www.census.gov/programs-surveys/sipp.html)
- [Machine-readable records and hashes](../records/us-atus-time-care-microdata-2024.json), [SHED care/work](../records/us-shed-care-work-adaptation-2024.json), [NHTS mobility](../records/us-nhts-mobility-material-work-care-2022.json), and [SIPP bridge](../records/us-sipp-childcare-work-hardship-bridge-2024.json)
