# SIPP utility pressure does not yield a usable monthly buffer transition

**Status:** local field-timing and transition gate · **Checked:** 2026-09-16  
**Source:** 2025 SIPP public-use file, 2024 reference period  
**Unit tested:** identified person, adjacent reference-month pair

## Why this gate was run

The broad program needs an end-to-end route from a material condition to the
options available when a household responds. The existing local SIPP slice
contains utility-payment difficulty, credit-balance, and savings-account
fields. This gate tested whether the latter two could be followed from month
*t* to month *t+1* with the 240-replicate Fay–BRR archive.

```text
utility-payment condition at month t
  -> credit-balance or savings state at month t+1
  -> buffer movement and recovery [test failed at the field-timing gate]
```

## Result

The analyzer read 379,215 primary rows, identified 31,874 person units, and
matched 294,145 adjacent-month keys to the replicate archive. There were
24,289 eligible pairs in the utility-difficulty group and 321,766 in the
no-difficulty group.

| Utility condition at *t* | Outcome at *t+1* | Valid pairs | Weighted share | Valid state changes |
|---|---|---:|---:|---:|
| Difficulty | Credit/store-card balance = yes | 19,080 | 35.23% (SE 1.51 pp) | 0 |
| Difficulty | Savings account = yes | 19,080 | 46.48% (SE 1.61 pp) | 0 |
| No difficulty | Credit/store-card balance = yes | 275,065 | 26.91% (SE 0.36 pp) | 0 |
| No difficulty | Savings account = yes | 275,065 | 64.91% (SE 0.42 pp) | 0 |

The zero-change result is the decisive gate outcome. The fields can be read at
the following month, but no valid adjacent pair changes state. They therefore
cannot identify whether utility pressure was followed by borrowing, saving,
liquidation, repayment, or another buffer response. The next-month level
shares are retained only as a diagnostic and are not a new trend estimate.

## Interpretation boundary

This does not show that households never change credit or savings position. It
shows that these particular public-use fields, as extracted in the 2024
reference-year SIPP slice, do not provide the required monthly transition. The
fields may be annual or repeated household-status measures, and account
ownership does not reveal balance, liquidity, payment success, or service
continuity.

The result also does not establish that utility difficulty caused the
conditional level differences. The person-record rows repeat household fields
and are not household-prevalence estimates. Fay–BRR intervals describe the
sampling-design uncertainty of the level diagnostics; they cannot repair the
missing state movement or event timing.

## What this changes in the broad goal

This gate closes one tempting but invalid route:

```text
utility difficulty at t -> monthly credit/savings movement at t+1
```

The broader material/time/care route remains active through the existing
utility/tenure/work and utility/care/food/housing screens, but its stronger
financial-buffer arrow requires a dated bill, account transaction, shutoff or
assistance event, or an authenticated panel with genuine state movement. This
is a useful negative result because it prevents a repeated status field from
being mistaken for household adaptation or recovery.

## Reproduction

```text
python3 scripts/analyze_sipp_utility_buffer_following.py \
  --primary /tmp/us-broad-sipp-2025/full-v18/sipp-household-slice.csv \
  --replicate-zip /tmp/rw2025_csv.zip \
  --output /tmp/us-broad-sipp-2025/full-v18/utility-buffer-following.json
```

The new analyzer is intentionally not registered as a promoted trend record:
it is a field-timing gate and produces no usable state-transition estimate.
The [reproduction audit](sipp-utility-buffer-following-reproduction-audit-2026-09-16.json)
preserves the local row counts, hashes, and zero-change result.
The existing [utility/credit/savings diagnostic](../us-household-financial-pressure/findings/us-household-financial-pressure-006.md)
remains the authoritative same-month comparison.

**Evidence status:** local reproducibility and field-timing gate passed; usable
monthly buffer transition, dated bill, causal ordering, liquidity, recovery,
remedy, trust, and political-action arrows remain open.
