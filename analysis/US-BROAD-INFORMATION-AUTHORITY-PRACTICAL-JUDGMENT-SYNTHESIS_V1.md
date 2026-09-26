# Information authority and practical judgment in the United States v1

**Checked:** 2026-09-24  
**Status:** source-led cross-domain synthesis; separate surveys and populations, not one respondent path  
**Question:** when people need to judge a health, financial, public, political, or AI-mediated question, which authority routes are available, what makes a route usable, and where does the evidence stop before a decision or outcome?

## The pattern visible across the source corpus

The available sources do not support a story in which one institution has been
replaced by platforms or AI. They show a more consequential, uneven pattern:
people use different mixes of institutional, professional, personal, platform,
and AI routes depending on the question. Use, trust, confidence, perceived
accuracy, ability to verify, privacy knowledge, and action are different
surfaces. A person can use a source they distrust because it is fast, free,
private, familiar, or the only available starting point.

```text
question, risk, or need
  -> available authority routes (professional / agency / news / family-peer / platform / AI)
  -> access, cost, convenience, privacy, and topic fit shape a route
  -> reported use, confidence, trust, or verification difficulty
  -> unobserved claim checking, deliberation, decision, care, purchase, vote, or action
  -> unobserved material, health, civic, or trust outcome
```

The first three stages are source-supported in different settings. The latter
two are usually not observed. That distinction matters: a large audience,
reported source use, or even a stated confidence rating is not evidence that a
person followed advice, received good advice, or experienced a better result.

## Different questions bring different source mixes

Pew's March 2026 topic-specific survey shows that a "main source" shifts by
subject. News media were named by 51% for foreign policy, 46% for immigration,
44% for the economy, and 37% for health care. Government sources were jointly
most common with news media for Social Security (31% each). Social media and
friends/family remained named routes, but their shares varied by topic. This is
evidence of topic-specific routing, not a hierarchy of accuracy or a measure of
what any respondent did next. [Source record](records/us-pew-information-source-topic-diversity-2026.json).

| Need surface | Directly measured route or judgment | What it does *not* establish |
|---|---|---|
| Health information | Providers, people with similar health issues, social media, and AI chatbots are all reported sources; conflicts and difficulty judging accuracy/trust are common | Claim accuracy, provider access, a clinician conversation, care seeking, treatment, adherence, cost, or health outcome |
| Health/wellness influence | Professional, coach, entrepreneur, and lived-experience identities coexist in large-account profiles; audience use and mixed trust are reported | Credential validity, sponsorship, recommendation quality, purchase, diagnosis, or health outcome |
| Financial guidance | Internet research, family, professionals, and AI are nonexclusive guidance routes; stressed and fulfilled groups report different mixes | Recommendation quality, decision influence, fee/loss avoidance, improvement, or recovery |
| Political/public information | Government-information trust and difficulty evaluating candidate and AI claims are separately reported | Information accuracy, exposure, correction, persuasion, turnout, or legitimacy change |
| AI assistant use | Task-specific platform routing, comparative trust, policy knowledge, reported protective tools, and hypothetical privacy valuations are measured among users | Telemetry, actual payment, data disclosure/loss, causal privacy protection, durable switching, or dependence |

The table is a comparison of measurement surfaces, not a pooled rate. Every row
uses a different questionnaire, population, topic frame, and denominator.

## Health: plural use does not resolve authority

The 2025 Pew health-information survey of 5,111 U.S. adults reports that 85%
get health information from providers at least sometimes and 66% from people
with a similar health issue; 36% report social-media use and 22% AI-chatbot use.
At the same time, 50% say judging accuracy is at least somewhat difficult, 76%
see conflicting information at least sometimes, and 54% say it is at least
somewhat difficult to know what to trust when information conflicts. Among
users, provider information is rated highly accurate by 65%, compared with 7%
for social-media health information. These are source-use and perceived-
credibility measures, not a clinical validation exercise. [Health-information
record](records/us-pew-health-information-source-trust-2025.json).

Pew's separate health/wellness-influencer study makes the authority cues more
complicated rather than resolving them. Of 6,828 prominent influencers in its
profile analysis, 41% self-described as health professionals, 31% as coaches,
and 28% as entrepreneurs. Forty percent of U.S. adults reported ever getting
health/wellness information from influencers or podcasts. Among consumers of
those sources, 10% trusted all or most of the information, 65% trusted some,
and 24% trusted not too much or none. Self-description, audience reach, and
reported understanding are not verification of expertise, commercial incentives,
or medical benefit. [Influencer-authority record](records/us-pew-health-wellness-influencer-authority-2025.json).

Read alongside the NBER health-care trust and care-seeking record, these sources
support a bounded social subtheme: health authority is distributed across
professional, peer, platform, and institutional routes, while the ability to
settle a conflict remains uneven. They do **not** create a same-person chain
from exposure to health outcome. [Care-trust record](records/us-nber-trust-health-care-seeking-behavior-2026.json).

## Financial judgment: support routes are social as well as digital

Among U.S. adults who sought financial guidance, Gallup/Edward Jones reports
73% used internet research, 35% family, 32% professional financial advisors,
and 18% AI tools. The sources are nonexclusive. Financially stressed
guidance-seekers reported family use more often than financially fulfilled
guidance-seekers (43% versus 19%) and AI use more often (21% versus 15%). Yet
no more than 30% of U.S. adults reported at least some confidence in AI's
financial expertise, and only 3% reported a great deal of confidence.

