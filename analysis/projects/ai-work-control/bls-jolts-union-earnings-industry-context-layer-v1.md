# BLS JOLTS, union, and earnings industry context layer v1

This layer adds a third conditioning dimension to the [JOLTS/union bridge](bls-jolts-union-industry-context-layer-v1.md):
2025 average hourly earnings from the BLS Current Employment Statistics
program. It compares four named sectors using separate BLS aggregates:
establishment mobility, CPS formal membership, and CES average hourly pay.

The 2025 context is visibly non-uniform. The annual mean quits rate ranges
from 1.39% in manufacturing to 3.93% in leisure/hospitality. Average hourly
earnings range from $22.84 in leisure/hospitality to $44.26 in professional and
business services. CPS union membership ranges from 2.1% in professional and
business services to 8.2% in education and health services.

These contrasts are not a ranking of good or bad work. CES is an establishment
average, JOLTS is an establishment rate, and CPS is a household-survey worker
measure. They do not share a worker identifier, and the CPS 2025 annual
estimate excludes October. The bridge therefore identifies cells for a
worker/workplace event study:

```text
sector mobility + representation + pay context
  -> worker exposure and schedule/control event
  -> grievance, health, household room, and exit
```

