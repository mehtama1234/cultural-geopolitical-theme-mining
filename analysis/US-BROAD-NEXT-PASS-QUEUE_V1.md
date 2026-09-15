# US broad program next-pass queue v1

**Checked:** 2026-09-15
**Purpose:** keep breadth across the 14-theme program while choosing depth that can change a claim
**Status:** execution queue; not a claim that any open link has been established

**Coverage checkpoint (2026-09-15):** the source-registry audit now finds all
114 registered source domains represented outside source-search packets; 106
have exact registered-URL references. The trend registry holds 241 records and
926 observations.
The reverse audit shows 28 observed domains outside registered families; these
remain a review queue because many are mirrors, delivery hosts, or one-off
citations rather than durable source families.
This confirms breadth coverage, not that every source has closed its open
behavior, meaning, institutional, or geopolitical arrow.

The [program continuity ledger](US-BROAD-PROGRAM-CONTINUITY-LEDGER_V1.md) is
the durable long-term control record. This queue selects the next empirical
pass; it does not narrow or complete the program.

The reader-facing [source family map](../site/source-registry.html) now makes
the 114 recurring source families, their roles, evidence types, and
interpretation limits searchable. The financial-capacity review confirms that
the existing BEA, Federal Reserve, OFR, IMF FAS, World Bank Findex, SHED, and
New York Fed layers are complementary but not joinable into a new household
estimate without a shared person/account event key. The next pass therefore
must acquire or identify that dated event rather than restate provider,
macro, and survey aggregates as one causal story.

This queue is the handoff from the current evidence map to the next empirical
passes. Every pass must identify the unit, date, geography, denominator,
missingness, uncertainty, and arrow status. A source can deepen one arrow
without completing the societal chain.

## Active continuation checkpoint

The program has completed broad anchor passes across all 14 themes and has
recently added depth in four rotating lanes: household adaptation and care;
time, work, and life-stage distribution; local business and service capacity;
and migration, place, and infrastructure/state dependence. These passes are
cross-source comparisons and bounded same-respondent analyses where the data
permit. They do not yet establish a single population-wide causal chain.

The reader layer now has dedicated routes for material/time/care linkage,
political meaning across scales, AI use/work/contact/exit, public help and
judgment, and housing/insurance/energy pressure. These routes are presentation
artifacts built from the validated records; they do not add new estimates or
close the same-unit event arrows. The authenticated PSID package remains
absent, while the 2025 SIPP archive, replicate-weight archive, and derived
full-file slice are available outside Git under `/tmp/us-broad-sipp-2025/`.
The utility-to-following-work screen has now been rerun from that full slice
and reproduces its committed point estimates and intervals. A follow-on
utility/tenure/child-care comparison now supplies the compatible annual
`EWORKMORE` universe while preserving its mixed-clock boundary. The next SIPP
gate is therefore a dated bill/service event or the stronger authenticated
PSID acquisition, followed by explicit universe, retention, missingness,
weighting, and timing checks.

The next active pass is **material/time/care linkage**, documented in the
[acquisition plan](projects/us-household-calendar-integration/material-time-care-linkage-acquisition-plan-v1.md)
and now operationalized by the [PSID extract specification](projects/us-household-calendar-integration/psid-material-time-care-extract-spec-v1.md).

### ILOSTAT comparison gate

ILOSTAT remains an open international comparison route for labor-force
participation, unemployment, working poverty, earnings, and youth exclusion.
The official catalog and bulk documentation are available, but the prior
candidate request returned zero bytes and the 2026-09-14 direct-route recheck
returned HTTP 404 HTML responses rather than CSV/GZIP data. No estimate is
promoted until the payload, indicator definition, source basis, reference area,
revision status, and matching US comparison are captured. See the
[ILOSTAT access audit](projects/ai-work-control/ilostat-access-audit-2026-09-15.md)
for the bulk and Rilostat API/RDS observations. The API metadata and RDS
routes also returned HTTP 200 with zero-byte `application/octet-stream`
responses; this is recorded as a delivery failure, not an empty dataset.
Its purpose is to
identify which missing variables prevent the existing evidence from becoming
an end-to-end societal result:

1. a dated bill, price, care need, rule, or work change;
2. the person or household's alternatives and schedule control;
3. the money and time response, including paid or unpaid substitution;
4. the protected and sacrificed outcomes; and
5. recovery, trust, collective action, or exit at a defined follow-up.

Until a same-unit or valid matched design supplies those fields, the safe
output is a measured distribution, an explicit comparison, or an acquisition
gap—not a claim that one cost caused one cultural or political outcome.

The [RECS household energy-burden layer](projects/us-household-calendar-integration/recs-energy-burden-household-layer-v1.md)
now supplies a same-household energy expenditure and assistance screen. The
next energy step is to connect this material vulnerability to dated bills,
housing tenure, health/care use, work or time substitution, and later trust or
political action; the 2020 RECS cross-section cannot establish those links.

The [MEPS Panel 27 health-cost longitudinal layer](projects/us-household-calendar-integration/meps-panel27-health-cost-longitudinal-layer-v1.md)
now supplies a repeated health-cost and coverage endpoint. The next material/
health step is to join valid panel health-cost change to care/time allocation,
employment, household resources, and treatment or work continuity, while
retaining the distinction between total expenditure, out-of-pocket spending,
coverage, and perceived health.
The [MEPS non-synchronization finding](projects/us-health-cost-household-choice/findings/us-health-cost-household-choice-001.md)
now records the interpretation and the counterexample: lower paired
out-of-pocket spending does not prove better health or lower total burden. The
next pass must add treatment continuity, unpaid care/time, employment, debt,
and food/housing trade-offs with design-based uncertainty.

The [2024 GSS financial-position and trust/politics layer](projects/us-cost-trust-politics/gss-2024-financial-position-trust-politics-layer-v1.md)
now supplies a same-respondent cross-sectional bridge from financial position to
trust, fairness, ideology, and vote intention. The next politics step is a
harmonized repeated-year or panel design with measured exposure and prior
identity, followed by direct action, institutional-response, and recovery
outcomes; this GSS layer is a co-occurrence screen only.
The [financial dissatisfaction/trust finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-012.md)
records the meaning boundary and counterexamples: distrust is not withdrawal,
and vote intention is not a measured response to a dated financial event. The
next pass must harmonize repeated years or use a timed panel with prior party
identity, attribution, civic action, and institutional response.

The [historical GSS financial/trust layer](projects/us-cost-trust-politics/gss-financial-trust-historical-layer-v1.md)
adds anchor-year context from 1972–2024. The next historical step is formal
harmonization of question availability, mode, weights, and covariate-adjusted
comparisons; the current layer deliberately avoids presenting the anchor years
as an unbroken causal trend. The new [historical GSS finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-024.md)
promotes that boundary into the reader-facing finding set: the within-year
financial-satisfaction/trust gradient recurs, while overall levels and gap size
move across decades. The next test remains harmonized repeated-year or timed
event evidence with prior identity, attribution, action, and recovery.

The new [household-room resource/tenure/liquidity finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-032.md)
keeps four adjacent but non-pooled surfaces visible: SIPP resource bands,
tenure-conditioned payment difficulty, SHED emergency-liquidity routes, and
consent-linked credit-balance change. It sharpens the material/time/care
extract specification by naming the missing middle—dated event, available
alternatives, payment or substitution choice, protected/sacrificed outcome,
and recovery—while preserving the PSID access gate as the next stronger test.

The [PSID 2023 field-audit finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-036.md)
now verifies the candidate backbone at the codebook level: the 2023 Family
File documents paid work, household labor, care, time pressure, health,
income, wealth, insurance, and utilities. The next pass is no longer field
discovery; it is the executed 2019/2021/2023 file audit with valid denominators,
weights, attrition, imputation handling, and first descriptive cells.

The new [multi-clock material/time/care synthesis](projects/us-household-calendar-integration/findings/us-household-calendar-integration-033.md)
adds the end-to-end reader frame: SIPP monthly resource/work transitions,
MEPS annual health-cost and health-status transitions, and SHED/ATUS care and
time surfaces are complementary clocks. The next acquisition remains a
same-person or same-family design that observes the dated trigger, alternative,
time/care substitution, protected or sacrificed outcome, recovery, and later
meaning/action without pooling incompatible samples.

The new [MEPS expenditure-conditioned finding](projects/us-health-cost-household-choice/findings/us-health-cost-household-choice-002.md)
adds a same-panel conditioning test: baseline total health-expenditure bands
have different perceived-health and employment-continuity profiles. Because
spending is also a marker of health need, age, retirement, insurance, and
service mix, the next acquisition must add treatment continuity, out-of-pocket
burden, unpaid care/time, debt, and baseline employment rather than promote a
health-cost causal effect.

The new [CMS-to-MEPS household health-cost synthesis](projects/us-health-cost-household-choice/cms-meps-household-health-cost-end-to-end-synthesis-v1.md)
places CMS national spending, payer and sponsor architecture beside MEPS
person-level expenditure, coverage, health, work, income, and utilization
transitions. It closes a presentation and interpretation gap between system
scale and household evidence without claiming a same-bill care decision,
medical-debt episode, unpaid-care substitution, trust response, or political
action. The next acquisition remains an event-oriented same-household route
with a dated need or bill, care decision, substitution, recovery, and
institutional response.

The new [public-system route-to-judgment synthesis](projects/us-safety-net-access/findings/us-safety-net-access-014.md)
rotates the program into the public-systems lane. It places administrative
timeliness, recipient-reported notice/time barriers, SIPP following hardship,
and Gallup institution-specific confidence into one bounded architecture. The
next acquisition remains a same-case episode record with notice, effort,
decision, amount/timing, interruption, remedy, material result, judgment, and
action; the WBNS respondent-file gate remains open.

The new [CFPB route-vintage audit](projects/us-customer-automation-recourse/findings/us-customer-automation-recourse-021.md)
rotates depth into consumer power. It tests the live API's two clocks—timely
label versus derived receipt-to-company-send lag—and audits the disappearance
of the narrative field in the current response surface. The next acquisition
must hold field definitions constant and add account exposure, effort, verified
correction, repeat contact, switching, and exit.

The new [USAspending supplier-concentration finding](projects/ai-work-control/findings/ai-work-control-072.md)
rotates depth into infrastructure/geopolitical capacity. It turns the
JASSM/LRASM recipient count into a concentration and repeat-recipient test,
showing why supplier-name breadth is not replaceability. The next pass must
link recipient names to parents, facilities, milestones, output, acceptance,
and substitute qualification before calling the network resilient or leveraged.

The new [official entity-parent-facility reconciliation finding](projects/ai-work-control/findings/ai-work-control-076.md)
adds the next bounded identity step. DLA CAGE records resolve the BAE route
from the reported Merrimack recipient through BAE Systems, Inc. to BAE Systems
plc, and resolve General Dynamics-OTS facilities through General Dynamics
Corp. The hierarchy sharpens jurisdiction and facility questions, but does not
assign the JASSM/LRASM work to a plant or establish workforce, production,
acceptance, delivery, replaceability, or leverage. The next pass must join
exact CAGE/UEI identifiers to procurement transactions and then trace facility
assignment, output, acceptance, and alternatives.

The follow-up [recipient-identifier ambiguity audit](projects/ai-work-control/findings/ai-work-control-077.md)
tests that join rather than assuming it. USAspending's official recipient
endpoint returns 17 BAE rows across 10 UEIs and three General Dynamics-OTS
rows, while the retained subaward rows contain no UEI/CAGE. One General
Dynamics UEI overlaps the selected DLA facility set, but this is not proof of
the selected subaward's plant assignment. The next acquisition must obtain an
identifier-bearing award/subaward or performance record and preserve endpoint
denominators, identifier vintage, component, production, acceptance, and
delivery fields separately.

The richer [subaward-to-UEI and location finding](projects/ai-work-control/findings/ai-work-control-078.md)
advances that gate. An official award-search route exposes a subrecipient UEI,
recipient location, and primary performance place for all 74 rows. The BAE
selected row resolves to `V7X9P6J9SUK1` in Nashua, NH; the General
Dynamics-OTS row resolves to `KZK8C85C1T94` in Niceville, FL. This closes the
recipient-identity/reporting-location link, not the CAGE-to-plant,
production-to-acceptance, delivery, or replaceability links. The next pass
must reconcile those UEIs to facilities and performance records without
collapsing reported location into manufacturing site.

The [facility-capability context finding](projects/ai-work-control/findings/ai-work-control-079.md)
adds independent capability evidence at both reported locations. BAE's
official certificate names 95 Canal Street, Nashua within a military-electronics
production/servicing scope; General Dynamics-OTS material names Niceville
Operations and warhead capability. The next pass must still obtain a
site-specific work-package, production, acceptance, delivery, or audit record;
capability context is not a JASSM/LRASM production assignment.

The [realization-stage milestone finding](projects/ai-work-control/findings/ai-work-control-080.md)
adds a dated support/capacity/test layer. DoD records a $999M JASSM/LRASM
production-support IDIQ; Lockheed reports capacity investment and ramp-up; and
its 2026 release records completion of the first F-35C LRASM flight-science
phase. The next pass must locate accepted quantities, shipment/delivery,
fielding, inventory, or maintenance records rather than treat production
support or flight testing as delivered capability.

The [Poland JASSM-ER delivery non-observation](projects/ai-work-control/findings/ai-work-control-081.md)
rechecks that customer arrow. The official Polish page still states a
2026–2030 delivery window, while a separate briefing states 2028–2030; no
reviewed official source reports a delivered quantity, acceptance, fielding,
training, or inventory change for the 2024 order. The next pass must search
lot-level, base-level, exercise, acceptance, and inventory records without
turning this non-observation into a claim of non-delivery.

The [historical Polish audit-control finding](projects/ai-work-control/findings/ai-work-control-082.md)
adds an implementation-control layer without turning accounting evidence into
delivery evidence. NIK reports that a JASSM-ER production-cost settlement was
supported by milestone/process material lacking a numeric value tied to the
settlement; a separate 32-unit delayed-contract example is explicitly not
assigned to JASSM. The next pass should seek the underlying FMS identifier,
later reconciliation, accepted quantity, shipment, fielding, and training
records.

The [FMS timing-asynchrony finding](projects/ai-work-control/findings/ai-work-control-083.md)
adds a cross-program clock: NIK says FMS schedules are estimates and records
four F-35 deliveries before the related settlement forms arrived. This does not
close the JASSM-ER arrow, but it changes the acquisition design: search
separately for shipment, acceptance, settlement, fielding, training, and use.

