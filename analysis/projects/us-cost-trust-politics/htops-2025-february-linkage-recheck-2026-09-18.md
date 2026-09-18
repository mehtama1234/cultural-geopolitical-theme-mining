# HTOPS February 2025 linkage recheck

**Checked:** 2026-09-18  
**Status:** official-file acquisition recheck; no valid February-to-April/June respondent join

## Result

The Census public-use page identifies the February 2025 HTOPS PUF as part of
the 2025 longitudinal design. The February PUF was retrieved with its
replicate-weight file and supplemental file, and the respondent key was tested
against the retained April and June 2025 PUFs.

| Release | PUF rows | Unique `SCRAMID` values |
|---|---:|---:|
| February 2025 | 6,740 | 6,740 |
| April 2025 | 8,850 | 8,850 |
| June 2025 | 7,485 | 7,485 |

Exact-key intersections were:

| Pair or sequence | Exact `SCRAMID` overlap |
|---|---:|
| February × April | 0 |
| February × June | 0 |
| April × June | 6,564 |
| February × April × June | 0 |

The February release therefore cannot supply a pre-April baseline for the
existing fraud/loss/report/recovery follow-up. The valid same-respondent route
remains April → June only. This is an acquisition and identification boundary,
not evidence that no February respondents were later surveyed: the public-use
IDs do not support the required join.

The Census page also states that HTOPS used a longitudinal design throughout
2025 but transitioned to a cross-sectional design beginning in March 2026.
Later 2026 releases therefore cannot be assumed to extend the 2025 respondent
chain either.

## Interpretation consequence

```text
February public file --X--> April fraud/loss module --SCRAMID--> June outcomes
                                             |
                                             +--> 6,564 retained respondents
```

The February file is not promoted into the end-to-end atlas. The existing
April–June result remains an exploratory same-respondent screen with
retrospective fraud timing, selective retention, no attrition-adjusted
longitudinal weight, and no verified remedy receipt or durable restoration.
Another cross-sectional February comparison would not close those gaps.

## Reproduction and hashes

```text
python3 - <<'PY'
import pandas as pd
paths = {
    "feb": "/tmp/htops-2502/HTOPS_HPS_2502_PUF.csv",
    "apr": "/tmp/htops-2504/TOPICAL_2504_PUF.csv",
    "jun": "/tmp/htops-2506/HTOPS_HPS_2506_PUF.csv",
}
sets = {k: set(pd.read_csv(v, usecols=["SCRAMID"])["SCRAMID"].astype(str))
        for k, v in paths.items()}
print({k: len(v) for k, v in sets.items()})
print("feb_apr", len(sets["feb"] & sets["apr"]))
print("feb_jun", len(sets["feb"] & sets["jun"]))
print("apr_jun", len(sets["apr"] & sets["jun"]))
print("triple", len(sets["feb"] & sets["apr"] & sets["jun"]))
PY
```

The compact [machine recheck](data/htops-2025-february-linkage-recheck-2026-09-18.json)
retains the release URLs, file hashes, row counts, and overlap result. Raw PUFs
remain outside the repository.

Primary sources: the Census [2025 PUF page](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.2025.html),
[February PUF](https://www2.census.gov/programs-surveys/demo/datasets/hhp/2025/topical/HTOPS_HPS_2502_CSV.zip),
[February supplemental PUF](https://www2.census.gov/programs-surveys/demo/datasets/hhp/2025/topical/HPS_HTOPS_2502_Supplemental_PUF_CSV.zip),
[April PUF](https://www2.census.gov/programs-surveys/demo/datasets/hhp/2025/topical/HTOPS_HPS_2504_CSV.zip),
and [June PUF](https://www2.census.gov/programs-surveys/demo/datasets/hhp/2025/topical/HTOPS_HPS_2506_CSV.zip).

**Evidence status:** official-file and key-overlap boundary reproduced; no
three-wave same-respondent estimate claimed.
