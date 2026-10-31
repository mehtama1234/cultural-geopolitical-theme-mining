# Bridge request 001 — care time and work capacity

**Status:** review required; no internal data connected
**External candidate:** `candidate-time-financial-pressure-practical-room`
**Purpose:** define the smallest internal test for whether external care/time
pressure is relevant to a company workflow.

## External evidence to carry forward

Use the candidate records as external context only:

- `comparative-abs-australia-time-use-2024-disability-carer-free-time-2026`
- `comparative-colombia-dane-enut-2024-25-unpaid-care-time-gender-migration`
- `comparative-eige-care-survey-2026-unpaid-care-work-life-digital-tools`
- `comparative-england-dhsc-sace-2025-2026-carer-time-work-social-capacity`
- `comparative-abs-general-social-survey-2025-cultural-participation-financial-stress-connection`
- `comparative-anz-roy-morgan-australian-consumer-confidence-september-29-2026-financial-outlook`
- `comparative-4culture-king-county-culture-communities-2026-participation-barriers-belonging`

These sources do not follow the same people or company and must not be
combined into a single care-burden estimate.

## Internal data needed

Select one company and one permissioned workflow, then provide:

1. **Company scope:** company ID, business unit, location, and decision owner.
2. **Workflow:** one measurable task such as shift completion, appointment
   attendance, customer-support completion, service delivery, or retention.
3. **Entity key:** an approved worker/customer/transaction identifier or a
   documented aggregate comparison; never use names as an assumed join key.
4. **Time window:** internal observation period aligned to the external
   candidate without claiming the periods are identical.
5. **Outcome:** completion, delay, absence, repeat contact, retention, or exit,
   with numerator, denominator, unit, and missingness.
6. **Care/time proxy:** only a lawful and privacy-reviewed field, such as
   declared schedule constraint, accommodation request, care leave, shift
   flexibility use, or a voluntary survey measure.
7. **Comparison:** an explicit baseline or comparison group, with subgroup
   denominators and an accessible counterexample.

## Test hypothesis

> In the selected workflow, greater care/time constraint or lower schedule
> flexibility is associated with a measurable difference in task completion,
> delay, repeat effort, absence, or retention, after accounting for the stated
> comparison variables.

This is a hypothesis only. It is not a finding about the company or its people.

## Required review before connection

- privacy and employment/customer-data review;
- data owner approval and retention period;
- external/internal geography and period compatibility;
- denominator and missingness audit;
- confounders and competing explanations;
- subgroup fairness and disclosure-risk review;
- explicit falsifier, such as no difference after adjustment or a stronger
  alternative explanation; and
- decision owner who can act on the result.

## Current decision

No internal bridge is approved yet. The next action is to select the company,
workflow, internal dataset, and lawful care/time proxy. If those cannot be
provided, retain this as an open bridge request rather than weakening the join.
