# Political-response measurement specification v1

**Purpose:** define the next test of the broad-program arrow from material
conditions to interpretation and political action. This is a measurement
specification, not a claim that the arrow has already been established.

## The estimand

For a defined US population and time window, estimate separately:

1. the change in material exposure (price, pay, bill, benefit, or job rule);
2. the household or consumer response (cut, delay, borrow, switch, work more,
   seek help, complain, or go without);
3. the person's interpretation (personal condition, national condition,
   fairness, blamed actor, policy knowledge, and confidence);
4. the political expression (trust, policy demand, contact, organizing,
   protest, or media action); and
5. the political action (turnout, vote, party change, or institutional response).

The target is not one composite “economic mood” score. A change in one stage
must not be reported as a change in a later stage.

## Current source-to-stage map

The broad program already has useful pieces, but they are not interchangeable.
This table is the current acquisition control: it shows what can be reported
now and what a real end-to-end instrument would still need.

| Source layer | Strongest stage(s) | Unit and time | Usable now | Missing for the full path |
|---|---|---|---|---|
| SHED 2025 cross-section | Adjustment and financial condition | US adult respondent, annual reference period | Population distribution of substitution, reduced use, saving cuts, borrowing, delay, extra work, and emergency capacity | Dated exposure, blamed actor, source environment, trust, and action in the same respondent record |
| SHED 2024–2025 panel | Adjustment persistence and broad condition transition | Recontacted respondent, two annual waves | Persistence and re-entry by worsening, same, or improving financial-condition path | Exact event timing, attribution, political interpretation, and later action |
| ANES 2024 and 2016–2020–2024 panel | Interpretation, trust, identity, and reported vote | Eligible-voter respondent, pre/post election; panel respondent across nine waves | The current release confirms a repeated-respondent panel with 2,171 2024 pre-election and 2,070 post-election panel interviews; the full-release layer measures financial worry, national judgment, government trust, perceived capture/waste, party identity, and reported vote | Local panel analysis is not yet run because the current CSV download returns a publisher web challenge; after acquisition, test equivalent variables, panel weights, attrition, and complex-design uncertainty |
| Pew 2025 | Source environment and civic expression | US adult respondent plus public account analysis | News-source use/trust, influencer exposure, discussion, volunteering, contact, voting, and engagement types | Same-respondent material exposure and platform encounter preceding interpretation |
| SIPP/administrative records | Material and program exposure | Person-month, program spell, place | Work, resources, SNAP receipt/transitions, reasons, food, and hardship context | Political meaning, trust, source, and action tied to the same episode |
| BLS/CE, election, and place records | Contextual exposure and population response | Item, consumer unit, county, election, year/month | Prices, spending, real wages, local conditions, and election/place outcomes | Individual attribution and the ability to distinguish ecological alignment from respondent experience |

The proper synthesis is therefore a staged population map. SHED can establish
that adaptation is widespread and persistent; ANES can establish that financial
worry coexists with different economic judgments and trust; and Pew can
establish differentiated civic participation and source environments. None of
these alone establishes that a particular cost produced a particular political
action.

## Required record

| Stage | Minimum fields | Valid unit |
|---|---|---|
| Exposure | amount, direction, date, category, location, policy/firm source, expected versus realized | person, household, consumer unit, county, or policy episode |
| Adjustment | purchase change, delay, substitution, borrowing, missed payment, extra work, care change, help sought | same person/household or clearly defined population comparison |
| Interpretation | personal and national economic rating, fairness, blamed actor, policy knowledge, expected future | same respondent and survey wave |
| Expression | trust, policy preference, complaint, contact, organizing, protest, media or civic action | same respondent and wave/episode |
| Action | registration, turnout, vote choice, party change, local measure, legislative or agency response | respondent/election where lawful, or county/election/institution |
| Context | party identity, race, income, age, family, work, health, place, news exposure, local industry, alternatives | same unit and time window |

## Preferred designs

### A. Repeated respondent panel

