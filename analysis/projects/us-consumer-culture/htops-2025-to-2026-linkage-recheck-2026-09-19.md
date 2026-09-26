# HTOPS June 2025 to March 2026 linkage recheck v1

**Checked:** 2026-09-19  
**Purpose:** test whether the retained March 2026 HTOPS archive can extend the
June 2025 same-respondent material-search bridge.

## Result

The June 2025 topical file contains **7,485** `SCRAMID` values. The retained
March 2026 public-use archive contains **12,521** `SCRAMID` values. Their exact
set intersection is **zero**.

The March archive therefore cannot supply a same-respondent nine-month
follow-up to the April-to-June 2025 material-search finding. It remains a
separate cross-sectional source unless an authorized harmonized linkage key or
different panel file is supplied.

The March 2026 PUF also does not expose the June endpoint contract used in the
search finding: its retained header includes `FDSCHL_EXPNSDIF` but no `AI4_*`
search fields or `TRUST2_CONGRESS` field. Even with a future linkage key, the
current March file would not reproduce the same search/AI/confidence outcomes.

## Interpretation boundary

- Zero overlap is a key/linkage result, not evidence that households' later
  search, recovery, trust, or action was unchanged.
- Missing comparable fields are a measurement boundary, not evidence that the
  March population did not search or change confidence.
- The March archive was already present locally as
  `/tmp/HTOPS_HPS_2603_CSV.zip`; no download, extraction, or respondent-level
  result was added to the repository.
- The April-to-June 2025 bridge remains the strongest retained same-respondent
  navigation result: it has time ordering but no search-result quality,
  completion, remedy, recovery, or exit endpoint.

## Reproduction boundary

The check reads only the `SCRAMID` columns from:

- `/tmp/htops-2506/HTOPS_HPS_2506_PUF.csv`
- `/tmp/HTOPS_HPS_2603_CSV.zip`, member `HTOPS_HPS_2603_PUF.csv`

No raw respondent file was copied into Git.
