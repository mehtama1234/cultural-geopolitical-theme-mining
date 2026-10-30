# Rotation AC: Synthetic information, verification and public trust

**Date:** 2026-10-29  
**Lane:** AI-generated information / digital culture / civic trust / fraud  
**Status:** Tier 2 mechanism plus source boundary

## Research question

As people encounter AI summaries, synthetic images, generated text and
impersonation, what converts exposure into verification, belief, action,
correction or withdrawal of trust?

## Conversion chain

```text
synthetic or AI-mediated content appears
  -> person recognizes or cannot recognize its provenance
  -> verification effort or trusted intermediary
  -> belief, sharing, click, purchase or civic action
  -> correction, harm, adaptation or institutional response
  -> repeated trust, skepticism, avoidance or exit
```

The audit must keep five units separate: content exposure, recognition,
verification behavior, downstream action and later correction. A survey about
what people value or a technical standard for provenance does not close the
behavioral chain.

## Evidence packet

| ID | Source and direct observation | Stage closed | Stage still open |
|---|---|---|---|
| AC1 | [Pew Research Center on detecting AI-generated content](https://www.pewresearch.org/wp-content/uploads/sites/20/2025/09/PS_2025.9.15_AI-and-its-impact_report.pdf) reports that 76% of U.S. adults say it is very or extremely important to tell whether images, video and text were made by AI or people; few feel confident they can do so. | Publicly expressed importance and self-confidence | Actual recognition, verification and downstream action by person/content |
| AC2 | [Pew on AI summaries in search](https://www.pewresearch.org/short-reads/2025/10/01/americans-have-mixed-feelings-about-ai-summaries-in-search-results/) reports that about half of Americans who encountered AI summaries had at least some trust in the information. | Exposure and self-reported trust among exposed users | Accuracy, source inspection, click, correction and later reliance |
| AC3 | [Pew browsing-data analysis](https://www.pewresearch.org/data-labs/2025/05/23/what-web-browsing-data-tells-us-about-how-ai-appears-online/) observes AI-related content in real browsing data while warning that tracked web browsing excludes apps, untracked devices, television and offline encounters. | Measured web exposure in a defined panel | Total exposure across media and what the person believed or did |
| AC4 | [NIST synthetic-content transparency report](https://www.nist.gov/publications/reducing-risks-posed-synthetic-content-overview-technical-approaches-digital-content) surveys provenance, labeling, watermarking, detection, testing and auditing approaches. | Technical option set and risk categories | Deployment coverage, interoperability, user comprehension, evasion and remedy |
| AC5 | [FTC 2025 imposter-scam data](https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-data-show-people-reported-losing-3-point-5-billion-imposter-scams-2025) reports $3.5 billion in reported losses to imposter scams in 2025, across channels including text, phone, email, social media and search. | Reported fraud loss and channel distribution | Which cases used generative AI, causal attribution, prevention and recovery |

## Stage audit

| Observed signal | Safe interpretation | Prohibited leap |
|---|---|---|
| People say detection is important | Provenance matters to public expectations | People can reliably detect synthetic content |
| People report trust in an AI summary | Some exposed respondents express trust | The summary was accurate, acted upon, or caused a belief change |
| Browsing data show AI-related exposure | AI-mediated encounters are present in a tracked web sample | All media exposure, comprehension or behavioral impact is measured |
| NIST catalogs provenance and detection methods | Technical and governance mechanisms exist | Labels are complete, understood, tamper-proof or effective |
| Imposter losses rise | Impersonation is a materially reported fraud problem | AI caused the losses or the same intervention would prevent them |

## Bounded finding

> Synthetic-information governance has an expectation-to-verification gap:
> people value provenance and encounter AI-mediated information, while public
> evidence remains weak on whether labels, provenance or detection tools produce
> reliable verification, safer action and recoverable harm.

This does not imply that AI content is uniformly deceptive or that provenance
tools are ineffective. It identifies the missing conversion from a technical or
policy feature to a person’s situated decision and later correction.

## Named-case refresh

These cases connect synthetic content to verification, platform controls,
institutional response and different forms of harm:

### AC6 — FTC voice-cloned family emergency scam

The FTC describes a case in which a scammer used a cloned voice to convince an
older couple that the caller was their grandson and needed money for bail; a
bank official alerted them before they lost nearly $9,400. This closes a
content-to-trust-and-financial-action route and shows why a familiar voice is
not a sufficient identity signal. The case does not establish how often such
scams succeed, whether the voice was fully AI-generated, or whether the FTC’s
recommended independent callback prevented harm for a wider population.

### AC7 — Michael Smith AI-assisted streaming fraud

The U.S. Department of Justice reports that Michael Smith pleaded guilty after
using hundreds of thousands of AI-generated songs and automated bots to create
billions of apparently genuine streams and obtain more than $10 million in
royalties. This is a platform-integrity case: content generation and synthetic
engagement combined to defeat the meaning of a popularity signal. It closes
the synthetic-content-to-economic-harm route, but the case is an enforcement
account and does not reveal the full detection timeline, all platform controls
or whether ordinary listeners were influenced by the fake popularity.

### AC8 — NIST provenance and labeling case studies

NIST summarizes case studies including OpenAI’s provenance classifier for
DALL-E images, BBC audio and on-screen disclosures for face-swapped interviews,
and Adobe’s C2PA implementation in Firefly. NIST emphasizes that these are
different mechanisms, that label effects depend on modality and use case, and
that the examples were submitted by participating entities. This closes a
technical-deployment route, not user verification or safer action. It also
creates a counterexample to treating a provenance mark as a universal remedy:
coverage, display, comprehension, stripping and trust remain unobserved.

### AC9 — DOJ AI-generated intimate-image harm

The Eastern District of New York describes charges against Cornelius Shannon
and Arturo Hernandez for allegedly publishing thousands of AI-generated sexual
images and videos depicting real people, including public figures and
non-public individuals. This makes synthetic content’s harm pathway concrete:
the key outcome is not whether viewers can identify the image as synthetic, but
whether victims can obtain removal, legal remedy, safety and reputational
recovery. The defendants are charged, not convicted; the case does not measure
prevalence, platform response time or victim recovery.

### AC10 — CISA election-integrity deepfake scenario

CISA’s trust-and-social-cohesion exercise uses a political-disruptor scenario
in which a deepfake video and manipulated voice circulate around an election
and trigger public reaction before the target can respond. The exercise is not
evidence that the scenario occurred exactly as described; its value is in
mapping the response sequence—rapid circulation, attribution uncertainty,
institutional denial, community reaction and possible correction. It closes a
preparedness and systems-response route while leaving real-world exposure,
belief, turnout, violence and correction effectiveness open.

### Case-ledger conclusion

The refresh closes portions of synthetic voice trust, fake engagement,
provenance deployment, intimate-image harm and election-response planning. It
also sharpens the core boundary: authenticity metadata, labels, detection tools
and institutional statements are interventions in the chain, not proof that a
person recognized content, withheld action, recovered from harm or restored
trust. The decisive ledger remains:

`content/channel → provenance visibility → verification/intermediary → belief or action → correction/removal → financial/civic/reputational recovery`

No case yet closes that chain across the same content, user and community over
time.

## Cultural and geographical interpretation

Trust is not only a property of content. It is a relationship among the
speaker, platform, language, community, institution and consequence. A label
may be legible to a highly connected user and invisible to someone receiving a
forwarded message in a different language or through a trusted community
channel. A local journalist, faith leader, family member or public agency can
function as a verification intermediary, but may also become an impersonation
target.

The geographical question is where verification capacity resides: who has
bandwidth, media literacy, trusted local institutions, time to cross-check and a
reachable remedy after harm. The political question is who bears the cost when
the content is wrong: the viewer, the impersonated institution, the platform,
the election/community, or the financial victim.

## Counterexamples and limits

- Synthetic content can be transparent, benign or useful; “AI-generated” is not
  equivalent to false.
- Human-generated content can also be inaccurate, manipulative or impersonating.
- Self-reported trust is not the same as belief, sharing, click-through or
  financial/civic action.
- Provenance can be absent because content was created outside a participating
  system, stripped by transformation, or encountered in a channel that does not
  display it.
- FTC imposter-loss data are reported losses, not a causal estimate of AI use or
  total harm; underreporting and channel ambiguity remain material.

## Promotion decision

Retain as a Tier 2 mechanism. Promote only after a named platform or community
study links content exposure to visible provenance, verification behavior,
downstream action, correction/recovery and subgroup or place differences.

## Next test

Build a content-level ledger with provenance state, language/channel, trusted
intermediary, user verification step, action, correction and recovery. Pair
platform telemetry or browsing data with consented interviews and a named
community setting so the atlas can distinguish reach from belief and belief from
consequence.
