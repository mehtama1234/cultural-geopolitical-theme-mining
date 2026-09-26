# Event-country-party-year acquisition manifest v1

**Checked:** 2026-09-20
**Status:** acquisition design; no new causal or leverage claim

## Purpose

Turn the geopolitical legitimacy question into a small, auditable event
ledger. The manifest keeps four things separate: what happened, how publics
interpreted it, what institutions did, and whether another actor changed
behavior. Existing records are candidate inputs, not a joined panel.

## Minimum row contract

```text
case_id, event_date, event_type, country, actor, recipient,
capability_or_policy, external_public_measure, US_party_or_generation_measure,
media_or_elite_frame, government_or_alliance_response,
market_or_consumer_response, aid_or_cooperation_status,
refusal/substitution/concession, later_reputation_or_action,
source_locator, denominator, status, missingness, counterexample
```

Promotion requires a dated event, a named country or actor, a compatible
before/after or comparison design, and an observed response. A survey judgment,
analyst assessment, contract, or public statement alone cannot populate the
response endpoint.

## Retained candidate inputs

| Candidate | What is already observed | Missing decisive fields | Safe use now |
|---|---|---|---|
| Pew 2026 U.S. global-role survey | Foreign-public reception, U.S. overall judgment, U.S. partisan/generational meaning | Dated triggering event, government response, alliance coordination, market/aid behavior | Baseline audience and interpretation layer |
| European Parliament Research Service, February 2026 | Analyst assessment of transatlantic reliability uncertainty across NATO, Ukraine, trade, technology, climate, and China | Public respondent denominator, event attribution, changed alliance behavior | Candidate event-window and field-definition context |
| Poland F-35 | Arrival, formal acceptance, first-pilot training, reported eight-aircraft threshold | Full readiness, sustainment, public/allied/adversary response, changed strategic behavior | Capability-realization comparator |
| Poland JASSM-ER | Authorization, procurement agreement, planned delivery windows, technology-sensitivity modification | Shipment, acceptance, fielding, inventory, operational use, external response | Non-observation and realization watchpoint |
| Poland Piorun/SAFE | Framework agreement, first executive contract, reported allied buyers, prior Norway handover, Lithuanian procurement-stage follow-up | Country-level quantities, SAFE attribution, delivery/acceptance, supplier dependence, durable external behavior | Strongest retained procurement-response candidate, still agreement/delivery-stage |
| Polish defense-financing opinion | Dated public judgment about SAFE and alternative financing routes, with ideological splits | Event attribution, later vote/action, procurement behavior, delivery, and policy durability | Public-consent layer, not behavior or leverage |
| Poland/E5 defense ministers, February 2026 | Joint language on NATO deterrence, hybrid threats, Ukraine support, defense-industrial cooperation, and allied infrastructure | Whether any commitment changed because of the F-35 milestone; implementation, spending, or operational follow-through | Pre-event alliance/context window |
| NATO Ankara declaration, July 2026 | Alliance commitment, new procurements, collective manufacturing, eastern-flank capability, and Ukraine assistance commitments | Country-level attribution, F-35-specific effect, delivery/use, public consent, and changed Russian or allied behavior | Post-event alliance/context window |
| Poland airspace violation, September 2025 | Article 4 consultation, Polish and allied aircraft/air-defense participation, and NATO solidarity statement | Attribution to any one capability, longer-term deterrence, Russian adaptation, and later public/policy durability | Genuine response-endpoint comparator, not an F-35 result |
| Virginia large-load/grid projects | Regulatory response, route decision, modeled cost allocation, related project energization | Household bill, resident acceptance, reliable service, replaceability, external response | Domestic legitimacy/capacity comparator |

## Next lawful acquisition

Choose one dated policy, conflict, alliance, aid, trade, or capability event
with country-level public reception and a traceable response record. The first
useful outcome is not a higher opinion score; it is one of:

- alliance coordination or refusal;
- aid acceptance, redesign, or rejection;
- procurement, supplier, or market substitution;
- diplomatic concession, retaliation, or policy change; or
- a documented domestic political action tied to the event.

Compare at least one exposed country with a plausible alternative or comparator
and preserve country, party, and time denominators separately. Do not pool the
Pew country median with U.S. respondents or join it to a procurement record by
date alone. For the Poland candidate, treat the E5 statement and Ankara
declaration as response-window context until a source identifies what actor
changed what behavior because of the F-35 milestone rather than the broader
security environment.

## Stop conditions

- Do not call public approval legitimacy-in-action.
- Do not call a contract or arrival leverage.
- Do not infer alliance behavior from analyst commentary.
- Do not treat a missing public response as evidence that no response occurred.
- Do not acquire restricted public-opinion microdata or diplomatic records
  without permitted access and a defined estimand.

**Related records:** [three-audience global-role layer](pew-2026-us-global-role-domestic-partisan-international-comparison-layer-v1.md), [capability-legitimacy clock synthesis](capability-legitimacy-clock-synthesis-v1.md), [strategic realization protocol](realization-ledger-protocol-v1.md).

**Candidate official sources:** [Poland E5 defense-minister statement, 20 February 2026](https://www.gov.pl/web/national-defence/strengthening-allied-relations-and-the-will-to-act-within-the-e5-group); [NATO Ankara Summit Declaration, 8 July 2026](https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2026/07/08/the-ankara-summit-declaration); [Polish F-35 acceptance record, 12 June 2026](https://www.gov.pl/web/obrona-narodowa/samoloty-f-35-na-wyposazeniu-wojska-polskiego); [Polish Piorun SAFE framework](https://www.gov.pl/web/obrona-narodowa/kolejne-ppzr-piorun-dla-armii-tym-razem-zakup-z-programu-safe); [Polish Piorun executive-contract update](https://www.gov.pl/web/premier/polski-przemysl-obronny-przyspiesza-dzieki-safe); [CBOS defense-financing opinion](https://www.cbos.pl/PL/publikacje/flashe_tekst.php?nr=11%2F2026).
The [NATO Poland airspace-incident statement, 10 September 2025](https://www.nato.int/en/news-and-events/events/transcripts/2025/09/10/statement) is retained as the response-endpoint comparator.

## Promotion disposition

The NATO incident is not promoted into the canonical portfolio in
this pass. It has a well-defined observed response, but it is a separate
airspace-violation case rather than a response to the F-35, Piorun, or SAFE
milestones. Keeping it here preserves the response comparator without
silently creating a cross-case causal arrow or inflating the reader with a
duplicate geopolitical finding. Promote it only if a later pass defines the
incident as its own country/Alliance case and adds the incident-to-response
source set, counterfactual/comparator, and later durability fields.
