# MEPS 2024 creates a bounded dated health-cost episode surface

**Checked:** 2026-09-15  
**Status:** descriptive episode-surface result; no causal household claim  
**Machine record:** [MEPS 2024 episode surface](data/us-meps-2024-episode-surface.json)

## Result in one line

The 2024 MEPS public-use files can connect dated office, emergency-room, and
inpatient events to the same person-panel key used by the consolidated person
file. The resulting surface carries annual insurance, poverty, work, health,
and medical-bill-problem fields with complete nonmissingness among the valid
event rows audited here. It is a usable event-to-person bridge, but it is not
yet a bill-to-care-choice-to-recovery panel.

## What was assembled

```text
HC-254 event record
  -> exact DUPERSID + PANEL key
  -> HC-256 INSURC24 / POVCAT24 / FAMINC24 / EMPST53 / RTHLTH53 / PROBPY42
  -> event date and event-specific self/family and total payment
```

The aggregate output contains no person identifiers or row-level records. It
retains event counts, unique people, linkage checks, date coverage, payment
means, zero-payment counts, and context-field completeness.

| Event surface | Valid event records | Unique people | Event date | Weighted self/family payment | Weighted total payment |
|---|---:|---:|---|---:|---:|
| Office-based provider | 144,206 | 14,198 | 2024 | $57.38 | $308.05 |
| Emergency room | 4,261 | 2,868 | 2024 | $148.22 | $1,405.11 |
| Inpatient stay | 1,881 | 1,391 | 2023–2024 | $865.20 | $18,892.70 |

All event rows matched HC-256 by `DUPERSID + PANEL`, all event identifiers were
unique, and the five annual context fields were nonmissing for 100% of valid
rows in each surface. The inpatient start-year range includes 2023 and is
preserved rather than being relabeled as a 2024-only event population.

The payment means reproduce the earlier event analyses because facility and
doctor payment components are summed for emergency-room and inpatient events.
The event file’s `PERWT24F` is used for payment means; event-record counts are
not presented as person prevalence.

## What this adds to the end-to-end program

This closes a meaningful middle layer:

```text
observed care event
  -> exact person identity
  -> event date
  -> payment channel
  -> annual coverage, resources, work, health, and bill-problem context
```

That is stronger than placing annual MEPS spending beside a separate survey.
It permits a future bounded comparison of event type and payment with the
person’s observed annual context while preserving the event’s own universe.
It also makes the missing fields concrete: the current public-use surface
does not show whether the person delayed this event, what alternatives were
available, whether the household borrowed or drew savings, whether unpaid
care or missed work followed, or whether the person recovered or changed
trust, use, or political behavior.

## Interpretation boundary

The higher inpatient and emergency payment means describe different event
surfaces and selection, not a household burden ranking. A zero self/family
payment event can reflect coverage, payment assignment, or edited expenditure
fields; it does not prove that care was affordable or that no other cost was
paid in time, transport, premiums, unpaid care, or foregone alternatives.

Annual `EMPST53`, `RTHLTH53`, `POVCAT24`, and `PROBPY42` values are context
fields, not automatically post-event outcomes. They do not establish that an
event caused work change, health change, poverty status, or trouble paying
medical bills. The same-year relation is temporal context, not an identified
before/after effect.

Prescription records remain outside this bounded surface because their
available medication-start date is not a complete transaction-date field for
all purchases. Their person key and payment fields are usable for a separate
purchase surface, but not for a fully dated purchase episode without an
additional timing rule.

## Next test

The next pass should select one event family—preferably office or emergency
care—and inspect MEPS round-level health, coverage, employment, and perceived-
health fields for a valid pre/post window. The promotion rule is strict: only
fields with a documented round date and a compatible denominator may be called
follow-up outcomes. If no such window exists, this artifact should remain the
correct endpoint and be paired with SHED or SIPP as contextual evidence only.

The unresolved target remains:

```text
dated need or event
  -> care decision and available alternative
  -> payment and time/work/debt response
  -> recovery or persistence
  -> institutional remedy, trust, action, or exit
```

This pass closes the identity/date/payment/context segment, not the full chain.
