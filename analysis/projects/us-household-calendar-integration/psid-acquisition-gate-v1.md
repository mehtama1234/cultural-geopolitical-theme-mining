# PSID acquisition gate

**Checked:** 2026-09-16
**Status:** open account-controlled acquisition gate; no PSID estimate published

## What is available

The official PSID packaged-data page lists the four packages needed for the
planned 2019/2021/2023 material, time, care, and wellbeing comparison:

- 2019 Main Study Family File
- 2021 Main Study Family File
- 2023 Main Study Family File
- 1968–2023 Cross-year Individual File

The [access-surface audit](psid-access-audit-2026-09-13.json) records the
official route for each package. The current download routes redirect to the
official Conditions-of-Use warning because the account has not accepted the
policy in the authenticated PSID session. The 2026-09-15 public-web recheck
confirms that the files are listed and the 2023 route is live, but the ZIP
remains account-controlled.

On 2026-09-14, an unauthenticated workspace probe of the official package
route returned HTTP 403 with a Cloudflare managed challenge requiring
JavaScript and cookies. This does not supersede the documented account and
Conditions-of-Use requirement; it records that an automated request cannot
demonstrate package access. No data file was downloaded or treated as evidence.

## What is not available

There are no 2019, 2021, or 2023 PSID data packages in the repository or its
temporary workspace. The official package page lists the target files, but the
download route requires registration and acceptance of the Conditions of Use;
the workspace has not completed that account-controlled step. The codebook,
field map, extract specification, and audit script are present, but they are
not substitutes for the microdata. No many-family PSID estimate, longitudinal
merge, or trend claim should be written from the documentation alone.

This is an access prerequisite, not a null finding and not evidence that the
planned relationship is absent.

The current official [PSID documentation page](https://psidonline.isr.umich.edu/Guide/documents.aspx)
continues to expose 2023 Main Study documentation and links to the Data Center
and registration routes. The official [Getting Started page](https://psidonline.isr.umich.edu/GettingStarted.aspx)
states that public-use data require researcher registration and agreement to
the Conditions of Use. This recheck confirms that the route is live; it does
not change the local-data gate or establish package retrieval. The direct
2026-09-16 route recheck returned HTTP 403 with HTML content and a Cloudflare
managed-challenge indicator. This is recorded as an access condition, not as
evidence that the file is absent or that the planned relationship is null.

## Required next handoff

An account holder must accept the official Conditions of Use and supply the
four public-use packages. Then run the [wave-file structural audit](psid-wave-file-audit-protocol-v1.md)
against the downloaded files and preserve its JSON output.

The structural pass must be followed by separate checks for:

1. codebook wording, universe, routing, and response codes;
2. family/person key uniqueness and merge counts;
3. zero, not-applicable, don't-know, refusal, and unavailable codes;
4. mover-out, family-composition, retention, and item-missingness patterns;
5. family and person weights, replicate variance, and valid denominators; and
6. weighted cells, uncertainty, subgroup differences, and counterexamples.

Only after those gates pass should the first bounded comparison be published.
The planned result remains a material/time/care comparison, not a claim that
PSID alone observes a dated shock, political meaning, verified remedy, or
geopolitical consequence.

## Current alternatives while the gate is open

The program continues the material/time/care lane with already acquired SIPP,
ATUS, SHED, NHTS, MEPS, RECS, and Consumer Expenditure layers. These sources
can add bounded population, time, health, mobility, and household-room
evidence, but they do not silently replace the intended PSID same-family
bridge.
