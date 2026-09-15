# AI can lower the barrier to cross-partisan contact, but the warmth fades quickly

**Status:** provisional preregistered experimental finding · **Checked:** 2026-09-14

## The bounded finding

A new five-study preprint tests whether a chatbot representing a political
outgroup can make cross-partisan contact easier to attempt. The evidence is
stronger than a survey association for the outcomes actually randomized: a
brief AI encounter changed immediate warmth, corrected some misperceptions,
and increased the share choosing a subsequent real outgroup conversation over
an aversive alternative. The same study also shows why the result should not
be inflated into a social depolarization claim: most immediate warmth movement
faded within a week.

```text
partisan avoidance or misperception
  -> brief outgroup-representing AI conversation
  -> warmth, belief accuracy, or willingness to try real contact
  -> [open] repeated contact, cooperation, policy judgment, turnout, or vote
  -> [open] durable trust, institutional legitimacy, or reduced conflict
```

The central result is therefore about an intervention and a short-run
behavioral opening—not about AI changing political culture at population
scale.

## What was tested

| Study | Comparison | Direct result | Boundary |
|---|---|---|---|
| S1, *N*=608 | Three-minute AI outgroup partner versus live human outgroup partner, with mortality reflection as the alternative | Participants accepted about 5.06 minutes of mortality reflection as equally aversive to the AI conversation, versus 9.65 minutes for the human conversation | Measures aversion to the experimental interaction, not ordinary political contact or a general preference for AI |
| S2, *N*=500 | Same people before and after a ten-minute outgroup-bot conversation | Outgroup warmth rose 4.3 points on a 0–100 thermometer, and belief accuracy improved | Within-person pre/post evidence can show movement but is not by itself a clean between-person causal estimate |
| S3, *N*=679 | Democratic participants: outgroup bot versus apolitical AI chat and Space Invaders | Warmth was higher after the outgroup bot than after either control, with *d* = 0.58 and 0.59 | The topic was environmental-consumption attitudes and the main sample was Democrats |
| S4, *N*=1,069 | Five-minute outgroup bot versus apolitical AI chat, then a costly real choice | 67% versus 61% chose a real outgroup conversation over mortality reflection; OR = 1.33, 95% CI 1.04–1.71 | The choice was immediate and experimental; it does not show later cooperation, voting, or policy agreement |
| S5, *N*=1,104 | Outgroup bot versus apolitical AI chat with a one-week follow-up | Immediate warmth effect *d* = 0.46; one-week preregistered mean effect *d* = 0.05, not significant | The short follow-up bounds persistence; a pooled exploratory analysis reports a small residual, but this is not a durable societal effect |

The paper reports five preregistered studies with a total of 3,960 U.S.
partisans. The public [Zenodo data-and-code package](https://zenodo.org/records/20971465)
contains de-identified analysis-ready inputs and a reproduction workflow. Its
archive SHA-256 is recorded in the [source record](../synthetic-contact-ai-source-record-v1.md).

The released Study 4 file was also checked directly using the authors' loader
filters. The reproduction retained 1,069 preregistered participants: 60.58%
of the apolitical-chat control and 67.18% of the outgroup-bot condition chose
the real outgroup conversation, matching the paper's rounded 61% versus 67%.
The [reproduction audit](../data/synthetic-contact-s4-reproduction-2026-09-14.json)
records the input archive, filters, condition counts, and the fact that this
does not reproduce withheld raw-data cleaning or the full regression.

## Why the control conditions matter

The result is not simply “talking to an AI makes people nicer.” S3 compares
political outgroup content with both an apolitical AI conversation and a
non-social game. S4 uses an apolitical AI chat as its control before the costly
choice. Those comparisons support a narrower interpretation: the outgroup
content, not merely screen time or conversational activity, contributed to the
measured short-run response in those experiments.

The study also reports that information or stereotype-disconfirming content
appeared more important than friendliness in distinguishing the outgroup-bot
conversations. That is a mechanism clue, not a universal result about how
political persuasion works. An inaccurate, one-sided, or strategically prompted
bot could produce the opposite effect.

## What this changes in the political-meaning lane

The atlas already contains survey evidence that political trust, source use,
identity, and civic engagement follow different routes. This experiment adds a
controlled bridge from an encounter to a selected action:

```text
avoidance of human outgroup contact
  -> AI representation lowers the immediate social barrier
  -> corrected perception / warmer feeling
  -> willingness to choose real outgroup contact
```

The chain is measured only inside the study's topics, prompts, samples, and
follow-up windows. It does not establish that the intervention changes a
person's vote, policy position, institutional trust, relationship network, or
political identity. It also does not tell us whether a platform, campaign, or
state actor could deploy such a system legitimately or safely.

## The persistence result is part of the finding

Immediate effects are easy to narrate as cultural change. The one-week result
forces a harder reading. In S5, the immediate effect is positive and the
one-week preregistered mean effect is small and statistically non-significant;
the paper's pooled exploratory follow-up estimates a small residual. The safe
claim is that a brief AI encounter can open a short-term window for contact,
while durable change requires repetition, reinforcement, real social
interaction, or a different intervention design.

This is a useful counterexample to both extreme stories: AI is not necessarily
just a polarization engine, but a single conversation is not a durable cure for
polarization either.

## Counterexamples and limits

- Warmth on a feeling thermometer is one dimension of affective polarization;
  it does not measure social distance, democratic norms, policy agreement, or
  willingness to accept electoral loss.
- The experiments cover U.S. online partisans and two issues, environmental
  consumption and immigration. Generalization across topics, populations,
  platforms, and model versions remains open.
- S2's pre/post design and the pooled persistence estimate require more caution
  than the between-person controlled contrasts.
- The costly choice to have a real conversation is closer to action than an
  attitude item, but it remains an experimental choice made immediately after
  treatment.
- An AI's representation of a political group can be inaccurate, biased,
  sycophantic, or strategically designed. A persuasive effect is not proof of
  truth or democratic benefit.
- The preprint is not a peer-reviewed population estimate, and the public
  package begins from de-identified analysis-ready inputs rather than all raw
  collection materials.

## Next test

Run a preregistered, version-stamped replication across both parties, more
issues, and multiple chatbot providers. Follow participants for at least one
month and measure repeated contact, belief accuracy, warmth, social distance,
policy judgment, cooperation, turnout intention, actual civic action, and
trust. Randomize disclosure, prompt framing, and human-versus-AI sequence;
audit the bot's factual representation of each outgroup; and record whether
participants can refuse, stop, or inspect the intervention.

The most important endpoint is not immediate warmth. It is whether the person
chooses and sustains a real, informed, non-coerced relationship across a
political difference.

## Sources

- [arXiv preprint](https://arxiv.org/abs/2607.02181)
- [SSRN working-paper record](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7042278)
- [Zenodo data-and-code archive](https://zenodo.org/records/20971465)
- [Source and reproducibility record](../synthetic-contact-ai-source-record-v1.md)
- [Pew news, platform, and civic-engagement layer](../../us-digital-habits-attention/pew-2025-news-civic-engagement-layer-v1.md)
- [GSS financial position, trust, and politics finding](us-cost-trust-politics-012.md)

**Evidence status:** provisional preregistered experimental evidence with a
public de-identified replication package. It supports short-run intervention
effects in the measured outcomes and a rapid-decay warning; durable political,
cultural, electoral, or institutional consequences remain open.