The new [comparative worker-control finding](projects/ai-work-control/findings/ai-work-control-068.md)
adds the worker-side JRC survey and ILO social-dialogue case layer to the US
NBER/OECD/BLS bridge. It makes the missing conversion explicit: information or
collective voice is not control until it changes a deployment rule, data limit,
consent condition, workload, appeal, or remedy. The next AI/work pass remains
a same-workplace US implementation event with exposure, worker outcomes, and
durable enforcement; the comparative sources are mechanism evidence, not US
population estimates. The new [WageIndicator IBM agreement finding](projects/ai-work-control/findings/ai-work-control-074.md)
adds a concrete institutional-design case: human decision boundaries, a
risk-based AI taxonomy, correction loops, fairness review, works-council
inspection rights, and retraining provisions are visible in the written rule.
It does not establish implementation, enforcement, or worker outcomes. The
next worker-control pass should compare this written architecture with an
implementation artifact, such as a system inventory, review record, audit,
correction log, or worker account.

The new [NBER W33795 field-experiment finding](projects/ai-work-control/findings/ai-work-control-075.md)
adds a randomized worker-level time and coordination layer: individual AI
access reduced email and after-hours work patterns in a six-month, 66-firm
experiment, while the paper reports no detectable change in overall task
quantity or composition from individual provision. It strengthens the
time-boundary arrow without closing the workplace-control arrow. The next
test remains a workplace event that observes whether saved time becomes rest,
care, additional work, higher expectations, reallocation, pay, or bargaining
power.

The new [AI-companion farewell finding](projects/us-digital-habits-attention/findings/us-digital-habits-attention-008.md)
adds a product-level exit-boundary mechanism to the culture/attention lane.
The behavioral audit and controlled experiments report farewell tactics and
short-run post-goodbye engagement responses, while preserving the distinction
between an exit signal, continued conversation, perceived manipulation, and
durable user harm. The next test is version-stamped repeated exit behavior with
deletion, switching, billing, human alternatives, and later trust or wellbeing;
the current evidence does not establish universal prevalence, dependence, or
legal violation.

The new [synthetic-contact finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-026.md)
adds a preregistered political-meaning intervention to the culture/attention
and political-action lanes. An outgroup-representing bot changed immediate
warmth and a costly choice of real outgroup contact in online U.S. partisan
experiments, while the one-week persistence result was small. The next test is
repeated, disclosed, version-stamped contact with cooperation, policy
judgment, civic action, and governance outcomes; the preprint does not
establish durable depolarization or electoral effects.

The new [July expense-to-confidence cross-tab](projects/us-cost-trust-politics/findings/us-cost-trust-politics-027.md)
adds a replicate-weighted within-release comparison: respondents reporting any
usual-expense difficulty had lower high confidence in federal statistical
agencies and Congress than respondents reporting no difficulty. The gap is
institution-specific and contemporaneous; the next test remains prior trust,
attribution, a dated material event, action, and recovery in the same unit.

The care-time subpass now has an official published-table baseline in the
[ATUS 2023–2024 care/work layer](projects/us-aging-care-strain/atus-2023-2024-published-care-work-layer-v1.md).
The [ATUS 2024 microdata record](records/us-atus-time-care-microdata-2024.json)
now adds a reproducible weighted population layer for work, care, travel,
household labor, socializing, secondary childcare, and eldercare. It clears
the population-estimate download gate but not the stronger same-respondent
schedule, care, health, and wellbeing comparison.
The [2024–2025 annual comparison](projects/us-household-calendar-integration/atus-time-care-annual-comparison-2024-2025-v1.md)
adds a second annual sample with replicate-weight errors. The next test is
still a same-unit event or panel design, not a stronger claim from annual
aggregate movement.
The new [annual-average versus life-stage distribution finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-035.md)
promotes the interpretation into the reader-facing layer: small year-to-year
movement can coexist with persistent sex, age, and care-network differences.
The next test remains repeated or event-compatible measurement of alternatives,
schedule control, health, work, and recovery.
The [eldercare roster comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-011.md)
now shows that roughly four in five provider respondents list a non-household
recipient in each annual sample, with about 1.3–1.4 listed recipients per
provider. The next test is distance, care intensity, shared support, and work
or health response within a repeated provider or household unit; the roster
does not establish burden or displacement.
The [provider-time comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-012.md)
now adds replicate-weighted same-diary contrasts: providers show more
household work and travel and less paid work and socializing in both samples.
The next test is covariate-adjusted or repeated-unit care timing with health,
schedule control, and recovery; the annual contrast is not causal.
The [standardized provider-time comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-013.md)
now controls the first composition surface—age, sex, and labor-force status—
within supported cells. Household work, travel, and social-time differences
persist, while paid-work differences are imprecise. The next test is richer
health/family/recipient adjustment or a repeated-unit dated-care design.
The [richer standardized comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-014.md)
adds household-child status and broad education. Care, household-work, and
travel differences remain, but social-time ordering varies by year and the
paid-work contrast is not stable enough for a work-loss claim. The next test is
health/family/recipient adjustment or a repeated-unit dated-care design.

The consumer-recourse lane now has a current [2025 CFPB endpoint refresh](projects/us-customer-automation-recourse/findings/us-customer-automation-recourse-015.md).
The response mix shifts toward explanation and away from relief labels, while
narrative visibility falls. The next test is product/firm-denominated exposure
and same-case verified remedy, repeat effort, switching, or trust—not treating
the pooled shift as consumer welfare.
The [product-conditioned route comparison](projects/us-customer-automation-recourse/findings/us-customer-automation-recourse-016.md)
now shows that the pooled shift is heterogeneous: mortgage remains explanation-
dominant, checking/savings and credit-card routes shift toward explanation, and
student-loan untimely labels rise sharply. The next step is a field-definition,
servicing, and case-level audit of that student-loan signal plus firm/account
denominators.
The [student-loan timing-field audit](projects/us-customer-automation-recourse/findings/us-customer-automation-recourse-017.md)
now separates `timely = No` from the narrower company-response untimely
category. The 2025 annual-report context aligns with the broader timely field,
not the narrower response label. The next step is servicing-transfer, notice,
elapsed-days, payment-status, and verified-remedy evidence.

The public-system lane now has a bounded transition-to-hardship estimate in
the [SIPP SNAP outcome layer](projects/us-safety-net-access/sipp-snap-transition-outcome-fay-brr-layer-v1.md).
The next missing public-system stage is the same-episode record of notice,
effort, amount, remedy, interpretation, and action—not another cross-sectional
receipt table.

The route mechanism is now documented in the [SNAP administrative-burden paper
scan](projects/us-safety-net-access/snap-administrative-burden-paper-scan-v1.md).
The next public-system advance should therefore be a same-episode or matched
route design, not another disconnected participation statistic.
The official [USDA FY2025 context layer](projects/us-safety-net-access/usda-snap-fy2025-current-context-layer-v1.md)
now anchors that route evidence in current program scale, state variation,
household composition, benefit distribution, and food-security research. It
does not change the next test: connect a real notice/route episode to amount,
interruption, material security, interpretation, and later action.
The [state participation distribution layer](projects/us-safety-net-access/usda-snap-fy2025-state-participation-layer-v1.md)
now preserves the underlying 51 state/DC rates and makes the next geographic
test explicit: match them to comparable need, eligibility, and administrative
route measures before interpreting the spread.
The first [USDA–ACS state crosswalk](projects/us-safety-net-access/findings/us-safety-net-access-001.md)
shows why the join matters: state participation is non-monotonic across ACS
income quartiles, while zero-vehicle and long-commute measures diverge. The
next [SNAP route-performance layer](projects/us-safety-net-access/findings/us-safety-net-access-002.md)
adds official FY2025 application and recertification timeliness plus the 2023
Program Access Index. It shows that participation and application timeliness
are almost uncorrelated across the 51 state/DC aggregates, preserving the
denominator distinction between receipt and administrative handling. The next
step now uses the [WBNS lived-route layer](projects/us-safety-net-access/findings/us-safety-net-access-003.md),
which reports notice, time, paperwork, interview, and interruption barriers from
the recipient side. The remaining gate is linked or matched same-episode
evidence for exact amount, gap days, correction/appeal, hardship, and action.
The current [route-to-security triangulation](projects/us-safety-net-access/findings/us-safety-net-access-004.md)
is the strongest bounded synthesis so far, but it remains a non-pooled chain;
the next pass now has a concrete [WBNS public-use acquisition gate](projects/us-safety-net-access/wbns-public-use-route-acquisition-audit-v1.md):
download ICPSR 39691, verify its codebook and weights, and test the documented
route variables against food, housing, work, health, and financial-security
fields. That will not replace a linked administrative episode, but it can add
exact respondent denominators and aligned cross-sectional route/outcome cells.
The new [WBNS food-insecurity persistence layer](projects/us-safety-net-access/wbns-food-insecurity-persistence-layer-v1.md)
adds the published material endpoint while that acquisition gate remains open:
working-age household food insecurity was 27.7% in December 2025 after rising
from 19.9% in 2021, with higher published exposure among families with children,
lower-income families, Black and Hispanic adults, and adults with disabilities.
The accompanying [finding](projects/us-safety-net-access/findings/us-safety-net-access-005.md)
keeps the 2025 methodology change, item universe, and non-causal policy boundary
visible. The next test remains a codebook-backed WBNS route/outcome cross-tab,
not a causal attribution from the published trend.
The [charitable-food access layer](projects/us-safety-net-access/wbns-charitable-food-access-layer-v1.md)
now adds the private/mixed-safety-net route: 16.7% of working-age adults
reported charitable-food participation in 2025, while 28.8% of food-insecure
adults reported unmet charitable-food need. Its access barriers—hours,
awareness, comfort, variety, transportation, safety, and perceived treatment—
make the remaining route-to-meaning questions explicit without converting them
into generalized trust or political action.

The new [food-security/safety-net route-buffer bridge](projects/ai-work-control/findings/ai-work-control-056.md)
updates that architecture with the 2025 WBNS food-insecurity trend and
charitable-food endpoints. It keeps formal timeliness, food insecurity,
charitable reach/unmet need, and SIPP following hardship as separate stages;
the next step remains a same-episode notice-to-benefit-to-food/household
outcome ledger with remedy, interpretation, and recovery.

The new [AI utilization/output/mobility bridge](projects/ai-work-control/findings/ai-work-control-057.md)
adds BEA's early industry-account and state-industry utilization estimates to
the NBER task/adoption and executive-expectation layers and BLS JOLTS mobility
context. Its BLS refresh now extends the mobility context through January–July
2026 while preserving July's preliminary status and the incomplete-year bound.
It keeps utilization, modeled association, expectation, and aggregate labor
movement separate; the next step remains a same-workplace implementation event
with exposure, pay, time, discretion, appeal, representation, and later
household or institutional outcome.

The new [place-capacity/growth/belonging bridge](projects/ai-work-control/findings/ai-work-control-058.md)
puts CES county growth and capacity cells beside the Chicago-area immigration
attitude case and ANES national meaning/action cross-tabs. It preserves the
non-monotonic and conditional patterns rather than collapsing them into a
single local trust or pro/anti-immigration score; the next step remains a
same-geography panel linking dated exposure, lived service access, belonging,
action, and institutional response.

The new [household-adaptation/recovery bridge](projects/ai-work-control/findings/ai-work-control-059.md)
puts SHED panel persistence, health/care transitions, food-pressure responses,
and fraud-recovery effort into one buffer architecture. It distinguishes
current stabilization from restored future room and keeps money, time, health,
care, dignity, trust, and verified remedy as separate endpoints; the next step
remains a same-household dated event ledger with protected and sacrificed
outcomes, attribution, recovery, and institutional response.

The new [consumer visibility/attention/remedy bridge](projects/ai-work-control/findings/ai-work-control-060.md)
places CFPB annual and product-conditioned response labels beside SHED fraud
loss/recovery burden, Pew platform and AI concern, and the FTC information-
gathering inquiry. It keeps visibility, remedy, attention, dependence, trust,
and exit separate; the next step remains a same-case or linked account ledger
with verified correction, repeat effort, switching, residual loss, and later
institutional or civic response.

The new [current macro-to-household bridge](projects/ai-work-control/findings/ai-work-control-061.md)
refreshes BEA income/outlays, BLS CPI and PPI, CPS/CES employment, JOLTS
January–July mobility, and SHED household-room measures in one release-aware
comparison. It preserves aggregate, upstream, establishment, household, and
conditional denominators; the next step remains a dated same-household or
same-worker price/payment/employment event with adaptation, attribution, and
recovery.

The new [safety-net transition/work-room bridge](projects/ai-work-control/findings/ai-work-control-062.md)
places SIPP SNAP entry beside following household-resource, earnings, hours,
job-count, rent/mortgage, and utility outcomes. Entry is followed by substantial
resource movement while job counts and hours are often unchanged, which makes
the transition a marker of a changing route through pressure rather than a
clean recovery or work-loss measure. The next step remains the same-episode
notice, amount, gap, remedy, care/work response, and later recovery ledger.

The new [care/time/material/mobility bridge](projects/ai-work-control/findings/ai-work-control-050.md)
keeps the material/time/care lane moving while PSID access remains gated. It
places SIPP child-care work prevention and following hardship beside SHED
caregiver adaptation, ATUS standardized eldercare time, and NHTS mobility
context. The comparison supports a recurring multi-currency pattern, not a
single care-burden index; the next decisive step remains a same-unit dated
episode with alternatives, institutional route, remedy, recovery, and action.

The migration/place lane now has a joint growth × foreign-born capacity screen
in the [joint capacity layer](projects/us-immigration-local-demand/migration-growth-nativity-joint-capacity-layer-v1.md).
The next place step is to add housing supply, travel, wages, provider
adequacy, and direct belonging/action measures to capacity-keeping-pace versus
capacity-lagging comparisons.

The place screen also has a housing/capacity option-stack layer with ACS
vacancy, rent, household income, crowding, language-access, commute mode,
QCEW wage, and Census Building Permits measures. The next step is a larger conditioned place
panel with travel, provider adequacy, and direct local meaning/action measures;
the current permit measure is authorized annual flow, not completed or occupied
housing. The new [immigration belonging,
attitude, and action source pass](projects/us-immigration-local-demand/immigration-belonging-attitude-action-source-pass-v1.md)
separates those respondent-level measures from place context. A first
weighted SDA cross-tab result now exists in the [immigration attitude/action
layer](projects/us-immigration-local-demand/immigration-attitude-action-sda-cross-tabs-v1.md);
the remaining place step is a valid geography/timing join, not more national
attitude tables.

