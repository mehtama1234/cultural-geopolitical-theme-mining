"""Refresh the manually designed big-picture page with current synthesis inserts."""
from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parents[1]
page = ROOT / "site/us-big-picture-synthesis.html"
html = page.read_text()
connections = json.loads((ROOT / "manifests/us-theme-connections.json").read_text(encoding="utf-8"))
edge_count = len(connections.get("edges", []))
html, lead_replacements = re.subn(r"\b\d+ recorded links\b", f"{edge_count} recorded links", html, count=1)
if lead_replacements != 1:
    raise SystemExit("big-picture lead link count not found")

# Rebuild the manually curated insert as one deterministic section. Earlier
# one-at-a-time refresh branches could append the same paragraph repeatedly;
# the published page should contain each current evidence note once.
if 'ai-work-control-035.html' in html:
    latest = '''<section id="latest-evidence"><h2>Latest evidence added to the living map</h2>
<p>The <a href="us-digital-habits-attention-005.html">Pew adult social-media layer</a> keeps adult platform reach and frequency separate from the teen platform/chatbot survey. YouTube and Facebook are broad, while Instagram and TikTok are more age-concentrated; reach is not logged attention, persuasion, or political power.</p>
<p>The <a href="us-financial-pressure-001.html">Federal Reserve household-pressure finding</a> adds the household room behind adaptation: income timing, outside support, public assistance, month-end margin, and the different choices households make under price pressure.</p>
<p>The <a href="ai-work-control-024.html">IMF April 2026 WEO finding</a> adds the macro middle between geopolitical shocks and lived conditions: growth, inflation, defense spending, debt, deficits, and possible social-spending trade-offs. These aggregate and conditional estimates do not establish household incidence, legitimacy, unrest, or alliance behavior.</p>
<p>The World Bank poverty, prosperity, and planet layer adds a distributional counterweight: global poverty concentration, climate exposure, shared-prosperity stagnation, and gaps in recent poverty-survey coverage. This is comparative context, not a US household result.</p>
<p>The <a href="ai-work-control-030.html">SIPRI 2025 military-expenditure finding</a> adds the geopolitical capacity side: global military spending reached an estimated $2.887 trillion in 2025, while US spending fell in real terms as European and Asian/Oceanian spending rose. These are fiscal and organizational inputs, not direct measures of realized capability, public legitimacy, or household welfare.</p>
<p>The <a href="us-fed-partisan-trust-001.html">Federal Reserve partisan-trust finding</a> adds the messenger layer: perceived institutional alignment is associated with trust, information demand, and the weight given to a Fed message when forming inflation expectations.</p>
<p>The <a href="us-household-calendar-integration-002.html">SIPP official-universe variance finding</a> adds a statistical-quality check to the material/time/care lane. Field-specific status flags, universes, and Fay-BRR replicate weights make comparisons more calibrated without turning person-record weights into household weights or closing the dated-trigger, time-substitution, trust, or political-action arrows.</p>
<p>The <a href="us-auto-ira-household-balance-sheets-001.html">Auto-IRA balance-sheet finding</a> adds a policy-exposure counterexample: retirement ownership/assets and checking/savings margins rise alongside a modest increase in credit-card debt. Current liquidity, future security, and voluntary choice must remain separate.</p>
<p>The <a href="ai-work-control-035.html">task-adoption and sector-mobility synthesis</a> keeps NBER task-level AI use separate from BLS establishment quits, union membership, and average pay. These are different exposure surfaces, not worker-control or household outcomes without a common worker or workplace key.</p>
<p>The <a href="us-customer-automation-recourse-018.html">consumer loss and complaint-visibility finding</a> places Federal Reserve/SHED household fraud loss and recovery burden beside CFPB complaint routing and response labels. Household harm and administrative visibility have different denominators; a complaint response is not verified recovery or practical exit.</p>
<p>The <a href="us-immigration-local-demand-001.html">local capacity and immigration-meaning finding</a> compares county growth/nativity/service-capacity screens with Chicagoland policy attitudes. Capacity stocks and respondent meaning are distinct layers; neither population growth nor foreign-born share is a proxy for belonging or political action.</p>
<p>The <a href="us-housing-insurance-risk-002.html">California insurance-sensitivity finding</a> shows that a low-income/high-risk nonrenewal ordering changes under a different income cut point. Place-market gradients therefore require pre-specified sensitivity and property-year validation before they become household displacement or insurance-failure claims.</p></section><section id="supports">'''
    latest = latest.replace('</section><section id="supports">', '''<p>The <a href="us-consumer-fraud-trust-001.html">fraud recovery burden finding</a> separates household fraud exposure, conditional unrecovered money, recovery time, and P2P route comparisons. The survey does not verify provider remedy, later trust, switching, or exit.</p>
<p>The <a href="us-cost-trust-politics-014.html">party-conditioned ANES finding</a> shows that strong partisan identity concentrates reported vote across worry categories while independents vary more visibly. The controlled export has no reproduced design-based standard errors and no dated material exposure.</p>
<p>The <a href="us-household-financial-pressure-003.html">payment-system incidence finding</a> connects NBER merchant/model evidence to separate SHED household-pressure measures. Modeled redistribution is not an observed household loss or welfare estimate.</p>
<p>The <a href="ai-work-control-036.html">infrastructure realization and control finding</a> separates Romania infrastructure completion, application migration, Malaysia operating capacity, and ownership transition. Capacity is not sovereignty, portability, or geopolitical leverage.</p>
<p>The <a href="ai-work-control-039.html">August 2026 BLS employment finding</a> adds a current labor-market checkpoint: payroll growth and low unemployment coexist with slower hiring, long-term unemployment, uneven industry movement, and modest real-room questions. A steady aggregate labor market is not the same as worker control or household security.</p>
<p>The <a href="ai-work-control-040.html">BLS/Fed/NY Fed/SIPP bridge</a> keeps labor-market steadiness separate from household exit options, liquid room, debt service, and resource/job transitions. These are linked evidence layers, not a person-level causal chain.</p>
<p>The <a href="us-household-financial-pressure-007.html">BEA July 2026 income-and-outlays finding</a> adds aggregate income, disposable income, consumption composition, and the low personal saving rate. Income growth and service-heavy spending do not identify which households have room or how they absorbed pressure.</p>
<p>The <a href="us-household-financial-pressure-008.html">August 2026 BLS CPI finding</a> adds the matching price checkpoint: CPI-U rose 0.4% in the month and 3.4% over the year, with gasoline and energy contributing materially to the movement. This is an official aggregate price index, not household hardship, substitution, borrowing, health/work effects, trust, or political response.</p>
<p>The <a href="us-household-financial-pressure-009.html">August 2026 BLS PPI finding</a> adds the upstream seller-side layer: final demand rose 0.4% in the month and 5.4% over the year, while diesel and intermediate goods moved more sharply. PPI is a possible transmission surface, not consumer pass-through, firm margin, household burden, or political-response evidence.</p>
<p>The <a href="us-household-financial-pressure-010.html">current macro cross-source synthesis</a> puts August labor, CPI, PPI, and July BEA income/outlays into one calendar-aligned conditioning frame while preserving their different units. The missing end-to-end test remains product/firm pass-through, household exposure and adaptation, recovery, trust, and political action.</p>
<p>The <a href="ai-work-control-041.html">BEA Q2 GDP-and-profits finding</a> adds growth, final-demand, price, and corporate-profit context. Economy-wide growth and profits do not settle who gains bargaining power, who bears price pressure, or whether workers can exit.</p>
<p>The <a href="ai-work-control-071.html">OFR institutional-finance finding</a> follows public financial visibility from 2022 repo and data pilots through 2025 repo collection, AI workflow use, and reported staffing/budget contraction. It strengthens the public-capacity middle between markets and households, while keeping visibility, intervention, remedy, and household protection separate.</p>
<p>The <a href="us-financial-intermediation-002.html">financial-access route synthesis</a> traces the doorway, provider setting, household failure burden, administrative response, and still-missing practical exit stage. Account and device ownership, branch density, fraud recovery, and complaint labels are complementary surfaces—not one consumer-power measure.</p>
<p>The <a href="us-local-business-place-007.html">place capacity/outcome diagnostic</a> adds CDC PLACES modeled county measures for transportation, food, housing, utility, mental-distress, insurance, and routine-care surfaces beside CBP health-sector stock and HRSA shortage components. Low/high capacity contrasts are descriptive and ecological; usable access, provider adequacy, and downstream political meaning remain open.</p>
<p>The <a href="us-local-business-place-008.html">PLACES vintage comparison</a> adds a same-county release check: routine-care and insurance measures move differently from transportation, food, housing, utility, and mental-distress measures, with changed BRFSS, population, geography, and availability inputs. It is a vintage diagnostic, not a same-resident trend or local intervention effect.</p>
<p>The <a href="us-local-business-place-009.html">HPSA component diagnostic</a> decomposes the county shortage flag into geographic, population, facility, tract, low-income, and migrant/seasonal categories. Component type changes the interpretation of the modeled county outcomes; no category is a person-level measure of reachable, affordable, effective care.</p>
<p>The <a href="us-local-business-place-010.html">HPSA operational-field audit</a> checks FTE, designated population, underserved population, score, shortage, and missingness by component type. The designation file supplies institutional context, not a complete provider-capacity ledger or patient-access outcome.</p>
<p>The <a href="us-household-calendar-integration-033.html">multi-clock material/time/care synthesis</a> puts SIPP monthly resource/work transitions beside MEPS annual health-cost/health-status transitions and SHED/ATUS care and time surfaces. These are complementary clocks, not a pooled household stress score; the dated trigger, alternative, protected/sacrificed outcome, recovery, and meaning/action chain remains the program's acquisition target.</p>
<p>The <a href="us-safety-net-access-014.html">public-system route-to-judgment synthesis</a> keeps USDA/FNA administrative timeliness, WBNS recipient barriers, SIPP following hardship, and Gallup institution-specific confidence as separate stages. It strengthens the public-system meaning route without claiming that one notice caused one hardship, trust change, or political action.</p>
<p>The <a href="us-customer-automation-recourse-021.html">CFPB route-vintage audit</a> keeps the API's <code>timely</code> label separate from elapsed receipt-to-company routing and records the current omission of <code>has_narrative</code> as unavailable. Public response labels and field changes are measurement surfaces, not verified consumer remedy or welfare trends.</p>
<p>The <a href="ai-work-control-072.html">USAspending supplier-concentration finding</a> adds a replaceability check to the state-capacity lane: one JASSM/LRASM subaward extract names 51 recipients, but the top five account for 49.50% of returned amount and the top ten 74.60%. Name breadth is not supplier independence, production, or geopolitical leverage.</p>
<p>The <a href="us-health-cost-household-choice-002.html">MEPS expenditure-conditioned finding</a> adds a same-panel test: baseline health-spending bands have different perceived-health and employment-continuity profiles. Spending is also a marker of need, age, retirement, insurance, and service mix, so this is not a causal work-loss or household-burden result.</p>
<p>The <a href="../analysis/projects/us-cost-trust-politics/htops-2026-vintage-recheck-2026-09-14.md">Census HTOPS/HPS vintage recheck</a> preserves the corrected March/May weights, July as the latest listed 2026 release, and the cross-sectional break. Movement across pulse snapshots is not a single household panel story.</p>
<p>The <a href="../analysis/projects/us-customer-automation-recourse/cfpb-api-vintage-refresh-2026-09-14.md">CFPB live-vintage recheck</a> reproduces the committed 2025 complaint aggregation against the live API while retaining the distinction between complaint visibility, response labels, verified remedy, and practical consumer exit.</p>
<p>The <a href="../analysis/US-RECURRENT-SOURCE-VINTAGE-WATCHLIST_V1.md">recurrent-source vintage watchlist</a> turns BEA, BLS, Fed, Census, CFPB, SIPP, PSID, World Bank, and defense refreshes into a continuing program: each new vintage must preserve the source, universe, unit, denominator, geography, method, uncertainty, and counterexample boundaries.</p></section><section id="supports">''', 1)
    html, replacements = re.subn(r'<section id="latest-evidence">.*?</section><section id="supports">', latest, html, count=1, flags=re.S)
    if replacements != 1:
        raise SystemExit("latest-evidence section not found for deterministic rebuild")
    page.write_text(html)
    print("REBUILT", page)
    raise SystemExit(0)

