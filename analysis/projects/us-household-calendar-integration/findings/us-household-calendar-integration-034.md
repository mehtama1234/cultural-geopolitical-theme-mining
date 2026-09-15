# Energy cost is also equipment risk and assistance dependence

**Status:** provisional RECS household energy-vulnerability finding · **Checked:** 2026-09-15

## The bounded finding

The 2020 Residential Energy Consumption Survey shows that energy exposure is
not just an annual spending category. It can also appear as a much larger
affordability burden at the bottom of the income distribution, dependence on
energy assistance, disconnection-related help, and inability to repair or
replace equipment.

The evidence supports a layered interpretation:

> **A household can face a manageable annual energy bill on average while a
> broken furnace, air conditioner, or disconnection episode creates a sharper
> need for assistance. Energy security therefore includes the usable condition
> of equipment, cash room, and the route to help—not expenditure alone.**

This is a weighted cross-sectional household comparison. It does not follow a
bill, outage, health event, work schedule, or recovery for the same household.

## Income-band energy estimates

| Household income band | Mean annual energy expenditure | Bounded burden proxy | Unweighted n |
|---|---:|---:|---:|
| Under $15,000 | $1,439.58 (95% CI $1,405.92–$1,473.25) | 28.73% (27.24–30.22%) | 1,805 |
| $15,000–$35,000 | $1,575.14 (1,539.68–1,610.61) | 6.40% (6.25–6.56%) | 3,092 |
| $35,000–$75,000 | $1,767.32 (1,744.72–1,789.91) | 3.38% (3.33–3.43%) | 5,673 |
| $75,000 or more | $2,255.28 (2,228.08–2,282.48) | 1.74% (1.72–1.76%) | 7,926 |

The expenditure means rise with income, but the burden proxy falls sharply.
That is not paradoxical: the proxy divides expenditure by the midpoint of the
income band. For the open-ended lowest and highest bands, the midpoint
construction is especially important. It is an affordability screen, not an
observed household share of income and not a bill-payment rate.

The estimates use the final RECS analysis weight and 60 supplied jackknife
replicate weights. The record preserves the weighted denominators and
replicate-weight intervals; the sample counts above are unweighted responding
households.

## Assistance and equipment surfaces

| Energy-vulnerability surface | Estimate | Valid household sample |
|---|---:|---:|
| Ever received home-energy assistance | 5.30% (95% CI 4.89–5.71%) | 18,496 |
| Received home-energy assistance in 2020 | 66.20% (62.51–69.89%) | 854 |
| Received assistance after a disconnection notice | 26.26% (23.58–28.94%) | 1,629 |
| Could not use broken heating equipment because repair/replacement was unaffordable | 2.72% (2.42–3.02%) | 18,496 |
| Received help after heating equipment was unaffordable to repair | 18.34% (14.41–22.27%) | 658 |
| Air-conditioning equipment broke | 4.47% (4.12–4.82%) | 18,496 |
| Received help after air-conditioning repair was unaffordable | 8.33% (6.13–10.54%) | 845 |

These percentages do not share one denominator. The assistance and equipment
questions have their own valid universes, and “received help” is not the same
as restored equipment, safe temperature, avoided illness, or a paid bill. The
record retains the separate denominators rather than treating the figures as a
single energy-insecurity rate.

## The route under test

```text
income, housing, climate, equipment, and energy prices
  -> annual cost and immediate cash requirement
  -> payment, assistance, disconnection, repair, replacement, or reduced use
  -> temperature, health, care, work, food, and household-time consequences
  -> trust, public demand, provider response, or political meaning
```

RECS measures parts of the first two stages. It does not identify the month of
the bill, the rate or fuel price, the duration of an outage or unsafe
temperature, the person who provided help, the time spent seeking it, or the
later household outcome.

## What this adds to the atlas

### Energy spending is not the whole exposure

Annual modeled expenditure is useful for comparing household income bands, but
it can hide an acute repair or disconnection problem. A household may pay its
usual bills and still lack the cash to replace a failed furnace. Conversely,
equipment failure may be repaired quickly through family help, a landlord, a
utility program, or a credit purchase without appearing as a high annual
energy-expenditure household.

### Assistance is a route, not proof of protection

The assistance questions show that help reaches households facing several
different conditions. They do not show whether eligibility was easy to
establish, whether help arrived before the loss, or whether it covered the
actual need. A household can receive assistance and still carry equipment
risk, time costs, or health consequences.

### Equipment converts a money problem into a time and health problem

When a heating or cooling system fails, the adjustment may be a repair bill,
borrowing, waiting for a contractor, moving temporarily, relying on another
household, changing work or care arrangements, or tolerating unsafe
temperatures. RECS identifies the equipment and affordability surface, but not
which of these substitutions occurred.

## Counterexamples retained

- Higher-income households spend more dollars on energy on average, while the
  lower-income burden proxy is much higher; dollar spending and affordability
  are different measures.
- Assistance receipt is not evidence that the route was timely or adequate.
- A broken appliance is not automatically an outage, unsafe temperature, or
  health event.
- Not reporting unaffordable repair does not prove that repair was affordable;
  households may defer, borrow, relocate, or use another source of help.
- A 2020 cross-section cannot distinguish durable vulnerability from a one-time
  event or identify later recovery.

## Next test

The decisive follow-up is a dated household energy episode with bill amount,
rate or fuel, equipment condition, disconnection notice, assistance application
and decision, repair wait, alternative heat/cooling, paid and unpaid care,
health, work, food, and later recovery. Compare households with similar
exposure but different equipment quality, tenure, cash room, provider access,
and public-assistance routes.

Add a place-year layer for weather, utility shutoff rules, energy prices,
housing quality, and provider capacity. Only after the household episode is
identified should the program test trust, blame, political demand, or public
institutional response.

## Sources and reproduction

- [Machine-readable RECS record](../../../records/us-recs-energy-burden-income-assistance-2020.json)
- [RECS household energy-burden layer](../recs-energy-burden-household-layer-v1.md)
- [EIA 2020 RECS microdata](https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata)
- [Material, time, care, and political meaning program](../material-time-care-program-v1.md)

**Evidence status:** weighted 2020 household cross-section with jackknife
uncertainty and field-specific denominators; no causal energy-assistance,
health, work, political, or recovery claim is established.