The [Federal Reserve 2025 housing and insurance risk record](records/us-federal-reserve-housing-insurance-risk-2025.json)
adds renter arrears, homeowner insurance gaps, neighborhood/income gradients,
and coverage affordability pressure. The next housing/place step is a matched
place-time panel linking rents, premiums, hazards, claims, repairs, service
access, and move/stay outcomes; the survey layer does not establish those
arrows.
The [Treasury FIO market layer](projects/us-housing-insurance-risk/treasury-fio-homeowners-insurance-market-layer-v1.md)
now supplies 2018–2022 ZIP-code premiums, nonrenewals, claim severity, and
cancellations, but excludes later activity and does not identify households.
The survey and market layers still do not establish the household-level arrows.
The new [Treasury × Census ZCTA context layer](projects/us-housing-insurance-risk/treasury-fio-census-zcta-context-layer-v1.md)
provides a 98.0%-matched 2022 place screen and a counterexample to a simple
income gradient. Next is hazard conditioning and a later market year, followed
by compatible property, mortgage, repair, and move/stay outcomes.
The [Treasury × FEMA NRI hazard layer](projects/us-housing-insurance-risk/treasury-fio-fema-nri-hazard-context-layer-v1.md)
adds a 99.0%-matched county hazard screen and shows that premium and nonrenewal
do not move monotonically across modeled-risk ratings. Next is a later market
year or state filing panel, with the FEMA assignment and temporal mismatch
kept as explicit limits.
The [housing-payment/coverage synthesis](projects/us-housing-insurance-risk/findings/us-housing-insurance-risk-001.md)
now states the combined interpretation: housing security has a payment side
and a coverage side. The next test is a compatible state/property-year panel
linking premiums, nonrenewal, hazards, claims, repairs, assistance, and
move/stay; another aggregate arrears or insurance screen will not close the
arrow.
The new [housing-payment/coverage/hazard/backstop bridge](projects/ai-work-control/findings/ai-work-control-055.md)
places Federal Reserve household reports beside Treasury/FIO market rows,
FEMA modeled hazard context, and California FAIR Plan stocks. It preserves the
distinction between arrears, premiums, nonrenewal, uninsured status, hazard,
and public-backstop scale; the next test remains a compatible property or
household-year panel with claims, repairs, assistance, and move/stay outcomes.
The [GAO 2019–2024 layer](projects/us-housing-insurance-risk/gao-homeowners-insurance-2019-2024-layer-v1.md)
now supplies a later market window and state-regulatory process evidence. The
next test is to align approved rates, residual-plan or nonrenewal exposure,
household costs, and post-loss outcomes for a compatible state/year panel.
The GAO layer also identifies 35 state FAIR/beach plans as of August 2025,
which supplies a public-backstop stage. Next is plan enrollment, premium,
coverage, assessment, and claim-outcome data by state, linked to household and
property outcomes without treating plan presence as availability success.
The California FAIR Plan layer now supplies a concrete 2021–2026 residual-market
time series for policies and insured exposure. Next is a state-level comparison
of voluntary-market coverage, FAIR enrollment, premiums, assessments, claims,
repairs, and household/property outcomes.
The FAIR/private-market crosswalk now supplies a 2022 ZIP-level comparison of
residual-market share and voluntary nonrenewal decisions. The new [CDI wildfire
county context layer](projects/us-housing-insurance-risk/california-doi-wildfire-county-context-layer-v1.md)
conditions a county-aggregated screen on modeled high/very-high exposure and
finds a modest descriptive gradient, while preserving the 2015-versus-2022
temporal mismatch. Next is conditioning the ZIP comparison on income and
property type. The new [ACS context layer](projects/us-housing-insurance-risk/california-fair-market-acs-context-layer-v1.md)
finds materially higher voluntary nonrenewal in the lowest-income ZIP
quartile, while preserving ZCTA approximation and denominator limits. Next is
a transparent joint screen across income, structure, county risk, and FAIR
share, then extending premiums, claims, and market transitions through later
years. The [joint context screen](projects/us-housing-insurance-risk/california-fair-joint-context-screen-v1.md)
now supplies that first stratified test: low-income/high-risk ZIPs have the
highest observed nonrenewal rate under one pre-specified split. The new
sensitivity layer shows the ordering changes under other cut points, so the
result remains unweighted, descriptive, and cut-point-sensitive.
The [California sensitivity finding](projects/us-housing-insurance-risk/findings/us-housing-insurance-risk-002.md)
promotes that counterexample into the published atlas and keeps the next test
on pre-specified multi-cut-point and property-year validation.

The [CES local trust/action context layer](projects/us-immigration-local-demand/migration-place-local-trust-action-context-v1.md)
now supplies a county-keyed political-context screen from public survey data;
it remains separate from the ANES immigration battery because the CES common
file does not contain the same immigration-specific questions.

The follow-up [joint growth × nativity CES screen](projects/us-immigration-local-demand/migration-place-local-trust-action-joint-axes-v1.md)
shows that federal trust is non-monotonic across the two axes and civic action
is comparatively stable; this supplies a counterexample screen, not a local
immigration-opinion estimate.

The [Chicagoland local immigration-attitude case](projects/us-immigration-local-demand/chicagoland-local-immigration-attitude-case-v1.md)
now supplies one direct local meaning source with documented geography and
sampling, paired with an ACS 2024 five-year material-context refresh. This
improves timing but does not create a same-period causal join; the next step
is direct same-geography evidence on provider capacity, travel, wages, and
political action, not national generalization.
The new [local capacity and immigration meaning finding](projects/us-immigration-local-demand/findings/us-immigration-local-demand-001.md)
publishes the joint boundary: county capacity patterns are non-monotonic while
local policy meaning differs across Chicago-area places. The next test is a
matched place/respondent panel with service exposure, alternatives, and action.

The [growth × HPSA capacity layer](projects/us-immigration-local-demand/migration-growth-hpsa-capacity-layer-v1.md)
conditions the 620-county growth screen on provider-shortage context. Among
HPSA counties, health employment per resident falls across growth quartiles,
but HPSA and CBP stocks are not lived access. The next place step remains
travel, wages, provider adequacy, service use, and direct local meaning/action.

The immediate PSID gate was rechecked on 2026-09-14 and remains concrete: the
official package routes are listed but require an authenticated account and no
target PSID data files are present in the workspace. Obtain the 2019, 2021,
and 2023 main files, run the [wave-file audit protocol](projects/us-household-calendar-integration/psid-wave-file-audit-protocol-v1.md),
verify the mapped fields and their universes across waves, measure
person/family retention and missingness, preserve weights, and then publish
the first many-family comparison. No result should be promoted before that
gate is passed.
The [SIPP material/time/care population record](records/us-sipp-material-time-care-population-2024.json)
now supplies a reproducible person-weighted monthly diagnostic while the PSID
gate remains open. It shows why utility, food, savings, debt, child-care, and
job fields cannot be collapsed into one stress score. The next SIPP pass is
field-specific replicate-weight variance and explicitly defined household
selection for joint outcomes. The [official-universe variance finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-002.md)
now completes the first five-field Fay-BRR check; the remaining care, work,
and household-selection cells are still queued. The [care/work variance finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-003.md)
now applies the same gate to four child-care measures, with the small
conditional time-lost universe retained as a precision warning.
The follow-up [income-band comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-004.md)
shows paid care, assistance, and work prevention diverge across poverty-ratio
bands; further stratification remains contingent on cell precision.
The [tenure comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-005.md)
now adds owner/buyer, renter, and sparse no-rent cells; renter work
prevention is higher while paid-care use is lower, with housing causation left
open.
The [regional comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-008.md)
now adds place context: paid-care use is similar across regions while work
prevention varies more; local supply and employer mechanisms remain open.
The [child-presence comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-009.md)
now identifies a universe boundary: household members under 18 and
reference-parent child-care fields are not interchangeable. The next step is
field-level parent/child-age auditing before further intersections.
The [reference-parent universe audit](projects/us-household-calendar-integration/findings/us-household-calendar-integration-010.md)
now confirms the timing mismatch: `RHNUMU18` is monthly while `ERP` and care
questions use reference-year/fall/December universes. Rebuild parent-status
estimates only after aligning those fields.
The [race-group comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-006.md)
now adds the released race recode with uneven precision; it is a distributional
screen, not a cultural-meaning or discrimination measure.
The [disability-status comparison](projects/us-household-calendar-integration/findings/us-household-calendar-integration-007.md)
now adds the health/work-limitation moderator; its time-lost condition cell is
too sparse for a stable ranking, so direct accommodation and follow-up remain
open.
The new [work-limitation × children × resources finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-015.md)
promotes the completed three-way Fay-BRR layer into the canonical registry.
It shows that utility, food, and job outcomes occupy different joint cells,
including a sparse high-resource counter-pattern. The next test is a valid
care-time, schedule, benefit-route, or health endpoint—not a universal
intersectional hardship score.
The follow-up [household-selection diagnostic](projects/us-household-calendar-integration/findings/us-household-calendar-integration-016.md)
now makes the unit problem executable: one ERP-preferred record per
household-month changes the utility-payment, rent/mortgage, and food-security
diagnostics relative to all person records. The selected view still reuses a
person weight, so it is a sensitivity check rather than an official household
estimate. The next gate is an official household-weight route or a documented
household estimator before joint household claims are promoted.

The consumer-power lane now has a bounded institutional-response layer in the
[CFPB response route comparison](projects/us-consumer-fraud-trust/cfpb-response-route-layer-v1.md).
It adds product-conditioned response, relief, explanation, and timeliness
patterns. The next missing step is linked consumer follow-up—verified remedy,
repeat effort, switching, dependence, and later trust—not another complaint
count.

The [CFPB product × state rate layer](projects/us-customer-automation-recourse/cfpb-product-state-rate-layer-v1.md)
now conditions the visible complaint geography on six financial products. It
shows that place patterns differ by product, while preserving the distinction
between published visibility and harm or remedy. The next consumer-power step
is a product/state case sequence with account denominators and follow-up, not a
larger unnormalized complaint table.

The [CFPB × CBP finance-state context layer](projects/us-customer-automation-recourse/cfpb-cbp-finance-state-context-layer-v1.md)
places product complaint visibility beside 2023 finance-sector establishment
and employment stocks. Its non-monotonic quartile screen is a counterexample
to treating local firm presence as consumer protection or harm. The next step
is account exposure, branch/digital access, and case-level follow-up.

The [CFPB product response-route layer](projects/us-customer-automation-recourse/cfpb-product-response-route-layer-v1.md)
now extracts product-conditioned monetary relief, non-monetary relief,
explanation, and untimely-response shares from the same complaint slices. It
shows that institutional endpoints are product-shaped; it still does not
observe remedy adequacy, repeat effort, switching, dependence, or trust.

The [CFPB product visibility-route layer](projects/us-customer-automation-recourse/cfpb-product-visibility-route-layer-v1.md)
now adds narrative presence and submission channel to that product comparison.
Web submission dominates all six slices, but phone/referral use and narrative
presence vary materially by product. This deepens the cultural/institutional
question of whose account becomes visible without treating missing narratives
or channel choice as direct measures of access, harm, or consumer ability.
The next step remains a case-level or panel follow-up with failed attempts,
repeat effort, verified remedy, switching, and trust.

The [2026-09-13 CFPB aggregation refresh](projects/us-customer-automation-recourse/cfpb-2024-aggregation-refresh-2026-09-13.md)
rechecked the live official API, preserved current index metadata and a
retrieval hash, and added an aggregate-only fetcher. The consumer-power lane
is therefore current through institutional response; its next step remains a
same-case or linked follow-up with verified remedy, repeat effort, switching,
dependence, and later trust.

The [2020–2025 annual CFPB response trend](projects/us-customer-automation-recourse/cfpb-annual-response-trend-2020-2025-v1.md)
adds a time comparison to the institutional-response arrow. It is explicitly
a trend in published complaint records, not a trend in consumer harm,
verified remedy, or trust; the next step remains case-level follow-up.

The [2024 CFPB case-route sample](projects/us-customer-automation-recourse/cfpb-case-route-sample-2024-v1.md)
adds a bounded first-handoff diagnostic: receipt-to-company routing time,
channel, narrative/public-response visibility, and product-conditioned response
labels. It is not a random sample and does not measure remedy. The unresolved
consumer-power task is still a same-case or valid panel ledger from contact
through effort, decision, verified remedy, repeat effort, switching, trust, and
exit.
The new [consumer loss and complaint visibility finding](projects/us-customer-automation-recourse/findings/us-customer-automation-recourse-018.md)
places that administrative visibility beside the Federal Reserve/SHED household
loss and recovery burden. It confirms the denominator gap and keeps the next
test on linked case follow-up rather than complaint-volume interpretation.

The [CFPB public event-ledger acquisition audit](projects/us-customer-automation-recourse/cfpb-public-event-ledger-acquisition-audit-2026-09-14.md)
now proves that a small public administrative episode ledger can be built and
validated from receipt, routing, channel, narrative visibility, timeliness,
and response labels. It does not create remedy, trust, switching, or exit
outcomes; the next consumer-power test remains a lawful same-case or linked
follow-up design.

The [Federal Reserve household fraud and recovery layer](projects/us-consumer-fraud-trust/federal-reserve-household-fraud-recovery-layer-v1.md)
now supplies the household side of that consumer-power chain: exposure,
conditional direct loss, unrecovered money, and recovery time. It is a survey
denominator distinct from FTC reports and CFPB complaints. The next pass should
condition this path on payment rail, age, income, disability, language, and
digital access, then seek same-person evidence of firm response, verified
recovery, later financial use, trust, or exit.
The new [SHED fraud subgroup layer](projects/us-consumer-fraud-trust/shed-fraud-subgroup-layer-v1.md)
adds codebook-backed age, income, and account-route conditioning. It shows a
nonmonotonic income pattern and higher descriptive recovery/time burden in P2P
account cases, while confirming that general digital-access and disability
measures are not available for this path in the public file. The next step is
still a linked payment/account case with verified firm response and later trust
or exit.

The new [consumer-loss/recourse/recovery bridge](projects/ai-work-control/findings/ai-work-control-054.md)
places Federal Reserve household burden beside FTC administrative loss and CFPB
response/timing fields. It clarifies that reporting, routing, explanation,
relief labels, recovery, and trust are different endpoints; the next test is a
lawful same-case or linked account ledger with verified remedy, repeat effort,
switching, and later institutional response.

The [SHED annual fraud comparison](projects/us-consumer-fraud-trust/shed-fraud-annual-comparison-layer-v1.md)
repeats the age/income definitions in the 2025 file. The income pattern
persists descriptively, but the age ordering changes across annual samples;
this is a time-based weakening test, not a panel trend. The 2025 file lacks the
account-route fields, so P2P burden remains a 2024-only screen. The [fraud
recovery burden finding](projects/us-consumer-fraud-trust/findings/us-consumer-fraud-trust-001.md)
now publishes that subgroup result with its conditional denominators and
counterinterpretations; it adds a detailed memo without creating a new trend
record.

