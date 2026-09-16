# SHED coverage-to-care-foregoing reproduction audit

**Checked:** 2026-09-16  
**Status:** reproduced from existing local artifacts; no new download

## Result

The 2024–2025 SHED coverage-transition analysis was rerun from the existing
local public-use ZIPs. The rerun reproduced the canonical 4,419-person paired
universe and all four coverage-path cells:

| 2024 → 2025 coverage path | Paired respondents |
|---|---:|
| Insured → insured | 3,964 |
| Insured → uninsured | 158 |
| Uninsured → insured | 115 |
| Uninsured → uninsured | 182 |

The rerun also reproduced the published care-path estimates. The insured →
insured path had 6.739% care-foregoing entry and 14.527% persistence; the
insured → uninsured path had 13.012% entry and 19.531% persistence; the
uninsured → insured path had 17.221% entry and 22.498% persistence; and the
uninsured → uninsured path had 13.760% entry and 37.347% persistence.

## Reproduction command

```text
python3 scripts/analyze_shed_panel_care_foregoing_paths.py \
  --old /tmp/cgtm-shed/shed2024.zip \
  --new /tmp/cgtm-shed/shed2025.zip \
  --output /tmp/shed-panel-coverage-care-foregoing-reproduction.json
```

Local input, script, and output hashes:

```text
SHED 2024: b455d02356a0c01a02d7f478c02d772515491564e905ce13db55f272f83567c1
SHED 2025: a4ab3f7d042f16d63626b1af9aeb6f0b8a0b39e412fa94b87265bc67fe26de14
script:     9219c16e378bd280a044c74401319a8529eef625ef033b9bd5e6de3cd1abb2c8
output:     93e36f61cd3c810646340d27b1c7f77138de84f91f3ff952f5bb549758bbbbc3
```

## Interpretation boundary

This validates a same-respondent annual coverage and care transition, not a
dated bill or clinical episode. Coverage is an imperfect protection marker:
the fields do not capture plan generosity, network access, prior
authorization, provider supply, or affordability. The comparison is
descriptive and does not establish an insurance effect, recovery, remedy,
trust, or political action.
