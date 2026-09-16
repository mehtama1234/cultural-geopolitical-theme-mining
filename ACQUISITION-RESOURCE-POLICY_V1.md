# Acquisition resource policy v1

**Checked:** 2026-09-16  
**Scope:** all external files acquired for the cultural/geopolitical theme
atlas

The working environment has limited storage. Research progress must therefore
prefer small, reproducible artifacts and existing local inputs over bulk
downloads.

## Default operating rule

1. Inspect the repository and existing temporary acquisition directories first.
2. Use official metadata, documentation, schemas, HTTP headers, byte ranges,
   streaming parsers, or small extracts whenever they can answer the question.
3. Do not download a large microdata archive merely to discover its schema or
   availability.
4. A bulk archive is opt-in only when its exact size and purpose are known,
   the user has approved the acquisition, and there is a cleanup or retention
   plan.
5. Keep downloaded source data outside Git; commit only scripts, hashes,
   compact derived outputs, and source-traceable writeups.

## Size gates

| Estimated transfer | Default action |
|---:|---|
| ≤ 25 MB | May retrieve when directly necessary; record URL and hash if retained |
| > 25 MB and ≤ 100 MB | Ask before downloading; prefer a range request or small extract |
| > 100 MB | Do not retrieve without explicit approval and a stated cleanup plan |

If a server does not expose a reliable size, treat the transfer as unknown and
do not follow it beyond a small probe. A partial or interrupted archive is not
an analysis input and must not be presented as a valid dataset.

The read-only checker
[`scripts/check_acquisition_resource_policy.py`](scripts/check_acquisition_resource_policy.py)
can inspect a file or temporary directory before analysis:

```bash
python3 scripts/check_acquisition_resource_policy.py /tmp/acquisition-dir
```

It reports `allow`, `ask`, and `block` files and exits nonzero only when a file
exceeds the blocking threshold. For directory checks it also reports total
bytes and the five largest files, so a collection can be reviewed for storage
impact even when no individual file crosses the blocking threshold.

## Evidence and cleanup record

For every retained external artifact, record its official URL, retrieval date,
size, checksum when practical, file role, and whether it is required for a
published estimate. Temporary downloads must be removed after the analysis
unless the user explicitly requests retention. Removing a temporary file does
not remove its derived, source-traceable result from the repository.

## Current consequence for open gates

The PSID and full SIPP replicate-file routes remain acquisition gates. Existing
local derived SIPP outputs and scripts can be reviewed or validated without
retrieving bulk files. New estimates requiring absent replicate weights or
account-gated PSID files must remain unpromoted until the relevant input is
available under the size rule above.
