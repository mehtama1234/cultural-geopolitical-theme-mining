# PSID wave-file audit protocol v1

**Checked:** 2026-09-13  
**Status:** executable acquisition gate; no PSID microdata are present locally

The latest [access-surface audit](psid-access-audit-2026-09-13.json) confirms
that the official page lists the 2019, 2021, 2023, and 1968–2023 packages, but
the download routes redirect to the Conditions-of-Use warning for the current
unauthenticated session. This is an access prerequisite, not a null finding.

This protocol is the first step after authenticated PSID downloads arrive. It
checks file structure against the [PSID material/time/care field
map](../../../manifests/us-psid-material-time-care-field-map-v1.json) before
any merge, weighting, or estimate. It does not establish that questions have
comparable universes or response codes; those remain the next audit stage.
The file/key assumptions should be checked against PSID's official
[file-structure and merging guide](https://psidonline.isr.umich.edu/Guide/FileStructure.pdf)
for the release actually downloaded.

## Run the structural gate

Supply the family file for each target wave and the PSID cross-year individual
file. The official file-structure guide describes the 1968–2023 cross-year
individual package as containing individual-level items through 2023, so the
same individual file can cover the three target waves. Multiple `--file`
arguments for one year remain supported for wave-specific person exports or
alternate family packages because PSID family- and person-level fields are not
expected to live in the same file. Delimited exports are handled with the
standard library; Stata/SAS/SPSS formats use pandas when available.

```bash
python3 scripts/audit_psid_wave_files.py \
  --file 2019=/path/to/FAM2019ER.csv \
  --file 2021=/path/to/FAM2021ER.csv \
  --file 2023=/path/to/FAM2023ER.csv \
  --file 2019=/path/to/IND1968_2023ER.csv \
  --file 2021=/path/to/IND1968_2023ER.csv \
  --file 2023=/path/to/IND1968_2023ER.csv \
  --identifier ER30001 --identifier ER30002 \
  --out analysis/projects/us-household-calendar-integration/psid-wave-file-audit-YYYY-MM-DD.json
```

Identifier arguments are deliberately explicit because the family and
individual file architectures must be confirmed from the downloaded package;
the tool will not guess which PSID keys are safe. The structural gate checks
that every requested key appears in at least one supplied file for each wave;
the subsequent merge audit must establish which key belongs to which file and
whether it is unique. Repeat `--identifier` for every key required by the
planned merge.

## What the report proves

For each supplied wave it records each reader, the union of observed columns,
expected mapped columns, missing mapped variables, missing identifiers, and
file-level status. It also fails when a target wave is absent or a file cannot
be inspected. A passing report means only that the structural surface is ready
for the next gates:

1. codebook wording, universe, routing, and response-code comparison;
2. family/person key uniqueness and merge counts;
3. zero, not-applicable, don't-know, refusal, and unavailable separation;
4. retention, mover-out, family-composition, and item-missingness checks;
5. weight and replicate-variance identification; and
6. weighted descriptive cells with counterexamples and uncertainty.

No result should be promoted from this structural pass alone. The eventual
extract must still preserve the distinction between typical-week time reports,
detailed diaries, material resources, dated triggers, and cultural or
political meaning.

## Current access boundary

The official [PSID packaged-data page](https://simba.isr.umich.edu/Zips/ZipMain.aspx)
lists the 2019, 2021, and 2023 main Family Files and the 1968–2023 Cross-year
Individual File. The [PSID getting-started page](https://psidonline.isr.umich.edu/GettingStarted.aspx)
says public-use data are free after registration and acceptance of the
Conditions of Use; an unauthenticated ZIP request redirects to the official
[download warning](https://simba.isr.umich.edu/Zips/ZipWarnAccess.aspx).

As of the check date, no PSID data files are present in the workspace. This is
an access prerequisite, not a null finding. Once the account-controlled files
are supplied, run this structural gate with the cross-year individual package
attached to each target wave entry, then perform the separate family/person
key, universe, retention, missingness, weight, and merge audits. Do not treat
the repeated path names in the command as proof that one file contains all
family-level fields.

Related: the [extract specification](psid-material-time-care-extract-spec-v1.md),
the [acquisition plan](material-time-care-linkage-acquisition-plan-v1.md), and
the [broad program queue](../../US-BROAD-NEXT-PASS-QUEUE_V1.md).
