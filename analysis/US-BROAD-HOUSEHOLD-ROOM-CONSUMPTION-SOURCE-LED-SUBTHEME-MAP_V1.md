# Household room and consumption: source-led subtheme map v1

**Checked:** 2026-09-24  
**Scope:** 461 registry records carry the `household_room_consumption` label.
This map treats “room” as the capacity to meet needs and absorb a shock, not as
income, a balance, receipt of a benefit, or a single consumption item.

## What the source material supports

The corpus repeatedly separates:

> price adaptation from adequate consumption; financial confidence from an
> actual bill or care episode; benefit receipt from recovery; credit use from
> repayment; and service restoration from a durable buffer.

## 1. Price adaptation shows tradeoffs, not which need was ultimately protected

The [SHED food-pressure record](records/us-shed-food-pressure-adaptation-2024-2025.json)
reports 8% prior-month food insufficiency in 2025, 58% saying higher prices
worsened their financial situation, and 16% not paying all bills in full.
Food insufficiency was 21% for the under-$25,000 family-income group and 1%
for the $100,000+ group. In 2024, respondents reported switching to cheaper
products (63%), using less/stopping products (61%), delaying major purchases
(46%), reducing savings (43%), borrowing more (16%), and working more (18%).
Those are overlapping and non-sequential answers.

**Supported subtheme:** households can preserve one need by changing quality,
quantity, timing, saving, borrowing, or work elsewhere.  
**Not established:** a household-level order of sacrifice, food-price causation,
benefit adequacy, health effect, or recovery.

## 1a. A better reported financial condition does not automatically end prior price adaptations

The [paired SHED adaptation/financial-condition record](records/us-shed-panel-adaptation-condition-path-2024-2025.json)
follows 4,419 recontacted respondents from 2024 to 2025 and asks whether people
who had already adapted continued doing so. Among prior adopters whose reported
financial condition worsened, 86.9% still bought cheaper products, 84.8% still
used less or stopped products, 75.2% still delayed a major purchase, 71.0%
still reduced savings, and 65.1% still increased borrowing. Among those whose
condition improved, the corresponding persistence shares were still 68.8%,
66.1%, 56.6%, 55.0%, and 45.0%. Each measure has its own valid-pair denominator;
the retained panel comparison has no replicate-weight standard errors.

**Supported subtheme:** reported financial improvement and reversal of an
earlier consumption, saving, borrowing, or purchase-timing adaptation are
separate stages. A household can report a better broad condition while still
operating with a constrained consumption or balance-sheet strategy.  
**Not established:** that the condition change caused persistence; an objective
income, price, debt, health, care, or housing trajectory; whether the
adaptation was harmful or chosen; material adequacy; repayment; or durable
recovery. These are persistence estimates among people who had already adopted
each behavior, not population prevalence.

## 1b. The same inflation information can update beliefs without producing the same purchase response

The [inflation-information/homeownership record](records/us-nber-inflation-information-homeownership-spending-2026.json)
uses randomized inflation-information treatments with U.S. households. Renters
showed the stronger reported revision in inflation expectations but no detected
durable-purchase adjustment; homeowners showed a more modest expectation
revision and a significant increase in durable spending. The paper interprets
the contrast through attention and available adjustment margins, including
renters' greater likelihood of liquidity constraint. The public abstract does
not disclose the full analytic denominator or all treatment details.

**Supported subtheme:** price information, belief revision, and purchase
capacity are distinct links. A tenure-linked balance-sheet position can shape
whether a person acts on the same information rather than whether they receive
or understand it.
**Not established:** total consumption, actual inflation exposure, welfare,
the precise role of liquidity, any political attribution or trust effect, or a
general rule for every renter, homeowner, wealth level, debt position, and
housing market. Homeownership is not a complete measure of resources.

## 2. Financial room, debt, and care access are related but not a single event

