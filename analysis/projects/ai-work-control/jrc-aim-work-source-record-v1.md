# Source record: JRC AIM-WORK survey and analysis

**Checked:** 2026-09-15
**Source family:** official EU worker survey and analysis  
**Use:** worker-side evidence on algorithmic management, monitoring, and job quality

## Sources

1. [JRC AIM-WORK project page](https://joint-research-centre.ec.europa.eu/scientific-activities/employment/algorithmic-management-and-digital-monitoring-work_en), accessed 2026-09-11.
2. [Methodology of the AIM-WORK survey, JRC143933](https://publications.jrc.ec.europa.eu/repository/handle/JRC143933), accessed 2026-09-11.
   [Direct PDF](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC143933/JRC143933_01.pdf), reviewed 2026-09-15.
3. [Algorithmic management and working conditions in Europe: Evidence from the AIM-WORK Survey, JRC147505](https://publications.jrc.ec.europa.eu/repository/handle/JRC147505), 6 July 2026, accessed 2026-09-11.
4. [Digital Monitoring, Algorithmic Management and the Platformisation of Work in Europe, JRC143072](https://publications.jrc.ec.europa.eu/repository/handle/JRC143072), 13 October 2025, accessed 2026-09-11.

## Design and coverage

- The survey collected responses from 70,316 people aged 16–65 across all 27 EU Member States.
- Fieldwork ran from 23 October 2024 to 21 January 2025.
- The methodology describes a mobile-only computer-assisted telephone interview approach using random-digit dialing, translation and cognitive testing, fieldwork training and quality control, data validation, weighting, and occupation and industry coding.
- The survey asks about digital devices, AI tools, digital monitoring, algorithmic management, and platformisation of work.

## Methodology audit

The methodology report makes the headline sample more specific. It describes
an independent country sample of 1,253 to 3,781 respondents aged 16–65 in each
EU Member State, with target sizes of 3,750 in Italy, France, Germany, Spain,
and Poland; 1,250 in Cyprus, Malta, and Luxembourg; and 2,500 in the remaining
Member States. The main fieldwork used CATI and ran from 23 October 2024 to 21
January 2025; a validated, weighted dataset was delivered on 18 February
2025.

The questionnaire targets the full working-age population but routes the main
algorithmic-management and AI-work block to people in paid work. The design
therefore supports population and worker comparisons only after the relevant
routing, weights, nonresponse, and item denominators are checked. The public
methodology does not turn a worker’s report of a practice into a firm-level
implementation record, nor does it identify a matched pre/post workplace.

The report also defines platformisation broadly as the combination of digital
devices, digital monitoring, and algorithmic management in ordinary workplaces;
it is not synonymous with digital-labour-platform work. This distinction is
important when interpreting the analysis and prevents treating every digital
tool as one exposure.

This is a large cross-country worker survey. It is not a panel experiment and does not by itself prove that a specific technology caused a specific worker outcome.

## Main reported results

- The JRC reports that about one third of EU workers use AI for work-related purposes and that digital monitoring and algorithmic management are significant across countries and sectors.
- Automated allocation of shifts or working time is the most common form of algorithmic management in the project summary.
- The 2026 analysis reports that algorithmic management is associated overall with lower autonomy, less ability to take breaks, and higher work-related stress, but that the size and direction vary by practice.
- Direct algorithmic direction of tasks and work pace has the strongest reported association with lower discretion and greater work intensification.
- Exposure to several practices at once is associated with more negative outcomes, and effects differ substantially across countries.
- The JRC also reports that some forms of platformisation have no significant implications for working conditions; the negative pattern is not a claim about every digital tool.

## Mechanism relevance

```text
monitoring or automated direction -> less discretion or fewer breaks
-> greater work intensity or stress -> changed job quality
```

The survey and analysis support associations along this path. They do not identify a single cause for every worker or establish that the IBM framework, a specific vendor, or AI alone produced the outcomes.

## Coding

| Field | Coding |
|---|---|
| Unit | Working-age individual worker |
| Geography | All 27 EU Member States |
| Time | Fieldwork October 2024–January 2025; analysis published 2026 |
| Sample | 70,316 respondents aged 16–65 |
| Method | Mobile-only CATI, random-digit dialing, weighting, occupation and industry coding |
| Outcomes | Autonomy, breaks, stress, work intensity, and working conditions |
| Evidence class | Weighted survey and cross-country association analysis |
| Main limits | Self-report, cross-sectional evidence, practice differences, and no direct test of one firm’s governance agreement |

## Acquisition status

**Methodology:** reviewed and promoted to the evidence record.
**Practice/outcome and qualitative country-map extraction:** completed in the
[practice and country map](jrc-aim-work-practice-country-map-v1.md).
**Full Table 2 transcription:** completed for all 16 outcomes in [the
machine-readable record](data/jrc-aim-work-table2-full-v1.json); the five-outcome
[core record](data/jrc-aim-work-table2-core-v1.json) remains available for quick
review.
**Country/sector table extraction with denominators, standard errors, and
uncertainty:** still open.
**Microdata or code replication:** not established from the public publication
record; the JRC analysis page lists no public dataset or source-code link in
the accessible metadata.
**Safe current use:** report the published sample and associations, preserve
the worker-level and cross-sectional unit, and do not infer firm-level causal
effects or worker appeal/override from the survey alone.

## Relation to the project

This record supplies the worker-side comparison for [Finding 009](findings/ai-work-control-009.md). It helps test whether formal oversight corresponds to lived autonomy and stress, but the available public record does not identify workers covered by the IBM agreement or provide a matched comparison group.
