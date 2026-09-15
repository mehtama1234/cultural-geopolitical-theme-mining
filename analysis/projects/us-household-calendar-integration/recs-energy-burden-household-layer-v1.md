# RECS household energy-burden and assistance layer v1

The 2020 Residential Energy Consumption Survey adds a household-level
material layer to the atlas: modeled annual energy expenditure, income-band
affordability, energy assistance, and equipment-repair hardship are observed
in the same responding household.

| 2020 household income band | Mean modeled annual energy expenditure | Midpoint burden proxy |
|---|---:|---:|
| `<$15k` | $1,439.58 (95% CI $1,405.92–$1,473.25; n=1,805) | 28.73% (27.24–30.22%) |
| `$15k–$35k` | $1,575.14 (95% CI $1,539.68–$1,610.61; n=3,092) | 6.40% (6.25–6.56%) |
| `$35k–$75k` | $1,767.32 (95% CI $1,744.72–$1,789.91; n=5,673) | 3.38% (3.33–3.43%) |
| `$75k+` | $2,255.28 (95% CI $2,228.08–$2,282.48; n=7,926) | 1.74% (1.72–1.76%) |

The central finding is not that low-income households necessarily consume more
energy. Mean modeled expenditure is higher in the high-income bands, while the
affordability proxy is much higher at the bottom because RECS reports income
bands rather than continuous income. This is a descriptive material-pressure
gradient, not an observed bill-to-income ratio.

Additional vulnerability fields show that 5.30% of households had ever
received home energy assistance (95% CI 4.89–5.71%; n=18,496), while 2.72%
reported being unable to use broken heating equipment because repair or
replacement was unaffordable (2.42–3.02%). Among the field-specific valid
universes, 26.26% received energy assistance after a disconnection notice
(23.58–28.94%; n=1,629), and 18.34% received help after unaffordable heating
equipment repair (14.41–22.27%; n=658). These denominators are not
interchangeable: the latter measures are conditional on being asked the
relevant follow-up question.

Estimates use the final RECS analysis weight and 60 supplied Jackknife
replicate weights. EIA recommends caution for estimates with relative standard
error above 50% or fewer than 10 households; this layer retains sample counts
and replicate-weight intervals for later audit. Most questionnaire variables
are imputed where necessary, and the public file supplies imputation flags.

This layer supports the atlas arrow from household material conditions to
adaptation, public assistance, and unequal exposure. It does not establish
causality, monthly payment timing, energy insecurity as a full construct,
health effects, political response, or consumer behavior. The `$75k+` and
`<$15k` midpoint assumptions are especially consequential because both are
open-ended bands.

[Machine-readable record](../../records/us-recs-energy-burden-income-assistance-2020.json)  
Analysis script: `scripts/analyze_recs_energy_burden.py`

Sources: [2020 RECS microdata page](https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata),
[RECS public-use microdata guide](https://www.eia.gov/consumption/residential/data/2020/pdf/microdata-guide.pdf),
and [2020 RECS codebook](https://www.eia.gov/consumption/residential/data/2020/xls/RECS%202020%20Codebook%20for%20Public%20File%20-%20v7.xlsx).