The [FTC 2025 extension](records/us-ftc-consumer-sentinel-2025-extension.json)
adds the next administrative time point and separates imposter and investment
loss categories. The remaining consumer-power test is not more aggregate
reports: it is a linked payment/account case from reported scam through loss,
recovery, time cost, institutional response, and later trust or exit.
The accompanying [fraud reporting-to-recovery finding](projects/us-consumer-fraud-trust/findings/us-consumer-fraud-trust-002.md)
now writes this boundary in detail, keeping FTC scale, SHED household burden,
and CFPB response routes as complementary rather than same-case evidence.

The [SHED financial-path health/care trend record](records/us-shed-financial-path-health-care-2024-2025.json)
now adds six conditional same-respondent observations: health direction by
financial path and unpaid adult-care entry by financial path. It strengthens
the material-to-wellbeing bridge while preserving the counterexample that
financial improvement does not guarantee health improvement. The next step is
care intensity, schedule control, dated trigger, and later meaning/action—not
another pooled stress index.

The [SHED adaptation-by-health-direction layer](projects/us-household-financial-pressure/shed-panel-adaptation-health-path-layer-v1.md)
now conditions adaptation persistence and entry on 2024→2025 self-rated-health
direction. Improved health does not automatically unwind borrowing or delayed
purchases, while reduced-savings persistence is lower in the improved-health
path. This advances the recovery arrow but remains descriptive: annual health
categories do not identify a dated bill, treatment decision, or causal ordering.

The [ATUS care/work trend record](records/us-atus-eldercare-work-time-2023-2024.json)
adds a population-scale time/care source to the registry: 38.192 million
reported eldercare providers, a high provider rate among ages 55–64, and
conditional care-day intensity for employed and full-time workers. It remains
a published-table layer; the next step is respondent-level work, household,
health, and later-wellbeing linkage.

The [ATUS eldercare roster record](records/us-atus-eldercare-roster-2024-2025.json)
adds a relational comparison: provider respondents commonly list recipients
outside their household, and some list multiple recipients. This strengthens
the cross-household coordination hypothesis but does not measure distance,
hours, costs, shared-care substitution, or outcomes; those remain the next
acquisition gap.

The [ATUS provider-time record](records/us-atus-eldercare-provider-time-2024-2025.json)
adds four replicate-weighted provider/nonprovider cells for household work,
care, paid work, travel, socializing, secondary childcare, and eldercare
minutes. It deepens the time profile while preserving the central selection
problem: provider status is not a dated or exogenous care shock.

The [ATUS standardized provider-time record](records/us-atus-eldercare-provider-standardized-2024-2025.json)
adds two age/sex/labor-force-standardized contrasts with replicate uncertainty.
It is a stronger descriptive test of composition, not a causal care estimate;
health, family, recipient, occupation, schedule, and timing controls remain
the next acquisition gap.

The [ATUS richer standardized provider-time record](records/us-atus-eldercare-provider-richer-standardized-2024-2025.json)
adds household-child status and broad education to the supported-cell target.
It strengthens the robustness check while preserving annual variation and the
open health, recipient, schedule, and dated-care arrows.

The [CFPB annual response record](records/us-cfpb-annual-response-trend-2020-2025.json)
now extends through calendar 2025 using a fresh official API hash. The next
recourse pass is a denominator-aware product/firm comparison or linked case
follow-up that can observe verified correction, repeat effort, exit, or trust.

The [CFPB product-year route record](records/us-cfpb-product-response-routes-2024-2025.json)
adds twelve matched product-year observations and preserves product-specific
denominators, response categories, timeliness, narrative visibility, and the
2025 in-progress category. The student-loan timing spike is held as an audit
target rather than promoted into a welfare claim.

The [CFPB student-loan timing audit record](records/us-cfpb-student-loan-timing-field-audit-2024-2025.json)
adds the two distinct timing fields and the annual-report context. It prevents
the broader no-timely field from being misreported as the narrower company
response category and keeps the borrower-outcome arrow open.

The [BLS representation trend record](records/us-bls-union-representation-2024-2025.json)
adds a worker/institution source to the registry: national membership and
contract-representation rates for 2024 and 2025, with age/occupation/state
heterogeneity retained in the source memo. The next step is a worker-event
comparison linking representation to a defined tool, schedule, safety,
appeal, household-time, or collective-action outcome.

The [CPS participation-friction trend record](records/us-cps-voting-participation-friction-2024.json)
adds a political-voice source to the registry: turnout and registration beside
separate schedule, health, administrative, transport, interest, and candidate
barriers among nonvoters. The next step is a repeated-election or event-based
design with exposure, attribution, participation, and vote measured in time.

The [SIPP SNAP transition/hardship trend record](records/us-sipp-snap-transition-following-hardship-2024.json)
adds a public-system source with four adjacent-month transition states,
transition-specific denominators, and Fay-BRR uncertainty. It preserves the
counterexample that exit does not imply restored security and continued receipt
does not guarantee housing or utility security. The next step is same-episode
notice, effort, amount, remedy, interpretation, action, and recovery.

The [SIPP stable-state child-care bridge](records/us-sipp-snap-stable-state-childcare-2024.json)
adds the same-person care/work boundary: continued SNAP receipt coexists with
higher child-care assistance and reported work prevention, while paid care is
lower than in stable nonreceipt. Sparse entry/exit cells remain open. The next
step is still the same-episode route ledger for notice, effort, amount, remedy,
and interpretation.

The [SIPP child-care time-loss layer](projects/us-household-calendar-integration/sipp-snap-childcare-time-loss-layer-v1.md)
and its [published finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-018.md)
now add `ETIMELOST`/`ETIMELOST_TP` to that same-person bridge. Stable SNAP
respondents show a higher descriptive work-prevention share (7.43% versus
3.42%), with wide uncertainty and only 23 valid time-loss cases. A current
full-slice rerun reads 379,215 rows, matches 31,335 replicate pairs, and
reproduces all committed estimates and standard errors. The next substantive
gate remains a dated care episode with alternatives, schedule control, and
outcome follow-up.

The [child-care work/hardship bridge](projects/us-household-calendar-integration/sipp-childcare-work-hardship-bridge-v1.md)
and its [published finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-019.md)
now condition following rent/mortgage and utility hardship on that same
work-prevention measure. Stable SNAP respondents reporting work prevention have
43.65% rent/mortgage hardship and 32.39% utility hardship, versus 12.01% and
19.43% without it; the work-prevention cell has only 23 records and wide
intervals. The next step remains adjustment or a dated episode, not causal
interpretation.

The [CCES joint trust/action layer](projects/us-cost-trust-politics/cces-trust-action-joint-layer-v1.md)
now separates trust from civic action inside four gig-work/student-debt proxy
cells. The smallest joint proxy cell has the highest high-trust/action share,
while low federal trust with action is not highest there—a counterexample to
equating distrust with withdrawal. The result is cross-sectional and has no
complex-design variance; the next political test remains a timed respondent or
event design with attribution and prior identity.

The [LBNL data-center energy trend record](records/us-lbnl-data-center-electricity-load-2023-2030.json)
adds an infrastructure/state-power source with historical 2023 load, a 2030
reference case, and explicit scenario bounds. The next step is a place-utility
comparison that observes approved versus actual load, rate recovery, local
benefits and costs, ownership, replaceability, and any changed state or
external behavior.

The [Romania–Malaysia infrastructure case record](records/us-geopolitical-ai-infrastructure-case-comparison-2023-2026.json)
adds the first case-level geopolitical/state-capacity object to the trend
registry. It preserves a Romanian public-cloud target and a Malaysia financing/
ownership sequence without calling either sovereignty or leverage. ADR's
September 2026 announcement now closes the separate Romanian infrastructure
implementation stage; it does not close application migration, service quality,
control rights, local incidence, portability, replaceability, or an observed
state or external response. The [infrastructure realization and control
finding](projects/ai-work-control/findings/ai-work-control-036.md) now
publishes the Romania–Malaysia milestone comparison. It adds a detailed
operational/ownership boundary without promoting infrastructure completion to
sovereignty or geopolitical leverage.

The [SIPRI military-expenditure record](records/us-sipri-military-expenditure-state-capacity-2015-2024.json)
adds aggregate state-capacity context: global and US spending growth, US/China
scale, NATO concentration, and military burden. It is not a leverage finding.
The next geopolitical pass must connect resources to procurement realization,
industrial inputs, domestic incidence, alliance decisions, and an observed
external response.

The [USAspending defense-award acquisition layer](projects/ai-work-control/usaspending-defense-award-acquisition-layer-v1.md)
now provides the executable procurement bridge: a bounded FY2024 DoD award
retrieval with request and raw-response hash. The next pass must add
transaction-level obligations, recipient/place/product fields, supplier and
ownership exposure, delivery/performance, and a realized capability or
external-response event.
The [transaction profile](projects/ai-work-control/usaspending-defense-transaction-profile-v1.md)
now selects candidate firms, places, and industrial codes from 100 transactions
without treating page concentration as supplier market share. The next case
pass should audit one weapons-system transaction and one service transaction
through ownership, modifications, performance, workforce, inputs, and delivery.
The [JASSM/LRASM award-detail case](projects/ai-work-control/usaspending-jassm-lrasm-award-detail-v1.md)
now completes the first weapons-system selection through award obligation,
subawards, program, competition, duration, ownership, and place. The remaining
case work is delivery/modification history, subcontractor and input exposure,
workforce/production evidence, and any realized strategic or external response.
Its persisted 19-action history now supplies the modification sequence through
April 2026, including zero-dollar and later positive actions. The next step is
to link those actions to delivery/acceptance, supplier inputs, workforce, and
operational or alliance outcomes.
The new 74-record subaward extract supplies 51 reported subordinate recipients
and $1.143B in associated amounts. The next supplier pass should reconcile
those records to component/input descriptions, ownership, geography, workforce,
and delivery evidence; do not treat the extract as a complete tier map.
The first ownership pass now shows why prime-level “US-owned” metadata cannot
be copied onto every subordinate entity: the largest reported recipient is
listed in BAE Systems plc's group subsidiary materials, alongside a US
security-control arrangement. The next pass should resolve legal-entity
registration, UEI/DUNS, plant geography, and workforce for the top recipients.
The SAM.gov entity route is now documented as an acquisition dependency because
GSA requires a public API key for entity queries; the absence of a key is not a
negative registration finding.
An official DLA CAGE lookup now resolves the largest recipient by exact legal
name to CAGE 81J97, UEI SL2KEMFACM69, an active Merrimack, NH address, and
linked parent CAGE 1BNT5. The remaining join is to obtain the same identifier
in the USAspending subaward record and test facility-level production,
workforce, and delivery evidence.
The parent CAGE now resolves to BAE Systems, Inc. in Falls Church, VA, with
BAE Systems plc above it. The case therefore has a three-level entity/facility
hierarchy, while revenue, workers, component flow, and output remain open.
The comparison supplier pass adds General Dynamics-OTS, whose reported
$80.55M case-assembly subaward name maps to three active DLA facilities under
General Dynamics Corp. The next step is an identifier-bearing procurement or
performance record that can assign work to a facility, followed by workforce
and delivery evidence.
The General Dynamics parent record is now resolved as CAGE 95403 in Reston,
VA, confirming the parallel group/parent/facility hierarchy seen in the BAE
case. The unresolved issue is facility-level assignment of the subaward.
The BAE parent CAGE now resolves to an active London, UK BAE Systems plc
record, completing that public entity chain. The next evidence must move from
identity and jurisdiction to plant-level work, workforce, delivery, and
operational outcomes.
An initial realization pass now adds dated production-capacity and LRASM/F-35B
flight-test milestones, plus a DoD Lot 22/FMS production notice. The next step
is to connect those milestones to accepted quantities, delivery/fielding,
facility workforce, and an observed operational or external response.
The first external-response record now captures Poland's signed JASSM-ER
agreement and planned delivery window, plus a separate historical comparator:
the Polish Ministry's January 2017 announcement of first guided JASSM delivery
to the Poznań-Krzesiny F-16 base. The comparator confirms that an earlier
procurement reached a reported delivery stage, but it does not establish
delivery of the 2024 JASSM-ER order. The next step is to observe the 2024–2030
order's delivery, acceptance, integration, inventory/availability, training,
or a dated Polish/allied action that follows the capability—not infer it from
the purchase decision or from the earlier JASSM stock.
The [2026 delivery watchpoint](projects/ai-work-control/jassm-er-delivery-watchpoint-2026-09-13.md)
was rechecked on 2026-09-14 against current Polish and US official-source
releases and still finds a planned 2026–2030 window, not a separately reported
delivery or acceptance event. A second December 2024
Polish MOD briefing states 2028–2030 in its JASSM discussion, creating a
schedule-vintage conflict without identifying a contract amendment. The
realized-capability arrow therefore remains open.

The new [Poland reciprocity and co-production finding](projects/ai-work-control/findings/ai-work-control-042.md)
adds two official 2026 response-stage observations: a Polish-US UAS/C-UAS
cooperation arrangement that describes potential buyer/seller roles and shared
procurement/interoperability infrastructure, and a Poland-US-Estonia-Latvia
agreement describing planned regional Barracuda B500M production with Poland as
the intended European center. These move the case beyond a buyer-only
procurement signal, but remain agreement-stage evidence. The next pass must
retrieve a named transaction, plant commissioning, output, delivery, component
control, workforce, or a dated negotiation/switching event before claiming
industrial autonomy or leverage.
The July 6 Bydgoszcz account sharpens that gate: it reports a PGZ/WZL-2/Anduril
agreement for Polish assembly followed by production, PGZ exclusivity for a
Polish version, and technology/know-how/competence transfer language. These
are implementation terms, not proof that the plant is commissioned or that
control rights, output, or replacement capacity have materialized.
An August 19 BBN follow-up with Anduril keeps the program at the institutional
competence-building stage: it records senior-level discussion of Barracuda-500M
and Polish implementation competencies, not production, delivery, or an
amended contract.
The Ministry of State Assets' detailed July production page adds reported
targets of thousands of systems and staged growth in Polish and European
supplier participation. These sharpen the scale/local-content tests but remain
plans until completed units, supplier contracts, and actual shares are observed.
The September 9 Poland-US Foreign Military Financing agreement adds a broader
resource checkpoint: Poland reports $4 billion in FMF and acceleration of
existing contracts, including Apache helicopters. It is not Barracuda-specific,
so it belongs to the financing/implementation stage and cannot substitute for
plant, output, delivery, or local-content evidence.
The [September realization watchpoint](projects/ai-work-control/findings/ai-work-control-043.md)
records the current public-source non-observation and prevents the same
agreement-stage evidence from being counted as a new production result.

