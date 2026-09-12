# Transport paper scan v1

**Checked:** 2026-09-12  
**Purpose:** turn a short reading pass into testable questions for the US household calendar.

This is a paper scan, not a list of headlines. The papers look at different levels. Some study a person’s choice, some study a whole city, and some study workers or firms. Those levels must not be blended into one claim.

## What the sources actually studied

| Source | Place and material | What it reports | Hard limit | Use in our project |
|---|---|---|---|---|
| [HBS: Customers’ routines](https://www.library.hbs.edu/working-knowledge/with-predictive-analytics-companies-can-tap-the-ultimate-opportunity-customers-routines) | About 2,000 New York rideshare users, with ride timing over 2018 | Repeated travel patterns helped sort users by how routine their rides were. Routine users were more valuable, stayed longer, and appeared more tolerant of price or service problems. | HBS is summarizing the paper, not giving us the raw user records. The result is about platform users, not all travelers. | Ask whether repeated need gives a platform more power over price, service, or access—and whether the rider has a real alternative. |
| [HBS: Carpool sign-up effort](https://www.library.hbs.edu/working-knowledge/want-people-to-commit-make-signing-up-a-little-harder) | 27,227 inactive Oregon carpool-platform users during a 2019 system change | A harder sign-up path cut enrollment by 25%, but people who completed it took about 1.6 times as many carpool trips per week. | Friction both blocks entry and filters for people who follow through. It does not mean friction is good for everyone. | Record where a transport service asks for time, forms, deposits, or repeated proof, and separate access from later use. |
| [NBER: Driving to Opportunity](https://www.nber.org/papers/w19922) | 2,071 US areas; wages, housing costs, and commuting costs | Housing and travel costs jointly change the value of a place. A higher wage does not tell the whole story if housing and the trip to work also cost more. | It is a model of a typical mobile household, not a dated record of actual household choices. | Treat commute time and transport cost as part of the price of living somewhere, then test who can move and who cannot. |
| [NBER: The Cost of Convenience](https://www.nber.org/papers/w26783) | US cities before and after ridehailing arrived | The study reports about a 3% rise in traffic fatalities and related increases in driving, fuel use, and delay after ridehailing entered. | This is a city-level study. It cannot identify every ride or prove that every change came from a ridehailing vehicle. The authors note that longer-run effects may differ. | Keep private convenience and public cost in the same frame: who saves time, and who bears danger, delay, or pollution? |
| [NBER: Launching with a Parachute](https://www.nber.org/papers/w27183) | 2,959 US cities, 2010–2016, around ridehailing rollout | The paper links ridehailing access with roughly 4–6% more new business registrations and a similar rise in small-business lending, with larger effects in less advantaged places. | A new business is not the same as a stable business or better household welfare. | Test whether flexible driving income is a bridge during a job shock, and whether it leaves the household with debt, wear, or unstable hours. |
| [NBER: Driving the Gig Economy](https://www.nber.org/papers/w32766) | US administrative tax records and Uber rollout | Rideshare expanded entry into taxi and limo work. It drew in younger and female workers, gave some displaced workers a fallback, and increased exits among lower-earning traditional drivers. | The study describes labor-market change; it does not by itself show whether workers became more secure. | Track why a person starts, what other work they had, hours and costs, and whether the fallback still works after several months. |
| [NBER: Disruptive Change in the Taxi Business](https://www.nber.org/papers/w22083) | UberX and traditional taxis in five cities | UberX vehicles spent more time or miles carrying passengers. The paper points to matching technology, flexible labor, scale, and older taxi rules as possible reasons. | It is an early comparison, before the market and rules changed further. Better vehicle use does not prove lower household cost. | Separate service capacity from the rider’s price, wait, safety, and ability to complain or switch. |
| [NBER: Generational Trends in Vehicle Ownership and Use](https://www.nber.org/papers/w25674) | US NHTS, Census, and ACS data | Tests whether differences often linked to Millennials remain after accounting for age, income, place, and wider conditions. | Generation labels can hide the effects of life stage, housing, work, and local transport. | Compare age with the actual constraint: vehicle access, commute, housing, income timing, and household composition. |

## The connected picture

### 1. Repeated need can become a source of control

The routines study points to a quiet shift. A platform does not need to know a person’s full life to learn that a trip is hard to avoid. Repeated timing can reveal work, care, or other fixed duties. That can improve matching, but it can also help a firm decide who is likely to tolerate a higher price or a bad service day.

The calendar should therefore record not only the fare. It should record whether the trip was optional, what alternative existed, how much notice the household had, and what happened when the service failed.

### 2. A barrier has two effects

The carpool study shows why a simple “more access” measure is not enough. A hard step can reduce the number of people who enter while making the remaining users more committed. We need two numbers: who was kept out, and what happened to those who got through.

This applies beyond transport. Deposits, identity checks, forms, wait lists, and customer-service steps can sort people before the final outcome is visible.

### 3. Transport is part of the price of a place

The local-rent study treats commuting as part of the cost of living, not as a separate inconvenience. This gives the household calendar a sharper question: did a cheaper home remain cheaper after the travel time, fuel, repairs, parking, and schedule risk were counted?

The answer will differ by who can move, who owns a car, who can work remotely, and who must arrive at a fixed time. A city average cannot answer that alone.

### 4. Convenience can move a burden elsewhere

Ridehailing may save a rider a wait or make work reachable. At the same time, a city may see more traffic, delay, fuel use, or danger. These are not competing stories. They can be true at the same time because the benefit and the cost land on different people.

Every transport finding should name both sides: the person who gained an option and the people or systems that carried the added cost.

### 5. One service can be both a consumer tool and a worker safety net

The business-formation and gig-work papers show that ridehailing is not only about getting from one place to another. It can also be a quick way to earn after job loss or during a weak labor market. That option may protect a household for a while, but the papers do not establish that it creates lasting security.

The calendar must follow the fallback over time: start date, prior work, hours, fuel and repair cost, debt, other work, and the point at which the option stops covering the need.

## The three levels we must keep apart

```text
household level:  trip, fare, wait, missed shift, substitute, recovery
city level:       traffic, safety, delay, fuel, public space
market level:     jobs, wages, entry, firm power, rules, investment
```

A city-level association cannot prove a household-level motive. A worker entering a platform cannot prove the household became safer. A more efficient vehicle cannot prove a lower fare. The synthesis is useful only when the level and unit stay visible.

## Next bounded test

Join the paper questions to the existing NHTS comparison and the calendar design:

1. Compare vehicle access, recent rideshare use, work-trip mode, and urban/rural setting.
2. Add time and spending categories from ATUS and CE as population reference points, without pretending they follow the same household.
3. In a future consent-based panel, record one dated transport disruption in full: need, alternatives, minutes, dollars, person with control, and next-month effect.
4. Test one counterexample: a household with the same transport shock that recovered without debt, missed work, or a weaker option.

The first useful finding should be modest: **transport dependence is not one condition. It can mean a fixed work or care duty, a lack of vehicle access, a platform that knows a repeated need, or a worker using the same platform as a fallback. Those forms create different kinds of risk.**

## Reading rule

When a source says transport “improves access,” ask: access for whom, to what, at what price, with what time cost, and with what alternative if the service fails?
