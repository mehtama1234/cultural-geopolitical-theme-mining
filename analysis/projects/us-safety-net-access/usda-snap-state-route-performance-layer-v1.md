# USDA SNAP state route-performance layer: participation, processing, and access are different signals

**Status:** bounded descriptive comparison; not a causal estimate  
**Updated:** 2026-09-14  
**Geography:** 50 states and the District of Columbia  
**Machine extraction:** `analysis/records/usda-snap-state-route-performance-2026.json`  
**Reproduction:** `scripts/analyze_usda_snap_route_state_context.py`

## Question

The preceding state crosswalk showed that FY2025 SNAP participation does not form a simple ranking by state income or mobility exposure. The next question is whether a high or low participation rate can be read as administrative performance. It cannot be read that way from the participation series alone, so this layer puts three related but non-interchangeable administrative/access measures beside the participation rate:

1. **FY2025 SNAP participation:** average monthly participants as a percent of the state population.
2. **FY2025 application processing timeliness (APT):** the share of applications in the FNA timeliness measure processed in time for an opportunity to participate—within 30 days for regular service or 7 days for expedited service, subject to the page's routing and exclusion rules.
3. **FY2025 recertification processing timeliness (RPT):** the share of recertifications in the timeliness measure for which the household had access to its benefit allotment by the normal issuance date. FNA separates client-caused from agency-caused delays in its monitoring framework.
4. **Calendar-year 2023 Program Access Index (PAI):** average monthly participation divided by the number of people with income below 125 percent of the federal poverty line. PAI is a direct-access indicator, but not a strict count of eligible nonparticipants; its ratio can exceed 1.

## What the 51-state/DC comparison shows

| Measure | Period | Unit and universe | Minimum | Median | Mean | Maximum |
|---|---|---|---:|---:|---:|---:|
| SNAP participation | FY2025 | Percent of state population; unweighted state rates | 4.70 | 11.30 | 11.52 | 21.90 |
| Application timeliness | FY2025 | Percent timely among applications subject to APT measure | 61.24 | 87.12 | 84.98 | 97.22 |
| Recertification timeliness | FY2025 | Percent timely among recertifications subject to RPT measure | 25.23 | 93.75 | 90.79 | 99.87 |
| Program Access Index | 2023 | Ratio: average monthly participants / people below 125% FPL | 0.356 | 0.793 | 0.768 | 1.320 |

These ranges make the first boundary visible: a state can have a low participant share and weak route performance, or a high participant share and strong route performance. The measures are describing different stages and denominators, not four interchangeable versions of “access.”

## Cross-measure screen

The unweighted Pearson screens across the 51 state/DC aggregates are:

| Comparison with FY2025 participation | Correlation |
|---|---:|
| Application timeliness | 0.033 |
| Recertification timeliness | 0.211 |
| 2023 Program Access Index | 0.799 |

The near-zero APT association is useful as a warning against treating participation as a proxy for application handling. RPT has a small positive descriptive association, but it is not a causal estimate and is highly sensitive to the unusually low Alaska value and to the fact that the route measures are administrative-quality measures rather than population shares. The PAI association is expected to be much larger because PAI is mathematically built from participation and a low-income population denominator; it should not be presented as independent confirmation of the participation rate.

## Counterexamples that keep the interpretation honest

- **Georgia:** 15.6% participation, but 61.24% APT—the lowest application-timeliness rate among the states/DC in this extraction. High participation does not imply high application-route performance.
- **Wisconsin:** 11.6% participation and 97.22% APT—the highest APT rate. A middling participation share can coexist with strong application processing.
- **Alaska:** 8.8% participation, 64.26% APT, and 25.23% RPT—the lowest route values in the common-state extraction. Low participation is not evidence of low administrative friction.
- **Idaho:** 6.6% participation, 96.30% APT, 99.87% RPT, and 0.482 PAI. Strong route timeliness can coexist with a low participation share, which may reflect need, eligibility, geography, take-up, or population composition rather than a single administrative explanation.
- **District of Columbia:** 20.3% participation and 1.320 PAI, with 85.48% APT and 91.72% RPT. A high participation/access ratio and less-than-top route timeliness can coexist in a dense, distinctive jurisdiction.
- **New Mexico:** 21.9% participation but 92.03% APT. High participation is compatible with comparatively strong application timeliness; participation is not a direct performance score.

## Interpretation for the larger atlas

The useful mechanism is not “administration causes participation” from this crosswalk. The supported claim is narrower: **the public experience of a safety-net system has separate exposure points—whether people participate, whether a new application is processed in time, whether an existing household receives a recertification without an issuance interruption, and how participation compares with a low-income population benchmark.** A household may experience a benefit as unavailable because of a rule, an application delay, a recertification interruption, a documentation burden, geographic distance, or low take-up even when a state-wide participation rate is high.

This distinction connects to the program's broader themes without collapsing them: administrative route quality is part of time and access; route failure can create material costs and perceived institutional unfairness; repeated friction may affect trust or political judgment. Those latter consequences require household or individual evidence and are not identified by this state crosswalk.

## Method and limits

- The extraction joins four official USDA/FNA state tables by state name and retains only the 50 states and DC common to all four tables. Territories are excluded from the comparison rather than silently dropped from a larger “US” claim.
- Participation is FY2025 and both timeliness measures are FY2025; PAI is calendar year 2023. PAI is therefore a historical access context, not a same-year independent predictor.
- APT and RPT have program-specific quality-control universes and routing rules. Their denominators are not the state population and are not interchangeable with the participation denominator.
- The comparison uses unweighted state aggregates. It does not propagate margins of error, adjust for case mix, distinguish urban/rural office structure, model applicant-caused versus agency-caused delays beyond the published measure definitions, or establish causality.
- State-level values cannot establish household-level relationships. A high rate can coexist with concentrated failure among a subgroup, county, language group, or procedural stage.
- The PAI can exceed 1 because its denominator is the population below 125% FPL, not the exact eligible population; it should not be described as a percentage of eligible people served.
- The HTML pages are current source pages as retrieved for this pass; the committed machine record preserves the extracted values and the layer hash, while the official links remain open for later vintage checks.

## Official sources

- [FY2025 SNAP state participation chart data](https://www.ers.usda.gov/media/29462/55416-chart-data-file.xlsx?v=68216)
- [FY2025 SNAP Application Processing Timeliness](https://www.fna.usda.gov/snap/qc/timeliness/apt-fy25)
- [FY2025 SNAP Recertification Processing Timeliness](https://www.fna.usda.gov/snap/qc/timeliness/rpt-fy25)
- [SNAP Program Access Index](https://www.fna.usda.gov/snap/qc/pai)
- [USDA/FNA SNAP efficiency and effectiveness measures](https://www.fna.usda.gov/snap/qc)

