# US household calendar source search record v1

**Search date:** 2026-09-12  
**Question:** Which public US sources can help us test how dated changes in money, time, care, housing, transport, services, and public decisions affect the next month?

This is a source map, not a finding. The sources below should be used to build a joined picture of the problem, not treated as if they followed the same people.

## The short answer

The strongest public backbone is the Census Bureau’s [Survey of Income and Program Participation (SIPP)](https://www.census.gov/programs-surveys/sipp.html). It follows people for several years and records monthly changes in income, work, household structure, government programs, child care, health insurance, and food security.

It does not give us a full daily spending diary, a complete record of every bill and trip, or a clean measure of how a person interpreted a political event. Those gaps need other sources and, if we want the full chain, a small consent-based calendar panel of our own.

## Source roles

| Source | Best use | Time shape | Join level | What it cannot do alone |
|---|---|---|---|---|
| [SIPP](https://www.census.gov/programs-surveys/sipp.html) | Monthly income, work, household change, program use, child care, food security, wealth, and health insurance | Monthly; people are interviewed for several years | Person, family, household | It is not a daily bill, trip, service-contact, or political-behavior record |
| [BLS Consumer Expenditure Survey](https://www.bls.gov/cex/) | Rent, utilities, transport, food, repairs, fees, income, and household traits | Interview covers major or recurring items; diary covers two weeks of frequent purchases; annual estimates are published | Consumer unit and household address | It is not a twelve-month follow-up of the same household; recall and coverage differ between Interview and Diary surveys |
| [BLS American Time Use Survey](https://www.bls.gov/tus/) | Paid work, child care, elder care, travel, household work, rest, and social time | A time diary for one selected day | Person | It does not show the household’s full budget, repeated shocks, or who controlled the remedy |
| [BEA Personal Consumption Expenditures](https://www.bea.gov/data/consumer-spending/main) | National and state-level spending and price context | Monthly, quarterly, and annual national estimates; annual state estimates | National or state economy | It measures spending by or for people, not the choices of a named household; it is not the same scope as CPI |
| [Federal Reserve SHED](https://www.federalreserve.gov/publications/shed.htm) | Financial room, credit, savings, housing, care, hardship, work, and views of the economy | Mostly annual; some respondents can be linked across survey years | Adult respondent and household context | It is not a monthly event log; question wording and modules change across years |
| [MEPS Household Component](https://meps.ahrq.gov/survey_comp/household.jsp) | Health conditions, care use, charges, payments, insurance, income, and employment | Panel-based household survey with repeated collection | Person, event, condition, job, household | It is strongest for health costs, not the full chain of housing, transport, bills, and political judgment |
| [EIA RECS](https://www.eia.gov/consumption/residential/about.php) | Home type, energy equipment, energy use, energy cost, and energy insecurity | Periodic survey; supplier data support energy use and cost estimates | Housing unit and household characteristics | It is not a recurring panel; it cannot show whether the same household recovered the next month |
| [FHWA National Household Travel Survey](https://www.fhwa.dot.gov/policyinformation/nhts.cfm) | Trip purpose, mode, travel time, vehicle access, and daily travel | Periodic; the core diary covers one 24-hour period | Household, person, vehicle, and trip | It does not show monthly fare burden, rideshare dependence, missed work, or the outcome after a service failure |
| [USDA CPS Food Security Supplement](https://www.ers.usda.gov/data-products/food-security-in-the-united-states) | Food access, food spending, and food and nutrition assistance | Annual supplement; includes a 30-day and prior-year view | Household | It does not show the exact bill, payday, or tradeoff that preceded the food problem |
| [BLS Current Population Survey](https://www.bls.gov/cps/cps_over.htm) | Monthly employment, unemployment, hours, earnings, and labor-force status | Monthly; rotating household sample | Person and household | It does not follow every household for a full year in a single simple file, and it does not record bills, care, or remedies |

## What can be joined safely

1. **Use SIPP as the household-change spine.** Test whether monthly income, work, benefit, care, health-insurance, and food-security changes move together for the same people.
2. **Use CE to set spending categories and timing questions.** Its Interview and Diary designs tell us what people can report well, but their samples should not be joined to SIPP as if they were the same households.
3. **Use ATUS to price time.** A cheaper route or service is not truly cheaper if it takes more unpaid care, travel, or work time. ATUS can set population patterns; our calendar can record the household’s actual tradeoff.
4. **Use SHED to test financial room and public interpretation.** Its repeated respondent IDs can support some year-to-year analysis, but not a monthly chain from a bill to a later opinion.
5. **Use MEPS and RECS as specialist checks.** They can make health and energy parts of the calendar more precise without being mistaken for the main panel.
6. **Use NHTS for the transport baseline.** It can separate a necessary trip from an optional trip, and show how mode and travel time differ by place and household type. It cannot tell us what the trip cost the household later.
7. **Use CPS and CPS-FSS for labor and food checks.** They provide monthly labor context and annual food-security detail, but they do not replace a dated event record.
8. **Use BEA as the outside economic clock.** Compare household reports with national spending and price movement, while keeping the difference between a macro measure and an out-of-pocket household measure visible.

## The key boundary

The public sources mostly answer one of three different questions:

```text
What changed for many US households?
  SIPP, CE, ATUS, SHED, MEPS, RECS, BEA

What happened to this household month by month?
  A consent-based calendar panel

Who had the power to fix it, and what did the fix cost later?
  Calendar records plus notices, bills, service contacts, and permitted records
```

The last two lines are where the deeper work is. Public survey data can show that a pattern exists. It usually cannot show the exact warning, deadline, substitute, failed contact, family transfer, or next-month loss for the same household.

## Initial gaps to fill in the next source pass

- **Transport:** NHTS covers purpose, mode, time, and vehicle access, but the public gap remains fare, rideshare choice, missed work, and next-month recovery in the same household.
- **Bills and service failure:** find public utility, eviction, debt, and complaint records with dates and outcomes that can be compared by place.
- **Care and work:** separate paid care costs from unpaid care time, schedule control, and lost work in the same event.
- **Politics:** connect material pressure to blame, trust, policy knowledge, and action only where the source measures the steps in between.
- **Small firms:** add owner-household sources so business survival is not counted as household success without checking owner cash, time, and debt.

## Search log

| Date | Search focus | Sources screened | Decision |
|---|---|---|---|
| 2026-09-12 | Monthly household change and program participation | Census SIPP | Backbone candidate |
| 2026-09-12 | Spending, bills, transport, food, and repair categories | BLS CE Interview and Diary materials | Spending vocabulary and timing design; not a long panel |
| 2026-09-12 | Work, travel, child care, elder care, and unpaid time | BLS ATUS | Time-cost reference; not an event panel |
| 2026-09-12 | Macro spending and price context | BEA PCE materials | Context only; not household evidence |
| 2026-09-12 | Financial room, credit, hardship, care, housing, and views | Federal Reserve SHED | Annual perception and financial-room check |
| 2026-09-12 | Health cost and access events | AHRQ MEPS | Health-cost specialist layer |
| 2026-09-12 | Home energy, energy cost, and energy insecurity | EIA RECS | Energy specialist layer; periodic, not longitudinal |
| 2026-09-12 | Trip purpose, mode, travel time, and vehicle access | FHWA NHTS | Transport baseline; not a monthly cost-and-recovery panel |
| 2026-09-12 | Food access, food spending, and food assistance | USDA CPS-FSS | Annual outcome check; not a dated monthly event record |
| 2026-09-12 | Monthly work and labor-force change | BLS CPS | Labor context; rotating sample and limited household continuity |

## Working decision

Do not begin by downloading every file. First build a source-to-question matrix, then pull one test extract from SIPP, CE, ATUS, SHED, MEPS, RECS, and BEA. The first analysis should ask which links are truly observable in public data and which require our own calendar panel. That result should shape the field form before any broad collection effort.
