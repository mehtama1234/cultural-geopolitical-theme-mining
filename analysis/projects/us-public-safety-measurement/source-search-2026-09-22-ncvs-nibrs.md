# Source search: victim surveys versus police-recorded crime

**Search date:** 2026-09-22  
**Geography:** United States  
**Status:** bounded pass complete; NCVS and NIBRS are complementary, not interchangeable

## Working question

Why can two official crime measures show different rates for the same year?

## Opening source

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-BJS-NCVS-NIBRS-2023 | [The National Crime Victimization Survey and National Incident-Based Reporting System: A Complementary Picture of Crime in 2023](https://bjs.ojp.gov/library/publications/national-crime-victimization-survey-and-national-incident-based-reporting-system-2023) | BJS compares victim-reported crime, including incidents not reported to police, with FBI NIBRS incidents recorded by law enforcement. | Official BJS/FBI comparison | It does not reconcile a particular victim, police response, case outcome, or later trust across the two systems. |

## First pattern

```text
crime experienced or recorded
  -> survey report or police record
  -> different definitions, populations, and denominators
  -> public trend, policy judgment, and institutional response [open]
```

For 2023, the comparable violent-crime-excluding-simple-assault rate was 4.42
per 1,000 in NCVS reported-to-police victimizations and 3.88 per 1,000 in NIBRS
recorded incidents. Property crime was 30.61 per 1,000 households in NCVS and
20.15 per 1,000 persons in NIBRS. BJS warns that the property denominators are
different and that NIBRS includes populations and crime types NCVS does not.

## Counterpoint to keep visible

The two sources trend similarly over time, but a same-year gap is not a simple
underreporting percentage. NCVS uses interviews and includes crimes not
reported to police; NIBRS uses law-enforcement records and adjusts for
incomplete agency reporting. Crime definitions, covered populations, reference
periods, and units differ.

## Decision rule

Use NCVS for victim experience and reporting behavior and NIBRS for
law-enforcement-recorded incidents. Do not merge their rates into one crime
trend or infer response quality, safety, or trust without an episode-level link.
