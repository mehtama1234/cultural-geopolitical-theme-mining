# A written AI agreement can give workers procedural power without proving lived control

**Status:** provisional institutional-governance finding · **Checked:** 2026-09-14

## The bounded finding

An archived 2020 collective agreement between IBM Central Holding GmbH and its
group works council shows a concrete way that worker representation can be
built into the introduction of workplace AI. The agreement requires a human
decision at the end of an AI-supported process, assigns systems to a risk
spectrum, requires increasing levels of transparency as risk rises, creates a
correction loop for wrong recommendations, and gives the works council review
and monitoring rights.

The safe interpretation is:

> **Worker power over AI can be designed as a procedure: classify the risk,
> disclose the inputs and confidence where required, provide a route to correct
> an error, and give worker representatives information and participation
> rights. A written procedure is evidence that these protections were agreed as
> rules. It is not evidence that every system was covered, that the rules were
> enforced, or that workers experienced less surveillance, discrimination, job
> loss, or stress.**

This is an institutional case record, not a representative survey of IBM
workers and not a US estimate.

## What the agreement actually says

The source is titled *Konzernbetriebsvereinbarung über die Einführung und den
Einsatz von Systemen der Künstlichen Intelligenz / Artificial Intelligence*.
It identifies IBM Central Holding GmbH as the employer and the company's group
works council as the employee-side party. The page gives a version date of
25 June 2020 and a signing date of 30 July 2020. WageIndicator classifies it
under data processing and databases in the private sector.

| Design element | Rule in the agreement | Why it matters | What remains unknown |
|---|---|---|---|
| Human decision | AI is described as preparing data-supported decisions; it may not replace the final human decision | A formal human-in-the-loop boundary is stated | Whether a human could meaningfully disagree, or merely approve an AI recommendation |
| Risk classification | Five categories range from no risk to very high risk; recommendations or automatic personnel decisions without a benefit/risk-minimization rationale are placed in the highest category | Governance effort is tied to possible worker harm and its probability | How many systems fell into each category, and how classifications were challenged |
| High-risk exclusion | Category 5 systems may not be introduced or used | A written prohibition is stronger than a general ethics aspiration | Whether any system was rejected, redesigned, or moved into a lower category |
| Transparency | For higher categories, workers should receive information about the inputs, their influence on the result, and the confidence level | Workers and representatives can potentially contest an opaque recommendation | Whether the information was understandable, timely, and supplied in practice |
| Correction loop | From category 2 onward, a process must exist to report and correct false recommendations; category 4 adds rapid correction and direct access to the AI Ethics Council | Error correction is treated as an operational requirement, not only a complaint after harm | Error counts, response times, correction rates, and whether corrections changed the model |
| Fairness | The employer must demonstrate testing for discrimination and fairness, including methods such as Watson OpenScale | A documented test obligation creates an auditable control point | The tests, protected groups, thresholds, results, and independent review |
| Worker representation | The works council evaluates systems, participates in the next steps, and may inspect data-quality, non-bias, transparency, purpose, and objective information | Collective representation is embedded before and during deployment | The council's resources, technical expertise, access quality, and actual leverage |
| AI Ethics Council | A cross-functional team includes data privacy, business units, the works council, the central representative body for disabled employees, and HR labor relations | Governance is distributed across worker, privacy, operational, and HR functions | Membership over time, meeting records, decisions, appeals, and independence |
| Employment transition | If AI removes a job or changes a worker's activity, the agreement points to an equal job where possible and retraining where needed | The document links technical change to redeployment and skills | Whether comparable jobs and training were actually available, and for whom |

The agreement also says that worker rights remain intact and that a worker is
entitled to correction when an AI recommendation is demonstrably wrong. That is
an important procedural promise, but “demonstrably wrong” still leaves an
evidentiary question: who can see enough of the system to demonstrate the error?

## The accompanying interview moves the case one step toward implementation

A 2022 BTQ Kassel interview with Frank Remers, identified as a speaker of the
IBM Group Works Council specialist committee for personnel data systems, adds a
reported practice layer. He says IBM was using AI in internal call centers and
for recommendations about training and possible career paths. He also says
that a global system recommending salary increases for managers, and a system
estimating the probability of voluntary resignation, had not been used for
employees in Germany at that time.

This is stronger than a purely aspirational policy document because it names
systems reportedly in use and systems reportedly withheld. It still does not
close the implementation arrow:

```text
written rule
  -> reported German deployment boundary
  -> named tools and withheld tools
  -> unknown worker exposure, decisions, corrections, and outcomes
```

The interviewee also says the agreement helps control introduction for German
employees but cannot necessarily prevent global development teams from creating
systems. That distinction is analytically important: a local works-council
agreement can govern deployment in its jurisdiction without governing the
upstream model, vendor, or product-development pipeline.

## The deeper theme: control is a chain, not a slogan

The document makes a useful distinction between several kinds of control that
are often collapsed into “responsible AI”:

```text
system introduction
  -> risk classification
  -> information and explanation
  -> worker / works-council review
  -> recommendation or decision
  -> challenge and correction
  -> model or outcome change
  -> review of the changed system
```

