# NHTS transport comparison v1

**Run date:** 2026-09-12  
**Source:** [2022 NHTS CSV V2.1 archive](https://nhts.ornl.gov/downloads)  
**Documentation:** [2022 NHTS documentation](https://nhts.ornl.gov/documentation)  
**Analysis script:** [analyze_nhts_transport_comparison.py](../../../scripts/analyze_nhts_transport_comparison.py)

## The finding

Urban and rural households face different transport problems.

In the weighted 2022 NHTS data, **9.73% of urban households had no vehicle, compared with 2.82% of rural households**. Among people with a valid answer, **20.05% of urban respondents reported using rideshare in the prior 30 days, compared with 5.69% of rural respondents**.

That does not mean urban people are “dependent on rideshare.” It means rideshare appears more often in the urban transport layer, where car access is also less universal. The two facts belong in the same picture, but the dataset does not prove that rideshare is the reason a person can reach work, care, food, or medical care.

The rural pattern is different. Among weighted work trips, **pickups made up 22.92% of rural work trips, compared with 12.09% of urban work trips**. Urban work trips had higher shares for walking, public buses, subways, and rideshare in this comparison. A car-centered measure that treats every car-like mode as the same would miss this difference in how work access is built.

## What was measured

| Measure | Urban | Rural |
|---|---:|---:|
| Households with zero vehicles | 9.73% | 2.82% |
| People using rideshare in prior 30 days, among valid answers | 20.05% | 5.69% |
| Taxi or rideshare share of all recorded trips | 0.53% | 0.16% |
| Pickup share of work trips | 12.09% | 22.92% |
| Walk share of work trips | 3.06% | 0.41% |
| Public bus share of work trips | 1.64% | 0.03% |
| Subway share of work trips | 1.20% | 0.25% |
| Rideshare share of work trips | 0.86% | 0.10% |

The household and person figures use final household and person weights. Trip figures use the final travel-day weight. The comparison uses the full 2022 archive, with 7,893 household rows, 16,997 person rows, 31,074 trip rows, and 14,684 vehicle rows in the extracted files.

## The deeper connection

The visible story is “city people use rideshare more.” The more useful story is about the shape of the available choice:

```text
vehicle access differs by place
  -> the set of usable modes differs
  -> time, price, and failure risk are carried differently
  -> the same work or care trip can create a different household cost
```

NHTS measures the first two arrows well. It measures some of the time cost. It does not measure the household’s actual fare, whether a ride was the only workable option, whether a person missed work, or what happened to the budget afterward.

## Limits that matter

- The NHTS travel file records a travel day, not a twelve-month household calendar.
- “Used rideshare in the last 30 days” is a person-level report, not proof of regular dependence.
- Taxi and rideshare trip modes are rare in the recorded travel-day trips; small subgroup results need careful uncertainty checks.
- “Urban” and “rural” are broad categories. They hide differences among downtowns, suburbs, small towns, and remote areas.
- The figures are descriptive. They do not establish that geography caused rideshare use or that rideshare solved a transport problem.
- The comparison does not join to exact fares, pay dates, bill dates, missed work, safety, or recovery. Those remain panel-required fields.

## What this changes in the household calendar

The questionnaire should ask about each important trip:

1. Why was the trip needed?
2. Which modes were genuinely available that day?
3. What did each option cost in dollars and time?
4. Who could change the transport condition—the household, employer, provider, transit agency, or another person?
5. What happened when the preferred option failed?
6. Did the trip create debt, missed work, lost care, or a weaker choice the next month?

That is the missing bridge between transport exposure and household pressure.

## What would change the finding

The working picture would weaken if, after proper weighting and uncertainty checks, urban and rural households had similar vehicle access and rideshare exposure; if the differences disappeared after accounting for household composition and work status; or if households with limited vehicle access could consistently reach work, care, food, and health services without extra time, cost, or missed opportunities.
