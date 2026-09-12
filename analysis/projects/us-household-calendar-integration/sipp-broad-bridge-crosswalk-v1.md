# SIPP broad-bridge crosswalk v1

**Checked:** 2026-09-12  
**Source:** [2025 SIPP public-use data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html), [official schema](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/pu2025_schema.json)  
**Data layer:** selected records from the 2025 SIPP file, covering the 2024 reference year  
**Weight currently available:** `WPFINWGT`, final person weight

## Why this crosswalk exists

SIPP can supply a population-survey layer for several broad bridges, but it cannot answer the entire societal chain by itself. This record maps the selected fields to the questions they can inform. It keeps the official variable meaning beside the project interpretation and names what remains outside SIPP.

| SIPP field | Official schema meaning | Broad bridge or theme | What it can help measure | What it cannot establish alone |
|---|---|---|---|---|
| `ETENURE` | Tenure at time of interview | Housing, place, inequality | renter/owner tenure differences in other measured conditions | insurance price, repair cause, displacement, or ability to stay |
| `EUTILITIES` | Whether the household paid separately for water, electricity, gas, or oil in addition to rent | Housing, energy, household room | exposure to separately billed utilities | bill amount, shutoff, safety, or energy burden without a cost measure |
| `EENERGY_ASST` | Received government energy assistance during the reference period | Public aid; housing and energy | reported program exposure | take-up barrier, benefit adequacy, repair, or political interpretation |
| `EAWBMORT` | Was unable to pay rent or mortgage | Household room; housing | reported housing payment difficulty | cause, arrears amount, eviction, foreclosure, or later move |
| `EAWBGAS` | Was unable to pay utility bills | Household room; housing and energy | reported utility-payment difficulty | shutoff, reconnection, health effect, or exact bill timing |
| `EOWN_SAV` | Owned any savings accounts during the reference period | Household room; financial security | liquid-account ownership as a buffer indicator | balance, liquidity at the shock date, or whether savings were used |
| `EDEBT_CC` | Carried a store or credit-card balance from one month to another | Consumer finance; household room | revolving-balance exposure | interest paid, medical or utility cause, delinquency, or later recovery |
| `RFOODS` | Recode for food-security status | Household room; health and care | food-security category, after official value labels are attached | which bill or event caused the condition, health result, or political response |
| `RFOODR` | Recode for raw food-security score, a count of affirmative responses | Household room; health and care | graded food-hardship measure | causal source of the hardship or household substitution |
| `EFOOD1` | Whether food bought did not last | Household room; consumer conditions | one food-shortage condition | price, income timing, or assistance response |
| `EFOOD3` | Whether meals were cut or skipped because there was not enough money for food | Household room; health and care | reported food sacrifice | health consequence, duration, or protected competing expense |
| `EFOOD6` | Whether someone was hungry but did not eat because there was not enough money for food | Household room; health and care | severe reported food hardship condition | illness, exact resource loss, or later recovery |
| `EPAY` | Whether a reference parent or family paid for child-care arrangements during a typical fall week | Time, care, and work | paid-care exposure | total care hours, unpaid replacement care, price, or job consequence |
| `EPAYHELP` | Whether a reference parent received help paying for child care | Public aid; care and work | child-care payment assistance exposure | program identity, take-up process, adequacy, or work result |
| `EWORKMORE` | Whether child-care arrangements prevented a reference parent from working or working more | Time, care, and work | reported work constraint linked to child care | wage loss, schedule control, provider failure, or counterfactual job |
| `RMNUMJOBS` | Recode of number of jobs held within the reference month | Work, control, and household room | multiple-job exposure by month | whether jobs were chosen or forced, hours, travel, benefits, or bargaining power |
| `WPFINWGT` | Final person weight | Population measurement | person-level weighted descriptive estimates | a household weight, causal identification, or variance estimates by itself |

## Current descriptive evidence

The [weighted raw-code scan](sipp-weighted-code-scan-v1.md) shows that the selected fields can be read across all twelve reference months and weighted at the person-record level. It reports raw code distributions and missingness only. The selected variables include housing payment difficulty, utility-payment difficulty, energy assistance, food-security measures, child-care payment and work constraints, savings, credit-card balances, and number of jobs.

The next valid table should attach the official value labels and status-flag rules, report the denominator and universe for each field, and stratify the measures by month and relevant population groups. Conditional blanks must remain outside the applicable universe or unknown; they must not be recoded as “no.”

## Unit and weighting rule

The extracted file is person-record by reference month. Some selected fields describe a household or parent and are copied across members. Therefore:

- use `WPFINWGT` for person-level estimates;
- do not call a person-weighted repeated household field a household prevalence estimate;
- define a household selection or household-weight method before making household claims;
- retain the household and sample identifiers for within-file structure, but do not infer a causal event from repeated monthly records alone;
- use SIPP as one population layer and do not join it to CE, ATUS, NHTS, SHED, MEPS, or RECS as if records were the same people or households.

## Bridge coverage and missing links

SIPP is immediately useful for the material and work portions of the broad program. It can show how measured conditions are distributed across people and months. It is weaker for the middle and outer links: exact prices and bills, service contacts and remedies, firm rules, cultural interpretation, trust, political action, company performance, and geopolitical exposure. Those require the corresponding source families and must remain separate until a lawful, documented join exists.
