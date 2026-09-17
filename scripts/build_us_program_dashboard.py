#!/usr/bin/env python3
"""Build the server-visible control dashboard for the long-term US program."""
from __future__ import annotations
import html, json
from datetime import date
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
records = [json.loads(p.read_text()) for p in sorted((ROOT / "analysis/records").glob("*.json"))]
themes = [
 ("household_room_consumption", "Household room and consumption"), ("time_hidden_price", "Time, care, and social reproduction"),
 ("consumer_power_recourse", "Consumer power and recourse"), ("platforms_data_attention", "Platforms, data, and attention"),
 ("work_control_bargaining", "Work, control, and bargaining"), ("care_health_reproduction", "Care, health, and reproduction"),
 ("housing_place_mobility", "Housing, place, and mobility"), ("unequal_exposure_status", "Unequal exposure and status"),
 ("trust_identity_meaning", "Trust, identity, and meaning"), ("public_systems_feedback", "Public systems and policy feedback"),
 ("political_judgment_action", "Political judgment and collective action"), ("firm_sector_market_power", "Firm, sector, and market power"),
 ("infrastructure_technology_dependency", "Infrastructure, technology, and dependency"), ("geopolitical_state_consequences", "Geopolitical and state consequences"),
]
theme_counts = Counter(t for r in records for t in r.get("program_theme_ids", []))
observations = sum(len(r.get("observations", [])) for r in records)
source_packets = len(list((ROOT / "analysis").glob("**/source-search-*.md")))
source_families = [
 ("Household and time", "SIPP, SHED, PSID, ATUS, MEPS, RECS, CE, NHTS"),
 ("Economic and financial", "BEA, BLS, Federal Reserve, OFR, NBER"),
 ("Public systems and firms", "CFPB, FTC, USAspending, DLA, company filings"),
 ("Opinion, culture, and politics", "Pew, Gallup, ANES, GSS, CCES, local attitude studies"),
 ("International and geopolitical", "IMF, World Bank, SIPRI, ILO, OECD and comparable institutions"),
]
def esc(x): return html.escape(str(x))
rows = "".join(f"<tr><td>{esc(title)}</td><td>{theme_counts.get(tid, 0)}</td><td>{'covered' if theme_counts.get(tid) else 'open'}</td></tr>" for tid,title in themes)
families = "".join(f"<article><h3>{esc(a)}</h3><p>{esc(b)}</p></article>" for a,b in source_families)
arrows = "".join(f"<li>{esc(x)}</li>" for x in [
 "material pressure → same-unit time/care substitution → health, recovery, trust, and political action",
 "complaint or institutional route → verified remedy → repeat effort, switching, exit, and trust",
 "work/tool or infrastructure change → control and bargaining → household and local power",
 "domestic affordability and capacity → state legitimacy and geopolitical leverage"])