The [MEPS financial-room/care record](records/us-meps-2024-financial-room-care-delay-2024.json)
finds 14.15% cost-related medical-care delay among people not confident they
could pay an unexpected expense versus 5.36% among confident people; the
corresponding comparison is 16.98% versus 4.57% for any versus no medical
debt. These are same-round associations and cannot say whether the bill,
illness, debt, denial, or delay came first.

**Supported subtheme:** room for an unexpected expense and medical debt are
important contexts for care access, but neither is a claim-level pathway.  
**Not established:** causal debt effects, care completion, appeal, remediation,
or health recovery.

## 3. A buffer and credit route can protect the immediate moment while shifting risk forward

The [financial-buffer record](records/us-federal-reserve-financial-buffer-credit-exposure-2025.json)
reports that 63% of adults would cover a $400 expense with cash/equivalent,
while 15% would put it on a card and carry a balance and 10% would borrow from
friends/family. Among consented credit-matched respondents, balances rose
$2,530 (37%) from 2023–2025 for those finding it difficult to get by, versus
$59 (1%) for those living comfortably. The comparison is descriptive; a
balance does not reveal charge purpose, rate, repayment, or distress.

**Supported subtheme:** liquidity, family support, revolving credit, and
retirement drawdown are distinct ways to bridge a gap with different remaining
exposure.  
**Not established:** delinquency, lender treatment, future consumption, or
whether using credit improved or worsened a particular household's outcome.

## 3a. Informal expense help is a distributed buffer, not a measured recovery route

The [income-volatility and support record](records/us-federal-reserve-income-volatility-support-2025.json)
finds 23% of adults received outside-household help with a listed expense in
2025. The reported share was 47% among adults ages 18–29, 26% among ages
30–44, and 13% among adults 45 and older; among the youngest group, help with
phone, general, housing, car, medical, and education expenses were distinct,
overlapping routes. Thirty percent of adults also reported income varying at
least occasionally and 11% said variability made bills difficult. The repeated
survey does not link a dated income change to help, transfer amount, provider,
reciprocity, or later security.

**Supported subtheme:** outside help is an uneven household-buffer surface
alongside income timing, public assistance, savings, credit, and price
adaptation. Receiving help is neither evidence of sufficiency nor evidence of
dependency; it cannot be assumed to replace formal care, benefits, or income.

**Not established:** whether help prevented hardship, who supplied it, its
value or timing, obligations created, effect on care/work choices, or durable
recovery.

## 3b. Payment rewards can shift a shared price burden without appearing on a household bill

The [payment-rewards redistribution record](records/us-nber-payment-rewards-redistribution-2026.json)
combines merchant settlement and transaction data with a sufficient-statistics
incidence model. It estimates a $30 billion annual transfer from cash/debit
users to credit-card users through common merchant prices and rewards; the
model estimates $9.2 billion flows toward households earning above $150,000
and a 26% higher effective sales-tax-equivalent burden for cash users than for
premium-card users. Merchant data cover large payment-platform surfaces, not a
national household panel, and the dollar incidence depends on pass-through,
matching, merchant sorting, and payment-choice assumptions.

**Supported subtheme:** consumer financial room can be shaped by a payment
system's common-price and reward design, not only by visible fees, balances,
or a household's own transaction. The distributional mechanism runs through
merchant cost and pricing as well as through a cardholder's reward receipt.

**Not established:** an observed household bill, a welfare or financial-stress
effect for a named cash/debit user, uniform merchant pass-through, credit
access, or political response. These are modeled incidence estimates, not
directly observed individual transfers.

## 3c. A business revenue shock can pass only partly into the owner's measured consumption while the firm remains exposed

The [owner-business revenue/consumption record](records/us-owner-business-revenue-consumption-covid-2020.json)
uses linked U.S. small-business and owner-household financial accounts during
the first two months after the March 2020 National Emergency. Business revenue
fell 40%, while estimated owner-consumption pass-through was only $0.016 per
dollar of business-revenue loss. The muted pass-through persisted through 2021,
including after vaccines. The authors identify federal subsidies and pandemic
limits on spending opportunities as possible reasons; the retained official
abstract does not provide exact panel counts, account-selection rules, or full
specification details.

