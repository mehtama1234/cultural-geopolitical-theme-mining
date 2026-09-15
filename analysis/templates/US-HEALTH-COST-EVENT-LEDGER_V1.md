# US health-cost event ledger v1

## Purpose

Use this ledger to follow a defined health-cost episode from a dated need,
bill, coverage rule, or payment problem through care, household substitution,
recovery, institutional response, and later meaning or action. It is an
instrument for future linked or same-household evidence, not a claim that
CMS, MEPS, SHED, SIPP, or any existing record already observes every field.

The ledger must preserve the source's unit. A national account, person survey
record, household record, provider encounter, complaint, and political response
are adjacent rows only when their linkage, date, geography, and denominator are
explicitly documented.

## Required episode fields

| Field | Required content | Do not infer |
|---|---|---|
| `episode_id` | Stable pseudonymous episode key and linkage rule | Identity beyond the approved research design |
| `source_record` | Dataset, file/wave, URL, retrieval date, release/vintage, hash | That a landing page is the observed episode |
| `person_household_unit` | Person, family, household, provider, payer, or administrative case | That person and household are interchangeable |
| `geography` | Residence, provider, service, or administrative geography with level | A national average as local access |
| `trigger_date_window` | Date or bounded period for need, bill, coverage change, or payment problem | Timing from an annual aggregate alone |
| `health_need_or_service` | Need, diagnosis, service, medication, preventive care, or care-seeking event | Severity or clinical necessity not measured by the source |
| `coverage_and_terms` | Insurance status, payer, deductible, denial, network, authorization, or public-program rule | Coverage as proof of affordability |
| `bill_and_payment` | Billed, allowed, paid, out-of-pocket, premium, debt, assistance, or unresolved amount | A payer total as one household bill |
| `care_decision` | Received, delayed, skipped, substituted, abandoned, or unknown; reason and date | Causation from expenditure alone |
| `available_alternatives` | Provider, treatment, transport, schedule, family, credit, savings, or public-help options | Choice where alternatives were not measured |
| `money_time_care_response` | Borrowing, savings draw, work change, unpaid care, travel, waiting, food/housing tradeoff | A measured payment as the full burden |
| `downstream_outcome` | Health, work, income, debt, coverage continuity, recovery, or unresolved status | Improvement as proof the episode was affordable |
| `institutional_response` | Provider, insurer, employer, regulator, court, or public-program action | Complaint closure as verified remedy |
| `meaning_action_exit` | Trust, fairness, attribution, political/civic action, switching, or continued use when directly measured | Vote intention as response to this episode |
| `uncertainty_and_missingness` | Missing fields, attrition, nonresponse, weighting, intervals, and linkage failure | Silence as absence of harm or response |

## One-row episode form

```yaml
episode_id: "local-pseudonymous-key"
source_record:
  dataset: ""
  file_wave: ""
  source_url: ""
  retrieval_date: ""
  vintage: ""
  artifact_hash: ""
person_household_unit: "person | household | provider | payer | case"
geography:
  type: "residence | provider | service | administrative"
  value: ""
trigger_date_window:
  start: ""
  end: ""
health_need_or_service:
  category: ""
  observed_measure: ""
  denominator: ""
coverage_and_terms:
  status: ""
  payer: ""
  restriction_or_rule: ""
bill_and_payment:
  billed_amount: null
  allowed_amount: null
  paid_amount: null
  out_of_pocket_amount: null
  debt_or_unresolved_amount: null
  currency_and_price_year: ""
care_decision:
  status: "received | delayed | skipped | substituted | abandoned | unknown"
  reason: ""
  decision_date: ""
available_alternatives:
  provider: ""
  treatment: ""
  transport: ""
  schedule: ""
  family_or_public_help: ""
money_time_care_response:
  money: ""
  paid_work: ""
  unpaid_care: ""
  waiting_or_travel: ""
  protected_or_sacrificed_need: ""
downstream_outcome:
  health: ""
  work_income: ""
  debt_credit: ""
  coverage_continuity: ""
  recovery_status: ""
institutional_response:
  actor: ""
  action: ""
  response_date: ""
  verified_remedy: "yes | no | unknown"
meaning_action_exit:
  trust_or_fairness: ""
  attribution: ""
  civic_or_political_action: ""
  switching_or_exit: ""
uncertainty_and_missingness:
  missing_fields: []
  sample_or_linkage_limit: ""
  standard_errors_or_interval: ""
  counterinterpretation: ""
```

## Assembly rules

1. Start with the narrowest observed event. Do not backfill a trigger from a
   later outcome.
2. Keep billed, allowed, paid, out-of-pocket, premium, debt, and public
   spending amounts in separate fields.
3. Record the decision-maker and the available alternative before describing a
   behavior as a choice.
4. Mark every cross-source join as exact, probabilistic, contextual, or open.
5. Keep annual, monthly, diary-day, encounter, and administrative clocks
   separate; a common calendar year is not a same-episode key.
6. Publish a negative or incomplete episode as an acquisition gap, not as
   evidence that no burden, care delay, or institutional response occurred.
7. Report subgroup and place differences only with their own denominators,
   uncertainty, and coverage universe.

## Minimum evidence package before promotion

An episode-derived finding can enter the atlas only when it has:

- a source artifact and retrieval hash;
- a defined unit, geography, date window, and denominator;
- a documented linkage or an explicit non-linkage boundary;
- the measured care, money, time, and downstream fields;
- subgroup, missingness, uncertainty, and counterexample notes; and
- a reader-facing explanation of what remains open before trust, political
  action, institutional power, or geopolitical meaning is discussed.

## Current source roles

| Source | Strongest current role | Missing episode fields |
|---|---|---|
| CMS NHEA | National spending, payer, sponsor, service, and GDP scale | Same household, bill, care decision, time, recovery |
| MEPS Panel 27 | Person expenditure, coverage, perceived health, work, income, and utilization transitions | Dated bill/need, alternatives, unpaid care, debt episode, remedy |
| SHED | Reported care choices, hardship, debt, liquidity, and adaptation | Clinical/event linkage, provider action, exact bill, later recovery |
| SIPP | Monthly resources, work, programs, health, and household transitions | Health-service episode, bill, care decision, institutional response |
| CFPB/DFS/other administrative routes | Complaint, routing, response, and regulator action | Same patient/household exposure, care outcome, verified recovery |

The next acquisition should fill the middle of the chain rather than add
another aggregate spending total.
