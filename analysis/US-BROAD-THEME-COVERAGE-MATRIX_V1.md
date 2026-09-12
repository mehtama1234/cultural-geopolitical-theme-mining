# US broad theme coverage matrix v1

**Purpose:** preserve the full program as a multi-level research map. This
matrix prevents the currently active dataset or bridge from becoming the
definition of the project.

**Status key:** `Observed` means a source directly measures the named unit and
outcome; `Reported` means a source reports an experience or estimate;
`Compared` means separate groups or source layers have been aligned;
`Open` means the next arrow is not measured well enough.

| Theme | Current evidence anchor | Level actually measured | Current status | Missing end-to-end link / next test |
|---|---|---|---|---|
| Household room and consumption | [Price/payment bridge](bridges/us-price-payment-household-room-v1.md); [2025 SHED price-adaptation layer](projects/us-household-financial-pressure/shed-2025-price-adaptation-layer-v1.md); [USDA 2024 food-security layer](projects/us-food-budget-security/usda-2024-food-security-layer-v1.md); SIPP Fay-BRR layers | Person, consumer unit, product, household record | Compared / Reported | Join a defined price or payment shock to spending, food security, debt, substitution, and recovery; keep the protected and sacrificed needs separate. |
| Time as a hidden price | [ATUS 2024 time layer](projects/us-household-calendar-integration/atus-2024-time-hidden-price-layer-v1.md); [NHTS transport comparison](projects/us-household-calendar-integration/nhts-transport-comparison-v1.md); [2025 SHED price-adaptation layer](projects/us-household-financial-pressure/shed-2025-price-adaptation-layer-v1.md); caregiving and multiple-job packets | Person, diary day, trip, worker, household | Reported / Compared | Measure waiting, travel, care, paperwork, and service effort against the time or money they displace. |
| Consumer power and recourse | [Service/platform bridge](bridges/us-service-platform-recourse-trust-v1.md); [CFPB complaint layer](projects/us-customer-automation-recourse/cfpb-complaint-response-descriptive-layer-v1.md); [state-normalized CFPB layer](projects/us-customer-automation-recourse/cfpb-state-population-normalized-layer-v1.md); FTC findings | Customer case, platform user, complaint, firm, place | Compared / Reported | Follow contact → repeat effort → remedy or abandonment → switching, trust, or non-use in the same service episode. |
| Platforms, data, and attention | [Pew 2025 news/civic-engagement layer](projects/us-digital-habits-attention/pew-2025-news-civic-engagement-layer-v1.md); privacy, reviews, subscription, marketplace, and platform-data findings | User, respondent, account, transaction, platform, seller | Reported / Compared / Inferred | Verify ranking, data use, identity, attention, and exit effects with independent platform or transaction records. |
| Work, control, and bargaining | [AI work-control project](projects/ai-work-control/README.md); SIPP work transitions; job-lock findings | Worker, task, job, workplace, firm | Compared / Reported | Pair system or benefit exposure with decision rights, schedule, pay, health, worker voice, household security, and bargaining outcome. |
| Care, health, and social reproduction | [Health-cost paper scan](projects/us-health-cost-household-choice/paper-scan-v1.md); [USDA 2024 food-security layer](projects/us-food-budget-security/usda-2024-food-security-layer-v1.md); [2025 SHED price-adaptation layer](projects/us-household-financial-pressure/shed-2025-price-adaptation-layer-v1.md); caregiving and medical-debt findings | Person, caregiver, household, health event | Reported / Compared | Follow care or food need → price/coverage/travel → care, diet, and unpaid time → work, debt, health, and family outcome. |
| Housing, place, and mobility | [Housing/energy/insurance bridge](bridges/us-housing-energy-insurance-place-v1.md); [local business formation/place layer](projects/us-local-business-place/local-business-formation-place-layer-v1.md); SIPP tenure/resource layer; NHTS | Home, person, trip, ZIP/year, disaster event, county, firm | Compared / Reported | Link risk or bill and business change to repair, coverage, credit, health, services, move/stay, and recovery for comparable places or properties. |
| Unequal exposure and status | SIPP tenure × resource estimates; discrimination, local-price, disability, age, and migration packets | Person, household, place, customer, worker | Compared | Test whether exposure, treatment, remedy, and exit differ by intersecting status and available alternatives, not just by one demographic axis. |
| Trust, identity, and cultural meaning | [Pew 2025 news/civic-engagement layer](projects/us-digital-habits-attention/pew-2025-news-civic-engagement-layer-v1.md); [Cost/trust/politics scan](projects/us-cost-trust-politics/paper-scan-v1.md); privacy, fraud, reviews, and habit findings | Respondent, customer, survey wave, community, source ecosystem | Reported / Compared / Open | Measure the interpretation between material experience and action: dignity, blame, belonging, institutional trust, and changing norms. |
| Public systems and policy feedback | [Public-aid bridge](bridges/us-public-aid-interpretation-political-response-v1.md); [safety-net administrative-burden layer](projects/us-safety-net-access/administrative-burden-access-layer-v1.md); benefit, utility, eviction, and assistance findings | Person, household, program spell, agency, place, census tract | Compared / Reported | Add notice, eligibility, burden, application, denial, take-up, timing, interruption, and later institutional demand or behavior. |
| Political judgment and collective action | [ANES 2024 political judgment layer](projects/us-cost-trust-politics/anes-2024-political-judgment-layer-v1.md); [Pew 2025 news/civic-engagement layer](projects/us-digital-habits-attention/pew-2025-news-civic-engagement-layer-v1.md); [safety-net administrative-burden layer](projects/us-safety-net-access/administrative-burden-access-layer-v1.md); economic-voting, benefit-sentiment, fiscal-news, employer-politics, and inflation-belief findings | Respondent, source ecosystem, program episode, county, election, campaign/event | Compared / Open | ANES aligns financial worry with judgment, trust, institutional meaning, reported vote, and post-election legitimacy; Pew adds distinct participation and source-environment types; safety-net evidence adds a route-to-help mechanism; exact exposure, attribution, information, and causal action path remain open. |
| Firm, sector, and market power | [Local business formation/place layer](projects/us-local-business-place/local-business-formation-place-layer-v1.md); company bridges, [CFPB complaint layer](projects/us-customer-automation-recourse/cfpb-complaint-response-descriptive-layer-v1.md), payment/insurance/utility/platform findings, SEC/industry records | Firm, product, market, worker, owner, community, county | Reported / Compared | Record when a firm decision shifts price, waiting, access, risk, or data to customers, workers, owners, or public systems—and who can resist. |
| Infrastructure, technology, and dependency | [AI capability/dependence layer](projects/ai-work-control/ai-capability-dependence-layer-v1.md); [AI macro/infrastructure packet](projects/ai-work-control/macro-infrastructure-source-packet-v1.md); Romania/Malaysia cases | Firm, datacenter, grid, public system, sector, country | Reported / Compared / Inferred | Compare ownership, power/water burden, data location, local skills, interoperability, provider switching, and realized public capability. |
| Geopolitical and state consequences | [AI capability/dependence layer](projects/ai-work-control/ai-capability-dependence-layer-v1.md); [AI infrastructure case record](projects/ai-work-control/romania-malaysia-ai-infrastructure-case-record-v1.md); tariff, trade, energy, finance, and migration packets | Sector, commodity, firm, infrastructure project, country | Reported / Compared / Open | Trace domestic distribution and industrial capacity into state dependence, alliance leverage, strategic choice, and external response without inventing a household-to-state join. |

## How to use it

Each new topic should be assigned to one or more rows, then tested across
adjacent levels. A source can populate a row without completing its chain.
When a link is missing, write the missing unit, time window, and actor before
adding another narrative source. Cross-source alignment is useful for context
but is not a person-, household-, or firm-level join.

## Current program-wide gaps

- Same-unit longitudinal records are scarce at the transition from material
  pressure to interpretation and political action.
- Firm success, public-program delivery, and service restoration are often
  measured without the recipient's later security, remedy, or exit.
- Cultural meaning is frequently inferred from hardship, sentiment, or media
  rather than measured directly.
- Infrastructure and geopolitical records show capability and exposure, but
  rarely the distribution of local gains, costs, and replaceability.
- Every theme needs counterexamples, subgroup distributions, source methods,
  and explicit uncertainty before it can support a settled claim.

The [theme inventory](US-BROAD-THEME-INVENTORY_V1.md) defines the scope; the
[evidence matrix](US-BROAD-EVIDENCE-MATRIX_V1.md) assigns arrows and methods;
the [recovery brief](../END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md) preserves the
objective after a crash.
