# SIPP SNAP transition reason layer v1

**Checked:** 2026-09-14
**Source:** 2025 SIPP public-use file and official 240-replicate-weight file; 2024 reference year
**Unit:** identified person, adjacent reference-month SNAP transition
**Method:** Fay BRR with `G = 240` and perturbation factor `0.5`; descriptive only

## Bounded result

Among 437 observed no-to-yes transition pairs, 217 had a classified entry
reason. The largest recorded entry categories were job loss, layoff, or wages
reduced (30.10%; SE 3.94 pp; 95% CI 22.38–37.83), other income loss or
reduction (15.72%; SE 3.13), and becoming disabled or unable to work (10.67%;
SE 2.56). The `other` category was 23.33% (SE 3.43), so the listed categories
do not form a complete mechanism account.

Among 387 observed yes-to-no transition pairs, 188 had a classified exit
reason. Income increased and the person became ineligible was 32.40% (SE 4.26
pp; 95% CI 24.04–40.75), while `other` was 49.53% (SE 4.34). Time limit
reached was 6.21% (SE 2.14), and benefits not worth the trouble was 2.15% (SE
1.10). The entry and exit taxonomies are distinct and should not be compared
as if they were symmetric response choices.

## Interpretation boundary

The reason fields add a respondent-recorded mechanism layer between a monthly
status transition and the broader material/work context. They do not supply a
dated notice, exact benefit amount, administrative case record, provider or
employer response, alternative resources, or later recovery. A reason is not a
causal exposure, and a monthly transition is not a complete benefit spell.

The classified cells are subsets of all observed transitions. Missing or
unclassified reasons remain part of the audit and are not assigned to `other`.
The `other` response itself is a recorded category, not an analyst-imputed
residual.

## Reproduction

```text
python3 scripts/analyze_sipp_snap_transition_reason_fay_brr.py \
  --primary /path/to/sipp-household-slice.csv \
  --replicate-zip /path/to/rw2025_csv.zip \
  --output /tmp/sipp-snap-transition-reasons-fay-brr.json
```

The v16 rerun read 379,215 primary rows and 378,291 replicate rows; 405
classified transition pairs matched the replicate archive. Input and output
hashes and the full transition counts are preserved in the [reproduction
audit](sipp-snap-transition-reasons-reproduction-audit-2026-09-14.json).

Related layers: [transition context](sipp-snap-transition-context-fay-brr-layer-v1.md),
[following context](sipp-snap-following-context-reproduction-audit-2026-09-14.json),
and the [machine-readable record](../../records/us-sipp-snap-transition-reasons-2024.json).

## Next test

Join recorded reason categories to notice, effort, benefit amount, household
composition, food/housing outcomes, and later re-entry where compatible
timing and units exist. The same-episode interpretation, remedy, trust, and
political-action fields remain open.
