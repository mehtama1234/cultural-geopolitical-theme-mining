# Source record: German works-council AI rules

**Checked:** 2026-09-14
**Source family:** company and union records  
**Use:** direct check of the Deutsche Telekom and IBM portions of the ILO case summary

## Sources

1. [Deutsche Telekom: Digital Ethics](https://www.telekom.com/en/company/digital-responsibility/details/our-action-areas-digital-ethics-1008324), accessed 2026-09-11.
2. [Deutsche Telekom and Group Works Council adopt AI manifesto](https://www.telekom.com/de/konzern/details/telekom-verpflichtet-sich-auf-ki-ethik-1025794), accessed 2026-09-11.
3. [ver.di: Mensch vor Maschine](https://publik.verdi.de/ausgabe-202304/mensch-vor-maschine/), accessed 2026-09-11.
4. [ver.di: Auch die KI macht Fehler](https://publik.verdi.de/ausgabe-202503/auch-die-ki-macht-fehler/), accessed 2026-09-11.
5. [WageIndicator transcription of IBM Central Holding GmbH / Group Works Council AI framework, version 25 June 2020](https://wageindicator.org/de-de/arbeiten-in-deutschland/tarifvertrag/konzernbetriebsvereinbarung-uber-die-einfuhrung-und-den-einsatz-von-systemen-der-kunstlichen-intelligenz-artificial-intelligence), accessed 2026-09-11.
6. [BTQ Kassel interview with IBM Group Works Council representative Frank Remers](https://www.btq-kassel.de/interview_frank_remers/), 10 March 2022 interview, accessed 2026-09-11.
7. [Krzywdzinski, Gerst, and Butollo, “Promoting human-centred AI in the workplace”](https://doi.org/10.1177/10242589221142273), accessed 2026-09-15.

These records are published by the company, the union, and WageIndicator. The WageIndicator page reproduces the IBM framework text and identifies IBM Central Holding GmbH, its Group Works Council, and a 30 July 2020 signature date. It is an accessible archive of the agreement, not the original IBM document host. None of these records independently shows compliance, worker coverage outside the named German entities, or effects on pay, productivity, or stress.

The peer-reviewed study independently describes the IBM agreement as a joint
works-council, HR, and expert project, including its human-final-decision
principle and AI Ethics Council. It corroborates the architecture and
development pathway, but does not add a worker-level outcome or audited
deployment record.

The WageIndicator acquisition is preserved in the [machine-readable acquisition
record](data/wageindicator-ibm-ai-framework-acquisition-v1.json). The fetched
HTML response was 681,137 bytes, returned HTTP 200 as `text/html`, and has
SHA-256 `37d16c3e02a17a4698d5d3a23ae608829b5f1f1e0ecdfef32db8470c15d2e6d3`.
The text was reviewed section by section after HTML-to-plain-text extraction;
the hash identifies the retrieved page, not an original IBM document file.

The [BTQ Kassel interview acquisition record](data/btq-ibm-ai-framework-interview-acquisition-v1.json)
preserves the complementary implementation-status account. The retrieved HTML
response was 85,800 bytes, returned HTTP 200 as `text/html`, and has SHA-256
`d03fcd5818067d6eade29cb97cbca762056321e8e8bcaa7a265f8413b80a1a6d`. The
interviewee reports internal call-center and training/career recommendation
systems in use, while a manager salary-increase recommender and voluntary-
resignation probability system were not used in Germany at that time. These
are reported practice and scope signals, not an audited inventory or outcome
evaluation.

## What the records say

- Deutsche Telekom says it adopted an AI manifesto with its Group Works Council and that the manifesto sets standards for processing employee data in AI systems.
- Deutsche Telekom describes AI governance as a co-creation structure involving steering, technical, and regulatory authorities.
- ver.di reports that IBM Germany agreed a framework agreement in 2020 for introducing and using AI systems, with the principle that AI supports human decisions and a human makes the final decision.
- ver.di’s IBM example names a “Skill Recommendation” tool that uses workplace data to suggest development options, while retaining a human decision-maker.
- The archived IBM framework says its rules are immediately binding within scope, requires transparency, explainability, human decision-making, non-discrimination, data and algorithm quality checks, an AI Ethics Council, and risk classification.
- The framework prohibits category-5 systems: recommendations for or automatic decisions about personnel measures without a benefit or harm-reduction potential for a substantial part of the workforce.
- For categories 2 through 4, the framework requires a correction process for false recommendations; for category 4, workers can contact the AI Ethics Council and the application must support rapid correction.
- The framework gives works councils inspection rights over data-quality methods, bias analysis, transparency information, and the purpose of the AI system. It says that if an AI system eliminates a job or changes work, an equivalent job should be offered where possible and retraining provided if needed.
- The union and company descriptions establish rule design and institutional participation; they do not establish compliance, use across all IBM entities, or whether the controls prevent all individual monitoring in practice.
- In the 2022 BTQ interview, the IBM works-council representative said the framework was created early, before AI applications had affected employees’ daily work, and described its purpose as setting conditions before wider use.
- The same interview says the very-high-risk category leads IBM not to deploy such systems. This is a representative’s account of the framework’s operation, not an independently audited deployment log.

## Mechanism relevance

```text
works-council rights -> joint review and stated limits -> bounded data use and human review
```

This is a documented governance path with concrete review, correction, and exclusion rules. The available record also suggests it was designed before routine workplace use, so it is not yet a measured outcome path. The next evidence must show cases where a live deployment was changed or stopped and worker outcomes after implementation.

## Coding

| Field | Coding |
|---|---|
| Level | Company and workplace agreements |
| Worker representative | Group works council; works councils; ver.di in the IBM account |
| Before deployment | Manifesto/framework, consultation, and stated AI-use standards |
| Data or asset at issue | Employee data, workforce analytics, recommendations, and monitoring systems |
| Worker remedy or leverage | Correction process, AI Ethics Council, works-council inspection, and retraining language |
| Direct outcome measure | None in the cited records |
| Evidence class | Archived agreement text plus company and union records |
| Main uncertainty | Live deployment cases, enforcement, scope, and worker-level effects |

## Relation to the ILO case table

This record strengthens the Deutsche Telekom and IBM row in [the ILO social-dialogue case table](ilo-social-dialogue-case-table-v1.md) while keeping the distinction between a stated rule and an observed result.
