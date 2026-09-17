# Gallup 2026 institutional-confidence divergence layer v1

**Checked:** 2026-09-17  
**Source:** Gallup, Confidence in U.S. Institutions  
**Field dates:** June 1–15, 2026  
**Status:** current institution-specific confidence layer; no generalized trust or behavior claim

## Why this update matters

The atlas now has a detailed press-government legitimacy layer. Gallup adds a
broader institution map and shows why “trust in institutions” should not be
collapsed into one number. Average confidence is historically low, but the
institutional pattern is sharply uneven: small business remains comparatively
strong while large technology companies are near a new low, and party
confidence varies with who holds political power.

## Recorded findings

| Surface | 2026 result | Careful interpretation |
|---|---:|---|
| Average across 14 core institutions | 27% | Near the historic low; one point above 2023’s record low |
| Large technology companies | 20% | New low in Gallup’s series, distinct from actual technology use or dependence |
| Small business | 67% | Relatively high confidence, not proof of universal local access or fair treatment |
| Republican–Democratic average gap | 13 points | Republicans report more confidence on average in the current political context |
| Presidency partisan gap | 70 points | A particularly large institution-specific contrast |

Gallup reports that 12 of 14 long-tracked institutions are at or near their
lowest points. It also identifies banks and organized labor as exceptions to
that particular low-point pattern, while small business remains much stronger
than large technology companies. These differences matter more than the
average alone.

## What this adds to the broad goal

The new layer makes four distinctions explicit:

1. **Confidence is institution-specific.** A person can distrust large
   technology companies while continuing to use their products because exit is
   costly or alternatives are weak.
2. **Confidence is politically situated.** Party gaps can reflect control of
   the presidency and institutional identity, not simply a stable personal
   trait.
3. **Confidence is not performance.** The rating does not tell us whether an
   institution delivered a remedy, protected a customer, created a job, or
   provided a public service.
4. **Confidence is not action.** Low confidence can coexist with voting,
   complaint, organizing, continued use, subscription payment, or non-use.

The comparison with the Pew press layer is useful: Pew measures judgments about
power and acceptable criticism, while Gallup measures confidence ratings. The
two sources should be read together but not pooled.

## Open arrows and next test

The next stronger design would follow the same respondent from a concrete
institutional episode—news correction, platform moderation, bank error,
consumer remedy, public-service encounter, or local-business interaction—to
confidence, attribution, continued use, switching, complaint, and political
action. The current Gallup release supplies the legitimacy benchmark but not
the episode-level mechanism.

## Boundaries

The 14-institution mean mixes public and private organizations and should not
be treated as a latent trust index. Party differences are descriptive. This
layer does not measure actual conduct, news accuracy, data practices,
institutional access, compliance, switching, turnout, vote choice, or causal
polarization. This pass downloaded no trend PDF or microdata.

**Official article:** <https://news.gallup.com/poll/712436/confidence-institutions-remains-near-time-low.aspx>

**Machine record:** [Gallup institutional-confidence record](../../records/us-gallup-institutional-confidence-2026.json)
