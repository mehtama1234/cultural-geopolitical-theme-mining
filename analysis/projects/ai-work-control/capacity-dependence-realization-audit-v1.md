# Capacity and dependence realization-stage audit v1

**Status:** stage-coverage audit; no capability, autonomy, or leverage estimate  
**Checked:** 2026-09-20
**Cases:** US data-center capacity/governance and Poland JASSM-ER procurement  
**Machine-readable audit:** [capacity/dependence realization audit](data/capacity-dependence-realization-audit-v1.json)

## Question

The broader program asks when an announced strategic objective becomes usable
capacity, who controls it, who bears its costs, and whether another actor's
options actually change:

```text
objective or demand
  -> authorization/agreement
  -> named capacity and place
  -> delivery, operation, or accepted output
  -> control, maintenance, and replaceability
  -> public/partner outcome
  -> changed external behavior or leverage
```

The local ledgers allow this chain to be audited without treating every dated
record as the same kind of realization.

## Cross-case result

| Case | Observed or planned stages | Still not established |
|---|---|---|
| US data centers | Modeled national demand; local capacity/revenue; utility governance; two large-load drop events; customer-response records; comparator and non-observation records | Facility-level operating load tied to public cost, household/business incidence, ownership, replaceability, reliable service outcome, and public legitimacy |
| Poland JASSM-ER | Possible-sale authorization; procurement agreement; planned 2026–2030 delivery; technology-sensitivity modification; broad official report of JASSM-ER family equipment delivered since 2022 | The prior-delivery report has no quantity, receiving unit, acceptance record, or link to the 2024 order; current-order production, shipment, acceptance, training/fielding, inventory, operational availability, substitution, and external response remain open |

The shared pattern is not “capacity failed” or “capacity succeeded.” It is
that commitments and some intermediate realization signals are visible before
the endpoints that make capacity politically meaningful: accepted output,
replaceability, distributional incidence, and changed behavior.

## Stage counts from the local ledgers

The machine audit classifies event types into comparable analytical stages;
this classification is a reading aid, not a new source claim.

| Case | Events | Commitment | Capacity/operation | Delivery/operation | Governance/external response | Missing-stage record |
|---|---:|---:|---:|---:|---:|---:|
| US data centers | 13 | 0 | 5 | 2 | 4 | 1 |
| Poland JASSM-ER | 13 | 3 | 0 | 4 (1 planned; 3 comparator milestones) | 0 | 1 |

The counts are not quantities, readiness scores, or comparable performance
rates. The data-center ledger has operating-stress and customer-response
events without a complete named-facility service outcome. The JASSM-ER ledger
has an authorization/agreement and planned delivery but no public record in
this packet proving shipment or acceptance of the specific 2024 order.

The 2026-09-20 rerun also preserves a useful comparator boundary: the ledger
contains separate F-35 arrival and official-acceptance milestones, but those
events do not upgrade the JASSM-ER order to shipped, accepted, trained, or
operational. A public acceptance trail is evidence about what a realized
capability record would look like, not evidence that another program reached
the same stage.

## Mechanism boundary

The most defensible current finding is:

> Strategic capacity becomes institutionally visible before its public,
> replaceability, and geopolitical consequences are fully observable.

For the data-center case, the next decisive join is facility or large-load
account → actual energized load → utility cost and reliability → affected
customer/public outcome → alternative or renegotiation. For the defense case,
it is order identifier → production/shipment → acceptance/training/fielding →
maintenance and inventory → substitution or partner/external response.

Neither chain should borrow evidence from the other. County revenue is not
missile delivery; a procurement agreement is not local operating load.

The critical-materials extension adds a third realization boundary. GAO/USGS
can identify import reliance, China exposure, application-specific substitution
limits, recycling horizons, and federal research response, but a domestic
award or prototype is not qualified output, a second source, or reduced
geopolitical dependence. The correct unit is the
`mineral–application–process–firm` chain, followed through qualification,
volume, cost, switching, and an observed external response.

## Current official procurement recheck