This is not evidence that family or AI solves financial stress, nor that either
replaces professionals. It identifies an important consumer and cultural
subtheme: under financial pressure, practical judgment can depend on a blended
support system whose human and digital parts carry different confidence,
availability, and likely cost profiles. The source does not observe the question
asked, the recommendation, a transaction, debt, loss, savings, or recovery.
[Financial-guidance record](records/us-gallup-financial-guidance-ai-trust-2026.json).

## AI: convenience, experience, and control are not the same thing

The AI-assistant study is limited to a weighted sample of 1,999 U.S. adult AI
users, but it supplies a more detailed platform-choice layer. About 43% reported
intentionally routing tasks to more than one assistant; platform choice varied
by task. Over 80% reported concern about conversation-data use, roughly 60% did
not know whether their assistant trained on conversations, and only 18% had paid
for a better-privacy plan. The study associates knowledge of a training policy
more strongly with reported protective-tool use than a one-point increase in
concern; its embedded experiment estimates hypothetical willingness to pay,
not purchases.

The safe inference is not that informed users are protected. It is that concern,
knowledge, price, task sensitivity, and defaults can occupy separate positions
in a practical-control route. The record does not observe actual privacy harm,
policy comprehension, platform retention, or a causal effect of knowledge.
[AI choice/trust/privacy record](records/us-ai-assistant-platform-choice-trust-privacy-2026.json).

The related cookie-consent experiment provides a mechanism, with an important
scope boundary: an interface can alter observed consent choices when options
are more or less accessible. Its comparative experimental result should not be
recast as a U.S. population rate or as proof of informed consent. [Cookie-
consent record](records/comparative-nber-cookie-consent-choice-architecture-2025.json).

## Public and political judgment: trust and verification are distinct burdens

AP-NORC's 2026 State of the Facts survey reports lower trust in federal
government information than in 2024 on several issue surfaces, including
inflation/cost of living (18% versus 26%), health care (16% versus 26%), and
elections/politics (13% versus 22%) expressing a great deal or quite a bit of
trust. In the same 2026 survey, 37% said it is difficult to know whether
candidate information they encounter is true, 43% said it is difficult to tell
whether candidates' statements are true, and only 20% said it is easy to verify
AI information.

These are related but noninterchangeable social conditions. Trust concerns the
perceived credibility of an institution or source; verification difficulty
concerns the work of judging a claim. A person may distrust government
information yet be able to verify a particular claim, or trust an institution
but struggle to assess AI-generated material. The survey does not audit truth,
observe search time, track correction, or link these attitudes to voting or
political action. [AP-NORC record](records/us-apnorc-state-of-facts-information-trust-2026.json).

## What is the actual cross-source trend?

The defensible trend is **fragmented practical authority**: a growing set of
questions is answered through mixed routes, while the work of comparing,
verifying, protecting data, and turning information into action remains visible
only in pieces. This has social, cultural, consumer, health, platform, and
political dimensions:

| Subtheme | Evidence-supported meaning | Boundary that must stay attached |
|---|---|---|
| Topic-specific authority | Different questions lead people toward different declared primary sources | A main source is not exclusive use, trust, accuracy, or decision reliance |
| Relational fallback | Family, peers, and people with similar experience are part of health and financial information routes | Reported use does not prove advice quality, support adequacy, or outcome |
| Platform-mediated authority | Influencers, social media, AI, and consent design shape the route through which information or control is encountered | Reach, self-description, interface choice, or experimentation does not prove influence, informed choice, or harm |
| Verification as a hidden cost | Conflict, accuracy difficulty, candidate-claim difficulty, and AI verification difficulty reveal effort before action | Perceived difficulty is not observed time, misinformation prevalence, or a causal barrier |
| Knowledge-control gap | Privacy concern and actual knowledge/action can diverge | Cross-sectional associations do not show that disclosure knowledge causes protection |

## The next valid evidence step

The useful next study is not another generic trust percentage. It is a
question-level, time-ordered panel or field design that records:

1. the actual question or decision context and stakes;
2. every source encountered, including search/ranking/default exposure;
3. cost, waiting, privacy, language, access, and social-support constraints;
4. what was believed, checked, discussed, ignored, or acted on;
5. expert or factual evaluation appropriate to the topic;
6. the resulting care, financial, consumer, civic, or political outcome; and
7. later trust, switching, correction, and willingness to use the route again.

It must retain counterexamples: people who use AI or social media carefully and
benefit, people who trust professionals but cannot access them, people who use
family advice alongside formal advice, and people who report high concern but
take no protective action because price or defaults constrain their options.

## Source set

- [Pew topic-specific information-source record](records/us-pew-information-source-topic-diversity-2026.json)
- [Pew health-information source/trust record](records/us-pew-health-information-source-trust-2025.json)
- [Pew health/wellness influencer-authority record](records/us-pew-health-wellness-influencer-authority-2025.json)
- [NBER health-care trust/care-seeking record](records/us-nber-trust-health-care-seeking-behavior-2026.json)
- [Gallup financial-guidance/AI-trust record](records/us-gallup-financial-guidance-ai-trust-2026.json)
- [AI-assistant choice/trust/privacy record](records/us-ai-assistant-platform-choice-trust-privacy-2026.json)
- [AP-NORC State of the Facts record](records/us-apnorc-state-of-facts-information-trust-2026.json)
- [Comparative cookie-consent choice-architecture record](records/comparative-nber-cookie-consent-choice-architecture-2025.json)
