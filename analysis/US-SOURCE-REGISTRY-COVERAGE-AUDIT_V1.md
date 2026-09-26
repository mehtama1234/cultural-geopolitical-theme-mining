# Source registry coverage audit v1

**Checked:** 2026-09-26

This control compares the registered source universe with the files under
`analysis/`. It distinguishes a registered source from evidence that uses
the source's domain. A domain hit can reflect a source-search packet, a
record, a finding, or a related-source citation; it is not a quality score
or proof that every source item was read in full.

- Registered source entries: **114**
- Entries with a domain reference anywhere in analysis: **114**
- Entries with a domain reference outside source-search packets: **114**
- Entries with an exact source URL in a machine record: **75**
- Entries with an exact registered-URL reference: **106**
- Registered entries with no analysis-domain hit: **0**

## Coverage states

- **evidence-bearing:** the source domain appears outside a source-search
  packet, in a record, finding, layer, bridge, or other analysis artifact.
- **machine-record URL:** the exact registered URL appears in an
  `analysis/records/*.json` object.
- **search-only:** the domain appears only in source-search packets and is
  not yet visible in a substantive evidence artifact.
- **exact URL referenced:** the registered landing URL itself appears in
  the analysis corpus.
- **no hit:** the source is registered but is not visible in the analysis
  corpus; it remains a candidate acquisition or search lane.

## Registered sources

