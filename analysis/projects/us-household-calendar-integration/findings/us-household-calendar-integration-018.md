# SNAP status and child-care work loss belong to the same material-time chain, but not the same causal episode

## The bounded finding

The 2025 SIPP public-use extraction pairs each identified person's November and
December SNAP status with annual fall child-care fields. Among 2,295 valid
November-to-December stable no-SNAP pairs, 3.42% reported that child-care
arrangements prevented them from working or working more (Fay-BRR SE 0.45;
95% CI 2.54–4.30). Among 351 stable-SNAP pairs, the corresponding share was
7.43% (SE 1.88; 95% CI 3.75–11.11).

Among the small valid time-loss cells, stable no-SNAP respondents reported
hours, days, and weeks as the type of time lost in shares of 38.52%, 49.94%, and
11.55%. Stable-SNAP respondents reported 48.83%, 34.95%, and 16.22%. The stable
SNAP time-loss denominator was only 23 records, so these are broad descriptive
profiles, not precise rankings.

## What the same-person bridge adds

The comparison keeps a person-level November-to-December SNAP transition
anchor while connecting it to work and child-care constraints:

`SNAP status at t → reported child-care work prevention/time-loss field → paid-work capacity`

That is more informative than placing SNAP participation and child-care
statistics in unrelated populations. It shows that stable program status and
reported child-care work constraint can coexist in the same extracted person
frame, and that the stable-SNAP cell has a higher descriptive work-prevention
share.

It does not show that SNAP caused child-care loss, that receipt solved or
worsened care constraints, or that the reported fall time loss occurred in
December. The child-care questions refer to the fall reference year and are
carried into monthly records; the SNAP pair is an adjacent-month status bridge.

## Why the route remains unresolved

The result does not observe child-care price, provider availability, work
schedule control, employer response, exact hours lost, the date of the care
problem, benefit amount/timing, notice, application effort, or whether a family
used paid care, family help, schedule changes, or missed work instead. Stable
SNAP status can also mark different household composition, income, employment,
eligibility, disability, and care needs.

The entry and exit groups contain only 4 and 2 valid work-prevention records and
no valid time-loss cases. They remain visible as sparse cells rather than being
converted into zeroes or omitted from the transition frame.

## What this contributes to the end-to-end atlas

This layer strengthens one middle segment of the long-term chain:

`material pressure / public support → care and schedule constraint → paid work or time loss → later security and meaning`

The first and last arrows remain open. The evidence supports preserving care,
work, SNAP receipt, and time loss as separate stages with their own universes.
It does not support a single “benefit success,” “child-care burden,” or
household-security score.

## Reproduction and controls

The analysis was rerun on 2026-09-14 against 379,215 rows from the current
local `full-v15` SIPP slice and the 240-replicate `rw2025.csv` archive. It matched
31,335 replicate pairs and exactly reproduced the committed point estimates and
standard errors. The flag-inclusive rerun uses `AWORKMORE`, `ATIMELOST`, and
`ATIMELOST_TP`; unavailable and non-applicable codes remain excluded.

The method is descriptive Fay-BRR with perturbation factor 0.5. The source
record preserves weighted denominators, unweighted valid counts, confidence
intervals, missingness boundaries, and the non-causal interpretation.

## Sources and limits

- [Machine-readable SIPP record](../../../records/us-sipp-snap-childcare-time-loss-2024.json)
- [Detailed SIPP layer](../sipp-snap-childcare-time-loss-layer-v1.md)
- [SIPP 2025 public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP 2025 data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [Same-episode public-system event-ledger design](../../us-safety-net-access/same-episode-event-ledger-design-v1.md)

The next test is a dated care/work episode with provider or family alternatives,
schedule control, SNAP notice/effort/amount, work outcome, and later recovery or
interpretation. Until those fields are linked, this remains a reproducible
material-time bridge rather than a causal or political finding.