marker = '<section id="supports">'
insert = '''<section id="latest-evidence"><h2>Latest evidence added to the living map</h2>
<p>The <a href="us-digital-habits-attention-005.html">Pew adult social-media layer</a> keeps adult platform reach and frequency separate from the teen platform/chatbot survey. YouTube and Facebook are broad, while Instagram and TikTok are more age-concentrated; reach is not logged attention, persuasion, or political power.</p>
<p>The <a href="us-financial-pressure-001.html">Federal Reserve household-pressure finding</a> adds the household room behind adaptation: income timing, outside support, public assistance, month-end margin, and the different choices households make under price pressure.</p>
<p>The <a href="ai-work-control-024.html">IMF April 2026 WEO finding</a> adds the macro middle between geopolitical shocks and lived conditions: growth, inflation, defense spending, debt, deficits, and possible social-spending trade-offs. These aggregate and conditional estimates do not establish household incidence, legitimacy, unrest, or alliance behavior.</p>
<p>The World Bank poverty, prosperity, and planet layer adds a distributional counterweight: global poverty concentration, climate exposure, shared-prosperity stagnation, and gaps in recent poverty-survey coverage. This is comparative context, not a US household result; the <a href="https://www.worldbank.org/en/publication/poverty-prosperity-and-planet">official report</a> is the source page.</p>
<p>The <a href="ai-work-control-030.html">SIPRI 2025 military-expenditure finding</a> adds the geopolitical capacity side: global military spending reached an estimated $2.887 trillion in 2025, while US spending fell in real terms as European and Asian/Oceanian spending rose. These are fiscal and organizational inputs, not direct measures of realized capability, public legitimacy, or household welfare.</p>
<p>The <a href="us-fed-partisan-trust-001.html">Federal Reserve partisan-trust finding</a> adds the messenger layer: perceived institutional alignment is associated with trust, information demand, and the weight given to a Fed message when forming inflation expectations. It does not establish actual spending, borrowing, voting, or the Fed's objective political alignment.</p>
<p>The <a href="us-cost-trust-politics-009.html">New York Fed Economic Heterogeneity Indicator finding</a> adds the distributional context behind that messenger problem: constructed inflation gaps, earnings ratios, and income-stratified retail-consumption directions show why a national price or policy story can meet different lived baskets and different amounts of room to respond.</p>
<p>The <a href="us-household-calendar-integration-002.html">SIPP official-universe variance finding</a> adds a statistical-quality check to the material/time/care lane. Applying field-specific status flags, universes, and Fay-BRR replicate weights gives uncertainty intervals for hardship, food security, hunger, and job-count diagnostics. This makes comparisons more calibrated; it still does not turn person-record weights into household weights or close the dated-trigger, time-substitution, trust, or political-action arrows.</p>
<p>The <a href="us-auto-ira-retirement-claiming-001.html">Auto-IRA retirement-timing finding</a> extends the balance-sheet result: a Georgetown brief reports later work and Social Security claiming in a SIPP policy-timing comparison, while choice versus constraint, health, job quality, and net welfare remain open.</p>
</section>'''

