# Formal and informal support are different protection routes v1

**Checked:** 2026-09-17
**Scope:** household protection, care, food, neighborhood, religious/community, and public-system evidence already retained in the atlas
**Status:** cross-source route synthesis; not a resilience index or estimate of substituteability

## The central finding

When households face pressure, protection can arrive through family, neighbors,
religious or community institutions, charities, employers, insurance, or public
programs. These routes are not interchangeable. They differ in eligibility,
visibility, speed, dignity, reciprocity, administrative effort, financial cost,
and whether they preserve or consume the helper’s own time and resources.

The broad goal should therefore ask not only “did help exist?” but:

```text
who supplied protection -> through which route -> at what burden
-> with what adequacy and continuity -> with what meaning and later action
```

## Route comparison

| Route | What the atlas observes | Distinct failure or cost | Missing same-unit stage |
|---|---|---|---|
| Family/kinship | Kinship families, multigenerational living, outside help, and intergenerational care | Poverty, disability, housing/work displacement, hidden reciprocal labor | Actual transfer, caregiver burden, adequacy, later household recovery |
| Neighbors/friends | Local familiarity/trust and stated willingness to hold keys, provide meals, errands, money, or emergency conservation | Reciprocity expectations are lower than willingness; resources and place condition capacity | Dated crisis, help delivered, duration, burden, adequacy |
| Religious/community | Affiliation, attendance, cultural identity, community connection, charitable or civic potential | Formal identity does not imply practice, institution, or available material support | Named institution, request, delivery, cost, continuity, political meaning |
| Charitable food/support | Food-bank reach, reported use, stigma, difficulty, and unmet need | Coverage can coexist with hunger, time cost, uncertainty, and stigma | Same household’s need, route effort, receipt, adequacy, repeat use |
| Public benefits | SNAP/Medicaid/LIHEAP receipt, transitions, reasons, processing, interruptions, and restoration | Notices, recertification, interviews, data governance, interruption, and eligibility churn | Same episode’s notice, effort, decision, remedy, recovery, trust |
| Employer/market | Wages, work intensity, employer concentration, insurance, credit, and platform routes | Work and benefits can coexist; formal access may leave cost, dependence, or weak exit | Terms, alternatives, remedy, household incidence, switching |

## What the combined evidence supports

### Protection is a portfolio, not a single program

The same household can combine wages, public benefits, family transfers,
neighbor help, charity, credit, and reduced consumption. A route’s existence
does not tell us whether it was preferred, adequate, or sustainable. Substitution
can conceal hardship: a parent may provide housing, a neighbor may provide an
errand, or a food pantry may prevent an empty meal while transferring time,
privacy, stigma, or financial pressure elsewhere.

### Informal support is capacity with a balance sheet

Neighbor survey responses show that people often say they would help more than
they expect others to help them. Family and kinship evidence similarly shows
care being absorbed by households. These are not merely signs of social virtue;
they are potential reallocations of labor, money, housing, risk, and attention.
The helper’s burden must be measured alongside the recipient’s protection.

### Formal access is not usable access

Public programs and institutions can have large reach or nominal coverage while
the route to help remains difficult. The relevant outcome is not enrollment or
availability alone, but completed, adequate, timely, and durable protection. A
failed notice, inaccessible office, recertification interruption, or missing
accommodation can make formal capacity functionally unavailable.

### Meaning changes with the route

The same material protection can be interpreted as security, dignity, family
duty, charity, dependency, unfairness, reciprocity, or public entitlement. The
current evidence documents many of these candidate meanings separately, but no
source follows one household from route selection through interpretation and
later civic or political action.

## The important counterexamples

- Help can exist without recovery: food access, outside medical help, or a
  benefit payment may coexist with continuing hardship.
- Work can coexist with public benefits: employment does not prove household
  security or employer responsibility.
- Trust can coexist with low capacity: a person may trust neighbors but lack
  time, money, transportation, or health to help.
- Formal coverage can coexist with non-use: eligibility or route availability
  does not prove a person could safely, affordably, or respectfully use it.
- Informal help can protect one household while burdening another; apparent
  resilience is not necessarily a net welfare gain.

## End-to-end position

The strongest bounded chain is:

```text
pressure or need
  -> available formal and informal routes
  -> selected or forced route
  -> delivered protection and helper/recipient burden
  -> adequacy and continuity
  -> meaning, trust, switching, or political demand
```

The atlas currently has separate observations for nearly every stage, but not
one lawful same-household or same-person record that closes the chain. The
absence is substantive: route choice, non-use, and burden are likely part of
the cultural and political story, not noise around program participation.

## Next executable design

Extend the cultural-meaning episode matrix with a support-route module:

```text
unit_id, need_date, need_type, route_available, route_selected,
formal_or_informal, requester_effort, provider_burden, aid_received,
adequacy, continuity, dignity_or_fairness, later_trust, action_or_exit
```

Begin with existing recontact or event-compatible artifacts. Acquire new data
only when a source exposes both the recipient and route stages, permits linkage,
and has a defined denominator. Do not create a “resilience” score by adding
benefits, family support, trust, or charity into one total.

## Boundary

This synthesis compares evidence with different populations, dates, units, and
methods. It does not estimate the share of households using each route, rank
formal against informal support, or claim that one route causes later trust,
political action, or recovery. “Support route” includes a potential option only
when the source observes it; availability, willingness, receipt, adequacy, and
continuity remain separate.