The work/control lane now has a population bargaining-context baseline in the
[BLS union and bargaining-room layer](projects/ai-work-control/bls-union-bargaining-room-layer-v1.md).
It adds representation, coverage, earnings association, and distribution by
worker group, occupation, industry, and state. The next missing step is a
worker-event comparison linking a tool, schedule, benefit, or safety change to
control, voice, household security, and exit.
The [OECD algorithmic-management record](records/us-oecd-algorithmic-management-2024.json)
now adds a cross-country employer measure with US-specific adoption,
monitoring, evaluation, worker-concern, and governance rates. It strengthens
the exposure and institutional-governance stages while preserving the central
gap: worker-level exposure, discretion, appeal, health, bargaining, and
household outcomes remain unmeasured.

The new [AI/work-power bridge](projects/ai-work-control/findings/ai-work-control-052.md)
places the NBER assistance and task experiments, OECD employer-reported
algorithmic management, NBER executive expectations, and BLS representation
context in one non-pooled architecture. It clarifies that productivity,
provision, expectations, and formal coverage are possible stages—not proof of
worker control or bargaining. The next test is a same-workplace technology
event with exposure, monitoring, discretion, appeal, representation, and later
household or collective outcomes.

The NBER W35677 pass now includes the acquired public Detailed, Intermediate,
and Broad Work Activity indexes in the shared registry, with retrieval hashes
and the 20-observation suppression rule preserved. An official O*NET 31.0
release audit now shows normalized labels uniquely match 1,653 of 1,655 DWA
rows and all 322 IWA rows, while the identifier hierarchy does not match
exactly. All nine BWA IDs now have transparent O*NET GWA prefix members, but
semantic aggregation remains open. The next work/control step is to
version the O*NET/crosswalk metadata and obtain compatible worker-level
subgroup data, then connect adoption to training, monitoring, discretion, pay,
and voice; the public indexes alone cannot establish those outcomes.
The first BWA/DWA consistency diagnostic finds that eight of nine broad rates
exceed the displayed DWA weighted means, while physical/manual work is slightly
lower; this is retained as a measurement-layer result, not a data-error or
workplace-control claim.
The published Management Science article now supplies a separate late-2024
anchor—27% of employed respondents used genAI for work in the prior week, with
reported assisted-hour and time-saving measures. Its replication files remain
access-limited, and the estimate is not merged into the later W35677 trend
record until question, wave, weight, and denominator harmonization is complete.

The [IMF April 2026 WEO geopolitical/fiscal shock layer](projects/ai-work-control/imf-weo-geopolitical-fiscal-shock-2026-layer-v1.md)
now adds the macro middle of the geopolitical-to-household bridge: conditional
growth/inflation projections, defense-boom debt and social-spending trade-offs,
conflict recovery scarring, and a vintage-specific US projection series. The
next test is to align those aggregates with defense procurement, energy/trade
exposure, budget composition, household adaptation, trust, and political
action; none of those downstream arrows is promoted yet.

The [World Bank Poverty, Prosperity, and Planet layer](projects/ai-work-control/world-bank-poverty-prosperity-planet-2024-layer-v1.md)
adds the distributional counterweight to that macro frame: global poverty
thresholds, regional and fragility concentration, shared-prosperity stagnation,
climate exposure, and poverty-data coverage. It is comparative context, not a
US outcome; the next test is a country/place panel joining macro shocks to
social protection, climate exposure, migration, and political response.

The new [AI capability/dependence/state-control bridge](projects/ai-work-control/findings/ai-work-control-053.md)
places the World Bank adopt/adapt/advance framework beside Romania and Malaysia
infrastructure milestones, OFR public data capacity, and US data-center load,
fiscal, and utility-governance evidence. It sharpens the distinction between
capability, ownership, public visibility, replaceability, and leverage; the
next test is a critical-system contract/continuity/switching event with public
incidence and observed external response.

The cross-source [macro-to-legitimacy synthesis](projects/ai-work-control/findings/ai-work-control-026.md)
now lays out the full testable route across IMF, World Bank, SIPRI, Federal
Reserve, and ANES. It explicitly separates macro, distributional, household,
and political units and records counterexamples where the predicted trade-off
may not occur. The same-unit exposure-to-action link remains the priority gap.
The follow-up [AI capability/shared-control synthesis](projects/ai-work-control/findings/ai-work-control-031.md)
now consolidates the NBER, BIS, BEA, IMF, OFR, and World Bank evidence. It
sharpens the next test from “does AI raise productivity?” to whether gains,
review, ownership, exit, and bargaining are distributed across firms, workers,
households, public institutions, and countries. The required next pass is
compatible firm/workplace, household-price, public-service, and
country-replaceability panels—not another headline adoption aggregate.
The [World Bank Enterprise Surveys AI follow-up access recheck](projects/ai-work-control/world-bank-wbes-ai-access-recheck-2026-09-14.md)
confirms that the US firm microdata and documentation remain behind the
authenticated portal. The next firm-level gate is therefore file retrieval and
survey-design auditing, not an estimate inferred from the WDR narrative.
The new [public US firm-capacity baseline](projects/ai-work-control/findings/ai-work-control-063.md)
uses the official 2024 country profile to add size-conditioned training,
employment growth, outage exposure, finance, and obstacle context. It is a
descriptive non-AI layer; the next pass must join the AI follow-up to these
size/sector strata and retain firm-level uncertainty rather than treating the
baseline as an adoption score.
The follow-up [firm-to-worker comparison](projects/ai-work-control/findings/ai-work-control-064.md)
now puts the baseline beside NBER task adoption, BLS representation, and JOLTS
mobility. The next decisive test is a dated workplace implementation event with
permission, monitoring, discretion, appeal, household response, and exit; no
one of the four context layers can substitute for that key.

The [BFS–BDS sector divergence layer](projects/us-local-business-place/bfs-bds-sector-divergence-layer-v1.md)
adds a full 19-sector comparison of application volume, realized openings and
closings, and net-job intensity. It makes the counterexample explicit: retail
has the largest application count but modest net-job intensity, while health
care/social assistance and accommodation/food have much larger net-job
intensity; administrative/support has positive entry minus exit but negative
net job creation. The next step is firm-level and place-level matching with
ownership, service access, wages, quality, and worker control.

The [BFS–BDS state archetype layer](projects/us-local-business-place/bfs-bds-state-archetype-layer-v1.md)
now groups all 51 matched states/DC records by application intensity. Higher
application quartiles have higher median entry, exit, and net-job rates, but
the top group contains both high-churn states and contrasting job outcomes;
Alaska and Nebraska supply low-application/high-net-job counterexamples. The
next place step is to attach county service access, ownership, worker quality,
and local political response without turning the state comparison into a
causal story.

The [BFS–BDS sector-dynamics trend record](records/us-bfs-bds-sector-dynamics-2023.json)
adds a firm/place source with eight sector observations and explicit
application denominators. It keeps retail’s high application volume separate
from realized job intensity and retains administrative/support’s entry-with-
net-job-loss counterexample. The next step is firm/place matching for survival,
ownership, wages, service access, worker control, and local political response.

The [local capacity and reachability finding](projects/us-local-business-place/findings/us-local-business-place-003.md)
now completes the first common-geography screen: 3,128 counties are split by
2023 health-sector establishment density and 2023 ACS zero-vehicle-household
context, with HPSA representation, RUCC, and commute measures retained. The
high-capacity/high-zero-vehicle cell is a concrete counterexample to equating
visible capacity with usable access. The next empirical pass must add prices,
hours, staffing, neighboring supply, service use, unmet need, work/care
displacement, and local meaning/action rather than another capacity split.

The [ANES panel worry/trust/vote record](records/us-anes-panel-worry-trust-vote-2024.json)
adds a same-respondent political-judgment source with pre-election worry and
post-election reported vote, alongside a separate trust cross-tab. It remains
descriptive and identity-confounded; the next step is a repeated exposure and
attribution design with source environment, trust, action, turnout, and vote.
The follow-up [political-meaning synthesis](projects/us-cost-trust-politics/findings/us-cost-trust-politics-013.md)
now keeps personal/national judgment, trust/fairness, vote preference, and civic
action as separate political outputs. SHED, GSS, ANES, and CCES together show
why material pressure is not automatically withdrawal or a vote mechanism;
the next test is a dated exposure design with baseline identity/trust,
attribution, action, institutional response, and recovery.
The [party-conditioned ANES finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-014.md)
now publishes the identity-conditioned counterexample as a detailed memo; it
does not add a causal vote estimate or a new material-exposure record.

The [material-to-trust/action bridge record](records/us-material-to-trust-action-bridge-2022-2025.json)
and [detailed bridge finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-015.md)
now place the SIPP work/resource, ATUS care/time, MEPS health/cost, ANES
worry/trust/vote, and CCES trust/action surfaces in one explicitly non-pooled
architecture. This closes a documentation and machine-record gap, not the
substantive causal gap: a same-person dated exposure-to-attribution-to-action
link remains the next priority.

The new [material/care/time/political-friction bridge](projects/ai-work-control/findings/ai-work-control-051.md)
adds the CPS voting-supplement route to that architecture. It separates
schedule, illness/access, transport, registration, and candidate/issue reasons
among nonvoters, then places them beside SIPP hardship, ATUS care-time, ANES
trust/vote, and CCES trust/action surfaces. It strengthens the friction and
meaning map without converting nonvoting into apathy or hardship into a vote
mechanism; the next step remains a dated repeated or event-based design.

The [HTOPS subgroup record](records/us-htops-material-trust-subgroups-2025.json)
and [subgroup finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-020.md)
now extend the April-to-June 2025 same-respondent panel by income and
race/ethnicity. The material-to-Congress-confidence cross-lag changes direction
across groups, so a pooled hardship-to-trust rule is not safe. This remains a
selected-panel descriptive result: attribution, action, remedy, and
attrition-adjusted population inference are open.

The [NBER real-wages/elections record](records/us-nber-real-wages-inflation-elections-2021-2024.json)
and [political-economy finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-021.md)
now synchronize the NBER study already referenced in the theme connections.
Its full-paper audit now preserves the 3,102-county frame, data construction,
state fixed effects, controls, robust/state-cluster bootstrap uncertainty, and
preferred wage–price-gap coefficients. Individual attribution, replication
materials, and county-to-person linkage remain open; county results are not
pooled with ANES respondent evidence.

The [NBER stimulus-transfer comparison](records/us-nber-stimulus-transfer-electoral-incentives-italy-2014.json)
and [full-paper finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-022.md)
add an international causal-design comparator. Italy's salient transfer
shows how receipt, consumption response, attribution, electoral reward, and
withdrawal punishment can diverge; it supplies a template for the US public-
system and stimulus lane, not a US estimate.

The [USDA food-security trend record](records/usda-food-security-2024.json)
adds a basic-security source with four conditional observations. It preserves
low versus very low food security, adult/child shielding, and assistance as a
coping/resource measure. The next step is same-period or longitudinal alignment
with prices, work, benefits, care, health, local access, and recovery.

The [BLS food-price trend record](records/us-bls-food-price-index-2020-2024.json)
adds the dated material-pressure side of that lane: food-at-home prices rose
through 2024 even as annual inflation moderated after 2022. This remains a
national index context, not a household trigger or causal estimate; the next
step is to align prices with household resources, benefits, local access, and
food-security timing.

The [SHED food-pressure trend record](records/us-shed-food-pressure-adaptation-2024-2025.json)
adds two annual household snapshots with income gradients and separate price
adaptations. It strengthens the pressure-to-adaptation comparison but is not a
linked panel; the next step remains a same-unit sequence connecting price or
income timing to food security, benefit receipt, care, health, and recovery.

The [Federal Reserve 2025 price-adaptation and judgment record](records/us-federal-reserve-price-adaptation-judgment-2025.json)
adds a current material-to-meaning layer: price pressure, household action,
bill/food hardship, personal financial status, and national economic judgment.
The next step is a valid same-respondent or event design that observes
attribution, trust, civic action, voting, and recovery after the adjustment.

The [July 2026 Census HTOPS/HPS record](records/us-census-htops-hps-material-trust-july-2026.json)
adds a current same-round bridge from expense and price perception to energy,
food, assistance, anxiety/loneliness, and institutional judgment. Its detailed
[finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-016.md)
shows why these endpoints must remain separate. The next test is replicate-
weighted subgroup comparison across corrected March/May and July 2026 releases,
then a dated event or panel design for attribution, recovery, and action.

That replicate-weighted comparison is now in the [March–May–July 2026 finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-017.md).
The broad expense measure is nearly flat from corrected May to July, while food,
energy, and institutional judgment move differently; the next step is a formal
independent-snapshot contrast table plus a same-person/event design. The 2026
files must not be described as a recontact panel because Census shifted HTOPS
from longitudinal collection in 2025 to cross-sectional HPS-focused releases
in March 2026.

The first [April–June 2025 same-respondent HTOPS linkage](projects/us-cost-trust-politics/findings/us-cost-trust-politics-018.md)
now supplies that missing identifier bridge for 6,564 respondents. It shows
persistence and entry/exit cells for expense difficulty, food insufficiency,
energy bills, price perception, job loss, federal-statistics judgment, and
Congress confidence. The next test is attrition conditioning and a documented
longitudinal weight or event-linked exposure; the current April-weighted result
must remain a selected-retention descriptive panel.
The [baseline-retention audit](projects/us-cost-trust-politics/data/htops-2025-panel-attrition-audit.json)
now shows lower retention in lower-income and materially pressured cells, so
the attrition-conditioning requirement is active rather than a generic caveat.
The [cross-lagged audit](projects/us-cost-trust-politics/data/htops-2025-cross-lagged-panel-audit.json)
now shows baseline expense difficulty alongside later food, energy, and
job-loss outcomes without a parallel Congress-confidence shift; the next test
is dated exposure and a valid attrition or event adjustment.

The new [Federal Reserve income-volatility and support layer](projects/us-cost-trust-politics/federal-reserve-income-volatility-support-2025-layer-v1.md)
adds the room around that adaptation: income timing, outside-household help,
public assistance, month-end margin, and the mix of substitution, delay,
savings, borrowing, and extra work. It remains a population distribution; the
next step is still a same-family dated-event comparison with time, care,
health, recovery, and attribution.

