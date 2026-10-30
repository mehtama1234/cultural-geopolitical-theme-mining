# Rotation GT — agentic AI, accountable action and reversibility

**Date:** 2026-10-29  
**Status:** Tier 1 bounded distinction plus Tier 2 conversion question  
**Research lane:** agentic AI, software identity, delegated authority, security, human oversight and public legitimacy

## Why this rotation exists

AI agents are moving from generating text or recommendations toward planning,
calling tools, changing records, communicating externally and acting for users
or organisations. The language of “autonomy” can hide the operational question:
who authorised the action, what did the agent know, what did it change, who can
stop or reverse it, and who bears the cost when it fails? This is distinct from
ordinary model quality or AI adoption. The object of study is delegated action
in a social and geographical environment.

## Research question

When an AI agent receives authority to act across software, data and real-world
workflows, under what conditions does it produce useful, safe and accountable
service while preserving human agency, traceability, correction, security,
redress and equitable access rather than silent error, hijacking, exclusion or
unrecoverable harm?

## Conversion chain

```text
goal / instruction / user authority / agent identity / tool access
  -> agent interprets context, plans and takes bounded actions with logs and controls
  -> person or institution receives a correct, timely and understandable result
  -> errors can be detected, stopped, reversed and remedied without shifting burden to the user
  -> authority, trust, safety and access remain legitimate across people and places
```

## Evidence snapshot

1. NIST describes AI agents as systems that can act autonomously for extended
   periods and interact with external systems and internal data. The promised
   utility is therefore connected to tool access and environmental action, not
   only conversational quality. This establishes a capability signal, not a
   reliable public outcome.
2. NIST's 2026 analysis of security RFI responses reports broad agreement that
   agents create novel security threats and that traditional cybersecurity
   practices need adaptation. Respondents identified government guidance,
   information sharing and standards as useful. The evidence supports a
   transition from model evaluation to agent-system security, but not a claim
   that deployed agents are safe.
3. NIST's agent-hijacking work shows how malicious instructions embedded in
   external data can cause an agent to take unintended actions. The mechanism is
   especially important where an agent can read sensitive information and write
   to external systems. A successful benchmark or mitigation does not establish
   that a named user avoided loss or received remedy in production.
4. NIST's identity-and-authority concept paper identifies identification,
   authorisation, auditing, non-repudiation and prompt-injection controls as
   open implementation questions. Agent identity is therefore a governance
   primitive: without it, responsibility for a tool call or state change may be
   difficult to assign.
5. The European Commission's AI Act FAQ explains that “AI agent” is not a
   separate legal category, but agents can fall within existing AI-system and
   GPAI obligations. It highlights transparency, prohibited manipulation,
   systemic-risk controls and future high-risk requirements. Legal coverage is
   a route to oversight, not proof of human understanding, reversibility or
   equitable service.
6. OECD's 2026 practitioner study examines how organisations are developing,
   deploying and governing agentic AI across regions and sectors. Its purpose is
   to strengthen the empirical base around applications, benefits, challenges
   and governance. The emerging evidence remains early and heterogeneous;
   practitioner adoption should not be promoted to durable productivity,
   worker autonomy, safety or public value without named deployment evidence.

## Bounded proposition

**An AI agent, tool call, workflow automation, delegated permission, identity
standard, safety evaluation, human-oversight policy, audit log or regulatory
classification is not by itself correct service, safety, accountability,
reversibility, human agency, fair access, productivity, worker benefit or public
legitimacy.** An agent that completes a task, sends a message, changes a record,
executes a transaction or passes a test does not establish that the action was
authorised, understood, proportionate, secure, reversible, contestable or
fairly remedied when it affected a named person or community.

## Cultural and geographical interpretation

Agentic authority is situated in an organisation, jurisdiction and relationship
of dependence. A person with reliable connectivity, language support and a
human escalation route may experience the same agent differently from a rural
user, migrant, disabled person, low-literacy worker or community served only by
an automated channel. An agent can also cross borders through cloud systems,
vendors and external tools, while responsibility remains locally unclear.