findings = [
 ("Automatic saving is a multi-currency policy, not a single security outcome", "us-automatic-saving-multi-currency-policy-bridge-001.html", "NBER/CRI Auto-IRA, Federal Reserve SHED, and BEA"),
 ("Macro shock can become a household and legitimacy problem", "ai-work-control-024.html", "IMF WEO, World Bank, SIPRI, Federal Reserve, and ANES"),
 ("Unequal optionality is the recurring structure behind pressure, adaptation, and power", "us-broad-program-unequal-optionality-path-001.html", "Program-level cross-source synthesis"),
 ("Care time is a household price paid in work, money, and reachable places", "us-care-time-hidden-price-matched-evidence-001.html", "ATUS, SHED, NHTS, and SIPP"),
 ("Material pressure can become a time and participation transfer", "price-pressure-time-social-participation-cross-source-bridge-v1.html", "SHED, ATUS, SIPP, NHTS, and CPS"),
 ("Income volatility changes the room available for adaptation", "us-cost-trust-politics-007.html", "Federal Reserve household survey"),
 ("AI adoption is not the same as workplace control", "ai-work-control-021.html", "NBER task-level adoption indexes"),
 ("The map of AI work changes with the measurement layer", "ai-work-control-027.html", "NBER, O*NET, and platform-measurement comparison"),
 ("Broad AI-work headlines are not simple sums of detailed task rates", "ai-work-control-028.html", "NBER DWA/BWA and O*NET-prefix consistency diagnostic"),
 ("Broad genAI adoption can rise quickly while control remains unmeasured", "ai-work-control-029.html", "Published Management Science article and NBER W35677"),
 ("A rate decision becomes a household story through expected costs", "us-household-monetary-policy-001.html", "BIS/NBER, Federal Reserve SHED, and GSS"),
 ("The same Federal Reserve message can arrive as information or partisan threat", "us-fed-partisan-trust-001.html", "NBER Working Paper 33071, with BIS and Federal Reserve context"),
 ("The national price story fragments into different household baskets", "us-cost-trust-politics-008.html", "New York Fed EHI, Federal Reserve SHED, and NBER"),
 ("A gasoline shock can reverse the apparent distribution of inflation", "us-cost-trust-politics-009.html", "April 2026 New York Fed EHI"),
 ("New York Fed EHI vintage comparison: December 2025 to April 2026", "us-nyfed-ehi-vintage-comparison.html", "Reproducible cross-vintage comparison"),
 ("A profitable small firm can still be losing local room", "us-local-business-place-001.html", "New York Fed EHI / Small Business Credit Survey"),
 ("The gasoline shock links household room, firm capacity, and public interpretation", "us-cost-trust-politics-010.html", "New York Fed EHI, SHED, NBER, and BIS"),
("A national shock can be sharper for a region's households and firms", "us-local-business-place-002.html", "April 2026 New York Fed regional EHI"),
("A regional price shock can narrow household room and firm room at the same time", "us-cost-trust-politics-015.html", "New York Fed regional EHI and Small Business Credit Survey"),
 ("The July 2026 household pulse separates pressure, assistance, and trust", "us-cost-trust-politics-016.html", "Census HTOPS/HPS public-use file and data dictionary"),
 ("Utility hardship is associated with more balance carrying and less savings", "us-household-financial-pressure-006.html", "Census SIPP same-month utility, credit, savings, and Fay-BRR diagnostic"),
("Digital reach, loss, and remedy are different control surfaces", "us-digital-habits-attention-007.html", "Pew digital-life, FTC, Federal Reserve SHED, and CFPB route evidence"),
 ("Bill-payment convenience can become a hidden household cost", "us-doxo-bill-payment-hidden-fees-001.html", "FTC Doxo complaint, settlement proposal, and case record"),
 ("A platform remedy can reach workers and diners without proving lived recovery", "us-grubhub-platform-remedy-001.html", "FTC Grubhub enforcement and refund-program records"),
 ("Practical exit is the missing consumer-power outcome", "practical-exit-cross-domain-synthesis-v1.html", "CFPB, CPSC, SHED, and platform-remedy comparisons"),
("Capacity and mobility cells do not carry one political response", "us-local-business-place-005.html", "CBP/ACS/HRSA/NHTS place context and county-keyed CES trust/action"),
 ("Three 2026 Census pulse snapshots show movement without one household story", "us-cost-trust-politics-017.html", "Census HTOPS/HPS corrected March, May, and July PUFs with replicate weights"),
 ("Linked HTOPS respondents show material and institutional measures changing on different paths", "us-cost-trust-politics-018.html", "Census HTOPS April–June 2025 linked PUFs and replicate weights"),
 ("Material pressure, care, and work appear as different SIPP constraints", "us-household-calendar-integration-001.html", "Census SIPP 2024 reference year"),
 ("SIPP material and food-security estimates survive a design-based uncertainty check", "us-household-calendar-integration-002.html", "Census SIPP official universes and Fay-BRR replicate weights"),
 ("SIPP care constraints are measurable, but payment, assistance, and lost work are different stages", "us-household-calendar-integration-003.html", "Census SIPP child-care universes and Fay-BRR replicate weights"),
 ("Paid care, assistance, and work constraints diverge across SIPP income bands", "us-household-calendar-integration-004.html", "Census SIPP income-to-poverty strata and Fay-BRR replicate weights"),
 ("Renters report more child-care work constraint while owners report more paid care", "us-household-calendar-integration-005.html", "Census SIPP tenure strata and Fay-BRR replicate weights"),
 ("SIPP care and work measures differ by race group, but the recode is not cultural meaning", "us-household-calendar-integration-006.html", "Census SIPP race strata and Fay-BRR replicate weights"),
 ("Work-limiting disability status is associated with less paid care, not clearly less reported work prevention", "us-household-calendar-integration-007.html", "Census SIPP disability strata and Fay-BRR replicate weights"),
 ("Regional SIPP differences are sharper for reported work prevention than paid-care use", "us-household-calendar-integration-008.html", "Census SIPP regional strata and Fay-BRR replicate weights"),
 ("SIPP child-presence comparisons expose a care-universe boundary", "us-household-calendar-integration-009.html", "Census SIPP child-presence and reference-parent universes"),
("SIPP’s “no under-18” care records are a timing and universe issue, not a childless-care finding", "us-household-calendar-integration-010.html", "Census SIPP reference-parent universe audit"),
("Eldercare often reaches beyond the provider’s household, but the roster does not measure burden", "us-household-calendar-integration-011.html", "BLS ATUS 2024–2025 eldercare roster comparison"),
("Eldercare providers show a distinct time profile, but the ATUS contrast is not causal", "us-household-calendar-integration-012.html", "BLS ATUS 2024–2025 provider/nonprovider time comparison"),
("Basic composition control preserves part of the eldercare time profile", "us-household-calendar-integration-013.html", "BLS ATUS 2024–2025 standardized provider-time comparison"),
("Eldercare time contrasts survive richer composition controls, with annual variation", "us-household-calendar-integration-014.html", "BLS ATUS 2024–2025 richer standardized provider-time comparison"),
("The visible complaint-response system shifted again in 2025", "us-customer-automation-recourse-015.html", "CFPB 2020–2025 published complaint-response trend"),
("CFPB response routes remain product-shaped in 2025", "us-customer-automation-recourse-016.html", "CFPB 2024–2025 product-conditioned response routes"),
 ("CFPB student-loan timing fields are not interchangeable", "us-customer-automation-recourse-017.html", "CFPB API field audit and 2025 Consumer Response Annual Report"),
 ("A public CFPB route ledger can observe handoff without claiming remedy", "cfpb-public-event-ledger-acquisition-audit-2026-09-14.html", "CFPB public administrative route records and validated event-ledger contract"),
 ("A public complaint ledger observes institutional handoff, not consumer remedy", "us-customer-automation-recourse-019.html", "CFPB 25-case student-loan event ledger"),
("SIPRI 2025 military expenditure: spending is capacity context, not capability", "ai-work-control-030.html", "SIPRI 2025 military-expenditure vintage"),
("Capacity is not leverage until an actor can refuse, switch, or impose a cost", "ai-work-control-023.html", "SIPRI, USAspending/DLA, defense realization, infrastructure, and large-load governance layers"),
("AI capability can grow faster than shared control", "ai-work-control-031.html", "BIS, NBER, BEA, IMF, OFR, World Bank, and Federal Reserve SHED"),
("A cooling labor market does not have one meaning of worker power", "us-cost-trust-politics-011.html", "BLS JOLTS, CPS union membership, and CES earnings"),
("Housing security is split between making the payment and keeping the risk covered", "us-housing-insurance-risk-001.html", "Federal Reserve, Treasury FIO, FEMA, GAO, and residual-market records"),
("Digital life is not one platform trend", "us-digital-habits-attention-005.html", "Pew adult, teen, AI, news, and civic-engagement surveys"),
("Health spending can rise while household payment and health direction diverge", "us-health-cost-household-choice-001.html", "MEPS Panel 27 longitudinal health-cost file"),
("Coverage transitions shape care and adaptation paths without an insurance effect estimate", "us-health-cost-household-choice-end-to-end-001.html", "SHED 2024–2025 coverage-transition panel and local reproduction audit"),
("Financial dissatisfaction is a trust signal before it is a vote mechanism", "us-cost-trust-politics-012.html", "GSS 2024 financial position, trust, fairness, and vote intention"),
("Material pressure enters politics through several unsynchronized channels", "us-cost-trust-politics-013.html", "Federal Reserve SHED, GSS, ANES panel, and CCES"),
("A benefit can be lost without the need going away", "us-safety-net-access-matched-evidence-001.html", "NBER, USDA, and Census SIPP transition/hardship evidence"),
("State SNAP participation is not a simple poverty or mobility ranking", "us-safety-net-access-001.html", "USDA FY2025 state rates and 2024 ACS state transportation context"),
("Participation is not administrative performance", "us-safety-net-access-002.html", "USDA/FNA FY2025 participation, application timeliness, recertification timeliness, and 2023 PAI"),
("Recertification failure is a lived interruption", "us-safety-net-access-003.html", "Urban December 2024 WBNS notice, time, paperwork, interview, and interruption evidence"),
("The SNAP route can change receipt before it changes security", "us-safety-net-access-004.html", "USDA/FNA, Urban WBNS, NBER route studies, and Census SIPP"),
("Material pressure is jointly distributed across work limitation, children, and resources", "us-household-calendar-integration-015.html", "SIPP 2024 reference year, official universes, and 240 Fay-BRR replicates"),
("Household selection changes the apparent size of SIPP material pressure", "us-household-calendar-integration-016.html", "SIPP person-record versus reference-person household-month diagnostic"),
("Mobility burden is split between vehicle scarcity, distance, and time", "us-household-calendar-integration-017.html", "NHTS 2022 and ACS 2024 household, person, trip, and state-context layers"),
("Financial recovery, health, and care do not move on one schedule", "us-household-financial-pressure-002.html", "Federal Reserve SHED 2024–2025 recontact panel"),
("US firms report widespread algorithmic management before worker control is measured", "ai-work-control-032.html", "OECD 2024 employer survey across six countries"),
("Data-center growth turns digital capability into a local fiscal and governance test", "ai-work-control-033.html", "LBNL, Prince William County GIS/revenue, and Virginia–Texas–Georgia large-load governance"),
("Annual time categories move modestly while the social architecture remains unequal", "us-household-calendar-integration-020.html", "BLS ATUS 2024–2025 annual diary samples and replicate weights"),
("Monthly resources and job counts move on different clocks", "us-household-calendar-integration-021.html", "Census SIPP 2025 public-use person-month transitions"),
("SNAP transitions can coincide with resource decline without a clear job-count change", "us-safety-net-access-007.html", "Census SIPP monthly SNAP transitions, income-ratio/job context, and Fay-BRR replicate weights"),
("Annual child-care routes differ across stable SNAP states while transition cells are too sparse", "us-safety-net-access-008.html", "Census SIPP November–December SNAP states and annual child-care fields with Fay-BRR replicate weights"),
("The month after a SNAP transition, resources still move more than jobs or hours", "us-safety-net-access-009.html", "Census SIPP three-month SNAP/resource/earnings/hours/job sequences with Fay-BRR replicate weights"),
 ("Administrative routes can change receipt without changing work or security", "us-safety-net-access-010.html", "NBER SNAP route studies, Census SIPP following sequences, and WBNS acquisition gate"),
("SNAP transition reasons separate job loss from other entry and exit paths", "us-safety-net-access-011.html", "Census SIPP 2025 public-use person-month records and Fay-BRR replicates"),
("Safety-net receipt can shift the route without closing the household gap", "us-safety-net-access-013.html", "USDA/FNA, Urban WBNS, Census SIPP, Federal Reserve SHED, and charitable-food route evidence"),
("Public systems are encountered as routes, buffers, and judgments—not as one trust score", "us-safety-net-access-014.html", "USDA/FNA route performance, WBNS barriers, SIPP hardship transitions, and Gallup institutional confidence"),
("CFPB “timely” is not elapsed routing time, and the public field surface changes by vintage", "us-customer-automation-recourse-021.html", "Live CFPB 2024/2025 case-route timestamps, response labels, and field-presence audit"),
 ("A broad defense supplier surface can remain financially concentrated", "ai-work-control-072.html", "USAspending JASSM/LRASM subaward recipient concentration and component-description audit"),
 ("The same household calendar pressure changes across race and tenure intersections", "us-household-calendar-integration-022.html", "Census SIPP 2024 reference-year fields and Fay-BRR replicate weights"),
 ("Disability and resources do not form one universal care-and-work pattern", "us-household-calendar-integration-023.html", "Census SIPP 2024 reference-year fields and Fay-BRR replicate weights"),
("Fraud recovery burden differs by age, income, and payment route", "us-consumer-fraud-trust-001.html", "Federal Reserve SHED 2024 fraud and recovery subgroup extraction"),
("Reported scam losses rose into 2025, but the household recovery path remains unmeasured", "us-consumer-fraud-trust-002.html", "FTC Consumer Sentinel, Federal Reserve SHED, and CFPB response routes"),
 ("Worry and reported vote align differently across party groups", "us-cost-trust-politics-014.html", "ANES 2024 panel worry, economic judgment, party, and vote fields"),
 ("Payment rewards redistribute modeled merchant incidence without measuring household welfare", "us-household-financial-pressure-003.html", "NBER payment-rewards model and Federal Reserve SHED adaptation context"),
 ("A larger public card-offer surface does not mean cheaper credit for households", "us-household-financial-pressure-004.html", "CFPB TCCP, NBER payment incidence, and Federal Reserve household context"),
("Task adoption and sector movement do not identify worker control", "ai-work-control-034.html", "NBER task adoption, BLS mobility, union coverage, and earnings"),
("A 2026 opening rate does not restore worker mobility", "ai-work-control-037.html", "BLS JOLTS January–July 2026 partial-year refresh"),
("Sector pay context does not restore worker control", "ai-work-control-038.html", "BLS CES January–August 2026 earnings and JOLTS mobility context"),
('A steady August labor market still leaves worker security and control unresolved', 'ai-work-control-039.html', 'BLS August 2026 CPS/CES Employment Situation and industry changes'),
('A steady labor market does not guarantee household room', 'ai-work-control-040.html', 'BLS, SIPP, Federal Reserve, and New York Fed cross-source bridge'),
('Growth and profits do not settle who gains control', 'ai-work-control-041.html', 'BEA Q2 2026 GDP, private demand, prices, and corporate profits'),
('Aggregate income growth does not identify household financial room', 'us-household-financial-pressure-007.html', 'BEA July 2026 income, PCE, outlays, saving, and household-pressure context'),
 ("A task-level adoption index is not evidence of worker authority", "ai-work-control-035.html", "NBER W35677 task adoption and BLS sector mobility/union/pay context"),
 ("Worker control requires a common workplace event key", "worker-workplace-event-ledger-v1.html", "Acquisition design linking NBER, BLS, SIPP, Federal Reserve, firm, and governance layers"),
 ("Infrastructure completion and ownership change do not by themselves establish sovereignty", "ai-work-control-036.html", "Romania and Malaysia data-center milestones, capacity plans, and ownership records"),
 ("A defense relationship can move toward reciprocal industrial room", "ai-work-control-042.html", "Official Poland-US-Estonia-Latvia procurement and co-production announcements"),
 ("Agreement-stage reciprocity is not yet realized capability or leverage", "ai-work-control-043.html", "Poland implementation and realization watchpoint"),
 ("Work location is not schedule control", "us-household-calendar-integration-029.html", "BLS ATUS 2025 work-location, care, education, and shutdown-coverage context"),
 ("Earnings change is not earnings gain, and hours change is not hours loss", "us-household-calendar-integration-030.html", "Census SIPP monthly directional transitions by resource band and work-limiting status"),
("A household can absorb pressure in money, time, health, or work—and the sources observe different clocks", "us-household-calendar-integration-033.html", "SIPP, MEPS, SHED, and ATUS end-to-end material/time/care synthesis"),
 ("Energy cost is also equipment risk and assistance dependence", "us-household-calendar-integration-034.html", "2020 RECS income-band energy expenditure, assistance, disconnection, and equipment vulnerability"),
("Baseline health spending marks different health and work paths, but it is not a burden score", "us-health-cost-household-choice-002.html", "MEPS Panel 27 expenditure-conditioned health and employment outcomes"),
 ("Income timing, outside help, and budget margin are different kinds of household room", "us-household-financial-pressure-013.html", "Federal Reserve 2025 SHED income, support, variability, and price-adaptation surfaces"),
("Firm AI expectations are not realized worker outcomes", "ai-work-control-044.html", "NBER W34836 executive firm survey, retrospective effects, and forward expectations"),
 ("Macro resilience and state-finance risk are simultaneous conditions", "ai-work-control-045.html", "IMF 2026 United States Article IV consultation and projections"),
 ("Financial-system resilience does not erase selective household credit pressure", "ai-work-control-046.html", "Federal Reserve May 2026 Financial Stability Report and July 2026 Monetary Policy Report"),
 ("Public financial capacity and household room are connected stages, not one pressure index", "ai-work-control-047.html", "BEA, Federal Reserve, OFR, IMF, and SHED cross-source comparison"),
 ("Defense spending and procurement are inputs to state capacity, not proof of leverage", "ai-work-control-048.html", "SIPRI, IMF WEO, USAspending, and Poland-US defense procurement/co-production records"),
 ("Data-center capacity, public revenue, and utility governance do not identify household benefit", "ai-work-control-049.html", "LBNL, Prince William County, Virginia SCC, Texas PUC, and Georgia PSC records"),
 ("Care constraints move through work, time, household room, and mobility rather than one burden channel", "ai-work-control-050.html", "SIPP, Federal Reserve SHED, BLS ATUS, and NHTS cross-source comparison"),
 ("Material and care constraints reach political life through distinct friction and meaning routes", "ai-work-control-051.html", "CPS, SIPP, BLS ATUS, ANES, and CCES cross-source comparison"),
 ("AI assistance and algorithmic management expand faster than evidence of worker control", "ai-work-control-052.html", "NBER, OECD, and BLS cross-source AI/work-power comparison"),
 ("AI capability can expand while infrastructure, ownership, and public-control dependence remain unresolved", "ai-work-control-053.html", "World Bank, Romania/Malaysia infrastructure, OFR, and US data-center governance"),
 ("Consumer protection has visible routing but unresolved recovery, remedy, and trust gaps", "ai-work-control-054.html", "Federal Reserve SHED, FTC, and CFPB household/administrative comparison"),
 ("Housing security has payment, coverage, hazard, and backstop layers that do not yet form a move outcome", "ai-work-control-055.html", "Federal Reserve, Treasury FIO, FEMA NRI, Census, and California FAIR Plan"),
 ("Food security depends on route quality, material adequacy, and layered buffers that are not interchangeable", "ai-work-control-056.html", "USDA/FNA, Urban WBNS, and Census SIPP public-system comparison"),
 ("AI utilization and modeled output signals do not yet identify worker gain or control", "ai-work-control-057.html", "NBER, BEA, and BLS task-to-industry-to-mobility comparison"),
 ("Place capacity and population change shape different political contexts without a single belonging gradient", "ai-work-control-058.html", "CES, Census/CBP, Chicagoland survey, and ANES place-to-meaning comparison"),
 ("Household adaptation can preserve the present while consuming future room", "ai-work-control-059.html", "Federal Reserve SHED panel, hardship, care, and fraud-recovery comparison"),
 ("Consumer protection visibility can expand while remedy, attention cost, and exit remain unresolved", "ai-work-control-060.html", "CFPB, Federal Reserve SHED, Pew, and FTC consumer/platform comparison"),
("Aggregate income and labor growth can coexist with price-specific household room loss", "ai-work-control-061.html", "BEA, BLS CPI/PPI/CPS/CES/JOLTS, and Federal Reserve SHED current-vintage comparison"),
("A safety-net transition can change the route without restoring household room", "ai-work-control-062.html", "SIPP SNAP transitions, resources, work measures, and following hardship"),
 ("US firm capacity is a size-stratified bundle, not one adoption score", "ai-work-control-063.html", "World Bank Enterprise Survey US 2024 size, training, infrastructure, finance, and obstacle profile"),
 ("Firm capacity, AI adoption, and labor mobility are different gates to worker control", "ai-work-control-064.html", "World Bank Enterprise Survey, NBER task adoption, BLS representation, and JOLTS mobility"),
 ("Sector mobility, pay, and representation describe different workplace rooms", "ai-work-control-065.html", "BLS JOLTS, CES earnings, and CPS union-membership sector comparison"),
("Defense announcements, awards, tests, and production plans are different capability stages", "ai-work-control-066.html", "DoD, DSCA, Poland, USAspending, DVIDS, and production/integration records"),
("Task-adoption comparisons depend on taxonomy reconciliation", "ai-work-control-067.html", "NBER W35677 and official O*NET 31.0 crosswalk inputs"),
("Worker voice is the conversion point between AI exposure and control", "ai-work-control-068.html", "JRC AIM-WORK worker survey and ILO social-dialogue case studies"),
("AI use does not automatically produce confidence or control", "ai-work-control-070.html", "UNDP 2025 AI and Human Development survey: use, control, domains, and work expectations"),
("Financial access is broadening, but digital reach and financial room remain different surfaces", "us-financial-intermediation-001.html", "World Bank Global Findex 2025 account, device, payment, borrowing, and resilience indicators"),
("Financial-system visibility is being built as a public capability, but visibility is not household protection", "ai-work-control-071.html", "OFR 2022–2025 annual reports, IMF Financial Access Survey, Global Findex, CFPB, and SHED"),
("The US financial-access chain is broad at the doorway and thin at the remedy", "us-financial-intermediation-002.html", "Global Findex, IMF Financial Access Survey, SHED, CFPB, OFR, and FTC"),
("County capacity and lived social need align descriptively, but capacity is not access", "us-local-business-place-007.html", "CDC PLACES, Census CBP, HRSA HPSA, and county population estimates"),
("The newer PLACES vintage moves county measures without producing one local-health trend", "us-local-business-place-008.html", "CDC PLACES 2024/2025 releases, Census CBP, and same-county FIPS comparison"),
("HPSA component type changes what a county shortage label can mean", "us-local-business-place-009.html", "HRSA primary-care HPSA components/population codes and CDC PLACES 2025"),
("HPSA designations carry operational fields, but those fields are unevenly populated", "us-local-business-place-010.html", "HRSA primary-care HPSA FTE, designated/underserved population, score, shortage, and missingness audit"),
("US financial access infrastructure contracted while reported account ownership stayed high", "imf-fas-provider-side-access-audit-2026-09-15.html", "IMF Financial Access Survey 2020–2024 provider counts, branches, deposits, and loans"),
("US provider contraction is widespread across the comparison set, but not universal", "us-financial-intermediation-001.html", "IMF Financial Access Survey selected-country comparison with India, Brazil, Mexico, China, and peer counterexamples"),
("Low-income and high-risk insurance pressure is sensitive to the chosen cutpoint", "us-housing-insurance-risk-002.html", "Treasury FIO, Census ACS, FEMA risk context, and California market records"),
("Local migration capacity and political meaning are different place layers", "us-immigration-local-demand-001.html", "ACS county growth/nativity/service-capacity screen and Chicagoland attitude study"),
 ("Business applications are an early signal, not realized local capacity", "us-local-business-place-011.html", "Census BFS applications and BDS establishment/job flows by sector"),
 ("Global poverty, climate exposure, and missing data define geopolitical context", "ai-work-control-073.html", "World Bank Poverty, Prosperity, and Planet comparative context"),
]
finding_html = "".join(f'<li><a href="{esc(link)}">{esc(title)}</a> <span class="small">— {esc(source)}</span></li>' for title,link,source in findings)
style = ":root{--paper:#f4f1e9;--ink:#1d2927;--muted:#5d6965;--line:#ccd4cd;--card:#fffdf7;--accent:#155f51;--gold:#b56a26}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 system-ui,sans-serif}main{max-width:1120px;margin:auto;padding:28px 22px 80px}a{color:var(--accent)}nav{font-size:.9rem}h1,h2,h3{font-family:Georgia,serif;font-weight:500;line-height:1.15}h1{font-size:clamp(2.8rem,7vw,5.5rem);max-width:900px;margin:45px 0 20px}.lede{font:1.25rem/1.5 Georgia,serif;max-width:850px;color:#46514e}.eyebrow{color:var(--accent);letter-spacing:.1em;text-transform:uppercase;font-size:.76rem}.metrics,.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:14px;margin:25px 0}.metric,article{background:var(--card);border:1px solid var(--line);padding:20px}.metric strong{display:block;font:2.5rem Georgia,serif;color:var(--accent)}.metric span{color:var(--muted)}.grid article h3{margin:0 0 8px}.grid article p{margin:0;color:var(--muted)}table{width:100%;border-collapse:collapse;background:var(--card)}th,td{text-align:left;border-bottom:1px solid var(--line);padding:10px}th{font-weight:600}.callout{border-left:5px solid var(--gold);padding:16px 20px;background:#fff8e9}.callout p{margin:0}.small{color:var(--muted);font-size:.92rem}footer{margin-top:55px;border-top:1px solid var(--line);padding-top:18px;color:var(--muted);font-size:.9rem}@media(max-width:700px){main{padding:22px 15px}table{font-size:.9rem}}"
html_doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>US program dashboard</title><style>{style}</style></head><body><main>
<nav><a href="index.html">Research home</a> · <a href="reading-room.html">Reading room</a> · <a href="theme-trends.html">Theme insights</a> · <a href="us-broad-program-map.html">14-theme map</a> · <a href="us-trend-observations.html">Trend registry</a> · Program dashboard</nav>
<p class="eyebrow">Long-term program control · checked {date.today().isoformat()}</p><h1>A living atlas of how conditions become meaning, power, and consequence.</h1>
<p class="lede">This is the operating view of the US-centered cultural, societal, consumer, political, institutional, financial, firm, infrastructure, and geopolitical program. It is a continuing research program: each pass adds or tests evidence; no single dataset or finding completes it.</p>
<div class="callout"><p><strong>Governing question:</strong> What forces are changing how people in the United States live, spend, work, borrow, vote, and trust institutions—and how do those changes affect firms, finance, and state power?</p></div>
<h2>Governing objective</h2><p>Explain how conditions and decisions become lived social, cultural, consumer, political, institutional, firm, and geopolitical consequences, while keeping the unit, date, denominator, source vintage, uncertainty, counterexample, and missing arrow visible.</p>
<div class="metrics"><div class="metric"><strong>14</strong><span>program themes</span></div><div class="metric"><strong>{len(records)}</strong><span>validated trend records</span></div><div class="metric"><strong>{observations}</strong><span>period-specific observations</span></div><div class="metric"><strong>{source_packets}</strong><span>source-search packets</span></div></div>
<h2>Source ecosystem</h2><p class="small">The program triangulates source families. A source contributes the unit and limit it can actually support; it is not silently promoted into evidence for a different stage of the chain.</p><div class="grid">{families}</div>
<h2>Theme coverage</h2><table><thead><tr><th>Theme</th><th>Tagged records</th><th>Current state</th></tr></thead><tbody>{rows}</tbody></table>
<h2>The end-to-end chain under test</h2><p>condition, price, rule, shock, technology, or institutional decision → money, time, access, control, status, health, or security → adaptation, delay, borrowing, switching, staying, organizing, or going without → institutional, firm, media, political, or foreign response → redistribution of cost, risk, data, assets, or power → cultural meaning, trust, identity, public action, company/sector exposure, or geopolitical leverage.</p>
<h2>Open arrows and next tests</h2><ul>{arrows}</ul><p class="small">The current depth lane is the material/time/care backbone, with <a href="psid-acquisition-gate.html">PSID 2019/2021/2023 as the hard acquisition dependency</a>. The PSID route is documented but account-controlled; no PSID result is promoted as downloaded evidence.</p>
<h2>Detailed findings already written</h2><p class="small">These are bounded findings, not a claim that every arrow is closed.</p><ul>{finding_html}</ul>
<h2>Detailed research record</h2><p><a href="theme-trends.html">theme trends and insights</a> · <a href="psid-acquisition-gate.html">PSID acquisition gate</a> · <a href="nber-w35677-paper-method-audit-2026-09-14.html">NBER paper method audit</a> · <a href="onet-release-metadata-gate-v1.html">O*NET release/identifier gate</a> · <a href="nber-w35677-index-acquisition-v1.html">NBER index acquisition record</a> · <a href="us-big-picture-synthesis.html">big-picture synthesis</a> · <a href="US-CROSS-SOURCE-TREND-SYNTHESIS_V1.html">cross-source synthesis</a> · <a href="US-BROAD-EVIDENCE-MATRIX_V1.html">arrow-level evidence matrix</a> · <a href="US-BROAD-THEME-COVERAGE-MATRIX_V1.html">theme coverage matrix</a> · <a href="US-BROAD-COUNTEREXAMPLE-REGISTER_V1.html">counterexample register</a> · <a href="US-BROAD-THEME-INVENTORY_V1.html">theme inventory</a> · <a href="US-BROAD-TREND-EXTRACTION-PROTOCOL_V1.html">extraction protocol</a> · <a href="US-BROAD-PROGRAM-CONTINUITY-LEDGER_V1.html">continuity ledger</a> · <a href="US-BROAD-CURRENT-STATUS-AUDIT_V1.html">current-status audit</a> · <a href="US-TREND-METADATA-COVERAGE-AUDIT_V1.html">metadata coverage audit</a> · <a href="US-SOURCE-REGISTRY-COVERAGE-AUDIT_V1.html">source-registry audit</a> · <a href="us-source-coverage.html">source coverage</a> · <a href="us-trend-observations.html">trend registry</a> · <a href="us-evidence-audit.html">evidence audit</a></p>
<footer>Generated by <code>scripts/build_us_program_dashboard.py</code>. The Markdown control records remain in the repository alongside this published view.</footer></main></body></html>'''
(ROOT / "site/us-program-dashboard.html").write_text(html_doc)
md = f'''# US program dashboard v1

