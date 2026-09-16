# SIPP SNAP reason-to-food-security reproduction audit

**Checked:** 2026-09-16  
**Status:** reproduced from existing local artifacts; no new download

## Result

The SNAP transition-reason analysis was rerun from the local v18 derived SIPP
slice and the existing 240-replicate archive. It reproduced the published
frame: 379,215 primary rows, 378,291 replicate rows, 437 entry pairs, 387
exit pairs, 217 classified entry pairs, 188 classified exit pairs, and 405
classified pairs matched to replicate weights.

The aggregate food-security estimates reproduced to the displayed precision:

| Classified transition | Valid food-security records | Low/very low food security |
|---|---:|---:|
| Entry | 188 | 26.12% (SE 3.82 pp) |
| Exit | 160 | 18.87% (SE 3.51 pp) |

The largest reason cells also reproduced: entry after job/wage loss was
22.94% (SE 6.38 pp), entry after disability was 31.73% (SE 14.51 pp), exit
for income increase was 25.69% (SE 7.38 pp), and exit for “other” reasons was
14.20% (SE 4.40 pp).

## Reproduction command

```text
python3 scripts/analyze_sipp_snap_reason_outcome_fay_brr.py \
  --primary /tmp/us-broad-sipp-2025/full-v18/sipp-household-slice.csv \
  --replicate-zip /tmp/rw2025_csv.zip \
  --output /tmp/sipp-snap-reason-outcome-reproduction.json
```

The local input hashes were:

```text
primary v18 slice: 4fe7395d4ecdb2f1a3f2879a394f47d1e809c9bdef3960b60543919b79a61eda
replicate archive: 3bf35c17723de10697d581d1122fda4d7cdecb34c6f9e9dfcb18ddc561c7c6b6
analysis script:   07afd9b96d5c844e4e0afb84ebb92f80acfe2590bd8a45c6ff1005f93c09c9c4
```

## Interpretation boundary

This verifies the computation, not a SNAP program effect. Reason categories
are missing for part of the transition frame, food security has its own valid
universe and reference period, and the following month is record order rather
than proof of bill or benefit timing. The result does not observe notice,
effort, benefit amount, gap days, remedy, substitution, recovery, trust, or
political action.
