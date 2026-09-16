# Utility difficulty, tenure, and child-care work prevention v1

**Status:** bounded SIPP time/care conditional comparison  
**Checked:** 2026-09-16
**Source:** 2025 SIPP public-use file, 2024 reference period  
**Unit:** identified reference-parent person record; annual fall child-care work-prevention report conditioned on December utility difficulty and tenure  
**Method:** `WPFINWGT` with 240 Fay-BRR replicate weights, `G=240`, perturbation factor `0.5`

## Why this pass matters

The utility/tenure work layer showed different next-month work-movement
surfaces. This pass adds a compatible care field without pretending that it is
a monthly bill response. It asks whether the annual SIPP report that child-care
arrangements prevented work or additional work is more common inside reported
utility-payment difficulty, and whether the descriptive surface differs by
housing tenure.

```text
utility condition + tenure at December
        -> annual fall child-care arrangement prevented work or more work
        -> time, income, and household room [open]
```

## Results

The percentages are person-weighted conditional shares. Parentheses contain
Fay-BRR standard errors in percentage points; intervals are approximate 95%
design-based intervals.

| Utility condition | Tenure | Valid records | Child-care arrangements prevented work or more |
|---|---|---:|---:|
| Difficulty | Owned/bought | 105 | 9.35% (3.11), CI 3.26–15.44 |
| Difficulty | Rented | 146 | 8.13% (2.43), CI 3.37–12.89 |
| No difficulty | Owned/bought | 1,677 | 2.84% (0.53), CI 1.80–3.87 |
| No difficulty | Rented | 673 | 5.01% (0.91), CI 3.22–6.80 |

The descriptive pattern is consistent with less available room among the
utility-difficulty reference-parent cells, but the small difficulty cells have
wide intervals and the care report is annual. Within reported difficulty,
renter and owner/buyer estimates overlap substantially. Outside difficulty,
renters report more work prevention than owners/buyers, but that contrast is
not a tenure effect.

## Measurement and uncertainty

The analysis reads 379,215 primary rows and matches 2,601 selected records in
the replicate archive. The key is
`SSUID + PNUM + SPANEL + SWAVE + MONTHCODE`, restricted to `MONTHCODE=12`.
The extracted slice exposes `ETENURE` but no separate `ATENURE` status flag;
the analysis therefore retains the released tenure response and records this
schema boundary rather than treating a missing flag as positive validation.

`EWORKMORE` belongs to the reference-parent and fall child-care universe. It
does not measure monthly care hours, the exact utility bill, a shutoff threat,
or the timing of a work decision. The four cells have separate valid
universes, and the difficulty cells are small enough that the interval—not
the point estimate alone—should guide interpretation.

## What this adds to the atlas

- It puts a time/care outcome beside the utility and tenure surface while
  preserving the official annual reference-year universe.
- It shows that a higher reported work-prevention share is concentrated in the
  utility-difficulty cells, but does not turn that alignment into a causal
  utility or housing claim.
- It supplies a more precise next-pass target: a dated bill or service event
  linked to care time, work schedule, health, and recovery.

## Counterexamples and boundaries

- A household may report no utility difficulty and still lack child-care
  alternatives or lose time elsewhere.
- A utility-difficulty respondent may have child-care work prevention because
  of labor demand, illness, family composition, or provider failure rather
  than the bill condition.
- Tenure is a bundle of payment, repair, insurance, neighborhood, family, and
  mobility conditions; it is not an intervention.
- `EWORKMORE` is a reported annual fall measure, not a dated event or monthly
  time-loss estimate.

## Next decisive test

The stronger test remains a same-person event design that records a dated bill,
shutoff, reconnection, or provider-assistance event, then follows work hours,
unpaid care, health, housing stability, and recovery at one-, three-, and
six-month windows. The authenticated PSID backbone remains the preferred route
for a richer family-level design.

## Reproduction

```text
python3 scripts/analyze_sipp_utility_tenure_childcare.py \
  --primary /tmp/us-broad-sipp-2025/full-v18/sipp-household-slice.csv \
  --replicate-zip /tmp/rw2025_csv.zip \
  --output /tmp/sipp-utility-tenure-childcare-v18.json
```

The [machine-readable record](../../records/us-sipp-utility-tenure-childcare-2024.json)
preserves the source, replicate, output, and script hashes. The [parent
utility/tenure work layer](sipp-utility-work-tenure-following-layer-v1.md)
preserves the adjacent-month work transition. The [reproduction audit](sipp-utility-tenure-childcare-reproduction-audit-2026-09-16.json)
records the current v18 rerun and matching conditional cells.

**Evidence status:** estimated descriptive conditional bridge with design-based
uncertainty. No causal utility, tenure, care, household-security, health,
trust, political-action, or geopolitical claim is made.
