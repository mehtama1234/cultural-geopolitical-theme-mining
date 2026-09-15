# US safety-net event ledger v1

**Purpose:** record one public-benefit episode from need through route, decision,
interruption, household result, and interpretation. This is a measurement
template, not evidence that every episode follows the full chain.

## Identification and consent

| Field | Record |
|---|---|
| Episode ID | Separate pseudonymous ID; never use name, address, or case number in the research table |
| Program and state | Program, administering agency, state, and local office or channel |
| Observation window | Start date, end date, and whether dates are exact or recalled |
| Household/person unit | Adult, child, household, or case unit; document the reporting universe |
| Consent and linkage | Permission, legal basis, linked sources, retention limit, and re-identification controls |

## Need and exposure

| Field | Record |
|---|---|
| Need or shock | Food, income, health, housing, care, work, disaster, or other need; date first noticed |
| Rule exposure | Work rule, income test, renewal, benefit change, office change, or other policy event |
| Expected support | Benefit type, amount, duration, restriction, and expected delivery date |
| Alternatives | Cash, family help, food bank, employer help, credit, other program, or no alternative |

## Route to help

| Field | Record |
|---|---|
| Notice | Date, channel, language, readability, deadline, and whether the person understood it |
| Application/renewal attempts | Date, channel, number of attempts, documents requested, and unresolved question |
| Practical cost | Hours, travel, fare, internet/device, phone, childcare, language help, disability accommodation, and missed work |
| Decision process | Human or automated step, verification, interview, denial reason, appeal option, and decision date |

## Benefit and interruption

| Field | Record |
|---|---|
| Result | Not applied, pending, approved, reduced, denied, interrupted, restored, or exited |
| Amount and timing | Amount actually received, date available, duration, and gap days |
| Reason for change | Income, rule, missed deadline, document, office/channel, agency error, voluntary exit, or unknown |
| Appeal/correction | Contact, appeal, correction, resolution, time, and cost |

## Household outcomes

Record each outcome for the same episode and date window. Do not substitute
participation or exit for any of them.

For every outcome window, record two separate fields: **protected outcome**
(what the household kept or avoided) and **sacrificed outcome** (what it lost,
delayed, transferred, or put at risk). If neither is observed, write unknown;
do not infer sacrifice from route burden or protection from continued receipt.

- food quantity, variety, skipped meals, and food-security status;
- work, hours, earnings, commute, missed shift, and job change;
- debt, borrowing, late payment, savings, and family or community help;
- health, delayed care, medication, stress, and caregiving time;
- housing payment, utility status, transportation, and ability to remain housed;
- return to the program, alternative assistance, and recovery after one, three,
  six, and twelve months.

## Interpretation and public response

Ask after the material result, and record the question wording:

- what changed and what the person thinks caused it;
- whether the process felt understandable, fair, respectful, or arbitrary;
- which actor is blamed or credited;
- trust in the program, agency, government, employer, or other institution;
- complaint, appeal, contact with an official, organizing, protest, turnout,
  vote, or no public action;
- source of information and prior political or institutional identity.

Interpretation and action are separate outcomes. Do not infer either from a
missed benefit, caseload change, or election result.

## Comparison and quality controls

Use comparison episodes with similar need but different notice, office, rule,
channel, timing, or outcome. Preserve:

1. eligible but never applied;
2. applied and received without interruption;
3. applied and delayed or denied;
4. received and then interrupted;
5. exited after improved circumstances;
6. exited without measured improvement.

Report missingness, recall, attrition, weights, universe, and exact dates. Keep
administrative records, survey answers, and researcher inferences in separate
columns. A caseload decline is not an employment result; employment is not food
security; food security is not trust; and trust is not a vote.

## Minimum end-to-end output

```text
need/rule
  -> route cost and decision
  -> receipt, interruption, or exit
  -> food/work/debt/health/housing result
  -> interpretation and action
  -> agency or policy response
```

The final report must state which arrows were observed, which were reported or
estimated, which comparisons were valid, which counterexample was retained,
and which link remains open.