**Supported subtheme:** an owner household and its firm can share a balance
sheet without converting every revenue loss directly into observed household
consumption. Revenue, owner consumption, public subsidy, cash buffer, firm
survival, and worker security are separate stages.
**Not established:** that an owner had adequate resources, that consumption
stability reflects wealth rather than timing or unavailable purchases, firm
survival, repayment, worker outcome, customer access, or generalization beyond
the COVID-era mix of shock, subsidies, and restricted consumption opportunity.

## 4. Public assistance can mark acute need without completing a material recovery sequence

The [SNAP-transition record](records/us-sipp-safety-net-transition-work-room-2024.json)
finds that 61.78% of selected no-to-yes SNAP transitions were followed by a
resource-ratio decline, while 16.4% and 20.8% were followed by rent/mortgage
and utility hardship respectively. The selected monthly transition screens are
descriptive; SNAP entry can be a response to a worsening condition.

**Supported subtheme:** receipt is a route into support, not evidence by itself
of pre-existing room, benefit adequacy, work recovery, or reduced hardship.  
**Not established:** the benefit's causal effect, timing of application,
amount, administrative burden, or durable outcome.

## 5. Energy insecurity puts food, medicine, temperature, and service on the same budget surface

The [energy-consequence record](records/us-energy-household-consequence-public-restoration-2024-2026.json)
preserves EIA's 2024 counts: 43.56 million homes with any energy insecurity,
32.89 million reporting a food-or-medicine tradeoff, 17.55 million unhealthy
indoor temperature, and 16.19 million a disconnect/delivery-stop notice.
LIHEAP separately reports nearly 6 million people/families helped and 279,000
restoration instances in FY2024. Conditions, reach, and restoration do not
share a denominator or establish repeated-crisis prevention.

The [Clean Energy Connector record](records/us-doe-clean-energy-connector-low-income-bill-credit-2024-2026.json)
adds a prospective low-income bill-credit route across six pilot jurisdictions:
LIHEAP recipients can be identified, opt in, and be enrolled by subscription
managers in community solar; the program requires at least a 20% difference
between household financial benefit and participation cost. The public program
page does not report eligible households, completed enrollment, credits posted,
fees, payment timing, persistence, energy burden, or an exit outcome.

**Supported subtheme:** energy burden is a material-allocation problem across
essential needs; public reach, reconnection, and a bill-credit enrollment route
are necessary but separate endpoints.  
**Not established:** a price effect, take-up rate, service duration, next bill,
health result, net household saving, or durable recovery.

## 5a. Similar annual energy spending can consume radically different income room across household bands

The [RECS energy-burden and assistance record](records/us-recs-energy-burden-income-assistance-2020.json)
adds a 2020 household distribution layer using EIA's replicate-weighted
Residential Energy Consumption Survey. Mean total energy expenditure was about
$1,440 in the under-$15,000 income band and about $2,255 in the $75,000-plus
band. Using each income band's midpoint only as a bounded affordability proxy,
those estimates correspond to 28.73% and 1.74% respectively. The open-ended
lowest and highest bands mean this is not a literal household energy-burden
rate.

The same survey records distinct support and equipment fields: 5.3% reported
ever receiving home-energy assistance, and 2.72% reported being unable to use
broken heating equipment because repair or replacement was unaffordable. Those
are self-reported conditions and experiences, not a utility bill timeline or a
measure of successful service restoration.

**Supported subtheme:** energy expenditure, relative income room, assistance
contact, and affordable-equipment repair are different household-energy stages.
Higher dollar spending does not imply higher burden, and assistance receipt
does not identify an adequate or durable energy route.

**Not established:** an actual household's income denominator, bill timing,
shutoff or restoration, energy use, health, food/medicine tradeoff, assistance
amount, causal benefit, or later recovery. The midpoint proxy and 2020 survey
context should not be carried forward as a current energy-insecurity rate.

## 6. Automatic saving can expand both assets and short-term revolving debt

