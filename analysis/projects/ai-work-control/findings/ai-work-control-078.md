# A richer award-search route closes the recipient join—but not the production join

**Status:** bounded procurement-to-entity/location bridge · **Checked:** 2026-09-14

## The correction and advance

The first USAspending subaward response used in this case contains 74 rows with
recipient name, description, date, amount, and subaward number, but no UEI or
location. That sparse response made an exact row-to-entity join appear open.

The official USAspending award-search endpoint provides a richer subaward view
when called with `subawards=true` and the subaward-specific fields. Re-running
the same parent-award case returned all 74 rows with a subrecipient UEI,
recipient location, and primary place of performance.

For the two focal rows, the bridge is now observed:

| Subaward | Recipient | UEI | Recipient location | Description boundary |
|---|---|---|---|---|
| `4106451402` | BAE Systems Information and Electronic Systems Integration Inc. | `V7X9P6J9SUK1` | Nashua, New Hampshire | RFS antenna / RF sensor procurement-control drawing; the row does not name a plant or prove manufacture |
| `4106475970` | General Dynamics-OTS, Inc. | `KZK8C85C1T94` | Niceville, Florida | Case assembly loaded-live, Lots 22–26; the row does not identify the production line, output quantity, acceptance, or delivery |

This corrects the earlier boundary without erasing it: the basic endpoint is
still sparse, but the official search route makes the subaward-to-UEI and
subaward-to-recipient-location links observable. The next bridge is harder:
the USAspending location is not automatically a DLA CAGE facility, production
site, or delivery event.

```text
parent award
  -> subaward row + component description + amount/date
  -> UEI + recipient location                 [now observed]
  -> CAGE/facility/work-package assignment    [still open]
  -> production, acceptance, delivery         [still open]
  -> maintenance, alternatives, response      [still open]
```

## What the richer response establishes

- **Coverage:** all 74 returned subaward rows have a subrecipient UEI, a
  recipient location, and a primary place of performance in this response.
- **BAE:** the selected $210,018,575 row maps to UEI `V7X9P6J9SUK1` and a
  USAspending recipient location in Nashua, NH.
- **General Dynamics-OTS:** the selected $80,550,804.12 row maps to UEI
  `KZK8C85C1T94` and a USAspending recipient location in Niceville, FL.
- **CAGE relationship:** neither row is yet assigned to a specific CAGE record
  in the retained evidence. The earlier selected BAE CAGE route points to
  Merrimack, NH and the selected General Dynamics-OTS CAGE set points to
  Hampton, AR; Colchester, VT; and Saco, ME. Those are not interchangeable
  with the USAspending recipient-location fields.

The geography difference is analytically useful, not an error to smooth away.
It may reflect a registered recipient address, a different operating site, a
historical identifier, data normalization, or a facility not yet acquired in
the DLA pass. It does not prove that Nashua or Niceville manufactured the
listed item, nor that Merrimack or one of the three selected CAGE sites did.

## Why this matters for capability and power

This moves the case from an anonymous name/amount surface to an identifiable
recipient and place. That supports better tests of local workforce, industrial
concentration, and geographic dependence. It still does not show usable
capability. A recipient address can be administrative; a primary place of
performance can be a reporting field; and a component description can be a
procurement label rather than a completed production record.

The end-to-end geopolitical proposition therefore remains conditional. To claim
that the award created resilient or leverage-bearing capability, the program
must still observe the work package at a facility, production or acceptance,
delivery/fielding, maintenance or inventory, and a qualified alternative or
external response.

## Counterinterpretations kept visible

- Nashua and Niceville may be recipient or reporting locations rather than
  manufacturing locations.
- The CAGE records acquired so far are comparison routes, not a complete search
  of every facility attached to the new UEIs.
- A subaward description can name a component or assembly without establishing
  quantity, completion, acceptance, or fielding.
- Geographic dispersion may create continuity, or all locations may share a
  parent, tooling, certification, software, or critical input.
- A visible UEI makes a join possible; it does not make the resulting claim
  causal or operational.

## Next decisive acquisition

Resolve `V7X9P6J9SUK1` and `KZK8C85C1T94` against DLA/SAM facility records and
then locate a performance, acceptance, delivery, contractor, or audit record
that names both the work package and physical site. Preserve the recipient
location, primary place of performance, CAGE address, and actual production
site as separate fields until the records agree.

## Sources and reproduction

- [Richer USAspending subaward response](../data/usaspending-jassm-lrasm-rich-subaward-search-2026-09-14.json)
- [Sparse USAspending subaward response](../data/usaspending-jassm-lrasm-subawards-2026-09-13.json)
- [DLA BAE facility route](../data/dla-cage-81j97-bae-iesi-2026-09-13.json)
- [DLA General Dynamics-OTS facility routes](../data/dla-cage-3x552-general-dynamics-ots-2026-09-13.json), [Colchester](../data/dla-cage-05606-general-dynamics-ots-2026-09-13.json), [Saco](../data/dla-cage-26978-general-dynamics-ots-2026-09-13.json)
- [Official USAspending award-search contract](https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/search/spending_by_award.md)
- [Acquisition script](../../../../scripts/fetch_usaspending_rich_subaward_search.py)

**Evidence status:** exact subaward-to-UEI and subaward-to-reported-location
links observed for all 74 rows; facility assignment, production, acceptance,
delivery, replaceability, and geopolitical response remain open.
