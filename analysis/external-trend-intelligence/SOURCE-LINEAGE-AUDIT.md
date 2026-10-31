# Source-lineage audit — first candidate wave

**Manifest:** `observation-manifest.json`
**Candidate set:** `candidate-comparisons.json`
**Status:** Candidate 1 partially reviewed; Candidates 2–4 remain unreviewed.

## Duplicate URL findings

Only Candidate 1 contains repeated URLs in the selected evidence records:

| URL | Count | Assessment |
|---|---:|---|
| `https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2025-10-31.htm` | 2 | Generic Fair Work Commission bulletin/index page; not enough to show the two records share the same case or evidence. |
| `https://www.fwc.gov.au/hearings-decisions/find-decisions-and-orders` | 3 | Generic decision-search page; navigation locator, not a unique source artifact. |

The duplicate URLs are generic navigation pages rather than unique case or
study locators. They must not be counted as independent confirmation, but they
also do not prove that the underlying records are duplicates. The record-level
source URLs and retrieval hashes remain the authority for deciding that.

## Candidate 1 partial review

The seven selected records identify seven distinct primary artifacts:

- four separate Fair Work Commission cases (`2025 FWC 3176`, `2026 FWC 48`,
  `2025 FWC 3111`, and `2024 FWC 3523`);
- one Fair Work Ombudsman Atkins enforcement follow-up;
- one GSMA ASEAN Consumer Scam Report 2026; and
- one British Social Attitudes 43 NHS report.

This supports `partially_reviewed` lineage for Candidate 1. It does not make
the four FWC cases independent institutions, and it does not establish that
the reports use unrelated underlying datasets. Publisher-level and study-level
independence remain open.

## Independence decision

Candidates 2–4 remain `independence_status: unverified` because:

- a different host can republish the same study, dataset, press release, or
  institutional claim;
- a generic page can hide the specific document used by the record; and
- the current compact manifest does not carry a full publisher lineage graph,
  citation chain, or study-level replication identity.

## Required next review

For each candidate, inspect the underlying source packet or record and add:

1. publisher and originating institution;
2. study, dataset, case, filing, or event identifier;
3. exact source artifact locator and retrieval hash;
4. whether another record cites the same underlying artifact;
5. whether the observation is a replication, extension, comparison, or only a
   restatement; and
6. a source-independence result: `independent`, `dependent_restatement`,
   `same_artifact`, or `unknown`.

Until that review is complete, host and URL counts are discovery coverage—not
confirmation strength.
