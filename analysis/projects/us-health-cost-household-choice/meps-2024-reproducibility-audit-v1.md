# MEPS 2024 reproducibility audit v1

**Checked:** 2026-09-15  
**Status:** acquisition and headline-estimate reproduction passed  
**Scope:** HC-256 full-year person file and HC-036BRR standard-BRR variance file

## Result

The current official MEPS 2024 archives were re-acquired from AHRQ into a
temporary working directory and the recorded HC-256 headline results were
reproduced without changing the analysis scripts.

| Check | Observed result | Status |
|---|---:|---|
| HC-256 rows | 19,140 | passed |
| HC-256 columns | 1,615 | passed |
| HC-256 positive final person weights | 18,683 | passed |
| HC-036BRR unique person IDs | 461,092 | passed |
| HC-256 IDs found in HC-036BRR | 19,140 / 19,140 | passed |
| BRR indicators | 128 | passed |
| Required structural fields | all present and nonmissing in the scan | passed |
| Total expenditure mean | $8,346.5249 | reproduced |
| Total expenditure BRR SE | $225.5589 | reproduced |
| Self/family payment mean | $1,117.2803 | reproduced |
| Self/family payment BRR SE | $37.7341 | reproduced |

The reproduced 95% normal-approximation intervals are $7,904.4295–$8,788.6203
for total expenditure and $1,043.3216–$1,191.2391 for self/family payment.
The estimates use the 18,683 records with positive `PERWT24F` and valid
outcome fields.

## Acquisition artifacts

The source archives were retrieved from the official AHRQ MEPS routes:

- [HC-256 Stata archive](https://meps.ahrq.gov/mepsweb/data_files/pufs/h256/h256dta.zip)
- [HC-036BRR Stata archive](https://meps.ahrq.gov/mepsweb/data_files/pufs/h036brr/h36brr24dta.zip)

The archive SHA-256 values are:

```text
HC-256 h256dta.zip
653891861ec18574b07f576915e6f9e423263fc947610dc34e1bd176feff7b40

HC-036BRR h36brr24dta.zip
0414ce196f10ef3d910e63dc4a3752e0c493884a410dd84bd2369041fc0929dd
```

The extracted-file hashes observed during this audit were:

```text
HC-256 h256.dta
b4bde859b39f626345561c05570292bb7264dd92eb76ce0c1a14d6b89076aed5

HC-036BRR h36brr24.dta
44f1e5a864c1d318327a0fbd3a0ff48a583c74c3a104aae357032cfbfaa5a32e
```

The archives and extracted files remain outside Git under
`/tmp/cgtm-meps-2024/`; the repository stores the retrieval hashes and the
reproduction record, not the temporary raw data.

## Reproduction commands

```text
python3 scripts/audit_meps_hc256_structure.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  --brr-file /tmp/cgtm-meps-2024/h36brr/h36brr24.dta

python3 scripts/analyze_meps_hc256_brr.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  /tmp/cgtm-meps-2024/h36brr/h36brr24.dta
```

The analysis uses the standard MEPS construction: each BRR flag is multiplied
by `2 * PERWT24F`, and variance is the mean squared deviation across the 128
replicate estimates. HC-256 and HC-036BRR are joined by `DUPERSID` and
`PANEL`; the audit observed no missing BRR flags after the join.

## What this closes

This audit closes the immediate artifact-availability and headline-estimate
reproduction gate for the 2024 person-level MEPS layer. It confirms that the
recorded results are executable from current official source archives and that
the basic person-to-replicate identity join is intact.

## What remains open

This does not create the end-to-end health-cost episode. The current files do
not, by themselves, establish a dated bill or need, available alternatives,
care delay, unpaid care, debt, work-time substitution, recovery, verified
institutional remedy, trust change, or political action for the same episode.
Event files also represent observed visits, purchases, emergency visits, or
stays and do not include people who never reached that event.

The next substantive pass should audit the person/event identifiers and date
surfaces needed to populate the health-cost event ledger, then test whether a
same-person episode can retain coverage, payment, care decision, work, health,
and follow-up fields without silently turning annual or event-level measures
into a household causal chain.
