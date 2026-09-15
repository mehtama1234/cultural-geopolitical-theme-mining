# Price pressure, time transfer, and social participation cross-source bridge v1

**Checked:** 2026-09-14
**Scope:** US consumer adaptation, paid/unpaid work, care, and social/civic availability  
**Status:** compared population layers; not a same-person price-to-time causal estimate

## The broader question

When money becomes tight, what is paid with time? People may substitute goods,
use less, delay purchases, borrow, work more, provide unpaid care, travel farther,
wait, or seek help. The societal issue is not only whether consumption changes,
but whose time absorbs the adjustment and what participation is displaced.

```text
price, bill, care need, or financial constraint
  -> spending substitution, reduced use, delay, borrowing, or extra work
  -> paid work, unpaid care, travel, paperwork, and household labor change
  -> rest, social connection, civic availability, health, and bargaining room change
  -> firms, families, agencies, and communities redistribute the burden
```

The project measures different arrows with different population sources. It does
not assume that a reported price adaptation and a time-use estimate describe the
same person.

## Source comparison

| Layer | Unit/time | What it contributes | Boundary |
|---|---|---|---|
| [SHED 2025 price adaptation](../us-household-financial-pressure/shed-2025-price-adaptation-layer-v1.md) | US adult; 2025 | 62.2% switched to cheaper products, 59.7% used less/stopped, 45.6% delayed a major purchase, and 17.0% worked more or got another job | Does not identify the hours added, need displaced, or later social/civic outcome |
| [SHED panel income × condition path](../us-household-financial-pressure/shed-panel-income-condition-path-layer-v1.md) | Recontacted respondent; 2024–2025 | Adaptation persistence and re-entry vary by income band and worsening, stable, or improving financial path | No diary, exact price/bill, employer, care event, or political-action follow-up |
| [ATUS 2024 time layer](atus-2024-time-hidden-price-layer-v1.md) | Person diary day; 2024 | 87% of full-time workers worked on an average weekday; 29% worked on an average weekend day; multiple-job holders had 50% weekend work; socializing/communication occurred for 30% on an average day | Does not identify which price, bill, or policy produced the allocation |
| [Time, work, care, and social participation](time-work-care-social-participation-layer-v1.md) | Person diary and subgroup; 2024 | Household labor, primary/secondary childcare, work location, and socializing are distinct time outcomes | One-day diary is not a household-month budget or longitudinal event record |
| [Care cost/work/family security](../us-health-cost-household-choice/care-cost-work-family-security-layer-v1.md) | Person, caregiver, household, health event | Care costs can move into unpaid family time, work loss, food/housing tradeoffs, and job dependence | Does not join a particular price adaptation to the same caregiver's time |
| [CPS participation-friction layer](../us-cost-trust-politics/cps-2024-turnout-participation-friction-layer-v1.md) | Adult respondent; 2024 election | Schedule, health, transport, registration, interest, and candidate-related nonvoting reasons are separately observable | Does not show which earlier financial or care event created the barrier |
| [SIPP race × tenure × resources](sipp-fay-brr-race-tenure-resource-layer-v1.md) | Person-month record; 2025 current-vintage extract | Utility difficulty, hunger, food security, and one-job status inside race/tenure/resource cells with Fay–BRR uncertainty | Person-weighted rather than household-weighted; no dated bill, move, care event, or downstream meaning |
| [SIPP work-limitation × resources](sipp-fay-brr-race-disability-resource-layer-v1.md) | Person-month record; 2025 current-vintage extract | Work-limiting condition, resource band, hardship, food security, and one-job status across displayed race groups | Work limitation is not a diagnosis or accommodation measure; current-vintage refresh is not identical to the earlier extract |

## What the comparison supports

### 1. Money and time are substitutable but not equivalent

SHED shows that some people respond to price pressure through additional work,
while ATUS shows how work, household production, childcare, and socializing are
distributed in the population. Together they establish a measurement need:
financial adjustment can be a time adjustment, but the sources do not estimate
the size of that conversion for the same people.

### 2. Time transfer can be hidden inside “successful” adaptation

