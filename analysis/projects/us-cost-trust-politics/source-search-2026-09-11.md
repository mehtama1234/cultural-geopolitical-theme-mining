# Source search: US cost of living, trust, and political response

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** short discovery pass; no settled finding

## Working question

Do changes in household money and choices affect how Americans judge the economy and public institutions, and how long does that effect last?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-FED-SHED-ECON-2025 | [Federal Reserve household report](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-executive-summary.htm) | Personal financial well-being was fairly stable overall, while views of the national economy remained much worse than before the pandemic; prices were the most common concern | Official household survey | Personal reports and national views are not the same measure; no voting cause is shown |
| US-FED-SHED-PRICE-ACTIONS-2025 | [Federal Reserve income and expenses](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-income-and-expenses.htm) | 77% of adults took at least one action after higher prices, including using cheaper products, using less, delaying purchases, reducing saving, borrowing, or working more | Official household survey | Multiple answers are allowed; actions do not show which price caused them |
| US-PEW-TRUST-2025 | [Pew: public trust in government](https://www.pewresearch.org/politics/2025/12/04/public-trust-in-government-1958-2025/) | Trust in the federal government was near a historic low in 2025 | Survey trend | A long trend cannot by itself identify the effect of current costs |
| US-PEW-ECON-2026 | [Pew: 2026 economic views](https://www.pewresearch.org/short-reads/2026/02/23/state-of-the-union-2026-where-americans-stand-on-key-issues-facing-the-nation/) | Americans named health care, housing, food, and consumer prices among top economic concerns; views differed strongly by party | Survey | Party identity may shape both views and reported concerns |
| US-NBER-CTC-SENTIMENT-35059 | [NBER: Child Tax Credit and consumer sentiment](https://www.nber.org/papers/w35059) | A working paper uses benefit loss and survey data to estimate changes in consumer sentiment after the expanded 2021 credit expired | Working paper with causal design | Review the paper, data, revision, and whether sentiment changes led to behavior |
| US-NBER-FED-TRUST-33524 | [NBER: central-bank communication and trust](https://www.nber.org/papers/w33524) | A survey experiment studies how political alignment affects views of the Federal Reserve and inflation expectations | Working paper; experiment | Fed trust is not the same as trust in government, firms, or parties |

## First pattern to test

```text
household cost or benefit change
  -> change in choices and financial room
  -> personal economic judgment
  -> national economic judgment and trust
  -> political demand or policy response
```

The first two links have survey evidence. The last two require a design that can separate money, party identity, media, and local conditions.

## Main gaps

- whether the same household changes both behavior and political view;
- whether effects last after the bill or benefit change ends;
- whether local prices and service failures matter more than national data;
- how firms and politicians assign blame;
- differences across income, race, age, disability, family type, and place;
- evidence showing that household costs do not change trust or political demand;
- whether people respond to actual costs or to expected future costs.

## Decision rule

Do one next pass with the NBER paper, its data or replication materials, and one household survey. If the link to behavior or politics cannot be separated from general party identity, record the topic as a perception pattern and move on.