The [Oregon Auto-IRA balance-sheet record](records/us-nber-auto-ira-household-balance-sheets-2026.json)
summarizes an SIPP quasi-experimental comparison of workers likely exposed to
OregonSaves with similar workers in states not yet adopting an Auto-IRA.
Exposure was associated with a 2.7-percentage-point increase in IRA ownership
(to 12.7%) and more than $8,500 in reported IRA balances; checking/savings
ownership and balances also rose. But credit-card debt incidence rose 2
percentage points and balances by $90. The public summary does not supply the
underlying sample, contribution, withdrawal, take-home-pay, interest, or
repayment detail.

**Supported subtheme:** a policy can improve longer-run asset ownership and
liquid-account holding while introducing or coinciding with a nearer-term debt
margin; balance-sheet movement is not one security score.  
**Not established:** a net welfare effect, debt harm, retirement adequacy,
consumption effect, or who bears the tradeoff.

## 6a. Retirement-account policy can change work and claiming timing without proving later-life security

The [Auto-IRA retirement-timing record](records/us-georgetown-auto-ira-retirement-claiming-2026.json)
uses SIPP 2014–2024 person-wave data for workers ages 55–75 and a staggered
difference-in-differences comparison of seven early-adopter states with
non-adopter states. It estimates a 1.2-percentage-point reduction in retirement
before age 65 from a 7.1% pre-policy mean, a 3.0-point increase in working past
age 67 from a 22.8% mean, and increases in IRA (3.8 points) and 401(k)
ownership (2.3 points). It separately estimates a 1.0-point reduction in early
Social Security claiming and a 1.8-point increase in claiming at age 70. The
retirement-asset estimate was not statistically significant.

**Supported subtheme:** auto-enrollment policy exposure → retirement-account
ownership → work and Social-Security-claiming timing. Account ownership,
staying in work, delayed claiming, benefit amount, and lived retirement
security are separate stages; a later exit may reflect added choice or a need
to keep working.
**Not established:** account type or balance for each person, a net-welfare or
lifetime-income gain, retirement adequacy, debt/liquidity tradeoffs, health,
job quality, care obligations, ability to refuse unwanted work, or the causal
mechanism. State policy, pandemic overlap, incomplete maturation, and other
state labor-market conditions remain relevant qualifications.

## 7. Keeping a housing asset can build wealth without restoring consumption

The [mortgage-modification record](records/us-nber-homeownership-loss-wealth-consumption-great-recession-2025.json)
follows seriously delinquent Great Recession homeowners who were nearly
identical in pre-trends but differed in modification receipt. Modified
homeowners were 36 percentage points more likely to retain their homes, with
more than half of that retention gap persisting almost a decade. The record
reports about $70,000 more housing wealth, but no higher consumption, in part
because tighter credit constraints limited borrowing against equity.

**Supported subtheme:** the conversion of retained housing into measured wealth
and the conversion of wealth into current spending are separate links.  
**Not established:** that modifications remove housing insecurity, that current
consumption exhausts the value of housing, or that results generalize beyond
this distress and modification setting.

## 8. Low liquidity does not create one universal spending response

The [low-liquidity consumption-wedges record](records/us-nber-consumption-wedges-low-liquidity-2026.json)
uses linked transaction and expectations data for middle-income, low-liquid-
wealth consumers. Its modeled median absolute gap between observed and
frictionless consumption was 40%; 49% of consumers were below the benchmark
and 51% above it. The authors find borrowing constraints alone cannot account
for both directions, while present bias plus constraints or consumption-
adjustment costs better fit the pattern. A frictionless benchmark is a model,
not a bill or direct welfare measure.

**Supported subtheme:** the same low-liquidity label can conceal constrained
under-consumption and elevated spending driven by different frictions; totals
alone do not identify a household's need or security.  
**Not established:** why a specific purchase occurred, whether it was
avoidable, or its later debt, care, housing, work, or welfare consequence.

## 9. Transfer form and recurrence change the first observed spending route

