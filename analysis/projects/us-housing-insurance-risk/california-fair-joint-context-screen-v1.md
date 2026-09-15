# California FAIR/private-market joint context screen v1

The California insurance lane now combines four linked place dimensions:
FAIR residential-structure share, voluntary-market nonrenewal decisions, ACS
income and detached-housing context, and CDI modeled county wildfire exposure.
The strictest screen retains 1,570 ZIP rows with all four dimensions.

The low-income/high-risk cell has a 12.72% voluntary nonrenewal rate among
renewed plus nonrenewed decisions, compared with 10.13% in the high-income/
low-risk cell under that definition. A subsequent [sensitivity layer](california-fair-joint-sensitivity-layer-v1.md)
shows that the ordering changes under other income and risk cut points, so
this is not a stable risk gradient.

```text
material risk + place resources + market backstop
  -> uneven observed nonrenewal pattern
  -> possible unequal ability to absorb cost or find coverage (open)
  -> repairs, staying, selling, lending, and political response (open)
```

This is a transparent stratified screen, not a regression or causal adjustment.
The CDI risk measure uses a 2015 dwelling-unit base, the market decisions are
from 2022, ACS measures are five-year ZCTA estimates, and FAIR structures and
voluntary policy decisions have different universes. ZIP-to-ZCTA and
ZIP-to-county approximations hide within-place variation. The low-income/high-
risk cell also has far fewer ZIP rows than the high-income/low-risk cell, so
the result should not be treated as a population-weighted effect.

## Next test

Add a documented multivariable or matched-place sensitivity analysis, including
detached/mobile structure composition and county fixed context where justified,
then seek compatible premiums, claims, repairs, and household/property outcomes.
