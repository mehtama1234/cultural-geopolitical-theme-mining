# From capability and dependence to alliance response and leverage

**Status:** fourteenth active depth artifact in the ongoing program  
**Checked:** 2026-10-18  
**Scope:** defense spending, procurement, industrial capacity, dependence, alliance implementation, public legitimacy, and observed external response

## The question

When a state spends more, signs a procurement agreement, builds an industrial
partnership, or hosts strategic infrastructure, what has actually changed?
Does the change create capability, an option to refuse or switch, alliance
cohesion, or leverage over another actor?

The stages are:

```text
threat or strategic objective
  -> budget and financing
  -> contract, ownership, supplier, and place
  -> production, delivery, training, and maintenance
  -> readiness, interoperability, and replaceability
  -> alliance implementation and public legitimacy
  -> refusal, substitution, concession, retaliation, or changed behavior
```

The evidence is strongest before the final arrow. Spending, procurement, and
official statements are not themselves leverage.

## Evidence packet

| Stage | Evidence | Safe interpretation | Missing link |
|---|---|---|---|
| Resources | SIPRI estimates 2025 world military spending at $2.887tn, with Europe up 14% in real terms and NATO accounting for 55% of world spending; IMF analysis reports a typical defense-boom increase of 2.7 percentage points of GDP, with 67% deficit-financed and debt rising about 7 points within three years. | States are allocating resources under fiscal and alliance constraints. | Readiness, household/service incidence, production, and usable capability. |
| Dependence model | NBER W34006 models asymmetric import dependence weighted by sectoral elasticities and finds more engagement/negotiation plus anticipatory trade adjustment when relationships worsen. | Dependence can create a bargaining mechanism in the model. | A named threat, successful coercion, concession, substitution, or durable geopolitical change. |
| Procurement network | One JASSM/LRASM parent-award extract contains 74 subaward records, 51 distinct recipient names, and about $1.143bn in reported amounts. | A bounded supplier and component map can be built. | Complete supply chain, facility assignment, delivery, acceptance, maintenance, and qualified alternatives. |
| Production and integration | Official and company records report production-support contracts, facilities, planned quantities, delivery windows, exercises, and testing. | Activity is becoming more concrete than an announcement. | Accepted inventory, sustained readiness, combat performance, and ability to replace or refuse a supplier. |
| Alliance implementation | NATO describes readiness, fielded capabilities, executable plans, industrial demand, and critical-infrastructure resilience; Lithuania/Germany report a multinational brigade exercise with about 2,900 personnel, 800 vehicles, eight nations, and live firing. | Training and institutional implementation are observable milestones. | Unit-level readiness, wartime performance, public burden acceptance, adversary adaptation, and deterrence. |
| Public legitimacy | A 2025 German survey reports 64% support higher defense spending, 73% support a common European security policy, 37% view the U.S. as a reliable partner, and 22% know something about the Lithuania mission; a 2023 Lithuanian poll reports 82% support for stationing a German brigade. | General support and host-country approval are separate legitimacy surfaces. | Event-specific informed consent, local costs, durable support, and link to operational behavior. |
| External response | NATO reports solidarity, Article 4 consultation, named allied assets, and Eastern Sentry after a reported airspace-violation episode. | A visible alliance response can be recorded. | Attribution to a particular new capability, adversary adaptation, deterrence, concession, or lasting alliance change. |

Primary records: [defense resources, procurement, and capability](../../records/us-defense-resource-procurement-capability-leverage-crosssource-2024-2026.json),
[NBER international power](../../records/us-nber-international-power-negotiation-2025.json),
[NATO/alliance response and legitimacy context](../../records/us-nato-lithuania-drone-interception-alliance-response-2026.json),
[SIPRI state capacity](../../records/us-sipri-military-expenditure-2025-state-capacity.json),
and the [realization ledger protocol](realization-ledger-protocol-v1.md).

## What the evidence shows together

### 1. Spending creates room, not readiness

