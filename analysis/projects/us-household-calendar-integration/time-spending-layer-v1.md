# Time and spending layer v1

**Checked:** 2026-09-12  
**Time source:** [BLS American Time Use Survey 2024 microdata](https://www.bls.gov/tus/data/datafiles-2024.htm)  
**Spending source:** [BLS Consumer Expenditure public-use microdata](https://www.bls.gov/cex/pumd_data.htm)

## Why these two sources belong together

The transport comparison showed that place changes the set of usable modes. The next question is whether the choice costs more than the posted fare. A household may pay with:

- money for a ride, fuel, parking, or repairs;
- time spent traveling, waiting, or arranging care;
- lost work or a shorter shift;
- unpaid help from another person;
- a worse product, missed appointment, or delayed task.

ATUS and CE measure different parts of that cost. They should be read together as two views of the mechanism, not joined as if they followed the same household.

## What ATUS can carry

The [2024 ATUS release](https://www.bls.gov/tus/data/datafiles-2024.htm) provides respondent, roster, activity, activity-summary, who, and eldercare files. The activity records contain the diary day’s activities, start and stop times, duration, and location. The respondent and roster layers provide work, earnings, and household-member context; the eldercare roster provides information about people receiving care.

For this project, ATUS can set population patterns for:

| Time cost | Useful ATUS view | What remains unknown |
|---|---|---|
| Travel | Minutes and activity type on a diary day | Fare, route failure, and the next month |
| Paid work | Work time and labor-force context | Whether a trip caused a missed shift |
| Child care | Care and household activity time | Whether care was purchased, refused, or covered by family that day |
| Eldercare | Care activity and eldercare roster | The helper’s later cash, health, or work loss |
| Household work | Time spent maintaining the household | Which bill, repair, or service failure created the work |

ATUS is therefore a **time-cost reference**. It is not an event diary for the same person over twelve months.

## What CE can carry

The [CE public-use data](https://www.bls.gov/cex/pumd_data.htm) comes in two separate survey files:

- **Interview:** larger or recurring purchases and bills, collected over repeated quarterly interviews;
- **Diary:** smaller, frequent purchases recorded for a short diary period.

CE can set spending patterns for rent, utilities, transport, food, repairs, fees, insurance, and other household categories. It also includes income and demographic context. The Interview and Diary surveys have different recall windows and should not be treated as interchangeable.

For this project, CE can answer:

1. Which transport and household-cost categories are large enough to matter?
2. How do those categories differ by income, tenure, household type, and other exposure groups?
3. Which recurring costs should the calendar ask for by date rather than as a monthly total?
4. Which small purchases or fees would disappear from a quarterly recall question and need an event diary?

CE cannot answer whether a named household paid a fare because its car failed, chose a longer route to protect a job, or borrowed from family after the purchase.

## The safe comparison

```text
ATUS: how much time does a type of household spend on travel, work, and care?
CE:   how much money does a type of consumer unit spend on transport and related needs?
panel: when did this household face the choice, what did it give up, and what happened next?
```

The first two lines can establish scale and categories. Only the third can carry the full chain from condition to choice to recovery.

## First bounded work

1. Use the ATUS 2024 activity and activity-summary files to build a weighted table of travel, paid work, child care, eldercare, and household-work time by broad respondent and labor groups.
2. Use the CE 2024 Interview and Diary files to build separate weighted tables for transport, fuel, parking, repairs, utilities, care, food, and fees.
3. Keep a source-specific time window and unit in every output.
4. Compare the category lists, not the individual records. Use the overlap to revise the household calendar fields.
5. Do not calculate a household “total cost of transport” by adding an ATUS time value to a CE spending value. The sources do not observe the same household or event.

## The fields the calendar must add

The public sources point to five missing fields that matter more than another broad survey question:

- **date:** when the trip, bill, repair, or care problem happened;
- **alternative:** what other mode, provider, route, or helper was actually available;
- **time price:** minutes, waiting, schedule loss, and unpaid care;
- **money price:** fare, fuel, parking, repair, fee, debt, or family transfer;
- **next effect:** missed work, delayed care, repeat cost, weaker choice, or recovery.

The calendar should ask these only after the household reports a material event. That keeps the form short and makes the record useful for the claims ledger.

## Limits

- ATUS is built around a selected diary day, so it cannot show a recurring transport problem from one record.
- CE’s Interview and Diary samples have different designs and recall periods.
- Neither source shows who had the power to fix the transport or spending problem.
- Neither source connects a cost to later trust, blame, voting, or policy action.
- Public source totals can establish a pattern; they cannot prove the household mechanism without a dated panel record.

