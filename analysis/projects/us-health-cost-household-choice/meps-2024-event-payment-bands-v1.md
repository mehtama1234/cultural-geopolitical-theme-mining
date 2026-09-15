# MEPS 2024 event payment bands separate payment from later bill and health context

**Checked:** 2026-09-15  
**Status:** weighted descriptive first-event screen; no causal claim  
**Machine record:** [event payment-band data](data/us-meps-2024-event-payment-bands.json)

## Result

The first valid office, emergency-room, or inpatient event for a person can be
linked exactly to the MEPS 2024 person file and divided by self/family payment
band. This adds resolution to the existing event ledger: it tests whether a
larger recorded event payment corresponds to a larger follow-up bill-problem,
health, work, or practical-financial-room share within the same event family.

The result is still not an affordability estimate. Event payment excludes
unobserved premiums, deductibles, unpaid family time, transport, denied care,
and bills from other events. The follow-up fields are annual/round context and
may include the event itself or prior conditions.

## Reading rule

Use the machine-readable table to compare payment bands within an event family,
not to compare office, emergency, and inpatient means as if their populations
were interchangeable. Each family has a separate first-event universe. A
pattern that rises across payment bands is compatible with payment-linked
burden, but also with severity, payer mix, age, selection, and service
composition. A flat or reversed pattern is a useful counterexample, not proof
that payment was harmless.

The first-event extract supplies a direct counterexample to treating payment as
a simple burden score. In the emergency-room universe, the zero-payment band
has 27.45% fair/poor follow-up health and 14.52% follow-up bill problems,
compared with 13.34% and 12.47% in the $2,000+ band. In the inpatient universe,
the corresponding fair/poor health shares are 35.25% and 26.54%. These are
selection patterns: zero payment may reflect payer protection, while the
event population may differ sharply in severity, age, disability, or prior
condition. They do not show that paying more improved health or that paying
nothing removed household burden.

The HC-256 file also carries round 4/2 financial-well-being context. The
payment-band output reports confidence paying an unexpected expense, missed
loan/credit payments, debt-collector contact, medical debt, late rent, and
unpaid utilities. These fields make the practical-room stage more explicit,
but they remain temporally broader than the first event and should not be read
as consequences of that event.

In the emergency-room first-event universe, 24.65% of the zero-payment band
was not at all or not too confident about paying an unexpected expense,
compared with 4.32% of the $2,000+ band. Medical debt moved in the opposite
direction in this comparison: 20.68% versus 32.99%. The two measures together
are a useful counterexample to a single burden interpretation. Zero payment
can coexist with less financial room, while a high payment band can contain
people with greater medical debt but more capacity to meet an unexpected bill.
Both patterns may be driven by selection, payer protection, severity, and
resources rather than the displayed event payment.

```text
first dated event
  -> self/family payment band
  -> bounded bill, health, work, and financial-room context
```

The missing arrows remain care continuation or foregoing, feasible alternative,
household payment timing, debt, unpaid care, remedy, trust, and action.

## Reproduction

```text
python3 scripts/analyze_meps_event_payment_bands.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  --office-file /tmp/cgtm-meps-2024/events/h254g.dta \
  --emergency-room-file /tmp/cgtm-meps-2024/events/h254e.dta \
  --inpatient-file /tmp/cgtm-meps-2024/events/h254d.dta \
  --output analysis/projects/us-health-cost-household-choice/data/us-meps-2024-event-payment-bands.json
```

## Sources and boundary

The source is AHRQ’s [MEPS 2024 HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256), joined to the [office HC-254G](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254G&prfricon=yes), [emergency-room HC-254E](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254E&prfricon=yes), and [inpatient HC-254D](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254D&prfricon=yes) files by `DUPERSID + PANEL`.

This screen advances the payment-to-context arrow only. It does not convert a
payment band into household welfare or complete the end-to-end goal.