The Polish Ministry of National Defence's current public JASSM-ER page still
describes the May 2024 agreement and a **2026–2030 delivery window**. The
official route does not identify shipment, acceptance by a Polish unit,
training completion, operational availability, or a changed external actor's
behavior for the specific order. The procurement therefore remains an
observed commitment and planned-delivery stage, not a verified operational
capability or geopolitical-leverage endpoint.

A second Polish MOD announcement describes the same program more specifically
as having **first deliveries planned for 2026**. That is a planned milestone,
not a delivery record: the reviewed public material still does not identify a
shipment, receiving unit, acceptance, training, inventory change, or
operational use.

The public record does contain a separate baseline signal: a 2023 Polish
Senate response lists JASSM-ER among equipment delivered to Poland since
February 2022. That supports a family-level prior-delivery proposition, but it
does not identify quantity, date, receiving unit, acceptance, or a connection
to the May 2024 order. The audit therefore separates **existing family-level
capability** from **realization of the current order**.

An older Polish Ministry page gives a more concrete but still separate
baseline: it reports that the first JASSM missiles had been delivered to the
Poznań-Krzesiny F-16 base in January 2017, while separately describing the
December 2016 JASSM-ER agreement. This confirms historical platform-level
integration for the JASSM family, not shipment, acceptance, or operational
availability of the May 2024 JASSM-ER order.

The public record also provides a useful separate comparator: the Polish
National Security Bureau reports that the first three F-35 aircraft landed at
Łask on 22 May 2026 and that an official acceptance ceremony occurred on 12
June 2026. The [machine-readable F-35 comparator ledger](data/poland-f35-husarz-arrival-acceptance-event-ledger-v1.json)
preserves that arrival-to-acceptance trail. This shows what a public
arrival-to-acceptance trail can look like, but it is not evidence about the
JASSM-ER order and does not establish training completion or full operational
availability.

**Current official-source recheck — 2026-09-20:** a fresh search of the Polish
Ministry of National Defence's JASSM-ER page found no newer public shipment,
receiving-unit, acceptance, training, inventory, or operational-use record for
the May 2024 order. The page still states that deliveries are planned for
2026–2030. This is a dated public-record non-observation, not evidence that no
delivery has occurred; it keeps the order at planned-delivery rather than
realized-capability status.

A separate Ministry statement from August 2026 says that not all elements of
Poland's wider integrated air-defence system had yet been delivered and that
some systems would arrive in 2026, 2027, or later. It does not identify the
JASSM-ER order, so it is contextual timing evidence only; it cannot be used as
proof of shipment, acceptance, or fielding for this specific procurement.

Sources: [Polish Ministry of National Defence JASSM-ER page](https://www.gov.pl/web/obrona-narodowa/jassm-er),
checked 2026-09-20; [Polish Senate response listing equipment delivered since February 2022](https://www.senat.gov.pl/download/gfx/senat/pl/senatoswiadczenia/4507/10_057_2065_1_odp.pdf),
checked 2026-09-19; [2017 Polish Ministry JASSM delivery page](https://www.gov.pl/web/obrona-narodowa/pociski-jassm-dla-f-16-2), checked 2026-09-19; [August 2026 integrated air-defence statement](https://www.gov.pl/web/obrona-narodowa/wicepremier-wladyslaw-kosiniak-kamysz-budujemy-wielowarstwowa-i-zintegrowana-obrone-polskiego-nieba),
checked 2026-09-19; [Polish MOD first-delivery announcement](https://www.gov.pl/web/obrona-narodowa/nowoczesne-pociski-dalekiego-zasiegu-jassm-er-dla-wojska-polskiego), checked 2026-09-19; [Polish National Security Bureau F-35 arrival and acceptance record](https://www.bbn.gov.pl/pl/wydarzenia/10408,Prezydent-RP-na-ceremonii-przyjecia-samolotow-F-35-quotHusarzquot.html), checked 2026-09-19.

## Reproduction and storage boundary

```text
python3 scripts/audit_capacity_dependence_realization_ledgers.py
```

The audit reads the two existing local JSON ledgers, downloads nothing, and
does not infer household incidence, operational readiness, replaceability,
strategic autonomy, or geopolitical leverage.
