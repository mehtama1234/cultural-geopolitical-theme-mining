# Official entity records compress the apparent defense supplier network—but not the capability question

**Status:** bounded procurement-entity reconciliation · **Checked:** 2026-09-14

## The bounded finding

The JASSM/LRASM subaward extract names suppliers at the recipient level, while
official DLA CAGE records expose a different structure: legal entities, active
facility identifiers, and parent-company links. For two visible comparison
routes, the public records show:

- BAE Systems Information and Electronic Systems Integration Inc. in Merrimack,
  New Hampshire, linked to BAE Systems, Inc. in Falls Church, Virginia, and then
  to BAE Systems plc in London;
- General Dynamics-OTS facilities in Hampton, Arkansas, Colchester, Vermont,
  and Saco, Maine, linked to General Dynamics Corp in Reston, Virginia.

This changes the unit of analysis. **A list of recipient names is not a list of
independent suppliers, and a corporate parent is not proof of facility output
or replaceability.**

```text
reported recipient name
  -> legal entity and CAGE/UEI
  -> facility and corporate-parent hierarchy
  -> [open] assigned work, workforce, inputs, production, delivery
  -> [open] substitution, operational capacity, alliance leverage
```

## What the public records establish

| Route | Publicly resolved structure | Evidence boundary |
|---|---|---|
| BAE | CAGE 81J97 / Merrimack, NH → CAGE 1BNT5 / BAE Systems, Inc. / Falls Church, VA → CAGE U2D80 / BAE Systems plc / London | Exact entity and displayed parent links; not proof that every subaward action occurred in Merrimack or that the parent controls the production step in question |
| General Dynamics-OTS | CAGE 3X552 / Hampton, AR; 05606 / Colchester, VT; 26978 / Saco, ME → CAGE 95403 / General Dynamics Corp / Reston, VA | Multiple active facility records under one parent; not proof that the selected case-assembly work was assigned to any particular facility |
| Parent-award context | USAspending extract reports 74 returned subaward records and 51 recipient names; BAE IESI is the largest reported named recipient at $210.0M, while General Dynamics-OTS is reported at $80.6M in the selected profile | Amounts and names remain bounded extract fields; CAGE records are not a retroactive join to every transaction |

The BAE route is especially important because it prevents two opposite errors.
The entity is not accurately described as simply a domestic standalone supplier,
but the public record also does not justify calling the reported work
uncontrolled foreign production. The observed structure is a US operating entity
inside a UK-headquartered group, with the DLA parent links and a separately
documented US security-control arrangement. That is jurisdictional and control
context, not a production or leverage estimate.

The General Dynamics route supplies a counterexample to a different shortcut:
several facility records can exist under one US parent. Geographic spread may
help with continuity, but it does not by itself show independent ownership,
substitutability, spare capacity, or assignment of the reported subaward.

## What this adds to the state-capacity chain

The earlier concentration result showed that 51 reported recipient names can
coexist with a large amount share held by a smaller group of names. This entity
pass adds the next measurement layer: **name diversity must be reconciled to
legal-entity and facility structure before it can be interpreted as industrial
redundancy.**

It still does not close the chain. The public CAGE records do not supply the
component-to-facility assignment, workers, production rate, accepted quantity,
delivery, maintenance, inventory, critical-input dependence, or a qualified
substitute. Nor do they show a state changing its negotiation, alliance, or
external behavior because of the observed structure.

## Counterexamples kept visible

- A corporate group can contain technically distinct and geographically spread
  facilities that are genuinely substitutable.
- A single parent can coordinate facilities that appear geographically diverse
  but share software, tooling, certification, or critical inputs.
- A small legally distinct supplier can be strategically irreplaceable even if
  its award amount is small.
- A displayed parent link is an entity record, not proof of effective control
  over every contract, plant, or component.
- A domestic address does not establish domestic content, local jobs, or local
  public benefit.

## Next decisive test

Join the recipient's exact UEI/CAGE to the USAspending transaction or subaward
record, then assign each action to a facility and component class. Follow the
case through production start, workforce, acceptance, delivery, maintenance,
inventory, and an alternative-supplier or qualification record. Only after
that should the program test whether a supplier structure created usable
continuation, a credible switch, or an observed alliance/geopolitical response.

## Sources and reproduction

- [USAspending JASSM/LRASM subaward extract](../data/usaspending-jassm-lrasm-subawards-2026-09-13.json)
- [USAspending recipient profile](../data/usaspending-jassm-lrasm-subaward-profile-2026-09-13.json)
- [BAE CAGE 81J97 record](../data/dla-cage-81j97-bae-iesi-2026-09-13.json)
- [BAE Systems, Inc. parent record](../data/dla-cage-1bnt5-bae-systems-inc-2026-09-13.json)
- [BAE Systems plc parent record](../data/dla-cage-u2d80-bae-systems-plc-2026-09-13.json)
- [General Dynamics-OTS CAGE records](../data/dla-cage-3x552-general-dynamics-ots-2026-09-13.json), [Saco](../data/dla-cage-26978-general-dynamics-ots-2026-09-13.json)
- [General Dynamics Corp parent record](../data/dla-cage-95403-general-dynamics-corp-2026-09-13.json)
- [Machine-readable entity-reconciliation record](../../../records/us-defense-procurement-entity-parent-facility-reconciliation-2026.json)

**Evidence status:** official entity and parent-record reconciliation for a
small comparison set; production, delivery, replaceability, local incidence,
and geopolitical leverage remain open.