The [BIS household monetary-policy record](records/us-bis-household-monetary-policy-beliefs-2026.json)
adds a randomized expectations channel: households report small spending
responses to hypothetical rate increases, while inflation expectations appear
to carry more of the response than expected income or rates alone. The survey
design does not close the actual-contract, household-room, trust, or political-
action arrows.
The [cross-source monetary-policy finding](projects/us-household-monetary-policy/findings/us-household-monetary-policy-001.md)
now connects the randomized expectations channel to separate Federal Reserve
price-adaptation and GSS judgment layers. It is a bounded mechanism synthesis;
same-household rate exposure, lived adjustment, and later political action
remain open.
The [NBER design-comparison record](records/us-nber-monetary-policy-information-treatments-2026.json)
and [finding](projects/us-household-monetary-policy/findings/us-household-monetary-policy-002.md)
now add a full-paper measurement result: hypothetical, randomized-information,
and actual-announcement designs agree on expectation direction, while the
one-year inflation response is about −2.04 pp for the 25 bp vignette, −0.83 pp
for the full RCT, and −0.72 pp for the balanced event-study panel. Prior
knowledge and announcement exposure explain much of the raw gap. The next step
is pre-registration alignment and borrower/saver exposure with realized-action
tests; no spending, debt, trust, or political effect is claimed.
The follow-up [expectation-to-intended-action finding](projects/us-household-monetary-policy/findings/us-household-monetary-policy-003.md)
now compares that expectation layer with BIS/NBER intended durable-spending
and portfolio responses. It preserves the non-comparable rate sizes, outcomes,
samples, and designs; the next depth pass is a realized borrower/saver event
or matched contract-exposure design, not another expectation survey.
The [Federal Reserve financial-exposure record](records/us-federal-reserve-financial-buffer-credit-exposure-2025.json)
now adds liquidity, revolving credit, linked credit-record balance growth,
student-loan repayment difficulty, and retirement-account actions. The [New
York Fed aggregate-credit comparison](projects/us-household-financial-pressure/findings/us-household-financial-pressure-005.md)
places current debt stocks and delinquency beside those household layers while
keeping aggregate, survey, and linked-record units separate. The realized
borrower-to-payment-to-trust arrow remains open.
The [SIPP utility-credit-savings joint finding](projects/us-household-financial-pressure/findings/us-household-financial-pressure-006.md)
now adds a same-month person-record bridge: utility-payment difficulty is
associated with more carried balances and less savings-account ownership, but
the resource-stratified pattern shows that credit access and hardship are not
the same axis. The next precision gate is Fay-BRR variance and adjacent-month
ordering, followed by matched account-level bill and payment outcomes.
The new [Federal Reserve partisan-trust finding](projects/us-fed-partisan-trust/findings/us-fed-partisan-trust-001.md)
adds the messenger-credibility layer: perceived in-group/out-group status is
associated with trust, inflation expectations, information demand, and source
weighting. The next test is whether that filter changes realized household
behavior after a dated communication, and whether attribution reaches political
judgment or action.
The [New York Fed Economic Heterogeneity Indicator record](records/us-nyfed-economic-heterogeneity-2025.json)
adds the distributional cost context: constructed inflation gaps, earnings
ratios, and income-stratified consumption directions through late 2025. It
sharpens the question of whose lived basket and spending room a policy message
describes, while preserving the derived-index and panel-selection limits.
The [April 2026 EHI vintage](records/us-nyfed-economic-heterogeneity-april-2026.json)
preserves the next-period reversal: gasoline-price pressure moved several
lower-income, racial/ethnic, rural, and regional groups above the national
inflation average, while lower-income groups reduced real gasoline spending
more. This creates a dated shock-and-adaptation test, not a household causal
estimate; the next step is to align actual fuel exposure, commuting, income,
and later trust or political judgment.
The [EHI small-business capacity record](records/us-nyfed-small-business-capacity-2025.json)
adds the firm side of that shock context: profitability, revenue expectations,
employment, pricing power, financing, and debt diverge by firm size. The next
local-business test is whether those firm outcomes alter services, jobs,
customer prices, and household security in a defined place.
The [regional EHI record](records/us-nyfed-economic-heterogeneity-regional-april-2026.json)
adds that place condition for the Second District: regional inflation and
transportation costs exceeded national levels while small-business revenue and
employment expectations weakened more sharply. The next test is a valid
place-level household/firm/service join, not a causal inference from regional
averages.
The accompanying [regional price-and-firm-capacity finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-015.md)
now writes that bounded interpretation in detail and preserves the counterexample
that lower real gasoline use can reflect substitution or travel composition,
not necessarily deprivation. Household incidence, service loss, trust, and
political action remain open.
The [SIPRI 2025 military-expenditure record](records/us-sipri-military-expenditure-2025-state-capacity.json)
updates the geopolitical state-capacity vintage: global spending rose while US
spending fell and European/Asian spending accelerated. The next test is to
connect allocation to procurement realization, industrial capacity, fiscal and
social trade-offs, and observed alliance or external behavior.

The [defense resource-to-capability finding](projects/ai-work-control/findings/ai-work-control-048.md)
now connects SIPRI and IMF resource/fiscal stages to a bounded USAspending
supplier extract and Poland-US procurement/co-production announcements. It
preserves the distinction between allocation, contract, supplier structure,
implementation plan, realized capability, and leverage; the next test is
verified production/delivery, local incidence, replaceability, and an observed
external response.

The [AI work adoption/control record](records/us-ai-work-adoption-control-2024-2026.json)
promotes the current work/technology comparison into the shared registry. It
keeps productivity, time, task performance, adoption depth, and worker power
separate across studies. The next step is within-occupation or within-workplace
longitudinal evidence on training, discretion, monitoring, correction, pay,
voice, and whether saved time remains with workers.

The [BLS JOLTS national mobility record](records/us-bls-jolts-national-mobility-2020-2025.json)
adds a seasonally adjusted establishment-based context for openings, hiring,
quits, layoffs, and total separations. The next work/control pass should
condition this cooling aggregate pattern by occupation, industry, establishment
size, worker demographics, union coverage, and AI exposure; the aggregate
series cannot establish who gained or lost control.
The [2026 partial-year JOLTS refresh](records/us-bls-jolts-national-mobility-2026-ytd.json)
extends the context through July using the BLS public series pages. Openings
are slightly above the 2025 annual mean while hires are similar and quits are
lower; July is preliminary. The detailed [finding](projects/ai-work-control/findings/ai-work-control-037.md)
keeps this as establishment context, not worker bargaining evidence.

The [selected-industry JOLTS record](records/us-bls-jolts-selected-industry-mobility-2022-2025.json)
adds manufacturing, professional/business services, education/health
services, and leisure/hospitality endpoint comparisons. The next step is to
join sector mobility to worker demographics, union coverage, AI exposure,
wages, schedules, and household room while preserving each source's unit.
The [JOLTS/union industry context record](records/us-bls-jolts-union-industry-context-2025.json)
now supplies that conditioning map: 2025 sector mobility beside formal
representation in manufacturing, professional/business services,
education/health services, and leisure/hospitality. The next step is a
compatible worker or workplace event design with schedules, pay, grievance
routes, AI exposure, household room, and exit; the bridge itself is not causal.

The [JOLTS/union/earnings context record](records/us-bls-jolts-union-earnings-industry-context-2025.json)
adds CES average hourly earnings as a third sector dimension. The next step is
now a compatible worker/workplace event design with worker exposure, schedule,
grievance, health, household, and exit outcomes; the three aggregate frames
cannot answer that by themselves.
The [2026 CES earnings record](records/us-bls-ces-industry-earnings-2026-ytd.json)
adds an eight-month update for the same four sector families. The [partial-year
finding](projects/ai-work-control/findings/ai-work-control-038.md) preserves
the pay-versus-mobility boundary; it does not replace the required
worker/workplace event design.
The [August 2026 Employment Situation record](records/us-bls-employment-situation-2026-august.json)
adds a current CPS/CES labor-market surface. Its [finding](projects/ai-work-control/findings/ai-work-control-039.md)
keeps unemployment, participation, payrolls, pay, hours, long-term
unemployment, and industry movement separate from JOLTS mobility and sector
earnings; the next step remains a same-worker or same-workplace design for
control, voice, household room, and exit.
The follow-up [labor-to-household-room finding](projects/ai-work-control/findings/ai-work-control-040.md)
connects the BLS surface to SIPP resource/job timing, Federal Reserve liquidity
and repayment, and New York Fed aggregate credit. The next acquisition remains
a common worker/workplace event design that observes household room, rule
changes, voice, and exit together.
The [BEA July 2026 income-and-outlays record](records/us-bea-personal-income-outlays-2026-july.json)
adds a current macro benchmark for income, PCE, outlays, saving, and
services-versus-goods composition. Its [finding](projects/us-household-financial-pressure/findings/us-household-financial-pressure-007.md)
keeps national accounts separate from household buffers and identifies the
September 30 annual update as the next required vintage check.
The [BEA Q2 2026 growth/profits record](records/us-bea-gdp-corporate-profits-2026q2.json)
adds a macro-firm conditioning layer for output, private demand, prices, and
profits. Its [finding](projects/ai-work-control/findings/ai-work-control-041.md)
keeps aggregate growth separate from worker control and household benefit; the
next step is a named-sector or firm/workplace bridge with distributional data.
The new [sector mobility, representation, and pay finding](projects/ai-work-control/findings/ai-work-control-034.md)
publishes that boundary as a detailed cross-source result and preserves
counterexamples where pay, membership, and quits do not align. The next pass
must obtain worker/workplace timing and control outcomes rather than adding
another aggregate sector ranking.
The follow-up [task-adoption/sector synthesis](projects/ai-work-control/findings/ai-work-control-035.md)
adds NBER's within-work adoption boundary: task use is not sector mobility,
and neither is worker control. The next acquisition target is a compatible
worker/workplace design with employer permission, monitoring, training,
correction, bargaining, and household outcomes.
The [worker/workplace event ledger](projects/ai-work-control/worker-workplace-event-ledger-v1.md)
now turns that missing key into an acquisition contract. It specifies event,
worker, exposure, outcome, voice, household, and exit tables, preserves the
source-role boundaries for NBER, BLS, SIPP, Federal Reserve, BEA/BIS, OECD/ILO,
OFR, World Bank, and IMF, and requires opt-outs, non-events, reversals, and
successful human-support counterexamples. It is a design artifact, not a
worker-level result.
The [firm AI expectations finding](projects/ai-work-control/findings/ai-work-control-044.md)
adds the executive-side baseline: 69% firm use, limited reported retrospective
effects, and larger forward expectations that diverge between employers and
employees. The next pass must test which expectations become implementation,
worker time/control, staffing, pay, household, and voice outcomes; expectations
must not be counted as realized effects.
The [worker-power finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-011.md)
records the resulting measurement boundary and counterexamples: quits,
membership, and average pay can point in different directions. The next pass
must obtain worker/workplace-level timing, schedule control, grievance route,
and household consequences rather than ranking sectors by one aggregate.

The [NHTS mobility-options record](records/us-nhts-urban-rural-mobility-options-2022.json)
promotes the existing transport comparison into the registry. It preserves
vehicle access, recent rideshare use, and work-trip mode differences without
calling them dependence or access. The next step is a common-geography join to
capacity, fares/fuel, travel time, service use, and missed work/care.
The [NHTS mobility-pressure record](records/us-nhts-mobility-material-work-care-2022.json)
now adds a reproducible place-by-income screen: vehicle scarcity, recorded
work-trip duration, and shopping-trip duration are kept as separate household
and travel-day measures. It strengthens the material/time bridge but remains
cross-sectional and uses shopping as only a daily-life proxy. The next step is
to connect this layer to actual fares, fuel/repair costs, care and medical
trips, missed activities, and a repeated household calendar.
The [ACS annual transportation layer](records/us-acs-transport-annual-national-2023-2024.json)
adds an independent national household/worker frame: no-vehicle households and
30-plus-minute commutes both move modestly from 2023 to 2024. It does not
replicate NHTS's urban/rural or income cells because its published universes
and geography are different. The next mobility test is state/place and
income-conditioned ACS tables with margin-of-error handling, followed by an
explicit comparison to NHTS rather than a respondent-level merge.
The [ACS state-income transportation context](records/us-acs-transport-state-income-context-2024.json)
now executes that state extension. Its non-monotonic vehicle/commute pattern is
a counterexample to a single mobility-burden score; the next test is explicit
household-income, urban-form, race, disability, transit-mode, and provider-
capacity conditioning with margin-of-error handling.
The [ACS PUMS mobility subgroup record](records/us-acs-pums-mobility-subgroups-2024.json)
now adds the household/person test. It shows a steep income gradient in vehicle
scarcity but a distinct long-commute gradient by income and race; this separates
resource access from time exposure. The next test is design-based uncertainty,
state/urban-form/transit interactions, and actual fare, fuel, repair, care, and
missed-activity measures.
The new [mobility cross-source synthesis](projects/us-household-calendar-integration/findings/us-household-calendar-integration-017.md)
promotes the comparison into a bounded finding: vehicle scarcity, commute time,
shopping time, income, race, and urban/rural context are distinct currencies.
The counter-patterns prevent a single mobility-burden score, while the
underlying layers remain cross-sectional and differently weighted. The next
test is a compatible place-year design with fares, reliability, care/medical
trips, missed activity, and alternatives.
The [SHED care/work adaptation record](records/us-shed-care-work-adaptation-2024.json)
adds the care-by-employment comparison to the registry. It preserves the
counterexample that being employed does not erase caregiver pressure and that
nonworking caregivers can still face substantial adaptation. The next step is
care-hour, schedule-control, paid-support, recipient-outcome, and longitudinal
recovery evidence.

The [large-load state-rate governance record](records/us-large-load-state-rate-governance-2025-2026.json)
adds the domestic institutional-response layer to the infrastructure lane. It
keeps Virginia approved provisions, Texas proposed rules, Georgia disclosure
requirements, modeled incidence, and public participation distinct. The next
step is implementation evidence: actual load, contracts, deposits, bills,
cost recovery, local effects, and observed public or provider response.

The [Chicagoland immigration-attitude record](records/us-chicagoland-immigration-belonging-action-2026.json)
adds a direct local meaning layer with three documented geographies and
conditional legal-inclusion measures. It remains a local attitude case rather
than a national or causal estimate; the next step is a valid same-geography
join to material conditions, belonging, attribution, trust, and civic action.
The [ANES immigration meaning/action record](records/us-anes-immigration-meaning-action-2024.json)
adds the national comparator with weighted complex-design cross-tabs for
economic meaning, job competition, legal inclusion, trust, and reported vote.
The next step is a repeated or event-based design with measured exposure,
attribution, identity, trust, action, and vote—not a larger pooled attitude
index.

