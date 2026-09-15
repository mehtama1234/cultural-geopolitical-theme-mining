# Source search: AI, work, and control

**Search date:** 2026-09-11  
**Geography:** United States with international comparison cases
**Project:** AI, work, and control  
**Status:** first pass; not exhaustive

## Working question

When firms adopt AI, does the main change come from better tools, tighter measurement, new supervision, or a shift in who owns the work process?

## Search paths

### HBS Working Knowledge

Searches and pages checked:

- Working Knowledge home and Artificial Intelligence collection.
- `AI at work`, `technology adoption`, `employee trust`, `productivity`, `supervision`, `agentic operating model`.
- [From P&G to Microsoft, How Companies Are Speeding AI Adoption](https://www.library.hbs.edu/working-knowledge/from-pg-to-microsoft-how-companies-speed-ai-adoption).

This is a research story and case index, not a causal estimate. It is useful for finding firm practices, responsibility rules, adoption barriers, and linked cases. HBS says the current story draws on cases involving P&G, Microsoft, Whoz, and JPMorgan Chase. The claims about productivity and adoption in those cases must be checked against the underlying case or operating data before being treated as measured results.

### NBER

Search terms:

- `generative AI at work`
- `rapid adoption generative AI`
- `labor market transformation generative AI`
- `what work does generative AI do`
- `firm AI investment organization capital`
- `AI productivity workforce executives`
- `digital surveillance managerial clarity performance`
- `shifting work patterns generative AI`

Initial records:

| ID | Source | Type | Why it is in scope |
|---|---|---|---|
| NBER-W31161 | [Generative AI at Work](https://www.nber.org/papers/w31161) | working paper; published version listed | Firm-level worker productivity and heterogeneity. |
| NBER-W32966 | [The Rapid Adoption of Generative AI](https://www.nber.org/papers/w32966) | working paper | Adoption, assisted hours, and reported time savings in the U.S. |
| NBER-W33777 | [Still Waters, Rapid Currents](https://www.nber.org/papers/w33777) | working paper | Denmark: adoption and task change compared with earnings and hours. |
| NBER-W35677 | [What Work Does Generative AI Do?](https://www.nber.org/papers/w35677) | working paper | Task-level adoption and variation among workers doing similar work. |
| NBER-W34984 | [Artificial Intelligence, Productivity, and the Workforce](https://www.nber.org/papers/w34984) | working paper | Executive reports, firm size, sector differences, and labor reallocation. |
| NBER-W31222 | [Generative AI and Firm Values](https://www.nber.org/papers/w31222) | working paper; revised | Firm exposure, data assets, labor demand, and value. |
| NBER-W33348 | [The Effects of Digital Surveillance and Managerial Clarity on Performance](https://www.nber.org/papers/w33348) | randomized experiment; working paper | Whether surveillance and its explanation change performance. |
| NBER-W33795 | [Shifting Work Patterns with Generative AI](https://www.nber.org/papers/w33795) | field experiment; working paper | Individual access, time use, and task composition across firms. |

### BLS JOLTS

The [BLS Job Openings and Labor Turnover Survey](https://www.bls.gov/jlt/)
and [field definitions](https://www.bls.gov/help/def/jt.htm) provide the
establishment-based context for openings, hires, quits, layoffs, and total
separations. The project now preserves a 2020–2025 seasonally adjusted API
extract and annual derivation in the [JOLTS mobility layer](bls-jolts-national-mobility-layer-v1.md).
This is a labor-market context source; it does not measure worker control,
job quality, or household outcomes.

### ILOSTAT international comparison route

The [ILOSTAT data catalog](https://ilostat.ilo.org/data/), [bulk-download
documentation](https://ilostat.ilo.org/data/bulk/), and [Rilostat workflow
documentation](https://ilostat.github.io/Rilostat/reference/get_ilostat.html)
were checked as the international comparison route for labor-force
participation, unemployment, earnings, working poverty, and youth exclusion.
The catalog and documented indicator families are in scope, but the current
API metadata and indicator delivery paths returned zero-byte payloads. No
ILOSTAT estimate is included in the atlas. The [route access
audit](ilostat-access-audit-2026-09-15.md) and [2026-09-15 recheck
record](data/ilostat-route-recheck-2026-09-15.json) preserve the exact URLs,
status codes, content type, byte count, and body hash. A numerical comparison
must wait for a delivered payload with indicator definition, reference area,
frequency, source basis, revision status, and a matched US concept.

## What remains to search

- Read the full papers, appendices, data notes, and later published versions.
- Find HBS faculty papers behind the cases, where available.
- Add worker voice, disability, gender, age, migration, and small-firm evidence.
- Add labor rules, collective bargaining, and workplace monitoring evidence.
- Add annual reports and filings only after the research claims are stable.
- Search non-U.S. evidence beyond Denmark and the U.S.
- Read the full surveillance and field-experiment papers, including disclosures and appendices.
- Add cross-country employer and worker-rights evidence on accountability, privacy, autonomy, and job quality.

## First-pass conclusion

The evidence is already strong enough to open a project, but not to close it. The first working hypothesis is:

> AI may change the structure and control of work before it changes average pay or employment.

This is a hypothesis because the sources measure different units: individual workers, workplaces, firms, and national labor markets. The next pass must test whether those differences explain the apparent disagreement.

## Control-layer result from the second pass

The next layer is not simply “AI increases monitoring.” The first relevant studies point to a conditional mechanism: the meaning and explanation of a control system may affect performance, while individual AI access can save time without changing the mix of tasks. This makes responsibility, review rights, and worker understanding central variables for the next search.

## Accountability search

| ID | Source | Type | Why it is in scope |
|---|---|---|---|
| OECD-AM-2025 | [Algorithmic management in the workplace](https://www.oecd.org/en/publications/algorithmic-management-in-the-workplace_287c13c4-en.html) | employer survey and working paper | More than 6,000 firms in six countries; use, effects, and governance concerns. |
| OECD-WORKER-CONSULTATION-2025 | [Exploring win-win outcomes of algorithmic management](https://www.oecd.org/en/publications/exploring-win-win-outcomes-of-algorithmic-management_84b59397-en.html) | worker-consultation laboratory experiment | Three German manufacturing firms and 16 participants; feature-level negotiation, autonomy disagreement, and expected—not realized—outcomes. |
| ILO-AM-2024 | [Algorithmic management practices in regular workplaces](https://www.ilo.org/publications/algorithmic-management-practices-regular-workplaces-case-studies-logistics) | comparative case study | Logistics and health care in France, Italy, India, and South Africa; job quality and surveillance. |
| CAPGEMINI-AR-2025 | [Capgemini 2025 Integrated Annual Report](https://reports.capgemini.com/2025/en/) | annual report and registration document | AI training, employee data platform, role changes, workforce monitoring, and restructuring. |
| JRC-AIMWORK-2025 | [Algorithmic management and digital monitoring of work](https://joint-research-centre.ec.europa.eu/projects-and-activities/employment/algorithmic-management-and-digital-monitoring-work_en) | EU worker survey and methodology | Worker-side evidence across all 27 EU Member States. |
| NBER-W35445 | [Organizational Incentives and the Returns to Technology Adoption](https://www.nber.org/papers/w35445) | randomized field experiment | Indian garment factories; communication technology, HR incentives, productivity, absenteeism, and earnings. |
| NBER-W35372 | [Empowering Inclusive Work](https://www.nber.org/papers/w35372) | platform study and difference-in-differences | Chinese food-delivery workers with hearing disabilities; AI-enabled text-to-speech and pay gap. |
| NBER-W35467 | [Women in the Platform Economy](https://www.nber.org/papers/w35467) | survey and administrative data | Women drivers in India and Indonesia; flexibility, safety, harassment, domestic limits, and unequal returns. |
| WORLD-BANK-LAC-AI | [Quantifying the Jobs Potential of AI in Latin America and the Caribbean](https://www.worldbank.org/en/results/2025/04/15/quantifying-the-jobs-potential-of-ai-in-latin-america-and-the-caribbean) | regional analysis using household and labor-force surveys | Infrastructure, exposure, productivity potential, and unequal regional effects. |
| ILO-SOCIAL-DIALOGUE-2025 | [Global case studies of social dialogue on AI and algorithmic management](https://www.ilo.org/publications/global-case-studies-social-dialogue-ai-and-algorithmic-management) | comparative labor-relations working paper | Worker representatives and AI decisions across Europe, North America, Asia, South America and the Caribbean, and Africa. |
| SAG-AFTRA-2023-AI | [2023 TV/Theatrical Contracts](https://www.sagaftra.org/contracts-industry-resources/contracts/2023-tvtheatrical-contracts) and [Digital Replicas 101](https://www.sagaftra.org/sites/default/files/sa_documents/DigitalReplicas.pdf) | union-published contract record and explanation | Direct check of notice, consent, compensation, digital alteration, and synthetic-performer rules in the ILO case. |
| GERMAN-AI-WORKS-COUNCILS | [Deutsche Telekom Digital Ethics](https://www.telekom.com/en/company/digital-responsibility/details/our-action-areas-digital-ethics-1008324), [Telekom AI manifesto](https://www.telekom.com/de/konzern/details/telekom-verpflichtet-sich-auf-ki-ethik-1025794), and [ver.di workplace AI examples](https://publik.verdi.de/ausgabe-202304/mensch-vor-maschine/) | company and union records | Direct check of the joint manifesto/framework and human-review claims in the ILO case. |
| KENYA-META-SAMA-COURT | [Kenya Court of Appeal judgment](https://new.kenyalaw.org/akn/ke/judgment/keca/2024/1152/eng%402024-09-20/source) | official appellate court record | Contested-case check: interim protections for outsourced content moderators were set aside on appeal; merits remained open in this judgment. |
| KENYA-META-MOTAUNG-COURT | [Kenya Court of Appeal judgment](https://new.kenyalaw.org/akn/ke/judgment/keca/2024/1262/eng%402024-09-20/source) | official appellate court record | Related appeal: Meta’s jurisdiction and interim-order challenges were dismissed; the merits remained open. |
| IBM-GERMANY-AI-FRAMEWORK-2020 | [IBM Central Holding / Group Works Council AI framework](https://wageindicator.org/de-de/arbeiten-in-deutschland/tarifvertrag/konzernbetriebsvereinbarung-uber-die-einfuhrung-und-den-einsatz-von-systemen-der-kunstlichen-intelligenz-artificial-intelligence) | archived agreement text | Concrete check of binding rules, risk classes, correction paths, AI Ethics Council, works-council inspection, and retraining language. |
| IBM-GERMANY-AI-IMPLEMENTATION-INTERVIEW | [BTQ Kassel interview with IBM Group Works Council representative](https://www.btq-kassel.de/interview_frank_remers/) | worker-representative interview | Checks timing and implementation: the framework was designed before AI was part of employees’ daily work; very-high-risk systems were described as excluded. |
| JRC-AIMWORK-METHOD-2025 | [Methodology of the AIM-WORK survey](https://publications.jrc.ec.europa.eu/repository/handle/JRC143933) | official EU survey methodology | 70,316 respondents, all 27 EU Member States, mobile CATI, random-digit dialing, weighting, validation, and occupation/industry coding. |
| JRC-AIMWORK-ANALYSIS-2026 | [Algorithmic management and working conditions in Europe](https://publications.jrc.ec.europa.eu/repository/handle/JRC147505) | official EU working paper | Cross-country associations between specific algorithmic-management practices, autonomy, breaks, stress, discretion, and work intensity. |

The OECD report says managers report concerns about unclear accountability, difficulty following the logic of decisions, and protection of workers’ health. The ILO study examines how algorithmic management changes work organization and industrial relations in ordinary workplaces, not only digital platforms. These sources broaden the project beyond software firms, but they do not replace worker-level outcome evidence.

The Capgemini report adds an operator view: AI adoption is tied to training at scale, internal knowledge and employee-data systems, changes to role definitions and career paths, and workforce adaptation costs. It is a company disclosure, so it shows management’s stated plan and risk framing—not whether the plan improved workers’ lives.

The JRC AIM-WORK survey adds the worker side. Its 2024–2025 fieldwork covered 70,316 people aged 16–65 across all 27 EU Member States. The Commission reports that 30% use AI at work, 37% are monitored for working hours, and 24% have schedules set automatically. It also reports that monitoring and management technologies can raise stress and reduce autonomy, with results varying by sector and practice.

The two NBER studies add a non-European and inclusion-focused test. In Indian garment factories, communication technology alone had no effect relative to control, while pairing it with HR-manager incentives raised productivity and worker earnings. In a Chinese food-delivery platform, an AI text-to-speech tool improved outcomes for deaf or hard-of-hearing workers and closed part of the hourly-pay gap. Both studies suggest that tool access is shaped by organizational design and worker difference.

The regional pass adds gender and infrastructure. NBER evidence from India and Indonesia finds that women value platform flexibility and supplemental earnings, but participation is very low and shaped by safety, household constraints, harassment, discrimination, and unequal hourly returns. The World Bank/ILO regional analysis finds that Latin American AI exposure does not automatically produce benefits where digital infrastructure is missing.

## Cross-source synthesis update — 2026-09-13

The current NBER results should be read as different measurement layers rather
than as contradictory estimates of one “AI effect”:

| Source | Unit and design | Direct result | What it contributes to the theme |
|---|---|---|---|
| [Generative AI at Work](https://www.nber.org/papers/w31161) | 5,179 customer-support agents; staggered access to an AI assistant | Average productivity rose 14%, with a 34% improvement for novice and low-skilled workers and little effect for experienced/high-skilled workers | Tool access can change task performance unevenly by worker experience |
| [Shifting Work Patterns with Generative AI](https://www.nber.org/papers/w33795) | Field experiment across 66 firms and 7,137 knowledge workers | Among treated users, work outside regular hours and email time fell; individual provision did not shift task quantity or composition | Time savings do not automatically imply job redesign or broader organizational change |
| [What Work Does Generative AI Do?](https://www.nber.org/papers/w35677) | Nationally representative worker survey linked to occupations and tasks | Adoption is widespread but shallow, with fewer than half of workers adopting within most occupations/tasks | Occupation-level exposure does not identify which similar workers adopt |
| [The Rapid Adoption of Generative AI](https://www.nber.org/papers/w32966) | Repeated nationally representative US surveys | By late 2024, 23% of employed respondents had used generative AI at work in the prior week and 9% used it every workday | Aggregate adoption can be substantial while intensity and worker-level participation remain uneven |

### Bounded interpretation

Together these sources support a provisional theme: generative AI is entering
work quickly, but its consequences are conditional on worker experience, task,
organizational setting, and depth of use. The evidence is consistent with work
being reorganized unevenly before a common change in pay, hours, or employment
appears.

The sources do not establish that AI has broadly shifted bargaining power,
promotion, health, job quality, household security, or political meaning. The
experiments and survey measure different populations, interventions, outcomes,
and time windows. The next evidence must connect adoption to workplace rules,
training, monitoring, discretion, correction, worker voice, and later material
and social outcomes.

The ILO social-dialogue study adds a governance path before harm occurs. It examines national, regional, sectoral, company, and workplace cases in five world regions and documents how worker representatives influence decisions about employment, algorithmic management, and working conditions. It is case evidence, not a measure of how common effective participation is.

## Macro, infrastructure, and country-capability pass

Search terms:

- `AI adoption productivity employment firm size complementary investment BIS`
- `AI adoption inequality wealth capital returns IMF`
- `AI output data capital productivity measurement BEA`
- `AI data centre electricity grid critical minerals IEA`
- `AI readiness cloud data centre connectivity power local data skills World Bank`
- `Romania government cloud migration applications public procurement`
- `Malaysia Johor data centre IFC Yondr Vantage financing ownership`

Included records:

| ID | Source | Type | Why it is in scope |
|---|---|---|---|
| IMF-AI-INEQUALITY-2025 | [AI Adoption and Inequality](https://www.imf.org/en/publications/wp/issues/2025/04/04/ai-adoption-and-inequality-565729) | household microdata and calibrated task model | Separates wage and wealth channels and models firm adoption choices and capital returns. |
| BIS-AI-FIRMS-1325 | [AI adoption, productivity and employment](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms) | matched firm study | Measures productivity, employment, wages, size, finance, software, data, and training across more than 12,000 firms. |
| BEA-AI-EXPECTATIONS-2026 | [AI Expectations and Outcomes](https://bea.gov/sites/default/files/papers/bea-wp2026-16.pdf) | official working paper and production-account analysis | Separates expected from reported use, records a survey-definition break, and links stated motivations to capital and industry outcomes. |
| IEA-ENERGY-AI-2025-2026 | [Energy and AI](https://www.iea.org/reports/energy-and-ai) and [Key Questions on Energy and AI](https://www.iea.org/reports/key-questions-on-energy-and-ai) | global energy analysis and scenarios | Measures electricity, grids, equipment, minerals, affordability, energy security, and data-centre capacity. |
| OFR-AR-2025 | [2025 Annual Report](https://www.financialresearch.gov/annual-reports/files/OFR-AR-2025.pdf) | official institutional report | Records AI use in a financial regulator alongside public analytical infrastructure, budget, and workforce changes. |
| WORLD-BANK-WDR2026-AI | [World Development Report 2026](https://www.worldbank.org/en/publication/wdr2026) | global development report | Provides adopt/adapt/advance and political, economic, social, and institutional AI frames. |
| WORLD-BANK-AI-READINESS-2026 | [Building Data Infrastructure for AI Readiness](https://www.worldbank.org/en/results/2026/05/06/data-infrastructure-for-ai) | development-finance results brief | Names the four Cs and gives Romania and Malaysia project records. |
| WORLD-BANK-WBES-AI-FOLLOWUP-2026 | [Enterprise Surveys data update](https://www.enterprisesurveys.org/en/data/data-updates) and [WDR 2026 reproducibility catalog](https://reproducibility.worldbank.org/catalog/624) | firm survey release and data-access record | Identifies the 2026 AI follow-up files for the United States and eight comparison economies; intended to measure firm AI impact and adjustment, but microdata access and survey-design documentation must be completed before estimates are promoted. |
| ROMANIA-MAS-IC | [Authority for Digitalization: cloud migration](https://www.adr.gov.ro/en/investitia-2-dezvoltarea-cloudului-si-migrarea-in-cloud) | government project record | Supplies a primary target, date, budget, beneficiaries, and public-cloud migration scope. |
| IFC-YONDR-MY-49145 | [IFC project disclosure](https://disclosures.ifc.org/project-detail/SII/49145/yondr-my-dc-2023) | development-finance project disclosure | Records the borrower, 96 MW first phase, up-to-US$150m loan, and project structure. |
| MALAYSIA-YONDR-VANTAGE-TRANSFER | [Yondr sale](https://www.yondrgroup.com/newsroom/press-release/yondr-group-completes-sale-of-johor-campus-to-vantage-data-centers) and [Vantage investment](https://vantage-dc.com/news/vantage-data-centers-completes-1-6b-investment-in-apac-platform-from-gic-and-adia-closes-acquisition-of-yondrs-300mw-hyperscale-campus-in-johor-malaysia/) | operator ownership records | Tracks the campus transfer and the investment structure around the APAC platform. |

The country records are not yet enough to measure realized local jobs, data control, energy burden, service quality, or switching costs. They are the first primary records for the next comparison.
