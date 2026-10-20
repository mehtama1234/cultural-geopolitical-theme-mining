# FEMA Los Angeles wildfire IHP current API recheck

**Checked:** 2026-10-20  
**Status:** current aggregate program-stage counts updated; individual payment and housing recovery remain open

## What changed

The current OpenFEMA API response for Los Angeles County disaster 4856 contains
621 city/ZIP rows and reports 261,118 valid registrations, 98,460 IHP
referrals, 35,169 IHP-eligible records, and $184.787 million in aggregate IHP
amounts. Compared with the retained September extraction, the current vintage
adds one valid registration, one referral, four eligible records, and about
$2.013 million in reported amount.

```text
wildfire registration
  -> IHP referral
  -> IHP eligibility
  -> aggregate amount reported
  -> [open] individual award and payment receipt
  -> [open] repair, stable housing, adequacy, trust, action, and exit
```

The update is a current administrative-vintage change, not a same-survivor
payment trajectory. The API does not provide a household panel, award timing,
receipt, appeal, adequacy, repair completion, or stable placement.

## Next decisive evidence

Seek a lawful aggregate of awards issued, payments delivered or returned,
appeals, housing-assistance duration, or later stable placement. Keep API stage
counts and amounts separate from individual recovery.

## Source

- [OpenFEMA Registration Intake and Individuals Household Programs API](https://www.fema.gov/api/open/v2/RegistrationIntakeIndividualsHouseholdPrograms?$filter=disasterNumber%20eq%204856&$top=100000)

**Evidence boundary:** the API supports current aggregate registration,
referral, eligibility, and IHP amount fields. It does not support individual
award, payment receipt, adequacy, repair completion, housing stability, trust,
or exit.
