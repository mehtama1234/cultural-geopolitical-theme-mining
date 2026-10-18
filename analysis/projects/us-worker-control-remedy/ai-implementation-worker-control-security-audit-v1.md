# AI implementation, worker control, and security audit

**Status:** active depth artifact; cross-source stage audit, not a workforce-wide causal estimate  
**Checked:** 2026-10-18  
**Scope:** AI adoption and output -> task redesign -> worker voice, autonomy, training, bargaining power, and durable security

## What we found

AI evidence is becoming more precise about activity and output, but the worker
conversion remains open. More commits, projects, or firm adoption do not tell
us who controls the pace, who receives the time or earnings gain, whether a
worker can challenge the system, or whether a household becomes more secure.

```text
AI access or organizational adoption
  -> task activity, time, or output
  -> workflow and monitoring change
  -> worker voice, autonomy, training, or outside option
  -> pay, hours, job quality, and household security
  -> continued work, bargaining, switching, or exit
```

## Comparable evidence ledger

| Source and unit | Observed implementation or output | Worker-control/security surface | What it establishes | Main limit |
|---|---|---|---|---|
| [NBER task-level adoption](../../records/us-nber-task-level-genai-adoption-2026.json), 13,920 workers and 55,634 worker-task observations, 2025–26 | Fewer than half adopt within most detailed occupations/tasks; exposure scores explain 5%–53% of occupation and 7%–44% of task adoption variation | Worker-level pay, discretion, voice, and security are not measured; the public task index reports reasoning/decision use at 30% and physical/manual work at 9.6% | Similar exposure does not imply similar adoption; workplace access, task fit, training, rules, privacy, and choice remain plausible conversion mechanisms | Descriptive working-paper evidence; exposure and adoption do not identify the mechanism or outcome |
| [NBER coding activity and shipped output](../../records/us-nber-ai-coding-productivity-shipping-output-2026.json), at least 500,000 GitHub developers plus four software marketplaces | Commits rose 30% with autocomplete, 180% with interactive agents, and 240% with autonomous agents; autonomous-agent projects rose 80% and releases 30%; marketplace total usage did not increase | Human–AI substitution elasticity estimated at 0.23; worker pay, authority, workload, and release quality are not followed | Activity attenuates as the chain moves from coding activity to projects, releases, and market use | Developer and marketplace measures are not one employment panel; association with tools does not identify who captures gains or bears risk |
| [NBER firm expectations](../../records/us-nber-firm-ai-expectations-2026.json), nearly 6,000 senior executives in US, UK, Germany, and Australia | 69% reported active AI use; 90% reported no employment or productivity impact over the prior three years; expected next-three-year productivity was +1.4% and output +0.8% | Employers expected employment -0.7% while employees expected +0.5% at their firms | Adoption, retrospective impact, and forward expectations are separate clocks and perspectives | Executive expectations are not realized worker outcomes, and the multinational sample is not a US administrative panel |
| [ILO Chinese enterprise study](../../records/comparative-ilo-chinese-enterprise-ai-adoption-hybrid-work-measurement-2026.json), 21 interviewed firms and 1,591 professionals | All 21 firms reported deployment or imminent adoption; reported examples include customer-service throughput from 6,000 to 15,000 issues/day for 300 employees and a specification-reading team falling from more than 10 workers to 2–3 | Firms lacked systematic measures of job quality, task composition, working conditions, redeployment, and who captures released time; 39% of professionals anticipated income declines and human review remained important | Organizational location and governance determine whether AI becomes assistance, process control, or labor-input reduction | Purposive interviews, self-reported firm metrics, and descriptive professional survey; no causal employment, wage, or household result |
| [ILO AI psychosocial-work review](../../records/comparative-ilo-ai-systems-work-psychosocial-autonomy-2026.json), evidence/policy synthesis | Identifies surveillance, work intensification, data collection, and algorithmic evaluation as possible AI-associated risks | Autonomy, dignity, transparency, participation, human oversight, and correction are treated as work conditions | Worker control is not just an employment count; design and governance can change psychosocial conditions | Review, not prevalence or workplace causal evaluation; no common probability, severity score, or compliance outcome |
| [NBER retraining returns](../../records/us-nber-ai-worker-retraining-returns-2026.json), WIOA training spells matched to job-search-only users | Estimated quarterly earnings return for high-exposure trainees was about $1,000 in 2012–19 and about $3,000 in 2022–24 | Gains were mainly associated with moving into less AI-exposed occupations, with a smaller AI-complementary route | Training can be a bridge to earnings, but the route may be occupational movement rather than control over the original job | Public abstract does not disclose sample size, completion, access, hours, benefits, stability, household costs, or worker preference |
| [NBER outside-option experiment](../../records/us-nber-gig-economy-outside-options-labor-supply-2026.json), Uber-driver pay experiments and competitor-access variation | Access to one competing platform nearly doubled drivers’ elasticity to Uber; implied markdown fell from about 68% to 50% | Outside options changed labor supply response; women were about twice as elastic to the market as men while no less elastic to Uber | Competition can increase bargaining leverage without requiring a formal voice institution | Driver count, geography, timing, net earnings, hours stability, safety, benefits, and durable household security are not disclosed |
| [ACCA professional survey](../../records/comparative-acca-global-talent-trends-2026-ai-hiring-hybrid-work-professional-trust.json), global accountancy/finance professionals, 2026 | 52% regularly used AI; 31% reported organizational AI-agent deployment; 93% of LinkedIn recruiters planned to increase AI use in hiring | 48% were not confident in AI recruitment versus 43% confident; 75% preferred hybrid work, 58% believed office presence affected promotion, and 43% of Gen Y would consider leaving after substantially more office time | Worker control includes human judgment, work-location choice, promotion visibility, and credible support—not only training | Self-report, profession-specific and non-representative; confidence, preference, and intention are not observed turnover or job quality |

