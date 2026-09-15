# NBER W35677 public adoption-index acquisition v1

**Checked:** 2026-09-13  
**Source page:** [RPS data page](https://sites.google.com/view/covid-rps/data)  
**Paper:** [NBER Working Paper 35677](https://www.nber.org/papers/w35677)  
**Status:** public index files acquired and structurally audited; raw-file retention remains external to Git

## Acquisition

The paper links three public Google Sheets to the task-level results. The
workbook exposes a README plus separate sheets for Detailed Work Activities
(DWA), Intermediate Work Activities (IWA), and Broad Work Activities (BWA).
The sheets were retrieved as CSV through the Google Sheets export endpoint:

| Level | Sheet identifier | Rows with rates | CSV retrieval hash |
|---|---:|---:|---|
| DWA | `416182935` | 682 | `sha256:897209aacafd51dcadb4f830f07d9f431af3646710563f26b14d8289e9478aaf` |
| IWA | `1821519318` | 256 | `sha256:be41e67b1344d795bc27c77aad1021a32c42f583d8b96929c46ca3435472871c` |
| BWA | `646067329` | 9 | `sha256:84660dd773d01ef72c17ac3667fb082704c6a396fc3b8115630127b42b0292e5` |

The workbook says the underlying survey is the Real-Time Population Survey,
pooled across August 2025, November 2025, February 2026, and May 2026. It says
rates are survey-weighted shares of performed work-activity observations for
which the respondent reports using generative AI; a respondent who does not
use generative AI at work contributes zero to task use. Cells with fewer than
20 unweighted observations are blank.

The workbook's citation block still contains an insertion placeholder for the
full measurement-paper citation. The paper and date are therefore recorded
from the linked NBER page, not from that unfinished workbook cell.

## Bounded checks

The acquired DWA sheet contains 682 nonblank rates. Its highest displayed rates
include reading technical documents (61.3%, 30 observations), preparing
research reports (60.7%, 69), and designing integrated computer systems (59.5%,
51). The lowest displayed cells are 0.0% but still have at least 20
observations, including arranging delivery of goods or services (23).

At the BWA level, reasoning and decision making is highest at 30.0% across
7,075 unweighted work-activity observations, while performing physical and
manual work is lowest at 9.6% across 8,351 observations. These are activity
patterns, not worker productivity, pay, or control estimates.

## Reproducibility and limits

The export can be reacquired with:

```text
https://docs.google.com/spreadsheets/d/17OI5xRALkN4lDZ1fHw2R9xPJUdDgWyFU/gviz/tq?tqx=out:csv&gid=416182935
https://docs.google.com/spreadsheets/d/17OI5xRALkN4lDZ1fHw2R9xPJUdDgWyFU/gviz/tq?tqx=out:csv&gid=1821519318
https://docs.google.com/spreadsheets/d/17OI5xRALkN4lDZ1fHw2R9xPJUdDgWyFU/gviz/tq?tqx=out:csv&gid=646067329
```

The sheets do not contain worker-level microdata, so they cannot support
subgroup estimates by age, education, race, gender, disability, employer size,
or place. The [O*NET release and crosswalk metadata gate](onet-release-metadata-gate-v1.md)
records the official 31.0 release boundary and the required identifier audit.
The O*NET database release and exact crosswalk version must also be recorded
before treating task labels as permanently comparable. Keep the
downloaded CSVs outside the repository and retain their retrieval date and
hashes when reproducing the summary.

The first audit found zero exact ID matches because NBER and O*NET encode the
task hierarchy differently, but normalized labels matched 1,653 of 1,655 DWA
rows and all 322 IWA rows. The nine NBER BWA labels require a separate
aggregation mapping. These results are retained in the
[machine-readable audit](data/onet-31-0-nber-crosswalk-audit-2026-09-13.json)
The post-acquisition reproduction is now in the [versioned crosswalk directory](data/onet-nber-crosswalk-2026-09-14/), including the [current crosswalk](data/onet-nber-crosswalk-2026-09-14/provisional-label-crosswalk.json), [identifier audit](data/onet-nber-crosswalk-2026-09-14/onet-nber-identifier-reconciliation-audit-2026-09-14.json), and [acquisition manifest](data/onet-nber-crosswalk-2026-09-14/acquisition-manifest.json).
and do not yet authorize a promoted crosswalk.

**Evidence status:** public, survey-weighted descriptive indexes acquired;
worker-level adoption determinants and adoption-to-control outcomes remain
open.
