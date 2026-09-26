# PSID account-holder request card v1

**Checked:** 2026-09-20  
**Purpose:** give an authorized PSID account holder the smallest useful first
extract for the broad atlas's material/time/care bridge.  This is an access
and field request, not an analysis result.

## What to request

Use the official PSID Data Center or the documented public-use packages after
registration and acceptance of the Conditions of Use. Request the 2019, 2021,
and 2023 Main Study family records plus the 1968–2023 cross-year individual
file, or an equivalent customized extract that retains the same identifiers,
weights, and codebook definitions.

Ask for:

- year-specific family and person identifiers, family-unit status, interview
  year, survey mode, and longitudinal/analysis weights;
- paid work hours, employment transitions, commute or work-from-home fields,
  work-intensity/rushed-at-work items, and work start/stop timing where valid;
- housework, personal-care, shopping/service, child-care, adult-care,
  volunteering, leisure/social interaction, family-meal, and outside-work
  rushed-time fields;
- paid child-care cost and months used;
- life satisfaction, general health, health-change, family composition,
  mover/family-unit status, and relevant disability/health controls; and
- family income, wealth, utility, home-insurance, selected essential-spending,
  and family longitudinal-weight fields.

The existing [material/time/care extract specification](psid-material-time-care-extract-spec-v1.md)
contains the wave-specific candidate variable names. Preserve the raw
variable names and labels in the delivery; do not send only recoded columns.

## What the account holder should return

1. The downloaded file names, release/version, and official codebook or Data
   Center extract definition.
2. SHA-256 hashes for every supplied file.
3. A note confirming that the account holder accepted the applicable Conditions
   of Use and that this processing route is permitted.
4. The family/person key architecture and the requested weights, including any
   replicate-weight or variance instructions.
5. The exact universe and special-code definitions for every selected field.

Do not include unnecessary raw files or identifiers in the repository. The
first workspace pass should retain hashes, a field manifest, structural-audit
JSON, compact derived records, and the permitted-use note; keep raw respondent
files in the authorized storage location.

## First workspace checks

Run the structural audit before merging or estimating:

```bash
python3 scripts/audit_psid_wave_files.py \
  --file 2019=/authorized/path/FAM2019ER.csv \
  --file 2021=/authorized/path/FAM2021ER.csv \
  --file 2023=/authorized/path/FAM2023ER.csv \
  --file 2019=/authorized/path/IND1968_2023ER.csv \
  --file 2021=/authorized/path/IND1968_2023ER.csv \
  --file 2023=/authorized/path/IND1968_2023ER.csv \
  --identifier ER30001 \
  --identifier ER30002 \
  --out analysis/projects/us-household-calendar-integration/psid-wave-file-audit-YYYY-MM-DD.json
```

The cross-year individual file is intentionally supplied once under each
target wave label so the audit checks that every requested wave is represented.
Replace the example paths only with files received through the authorized
account route.

```text
file inventory and hashes
  -> family/person key uniqueness and wave overlap
  -> codebook universes and routing
  -> zero / not-applicable / don't-know / refusal / unavailable codes
  -> mover-out, family-composition, retention, and item missingness
  -> weights and variance method
  -> merge counts and valid denominators
```

Stop if the files are incomplete, the account authority is unclear, keys do
not retain the same unit across waves, fields are not comparable, or weights
and missingness cannot be interpreted. Only after those checks should the first
descriptive cells be run:

- material-room change × paid work change;
- material-room change × paid and unpaid care;
- care-time change × work, health, commute, and social availability; and
- similar exposure × different alternative/support and later persistence.

## Claim boundary

This extract can test repeated distributions and within-unit change in
material room, work, care, health, wellbeing, and time pressure. By itself it
cannot identify a dated price, employer, agency, insurer, platform, or policy
shock; verified remedy receipt; trust; political action; or geopolitical
consequence. Those stages remain separate unless the supplied fields directly
measure them.

Related controls: the [PSID acquisition gate](psid-acquisition-gate-v1.md),
the [wave-file audit protocol](psid-wave-file-audit-protocol-v1.md), and the
[next authorized longitudinal handoff](../../data/next-authorized-longitudinal-pass-handoff-v1.json).