The agreement explicitly covers most links in this chain. It is especially
strong as a design for entry, review, and correction. It is much weaker as
evidence about the final links because the public page does not provide system
inventories, implementation records, worker complaints, model audits, meeting
minutes, correction logs, job outcomes, or health outcomes.

That distinction matters for the wider work-control theme. A firm can have a
formal human-review rule while workers still experience a recommendation as
mandatory. A fairness test can exist while the relevant group is not measured
well. A retraining clause can exist while the available replacement work is
lower paid, geographically inaccessible, or never offered. The agreement gives
us a testable institutional mechanism; it does not settle the outcome.

## What this adds to the cross-source atlas

### From abstract principles to an observable governance architecture

Many AI discussions use broad terms—human oversight, transparency, fairness,
ethics—without specifying who can act when a system is wrong. This agreement
turns those terms into potential observations:

- a named decision boundary;
- a risk taxonomy linked to documentation requirements;
- a prohibited highest-risk class;
- a defined error-reporting and correction loop;
- a named worker-representation body;
- inspection rights over data quality, bias analysis, purpose, and transparency;
- an employment-transition and training route.

Those are useful coding dimensions for comparing collective agreements,
company policies, public-sector rules, and legal regimes. They are not a score
of “good AI governance.” The dimensions should remain separate until
implementation evidence is available.

### A bridge between labor power and technical system behavior

The agreement places the works council near the point where technical design
becomes a workplace consequence. That creates a measurable bridge between
labor institutions and AI system behavior:

```text
collective representation
  -> access to system purpose, data, and risk information
  -> ability to contest classification or recommendation
  -> correction, redesign, or refusal
  -> worker exposure to surveillance, discrimination, job change, or retraining
```

The first three stages are directly documented in the agreement's rules. The
last stage requires implementation and worker-level evidence. This is why the
case should inform the atlas's work-control theme without being used as proof
that AI improved or harmed IBM workers in Germany.

### A comparative question for the US program

The relevant US comparison is not “does the United States have an AI ethics
policy?” It is more specific:

1. Who receives advance notice of an AI system used in employment?
2. Who can inspect the purpose, inputs, validation, and error rates?
3. Can a worker contest a recommendation without risking retaliation?
4. Is there a required human decision, and does that person have authority to
   disagree?
5. Is there a correction log and a deadline for action?
6. Can a worker representative stop, redesign, or refuse a high-risk system?
7. What happens to workers whose jobs or tasks change?

The US evidence base should compare these institutional rights with actual
deployment, complaints, audits, job transitions, and worker outcomes. A policy
document alone should remain in the institutional-design layer.

## Counterexamples and limits

- A written agreement can be strong on paper and weak in enforcement.
- “Human decision” can mean meaningful judgment, or a rubber stamp; the text
  alone cannot distinguish them.
- Transparency about inputs does not necessarily reveal training data,
  vendor logic, proxies, or the practical reason a recommendation was made.
- A fairness test can miss groups that are not measured, small samples, or harms
  that arise after deployment.
- A correction route is not equal to effective remedy if workers lack time,
  information, protection, or a trusted escalation path.
- The agreement is one IBM Germany case from 2020. It cannot represent all
  German workplaces, all IBM operations, or current practice in 2026.
- WageIndicator's catalog fields include many “No” or blank entries for
  unrelated labor topics. Those fields should not be read as a finding that
  the agreement lacked every protection; the detailed AI clauses are the
  relevant evidence here.

## Next test

Build a small comparative corpus of worker-governance documents and code each
one on the separate dimensions above. For every document, seek at least one
implementation artifact:

- system inventory or deployment register;
- risk-classification record;
- worker or works-council review record;
- bias or quality audit;
- correction and appeal log;
- retraining or redeployment outcome;
- worker interview or survey evidence.

Then compare cases with similar written safeguards but different observed
outcomes. The key question is not whether a firm has adopted the language of
responsible AI. It is whether workers and their representatives can convert
that language into information, refusal, correction, and material protection.

## Sources and reproduction

- [WageIndicator archived agreement page](https://wageindicator.org/de-de/arbeiten-in-deutschland/tarifvertrag/konzernbetriebsvereinbarung-uber-die-einfuhrung-und-den-einsatz-von-systemen-der-kunstlichen-intelligenz-artificial-intelligence)
- [Machine-readable acquisition record](../data/wageindicator-ibm-ai-framework-acquisition-v1.json)
- [BTQ Kassel interview](https://www.btq-kassel.de/interview_frank_remers/)
- [BTQ interview acquisition record](../data/btq-ibm-ai-framework-interview-acquisition-v1.json)
- The acquired HTML page is 681,137 bytes, HTTP 200, SHA-256 `37d16c3e02a17a4698d5d3a23ae608829b5f1f1e0ecdf32db8470c15d2e6d3`
- [AI work-control project README](../README.md)
- [BLS labor-context finding](ai-work-control-039.md)
- [OFR financial-system visibility finding](ai-work-control-071.md)

**Evidence status:** one archived German collective-agreement text plus one
worker-representative interview; strong evidence for stated institutional
design and reported deployment boundaries; no independently audited
implementation, enforcement, worker-outcome, representative-survey, or US
estimate established.
