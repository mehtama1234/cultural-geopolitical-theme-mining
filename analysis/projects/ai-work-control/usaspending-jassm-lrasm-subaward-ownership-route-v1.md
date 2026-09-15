# USAspending JASSM/LRASM subaward ownership route v1

**Checked:** 2026-09-13  
**Unit:** largest reported subordinate recipient in one parent award  
**Status:** ownership/jurisdiction reconciliation lead; not a leverage finding

## What the route establishes

The subaward extract for parent award `FA868224CB001` reports **BAE SYSTEMS
INFORMATION AND ELECTRONIC SYSTEMS INTEGRATION INC.** as the largest named
subordinate recipient, with **$210,018,575**, or **18.3798%** of the returned
subaward amount. The extract itself supplies no UEI, DUNS, incorporation
country, ownership, location, or control-rights fields.

BAE Systems plc's 2025 annual-report materials list BAE Systems Information
and Electronic Systems Integration Inc. among the Group's subsidiary
undertakings and state that the Group's subsidiary undertakings are held at
100% by the Group, with the report identifying BAE Systems plc as a UK company.
The same reporting materials describe the Electronic Systems business as
US- and UK-based and state that BAE Systems, Inc. and the US Government use a
Special Security Agreement for the ownership and control of US defence
businesses. This means the evidence supports a more precise description than
either “purely domestic supplier” or “uncontrolled foreign supplier”: a US
incorporated/operating subordinate entity appears within a UK-headquartered
corporate group subject to a US security-control arrangement.

## Why this matters to the end-to-end chain

```text
US defense allocation
  -> Lockheed Martin prime award
  -> reported subordinate component recipient
  -> corporate ownership and security-control arrangement
  -> [open] plant, workers, inputs, delivery, and local incidence
  -> [open] capability, substitution, alliance behavior, or external response
```

The ownership route changes the question from “is the award US-owned?” to
“which legal entity, corporate parent, jurisdiction, and security-control
arrangement govern each reported supplier?” It does not establish where the
reported components were made, who employed the workers, how profits or risks
were distributed, whether the supplier is replaceable, or whether any actor
changed behavior.

## Reproduction and source boundary

