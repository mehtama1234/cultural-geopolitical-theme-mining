# Synthetic contact with AI and cross-partisan openness: source record v1

**Checked:** 2026-09-14  
**Status:** provisional preprint with public de-identified replication package  
**Geography:** United States experiment participants  
**Study:** Lira, Castelo, Puntoni, and Toubia, *Synthetic Contact with AI
Reduces Cross-Partisan Animosity*

## Source and reproducibility

The paper is available as [arXiv:2607.02181](https://arxiv.org/abs/2607.02181)
and as an [SSRN working paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7042278).
The authors publish a [Zenodo data-and-code archive](https://zenodo.org/records/20971465)
with a de-identified public ZIP, analysis scripts, a compiled manuscript, and a
`make reproduce` workflow. The archive was downloaded during this pass.

| Acquisition item | Value |
|---|---|
| Archive file | `synthetic-contact-public.zip` |
| Archive size | 3,829,540 bytes |
| SHA-256 | `41841857b5684f5fb427fd18db8f899ac38f01e27afa30a88e129b047c993abf` |
| Zenodo DOI | `10.5281/zenodo.20971465` |
| Archive release | version 1.0.0; published June 27, 2026 |
| Reproduction scope | de-identified analysis-ready inputs and code; raw chatbot transcripts and some raw collection inputs are withheld |

The package README says that the released data and code reproduce the paper's
reported results, while noting that some inputs are pre-computed or derived
from withheld raw exports. That makes the package a strong reproducibility
artifact for the released analyses, not proof that every collection step can
be independently rerun from raw data.

### Study 4 reproduction check

The released `release/data/s4.parquet` was independently read with the
authors' exclusion logic from `release/code/s4__load.R`. After retaining the
preregistered `mortality_time == 3` and bot-check screen, the analysis frame
contains 1,069 participants. The apolitical-chat control has 332 of 548
participants choose the real outgroup conversation (60.583942%); the
outgroup-bot condition has 350 of 521 choose it (67.178503%). This reproduces
the paper's rounded 61% versus 67% result. The [reproduction audit](data/synthetic-contact-s4-reproduction-2026-09-14.json)
preserves every filter and the archive checksum.

This check reproduces the released descriptive shares, not the full logistic
regression or the withheld raw-data cleaning and transcript pipeline. The
experiment-specific boundary therefore remains unchanged.

## Study architecture

The five preregistered studies use distinct units and outcomes. They should
not be collapsed into one “polarization effect.”

| Study | N | Design and comparison | Primary outcome | Reported result |
|---|---:|---|---|---|
| S1 aversion | 608 | AI outgroup partner versus live human outgroup partner | Mortality-reflection minutes accepted as the alternative to a three-minute immigration conversation | AI 5.06 minutes versus human 9.65; Cohen's *d* = 0.34 |
| S2 within-person | 500 | Same respondents before and after a ten-minute outgroup-bot conversation | Outgroup warmth and belief accuracy | Warmth +4.3 points on a 0–100 thermometer; *d* = 0.37; *p* < .001 |
| S3 three-arm | 679 | Outgroup bot versus apolitical AI chat versus Space Invaders; Democrats | Outgroup warmth | *d* = 0.58 and 0.59 versus the two controls; *p* < .001 |
| S4 behavioral choice | 1,069 | Five-minute outgroup bot versus apolitical AI chat, followed by a costly real choice | Choose real outgroup conversation instead of mortality reflection | 61% control versus 67% outgroup-bot; OR = 1.33, 95% CI 1.04–1.71, *p* = .025 |
| S5 persistence | 1,104 | Outgroup bot versus apolitical AI chat with one-week follow-up; Democrats | Outgroup warmth immediately and one week later | Immediate *d* = 0.46; one-week *d* = 0.05, not significant (*p* = .16) in the preregistered mean model |

S1 and S4 include immigration as a more identity-salient behavioral topic;
S2, S3, and S5 use environmental-consumption attitudes for belief and warmth
measures. The paper reports that S4 moved a costly choice toward a later real
cross-partisan conversation, but the choice is still a study outcome, not
evidence of voting, organizing, policy agreement, or durable reconciliation.

## Method and boundary

The study uses random assignment in the between-subject experiments and a
within-person pre/post comparison in S2. The controls are important: S3
compares an outgroup-representing chatbot with both an apolitical chatbot and a
non-social game, and S4 compares the outgroup bot with an apolitical AI chat.
The paper also reports a one-week follow-up in S5; most of the immediate warmth
effect faded, with the pooled follow-up leaving a small residual.

The participants are online U.S. partisans recruited through CloudResearch
Connect. S1, S3, S4, and S5 have different party compositions; S3 and S5 are
Democrat-only in the main treatment descriptions, while S1 and S4 include both
parties. The estimands are therefore study-specific. The paper is a preprint,
not an established population trend or a peer-reviewed consensus result.

The public package contains analysis-ready de-identified files and code, but
the README notes that direct identifiers and raw chatbot transcripts are
removed, and that several cleaning or embedding inputs are withheld or
pre-computed. This is preserved as a reproducibility qualification.

## What this source adds to the atlas

It tests a link that the existing Pew, ANES, GSS, and platform layers could
only leave open:

```text
partisan avoidance and misperception
  -> brief AI-mediated outgroup encounter
  -> warmth, belief accuracy, and willingness to attempt real contact
  -> [open] repeated contact, cooperation, policy judgment, voting, or action
```

The result is unusually useful for the atlas because it measures both meaning
(warmth and perceived outgroup positions) and a subsequent costly choice. It
also provides a negative persistence result: immediate attitude movement is
not the same as a durable week-later change.

## Open questions

- Does repeated synthetic contact produce durable warmth or merely repeated
  short-run movement?
- Does the bot represent the outgroup accurately across topics, parties,
  languages, model versions, and political contexts?
- Does choosing a real conversation lead to a respectful interaction,
  cooperation, changed policy judgment, or no further change?
- Who controls the prompt, training data, moderation, and political framing?
- Can a platform deploy the intervention for civic benefit while preserving
  disclosure, user choice, privacy, and non-manipulation?
- Could an inaccurate or biased outgroup representation reinforce rather than
  correct misperceptions?

**Evidence status:** randomized experimental evidence for short-run openness,
warmth, and selected belief/behavior outcomes in online U.S. partisan samples;
the work is a provisional preprint. Societal-scale depolarization, durable
cooperation, electoral behavior, institutional trust, and safe governance are
not established.
