# Pew teens, social media, and AI chatbots 2025 layer v1

**Checked:** 2026-09-13 · **Status:** official teen survey extraction

## Why this layer matters

The existing digital lane is mostly adult news, platform, and chatbot
evidence. This Pew survey adds a defined adolescent subgroup and places social
platform intensity beside chatbot adoption. That matters for the program's
questions about attention, cultural meaning, family mediation, school use,
privacy, and the practical ability to stop or switch.

Pew surveyed 1,458 US teens ages 13–17 from September 25 through October 9,
2025, through Ipsos' probability-based KnowledgePanel. The survey was weighted
to teens living with parents. The [machine-readable record](../../records/us-pew-teens-social-ai-2025.json)
preserves the full-sample denominator, subgroup universes, PDF hash, and
question-specific boundaries.

## Direct evidence

Sixty-four percent of teens report ever using AI chatbots and 28% report daily
use; 16% use them several times a day or almost constantly. ChatGPT is used by
59% of teens, compared with 23% for Gemini and 20% for Meta AI. These figures
show rapid normalization of an instrumental or entertainment technology, not
attachment or dependence.

Social-media use is also frequent. Sixty-one percent report visiting TikTok
daily, 55% Instagram daily, and 46% Snapchat daily. Twenty-one percent say
they are on TikTok almost constantly and 20% say the same of YouTube. Across
five measured platforms, 36% use at least one almost constantly. The TikTok
near-constant estimate rose from 16% in 2022 to 21% in 2025, while the report
says the corresponding YouTube, Instagram, Snapchat, and Facebook estimates
changed little. This is a repeated population comparison, not a panel of the
same teenagers.

Access and use are socially patterned. Chatbot use is 68% among ages 15–17
and 57% among ages 13–14. It is 66% among teens in households earning at
least $75,000 and 56% among those under $30,000. Daily chatbot use is 35% for
Black teens, 33% for Hispanic teens, and 22% for White teens. Such differences
can reflect schoolwork, device access, family rules, language, product fit,
or reporting; they should not be converted into a simple capability hierarchy.

## Mechanism under test

```text
platform or chatbot availability
  -> repeated encounter, information, schoolwork, entertainment, or support
  -> time allocation, interpretation, trust, and social dependence
  -> ability to inspect, refuse, switch, or leave
  -> family, school, firm, regulator, or public response
```

This layer directly measures encounter and self-reported use. It partially
measures frequency and product choice. It does not measure logged time,
recommendation exposure, content accuracy, emotional reliance, family
oversight, school rules, data practices, or an attempted exit. The [adult Pew
AI layer](pew-2026-ai-daily-life-control-layer-v1.md) and [FTC AI-companion
inquiry](../../records/us-ftc-ai-companion-inquiry-2025.json) provide adjacent
adult and institutional evidence, but are not the same population or study.

## Cultural and power interpretation

The bounded interpretation is that digital life is becoming ordinary in two
different ways at once: social platforms occupy recurring attention, while
chatbots enter information and schoolwork routines. Those are not the same
kind of relationship. A daily information tool may be easy to replace; a
social platform can carry peer connection, identity, status, and audience.
The survey does not tell us which relationship is harder to leave.

The subgroup results also complicate a single “digital divide” story. Higher-
income teens report more chatbot use overall, while Black and Hispanic teens
report higher daily use than White teens. The difference could be access,
purpose, family mediation, school context, or product choice. It is evidence
for differentiated pathways, not a conclusion about harm or advantage.

## Counterexamples and limits

- High frequency can coexist with instrumental, bounded use.
- Lower reported use can reflect restricted access rather than greater agency.
- Platform frequency is not total attention time; substitution across apps is
  not observed.
- Self-reported use does not show what the system recommended or whether the
  teen trusted it.
- The survey does not measure privacy practices, monetization, emotional
  attachment, learning outcomes, mental health, or political persuasion.
- Parent participation and household weighting make this a specific teen
  population, not all minors or independent youth.

## What would change the finding

The interpretation would weaken if diary or device-log data showed that
reported frequency did not correspond to meaningful exposure, or if repeated
respondents showed that chatbot and platform use were mostly short-lived and
easily substituted. It would strengthen if longitudinal data linked a defined
product encounter to time allocation, trust, reliance, school or family
outcomes, and an observed attempt to stop or switch, with subgroup-specific
alternatives and safeguards measured.

## Next test

Pair the Pew teen survey with product-level safety and data disclosures,
school-policy records, parent/teen matched measures, and longitudinal time or
wellbeing data. Preserve separate units: teen respondent, parent/teen dyad,
platform account, product interaction, and institutional response. The next
test is practical exit and substitution—not another prevalence count.

## Reproducibility

- [Pew report](https://www.pewresearch.org/internet/2025/12/09/teens-social-media-and-ai-chatbots-2025/)
- [Pew methodology](https://www.pewresearch.org/internet/2025/12/09/teens-social-media-ai-methodology/)
- [Report PDF](https://www.pewresearch.org/wp-content/uploads/sites/20/2025/12/PI_2025.12.09_Teens-Social-Media-AI_REPORT.pdf)
- PDF SHA-256: `6d2c3552c715b990607d68b970d8f495f28f88b81839751d2307f031563643e1`

