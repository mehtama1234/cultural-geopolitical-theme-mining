# ILOSTAT labor-comparison route: official catalog reachable, bulk payload not acquired

**Status:** access audit · **Checked:** 2026-09-14

## Why this is recorded

ILOSTAT is part of the program’s international comparison layer for labor
participation, unemployment, working poverty, earnings, and youth exclusion.
Those measures can help put US work and household findings in a comparable
frame. They must remain a comparison, however: an international estimate is
not a substitute for a US household or worker observation.

## What was verified

The official [ILOSTAT data catalog](https://ilostat.ilo.org/data/) and
[bulk-download documentation](https://ilostat.ilo.org/data/bulk/) describe
programmatic indicator files, reference-area files, dictionaries, frequencies,
source metadata, and modelled-estimate boundaries. The official Rilostat
documentation identifies the indicator route and the unemployment-by-sex-and-
age dataset family.

The candidate official bulk payload
`UNE_2UNE_SEX_AGE_NB_A` was requested through the documented ILOSTAT host in
the prior recorded recheck. The response was HTTP-successful but contained zero bytes, so no
labor estimate was extracted or promoted into the trend registry. This is a
non-observation about access, not a claim about unemployment or participation.

## Follow-up route recheck

On 2026-09-14, the direct indicator paths documented by the Rilostat examples
were rechecked for `UNE_TUNE_SEX_AGE_NB_A`, `UNE_2UNE_SEX_AGE_NB_A`, and the
documented labour-force example `EAP_TEAP_SEX_AGE_NB_A`. The current
`www.ilo.org/ilostat-files/WEB_bulk_download/indicator/` and
`webapps.ilo.org/ilostat-files/WEB_bulk_download/indicator/` paths returned
HTTP 404 responses containing a 153-byte HTML error document, not CSV/GZIP
data. This is a route or file-version condition; it does not establish that
the indicators or their underlying estimates are absent. The earlier
HTTP-success/zero-byte observation is retained rather than overwritten.

The Rilostat source code documents a second delivery route under
`https://rplumber.ilo.org/files/indicator/{id}.rds`, and the Rilostat table-of-
contents documentation identifies the API metadata route at
`https://rplumber.ilo.org/metadata/toc/indicator/`. On the same 2026-09-14
recheck, the metadata route and the RDS routes for
`UNE_TUNE_SEX_AGE_NB_A`, `UNE_2UNE_SEX_AGE_NB_A`, and
`EAP_DWAP_SEX_AGE_RT_A` returned HTTP 200 with
`application/octet-stream` but zero-byte bodies. The empty-body SHA-256 was
`e3b0c44298fc1c149af4c8996fb92427ae41e464ca495991b7852b855` in each probe.
On 2026-09-15, a fresh recheck repeated the same zero-byte response for the
metadata route, the documentation route, the RDS route, and a CSV.GZ variant
for `UNE_TUNE_SEX_AGE_NB_A`. The route-level results are preserved in the
[durable recheck record](data/ilostat-route-recheck-2026-09-15.json). This
confirms a reproducible delivery failure in this environment; it does not
confirm an empty ILOSTAT dataset or a missing indicator.

## Acquisition gate

Before adding an ILOSTAT observation, the next pass must capture:

- the exact indicator and frequency;
- the reference area and sex/age universe;
- whether the value is national, reported, estimated, or projected;
- the source survey or administrative basis;
- the release/update date and revision status;
- the downloaded payload and SHA-256 hash; and
- a US comparison with matching concept, period, and subgroup definition.

Until that gate is met, the program uses ILOSTAT as a documented source and
open acquisition target, not as quantitative evidence.

## Sources

- [ILOSTAT data tools](https://ilostat.ilo.org/data/)
- [ILOSTAT bulk download facility](https://ilostat.ilo.org/data/bulk/)
- [ILOSTAT labor-force participation snapshot](https://ilostat.ilo.org/data/snapshots/labour-force-participation-rate/)
- [ILOSTAT unemployment snapshot](https://ilostat.ilo.org/data/snapshots/unemployment-rate/)
- [Rilostat data access documentation](https://ilostat.github.io/Rilostat/reference/get_ilostat.html)
- [Rilostat table-of-contents/API documentation](https://ilostat.github.io/Rilostat/reference/get_ilostat_toc.html)

**Boundary:** no ILOSTAT numerical finding is claimed in this audit. The
access route remains active in the next-pass queue.
