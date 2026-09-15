# SIPP SNAP stable-state and child-care constraint bridge v1

**Checked:** 2026-09-13  
**Reference period:** 2024, from the 2025 SIPP release  
**Unit:** identified person; November-to-December SNAP status paired with annual fall child-care fields  
**Status:** descriptive Fay-BRR comparison; no program effect claimed

## What this adds

The SIPP transition layers already show that SNAP receipt status, recorded
transition reason, and following material hardship are separate stages. This
bridge adds a care/work constraint to the same person's status comparison. It
uses the November-to-December transition because `EPAY`, `EPAYHELP`, and
`EWORKMORE` describe child-care conditions during the reference year's fall;
they are not monthly December outcomes.

## Stable-state comparison

| Annual fall child-care measure | No SNAP in Nov → Dec | SNAP in Nov → Dec |
|---|---:|---:|
| Paid child care | 31.0% (SE 1.3; n=1,783) | 23.9% (SE 3.1; n=259) |
| Received child-care assistance | 5.2% (0.7; n=1,783) | 14.6% (2.6; n=259) |
| Child-care arrangements prevented work or more work | 3.4% (0.4; n=2,295) | 7.4% (1.9; n=351) |

The continued-receipt cell therefore does not describe a single “protected”
condition. It has lower reported paid child care but higher reported
assistance and work constraint. That pattern is compatible with different
eligibility, household composition, employment, income, care needs, and
subsidy arrangements. It is not evidence that SNAP caused the constraint or
that nonreceipt means security.

The entry and exit cells are sparse for these annual child-care fields: only
three to four valid records for entry and two for exit, depending on the
measure. They remain open and are not interpreted as transition estimates.

## Definitions and limits

- `EPAY` asks whether the reference parent or family paid for child care during
  a typical week of the fall reference period.
- `EPAYHELP` asks whether the reference parent received assistance to pay for
  child care.
- `EWORKMORE` asks whether child-care arrangements prevented the reference
  parent from working or working more during the fall reference year.
- Each field has a separate universe and denominator; invalid or out-of-universe
  values are not recoded as “no.”
- The comparison has no notice comprehension, route effort, benefit amount,
  care quality, exact monthly timing, trust, or political-action measure.

## Reproduction

```text
python3 scripts/analyze_sipp_snap_transition_childcare_bridge.py \
  --primary /path/to/sipp-household-slice.csv \
  --replicate-zip /path/to/rw2025_csv.zip \
  --output /tmp/sipp-snap-childcare-bridge.json
```

The [machine-readable record](../../records/us-sipp-snap-stable-state-childcare-2024.json)
preserves the source and artifact hashes, transition counts, valid universes,
Fay-BRR standard errors, sparse-cell boundary, and counterinterpretations.

Related: [SNAP transition × following hardship](sipp-snap-transition-outcome-fay-brr-layer-v1.md),
[SNAP transition reason/outcome](sipp-snap-transition-reason-outcome-fay-brr-layer-v1.md),
and the [same-episode ledger implementation](same-episode-event-ledger-implementation-v1.md).