The key cultural question is whether people remain recognised as principals,
workers, citizens, patients, customers or knowledge holders, rather than being
reduced to inputs in an autonomous workflow. Trust requires understandable
disclosure, meaningful permission, human fallback, correction, appeal and a
record of who decided. Reversibility is partly technical and partly social:
refund, restoration, apology, compensation and institutional learning may be
needed after an automated action.

## Counterexamples and cautions

- Bounded agents can reduce repetitive work, improve accessibility and help
  people navigate complex systems; the packet does not claim autonomy is always
  harmful.
- Human oversight can be nominal if operators lack time, authority, context or
  the ability to stop the agent. “Human in the loop” is not a closed outcome.
- Logs support traceability but do not guarantee that a person can understand
  the decision, challenge it or obtain correction.
- Security controls may reduce hijacking while leaving bias, poor data quality,
  unequal access, vendor lock-in or harmful objectives unchanged.
- A failed action may be technically reversible but materially irreversible if
  it causes lost income, missed care, public exposure, immigration consequence,
  reputational damage or safety risk.

## Promotion decision

Promote as **Tier 1 bounded distinction**: official technical, regulatory and
policy sources identify agent-specific security, identity, authority,
transparency and oversight needs. Promote as **Tier 2 conversion question**:
agentic-ai-to-accountable-action-and-reversibility, requiring named evidence
from authorisation through tool execution, user result, error detection,
reversal, remedy and subgroup experience.

## Six-stage closure table

| Stage | What to observe | Current boundary |
|---|---|---|
| Signal | agent deployment, product claim, standard, RFI, regulation or workflow pilot | Official evidence is strong for capability growth and governance attention |
| Mechanism | identity, permissions, context, tool access, prompt injection, logging and oversight | Threats and controls are well described; field implementation varies |
| Operation | named agent takes a bounded action in a real system for a named principal | Early organisational cases exist; comparable production records are limited |
| Material consequence | correct service, completed task, avoided error, cost/time effect or harm | Same-user later outcomes and reversibility are not yet systematically established |
| Meaning | confidence, dignity, worker agency, fairness and institutional legitimacy | Principles and risk concerns are visible; lived trust after failure is under-measured |
| Power | authority allocation, stop/exit rights, contestation, remedy and vendor dependence | Formal oversight is developing; realized control across users and jurisdictions remains open |

## Next test

Select three contrasting deployments: an internal enterprise agent with write
access, a public-service or customer-service agent, and a high-stakes workflow
agent with human escalation. For each, log one action from instruction to tool
call, output, user notice, human review, error, stop/reversal, complaint and
remedy. Record identity, permission scope, data accessed, language and
accessibility, time-to-correction, financial or social loss, fallback route and
whether responsibility was assigned to the provider, deployer, operator or
user.

## Named deployment and human-escalation refresh

### 7. Air India AI.g: large-scale service access with customer choice and escalation

Microsoft's customer story reports that Air India's AI.g handles roughly
40,000 customer queries per day across more than 1,300 question types. The
company reports more than 13 million conversations resolved with a 97% success
rate, with about 3% escalated to human agents; it also reports that roughly
half of customers choose AI.g while the other half prefer human service. Air
India is testing agents that orchestrate refund workflows across systems.

This is a named, high-volume operation case with an explicit human fallback and
customer-choice signal. It does not establish whether “success” means correct
resolution, whether refunds are actually reversible, how language, disability,
older passengers or disrupted travellers fare, or whether the company-reported
figures have independent validation. The refund orchestration is a planned
workflow transformation, not evidence of completed financial remedy.

