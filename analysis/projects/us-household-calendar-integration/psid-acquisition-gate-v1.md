# PSID acquisition gate

**Checked:** 2026-09-24
**Status:** open account-controlled acquisition gate; no PSID estimate published

**Route-selection rule — 2026-09-20:** PSID is the first authenticated
acquisition for the broad atlas because its family/person longitudinal design
matches the material, work, care, wellbeing, and household-room bridge. UAS
remains the preferred route for the separate dated health-cost episode because
its monthly event and billing modules are more direct for that narrower case.
The two routes must not be silently pooled or treated as interchangeable.

**Current documentation recheck:** 2026-09-20 — official PSID pages continue
to state that public-use data are available after researcher registration and
acceptance of the Conditions of Use. This confirms an account-controlled
distribution route, not a substantive data absence.

The new [public-route recheck](psid-public-route-recheck-2026-09-19.json)
also confirms the 2023 Individual Release 2 documentation: 85,536 person
records, 2,771 variables, cross-wave information through 2023, and documented
longitudinal and cross-sectional weights. The Data Center is the preferred
first route because it can create a customized multi-wave extract; the first
authenticated pass should request a minimal field cart rather than download
all packaged files by default.

**Current public-route recheck — 2026-09-20:** the official [PSID Getting
Started page](https://psidonline.isr.umich.edu/GettingStarted.aspx) still says
that public-use data are available to researchers who register and accept the
Conditions of Use. It describes the Data Center and packaged-data routes and
continues to expose longitudinal family, employment, income, health, and
wellbeing content. This makes PSID the preferred first authenticated route for
the broad atlas's material/time/care bridge, ahead of the more restrictive UAS
route, subject to account access and the same structural audit. No PSID file
was downloaded or analyzed in this recheck.

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

The 2026-09-17 local workspace recheck searched `/tmp` and the repository for
PSID/UAS-named files. It found only documentation, manifests, scripts, and
small smoke-audit outputs; no target PSID package was present. No package was
downloaded during this check, and the absence of a local package is not
evidence that the substantive relationship is absent.

**Current local recheck — 2026-09-24:** a fresh repository/workspace inventory
again found only access notes, manifests, scripts, and compiled test artifacts;
there is no authorized 2019, 2021, or 2023 PSID package, UAS respondent file,
HRS file, or event-compatible restricted input. This confirms the operational
boundary, not a substantive null result. Do not retry an unauthenticated route
or treat documentation as respondent data.

The current official [PSID documentation page](https://psidonline.isr.umich.edu/Guide/documents.aspx)
continues to expose 2023 Main Study documentation and links to the Data Center
and registration routes. The official [Getting Started page](https://psidonline.isr.umich.edu/GettingStarted.aspx)
states that public-use data require researcher registration and agreement to
the Conditions of Use. This recheck confirms that the route is live; it does
not change the local-data gate or establish package retrieval. The direct
2026-09-16 route recheck returned HTTP 403 with HTML content and a Cloudflare
managed-challenge indicator. This is recorded as an access condition, not as
evidence that the file is absent or that the planned relationship is null.

**Current direct-route recheck — 2026-09-18:** an unauthenticated GET of the
official 2023 package route returned HTTP 403, `cf-mitigated: challenge`, and
an HTML response requiring JavaScript and cookies. Response SHA-256 is
`4fcaf4b248cb5cf275fbf095605f4d8f1833d9cb1bcc17f8e01df36d57c3e8d4`. The
route remains live but account/browser controlled; no respondent file was
downloaded or used as evidence. The machine audit records this recheck.

The accompanying [public-documentation recheck](psid-access-audit-2026-09-13.json)
also records the current Getting Started and FAQ language: PSID public-release
files are downloadable by registered researchers who accept the Conditions of
Use. The distinction matters operationally: the automated 403 is a session and
browser-access boundary, not evidence that the packages are unavailable or
that the planned household relationship is null.

## Required next handoff

An account holder must accept the official Conditions of Use and either supply
the four public-use packages or create the minimal multi-wave Data Center
extract specified in the [public-route recheck](psid-public-route-recheck-2026-09-19.json).
Then run the [wave-file structural audit](psid-wave-file-audit-protocol-v1.md)
against the downloaded files and preserve its JSON output.

The [account-holder request card](psid-account-holder-request-v1.md) is the
minimal operational handoff for the first authenticated extract. It keeps the
request small, preserves raw labels and weights, and states what must be
returned before analysis.

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