The procurement numerator and recipient identity are reproduced from the
[raw subaward extract](data/usaspending-jassm-lrasm-subawards-2026-09-13.json)
and its [profile](data/usaspending-jassm-lrasm-subaward-profile-2026-09-13.json).
The corporate-structure and security-control claims use the official
[BAE Systems 2025 annual-report materials](https://www.baesystems.com/annualreport/2025)
and the linked FY2025 annual report. The report's complete subsidiary schedule
is a large linked report artifact; direct binary retrieval was not retained in
the repository during this pass, so this memo does not claim an independently
parsed legal-entity database. The ownership conclusion should be rechecked
against the next annual report and, for each supplier, a legal-entity or
procurement-registration record.

**Next test:** resolve UEI/DUNS and incorporation/control fields for the top
reported recipients; join them to plant geography, employment, component
descriptions, contract modifications, and delivery/acceptance records without
equating corporate ownership with local benefit or operational readiness.

The official [GSA SAM.gov Entity Management API documentation](https://open.gsa.gov/api/entity-api/)
confirms that public entity queries require a SAM.gov account and public API
key. No such key is present in this environment, and the unauthenticated route
does not return an entity record. This is an acquisition dependency, not
evidence that the reported recipients lack registrations or UEIs.

The SAM.gov website/internal search route was also tested without a key using
the recipient name. Its response returned general opportunity/exclusion search
results and did not provide a stable entity-registration record that could be
assigned to this subaward. Because that internal route is not the documented
Entity Management API and its index behavior is not an entity-resolution
contract, it is retained as a negative capability test rather than as evidence
about the supplier.

As a discovery lead only, a public CAGE-data aggregator reports candidate
identifiers for this exact name, including CAGE `81J97`, UEI `SL2KEMFACM69`,
DUNS `081048710`, and a Merrimack, New Hampshire location. A second record for
the same name reports CAGE `8M6A5` and a Fort Wayne, Indiana location. Because
the aggregator is not the authoritative SAM/DLA record and the same name maps
to multiple records, these identifiers are deliberately **not assigned** to
the USAspending subaward. The ambiguity itself is evidence that recipient-name
matching cannot establish plant geography or local incidence.

Discovery references: [CAGE 81J97](https://cage.report/CAGE/81J97), [CAGE 8M6A5](https://cage.report/CAGE/8M6A5).

## Official CAGE reconciliation

The public [DLA CAGE detail route](https://cage.dla.mil/Search/Details?id=10332512)
was subsequently retrieved for CAGE `81J97`. It displays the exact
USAspending recipient name, UEI `SL2KEMFACM69`, an active status, the address
`21 Continental Blvd, Merrimack, NH 03054-4303`, and linked parent CAGE `1BNT5`
(`BAE SYSTEMS, INC.`). The raw response and retrieval hash are preserved in
[`data/dla-cage-81j97-bae-iesi-2026-09-13.json`](data/dla-cage-81j97-bae-iesi-2026-09-13.json),
and the fetch is reproducible with:

```text
python3 scripts/fetch_dla_cage_detail.py \
  --cage 81J97 \
  --output analysis/projects/ai-work-control/data/dla-cage-81j97-bae-iesi-2026-09-13.json
```

This materially strengthens the legal-entity and facility path, but the
USAspending record still lacks the UEI/CAGE field needed for an exact
machine-level join. The current link is an exact legal-name reconciliation
with an official CAGE record, not proof that every reported subaward action
was performed at Merrimack or that the facility supplied all listed items.

The linked parent CAGE `1BNT5` was also resolved through the official DLA
route. It displays **BAE SYSTEMS, INC.**, UEI `MJDNAS47MHP6`, active status, a
Falls Church, Virginia address, and parent CAGE `U2D80` for **BAE SYSTEMS PLC**.
The parent response is preserved at
[`data/dla-cage-1bnt5-bae-systems-inc-2026-09-13.json`](data/dla-cage-1bnt5-bae-systems-inc-2026-09-13.json).
The resulting hierarchy is therefore:

```text
BAE Systems plc (parent CAGE U2D80)
  -> BAE Systems, Inc. (parent CAGE 1BNT5; Falls Church, VA)
    -> BAE Systems Information and Electronic Systems Integration Inc.
       (CAGE 81J97; Merrimack, NH)
```

This hierarchy is an entity/control map, not a revenue, profit, employment,
component-flow, or facility-output map.

## Comparison hierarchy: General Dynamics-OTS

The comparison supplier's three selected active CAGE records—`3X552` (Hampton,
AR), `05606` (Colchester, VT), and `26978` (Saco, ME)—all display General
Dynamics Corp as parent CAGE `95403`. The official parent record displays
**GENERAL DYNAMICS CORP**, UEI `VF58HFRNGEL8`, active status, and a Reston,
Virginia address. Its raw response is preserved at
[`data/dla-cage-95403-general-dynamics-corp-2026-09-13.json`](data/dla-cage-95403-general-dynamics-corp-2026-09-13.json).

```text
General Dynamics Corp (CAGE 95403; Reston, VA)
  -> General Dynamics-OTS, Inc.
     -> CAGE 3X552 (Hampton, AR)
     -> CAGE 05606 (Colchester, VT)
     -> CAGE 26978 (Saco, ME)
```

The parallel hierarchy strengthens the finding that corporate parentage and
facility geography are separate analytical layers. It still does not identify
which plant performed the reported case-assembly subaward.

The BAE parent CAGE `U2D80` was also resolved through DLA. It displays **BAE
SYSTEMS PLC**, active status, and `6 Carlton Gardens, London, Greater London
SW1Y 5AD, United Kingdom`; no UEI is displayed. The response is preserved at
[`data/dla-cage-u2d80-bae-systems-plc-2026-09-13.json`](data/dla-cage-u2d80-bae-systems-plc-2026-09-13.json).
The BAE chain is therefore grounded in public entity records from the
Merrimack operating entity through the Falls Church US subsidiary to the
London parent, while the General Dynamics chain terminates at its US parent
record. This is jurisdictional context, not proof of effective control over
the reported subaward's production or delivery.
