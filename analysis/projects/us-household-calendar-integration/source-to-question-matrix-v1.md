# US household calendar source-to-question matrix v1

**Purpose:** decide what can be tested from public data before asking households for a new twelve-month record.

The matrix uses four levels:

- **Direct:** the source measures the needed item in the same unit and time window.
- **Useful proxy:** the source measures part of the question, but not the full event.
- **Context:** the source sets a national, state, or group pattern.
- **Missing:** a new calendar record or a permitted linked record is needed.

## Claim matrix

| Claim | Public sources | Direct pieces | Useful proxy or context | Still missing | First test |
|---|---|---|---|---|---|
| HC-001 Payment timing predicts which basic need is delayed after a short cash gap. | SIPP, CE, CPS, CPS-FSS | Monthly income and some program changes in SIPP; spending categories in CE | CPS labor change; USDA food outcome | Exact pay dates, bill dates, reserve, first cut, and next-month result in the same household | Compare households with similar monthly resources but different income and bill timing |
| HC-002 A lower posted cost is not a lower household cost when the alternative takes more time, risk, or debt. | CE, ATUS, NHTS, SHED | Spending categories; one-day time use; trip purpose, mode, and travel time | SHED financial room and credit access | Same purchase or trip’s price, time, safety, quality, debt, and result | Build a transport and purchase comparison with price, time, and substitute fields kept separate |
| HC-003 Service restoration does not always restore household room. | SIPP, CE, RECS, CPS-FSS | Household changes; utilities and housing-cost categories; energy insecurity; food outcome | RECS energy cost and home features | Shutoff warning, restoration fee, temperature, medicine or food tradeoff, work loss, repeat event | Look for households with service difficulty plus later debt, food, health, or housing pressure |
| HC-004 A benefit exit can reflect administrative failure rather than improved work or lower need. | SIPP, CPS, SHED | Program participation and income/work changes; some hardship and access questions | SHED reports of application and financial strain | Notice, deadline, document request, contact attempts, appeal, and exact exit cause | Separate exits paired with higher income from exits paired with paperwork or access problems |
| HC-005 Family help can protect one household while reducing another household’s future room. | SIPP, ATUS, SHED, CPS | Household composition, income, some care, time use, and financial strain | SHED care and hardship; ATUS unpaid care patterns | Linked helper and receiver records with cash, time, terms, work, health, and later shock | Treat family help as a transfer with a receiver, helper, date, and later capacity field |
| HC-006 A record or screening rule can make recovery more expensive after the original shock. | SIPP, SHED, CFPB and other administrative sources later | Income, wealth, credit access, and hardship in survey layers | Public complaints or firm rules can show system behavior | The same household’s record entry, decision, deposit, price, correction, debt, and later access | Start with the rule and outcome separately; do not infer household harm from complaints alone |
| HC-007 A firm or public program can look successful while shifting cost to a household, worker, customer, or future bill. | CE, SIPP, SHED, MEPS, RECS, BEA | Spending, income, hardship, health cost, and energy cost pieces | BEA and agency totals show the institutional scale | Recipient-level authority, remedy, time, debt, and later stability | For each program or firm outcome, name the person who paid and the later cost carrier |
| HC-008 Repeated material pressure may affect trust or public judgment through interpretation and action, not automatically. | SHED, SIPP, CPS, ANES or GSS later | Some financial views, household conditions, and demographics | Annual public judgment and economic-perception measures | Dated burden, remembered price, blamed actor, policy knowledge, action, turnout, and vote | Test the middle steps—burden, blame, belief, action—before connecting pressure to politics |

## The first extraction pass

The first pass should be small. It is meant to expose coding and join problems, not produce a headline finding.

| Order | Source | Pull | Output | Stop condition |
|---|---|---|---|---|
| 1 | SIPP | One recent public-use year; monthly income, work, household change, program use, child care, food security, and wealth fields | Household-month spine and missingness table | We cannot define a stable household-month key or date meaning |
| 2 | CE | One recent Interview file and one Diary file; rent, utilities, transport, food, repair, fees, income, and household traits | Spending-category dictionary and recall-window note | Categories or periods cannot be compared without a false precision claim |
| 3 | ATUS | One recent year; paid work, travel, child care, elder care, household work, and rest | Time-cost reference table | One-day diary cannot support the repeated event claim |
| 4 | NHTS | 2022 public data; mode, purpose, travel time, vehicle availability, rideshare questions, and geography | Transport access baseline | Fare, rideshare cost, or outcome is absent and must be marked missing |
| 5 | SHED | Latest public year plus one prior year where respondent linking is allowed; financial room, hardship, care, housing, credit, and economic views | Annual room-and-judgment check | Annual responses are mistaken for monthly observations |
| 6 | MEPS | One recent panel; medical events, payments, insurance, access, work, and income | Health-cost event dictionary | Restricted or event-level fields cannot be used in the planned access path |
| 7 | RECS | Latest public cycle; home type, energy insecurity, energy cost, and supplier-supported use | Energy burden and housing-type cross-check | Periodic estimates are presented as recovery over time |
| 8 | BEA and CPS-FSS | Matching recent periods; PCE, prices, labor, food spending, assistance, and food security | Outside context table | Macro or annual measures are called household evidence |

## Join rules

1. Join records by a documented source key only. Never join two public surveys by geography and call the result a household panel.
2. Keep the observation window beside every value: day, week, month, quarter, year, or periodic cycle.
3. Keep the unit beside every value: person, consumer unit, household, housing unit, trip, event, state, or nation.
4. Keep source weights and nonresponse limits in the extract notes.
5. Use `unknown` when a source does not observe a field. Do not turn a missing fare, bill date, or remedy into zero.
6. A public source can support a mechanism only to the level it measures. The exact chain from warning to choice to recovery still requires the calendar panel.

## Decision after the first pass

The extraction pass should end with three lists:

- **Testable now:** links that public data measure in a compatible unit and period.
- **Triangulable:** links supported by separate sources but not by the same household record.
- **Panel-required:** links that need dated household events, control, remedy, and next-month outcome.

Only the first list should produce a direct quantitative finding. The second should be written as connected evidence with limits. The third should shape the questionnaire and consent process.