Follow the same respondent before, during, and after a defined price, wage, or
benefit change. Measure exposure and adjustment first; ask interpretation and
action in separate waves. This is the strongest design for the missing middle,
but it requires valid panel identifiers and attrition checks.

### B. Policy or benefit event study

Compare eligible and less-exposed groups around a known start, expiration, or
rule change. Record notice, eligibility, take-up, timing, and material result
before interpreting sentiment. Test pre-trends and spillovers.

### C. Place-level contextual comparison

Compare counties or commuting zones by real-wage change, local prices, or
benefit exposure and then compare sentiment or election outcomes. This can
show population/place alignment, but it cannot identify an individual voter's
experience or reason. Never label it a household panel.

## Main contrasts

- same inflation, different real-wage change;
- same benefit exposure, different notice or payment timing;
- same measured burden, different party identity or news environment;
- same material pressure, different alternatives and ability to exit;
- same sentiment change, different turnout or non-electoral action.

## Counterexamples that must be sought

- material pressure rises but personal and national judgments do not change;
- sentiment changes while material exposure is stable;
- a person blames a firm, foreign actor, or local institution rather than the
  national government;
- trust changes but turnout, vote, or public contact does not;
- election results change in places where measured real wages and prices do not;
- a benefit improves spending but creates a later cliff or no durable security;
- party identity or media exposure predicts the judgment more strongly than
  the measured cost.

## Analysis rules

- Preserve the time order; do not use an outcome measured before the exposure.
- Report the price level, inflation rate, nominal pay, real pay, and necessary
  cost separately.
- Report exposure, adjustment, interpretation, expression, and action as
  separate outcomes with denominators and missingness.
- Condition on pre-exposure party identity and local context, but do not treat
  post-exposure trust or blame as a harmless control if it is part of the path.
- Inspect heterogeneous effects by income, race, age, gender, disability,
  family, work, migration, tenure, and place when the sample supports them.
- Use survey weights and design-based uncertainty where provided; test panel
  attrition, nonresponse, and ecological fallacy.
- A county result may contextualize a respondent result but may not substitute
  for it.

## Current evidence and next acquisition

The existing [cost/trust/politics scan](paper-scan-v1.md) supplies population
survey, sentiment, trust, and county-election starting points. The [real-wage
finding](../../findings/us-economic-voting-real-wages-matched-evidence-001.md)
supplies a place-level comparison, while the [public-aid bridge](../../bridges/us-public-aid-interpretation-political-response-v1.md)
defines the six-stage separation. The next acquisition should prioritize a
repeated respondent source with material exposure, attribution, trust, and
political-action fields in the same study, then use county or election records
as context rather than as a person-level replacement.

Until that source is obtained, the current conclusion remains bounded:
material conditions can align with economic judgments and population/place
political outcomes, but the same-person path through blame, trust, and action
is open.

The ANES panel is now a concrete acquisition target rather than a hypothetical
design. The official merged-file page reports nine waves and the current May
19, 2026 release, but the CSV endpoint returned web-challenge HTML in the
local shell attempt. No panel estimates should be produced until the ZIP is
obtained and its repeated-variable list, panel weights, missing codes, and
attrition are verified locally.

## Immediate executable pass

1. Use the SHED panel to define the material-transition sample and classify
   worsening, stable, and improving paths; retain adaptation persistence as a
   separate outcome.
2. Use ANES to specify the interpretation fields—worry, national judgment,
   trust, capture, waste, identity, attribution, and action—and record their
   valid universes and weights without importing SHED respondents.
3. Use Pew to classify source environment and civic-action style, preserving
   the distinction between encounter, trust, discussion, contact, volunteering,
   voting, and withdrawal.
4. Acquire or construct a repeated-respondent source that contains at least a
   material exposure, an attribution field, a trust/meaning field, and a later
   action field. If no source contains all four, state that the causal middle
   remains open and use the separate layers only as context.
5. Add one counterexample for every proposed bridge: pressure without changed
   judgment, changed judgment without pressure, trust without action, and
   action with a different blamed actor.
