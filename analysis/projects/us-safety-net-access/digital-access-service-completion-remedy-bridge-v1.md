# Digital access, service completion, and remedy bridge

**Status:** eighteenth active depth artifact in the ongoing program  
**Checked:** 2026-10-18  
**Scope:** digital public services, consumer interfaces, disability access, and unequal infrastructure

## Question

When a service is available online, does a person have a usable path to finish
the task, receive the result, correct an error, and obtain a human remedy?

The central distinction is:

```text
connectivity -> device and interface access -> task completion
  -> result quality and continuity -> correction / appeal / remedy -> trust
```

Internet access, application availability, form completion, and successful
resolution are different stages. A high national access rate cannot close the
later stages by itself.

## Evidence ledger

| Stage or link | Comparable observation | Method and unit | Boundary |
|---|---|---|---|
| Basic connectivity | Malaysia reported household Internet access of 97.1% in 2025, but 99.0% in urban households versus 90.7% in rural households. Individual mobile use was 99.6%, Internet use 98.3%, and computer use 81.5%. | DOSM ICT Use and Access survey; household and individual percentages. | Access is not skill, affordability, service quality, or completed task. The public summary does not disclose one pooled denominator for every estimate. |
| Disability interface friction | In Canada, 13% of people with disabilities reported barriers accessing government information, services, or supports online; 11% had barriers booking online and 9% banking or shopping online. Internet-use barriers were 28% among people with very severe disabilities versus 9% among people with mild disabilities. | Statistics Canada 2022 Canadian Survey on Disability; approximately 8 million Canadians aged 15+ with one or more disabilities in the published frame. | Self-reported cross-sectional barriers are not transaction logs, failed applications, lost income, or causal effects. |
| Friction inside the device and time budget | In Canada's 2024 accessibility ICT survey, 46% reported difficulty using a technological device, 25% an online communication barrier, 10% difficulty accessing support services through communication tools, and 9% time-limit barriers. | Statistics Canada Survey Series on Accessibility; survey estimates with a distinct 2024 frame. | These are not the same population or instrument as the 2022 disability survey and should not be pooled. |
| Formal digital government versus practical reachability | OECD indicators report 46% of people not confident they could access support when needed, 31% saying they could easily receive public benefits, and 28% believing a benefit application would be simple and quick. The Outlook describes repeated information requests and fragmented handovers across agencies. | OECD comparative synthesis of trust-survey indicators and digital-government implementation evidence. | Comparative secondary evidence, not administrative completion data or a causal digitalization estimate. |
| AI-enabled service legitimacy | BCG surveyed 48,500 respondents in 44 countries; nearly two-thirds still wanted human oversight embedded in digital services, even as AI use and comfort with agents increased among more proficient users. | Biennial citizen survey and public governance synthesis. | Public summary is not country-microdata, an appeals audit, an error-rate estimate, or proof that human oversight is available in practice. |
| Data portability and correction | Australia had 1.3 million Consumer Data Right users by July 2026, but stakeholders rated overall consumer-data quality 3.5/5 and resolution experience 3.1/5. Some tickets remained open more than six months, and some users lacked a clear escalation path. | ACCC survey of 16 data-right stakeholders plus follow-up meetings and regulatory observation. | Small, selected stakeholder frame; not a representative consumer study, switching estimate, or household-outcome effect. |
| Employment-service completion beyond placement | The ILO disability-employment review treats success as preparation, matching, reasonable accommodation, retention, skills, and progression, not placement alone. It notes digital tools are concentrated in access, job search, skills, and matching, with less evidence for accommodation, retention, and progression. | Practice exchange and mapping of European employment-service examples. | Practice evidence, not a comparative outcome evaluation or algorithmic-fairness audit. |

## Cross-source finding

The recurring pattern is a **completion and remedy gap**. Infrastructure can be
near-universal while the usable task path remains unequal. The gap is largest
where a person needs accessibility, a larger device, more time, cross-agency
coordination, or a human escalation route.

This produces four distinct failure modes:

1. **Entry failure:** the person cannot reach or authenticate to the service.
2. **Interaction failure:** the interface, device, language, disability access,
   or deadline prevents completion.
3. **Continuity failure:** agencies repeat information or a handoff loses the
   case, so a completed form does not produce a stable result.
4. **Remedy failure:** an error is visible but cannot be corrected within a
   usable time horizon.

The evidence supports these as mechanisms, but not one universal rate. OECD
confidence measures, Canadian disability barriers, and ACCC resolution evidence
point to the same open middle: what happens after attempted access and before
trust or exit?

## Bounded public discussion

The atlas's LinkedIn discussion of digitally deliverable services emphasizes a
different but related inequality: rapid digital growth can coexist with least
developed countries losing share because infrastructure and productive capacity
do not keep pace. This is a macro capacity warning, not a household usability
estimate. The wider public discussion around accessible digital services should
therefore be used to look for concrete failure modes—unsupported assistive
technology, inaccessible authentication, missing alternatives, and unresolved
cases—rather than to count engagement as successful access.

## Counterexamples and alternative explanations

- Mobile-first access can be an effective design choice for some users; lower
  computer use is not automatically exclusion.
- A person may report an online barrier but complete the task through a phone,
  family member, call centre, or in-person route. Barrier prevalence is not
  completion failure.
- Human oversight can improve legitimacy only if the human can actually review,
  explain, and change the decision; its presence in policy language is not
  operational remedy.
- A long data-quality ticket may reflect a difficult underlying correction, not
  only poor service design, but the six-month duration still matters to choice.
- AI may reduce waiting or paperwork for some users while increasing opacity or
  accessibility risk for others. Average adoption cannot resolve that split.

## Stronger next test

Build an episode-level completion ledger for the same service journey:

1. user need and eligibility;
2. device, accessibility, language, and authentication route;
3. submission, handoff, and time spent;
4. approval, denial, delay, or incomplete result;
5. alternate channel and human escalation;
6. correction, appeal, or remedy time; and
7. downstream security, trust, repeat use, or exit.

Stratify by disability severity, rurality, income, age, migration, device,
language, and AI-assisted versus human-only route. The strongest design joins
service logs to survey-reported friction and preserves unsuccessful attempts,
not just completed transactions. Compare services with the same access rate but
different correction and escalation performance.

## Current answer state

**Partly answered.** The evidence shows that connectivity, usable interface,
service completion, continuity, and remedy are separate stages. It does not yet
provide a same-episode population estimate linking accessibility friction to a
completed public result and later trust or exit.

## Stopping rule for this rotation

Do not claim digital inclusion from access or adoption alone. This chain is not
resolved until one longitudinal or episode-level source observes at least three
transitions—access, completed result, and correction/remedy—with subgroup
denominators and a documented alternate route or null case.

Related: [project README](README.md), [ongoing operating plan](../../ONGOING-GOAL-OPERATING-PLAN_V1.md), and the [public-system social-meaning bridge](public-system-social-meaning-bridge-v1.md).