| Source | Role | Search refs | Evidence refs | Evidence files | Record exact URL | State |
|---|---|---:|---:|---:|---:|---|
| [Harvard Business School Working Knowledge](https://www.library.hbs.edu/working-knowledge) | research story and topic discovery | 51 | 222 | 72 | 4 | evidence-bearing; machine-record URL |
| [SSRN research paper repository](https://papers.ssrn.com/) | public working-paper and preprint access for emerging social-science evidence | 2 | 22 | 20 | 9 | evidence-bearing; machine-record URL |
| [arXiv research preprints](https://arxiv.org/) | open preprint access and versioned paper text for emerging research | 0 | 23 | 13 | 10 | evidence-bearing; machine-record URL |
| [Zenodo research data archive](https://zenodo.org/) | versioned open research data and code archives | 0 | 5 | 4 | 1 | evidence-bearing; machine-record URL |
| [National Bureau of Economic Research Working Papers](https://www.nber.org/papers) | primary research and paper discovery | 152 | 1326 | 522 | 288 | evidence-bearing; machine-record URL |
| [NBER Working Papers and Chapters Metadata](https://www.nber.org/research/data/nber-working-papers-and-chapters-metadata) | coverage and trend analysis | 152 | 1326 | 522 | 0 | evidence-bearing |
| [NBER Public Use Data Archive](https://www.nber.org/research/data) | replication and extension data discovery | 152 | 1326 | 522 | 0 | evidence-bearing |
| [American Economic Association RCT Registry](https://www.socialscienceregistry.org/) | pre-registration and design-plan evidence for randomized social-science experiments | 0 | 9 | 8 | 4 | evidence-bearing; machine-record URL |
| [Urban Institute Well-Being and Basic Needs Survey](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey) | US household food, housing, health, employment, safety-net access, material hardship, and financial-security evidence | 0 | 58 | 18 | 3 | evidence-bearing; machine-record URL |
| [Microsoft Fiscal Year 2025 Annual Report](https://www.microsoft.com/investor/reports/ar25/) | company operating, workforce, infrastructure, and product evidence | 0 | 6 | 3 | 0 | evidence-bearing |
| [Whoz official product and company materials](https://www.whoz.com/en/) | small AI-forward firm and workforce-allocation product evidence | 0 | 2 | 1 | 0 | evidence-bearing |
| [Capgemini 2025 Integrated Annual Report](https://reports.capgemini.com/2025/en/) | customer/operator evidence on AI adoption, training, workforce redesign, and delivery economics | 1 | 9 | 4 | 0 | evidence-bearing |
| [Brookings Institution](https://www.brookings.edu/topics/) | policy research and competing interpretations | 0 | 3 | 3 | 0 | evidence-bearing |
| [Pew Research Center](https://www.pewresearch.org/) | public opinion, technology use, identity, and demographic change | 10 | 282 | 132 | 165 | evidence-bearing; machine-record URL |
| [World Bank Open Data](https://data.worldbank.org/) | country and development indicators | 0 | 6 | 6 | 4 | evidence-bearing; machine-record URL |
| [OECD Data](https://data-explorer.oecd.org/) | comparable country data on work, firms, tax, education, and living conditions | 0 | 1 | 1 | 0 | evidence-bearing |
| [OECD Algorithmic Management research](https://www.oecd.org/en/publications/algorithmic-management-in-the-workplace_287c13c4-en.html) | cross-country employer evidence on automated management, monitoring, evaluation, and governance | 2 | 101 | 30 | 1 | evidence-bearing; machine-record URL |
| [IMF Data](https://data.imf.org/en) | macro, fiscal, trade, balance-of-payments, and financial conditions | 0 | 15 | 10 | 2 | evidence-bearing; machine-record URL |
| [ILOSTAT](https://ilostat.ilo.org/) | work, wages, informal activity, migration, and labor standards | 2 | 15 | 3 | 0 | evidence-bearing |
| [International Labour Organization algorithmic management research](https://www.ilo.org/publications/algorithmic-management-practices-regular-workplaces-case-studies-logistics) | work organization, job quality, industrial relations, and worker-risk evidence | 4 | 81 | 23 | 0 | evidence-bearing |
| [ILO Global case studies of social dialogue on AI and algorithmic management](https://www.ilo.org/publications/global-case-studies-social-dialogue-ai-and-algorithmic-management) | worker-representative and social-dialogue evidence on workplace AI decisions | 4 | 81 | 23 | 1 | evidence-bearing; machine-record URL |
| [WageIndicator worker-rights and collective-agreement archive](https://wageindicator.org/) | comparative worker-rights, collective-agreement, and workplace-governance text archive | 1 | 15 | 9 | 0 | evidence-bearing |
| [European Commission Future of Work](https://employment-social-affairs.ec.europa.eu/policies-and-activities/rights-work/future-work_en) | official policy and rights evidence on algorithmic management, platform work, and worker protection | 0 | 6 | 4 | 0 | evidence-bearing |
| [European Commission JRC AIM-WORK survey](https://joint-research-centre.ec.europa.eu/projects-and-activities/employment/algorithmic-management-and-digital-monitoring-work_en) | EU-wide worker evidence on AI use, digital monitoring, algorithmic management, autonomy, and stress | 1 | 15 | 7 | 0 | evidence-bearing |
| [Federal Reserve Economic Data](https://fred.stlouisfed.org/) | high-frequency US economic series and historical revisions | 1 | 11 | 5 | 4 | evidence-bearing; machine-record URL |
| [UNDP Human Development Reports Data Center](https://hdr.undp.org/data-center) | human development, inequality, gender, and lived conditions | 0 | 32 | 7 | 2 | evidence-bearing; machine-record URL |
| [Stockholm International Peace Research Institute](https://www.sipri.org/databases) | arms transfers, military spending, arms industry, and peace operations | 1 | 27 | 11 | 3 | evidence-bearing; machine-record URL |
| [Chatham House](https://www.chathamhouse.org/topics) | geopolitical context, institutions, security, society, and resource conflict | 0 | 2 | 2 | 0 | evidence-bearing |
| [Carnegie Endowment for International Peace](https://carnegieendowment.org/research/) | country, regional, technology, and international-order analysis | 0 | 1 | 1 | 0 | evidence-bearing |
| [IMF publications by Manmohan Singh](https://www.imf.org/en/publications/publications-by-author?author=Manmohan%20Singh&name=Manmohan%20Singh) | author-level work on money, finance, crises, and macro policy | 1 | 69 | 31 | 0 | evidence-bearing |
| [Bank for International Settlements Papers](https://www.bis.org/publications/bis-paper) | central-bank, banking, payments, monetary, and financial-stability research | 1 | 26 | 18 | 0 | evidence-bearing |
| [US Bureau of Economic Analysis Learning Center](https://www.bea.gov/resources/learning-center) | definitions and methods for national accounts and economic measures | 5 | 87 | 39 | 2 | evidence-bearing; machine-record URL |
| [International Energy Agency Reports](https://www.iea.org/analysis?type=report) | energy systems, transition, supply security, technology, and geopolitics | 2 | 40 | 15 | 0 | evidence-bearing |
| [Office of Financial Research](https://www.financialresearch.gov/) | financial-system structure, stress, market plumbing, and systemic risk | 1 | 39 | 20 | 17 | evidence-bearing; machine-record URL |
| [World Bank Research](https://www.worldbank.org/en/research) | development research, poverty, institutions, growth, climate, and country change | 4 | 149 | 51 | 1 | evidence-bearing; machine-record URL |
| [World Bank Enterprise Surveys](https://www.enterprisesurveys.org/en/data) | firm-level business environment, establishment capacity, finance, infrastructure, management, and performance evidence | 1 | 26 | 8 | 3 | evidence-bearing; machine-record URL |
| [Federal Reserve Survey of Household Economics and Decisionmaking](https://www.federalreserve.gov/consumerscommunities/shed.htm) | US household financial well-being, hardship, credit, housing, and reported economic experience | 25 | 333 | 134 | 4 | evidence-bearing; machine-record URL |
| [U.S. Census Bureau Survey of Income and Program Participation](https://www.census.gov/programs-surveys/sipp.html) | US monthly household and person resources, work, program participation, health, food security, and care constraints | 31 | 1055 | 440 | 12 | evidence-bearing; machine-record URL |
| [Federal Reserve Bank of New York Economic Heterogeneity Indicators](https://www.newyorkfed.org/research/economic-heterogeneity-indicators) | demographic, geographic, and business-size heterogeneity in inflation, earnings, employment, consumer spending, wealth, and small-business conditions | 2 | 60 | 30 | 5 | evidence-bearing; machine-record URL |
| [Consumer Financial Protection Bureau consumer finance research](https://www.consumerfinance.gov/data-research/) | US consumer credit markets, complaints, fees, enforcement, and household financial protection | 20 | 236 | 90 | 64 | evidence-bearing; machine-record URL |
| [CFPB Consumer Complaint Database API documentation](https://cfpb.github.io/api/ccdb/api.html) | machine-access contract for CFPB complaint records, fields, filters, pagination, and public retrieval | 1 | 19 | 13 | 0 | evidence-bearing |
| [US Bureau of Labor Statistics consumer and household data](https://www.bls.gov/) | US prices, spending, income, employment, and household economic measures | 22 | 299 | 103 | 84 | evidence-bearing; machine-record URL |
| [US Census Bureau household and economic data](https://www.census.gov/data.html) | US household, demographic, income, housing, business, and place-level evidence | 31 | 1055 | 440 | 0 | evidence-bearing |
| [Harvard Business School Working Knowledge consumer and finance research](https://www.library.hbs.edu/working-knowledge) | US consumer behavior, pricing, payments, finance, and firm-strategy topic discovery | 51 | 222 | 72 | 4 | evidence-bearing; machine-record URL |
| [NBER household finance and consumer behavior papers](https://www.nber.org/papers) | US household debt, financial stress, credit, consumption, labor, and macro transmission research | 152 | 1326 | 522 | 288 | evidence-bearing; machine-record URL |
| [American National Election Studies](https://electionstudies.org/) | US political attitudes, identity, trust, economic judgment, participation, and vote reports | 0 | 18 | 9 | 1 | evidence-bearing; machine-record URL |
| [Cooperative Election Study](https://cces.gov.harvard.edu/) | large-sample US political, demographic, material-position, trust, and civic-action comparisons | 0 | 7 | 7 | 2 | evidence-bearing; machine-record URL |
| [BLS American Time Use Survey](https://www.bls.gov/tus/) | US paid work, care, household labor, travel, rest, and social-time allocation | 22 | 299 | 103 | 25 | evidence-bearing; machine-record URL |
| [Medical Expenditure Panel Survey](https://meps.ahrq.gov/mepsweb/) | US health conditions, care use, medical spending, insurance, employment, and household burden | 1 | 152 | 46 | 84 | evidence-bearing; machine-record URL |
| [USDA Economic Research Service Food Security Data](https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-us/) | US household and child food security, hunger, shielding, and assistance context | 4 | 54 | 28 | 0 | evidence-bearing |
| [HRSA Health Professional Shortage Areas](https://data.hrsa.gov/topics/health-workforce/shortage-areas) | US place-level provider-shortage and health-capacity context | 0 | 36 | 19 | 0 | evidence-bearing |
| [CDC PLACES: Local Data for Better Health](https://www.cdc.gov/places/) | US county, place, tract, and ZCTA modeled health, preventive-care, and health-related social-needs context | 2 | 43 | 24 | 4 | evidence-bearing; machine-record URL |
| [FEMA National Flood Insurance Program](https://www.fema.gov/flood-insurance) | US hazard exposure, flood insurance, claims, mitigation, and place-risk context | 0 | 4 | 3 | 0 | evidence-bearing |
| [American Community Survey](https://www.census.gov/programs-surveys/acs) | US place-level population, housing, income, migration, language, commuting, and inequality context | 31 | 1055 | 440 | 2 | evidence-bearing; machine-record URL |
| [US Energy Information Administration](https://www.eia.gov/) | US energy prices, consumption, insecurity, electricity systems, and infrastructure context | 21 | 67 | 27 | 15 | evidence-bearing; machine-record URL |
| [US Department of Energy](https://www.energy.gov/) | US energy policy, affordability tools, infrastructure, technology, and public investment context | 18 | 69 | 35 | 14 | evidence-bearing; machine-record URL |
| [US Federal Trade Commission](https://www.ftc.gov/) | US consumer protection, competition, privacy, fraud, platform, and enforcement evidence | 31 | 285 | 99 | 90 | evidence-bearing; machine-record URL |
| [US Department of Health and Human Services](https://www.hhs.gov/) | US health, care, public benefit, medical access, and program administration evidence | 8 | 42 | 18 | 0 | evidence-bearing |
| [Centers for Medicare & Medicaid Services](https://www.cms.gov/data-research) | US health coverage, claims, providers, spending, quality, and public-program evidence | 1 | 13 | 6 | 4 | evidence-bearing; machine-record URL |
| [US Small Business Administration](https://www.sba.gov/) | US small-business programs, lending, disaster support, procurement, and firm access context | 2 | 9 | 7 | 1 | evidence-bearing; machine-record URL |
| [US Department of the Treasury](https://home.treasury.gov/) | US financial policy, household finance, insurance, public spending, and fiscal context | 2 | 21 | 12 | 10 | evidence-bearing; machine-record URL |
| [US Government Accountability Office](https://www.gao.gov/) | US program evaluation, oversight, implementation, procurement, household, and institutional-capacity evidence | 23 | 558 | 269 | 229 | evidence-bearing; machine-record URL |
| [General Social Survey / NORC](https://gss.norc.org/) | US repeated cross-sectional evidence on social attitudes, trust, finance, institutions, and lived conditions | 0 | 28 | 6 | 18 | evidence-bearing; machine-record URL |
| [National Household Travel Survey](https://nhts.ornl.gov/) | US household travel, vehicle access, mobility, work, care, and place-connection evidence | 0 | 23 | 10 | 11 | evidence-bearing; machine-record URL |
| [US Consumer Product Safety Commission](https://www.cpsc.gov/) | US consumer-product hazards, recalls, injuries, safety standards, and enforcement evidence | 5 | 30 | 10 | 8 | evidence-bearing; machine-record URL |
| [US Environmental Protection Agency](https://www.epa.gov/) | US environmental exposure, regulation, emissions, waste, household risk, and place-capacity evidence | 2 | 9 | 6 | 2 | evidence-bearing; machine-record URL |
| [USASpending.gov](https://www.usaspending.gov/) | US federal awards, procurement, grants, recipients, places, and public-resource routing evidence | 0 | 25 | 14 | 0 | evidence-bearing |
| [US Securities and Exchange Commission](https://www.sec.gov/) | US public-company filings, risk disclosures, capital allocation, ownership, and firm-governance evidence | 1 | 13 | 11 | 10 | evidence-bearing; machine-record URL |
| [Georgetown Center for Retirement Initiatives](https://cri.georgetown.edu/) | retirement savings access, state auto-IRA implementation, participation, and household-balance-sheet evidence | 0 | 16 | 7 | 7 | evidence-bearing; machine-record URL |
| [Panel Study of Income Dynamics](https://psidonline.isr.umich.edu/) | US longitudinal household and individual evidence on income, wealth, employment, family, health, and mobility | 0 | 24 | 7 | 2 | evidence-bearing; machine-record URL |
| [PSID packaged-data delivery route](https://simba.isr.umich.edu/Zips/ZipMain.aspx) | authenticated PSID packaged files, wave archives, and reproducible longitudinal-data acquisition | 0 | 20 | 7 | 1 | evidence-bearing; machine-record URL |
| [European Commission Joint Research Centre](https://joint-research-centre.ec.europa.eu/) | comparative European evidence on algorithmic management, technology, labor, institutions, and public capacity | 1 | 15 | 7 | 0 | evidence-bearing |
| [European Commission JRC Publications Repository](https://publications.jrc.ec.europa.eu/repository/) | primary publication and technical-report delivery route for JRC comparative research | 2 | 29 | 12 | 1 | evidence-bearing; machine-record URL |
| [Chicago Council on Global Affairs](https://globalaffairs.org/) | US and comparative public-opinion and geopolitical context on migration, foreign policy, security, and international engagement | 0 | 11 | 5 | 8 | evidence-bearing; machine-record URL |
| [US Department of Defense](https://www.defense.gov/) | US defense policy, force posture, procurement, industrial-base, alliance, and operational-capacity records | 0 | 3 | 3 | 2 | evidence-bearing; machine-record URL |
| [Defense Security Cooperation Agency](https://www.dsca.mil/) | US foreign military sales, security cooperation notifications, partner procurement, and defense-transfer records | 0 | 5 | 5 | 2 | evidence-bearing; machine-record URL |
| [Polish government and national-security institutions](https://www.gov.pl/) | Polish defense, security, industrial, infrastructure, and alliance-policy records for geopolitical case comparisons | 0 | 101 | 33 | 27 | evidence-bearing; machine-record URL |
| [International Finance Corporation](https://www.ifc.org/) | development-finance, private-sector investment, infrastructure, technology, and cross-country capability evidence | 1 | 15 | 9 | 1 | evidence-bearing; machine-record URL |
| [Defense Visual Information Distribution Service](https://www.dvidshub.net/) | public US defense visual and operational event records used for milestone and activity context | 0 | 1 | 1 | 1 | evidence-bearing; machine-record URL |
| [Virginia State Corporation Commission](https://www.scc.virginia.gov/) | Virginia utility, rate-case, reliability, large-load, and public-service governance records | 0 | 46 | 20 | 19 | evidence-bearing; machine-record URL |
| [Prince William County, Virginia](https://www.pwcva.gov/) | local fiscal, land-use, data-center, revenue, tax, and public-capacity records | 0 | 19 | 5 | 14 | evidence-bearing; machine-record URL |
| [California Department of Insurance](https://www.insurance.ca.gov/) | California insurance regulation, wildfire risk, market availability, FAIR Plan, and consumer protection records | 0 | 25 | 12 | 16 | evidence-bearing; machine-record URL |
| [Lawrence Berkeley National Laboratory energy analysis](https://eta-publications.lbl.gov/) | US energy-system, data-center load, efficiency, infrastructure, and technology-demand analysis | 0 | 12 | 8 | 6 | evidence-bearing; machine-record URL |
| [Berkeley Social Sciences Data Laboratory](https://sda.berkeley.edu/) | public-use survey tabulation and microdata interface for social attitudes, political behavior, and subgroup comparisons | 0 | 34 | 12 | 20 | evidence-bearing; machine-record URL |
| [Inter-university Consortium for Political and Social Research](https://www.icpsr.umich.edu/) | archived social-science datasets, codebooks, public-use files, restricted-access routes, and reproducibility materials | 0 | 16 | 5 | 0 | evidence-bearing |
| [Gallup public opinion research](https://gallup.com/) | US and comparative public-opinion, institutional trust, social attitudes, wellbeing, and political-meaning context | 1 | 80 | 34 | 0 | evidence-bearing |
| [O*NET Resource Center](https://www.onetcenter.org/database.html) | US occupation, task, work-activity, skill, and taxonomy metadata for crosswalking labor-market evidence | 0 | 5 | 3 | 0 | evidence-bearing |
| [INFORMS Management Science](https://pubsonline.informs.org/) | peer-reviewed operations, management, technology-adoption, firm, and workforce research | 0 | 4 | 3 | 2 | evidence-bearing; machine-record URL |
| [USDA Food and Nutrition](https://fna.usda.gov/) | US nutrition-assistance program rules, participation, application, recertification, state administration, and access records | 0 | 27 | 10 | 0 | evidence-bearing |
| [Defense Logistics Agency CAGE search](https://cage.dla.mil/) | US defense legal-entity, facility, CAGE, UEI, address, and parent-link identity records for procurement joins | 0 | 4 | 3 | 3 | evidence-bearing; machine-record URL |
| [Authority for the Digitalization of Romania](https://www.adr.gov.ro/) | Romanian public digital-infrastructure, cloud, interoperability, procurement, and implementation records | 1 | 17 | 9 | 2 | evidence-bearing; machine-record URL |
| [Lockheed Martin official materials](https://www.lockheedmartin.com/) | official defense-company production, integration, industrial-capacity, and program-milestone records | 0 | 8 | 4 | 2 | evidence-bearing; machine-record URL |
| [BAE Systems official materials](https://www.baesystems.com/) | defense-company facility, certification, ownership, production, and capability context | 0 | 4 | 3 | 2 | evidence-bearing; machine-record URL |
| [General Dynamics Ordnance and Tactical Systems](https://www.gd-ots.com/) | defense-company facility, manufacturing, and technical-capability context | 0 | 2 | 2 | 1 | evidence-bearing; machine-record URL |
| [Polish Supreme Audit Office (NIK)](https://www.nik.gov.pl/) | Polish public audit evidence on defense procurement, FMS implementation, accounting controls, and state capacity | 0 | 6 | 4 | 2 | evidence-bearing; machine-record URL |
| [Yondr Group](https://www.yondrgroup.com/) | data-center ownership, construction, capacity, transfer, and infrastructure-realization records | 1 | 11 | 6 | 0 | evidence-bearing |
| [Vantage Data Centers](https://vantage-dc.com/) | data-center acquisition, ownership, investment, and infrastructure-capacity records | 1 | 8 | 5 | 0 | evidence-bearing |
| [SAG-AFTRA contracts and agreements](https://www.sagaftra.org/) | US worker representation, entertainment labor agreements, digital-replica rules, and negotiated technology governance | 2 | 14 | 4 | 0 | evidence-bearing |
| [Deutsche Telekom official materials](https://www.telekom.com/) | firm AI governance, digital ethics, workforce, and technology-implementation records | 2 | 13 | 4 | 0 | evidence-bearing |
| [ver.di public union materials](https://www.verdi.de/) | German worker-representation, social-dialogue, and algorithmic-management response evidence | 1 | 9 | 4 | 0 | evidence-bearing |
| [Kenya Law official legal repository](https://new.kenyalaw.org/) | official court decisions and legal records for comparative platform, content-moderation, labor, and institutional-power cases | 2 | 23 | 5 | 0 | evidence-bearing |
| [Georgia Public Service Commission](https://psc.ga.gov/) | Georgia utility rate, large-load, reliability, and public-service governance records | 0 | 12 | 4 | 5 | evidence-bearing; machine-record URL |
| [Dominion Energy official materials](https://www.dominionenergy.com/) | utility infrastructure, large-load interconnection, transmission, and implementation context | 0 | 14 | 10 | 2 | evidence-bearing; machine-record URL |
| [Congressional Budget Office](https://www.cbo.gov/) | federal budget, policy-cost, household-finance, housing, and distributional analysis | 0 | 9 | 6 | 7 | evidence-bearing; machine-record URL |
| [Federal Deposit Insurance Corporation](https://www.fdic.gov/) | banking, depositors, financial access, failures, and consumer-finance institutional evidence | 0 | 11 | 5 | 5 | evidence-bearing; machine-record URL |
| [Federal Housing Finance Agency](https://www.fhfa.gov/) | housing prices, mortgage finance, affordability, and housing-market regulation | 0 | 9 | 6 | 5 | evidence-bearing; machine-record URL |
| [Federal Highway Administration and National Household Travel Survey](https://www.fhwa.dot.gov/policyinformation/nhts.cfm) | household travel, mobility, transportation burden, and time-use context | 1 | 1 | 1 | 0 | evidence-bearing |
| [ENERGY STAR](https://www.energystar.gov/) | energy efficiency, consumer products, buildings, and utility-investment evidence | 1 | 9 | 4 | 4 | evidence-bearing; machine-record URL |
| [Pew Charitable Trusts](https://www.pew.org/) | policy research, state governance, public finance, and institutional trust context | 0 | 11 | 7 | 6 | evidence-bearing; machine-record URL |
| [New York State Department of Financial Services](https://www.dfs.ny.gov/) | state financial regulation, insurance, consumer protection, and enforcement records | 1 | 10 | 5 | 4 | evidence-bearing; machine-record URL |
| [Illinois Department of Financial and Professional Regulation](https://idfpr.illinois.gov/) | state financial, banking, and professional-regulatory records | 1 | 3 | 3 | 0 | evidence-bearing |
| [Texas Legislature Online statutes and codes](https://statutes.capitol.texas.gov/) | state statutory and legal text for consumer, housing, property, and institutional rules | 1 | 4 | 4 | 0 | evidence-bearing |
| [Texas Secretary of State and Texas Register](https://www.sos.state.tx.us/) | state administrative rules, proposed rules, and regulatory process records | 0 | 2 | 2 | 1 | evidence-bearing; machine-record URL |
| [Lawrence Berkeley National Laboratory Energy Analysis](https://energyanalysis.lbl.gov/) | energy-system, data-center load, efficiency, and infrastructure analysis | 0 | 1 | 1 | 0 | evidence-bearing |

## Reverse audit: observed domains outside the registry

This is a review queue, not an automatic registration list. It excludes
subdomains covered by a registered parent (for example `api.bls.gov` under
BLS). Remaining domains may be mirrors, delivery hosts, partner sites, or
one-off citations. Promote a domain only when it represents a durable source
family that will be acquired, compared, or maintained over time.

- Observed domains outside registered families: **274**
- Review queue shown: **40** highest-frequency domains

| Domain | References | Example evidence files |
|---|---:|---|
| `doi.org` | 232 | `analysis/projects/us-declining-occupations-career-outcomes/findings/us-nber-declining-occupations-career-earnings-2000-2020-001.md`; `analysis/projects/us-immigration-local-demand/migration-place-local-trust-action-joint-axes-v1.md`; `analysis/projects/us-immigration-local-demand/migration-place-local-trust-action-context-v1.md` |
| `fwc.gov.au` | 155 | `analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md`; `analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md`; `analysis/US-REMEDY-IMPLEMENTATION-RECOVERY-SYNTHESIS_V1.md` |
| `nato.int` | 45 | `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md`; `analysis/us-source-coverage.md` |
| `bjs.ojp.gov` | 33 | `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md` |
| `justice.gov` | 33 | `analysis/projects/us-safety-net-access/findings/us-safety-net-access-016.md`; `analysis/projects/ai-work-control/ier-california-rehire-seniority-backpay-record-v1.md`; `analysis/projects/ai-work-control/elegant-settlement-compliance-follow-up-audit-2026-09-17.md` |
| `unesco.org` | 28 | `analysis/records/comparative-unesco-world-trends-expression-media-information-integrity-2026.json`; `analysis/records/comparative-unesco-world-trends-expression-media-information-integrity-2026.json`; `analysis/records/comparative-unesco-world-trends-expression-media-information-integrity-2026.json` |
| `un.org` | 27 | `analysis/records/comparative-un-beyond-gdp-progress-dashboard-2026.json`; `analysis/records/comparative-un-beyond-gdp-progress-dashboard-2026.json`; `analysis/records/comparative-un-beyond-gdp-progress-dashboard-2026.json` |
| `privacy.ca.gov` | 26 | `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md`; `analysis/us-source-coverage.md`; `analysis/us-source-coverage.md` |
| `mohr.gov.my` | 23 | `analysis/projects/ai-work-control/malaysia-gig-workers-act-algorithmic-remedy-record-v1.md`; `analysis/projects/ai-work-control/malaysia-gig-workers-act-algorithmic-remedy-record-v1.md`; `analysis/projects/ai-work-control/malaysia-gig-workers-act-algorithmic-remedy-record-v1.md` |
| `uasdata.usc.edu` | 22 | `analysis/projects/us-household-constraint-cascade/next-acquisition-decision-v1.md`; `analysis/projects/us-household-constraint-cascade/next-acquisition-decision-v1.md`; `analysis/projects/us-health-cost-household-choice/uas-health-cost-legitimacy-acquisition-audit-v1.md` |
| `theguarantors.com` | 21 | `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md` |
| `huduser.gov` | 20 | `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md` |
| `unctad.org` | 20 | `analysis/records/comparative-unctad-creative-economy-digital-cultural-trade-2024.json`; `analysis/records/comparative-unctad-creative-economy-digital-cultural-trade-2024.json`; `analysis/records/comparative-un-beyond-gdp-progress-dashboard-2026.json` |
| `desapublications.un.org` | 19 | `analysis/records/comparative-un-women-desa-gender-snapshot-2025-poverty-conflict-digital-power.json`; `analysis/records/comparative-un-women-desa-gender-snapshot-2025-poverty-conflict-digital-power.json`; `analysis/records/comparative-un-desa-generational-economy-2026-transfers-care-fiscal-capacity.json` |
| `academic.oup.com` | 17 | `analysis/us-theme-atlas.md`; `analysis/US-BROAD-EXTERNAL-DATA-FIRST-PASS_2026-09-25.md`; `analysis/US-BROAD-EXTERNAL-DATA-FIRST-PASS_2026-09-25.md` |
| `bis.gov` | 17 | `analysis/US-BROAD-GEOPOLITICAL-STATE-SUBTHEME-SYNTHESIS_V1.md`; `analysis/records/us-gao-advanced-semiconductor-export-control-compliance-2022-2024.json`; `analysis/records/us-bis-bosch-foreign-produced-mems-huawei-settlement-2026.json` |
| `doee.dc.gov` | 15 | `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md`; `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md`; `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md` |
| `weforum.org` | 15 | `analysis/records/comparative-un-women-desa-gender-snapshot-2025-poverty-conflict-digital-power.json`; `analysis/records/comparative-wef-global-cybersecurity-outlook-ai-geopolitics-2026.json`; `analysis/records/comparative-wef-global-cybersecurity-outlook-ai-geopolitics-2026.json` |
| `apnorc.org` | 14 | `analysis/US-BROAD-EXTERNAL-DATA-FIRST-PASS_2026-09-25.md`; `analysis/projects/us-cost-trust-politics/findings/us-cost-trust-politics-062.md`; `analysis/projects/us-cost-trust-politics/findings/us-cost-trust-politics-060.md` |
| `fairwork.gov.au` | 14 | `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md`; `analysis/ACTIVE-GOAL-COMPLETION-AUDIT_2026-09-25.md`; `analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md` |
| `btq-kassel.de` | 13 | `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md`; `analysis/us-theme-atlas.md` |
| `fao.org` | 13 | `analysis/records/comparative-fao-healthy-diet-cost-food-security-2026.json`; `analysis/records/comparative-fao-healthy-diet-cost-food-security-2026.json`; `analysis/records/comparative-fao-healthy-diet-cost-food-security-2026.json` |
| `unstats.un.org` | 13 | `analysis/records/comparative-un-women-desa-gender-snapshot-2025-poverty-conflict-digital-power.json`; `analysis/records/comparative-un-habitat-world-cities-2026-housing-displacement-climate-delivery.json`; `analysis/records/comparative-un-sdg16-2026-institutions-justice-information-voice.json` |
| `nyc.gov` | 12 | `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md`; `analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md`; `analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md` |
| `undp.org` | 12 | `analysis/records/comparative-un-sdg16-2026-institutions-justice-information-voice.json`; `analysis/records/comparative-undp-democracy-development-lac-2026-institutions-trust-pressure.json`; `analysis/records/comparative-undp-democracy-development-lac-2026-institutions-trust-pressure.json` |
| `who.int` | 12 | `analysis/records/comparative-who-universal-health-coverage-financial-protection-2025.json`; `analysis/records/comparative-who-universal-health-coverage-financial-protection-2025.json`; `analysis/records/comparative-who-social-connection-loneliness-2025.json` |
| `cambridge.org` | 11 | `analysis/us-theme-atlas.md`; `analysis/us-source-coverage.md`; `analysis/US-BROAD-EXTERNAL-DATA-FIRST-PASS_2026-09-25.md` |
| `govinfo.gov` | 11 | `analysis/US-BROAD-GEOPOLITICAL-SOURCE-LED-SUBTHEME-MAP_V1.md`; `analysis/projects/us-safety-net-access/findings/us-safety-net-access-016.md`; `analysis/projects/us-safety-net-access/findings/us-safety-net-access-016.md` |
| `kam.lt` | 11 | `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md`; `analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md`; `analysis/projects/ai-work-control/findings/ai-work-control-130.md` |
| `ofcom.org.uk` | 11 | `analysis/records/comparative-ofcom-adults-media-use-attention-literacy-2026.json`; `analysis/records/comparative-ofcom-adults-media-use-attention-literacy-2026.json`; `analysis/records/comparative-ofcom-adults-media-use-attention-literacy-2026.json` |
| `reutersinstitute.politics.ox.ac.uk` | 11 | `analysis/records/comparative-reuters-digital-news-report-2026-platform-attention-trust-action.json`; `analysis/records/comparative-reuters-digital-news-report-2026-platform-attention-trust-action.json`; `analysis/records/comparative-reuters-digital-news-report-2026-platform-attention-trust-action.json` |
| `wto.org` | 11 | `analysis/records/comparative-wto-world-trade-report-2026-fragmentation-flexibility-ai-services.json`; `analysis/records/comparative-wto-world-trade-report-2026-fragmentation-flexibility-ai-services.json`; `analysis/records/comparative-wto-world-trade-report-2026-fragmentation-flexibility-ai-services.json` |
| `arts.gov` | 10 | `analysis/us-source-coverage.md`; `analysis/projects/us-cost-trust-politics/source-search-2026-09-22-arts-social-connectedness.md`; `analysis/projects/us-cost-trust-politics/findings/us-cost-trust-politics-066.md` |
| `circle.tufts.edu` | 10 | `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md`; `analysis/US-BROAD-EVIDENCE-MATRIX_V1.md`; `analysis/projects/us-cost-trust-politics/findings/us-cost-trust-politics-058.md` |
| `dol.gov` | 10 | `analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md`; `analysis/US-BROAD-NEXT-PASS-QUEUE_V1.md`; `analysis/US-BROAD-EVIDENCE-MATRIX_V1.md` |
| `freedomhouse.org` | 10 | `analysis/records/comparative-freedom-house-freedom-world-2026-political-rights-civil-liberties.json`; `analysis/records/comparative-freedom-house-freedom-world-2026-political-rights-civil-liberties.json`; `analysis/records/comparative-freedom-house-freedom-world-2026-political-rights-civil-liberties.json` |
| `idea.int` | 10 | `analysis/records/comparative-idea-global-state-democracy-2026-conflict-rights-rule-of-law.json`; `analysis/records/comparative-idea-global-state-democracy-2026-conflict-rights-rule-of-law.json`; `analysis/records/comparative-idea-global-state-democracy-2026-conflict-rights-rule-of-law.json` |
| `nisrf.nato.int` | 10 | `analysis/projects/ai-work-control/poland-eastern-sentry-persistence-legitimacy-audit-v1.md`; `analysis/projects/ai-work-control/findings/ai-work-control-135.md`; `analysis/records/us-nato-nisrf-agile-combat-employment-2026.json` |
| `static.cninfo.com.cn` | 10 | `analysis/records/us-china-hygon-dcu-realized-growth-deployment-2026.json`; `analysis/records/us-china-hunan-compute-platform-hygon-dcu-resource-integration-2026.json`; `analysis/records/us-china-hygon-dcu-large-model-cluster-realization-2026.json` |
| `transportation.gov` | 10 | `analysis/US-BROAD-INTERESTING-FINDINGS_V1.md`; `analysis/US-BROAD-EVIDENCE-MATRIX_V1.md`; `analysis/projects/us-dot-smart-transportation-demonstration/findings/us-dot-smart-transportation-demonstration-002.md` |

## Reverse-audit decisions

The table below records the current disposition of every observed outside
domain. A non-registration decision is deliberate: the domain may still
be useful evidence, but it is not promoted to a maintained source family
without a recurring acquisition need and source-specific metadata.

| Domain | Classification | Current decision |
|---|---|---|
| `doi.org` | citation/index host | Do not register; retain DOI as a source identifier and preserve the underlying publisher or institution separately. |
| `fwc.gov.au` | official labor tribunal | Retain as an official comparative tribunal source; promote as a maintained family only when recurring decisions are actively acquired and versioned. |
| `nato.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `bjs.ojp.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `justice.gov` | official US legal/enforcement source | Retain as a public-record comparator; preserve the responsible DOJ component and case or settlement identifier for each claim. |
| `unesco.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `un.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `privacy.ca.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `mohr.gov.my` | official Malaysian labor authority | Retain as a comparative public-record source; preserve the responsible department, instrument, date, and implementation status for each claim. |
| `uasdata.usc.edu` | official UAS data/documentation host | Retain as the official UAS source family; respondent-file downloads remain registration-gated, and no microdata are promoted without the acquisition manifest plus key, weight, and missingness checks. |
| `theguarantors.com` | commercial case source | Do not register as a recurring family yet; preserve product terms and treat the vendor material as case-specific evidence. |
| `huduser.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unctad.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `desapublications.un.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `academic.oup.com` | academic publisher | Retain the cited paper/publisher route; promote a recurring research family only when a sustained acquisition lane exists. |
| `bis.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `doee.dc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `weforum.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `apnorc.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `fairwork.gov.au` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `btq-kassel.de` | case-specific institution | Retain as a cited interview/organization record; promote only if a maintained recurring evidence series is acquired. |
| `fao.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unstats.un.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nyc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `undp.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `who.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `cambridge.org` | academic publisher | Retain the cited paper/publisher route; promote the specific research program only when it becomes a maintained acquisition lane. |
| `govinfo.gov` | official federal publication host | Retain as an official publication route; preserve the issuing agency, document identifier, version, and source context rather than treating the delivery host as the whole evidence family. |
| `kam.lt` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ofcom.org.uk` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `reutersinstitute.politics.ox.ac.uk` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `wto.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `arts.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `circle.tufts.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dol.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `freedomhouse.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `idea.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nisrf.nato.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `static.cninfo.com.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `transportation.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `worldhappiness.report` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `cppa.ca.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `eur-lex.europa.eu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `hrs.isr.umich.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `pmc.ncbi.nlm.nih.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `support.sayrhino.com` | commercial support host | Do not register; support content is a product-route citation, not an independent recurring evidence family. |
| `transit.dot.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unhcr.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ustr.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `cfpnet.com` | case-specific market source | Retain the California FAIR Plan citation, but use California DOI and official plan records as the durable source family. |
| `eac.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `edocket.dcpsc.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `eeoc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `esafety.gov.au` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `fec.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ferc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `jefnations.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `legistar.council.nyc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nlrb.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ofac.treasury.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unicef.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `english.mofcom.gov.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ico.org.uk` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ilostat.github.io` | official delivery/documentation host | Do not register separately; keep ILOSTAT as the source family and preserve this route as a delivery/access artifact. |
| `kff.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nces.ed.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nypa.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `saffm.hq.af.mil` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unep.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `act.nato.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `afajof.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `benklopack.github.io` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `cage.report` | delivery/lookup host | Do not register; use official DLA CAGE records as the authoritative identity source. |
| `congress.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dms-uat.fwc.gov.au` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `docs.fcc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `docs.google.com` | delivery/repository host | Do not register; preserve the underlying NBER, institution, or document identity and access route. |
| `help.theguarantors.com` | commercial support host | Do not register; treat as product documentation under the commercial case source. |
| `ipu.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nist.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nyiso.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `pjm.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `sam.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `topcat.aeaweb.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `trustforciviclife.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unhabitat.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `bundeswehr.de` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `caloes.ca.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `data.unodc.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `data.unwomen.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `eddataexpress.ed.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `flipsnack.com` | publication delivery host | Do not register; preserve the county report and issuer as the source family. |
| `freemalaysiatoday.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `github.com` | code/reproducibility host | Do not register; preserve repository, release, commit, and upstream institution separately. |
| `gm.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `gov.uk` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `home4.nyc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `hpwohio.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `hud.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `itu.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `journals.sagepub.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `media.bis.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nasbo.org` | state-fiscal policy source | Retain as a policy-research comparator for state fiscal capacity; promote it to a maintained source family only when recurring NASBO vintages are acquired and compared. |
| `nrdc-ita.nato.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nyserda.ny.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `production.humanresourcesonline.net` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `pubs.usgs.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `rules.cityofnewyork.us` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `services.arcgis.com` | data delivery host | Do not register; preserve FEMA or agency ownership and the layer/service query separately. |
| `unodc.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `wipo.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `bfi.uchicago.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `blog.google` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `business.columbia.edu` | academic case citation | Retain as a study or institutional page citation; it is not yet a recurring maintained source family in this atlas. |
| `c2h.fcc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `cbos.pl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dole.gov.ph` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `eeas.europa.eu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `gxt.hunan.gov.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `indium.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `internetconsultatie.nl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `kariuomene.lt` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `leapeasy.com` | commercial case source | Do not register as a recurring family yet; preserve product terms and use official state/regulatory records for durable claims. |
| `nature.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `news.caloes.ca.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nmlegis.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nyisoviewer.etariff.biz` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `publications.iom.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `sayrhino.com` | commercial case source | Do not register as a recurring family yet; preserve product terms and use official state/regulatory records for durable claims. |
| `sites.google.com` | delivery/repository host | Do not register; preserve the NBER paper, author, institution, or source record separately. |
| `support.leapeasy.com` | commercial support host | Do not register; support content is a product-route citation, not an independent recurring evidence family. |
| `uitspraken.rechtspraak.nl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `aeaweb.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `anduril.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `civicus.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `commerce.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `comptroller.war.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `corporate.walmart.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dropbox.com` | file delivery host | Do not register; preserve the NBER or author-provided artifact, version, and hash. |
| `forsvaret.no` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ftrebbi.com` | author/project host | Retain as a paper or author-data route; use the NBER record as the durable research family. |
| `ils.dole.gov.ph` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `imaginingthedigitalfuture.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `investors.capgemini.com` | company disclosure host | Do not register separately; preserve Capgemini as the company source family and the report/version as the evidence item. |
| `jtksm.mohr.gov.my` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `namratakala.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `policy.trade.ec.europa.eu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `povertyactionlab.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `sites.temple.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `social.desa.un.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `subscriptionmembershipsettlement.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `uscc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `villageofskaneateles.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `w.mesko.com.pl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `wetgevingskalender.overheid.nl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `wfp.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `a856-cityrecord.nyc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `americansurveycenter.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `americorps.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `boi.org.il` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `bwc.dole.gov.ph` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `cy.ico.org.uk` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `data.unicef.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dataclouds.cninfo.com.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dataverse.harvard.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `democracyinstitute.osu.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `docketnexus.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `docs.iza.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `docs.justia.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `documents.dps.ny.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dosh.gov.my` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dps.ny.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `dserver.bundestag.de` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `eaduan-gig.mohr.gov.my` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `econbiz.de` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `economics.princeton.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `exportcontrol.mofcom.gov.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `fairwork.oii.ox.ac.uk` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `federalregister.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `fma.no` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `grab.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `hogeraad.nl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `inl.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `insidelines.pjm.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `iza.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `law.stanford.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `link.springer.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `mesko.com.pl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `mfa.gov.ua` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `misslobang.my` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `myemail.constantcontact.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `nielseniq.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `pierrebodere.github.io` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `polisci.osu.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `prri.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `publications.civicus.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `rijksoverheid.nl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `saferproducts.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `samr.gov.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ssrn.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `tse-fr.eu` | academic/case citation | Retain the cited study route; it is not currently a maintained recurring family in the atlas. |
| `tsmc.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `uasvis.usc.edu` | official UAS visualization host | Retain as a public metadata and aggregate-explorer route; do not treat the visualization as a substitute for registration-gated respondent microdata or as a medical-expense-specific estimate. |
| `wedocs.unep.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `zms.bundeswehr.de` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `36kr.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `a860-openrecords.nyc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `acquisition.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `apnews.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `apps.who.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `bm.soyacincau.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `bpb-us-e1.wpmucdn.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `brasil.un.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `budget.lis.virginia.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `cbp.gov` | federal delivery and border source | Do not register separately for the current CPSC case; preserve CBP as the official import/border comparator and promote it only if import surveillance becomes a maintained acquisition lane. |
| `data.ipu.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `denkfabrik-bmas.de` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `digitalchina.gov.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `docs.house.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ec.europa.eu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ed.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `elon.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `europarl.europa.eu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `fao.sitefinity.cloud` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `fbi.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `files.worldhappiness.report` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `finance.sina.com.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `finlex.fi` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `government.se` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `hbs.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `howhousingmatters.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `hrsdata.isr.umich.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `icpsr.github.io` | data delivery/documentation host | Do not register separately; preserve ICPSR or the originating survey as the durable source family. |
| `investmentpolicy.unctad.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `investor.nvidia.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `isps.yale.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `journals.plos.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `journals.uchicago.edu` | academic publisher | Retain the cited paper/publisher route; it is not currently a maintained recurring family in the atlas. |
| `jstor.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `jwc.nato.int` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `kho.fi` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `kimi.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `knowledge.unwomen.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `kpms.mesko.com.pl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `legifrance.gouv.fr` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `m.skhynix.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `media.terytorialsi.wp.mil.pl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `mlvt.gov.kh` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `mofcom.gov.cn` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `monitor.civicus.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `myhealthrecord.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `ncdor.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `oaic.gov.au` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `onlinelibrary.wiley.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `open.gsa.gov` | government API delivery host | Do not register separately; preserve GSA/USAspending as the durable source family and the endpoint as the query route. |
| `openknowledge.fao.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `orbilu.uni.lu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `osf.io` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `population.un.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `public-inspection.federalregister.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `pubmed.ncbi.nlm.nih.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `rechtspraak.nl` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `rge.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `samsung.com` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `sdgs.un.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `senat.fr` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `stonecenter.gc.cuny.edu` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unesdoc.unesco.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unwater.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `unwomen.org` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `usitc.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `va.gov` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `vero.fi` | unclassified review candidate | Requires manual review before promotion or exclusion. |
| `wojsko-polskie.pl` | unclassified review candidate | Requires manual review before promotion or exclusion. |

## Interpretation rule

A source with no hit is not a failed source; it is an explicit breadth gap
or a source that has not yet been used in the current corpus. A domain hit
may come from a related citation rather than a direct estimate. Promotion
still requires a source record with unit, date, geography, denominator,
method, uncertainty, subgroup, counterexample, and boundary.

Generated by `scripts/audit_source_registry_coverage.py`.
