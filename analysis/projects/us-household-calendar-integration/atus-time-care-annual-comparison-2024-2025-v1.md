# ATUS time and care annual comparison 2024–2025 v1

**Checked:** 2026-09-14  
**Unit:** US ATUS respondent age 15+, one selected diary day per annual sample  
**Status:** weighted annual comparison; not a respondent panel

## Result

| Measure | 2024 | 2025 | Difference, 2025−2024 |
|---|---:|---:|---:|
| Primary household work | 120.7 min (SE 2.0) | 119.8 min (SE 1.9) | −0.8 min |
| Primary care for people | 32.8 (1.2) | 31.5 (1.2) | −1.4 |
| Primary paid work | 190.8 (3.1) | 185.7 (3.8) | −5.1 |
| Primary travel | 65.0 (1.1) | 62.3 (1.3) | −2.7 |
| Socializing/communication | 273.6 (2.9) | 276.1 (3.3) | +2.5 |
| Secondary childcare | 76.7 (2.3) | 72.9 (2.5) | −3.8 |
| Eldercare | 11.0 (1.1) | 10.3 (1.1) | −0.7 |

The annual movement is modest relative to the distribution across people and
life stages. The sex ordering remains visible in both years: women report more
primary household work, care for people, and secondary childcare, while men
report more primary paid work. The age ordering also persists: adults age 65+
report far more eldercare and socializing/communication and far less paid work
than adults age 25–44.

The related [work-location finding](findings/us-household-calendar-integration-029.md)
adds the published 2025 location tables: home and workplace work are overlapping
indicators, and their sex and education gradients are visible. It keeps location
separate from schedule control, total workload, care conflict, and employer
permission. The 2025 release also records missing ATUS interviews during the
October–November 2025 federal shutdown; the annual comparison therefore retains
that coverage caveat rather than treating the year as an uninterrupted diary
panel.

The official BLS release reports that approximately 6,100 people were
interviewed in 2025 and identifies the estimates as annual averages from the
continuous ATUS diary survey. It also reports the 2025 work-location, household
activity, leisure, and childcare tables used as the publication-level check for
the microdata comparison. The release is a vintage and coverage control, not a
second estimate to pool with the respondent files.

## Interpretation boundary

The annual figures are separate samples, not the same people followed from
2024 to 2025. They can identify population-level movement and recurring
distributional structure, but not individual change, a price or work-rule cause,
or a causal path from time allocation to health, trust, or political action.
Primary activities, secondary childcare, and eldercare remain separate
currencies. They should not be added into a single burden score or combined
with CE, SHED, SIPP, or PSID records as if they shared respondents.

## Reproduction

The [machine-readable annual record](../../records/us-atus-time-care-annual-comparison-2024-2025.json)
preserves source archive hashes, denominators, activity definitions, and
replicate-weight standard errors. Re-run:

```text
python3 scripts/analyze_atus_time_care_2024.py --year 2024 \
  --respondent /path/to/atusresp-2024.zip \
  --summary /path/to/atussum-2024.zip \
  --activity /path/to/atusact-2024.zip \
  --replicate /path/to/atuswgts-2024.zip \
  --eldercare-roster /path/to/atusrostec-2024.zip \
  --output /tmp/atus-2024.json

python3 scripts/analyze_atus_time_care_2024.py --year 2025 \
  --respondent /path/to/atusresp-2025.zip \
  --summary /path/to/atussum-2025.zip \
  --activity /path/to/atusact-2025.zip \
  --replicate /path/to/atuswgts-2025.zip \
  --eldercare-roster /path/to/atusrostec-2025.zip \
  --output /tmp/atus-2025.json
```

Official sources: [BLS ATUS 2024 files](https://www.bls.gov/tus/data/datafiles-2024.htm),
[BLS ATUS 2025 files](https://www.bls.gov/tus/data/datafiles-2025.htm), and the
[BLS 2025 ATUS results release](https://www.bls.gov/news.release/atus.nr0.htm).
