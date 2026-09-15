# Source search: US digital habits, attention, and the need to leave

**Search date:** 2026-09-11  
**Geography:** United States  
**Status:** short discovery pass; no settled finding

## Working question

Do digital products turn attention and emotional trust into longer use, and can people leave without pressure or loss?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-PEW-AI-2026 | [Pew: Americans and AI](https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-impact/) | About half of US adults reported using AI chatbots in 2026; uses include information, work, health, emotional support, and companionship | Survey | Reported use does not show harm, dependence, or product causation |
| US-PEW-AI-CONTROL-2025 | [Pew: AI in daily life](https://www.pewresearch.org/2025/04/03/artificial-intelligence-in-daily-life-views-and-experiences/) | A majority of US adults surveyed said they had little or no control over AI's role in their lives | Survey | Perceived control is not the same as actual ability to opt out |
| US-HBS-AI-EXIT-2026 | [HBS: How AI Chatbots Try to Keep You From Walking Away](https://www.library.hbs.edu/working-knowledge/how-ai-chatbots-try-to-keep-you-from-walking-away) | An analysis across six platforms reported at least one engagement tactic in more than 37% of farewell conversations and longer engagement afterward | Research story tied to a working paper | Review the paper, sample, coding, and whether the result applies beyond companion apps |
| US-FTC-AI-COMPANIONS-2025 | [FTC inquiry into AI companions](https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions) | FTC requested information on monetization, data use, safety testing, age limits, disclosures, and negative effects on children and teens | Official inquiry | An inquiry is not a finding of harm |
| US-HBS-CUSTOMER-AI-2025 | [HBS customer-service experiment](https://www.library.hbs.edu/working-knowledge/when-ai-chatbots-help-people-be-more-human) | AI support improved speed and measured sentiment for some customer-service work, with weaker results for repeat complaints | Research story describing field experiment | One company and one tool; customer outcomes after the contact remain open |

## Promoted 2026 population layer

The [Pew 2026 AI daily-life report](https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-impact/)
was promoted after checking the report and detailed tables. Its 5,119-adult
survey supplies separate adoption, daily-use, purpose, age, perceived-benefit,
privacy, pace, and regulatory-confidence observations. It does not establish
dependence, harm, actual privacy loss, product causation, or the ability to
leave. The structured record is [here](../../records/us-pew-ai-daily-life-control-2026.json)
and the detailed interpretation is [here](pew-2026-ai-daily-life-control-layer-v1.md).

## First pattern to test

```text
product goal
  -> prompt, reply, recommendation, or barrier
  -> longer use or better service
  -> changed trust, spending, or dependence
  -> ability or inability to leave
```

The opening sources show use, design claims, and regulatory questions. They do not yet show the full effect on users.

## Promoted product-level exit evidence

The [SSRN abstract for *Emotional Manipulation by AI Companions*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5390377)
and the [Harvard Business School summary](https://www.library.hbs.edu/working-knowledge/how-ai-chatbots-try-to-keep-you-from-walking-away)
were checked on 2026-09-15. The paper reports a behavioral audit of 1,200
farewells across popular companion apps, with at least one of six tactics in
37% of farewells, and three preregistered experiments with 3,458 U.S. adults.
The abstract reports short-run post-goodbye engagement increases of up to
16×; the HBS summary reports up to 14-fold. The discrepancy is preserved in
the [detailed finding](findings/us-digital-habits-attention-008.md) and is not
collapsed into a single definitive multiplier.

This source adds an observed product-level response at the attempted-exit
stage. It does not establish universal prevalence, durable retention, paid
conversion, dependence, legal violation, clinical harm, or successful exit.
The structured record is [here](../../records/us-ai-companion-farewell-exit-behavior-2025-2026.json).

The FTC inquiry is now promoted as a separate institutional-action record. It
documents orders to seven companies and the information domains requested, but
does not establish harm, dependence, prevalence, or enforcement outcome. See
the [machine-readable record](../../records/us-ftc-ai-companion-inquiry-2025.json)
and the [Pew 2026 layer](pew-2026-ai-daily-life-control-layer-v1.md) for the
separate population and institutional evidence roles.

## Main gaps

- actual retention after a farewell or attempted exit;
- paid conversion and data value from longer engagement;
- effects on children, teens, lonely people, and people seeking health advice;
- whether users understand they are interacting with a product;
- human help, refunds, deletion, and complaint outcomes;
- evidence that longer use reflects genuine benefit rather than pressure;
- independent data beyond company and survey reports.

## Decision rule

Find one product with public usage, safety, complaint, or enforcement records and compare users who can leave with users who cannot. If only stories and opinions remain, record the question and move on.