Source: [Microsoft, Air India AI.g customer-service case](https://www.microsoft.com/en/customers/story/26047-air-india-azure-openai-in-foundry-models).

### 8. PEBA: four autonomous agents entered a benefits workflow with measurable service effects

Microsoft reports that Public Employee Benefits Administrators (PEBA) put four
Copilot Studio agents into production: case management, case intent, knowledge
management and quality evaluation. The Case Management Agent turns shared-mailbox
emails into enriched cases, drafts responses and manages workflow; the Quality
Evaluation Agent assessed 983 cases and conversations after go-live, compared
with about 50 interactions in each earlier manual sample. The reported effects
were a 9% reduction in resolution time and a 6% response-time improvement
against a two-business-hour service level; PEBA also reports accepting a new
client that would increase membership 41% without planned additional staff.

This closes a concrete multi-agent workflow and measurement architecture, but
not the authority chain for each case, correction after an incorrect benefit
record, member notice, accessibility, worker workload, denial or appeal, or the
counterfactual behind the staffing claim. The case is a vendor-published
customer story and should be treated as operational evidence, not independent
benefit-administration evaluation.

Source: [Microsoft, PEBA autonomous-agent case](https://www.microsoft.com/en/customers/story/27179-public-employee-benefits-administrators-dynamics-365-customer-service).

### 9. Included Health: clinical risk stratification and 100% pilot review

A 2026 case study describes Included Health's clinically governed AI digital
assistant for patient guidance. The design classified inquiries into emergency,
high-risk and standard-risk tiers, blocked AI advice and escalated concerning
symptoms to human clinicians, and reviewed 100% of clinical interactions during
the pilot.

This is a stronger safety architecture than a generic chatbot because the
agent's authority is bounded by risk classification and human escalation. It
still does not establish diagnostic accuracy, patient comprehension, missed
escalations, time-to-care, language or disability equity, clinical outcomes,
data retention, compensation or what happens when a patient cannot reach a
human. A pilot audit rate is not the same as long-run reversibility after harm.

Source: [NEJM Catalyst, clinically governed AI digital assistant case](https://pubmed.ncbi.nlm.nih.gov/42418625/).

### 10. Microsoft Store Assistant: multi-agent orchestration included human transfer

Microsoft's engineering case study describes a Store Assistant launched in
October 2024 using a coordinator agent and specialist skills for product
discovery, technical support, phone-number retrieval and human transfer. It
reports several million annual chats, a four-star satisfaction rating, 142%
revenue versus forecast, a 31% purchase-conversion increase and 46% fewer human
transfers as of March 2025. The design used page context and explicit routing to
human sales assistance rather than treating every request as fully autonomous.

The case closes a useful bounded-action pattern: agent orchestration can include
clarification and human transfer. The metrics are vendor-reported and do not
show whether fewer transfers meant better self-service or hidden failure,
whether customers understood they were dealing with an agent, how vulnerable
users fared, or whether a wrong purchase, privacy exposure or account action
could be reversed with remedy.

Source: [Microsoft, Store Assistant case study](https://devblogs.microsoft.com/agent-framework/customer-case-study-microsoft-store-assistant-bringing-multi-expert-intelligence-to-microsoft-store-chat-with-semantic-kernel-and-azure-ai/).

## Source boundary

The official record is strong for agent capability, novel security threats,
identity and authorisation gaps, regulatory applicability and the need for
testing and governance. It remains weak for comparable, same-unit evidence
that agentic systems produce durable benefits with equitable access and real
reversibility in production. This is a Tier 2 research opportunity, not a
promoted performance claim.

## Sources

- NIST, [AI agent security RFI analysis](https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-ai).
- NIST, [AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure).
- NIST, [Agent hijacking evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations).
- NIST, [Identity and authority of software agents](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents).
- European Commission, [AI Act FAQ: how AI agents are addressed](https://ai-act-service-desk.ec.europa.eu/en/faq?page=0&trk=public_post_comment-text).
- OECD, [Agentic AI in organisations](https://www.oecd.org/en/publications/agentic-ai-in-organisations_1257a26f-en.html).