SIPRI and IMF establish scale and fiscal trade-offs. A defense buildup may
expand options, but imported equipment, workforce, maintenance, integration,
and budget timing determine whether the option can be used. Higher spending can
also reduce fiscal room for social services or increase debt, depending on the
financing and domestic capacity.

### 2. Dependence can create both vulnerability and engagement

The NBER model gives a useful counter to simple “dependence equals weakness”
stories: asymmetric dependence may induce negotiation because both sides have
something to protect. The paper’s power measure is modeled, not an observed
threat or concession. A country can have bargaining exposure without being able
to make the other side change course.

### 3. Procurement is not a fielded system

The JASSM/LRASM and allied-procurement records now show awards, subawards,
entity identities, production support, tests, and planned windows. The event
ledger still keeps shipment, acceptance, training, inventory, operational use,
and external response separate. This is not a documentation technicality: each
stage changes whether a state actually has an option.

### 4. Exercises show integration, not deterrence

The Lithuania exercise is a meaningful operational milestone: named units,
multinational participation, movement, tactics, and live firing. It does not
show performance under attack, sustained readiness, local burden distribution,
or that an adversary changed behavior because of it.

### 5. Legitimacy has more than one denominator

German support for defense investment, Lithuanian approval of a brigade, and
knowledge of a specific mission are not interchangeable. A public can support
alliance protection while opposing land use, cost, escalation, or a particular
deployment. Host approval before an exercise is not evidence of consent for
every later burden.

## Counterexamples and alternative explanations

- Spending can rise while readiness falls because procurement, staffing, or
  maintenance cannot keep pace.
- A diversified supplier list can reflect reporting structure rather than real
  substitute production capacity.
- Local assembly can coexist with foreign control of design, software,
  certification, finance, export permission, or critical parts.
- More engagement under dependence can reflect cooperation or routine trade
  management rather than credible coercion.
- A rapid alliance response can reassure partners without deterring an adversary.
- High public support can reflect threat perception while hiding low knowledge
  of the actual mission or unequal local costs.
- A completed exercise can improve interoperability without proving combat
  performance or durable alliance cohesion.

## Bounded social discussion

The social records add public meaning, not operational proof:

- [European strategic-autonomy discussion](../../social-discussions/records/geopolitical-state-linkedin-001.json)
  distinguishes interoperability from asymmetric dependence and ties autonomy
  to factories, supply chains, engineering, and production.
- [Geopolitical Reddit discussion](../../social-discussions/records/geopolitical-state-reddit-001.json)
  surfaces public reasoning about sovereignty, dependence, and state capacity;
  it is not a readiness or bargaining measure.
- [Geopolitical X discussion](../../social-discussions/records/geopolitical-state-x-001.json)
  shows platform interpretation of state action and strategic identity, not
  verified policy response.
- [SIPRI spending discussion](../../social-discussions/records/social-sipri-military-expenditure-2025-linkedin-001.json)
  makes defense allocation and burden-sharing visible to a professional
  audience; spending attention is not capability.

## Stronger next test

Use one country-year or incident ledger with separate rows for:

```text
threat/incident
  -> resource allocation
  -> contract and supplier
  -> production and shipment
  -> acceptance, training, and inventory
  -> operational performance
  -> public/local burden and legitimacy
  -> alliance or external response
  -> adversary adaptation, concession, substitution, or refusal
```

For each row record actor, date, quantity, unit, source, method, confidence,
and the next stage not observed. A leverage claim is promoted only when a new
capability or dependence is temporally close to an observed change in another
actor’s choice and plausible alternatives are checked.

## Current answer

**Answer state: partly answered.** The repo can now follow resources,
procurement, production activity, exercises, public legitimacy, and alliance
response as separate stages. It still lacks a clean named episode joining a
fielded capability or dependence to changed external behavior. The long-term
program remains active.

Related project: [AI, work, and control](README.md). Related operating plan:
[ongoing cross-source theme-mining program](../../ONGOING-GOAL-OPERATING-PLAN_V1.md).
