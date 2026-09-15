# MEPS 2024 event-linkage audit v1

**Checked:** 2026-09-15  
**Status:** person/event key gate passed; timing boundary identified  
**Scope:** HC-256 person file plus 2024 office, prescription, emergency-room, and inpatient files

## Result in one line

The 2024 MEPS event files can be linked exactly to HC-256 person records by
`DUPERSID` and `PANEL`, and the office, emergency-room, and inpatient files
carry complete plausible calendar timing. The prescription file has a unique
purchase key and exact person linkage, but its available date fields describe
medication start timing and are valid for only 65,563 of 204,550 records
(32.05%), so it cannot yet serve as a complete purchase-date episode clock.

## Linkage surface

| File | Records | Unique event keys | Person-panel matches | Date surface | Payment field |
|---|---:|---:|---:|---|---|
| HC-254G office | 145,818 | 145,818 | 100% | 145,818 valid event dates, 2024 | `OBSF24X` |
| HC-254A prescription | 204,550 | 204,550 | 100% | 65,563 valid medication-start dates, 32.05%; 2022–2024 | `RXSF24X` |
| HC-254E emergency room | 4,351 | 4,351 | 100% | 4,351 valid event dates, 2024 | `ERFSF24X` |
| HC-254D inpatient | 1,912 | 1,912 | 100% | 1,912 valid start dates, 2023–2024 | `IPFSF24X` |

HC-256 contains 19,140 unique person-panel keys and 18,683 records with a
positive `PERWT24F`. No duplicate event keys were observed in any of the four
event files. The event-to-person checks count event records, so a person with
multiple events contributes multiple successful matches; this is an identity
check, not a person-level prevalence estimate.

## What this makes possible

The public-use MEPS architecture now supports a defensible first stage of an
episode ledger:

```text
person and panel key
  -> unique event key
  -> event type and payment field
  -> event date for office, emergency, or inpatient care
  -> HC-256 coverage, income, health, work, and annual expenditure context
```

This is stronger than an annual aggregate because the person/event join and
several event clocks are explicit. It allows a future pass to compare the
observed payment channel and event type with person-level coverage, work,
health, and resource fields while keeping the event universe separate from
people who had no recorded event.

The inpatient start year extending into 2023 is retained rather than silently
forcing every event into calendar 2024. The file’s full-year event population
and its start-date window must remain distinct from the 2024 person file’s
annual observation.

## What this does not make possible

The key join is not a complete household episode. The public-use fields
audited here do not establish that a recorded payment caused a care choice,
that the person delayed care before appearing in an event file, or that a
household borrowed, drew savings, missed work, supplied unpaid care, changed
food or housing consumption, recovered, complained, switched, or changed
political judgment afterward.

The prescription date fields are especially limited: they are medication
start month/year fields with MEPS special codes, not a complete transaction
date for every purchase. A prescription purchase can therefore be linked to a
person and payment without being treated as a fully dated bill event.

## Reproduction

The audit is reproduced by:

```text
python3 scripts/audit_meps_event_linkage.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  /tmp/cgtm-meps-2024/events/h254g.dta \
  /tmp/cgtm-meps-2024/events/h254a.dta \
  /tmp/cgtm-meps-2024/events/h254e.dta \
  /tmp/cgtm-meps-2024/events/h254d.dta
```

Exact linkage uses `DUPERSID` and `PANEL`. Event uniqueness uses `EVNTIDX` for
office, emergency-room, and inpatient events and `RXRECIDX` for prescriptions.
Valid calendar dates require a year from 1900 through 2024 and a month from 1
through 12; this excludes MEPS negative special codes.

## Next decisive test

The next pass should use the exact person/event key to build a bounded office,
emergency, or inpatient episode extract with coverage, payment, event date,
annual work and health fields, and explicit missing episode fields. It should
then test whether the available MEPS round variables provide a usable
before/after window. If they do not, the result should be promoted as a
measurement boundary and paired with SHED or SIPP only as contextual evidence,
not as a fabricated same-household follow-up.
