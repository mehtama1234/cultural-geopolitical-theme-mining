# ATUS 2024 care/work acquisition record v1

**Checked:** 2026-09-12  
**Status:** official source located; microdata download blocked by the host in this environment; no new estimates claimed

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

On 2026-09-12, direct requests to the BLS file URLs returned HTTP 403
(`AkamaiGHost`, access denied) from the working environment. The page itself is
available and identifies the files, but the ZIP contents were not obtained in
this pass. This is an acquisition issue, not evidence that the files do not
exist or that care/work estimates are unavailable.

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