The [SHED condition-path record](records/us-shed-panel-adaptation-condition-path-2024-2025.json)
is now promoted after an official-file rerun and checksum audit. The key
correction is reduced-savings persistence: 71.0%, 58.7%, and 55.0% across
worsened, same, and improved financial-condition paths. The next test is to
attach dated price, income, health, housing, or employment events and then
observe attribution, trust, action, and recovery in the same respondent.
The [paired health/care finding](projects/us-household-financial-pressure/findings/us-household-financial-pressure-002.md)
now extends that panel into health direction and unpaid adult-care entry/exit.
It preserves the counterexample that financial improvement does not guarantee
health improvement and that care can enter under any financial path. The next
test is care intensity, schedule control, dated triggers, and recipient or
worker outcomes—not another pooled stress index.
The [panel work/health/care synthesis](projects/us-household-financial-pressure/findings/us-household-financial-pressure-011.md)
adds work-more, borrowing, and reduced-use persistence to those same paths.
The next test remains care intensity, paid/unpaid hours, schedule control,
dated triggers, and recipient or worker outcomes—not another pooled stress
index.
The [SHED weight-surface audit](projects/us-household-financial-pressure/shed-panel-weight-audit-layer-v1.md)
confirms that the public-use files contain main and panel weights but no
replicate or variance fields. Design-based uncertainty remains an explicit
acquisition gap rather than an invented standard error.

The [NBER payment-incidence layer](projects/us-household-financial-pressure/nber-w35067-payment-incidence-layer-v1.md)
now closes the earlier HBS-only review gap for the payment-rewards mechanism.
Its modeled merchant incidence should be paired with CFPB, SHED, and CEX/BLS
household evidence without treating the estimated transfer as an observed
household loss. The next test remains a matched payment exposure, price,
liquidity, and later-outcome design, with a surcharge or cash-discount
counterexample.
The [payment-system incidence finding](projects/us-household-financial-pressure/findings/us-household-financial-pressure-003.md)
now publishes the merchant-to-household bridge with modeled and observed
units kept separate; it does not create a household welfare or political
effect estimate.

The [CFPB 2025 credit-card market layer](projects/us-household-financial-pressure/cfpb-credit-card-market-2025-layer-v1.md)
now supplies the adjacent market surface for that test: balances, APRs,
assessed interest and fees, promotional balances, credit-tier patterns, and
disputed recurring transactions. These are separate market and administrative
units; the next pass must not read them as the NBER transfer or as a
same-household loss. The [TCCP product layer](projects/us-household-financial-pressure/cfpb-tccp-card-terms-2025-layer-v1.md)
now provides the public offer surface—APR, credit-tier variation, promotions,
fees, and rewards—for the next matched account/consumer test.

The [TCCP 2024–2025 comparison](projects/us-household-financial-pressure/cfpb-tccp-terms-trend-2024-2025-layer-v1.md)
adds a reproducible two-period offer-surface test. Its next step is field-level
harmonization across 2022–2025 and, where available, linkage to approval,
assigned terms, account use, balance, fees, rewards, and repayment. Product-row
changes must not be promoted to consumer exposure or market growth.
The accompanying [card-offer surface finding](projects/us-household-financial-pressure/findings/us-household-financial-pressure-004.md)
now records the visible-choice versus practical-access boundary in detail and
keeps the borrower-weighted cost, household room, remedy, trust, and exit
arrows open.

The [automatic-saving multi-currency bridge](findings/us-automatic-saving-multi-currency-policy-bridge-001.md)
now promotes the Auto-IRA project into the cross-source program layer. It places
NBER/CRI policy-exposure results beside Federal Reserve liquidity/credit and BEA
aggregate income/spending, preserves the conflicting balance-sheet estimates as
an unresolved harmonization task, and keeps current consumption, later work,
security, trust, and political response distinct. The next pass is a common
worker-level harmonization or appendix replication, not another aggregate
retirement ranking.

The material/time/inequality lane now has a design-based SIPP intersection in
the [work limitation × children × resources layer](projects/us-household-calendar-integration/sipp-fay-brr-disability-children-resource-layer-v1.md).
It adds a 16-cell comparison with Fay-BRR uncertainty. The next missing step is
care hours, schedule control, and genuine monthly work or benefit transitions;
household members under 18 must not be treated as a direct care measure.

The [SIPP care/work tenure × poverty layer](projects/us-household-calendar-integration/sipp-care-work-tenure-poverty-layer-v1.md)
adds a person-weighted distributional screen for paid child care, help paying,
and reported work constraint. Renter records show higher reported work
constraint than owner/buyer records across the displayed poverty bands, while
payment incidence rises at higher income and help is more concentrated in lower
income bands. The fields have different conditional universes and no
replicate-weight variance in this screen, so this is a societal distribution,
not a tenure or income causal estimate. The next missing step remains care
hours, schedule control, provider reliability, and a dated work/care event.

The same-respondent SHED panel now extends beyond financial adaptation in the
[health and adult-care path layer](projects/us-household-financial-pressure/shed-panel-health-care-path-layer-v1.md).
It shows health direction and entry/exit from unpaid adult care by financial
condition path. The next missing step is care intensity, schedule control,
trigger attribution, and later meaning or action—not another broad condition
cross-tab.

The place/public/politics lane has a distinct [CPS participation-friction
baseline](projects/us-cost-trust-politics/cps-2024-turnout-participation-friction-layer-v1.md).
It separates reported voting, registration, schedule, health, transport,
administrative, and candidate-related barriers. The next missing step is a
same-person or repeated-election design linking a defined material or
institutional exposure to interpretation, civic action, and vote.

The [worker representation and political availability bridge](projects/us-cost-trust-politics/worker-representation-political-availability-bridge-v1.md)
now places the BLS collective-representation baseline beside the CPS barrier
mix. It establishes two societal resources—formal workplace voice and usable
political time—without pretending they are the same respondents. The next step
is a worker-event or matched-workplace design with schedule control, grievance
route, civic action, and follow-up.

The [CCES material/work proxy trust-action layer](projects/us-cost-trust-politics/cces-material-proxy-trust-action-layer-v1.md)
adds a respondent-level descriptive screen using gig work and student-loan
responsibility alongside federal/state trust and civic action. Its non-monotonic
joint pattern is a useful counterexample; the next step is still a repeated or
event-based design with timing, attribution, prior identity, and uncertainty.

The follow-up [CCES subgroup layer](projects/us-cost-trust-politics/cces-material-trust-action-subgroup-layer-v1.md)
conditions that screen by ordered income-code bands and race groups. It shows
that the pooled proxy/trust/action pattern is heterogeneous, not a single
class-wide response. It remains descriptive: the next step is a repeated or
event-based design with timing, attribution, prior identity, and a valid
complex-survey variance procedure.

The infrastructure/state-power lane now has a US physical-demand baseline in
the [data-center energy load layer](projects/ai-work-control/us-data-center-energy-load-baseline-v1.md).
It separates historical electricity use, modeled future demand, policy claims,
local incidence, and state leverage. The next missing step is a place-utility
panel that observes approved versus actual load, cost allocation, local gains,
and public or provider replaceability.

The [large-load rate-risk control layer](projects/ai-work-control/large-load-rate-risk-control-layer-v1.md)
now specifies the institutional levers—upfront payments, collateral, minimum
commitments, take-or-pay, flexible load, separate tariffs, and queue management—
that can move risk among data-center firms, utilities, existing ratepayers, and
the state. The next step is still a two-place utility comparison with approved
and actual load, terms, bills, local benefits, and credible exit.

The [state rate-case comparison](projects/ai-work-control/large-load-state-rate-case-comparison-v1.md)
now supplies that comparison's policy spine: Virginia approved a large-load
framework, Texas has a proposed long-term billing/security framework, and
Georgia documents the load and revenue records needed for accountability. The
remaining work is implementation and incidence, not another policy summary.

The [Prince William County GIS incidence layer](projects/ai-work-control/prince-william-data-center-gis-incidence-layer-v1.md)
adds a local physical pipeline: 246 building records and 75 campus records,
with status, gross floor area, and planning-district concentration. It does
not measure load, bills, jobs, water, or community benefit. The next
infrastructure step is therefore a matched utility/place comparison, not a
larger national projection.

The [Prince William fiscal-revenue layer](projects/ai-work-control/prince-william-data-center-fiscal-revenue-layer-v1.md)
now adds the county's reported 2012–2024 data-center tax-revenue series plus a
separately sourced TY2025 extension ($465.9 million, up 59%). It advances
pipeline/operation → public-revenue visibility, but tax-rate changes,
preliminary status, and the changed source format are explicit boundaries. The
next step remains actual load, utility cost allocation, local service cost,
jobs/wages, and public response—not treating revenue as net local benefit.

The [fiscal-capacity bridge](projects/ai-work-control/prince-william-data-center-fiscal-capacity-bridge-v1.md)
now places the fiscal jump beside reported capacity and the local GIS pipeline.
This is matched-place context, not a revenue-per-MW or household-incidence
claim. The next infrastructure pass should obtain utility/load, water,
service-cost, employment, and resident-response evidence for the same place and
period.

The [Virginia large-load governance layer](projects/ai-work-control/virginia-large-load-governance-reliability-layer-v1.md)
now adds official regulatory and utility-response evidence: two reported
large-load drop events and a GS-5 framework for customers at or above 25 MW,
with minimum-demand obligations effective in 2027. The next test is actual
docket/customer cost allocation and a same-place household or community
outcome, not treating the tariff design as proof of avoided cost shifting.
The SCC's Rider T1 materials now provide a modeled $2.90-to-$0.94 typical-
residential projected increase comparison, while a Dominion filing provides
an initial 139-account/131-data-center GS-5 snapshot; both remain projections
or filings rather than observed customer incidence.

The new [data-center fiscal and governance synthesis](projects/ai-work-control/findings/ai-work-control-033.md)
joins the national LBNL demand model, Prince William's GIS and fiscal records,
and the Virginia–Texas–Georgia policy-stage comparison. It closes a useful
research-architecture gap—national demand, local pipeline, public revenue, and
institutional response are now visible in one bounded memo—while preserving
the missing actual-load, household-incidence, net-public-value, legitimacy,
and provider-exit tests. The next step is a dated matched-place utility ledger,
not another undifferentiated data-center projection.

The GIS layer now quantifies the planning concentration: Brentsville and
Gainesville hold 43.1% and 42.2% of planned campus GFA, with a four-district
planned-GFA HHI of 0.381; only 5.2% of campus planned GFA is in completed
projects in the snapshot. These are targeting metrics, not realized load or
incidence. The next step remains a matched utility/place comparison.

The public-system lane now has an intersectional SNAP transition outcome in the
[work limitation × children hardship layer](projects/us-safety-net-access/sipp-snap-transition-outcome-disability-children-fay-brr-layer-v1.md).
It adds 16 transition cells with Fay-BRR uncertainty. The next missing step is
the same-episode notice, effort, amount, remedy, interpretation, and action
ledger; another receipt cross-tab should not be treated as a substitute.

The follow-up [race × work limitation × children hardship layer](projects/us-safety-net-access/sipp-snap-transition-outcome-race-disability-children-fay-brr-layer-v1.md)
adds 64 cells and shows why the public-system distribution cannot be reduced to
one disability, race, or receipt average. Stable-state cells are interpretable;
rare entry/exit cells remain a design signal because their uncertainty is wide.
The next step is still the same-episode ledger, not an unbounded pile of
cross-tabs.

The [compound hardship layer](projects/us-safety-net-access/sipp-snap-transition-reason-compound-hardship-layer-v1.md)
adds a joint rent/mortgage-plus-utility outcome to the reason comparison. It
shows that receipt entry and recorded exit can both coexist with simultaneous
housing insecurity. This is a stronger material-security endpoint, but it does
not replace the missing notice, effort, amount, remedy, interpretation, and
action fields.

The [SNAP reason × following-hardship layer](projects/us-safety-net-access/sipp-snap-transition-reason-outcome-fay-brr-layer-v1.md)
now connects recorded entry/exit reasons to the following hardship fields on
the same adjacent-month person record. It separates job loss, income loss,
disability, family, and administrative routes. The next step remains a true
episode ledger with notice, route effort, amount, remedy, meaning, and action.

The new [reason uncertainty finding](projects/us-safety-net-access/findings/us-safety-net-access-011.md)
reruns the recorded reason categories with 240-replicate Fay–BRR intervals.
It confirms that job loss or reduced wages is the largest classified entry
category, while `other` dominates classified exits; the unclassified
transition gap remains explicit. This strengthens the reason stage without
closing the same-episode route or interpretation arrow.

The [public-system buffer-and-credit bridge](projects/us-safety-net-access/findings/us-safety-net-access-012.md)
now places the SIPP transition and following-hardship layers beside the 2025
Federal Reserve SHED liquidity, revolving-credit, linked-balance, student-loan,
and retirement-action layers. It is deliberately a non-pooled mechanism map:
the next test is a same-episode route ledger that can observe notice, benefit
amount, credit or cash response, household outcome, interpretation, and later
recovery together.

The [route-and-buffer synthesis](projects/us-safety-net-access/findings/us-safety-net-access-013.md)
now adds the WBNS lived-route and charitable-food layers to that mechanism map.
It sharpens the public/private substitution question—whether receipt,
interruption, cash or credit, supplemental food, and unmet need occupy the same
episode—without treating the separate published universes as a pooled result.
The next empirical gate remains the authenticated WBNS file or a linked route
ledger with notice, amount, gap days, remedy, buffer response, and recovery.

The [same-episode implementation specification](projects/us-safety-net-access/same-episode-event-ledger-implementation-v1.md)
now turns that next step into linked episode, route, decision, outcome, and
meaning/action tables with a multi-place sampling plan and source-role
contract. It is an acquisition instrument, not evidence that those fields are
already observed.

The [ATUS annual time-use finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-020.md)
now supplies the population-level time-architecture anchor: 2024–2025 annual
samples show modest movement across paid work, travel, household work, care,
childcare, eldercare, and socializing, while gender and life-stage ordering
persists. It is explicitly not a respondent panel or causal event study. The
next material/time pass should connect a dated pressure or care event to
desired versus actual time, schedule control, alternatives, recovery, and
meaning/action in a valid same-unit design.

The [SIPP monthly transition finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-021.md)
adds a same-person timing gate: explicitly monthly income-to-poverty bands and
job-count categories change on different clocks, while annual/reference-period
hardship fields are kept out of monthly event interpretation. This advances the
material/work backbone without claiming causality or household-weighted
volatility. The new SNAP-context pass adds monthly person earnings beside
household resources and job counts with Fay–BRR uncertainty. The next test is
hours, work loss/gain, care/time loss, and following recovery, preserving the
separate person, household, and reference-period universes. The new three-month
following-context pass now establishes the timing backbone; the remaining
missing stage is the same-episode administrative and lived outcome.
The [SIPP resource/job cross-lag finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-024.md)
now tests both directions with Fay-BRR uncertainty: resource band at month *t*
to job-count change at *t+1*, and job count at *t* to resource-band change at
*t+1*. The next material/work gate is monthly earnings, hours, SNAP status,
care/time loss, and a following hardship or recovery outcome.

