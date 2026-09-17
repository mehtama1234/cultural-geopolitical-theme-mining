# SIPP utility-to-time-loss gate reproduction recheck

**Checked:** 2026-09-16  
**Status:** exact local reproduction; no new estimate or download

## Recheck result

The utility-difficulty to childcare-related time-loss gate was rerun from the
retained v18 SIPP slice and the existing 240-replicate archive. The output
matches the committed machine-readable result exactly for the reported
results object.

| Integrity surface | Recheck result |
|---|---:|
| Primary rows read | 379,215 |
| Eligible positive-weight November–December pairs | 27 |
| Replicate pairs matched | 27/27 |
| Result cells reproduced | 4/4 |
| Utility-difficulty pairs | 7 total (4 owner/buyer; 3 renter) |
| No-difficulty pairs | 20 total (12 owner/buyer; 8 renter) |

The reproduced weighted means are 1.000 hours for difficulty/owner-buyer,
1.515 hours for difficulty/renter, 1.232 hours for no-difficulty/owner-buyer,
and 1.487 hours for no-difficulty/renter. These are conditional means among
respondents who also satisfy the `EWORKMORE=1` and valid `ETIMELOST` universe;
they are not average childcare time loss for households, parents, renters, or
owners.

## Interpretation boundary confirmed

The rerun strengthens computation integrity but does not strengthen the causal
arrow. `EAWBGAS` is reported utility-payment difficulty, not a dated bill,
arrears, shutoff, or assistance decision. `ETIMELOST` is a fall-reference-year
childcare time-loss measure asked only after work prevention is reported. The
official universe provides no comparable time-loss measure for respondents who
did not report work prevention, and only seven selected cases report utility
difficulty. The gate therefore cannot estimate utility-caused time loss or a
tenure burden gradient.

The correct next acquisition remains a dated utility or care-provider episode
with bill/notice timing, alternative care or family support, schedule control,
protected and sacrificed outcomes, remedy, and later recovery for the same
person or family.

## Reproduction command

```text
python3 scripts/analyze_sipp_utility_time_loss.py \
  --primary /tmp/us-broad-sipp-2025/full-v18/sipp-household-slice.csv \
  --replicate-zip /tmp/rw2025_csv.zip \
  --output /tmp/sipp-utility-time-loss-current.json
```

The local v18 slice hash is
`4fe7395d4ecdb2f1a3f2879a394f47d1e809c9bdef3960b60543919b79a61eda` and the
replicate archive hash is
`3bf35c17723de10697d581d1122fda4d7cdecb34c6f9e9dfcb18ddc561c7c6b6`.
The output was written under `/tmp` and no raw or derived bulk file was added
to Git.

See the [time-loss gate](sipp-utility-time-loss-following-gate-v1.md) and the
[machine-readable record](data/sipp-utility-time-loss-following-2024.json).
