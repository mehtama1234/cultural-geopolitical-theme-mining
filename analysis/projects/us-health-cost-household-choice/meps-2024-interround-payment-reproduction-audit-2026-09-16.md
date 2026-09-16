# MEPS 2024 inter-round payment follow-up reproduction audit

**Checked:** 2026-09-16  
**Status:** reproduced from existing local artifacts; no new download

## Result

The strict inter-round payment-band follow-up was rerun from the locally
available MEPS 2024 HC-256 person file, HC-256 BRR file, HC-254E emergency-room
file, and HC-254D inpatient file. The rerun reproduced the canonical sample
sizes, payment bands, weighted estimates, and BRR uncertainty values used by
the [payment-band finding](findings/us-health-cost-household-choice-004.md).

| Check | Reproduced value |
|---|---:|
| HC-256 person records | 19,140 |
| Valid round-ordered person records | 18,930 |
| ER strict-window people | 1,108 |
| Inpatient strict-window people | 552 |
| ER $0 / under $100 / $100+ people | 765 / 99 / 244 |
| Inpatient $0 / under $100 / $100+ people | 343 / 34 / 175 |

Selected weighted follow-up results also match: ER fair/poor health is
30.3419% in the zero-payment band and 17.8123% in the $100+ band; ER bill
problems are 14.2771% and 18.1149%, respectively. Inpatient fair/poor health
is 36.0782% and 25.3373%; inpatient bill problems are 11.7733% and 9.5820%.

## Reproduction command

```text
python3 scripts/analyze_meps_interround_payment_followup.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  /tmp/cgtm-meps-2024/h36brr/h36brr24.dta \
  --emergency-room-file /tmp/cgtm-meps-2024/events/h254e.dta \
  --inpatient-file /tmp/cgtm-meps-2024/events/h254d.dta \
  --output /tmp/meps-interround-payment-reproduction.json
```

The local input hashes match the hashes recorded in the canonical record:

```text
h256: b4bde859b39f626345561c05570292bb7264dd92eb76ce0c1a14d6b89076aed5
brr:  44f1e5a864c1d318327a0fbd3a0ff48a583c74c3a104aae357032cfbfaa5a32e
HC-254E: 23071ad1ffa7a2abf46721f4388be6b462f2fc6413dbef8323282db276081723
HC-254D: 5a71c7680f11ebb7dfc5e579ea8b63e6fb090b2ff2eb9a943c7abccdc13cb464
script: f1436fdcf39f71550f901e626c06e5e2209080db0b0e937221b9383b371c5fcf
```

## Interpretation boundary

This verifies the computational result, not a causal explanation. Family-paid
amount is an event-level contribution, not a complete bill or household
obligation. Zero payment may reflect coverage, payer mix, imputation, or
payment coding. Event severity and selection remain. The layer still does not
observe the dated need, feasible alternative, borrowing or savings response,
treatment continuity, recovery, remedy, trust, political action, or
geopolitical consequence.