The [intersectional material-room finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-022.md)
now promotes the race × tenure × monthly-resource comparison into a detailed
reader-facing memo. A current-vintage SIPP rerun reproduces the prior
Fay–BRR estimates and adds a control result without creating a new trend
observation. The next extension remains household composition, disability,
and a downstream work/care or institutional outcome in the same valid unit.

The [work-limiting-condition material-room finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-023.md)
adds the pre-specified race × disability × resource refresh. It keeps the
current v16 estimates separate from the earlier v10 vintage because the cells
are directionally consistent but not identical. The next test is tenure,
household composition, and a downstream work/care or institutional outcome.

The new [work-limitation × monthly resource/job cross-lag finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-025.md)
adds a same-person Fay-BRR test of whether monthly resource and job movement
differs by reported work-limiting status. The result is a conditional
descriptive transition screen, not a disability, accommodation, causal, or
household estimate; the next test is to add monthly hours, earnings, SNAP,
care/time, and housing fields with aligned universes.

The follow-up [work-limitation × monthly earnings/hours cross-lag finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-026.md)
adds valid numeric `TPEARN` and `TMWKHRS` outcomes to that same-person design.
It shows distinct earnings-change and hours-change surfaces while preserving
their separate valid-pair universes. Direction, desired hours, accommodation,
care response, and downstream security remain open.

The new [work/care/health cross-source bridge](projects/us-household-calendar-integration/findings/us-household-calendar-integration-027.md)
places the SIPP monthly work transition, ATUS standardized care-time contrast,
and MEPS longitudinal health-cost change in one architecture. It does not pool
the sources or create a burden index; the next gate remains a same-person or
valid matched design linking dated care/health events to money, time, coverage,
recovery, and later meaning or action.

The new [utility-to-work following-month screen](projects/us-household-calendar-integration/findings/us-household-calendar-integration-028.md)
adds a same-person SIPP timing layer: reported utility-payment difficulty or
energy-assistance status at month *t* is placed beside earnings and hours change
at month *t+1*, with Fay-BRR uncertainty. Earnings changes are common across
all groups, while the utility-difficulty hours estimate is imprecise; the
assistance comparison is selected and non-causal. The next test is a dated bill
or provider event linked to payment, assistance route, care/travel time, work,
and later hardship or recovery—not another generic monthly cross-tab. Its
2026-09-14 full-input reproduction audit confirms the published computation and
hashes, so the next pass should advance the event key rather than repeat this
screen.

The new [utility-difficulty × tenure following-work layer](projects/us-household-calendar-integration/sipp-utility-work-tenure-following-layer-v1.md)
conditions that same-person monthly transition by owned/bought versus rented
status. Among utility-difficulty respondents, next-month earnings movement is
80.5% for owners/buyers and 82.5% for renters; hours movement is 7.6% in both
groups, with Fay-BRR intervals and distinct valid-pair denominators retained.
This sharpens the housing-position comparison but does not identify a bill
shock, tenure effect, desired-hours response, care substitution, or recovery.
The next decisive gate remains a dated provider/bill event or the authenticated
PSID backbone, not another undated cross-sectional housing split.

The follow-on [utility-difficulty × tenure × child-care layer](projects/us-household-calendar-integration/sipp-utility-tenure-childcare-layer-v1.md)
adds the compatible annual `EWORKMORE` time/care universe. Child-care
arrangements reportedly prevented work or more work for 9.35% of owners/buyers
and 8.13% of renters inside utility-difficulty cells, versus 2.84% and 5.01%
without reported difficulty. The difficulty cells are small and the measure is
annual rather than a monthly bill response; this is a bounded descriptive
bridge, not a utility, tenure, or care causal result. The next decisive test
remains a dated bill/service event or the authenticated PSID backbone.

The new [CDC PLACES/CBP/HRSA place diagnostic](projects/us-local-business-place/findings/us-local-business-place-007.md)
adds modeled county social-need outcomes to the capacity and mobility lane. The
lowest health-establishment-capacity quartile has higher transportation, food,
housing, utility, mental-distress, and uninsured medians than the highest
quartile, while routine-checkup medians are nearly unchanged. The next test is
component-level HRSA geography plus travel, wait, price, insurance acceptance,
provider workload, and actual care use; this county screen remains ecological
and cross-vintage.
The [PLACES vintage comparison](projects/us-local-business-place/findings/us-local-business-place-008.md)
now adds a same-county release check across 2,885 FIPS. It shows why a newer
modeled measure cannot be promoted into a resident-level local trend: the
BRFSS, population, ACS, geography, measure, and availability surfaces change.
The next place pass must carry confidence limits, harmonized universes,
component-level HPSA geography, travel/wait/price, and actual care use.
The [HPSA component diagnostic](projects/us-local-business-place/findings/us-local-business-place-009.md)
now conditions the current PLACES surface on geographic, population, facility,
tract, low-income, and migrant/seasonal designation categories. The next place
pass must move from categories to component boundaries, designated populations,
provider locations, hours, insurance acceptance, wait, travel, and service use;
overlapping county medians are not a treatment comparison.
The [HPSA operational-field audit](projects/us-local-business-place/findings/us-local-business-place-010.md)
shows that the designation file contains useful FTE, score, shortage, and
population fields but with type-specific missingness; the next acquisition must
link component IDs to provider locations, active status, hours, acceptance,
wait, travel, and service use rather than treating missing operational fields
as zero.

| Theme | Current anchor | Next depth pass | Required counterexample | Durable output |
|---|---|---|---|---|
| 1. Household room and consumption | SHED panel, CE income-quintile spending, food security, SIPP, prices | Follow a dated price/payment event through spending, food, debt, health, and recovery in the same unit | Pressure rises but no other need is displaced because a buffer or substitute protects the unit | Event-ledger extract plus distribution table |
| 2. Time as hidden price | ATUS, NHTS, caregiving, multiple-job, participation-friction layers | Measure waiting, travel, care, paperwork, and schedule control beside the money response | A high-time-cost route does not reduce work, care, rest, or civic availability | Time-displacement comparison |
| 3. Consumer power and recourse | CFPB process/product layers, complaint records, platform and repair findings | Trace first contact, effort, response, verified remedy, abandonment, switching, and later trust | A difficult route still produces a timely verified remedy and equal exit | Same-case recourse ledger |
| 4. Platforms, data, and attention | Pew source ecosystems, platform/data/agency layer, privacy and review findings | Compare the same issue across source environments, measuring encounter, interpretation, sharing, and action separately | Exposure differs but belief/action does not, or users retain practical inspection and exit | Respondent/source measurement table |
| 5. Work, control, and bargaining | AI work-control cases, SIPP work transitions, job-lock and employer records | Pair a tool, benefit, or schedule change with pay, hours, discretion, health, worker voice, and exit | Productivity or benefit change occurs without reduced control or bargaining room | Worker-event comparison |
| 6. Care, health, and social reproduction | SHED 2024/2025 care layers, care/work split, ATUS plan, medical-cost research | Follow a recurring care need through paid/unpaid labor, work, food/housing, health, and recipient outcome | Care remains high while work, health, and recipient safety remain stable through real support | Same-family longitudinal design or explicit acquisition gap |
| 7. Housing, place, and mobility | Insurance, housing, energy, NHTS, CBP, HRSA, migration/place profiles | Match place risk and local capacity to travel, price, repair, service use, move/stay, and work | Low nominal capacity is offset by neighboring access, public provision, or affordable mobility | Matched-place panel |
| 8. Unequal exposure and status | SIPP intersectional Fay-BRR layers, SHED panels, USDA, ATUS, migration | Estimate joint distributions of cash, time, support, rights, access, and exit rather than one demographic penalty | A high-exposure group retains options through an observed institution or social network | Distribution and uncertainty register |
| 9. Trust, identity, and cultural meaning | ANES trust/meaning, Pew source trust, CFPB cultural themes, migration meaning design | Measure attribution, dignity, belonging, blame, legitimacy, and norm change after a defined encounter | Hardship occurs without distrust, or trust changes without the predicted material exposure | Meaning/action instrument |
| 10. Public systems and policy feedback | SIPP SNAP transitions/reasons/Fay-BRR, administrative-burden and event-ledger designs | Follow notice, effort, receipt, interruption, remedy, security, interpretation, and later action | Exit follows improved security or a low-burden route yields no material loss | Same-episode public-system ledger |
| 11. Political judgment and collective action | ANES worry/judgment/trust/vote, CPS participation friction, Pew engagement styles | Use repeated respondents or a policy event to separate exposure, attribution, trust, civic action, and vote | Pressure does not change judgment; judgment changes without pressure; trust changes without action | Longitudinal political instrument |

The [ANES party-conditioned worry/vote layer](projects/us-cost-trust-politics/anes-panel-worry-vote-party-conditioned-layer-v1.md)
adds a controlled descriptive check to this lane. It shows that the pooled
relationship between financial worry and reported presidential vote cannot be
read as one society-wide mechanism: among strong partisans, vote choice is
highly concentrated within prior identity across worry categories, while
independents show more visible worry/vote variation. The SDA export has no
design-based standard errors, so this is a conditioning result, not a causal
estimate or a claim about every subgroup.
| 12. Firm, sector, and market power | BFS, BDS, CBP, establishment scale, firm/market-power layer, CFPB | Follow one firm or sector decision across customer, worker, owner, place, and public-system outcomes | Similar decision leaves terms unchanged because alternatives or worker/customer power are real | Matched firm-event record |
| 13. Infrastructure, technology, and dependency | AI capacity/ownership cases, state-leverage ledger, domestic-capacity bridge | Verify operational capacity, ownership, local incidence, energy/water burden, interoperability, and switching | Capacity rises with local learning, public inspection, and provider replaceability | Realization/control ledger |
| 14. Geopolitical and state consequences | Tariff/price, energy, finance, migration, and AI state-leverage layers | Trace domestic capacity or dependence to an observed state choice, external response, alliance, or leverage change | Domestic dependence does not alter strategic choice, or capability is replaceable without external concession | State-leverage case comparison |

The [Pew teen social/AI layer](projects/us-digital-habits-attention/pew-teens-social-ai-2025-layer-v1.md)
adds an adolescent subgroup and separates socially embedded platform use from
instrumental chatbot use. The next test is measured substitution, family or
school mediation, and practical exit—not another undifferentiated screen-time
or adoption count.
The [digital-life synthesis](projects/us-digital-habits-attention/findings/us-digital-habits-attention-005.md)
now supplies the cross-source comparison across adults, teens, AI use, news,
and civic styles. The next test is a matched age-specific encounter panel with
purpose, content, trust, error, correction, human alternative, and exit—not a
single screen-time or platform-reach index.

The [ATUS work-location finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-029.md)
adds a current published-table counterexample to the work/time lane: working at
home and working at the workplace are overlapping locations, not autonomy
measures. The next test is a same-worker location/rule event with total hours,
care interruptions, monitoring, pay, representation, health, and exit; the
2025 federal-shutdown coverage warning must remain attached to annual estimates.
The [directional SIPP finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-030.md)
adds the missing sign to the adjacent-month work transition: earnings increases
and decreases are separated, and hours are usually unchanged. The next pass
must condition those directions on children, tenure, SNAP, hardship, and care
flags before following them to a later material or assistance outcome.

The [IMF Article IV finding](projects/ai-work-control/findings/ai-work-control-045.md)
adds the country-surveillance layer to the macro/state lane: output and
productivity resilience coexist with fiscal, external, tariff, energy, and
financial-stability risks. The next test is a dated adjustment or policy event
joined to firm, household, worker, and political-response outcomes; IMF
projections must remain conditional scenarios rather than realized trends.

The [Federal Reserve financial-stability and monetary-policy finding](projects/ai-work-control/findings/ai-work-control-046.md)
adds the institutional-financial layer: system resilience can coexist with
selected household delinquency, tight credit, elevated inflation, high asset
valuations, and funding-risk exposure. The next test is a dated rate, energy,
tariff, credit, or funding event joined to borrower type, firm size, repayment or
spending response, and later trust, institutional use, or political action; Fed
aggregates must not be treated as household welfare or causal political evidence.

The [public financial-capacity and household-room bridge](projects/ai-work-control/findings/ai-work-control-047.md)
puts BEA, Federal Reserve, OFR, IMF, SHED, and New York Fed evidence into one non-pooled
macro-to-household architecture. It distinguishes aggregate growth and profits,
financial-system conditions, public market visibility, fiscal scenarios,
aggregate debt/delinquency, and household liquidity. The next test remains a dated event joined to compatible
exposure, immediate adjustment, attribution, action, and later remedy or recovery.

The reader-facing [macro-to-household financial-capacity synthesis](projects/us-financial-intermediation/macro-to-household-financial-capacity-synthesis-v1.md)
now makes that architecture legible as a long-form route. It adds the IMF
Financial Access Survey and World Bank Findex provider/user distinction and
keeps the central counterexamples visible: macro growth can coexist with low
household room, provider expansion can coexist with unusable access, and public
monitoring capacity is not itself a customer outcome. The same-unit dated
financial event remains the next empirical gate.

## Sequencing rule

Run the next passes in four rotating lanes so breadth is preserved:

1. **Material and time:** themes 1, 2, 6, and 8;
2. **Consumer, platform, and work power:** themes 3, 4, 5, and 12;
3. **Place, public systems, and politics:** themes 7, 10, and 11;
4. **Meaning, infrastructure, and state consequences:** themes 9, 13, and 14.

After each lane produces one depth artifact, return to the widest lane with
the fewest measured arrows. Do not add a new narrative packet merely because
an existing open link is difficult; record the acquisition or identification
gap and test a counterexample instead.

## Promotion rule

A provisional societal trend may be strengthened only when the next pass adds
at least one of the following: a same-unit or valid matched design, a second
time period, a subgroup or place conditioning check, design-based uncertainty,
a verified institutional outcome, or a measured reversal/counterexample. A
cross-source alignment without one of these remains context, not a completed
arrow.

## Relationship to the program

This queue operationalizes the [14-theme inventory](US-BROAD-THEME-INVENTORY_V1.md),
the [coverage matrix](US-BROAD-THEME-COVERAGE-MATRIX_V1.md), the [trend register](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md),
and the [broad trend-extraction protocol](US-BROAD-TREND-EXTRACTION-PROTOCOL_V1.md).
The [recovery brief](../END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md) remains the
canonical end-to-end objective.
