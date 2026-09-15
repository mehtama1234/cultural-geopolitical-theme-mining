# Participation is not administrative performance

## The short finding

State SNAP participation tells us how many people are receiving benefits relative to the state population. It does not tell us whether a new application was processed on time, whether a returning household received a recertification without an issuance interruption, or how participation compares with a low-income population benchmark.

The FY2025 state data make that distinction concrete. Across the 50 states and the District of Columbia, application timeliness ranges from 61.24% to 97.22%, while participation ranges from 4.7% to 21.9%. The unweighted correlation between the two state-level measures is only 0.033. Recertification timeliness ranges from 25.23% to 99.87%, with a 0.211 correlation to participation. These are not evidence that administration has no effect; they are evidence that participation cannot stand in for route performance.

## Four different questions hiding inside “access”

| Question | Measure used here | What it can say | What it cannot say |
|---|---|---|---|
| How large is the participating population? | FY2025 SNAP participant rate | Relative population exposure to SNAP receipt | Whether applications or renewals were handled well |
| Did a new applicant receive an opportunity in time? | FY2025 Application Processing Timeliness | Route performance for applications in the official APT universe | Whether everyone in need applied, qualified, or stayed enrolled |
| Did a renewing household retain access by the normal date? | FY2025 Recertification Processing Timeliness | Route performance for recertifications in the official RPT universe | Whether a household faced other barriers or whether the benefit was adequate |
| How does participation compare with a low-income benchmark? | 2023 Program Access Index | A broad direct-access context | Exact eligible take-up; it can exceed 1 and is from a different period |

The denominator is the argument. The state population, the APT case universe, the RPT case universe, and the population below 125% of the federal poverty line are not the same population. Treating their rates as if they were interchangeable produces a clean-looking but invalid story.

## The counterexamples

**Georgia** has 15.6% participation but 61.24% application timeliness, the lowest APT value in the common state/DC extraction. A high participant share does not mean that the entry route is working smoothly.

**Wisconsin** has 11.6% participation and 97.22% application timeliness, the highest APT value. A middling participant share can coexist with very strong application-route performance.

**Alaska** has 8.8% participation, 64.26% APT, and 25.23% RPT. Low participation is not evidence that the administrative path is low-friction; in this extraction Alaska has the weakest values on both route measures.

**Idaho** has 6.6% participation, 96.30% APT, 99.87% RPT, and a 0.482 PAI. Strong processing timeliness can coexist with a low participant share. That combination could reflect lower need, eligibility composition, geography, take-up, or population structure; it does not identify one explanation.

**The District of Columbia** has 20.3% participation and a 1.320 PAI, alongside 85.48% APT and 91.72% RPT. A high participation/access context can coexist with route performance that is not at the top of the state distribution.

## Why the access-index correlation is different

The 2023 PAI has a 0.799 unweighted correlation with FY2025 participation in the matched state/DC screen. That is not surprising: PAI is constructed from average monthly participation divided by a low-income population denominator. It is useful as a benchmark for direct access, but it is not an independent administrative-performance measure and should not be used to “validate” the participation rate.

The 2023 PAI ranges from 0.356 in Wyoming to 1.320 in DC. A value above 1 does not mean that more than 100% of eligible people received SNAP. The denominator is people below 125% of the federal poverty line, not the exact eligible population, and eligibility rules and composition differ.

## What this adds to the wider theme atlas

The finding is about the route through an institution. A household can experience the safety net as unavailable because it cannot complete an application, waits beyond a useful deadline, loses access during recertification, lacks required documentation, cannot reach the relevant office or channel, or does not take up a benefit despite being near the income benchmark. Those are different forms of friction even when they end in the same observed state participation rate.

This gives the larger program a more disciplined mechanism chain:

`material need or eligibility context → application/renewal route → delay, interruption, or receipt → time, money, and perceived institutional treatment → possible adaptation or judgment`

The state crosswalk supports the first three links only at an aggregate descriptive level. It does not prove that administrative friction changes trust, voting, organizing, or cultural meaning. Those downstream links require household, survey, qualitative, or longitudinal evidence and must be joined separately.

## Method and limits

- The extraction uses official USDA FY2025 participation chart data, official FNA FY2025 APT, official FNA FY2025 RPT, and the official FNA 2023 PAI table.
- It keeps 50 states and DC common to all four tables and excludes territories from the comparison rather than silently mixing geographies.
- The route measures use program-specific quality-control universes and definitions. APT concerns timely opportunity to participate; RPT concerns access to the benefit allotment by the normal issuance date.
- The reported correlations are unweighted Pearson screens across 51 state/DC aggregates. They are not causal estimates, do not adjust for case mix, and do not transfer to households.
- The periods are not all identical: participation, APT, and RPT are FY2025; PAI is calendar year 2023.
- The extraction does not identify county, office, language, disability, household, or applicant/agency subgroup disparities. It also does not measure benefit adequacy, food security, or procedural denials in the same state universe.

## Sources and reproducibility

- [Detailed route-performance layer](../usda-snap-state-route-performance-layer-v1.md)
- [Machine-readable observation record](../../../records/usda-snap-state-route-performance-2026.json)
- [Reproduction script](../../../../scripts/analyze_usda_snap_route_state_context.py)
- [FY2025 USDA state participation chart data](https://www.ers.usda.gov/media/29462/55416-chart-data-file.xlsx?v=68216)
- [FY2025 FNA Application Processing Timeliness](https://www.fna.usda.gov/snap/qc/timeliness/apt-fy25)
- [FY2025 FNA Recertification Processing Timeliness](https://www.fna.usda.gov/snap/qc/timeliness/rpt-fy25)
- [FNA Program Access Index](https://www.fna.usda.gov/snap/qc/pai)
