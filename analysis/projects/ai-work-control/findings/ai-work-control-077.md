# Identifier ambiguity blocks facility attribution in the defense supplier case

**Status:** bounded procurement-identity audit · **Checked:** 2026-09-14

**Subsequent correction:** a richer USAspending award-search route later
exposed UEI and location fields for all 74 rows. This finding remains an audit
of the sparse `/subawards/` response; the corrected end-to-end result is
[Finding 078](ai-work-control-078.md).

## The finding

The official USAspending recipient endpoint can return UEIs and recipient
identifiers for a name, but a name search is not the same thing as an exact
join from a particular subaward row to a particular facility.

For the two named recipients examined in the JASSM/LRASM extract:

- the exact BAE name returned **17 USAspending recipient rows representing 10
  distinct UEIs** across parent/child levels and DUNS histories;
- the DLA CAGE record for the Merrimack BAE facility displays UEI
  `SL2KEMFACM69`, but that UEI did not appear in the returned USAspending rows
  for the same name query;
- the exact General Dynamics-OTS name returned **three USAspending UEIs**;
- the three selected DLA facility records display UEIs
  `JCUNVL6B1QJ8`, `Q9SBTF8ELUP4`, and `C9JJM67GNFZ1`; only `Q9SBTF8ELUP4`
  overlapped the name-query result.

This is not evidence that the records contradict one another. The USAspending
recipient endpoint is a broad recipient search with aggregate values, while
the retained subaward rows contain only recipient name, description, date, and
amount. The result is a measurement boundary: **legal-entity and facility
identity cannot be assigned to the selected subaward action by name alone.**

```text
subaward row: name + component description + date + amount
       |
       +-- name search -> several USAspending UEIs / parent-child records
       |
       +-- DLA CAGE lookup -> one or more facility CAGE/UEI records
       |
       `-- [open] exact row-to-UEI/CAGE join -> plant assignment -> output/delivery
```

## What the audit establishes

| Question | Result | Safe interpretation |
|---|---:|---|
| BAE USAspending name-search rows | 17 | Multiple identifier histories/recipient levels appear under the same displayed name |
| BAE distinct UEIs in USAspending response | 10 | A name search does not select the Merrimack facility or one legal-entity record |
| BAE DLA facility UEI in CAGE 81J97 | `SL2KEMFACM69` | Official facility identity, not an observed join to the subaward |
| General Dynamics-OTS USAspending UEIs | 3 | The name maps to multiple recipient identifiers in the broad endpoint |
| General Dynamics DLA selected-facility UEIs | `JCUNVL6B1QJ8`, `Q9SBTF8ELUP4`, `C9JJM67GNFZ1` | Three active facility records under the parent route |
| Exact subaward-to-facility assignment | Not observed | The current public row lacks UEI/CAGE and cannot establish plant work |

The USAspending result also carries aggregate endpoint amounts. Those amounts
are useful for discovering identifier candidates, but they are not the
$210.0 million BAE or $80.6 million General Dynamics-OTS amount in the single
JASSM/LRASM subaward extract. Mixing the two denominators would manufacture a
false reconciliation.

## Why this matters for the end-to-end geopolitical question

The program is trying to follow a defense commitment through industrial
capacity and, eventually, usable state capability and external response. That
chain requires more than knowing that a corporate name appears in a federal
record:

1. identify the exact legal entity behind the award action;
2. assign it to a facility or production location;
3. identify the component or work package;
4. observe workforce, production, acceptance, delivery, and maintenance;
5. test qualified alternatives, switching cost, or an observed response.

The new audit strengthens step 1 only partially and shows why step 2 cannot be
skipped. A parent group can contain multiple UEIs, CAGE facilities, DUNS
histories, and recipient-level records. Conversely, a facility can have a
current DLA identity that is not exposed in the retained subaward response.

## Counterinterpretations kept visible

- The USAspending name query may include historical, parent, child, or
  unrelated contract records outside this one JASSM/LRASM award.
- A missing UEI in the subaward response does not mean the supplier lacks an
  identifier; it means this retained endpoint response did not expose one.
- An overlapping UEI is not proof that the selected subaward was performed at
  the corresponding facility.
- A non-overlap may reflect identifier vintage, recipient normalization,
  address changes, or a different legal entity—not foreign control or missing
  production.
- Aggregate recipient amounts are not facility revenue, component value, or
  delivered capability.

## Next decisive acquisition

The next pass should obtain an identifier-bearing USAspending transaction or
award-performance record for the selected subaward numbers, then reconcile the
identifier to SAM/DLA location and component records. If the public API cannot
expose that join, the atlas should record the limitation explicitly and seek a
contractor, award-file, audit, or production/acceptance source that names both
the work package and facility.

## Sources and reproduction

- [USAspending recipient reconciliation response](../data/usaspending-recipient-reconciliation-2026-09-14.json)
- [USAspending JASSM/LRASM subaward extract](../data/usaspending-jassm-lrasm-subawards-2026-09-13.json)
- [DLA BAE facility record](../data/dla-cage-81j97-bae-iesi-2026-09-13.json)
- [DLA General Dynamics-OTS records](../data/dla-cage-3x552-general-dynamics-ots-2026-09-13.json), [Colchester](../data/dla-cage-05606-general-dynamics-ots-2026-09-13.json), [Saco](../data/dla-cage-26978-general-dynamics-ots-2026-09-13.json)
- [USAspending recipient API documentation](https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/recipient.md)
- [Acquisition script](../../../../scripts/fetch_usaspending_recipient_reconciliation.py)

**Evidence status:** official identifier-search audit; exact subaward-to-facility
assignment, production, delivery, replaceability, and geopolitical response
remain open.