if 'ai-work-control-035.html' not in html and 'id="latest-evidence"' in html:
    boundary = '</section><section id="supports">'
    addition = '''<p>The <a href="ai-work-control-035.html">task-adoption and sector-mobility synthesis</a> keeps NBER task-level AI use separate from BLS establishment quits, union membership, and average pay. These are different exposure surfaces, not worker-control or household outcomes without a common worker or workplace key.</p><p>The <a href="us-customer-automation-recourse-018.html">consumer loss and complaint-visibility finding</a> places Federal Reserve/SHED household fraud loss and recovery burden beside CFPB complaint routing and response labels. Household harm and administrative visibility have different denominators; a complaint response is not verified recovery or practical exit.</p><p>The <a href="us-immigration-local-demand-001.html">local capacity and immigration-meaning finding</a> compares county growth/nativity/service-capacity screens with Chicagoland policy attitudes. Capacity stocks and respondent meaning are distinct layers; neither population growth nor foreign-born share is a proxy for belonging or political action.</p><p>The <a href="us-housing-insurance-risk-002.html">California insurance-sensitivity finding</a> shows that a low-income/high-risk nonrenewal ordering changes under a different income cut point. Place-market gradients therefore require pre-specified sensitivity and property-year validation before they become household displacement or insurance-failure claims.</p></section><section id="supports">'''
    if boundary not in html:
        raise SystemExit("latest-evidence boundary not found")
    html = html.replace(boundary, addition, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'cross-paper boundary' not in html and 'id="latest-evidence"' in html:
    old = '<p>The <a href="us-auto-ira-household-balance-sheets-001.html">Auto-IRA balance-sheet finding</a> adds a policy-exposure counterexample: retirement ownership/assets and checking/savings margins rise alongside a modest increase in credit-card debt. It strengthens the current-versus-future security distinction without establishing take-home-pay, debt-cost, spending, or net-welfare effects. The <a href="us-auto-ira-retirement-claiming-001.html">retirement-timing finding</a> adds reported later work and Social Security claiming, but does not establish health, job quality, voluntary choice, or net-welfare effects.</p>'
    new = old[:-4] + ' The <a href="us-auto-ira-retirement-claiming-001.html#what-this-changes-in-the-program">cross-paper boundary</a> keeps the two designs and balance-sheet measures separate.</p>'
    if old not in html:
        raise SystemExit("Auto-IRA balance paragraph not found")
    html = html.replace(old, new, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'world-bank-poverty-prosperity-planet-2024-layer-v1.md' not in html and 'id="latest-evidence"' in html:
    boundary = '</section><section id="supports">'
    addition = '<p>The World Bank poverty, prosperity, and planet layer adds the distributional counterweight: global poverty concentration, climate exposure, shared-prosperity stagnation, and gaps in recent poverty-survey coverage. This is comparative context, not a US household result; see the <a href="https://www.worldbank.org/en/publication/poverty-prosperity-and-planet">official report</a>.</p></section><section id="supports">'
    if boundary not in html:
        raise SystemExit("latest-evidence boundary not found")
    html = html.replace(boundary, addition, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'us-fed-partisan-trust-001.md' not in html and 'id="latest-evidence"' in html:
    boundary = '</section><section id="supports">'
    addition = '<p>The <a href="us-fed-partisan-trust-001.html">Federal Reserve partisan-trust finding</a> adds the messenger layer: perceived institutional alignment is associated with trust, information demand, and the weight given to a Fed message when forming inflation expectations. It does not establish actual spending, borrowing, voting, or the Fed\'s objective political alignment.</p></section><section id="supports">'
    if boundary not in html:
        raise SystemExit("latest-evidence boundary not found")
    html = html.replace(boundary, addition, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'new-york-fed-economic-heterogeneity-layer-v1.md' not in html and 'id="latest-evidence"' in html:
    boundary = '</section><section id="supports">'
    addition = '<p>The <a href="us-cost-trust-politics-009.html">New York Fed Economic Heterogeneity Indicator finding</a> adds the distributional context behind that messenger problem: constructed inflation gaps, earnings ratios, and income-stratified retail-consumption directions show why a national price or policy story can meet different lived baskets and different amounts of room to respond.</p></section><section id="supports">'
    if boundary not in html:
        raise SystemExit("latest-evidence boundary not found")
    html = html.replace(boundary, addition, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'sipri-2025-military-expenditure-state-capacity-layer-v1.md' not in html and 'id="latest-evidence"' in html:
    boundary = '</section><section id="supports">'
    addition = '<p>The <a href="ai-work-control-030.html">SIPRI 2025 military-expenditure finding</a> adds the geopolitical capacity side: global military spending reached an estimated $2.887 trillion in 2025, while US spending fell in real terms as European and Asian/Oceanian spending rose. These are fiscal and organizational inputs, not direct measures of realized capability, public legitimacy, or household welfare.</p></section><section id="supports">'
    if boundary not in html:
        raise SystemExit("latest-evidence boundary not found")
    html = html.replace(boundary, addition, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'us-household-calendar-integration-002.html' not in html and 'id="latest-evidence"' in html:
    boundary = '</section><section id="supports">'
    addition = '<p>The <a href="us-household-calendar-integration-002.html">SIPP official-universe variance finding</a> adds a statistical-quality check to the material/time/care lane. Applying field-specific status flags, universes, and Fay-BRR replicate weights gives uncertainty intervals for hardship, food security, hunger, and job-count diagnostics. This makes comparisons more calibrated; it still does not turn person-record weights into household weights or close the dated-trigger, time-substitution, trust, or political-action arrows.</p></section><section id="supports">'
    if boundary not in html:
        raise SystemExit("latest-evidence boundary not found")
    html = html.replace(boundary, addition, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'us-safety-net-access-006.html' not in html and 'id="latest-evidence"' in html:
    boundary = '</section><section id="supports">'
    addition = '<p>The <a href="us-safety-net-access-006.html">WBNS charitable-food finding</a> adds the mixed public/private safety-net route: participation remains elevated while unmet need persists among food-insecure adults, and hours, awareness, comfort, variety, transportation, safety, and perceived treatment shape usable access. This is not provider-capacity, causal policy, trust, or political-action evidence.</p></section><section id="supports">'
    if boundary not in html:
        raise SystemExit("latest-evidence boundary not found")
    html = html.replace(boundary, addition, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'us-auto-ira-household-balance-sheets-001.html' not in html and 'id="latest-evidence"' in html:
    boundary = '</section><section id="supports">'
    addition = '<p>The <a href="us-auto-ira-household-balance-sheets-001.html">Auto-IRA balance-sheet finding</a> adds a policy-exposure counterexample: retirement ownership/assets and checking/savings margins rise alongside a modest increase in credit-card debt. It strengthens the current-versus-future security distinction without establishing take-home-pay, debt-cost, spending, or net-welfare effects.</p></section><section id="supports">'
    if boundary not in html:
        raise SystemExit("latest-evidence boundary not found")
    html = html.replace(boundary, addition, 1)
    page.write_text(html)
    print("REFRESHED", page)
elif 'id="latest-evidence"' not in html:
    if marker not in html:
        raise SystemExit("big-picture supports section marker not found")
    html = html.replace(marker, insert + marker, 1)
    page.write_text(html)
    print("REFRESHED", page)
else:
    print("UNCHANGED", page)
