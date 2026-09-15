# ATUS 2024 care/work acquisition record v1

**Checked:** 2026-09-13
**Status:** official source located and 2024 respondent/activity/summary microdata extraction completed; eldercare-roster extension remains open

## Target files

The BLS [ATUS 2024 microdata page](https://www.bls.gov/tus/data/datafiles-2024.htm)
identifies these files:

| File | Official URL | Needed use |
|---|---|---|
| Respondent | [atusresp-2024.zip](https://www.bls.gov/tus/datafiles/atusresp-2024.zip) | labor force, earnings, demographics, final weight |
| Activity | [atusact-2024.zip](https://www.bls.gov/tus/datafiles/atusact-2024.zip) | care, work, travel, location, and diary timing |
| Eldercare roster | [atusrostec-2024.zip](https://www.bls.gov/tus/datafiles/atusrostec-2024.zip) | care recipient roster and duration fields |
| ATUS-CPS | [atuscps-2024.zip](https://www.bls.gov/tus/datafiles/atuscps-2024.zip) | household and labor context collected before the diary |

The page says the files contain CSV data plus programs/documentation. It also
provides the 2024 interview data dictionary, which must be used to confirm
variable names and universes before analysis.

## Access check

The BLS page and file URLs remain official. Initial direct requests returned
HTTP 403 from the working environment, but a browser-style request with a
referer and cache-busting query obtained the respondent, activity, activity
summary, and eldercare-roster ZIPs on 2026-09-13. The first extraction uses the
respondent, activity, and activity-summary files; the eldercare-roster extension
is retained for the next pass.

The official published release remains usable while the ZIP route is blocked.
The [2023–2024 published care/work layer](atus-2023-2024-published-care-work-layer-v1.md)
records the population estimates for provider scale, age, sex, employment,
care frequency, and hours on care days. Those tables do not replace the
microdata target because they do not retain the same respondent's full work,
care, household, and follow-up fields.

**Current decision:** promote the weighted microdata estimates as a bounded
population time-use layer, while keeping event causation, household totals,
work displacement, and longitudinal recovery open.

## 2024 microdata extraction

The [machine-readable ATUS time/care record](../../records/us-atus-time-care-microdata-2024.json)
and `scripts/analyze_atus_time_care_2024.py` aggregate 139,535 activity rows
for 7,669 merged diary respondents. The extraction preserves primary household
work, care for people, paid work, travel, and socializing/communication, plus
secondary childcare and eldercare minutes. It also reports sex, age, and labor
force comparisons. Archive SHA-256 values are stored in the record; no raw ZIP
is committed.

## Planned bounded estimate

After acquisition, merge respondent, activity, and eldercare-roster records by
the documented case key and calculate weighted descriptive results for:

1. eldercare provider versus non-provider;
2. employed provider versus non-employed provider;
3. full-time/part-time status among providers;
4. care-day hours, work hours, travel, and household production;
5. provider age, sex, family composition, and earnings context.

Report provider prevalence, mean care time on care days, work status, and
standard errors or replicate-weight intervals where supported. Do not describe
care time as lost work time unless the record measures the counterfactual or a
longitudinal earnings outcome.

## How it fits the broader program

This is the time/work measurement layer beneath the [aging, care supply, and
social capacity bridge](aging-care-system-capacity-bridge-v1.md). It can deepen
the population distribution of the care input, but it cannot by itself connect
the same caregiver to later earnings, sleep, health, recipient safety, or
political action. Those remain separate arrows requiring linked or longitudinal
records.
