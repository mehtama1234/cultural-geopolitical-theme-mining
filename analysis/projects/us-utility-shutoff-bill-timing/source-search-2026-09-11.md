# Source search: US utility shutoff and bill timing

**Search date:** 2026-09-11  
**Geography:** United States, with a Rhode Island administrative-data study  
**Status:** opening pass; bill timing is a concrete mechanism, wider health effects remain open

## Working question

Can the date a bill is due change whether a household keeps basic utility service?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-NBER-UTILITY-TIMING | [The Impact of Benefit Receipt on Financial Security Among Low-Income and Aged Households](https://www.nber.org/programs-projects/projects-and-centers/retirement-and-disability-research-center/7573-nb19-09-impact-benefit-receipt-financial-security-among-low-income-and-aged-households-new) | The project uses private and linked administrative data to test whether having a utility bill due late in the month, after income arrives, changes late payment, shutoff, credit scores, emergency-department use, arrests and other outcomes. | NBER research project | The project description states the outcomes to be studied; it is not by itself a completed estimate for every outcome. |
| US-NBER-BILL-DIGEST | [How Bill Timing Affects Low-Income and Aged Households](https://www.nber.org/brd/how-bill-timing-affects-low-income-and-aged-households) | NBER explains that benefit and bill timing can affect whether households pay necessary bills, and describes electricity payment as a concrete test of the problem. | NBER research digest | The digest does not establish that timing alone caused a shutoff or health change for every household. |
| US-DOE-ENERGY-BURDEN | [Low-Income Energy Affordability Data Tool](https://www.energy.gov/cmei/scep/low-income-energy-affordability-data-lead-tool) | DOE measures energy burden as the share of income spent on home energy and shows that the burden differs by income and place. | Official US data tool | The measure does not include bill due dates, shutoffs or the household's next choice. |
| US-HBS-HOME-SAFETY | [Who Guarantees Your Workplace Is Safe for Return?](https://www.library.hbs.edu/working-knowledge/who-guarantees-your-workplace-is-safe-for-return) | HBS shows why safe basic conditions depend on rules, monitoring and who is responsible for acting when a risk is visible. | HBS Working Knowledge | This is a workplace example, not evidence about residential utility shutoffs; it is a comparison for responsibility and response. |

## First pattern to test

```text
income or benefit arrives
  -> utility bill is due at a different time
  -> late payment or arrears
  -> shutoff, reconnection fee, borrowing, or a missed service
  -> credit, health, work, or trust in institutions changes
```

The NBER project makes timing a testable part of household financial security. DOE's burden measure explains why the same timing problem may be harder for one household than another. The missing proof is the size and direction of each later effect.

## Counterpoint to keep visible

Many households can shift a due date, use assistance or pay the bill without a shutoff. A late payment may be temporary and a service rule may prevent immediate harm. The analysis must count those protections.

## Main gaps

- exact income and bill dates;
- arrears, shutoff and reconnection charges;
- weather and medical equipment needs;
- credit, emergency care and work outcomes after a shutoff;
- utility rules and aid programs by state;
- households that avoid shutoff by borrowing or family help.

## Decision rule

Use observed bill and income dates with service and outcome records. If only energy burden is available, describe exposure and move on without claiming a shutoff effect.
