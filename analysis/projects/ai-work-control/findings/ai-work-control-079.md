# Reported subaward locations have real capability context—but not a proven JASSM production assignment

**Status:** bounded facility-capability context pass · **Checked:** 2026-09-14

## The finding

The richer USAspending response identifies the selected BAE subaward at a
recipient location in Nashua, New Hampshire, and the selected General
Dynamics-OTS subaward at a recipient location in Niceville, Florida. A new
official-source pass finds capability context at those same locations:

- BAE Systems' official quality certificate lists **95 Canal Street, Nashua**
  among certified sites for the design, production, and servicing of electronic
  components, subsystems, and systems for military and commercial products.
- General Dynamics-OTS's official product material identifies **Niceville
  Operations, 115 Hart Street**, and describes advanced warhead technology and
  modeling/simulation capabilities.

This is a meaningful bridge from “reported address” to “documented industrial
capability.” It is still not a production assignment. Neither source says that
the specific JASSM/LRASM subaward row was performed at the site, that the
listed item was completed there, or that the output was accepted or delivered.

```text
subaward row -> UEI/location                 [observed]
location -> documented industrial capability [now contextualized]
location -> this exact work package          [not observed]
work package -> accepted/delivered capability [not observed]
capability -> alternative or external response [not observed]
```

## Evidence table

| Case | Procurement observation | Official capability context | What remains unproven |
|---|---|---|---|
| BAE | Subaward `4106451402`, UEI `V7X9P6J9SUK1`, $210,018,575, reported recipient location 95 Canal St, Nashua, NH; description references RFS antenna/RF sensor procurement-control drawing | BAE certificate US014595 lists 95 Canal Street, Nashua as a certified military-electronics design/production/servicing site | That this row’s RF work occurred there, the quantity completed, acceptance, delivery, or facility-specific workforce |
| General Dynamics-OTS | Subaward `4106475970`, UEI `KZK8C85C1T94`, $80,550,804.12, reported recipient location 115 Hart St, Niceville, FL; description references case assembly loaded-live, Lots 22–26 | General Dynamics-OTS product material identifies Niceville Operations at 115 Hart Street and presents advanced warhead technology/modeling capabilities | That this JASSM/LRASM case assembly was performed there, the output accepted or delivered, or that the site is independently replaceable |

The source types are deliberately kept separate. USAspending is the award
record. The BAE certificate is a quality-scope document. The GD-OTS document is
company product/capability material. Their geographic overlap makes a facility
assignment plausible enough to investigate, not strong enough to report as
observed.

A secondary public CAGE aggregation currently reports likely identifier leads:
BAE UEI `V7X9P6J9SUK1` with CAGE `7P325`, and General Dynamics-OTS UEI
`KZK8C85C1T94` with CAGE `4R854`. These are retained as discovery leads only;
the official DLA detail response has not yet been retrieved for these two
candidate records, so they are not promoted to the machine-readable facility
join.

## Why it matters for the end-to-end chain

This closes a useful middle layer. Industrial capability is no longer inferred
only from a corporate name or a generic location; each site has an independent
documented capability signal. That supports a more serious test of whether a
procurement relationship creates domestic capacity, specialized dependence, or
geographic concentration.

But the geopolitical claim remains conditional. A capability brochure or
quality certificate does not show current line utilization, the specific
contract's work allocation, production rate, accepted quantity, delivery,
maintenance, or a buyer's ability to switch. The next decisive evidence must
be a production, acceptance, delivery, audit, contract attachment, or facility
record that joins the work package to the site.

## Counterinterpretations kept visible

- A certified site can support a capability without performing every product or
  every contract associated with the legal entity.
- A company product document can describe organizational capability rather than
  the exact production run or current capacity.
- A recipient location can be an administrative or reporting address even when
  the company has capability there.
- Shared parent ownership, tooling, certification, or inputs can make several
  sites look geographically redundant while remaining operationally dependent.
- Even a confirmed site assignment would not by itself prove delivery,
  readiness, replaceability, or geopolitical leverage.

## Next decisive acquisition

Seek a site-specific contract attachment, manufacturing/quality record, audit,
acceptance or delivery notice, or official facility statement that names the
JASSM/LRASM work package or the relevant antenna/case assembly. Then compare
the dated production/acceptance record with the award modification and Poland
delivery watchpoint before making a capability or leverage claim.

## Sources and reproduction

- [Richer USAspending subaward response](../data/usaspending-jassm-lrasm-rich-subaward-search-2026-09-14.json)
- [BAE official quality certificate, US014595](https://www.baesystems.com/en-us/dam/jcr%3A7ea82997-4d3a-4b47-852e-540a196824a2/AS9100D-ISO9001-2015-BVC-multi-site-cert-US014595-1-exp-05-07-2023.2025-06-27-16-16-52.pdf) · retrieval SHA-256 `d667a22fa28687e07b3c2e800966757369c66e73173a199756e781a2d1bd0b5c`
- [General Dynamics-OTS official Advanced Warhead Technology material](https://www.gd-ots.com/wp-content/uploads/2023/02/Advanced-Warhead-Technology-202301-1.pdf) · retrieval SHA-256 `7ec9756d27ce13ef1cae81b21ccf05583d16e9f3b9a140aba95d32f8e46f4486`
- [DLA BAE facility route](../data/dla-cage-81j97-bae-iesi-2026-09-13.json)
- [DLA General Dynamics-OTS facility routes](../data/dla-cage-3x552-general-dynamics-ots-2026-09-13.json), [Colchester](../data/dla-cage-05606-general-dynamics-ots-2026-09-13.json), [Saco](../data/dla-cage-26978-general-dynamics-ots-2026-09-13.json)
- [Secondary BAE CAGE discovery record](https://cage.report/CAGE/7P325) · [secondary General Dynamics-OTS CAGE discovery record](https://cage.report/SAM/8EAU4) — discovery only, not an official DLA-detail promotion

**Evidence status:** reported subaward locations now have independent capability
context; exact work-package assignment, production, acceptance, delivery,
replaceability, and geopolitical response remain open.