**Checked:** {date.today().isoformat()}  
**Status:** active long-term program control view

The program maintains a US-centered, cross-source living atlas of cultural,
societal, consumer, political, institutional, financial, firm, infrastructure,
and geopolitical themes. Each pass adds or tests evidence; no one dataset,
finding, or session is the completion condition.

## Governing objective

Explain how conditions and decisions become lived social, cultural, consumer,
political, institutional, firm, and geopolitical consequences, while keeping
the unit, date, denominator, source vintage, uncertainty, counterexample, and
missing arrow visible. The execution charter is the [US broad research pass](US-BROAD-RESEARCH-PASS_V1.md),
and the [evidence matrix](US-BROAD-EVIDENCE-MATRIX_V1.md) assigns each arrow to
a source and next test.

## Current scale

- **14** program themes
- **{len(records)}** validated machine-readable trend records
- **{observations}** period-specific observations
- **{source_packets}** source-search packets

## Source ecosystem

| Family | Sources |
|---|---|
'''
for a,b in source_families: md += f"| {a} | {b} |\n"
md += '''
The source families are used for triangulation. Every result keeps its unit,
date, geography, denominator, method, uncertainty, subgroup, counterexample,
and open arrow visible.

## Open arrows

- Material pressure → same-unit time/care substitution → health, recovery, trust, and political action.
- Complaint or institutional route → verified remedy → repeat effort, switching, exit, and trust.
- Work/tool or infrastructure change → control and bargaining → household and local power.
- Domestic affordability and capacity → state legitimacy and geopolitical leverage.

The active depth lane is the material/time/care backbone. The immediate PSID
2019/2021/2023 acquisition gate is documented, but account-controlled; no PSID
result is promoted as downloaded evidence before the gate is passed.

Read the [HTML dashboard](../site/us-program-dashboard.html), [continuity ledger](US-BROAD-PROGRAM-CONTINUITY-LEDGER_V1.md), [current status audit](US-BROAD-CURRENT-STATUS-AUDIT_V1.md), [source-registry audit](US-SOURCE-REGISTRY-COVERAGE-AUDIT_V1.md), and [cross-source synthesis](US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md).
'''
(ROOT / "analysis/US-PROGRAM-DASHBOARD_V1.md").write_text(md)
print(f"Built program dashboard: {len(records)} records, {observations} observations.")
