# SHED care-foregoing persistence reproduction audit

**Checked:** 2026-09-16  
**Status:** reproduced from existing local artifacts; no new download

## Result

The 2024–2025 SHED care-foregoing transition analysis was rerun from the
local public-use ZIPs and reproduced the canonical path frame and published
weighted results. The rerun retained 4,419 paired respondents:

| 2024 → 2025 path | Paired respondents |
|---|---:|
| No → No | 2,976 |
| No → Yes | 327 |
| Yes → No | 444 |
| Yes → Yes | 672 |

Selected 2025 adaptation estimates matched the canonical record: reduced
savings was 28.734%, 59.665%, 44.497%, and 65.334% across those four paths;
medical debt was 7.192%, 30.366%, 19.116%, and 41.783%; delayed major
purchase was 31.964%, 62.952%, 51.988%, and 76.442%.

## Reproduction command

```text
python3 scripts/analyze_shed_panel_care_foregoing_paths.py \
  --old /tmp/cgtm-shed/shed2024.zip \
  --new /tmp/cgtm-shed/shed2025.zip \
  --output /tmp/shed-panel-care-foregoing-reproduction.json
```

Local input and script hashes:

```text
SHED 2024: b455d02356a0c01a02d7f478c02d772515491564e905ce13db55f272f83567c1
SHED 2025: a4ab3f7d042f16d63626b1af9aeb6f0b8a0b39e412fa94b87265bc67fe26de14
script:     9219c16e378bd280a044c74401319a8529eef625ef033b9bd5e6de3cd1abb2c8
```

## Interpretation boundary

This validates a same-respondent annual transition, not a dated bill or
clinical episode. Care foregoing, financial adaptation, and health remain on
source-specific clocks; the result does not establish causality, care
completion, recovery, remedy, trust, or political action.