## What this connects to

The evidence supports a **conversion gap**, with three distinct bottlenecks.

First, activity is not output. The coding study finds large increases in
commits and projects but smaller release growth and no marketplace-use growth.
This is a counterexample to treating tool activity as realized economic value.

Second, output is not control. Firm examples can show faster service or fewer
labor inputs while lacking measures of job quality, redeployment, workload,
voice, or who controls released time. ILO's psychosocial review identifies the
possible cost as intensified monitoring or pace, not merely job loss.

Third, training is not security. The NBER retraining evidence suggests earnings
gains often arrive through movement into less exposed occupations. That may be
valuable, but it is different from a worker gaining bargaining power or keeping
control over the original job. The outside-option experiment supplies a useful
counterexample: competition can improve leverage even when no training or
formal representation is observed.

## Bounded public discussion

Public discussion adds interpretation and contested expectations, not
population estimates:

| Record | Discussion signal | Use and limit |
|---|---|---|
| [ILO work discussion](../../social-discussions/records/ai-work-control-005.json) | AI is discussed as a productivity, inequality, autonomy, and job-quality issue rather than only a displacement count | Keeps output and control separate; selected professional discussion is not worker prevalence |
| [AI hiring discussion](../../social-discussions/records/atlas-acca-ai-hiring-linkedin-001.json) | Skills-based hiring, hybrid flexibility, human judgment, and distrust of AI screening are treated as linked worker concerns | Identifies a control and legitimacy hypothesis; report commentary is not a hiring-system audit |
| [Automation and meaning discussion](../../social-discussions/records/atlas-batch-0064-automation-meaning-linkedin-001.json) | Discussion treats automation as a question of purpose, dignity, and what work is for | Adds cultural meaning; replies do not measure job redesign or wellbeing |
| [Career uncertainty discussion](../../social-discussions/records/ai-work-control-003.json) | Workers debate mass unemployment, new work, and the credibility of alternatives | Makes perceived outside options visible; self-selected Reddit comments are not employment data |
| [AI workplace surveillance discussion](../../social-discussions/records/atlas-batch-0055-surveillance-linkedin-001.json) | Surveillance and performance targets are discussed as possible safety tools or anxiety/injury risks | Preserves the counterexample that the same monitoring can protect or intensify work; no worker-level outcome |

The discussion layer reinforces the central finding: workers ask who decides,
who verifies, who benefits, and what alternative exists. It does not answer
those questions for any measured firm or worker.

## Missing links and challenge checks

- Do not join worker-task adoption to firm expectations by occupation alone.
- Do not treat commits, tasks, or throughput as earnings, job quality, or
  worker control.
- Do not treat a reported reduction in labor input as worker displacement or
  household harm without a defined denominator and counterfactual.
- Do not treat training returns as proof of accessible, preferred, or durable
  transition.
- Do not treat outside-option elasticity as realized household security.
- Keep worker, employer, platform, customer, and household units separate.
- Preserve the positive counterexample: AI can reduce routine work or improve
  safety when workers have review, participation, and a credible alternative.

## Stronger next test

The next high-value record is one same-worker or same-workplace episode with:

1. baseline role, task, pay, hours, and system exposure date;
2. employer decision, notice, training, monitoring, and worker voice;
3. task, pace, schedule, pay, health, and household-time changes;
4. review, correction, remedy, or an accessible human fallback;
5. outside alternatives, bargaining, continued work, or switching; and
6. later earnings, job quality, recurrence, trust, and exit.

If that record cannot be lawfully obtained, preserve the stage comparison and
seek a bounded workplace or platform episode rather than infer durable control
from aggregate adoption or expectations.

## Deeper question

**When does AI-enabled output become worker security and bargaining power, and
when does it become a private adaptation whose time, risk, and meaning are
assigned by the firm?**

## Stopping rule

This pass is sufficient when adoption, task activity, output, organizational
design, worker control, training, outside options, earnings, and exit have been
separated by unit, date, method, and limits; the social discussion is bounded;
and the same-workplace missing middle is explicit. The broader 14-theme program
remains active.

## Sources

- [NBER task-level adoption](../../records/us-nber-task-level-genai-adoption-2026.json)
- [NBER coding productivity and shipped output](../../records/us-nber-ai-coding-productivity-shipping-output-2026.json)
- [NBER firm AI expectations](../../records/us-nber-firm-ai-expectations-2026.json)
- [ILO Chinese enterprise AI adoption](../../records/comparative-ilo-chinese-enterprise-ai-adoption-hybrid-work-measurement-2026.json)
- [ILO AI psychosocial work](../../records/comparative-ilo-ai-systems-work-psychosocial-autonomy-2026.json)
- [NBER AI retraining returns](../../records/us-nber-ai-worker-retraining-returns-2026.json)
- [NBER gig-worker outside options](../../records/us-nber-gig-economy-outside-options-labor-supply-2026.json)
- [ACCA global talent trends](../../records/comparative-acca-global-talent-trends-2026-ai-hiring-hybrid-work-professional-trust.json)
- [ILO work discussion](../../social-discussions/records/ai-work-control-005.json)
- [AI hiring discussion](../../social-discussions/records/atlas-acca-ai-hiring-linkedin-001.json)
- [Automation and meaning discussion](../../social-discussions/records/atlas-batch-0064-automation-meaning-linkedin-001.json)
- [Career uncertainty discussion](../../social-discussions/records/ai-work-control-003.json)
- [Workplace surveillance discussion](../../social-discussions/records/atlas-batch-0055-surveillance-linkedin-001.json)