Buying cheaper goods or keeping a bill current may preserve immediate
consumption while requiring more shifts, unpaid family care, longer travel, or
more administrative effort. A household that avoids borrowing may still lose
rest, social contact, health, or civic availability. A stable job count is not
proof that time and control were preserved.

### 3. Resource room is conditional on housing and work position

The refreshed SIPP intersection layers make the subgroup boundary more
concrete. In the displayed White-alone and Black-alone cells, renter/owner
differences in utility difficulty and food-security measures appear at both
low and high resource endpoints, although the Black-alone ordering is not
uniform and some hunger cells are imprecise. In the separate
work-limitation-by-resource layer, people reporting a work-limiting condition
show more utility difficulty, lower high/marginal food security, and fewer
one-job records within the displayed race groups.

These are not proof that race, tenure, or disability caused hardship. They show
why a single income gradient or universal “time poverty” score can hide the
different alternatives available inside the same broad resource band. The
current records still do not observe the time or care substitution that follows
those positions.

### 4. Control matters as much as hours

ATUS shows differences in weekend work and working from home by job and
education group. The relevant inequality is not simply who works more; it is
who can choose when and where work occurs, combine work with care, refuse an
extra shift, or recover time after a shock. Schedule control is a resource that
can mediate the same financial pressure.

### 5. Social participation is an outcome, not leftover leisure

ATUS reports socializing or communicating on 30% of average days in 2024,
compared with 38% in 2014. CPS separately records nonvoting barriers, including
time and health. Neither should be called cultural decline or political apathy
without identifying what displaced the time and whether people wanted or could
recover it.

### 6. The burden can move between households and institutions

Unpaid family care, outside financial help, employer schedule changes, and
public-program paperwork redistribute the adjustment. One person's avoided
missed bill may be another person's lost work or care time. This connects
consumer culture, social reproduction, public administration, firms, and
political availability without reducing them to household spending.

## Arrow ledger

| Arrow | Status | Safe current conclusion | Missing test |
|---|---|---|---|
| Financial pressure → consumer adaptation | Reported / Compared | Substitution, reduced use, delay, borrowing, saving cuts, and extra work are distinct responses | Dated price/bill and exact need for the same respondent |
| Adaptation → paid or unpaid time | Open | Extra work and care are plausible time channels | Same-person time diary or panel before and after the event |
| Time allocation → schedule control and security | Compared / Open | Work location, weekend work, care, and household labor differ across groups | Employer rule, pay, care alternative, and time-control measure |
| Time displacement → social/civic participation | Open | ATUS and CPS measure time and participation barriers separately | Same respondent with desired time, displacement, civic action, and recovery |
| Time transfer → family/institutional burden | Open | SHED help, care, and public-system layers identify redistribution channels | Follow both receiver/helper or applicant/agency around one episode |
| Material/time experience → cultural or political meaning | Open | Trust, fairness, belonging, and action require direct measurement | Attribution, identity, source, trust, and action after a defined event |

## Bounded event design

Select one essential expense or need—food, transport, energy, health care, or
housing—and follow a person/household through a defined pressure episode. Record:

1. price, bill, income, job, care need, and date;
2. purchase substitution, reduced use, delay, borrowing, saving change, or
   extra work;
3. travel, waiting, paperwork, paid care, unpaid care, and schedule control;
4. sleep, rest, health, family time, socializing, civic participation, and
   desired-versus-actual time;
5. employer, firm, family, agency, or community response;
6. remedy, recovery, later financial room, trust, attribution, and action.

Compare people with similar exposure but different schedule control, transport,
care alternatives, family help, and practical exit. Include a counterexample
where a similar cost was absorbed without added work, reduced social time, or
unpaid-care transfer. Keep time spent, time desired, time controlled, and time
displaced as separate measures.

## What this changes in the broad program

The societal trend is not simply that prices are high or people are working
more. It is that financial pressure can reorganize the time architecture of
ordinary life: who works extra, who provides unpaid care, who waits or travels,
who loses social availability, and who still has the power to refuse or recover.
Whether that becomes isolation, solidarity, distrust, organizing, or political
action remains an empirical question.
