# HTOPS wave-overlap audit: retained files do not form a new panel

**Status:** storage-light acquisition/design audit · **Checked:** 2026-09-19

## Result

The retained February 2025, June 2025, and March 2026 HTOPS/HPS public-use
files all contain `SCRAMID`, but their identifiers do not overlap:

| Pair | Rows | Shared `SCRAMID` |
|---|---:|---:|
| February 2025 × June 2025 | 6,740 × 7,485 | 0 |
| June 2025 × March 2026 | 7,485 × 12,521 | 0 |
| February 2025 × March 2026 | 6,740 × 12,521 | 0 |

This is a useful negative result. A shared identifier column does not mean
that independently sampled waves can be joined. The existing April-to-June
2025 cross-lagged analysis is a separate retained cohort and should not be
quietly extended to these files.

## What this prevents

The wave files cannot support a new same-respondent claim about whether
expense difficulty, trust, food security, work loss, or search behavior changed
between these dates. Comparing their marginal distributions would be a
cross-sectional vintage comparison, not a longitudinal transition.

The zero intersection does not mean people changed, recovered, or disappeared.
It only establishes that these retained public-use files do not provide a
common respondent key for the proposed join. The [reproduction script](../../../scripts/audit_htops_wave_overlap.py)
records the file hashes, row counts, and pairwise intersections without
retaining respondent data in the repository.

## Next route

Additional same-person work requires a documented common-cohort release or an
authorized longitudinal file. Until then, keep the existing April-to-June
linked result bounded and treat these waves as separate cross-sectional
context. The machine-readable counts are in the [overlap audit](data/htops-wave-overlap-audit-2025-2026.json).
