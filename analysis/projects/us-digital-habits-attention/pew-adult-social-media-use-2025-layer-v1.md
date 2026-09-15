# Pew adult social-media use 2025 layer v1

**Checked:** 2026-09-13 · **Status:** official adult survey extraction

## Why this layer matters

The teen platform/chatbot layer needed an adult comparator with the same discipline around reach, frequency, subgroup patterning, and exit-cost limits. Pew's 2025 adult report supplies that comparator, while its separate frequency survey prevents platform prevalence from being mistaken for daily exposure.

Pew surveyed 5,022 US adults from February 5 through June 18, 2025 using address-based sampling and a web, mail, and phone protocol. A separate American Trends Panel survey of 5,123 adults from February 24 through March 2, 2025 measured frequency. The [machine-readable record](../../records/us-pew-adult-social-media-2025.json) preserves both denominators and the source-page hash.

## Direct evidence

YouTube reaches 84% of US adults, Facebook 71%, Instagram 50%, TikTok 37%, WhatsApp 32%, and Reddit 26%. Since 2021, TikTok, Instagram, WhatsApp, and Reddit grew in reported adult reach while YouTube and Facebook remained comparatively stable. In the separate frequency sample, about half of adults visit Facebook and YouTube daily; 24% visit TikTok daily and 10% visit X daily.

The adult distribution is socially patterned. Instagram use is 80% among adults ages 18–29 and 19% among those 65 and older; it is 55% among women and 44% among men, and 62% among Hispanic adults versus 45% among White adults. TikTok daily use is roughly 50% among 18–29-year-olds and 5% among adults 65 and older. These are descriptive distributions, not evidence that a demographic group has a single culture or political response.

## Mechanism under test

```text
platform availability and social fit
  -> repeated visits and differentiated audience formation
  -> information, identity, commerce, or belonging
  -> trust, attention allocation, and perceived switching cost
  -> firm, household, institutional, or political response
```

The report observes self-reported reach and frequency. It does not observe logged minutes, content or recommendation exposure, monetization, privacy practices, persuasion, or an attempted exit. The arrow from broad reach to cultural or political power remains open.

## Interpretation

The adult pattern is not one unified “social media” phenomenon. YouTube and Facebook are broad infrastructure; Instagram and TikTok are more age-concentrated; WhatsApp and Reddit add different social and informational pathways. Platform substitution and audience sorting can therefore produce different cultural effects even when aggregate reach is stable.

The age and race/ethnicity distributions also mean that national averages can hide who is most exposed to a given platform. That matters for later work on news, consumer discovery, identity, and political voice. It does not justify treating platform membership as a proxy for beliefs or behavior.

## Limits and next test

- Self-reported use is not device-logged exposure or total attention.
- Repeated cross-sectional changes are not individual trajectories.
- Reach does not identify content, recommendation, monetization, or political influence.
- Daily use can be purposeful, brief, relational, or replaceable.
- The frequency sample is separate from the platform-reach sample.

Next, link adult platform distributions to news-use, creator/commerce, and institutional-response records while preserving platform, respondent, content, and outcome units. The high-value question is whether differentiated reach translates into durable changes in trust, spending, identity, or political action—and for whom.

## Reproducibility

- [Pew report](https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/)
- Source-page SHA-256: `80b714a2bfdd7052caf635bb0682b8f5e27c5a0a7a77f2d337fd5f64e8f99e3b`
