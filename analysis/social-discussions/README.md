# Social-discussion complement

This subfolder adds public discussion to the research atlas. It does not treat
posts, comments, videos, or engagement as survey results. Each item is kept as
a traceable discussion signal and is linked back to a research claim, topic,
and mechanism.

## First bounded wave

The first wave covers three atlas topics:

1. **AI and work control** — whether AI changes productivity, job access,
   skills, autonomy, workload, or early-career opportunity.
2. **Platform attention and exit** — whether people can reduce use, leave, or
   substitute platforms when status, information, or social connection makes
   exit costly.
3. **AI companionship and trust** — whether AI becomes an emotional or social
   substitute, support route, or source of dependence and uncertainty.

The initial observation window is **2025-10-17 through 2026-10-17**. The
selection is a pilot, not a claim that these are the only important topics.
They were chosen because the atlas already contains research records and open
arrows for each one, and because each has observable public discussion across
multiple platforms.

## Evidence rule

For every platform item, record:

- canonical URL, platform, author/account, publication date, and retrieval date;
- the item type: creator/post claim, audience reaction, lived example,
  disagreement, repetition, or speculation;
- the linked research claim and mechanism;
- engagement only as a platform-native visibility signal, never as prevalence;
- access, ranking, moderation, search, language, and sampling limits.

The discussion layer can show what is being said, repeated, contested, or made
salient. It cannot by itself establish population prevalence, causal effect,
representativeness, or the truth of a claim.

## Files

- `topic-registry.md` — selected topics and research anchors.
- `acquisition-log.md` — queries, successful finds, and platform gaps.
- `records/` — normalized one-item-per-record evidence.
- `findings/` — topic-level cross-platform synthesis after enough records are
  collected.

Validate the normalized records with:

```text
python3 scripts/validate_social_discussions.py
```

The first normalized records are deliberately small. They preserve links and
bounded summaries rather than copying full posts or comments.
