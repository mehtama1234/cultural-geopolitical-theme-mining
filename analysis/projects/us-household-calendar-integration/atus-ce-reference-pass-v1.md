# ATUS and CE reference pass v1

**Checked:** 2026-09-12  
**Purpose:** set a public-data baseline for the time and money that surround transport.  
**Evidence type:** published BLS tables, not a same-household panel.

## The small set of numbers

| Source and measure | Published result | What it tells us | What it does not tell us |
|---|---:|---|---|
| [BLS Consumer Expenditure Survey, 2024](https://www.bls.gov/opub/reports/consumer-expenditures/2024/home.htm): average annual spending | $78,535 per consumer unit | The average unit spent 1.8% more in dollars than in 2023. | It is an average, not the cash room of a particular household. |
| CE, 2024: transportation share | 17.0% of spending | Transport is a large household commitment beside housing, food, health, and insurance. | The share does not show car dependence, payment timing, debt, or a missed trip. |
| CE, 2024: transportation spending change | +1.1% from 2023 | The category grew more slowly than in the two prior years. | A slower average increase does not mean every household paid less or regained room. |
| [BLS ATUS Table A-2A, 2024](https://www.bls.gov/tus/tables/a2-2024.pdf): travel related to work, weekdays | 0.31 hours per day across people 15+; 37.4% engaged; 0.84 hours among those engaged | Work travel takes real time, and the average across everyone hides the people who travel. | It does not give the fare, the route, the worker’s wage, or what happens when the trip fails. |
| ATUS 2024: travel related to care of household children | 19 minutes for women and 9 minutes for men among adults with a child under age 6, on an average day | Care travel is part of the work of keeping a household running, and it is not evenly carried. | This is a population average for a diary day, not a record of a family’s full care week. |
| ATUS 2024: primary childcare | 2.5 hours per day among adults living with a child under age 6 | Transport can sit inside a wider time burden of care. | It does not show whether paid care was available, whether a shift was missed, or who could fix the gap. |

## The finding this supports

Transport has two visible prices:

```text
money: fuel, vehicle, insurance, repairs, fares, parking
time:  travel, waiting, arranging care, and keeping a fixed schedule
```

The public data show that both matter. CE places transportation at 17.0% of average spending. ATUS shows work travel taking time on the days when people do it, and care travel adding to the unpaid work of families with young children.

The deeper point is not that every household has a 17% transport burden or the same travel time. It is that a transport choice can consume a large money category and a scarce time category at once. A cheaper option may still be unusable if it breaks a work or care schedule.

## Why we keep the sources separate

CE measures consumer-unit spending over its own survey periods. ATUS measures one selected diary day for people age 15 and over. Their units, timing, and sample designs differ. We can use them to set categories and population scale, but we must not add a CE dollar figure to an ATUS time figure and call that a household total.

The correct bridge is a future dated event record:

| Calendar question | Why it matters |
|---|---|
| What was the trip or care need? | Separates required movement from optional movement. |
| What did the usable choices cost in dollars? | Captures fare, fuel, parking, repair, fee, and debt. |
| What did they cost in time? | Captures travel, wait, arranging help, and schedule loss. |
| Who could change the condition? | Separates the payer from the employer, provider, landlord, agency, or family helper with control. |
| What happened next month? | Shows whether the cost ended or moved into debt, missed work, lost care, or a weaker option. |

## What would change the working picture

The working picture would weaken if household records showed that time and money rarely competed after a transport problem; if lower-price options were generally usable without extra delay or risk; or if a restored trip reliably restored the household’s later cash, work, care, and choice.

## Access check for the next extraction

The official [ATUS 2024 microdata page](https://www.bls.gov/tus/data/datafiles-2024.htm) lists the Respondent, Roster, Activity, and Activity Summary ZIP files and says they are available for user tabulations. A direct download attempt from this environment reached the BLS page but returned HTTP 403 for the Activity ZIP. No raw ATUS file was retained and no microdata result is being presented here.

That is a source-access problem, not evidence that the extraction is complete. The published table values above remain usable because they were checked against the official BLS tables. The microdata task stays open.

## Next bounded extraction

The next data step is to use the 2024 ATUS microdata to reproduce the published work-travel and care-travel measures by broad employment, sex, and household-child groups. The output should carry the activity definition, diary-day unit, weight, and suppression rule. CE should remain a separate spending table by transport subcategory and income or tenure group.

Sources: [ATUS 2024 microdata files](https://www.bls.gov/tus/data/datafiles-2024.htm), [ATUS 2024 results](https://www.bls.gov/news.release/archives/atus_06262025.htm), [CE 2024 report](https://www.bls.gov/opub/reports/consumer-expenditures/2024/home.htm).