The [transfer-design record](records/us-nber-transfer-design-household-spending-2026.json)
links pandemic-era benefit changes to high-frequency scanner data for
low-income families with children. Short-run food-store marginal propensity to
consume was 0.18 for one-time in-kind benefits and 0.38 for recurring in-kind
benefits, compared with 0.06 and 0.20 for one-time and recurring cash. The
authors interpret the pattern as consistent with labeling, mental accounting,
and forward-looking responses; food-store purchases are not total household
consumption.

**Supported subtheme:** benefit amount is not the whole intervention: label and
schedule shape the first spending channel observed in the data.  
**Not established:** that in-kind aid is superior to cash, that a lower
food-store response means cash was less useful, or that either design created
lasting food security or household room.

## 9a. A temporary payment can become a durable purchase and a future loan obligation

The [stimulus-to-vehicle-financing record](records/us-nber-transitory-income-durable-purchases-vehicle-financing-2008.json)
uses variation from the 2008 Economic Stimulus Act. Within three months,
households spent about 80% of the payment on durable goods; most of the durable
response was motor vehicles and about 20% was smaller items. The study reports
that the average household borrowed about 40 cents per stimulus dollar to
purchase motor vehicles, which were often financed, used, or both. The public
extraction does not disclose the full analytic expenditure or financing
denominator.

**Supported subtheme:** a cash transfer can be converted into a durable
consumer good through a financing route. Payment receipt, purchase, vehicle
mobility, loan leverage, recurring ownership cost, and later household room
are distinct stages, so a high initial spending response does not identify the
meaning of the purchase.
**Not established:** purchase need, loan terms, payment burden, delinquency,
insurance/fuel/repair cost, resale, work or care access, welfare, or later
security. The 2008 policy and vehicle market are a specific context, not a
universal response to temporary income or current credit conditions.

## 10. Work location can redistribute shopping time, responsibility, price, and product choice inside a household

The [remote-work shopping record](records/us-nber-remote-work-shopping-consumption-2026.json)
combines a survey with Nielsen consumer-panel and marketing data. It reports
that working from home increased online shopping, weekday store-trip share,
total spending through quantity and range, and prices paid, while lowering
deal use and price elasticity. The estimated grocery-price increase was about
1%. Remote workers made more shopping trips but spent fewer minutes shopping;
among married households, the price increase was concentrated where shopping
responsibility shifted, especially when the new remote worker was male.

**Supported subtheme:** a change in work location can alter a household's
consumer process—who plans and shops, when trips occur, the basket selected,
time spent, deals used, and prices paid—rather than simply reducing commuting.
Time savings and a higher cash price can coexist.  
**Not established:** full household welfare, unpaid planning/return labor,
delivery and accessibility effects, local-store survival, neighborhood change,
long-run work arrangement, or effects for people unable to work remotely.
Higher spending and prices can reflect valued convenience, product choice, or
household needs rather than a net loss.

## Cross-subtheme finding and next test

```text
price, income, bill, debt, service disruption, care need, asset, or transfer
  -> substitution, delay, borrowing, saving, benefit application, or assistance route
  -> consumption protected, reduced, deferred, financed, or redirected
  -> next bill, credit, work, care, food, housing, and energy condition
  -> remaining buffer, security, and later judgment
```

The missing decisive unit is a dated household ledger connecting the first
shock to all adaptations, benefit/credit route, payment or service outcome,
and next-period buffer. Cross-sectional hardship and aggregate program reach
cannot substitute for that sequence.

## Related atlas surfaces

- [source-led maps index](US-BROAD-SOURCE-LED-MAPS-INDEX_V1.md)
- [care source-led map](US-BROAD-CARE-SOURCE-LED-SUBTHEME-MAP_V1.md)
- [consumer source-led map](US-BROAD-CONSUMER-SOURCE-LED-SUBTHEME-MAP_V1.md)
- [public-systems source-led map](US-BROAD-PUBLIC-SYSTEMS-SOURCE-LED-SUBTHEME-MAP_V1.md)
