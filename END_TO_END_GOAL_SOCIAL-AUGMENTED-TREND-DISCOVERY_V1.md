# Long-term end-to-end goal: 14-theme research, social meaning, and new trend discovery

## The goal in one sentence

Build a long-term, US-centered 14-theme trend system that uses the existing
research atlas as its core, connects measured evidence to bounded public
discussion, and independently looks for new social trends that research has
not yet explained.

## Non-negotiable corpus scope

The unit of completion for the research-augmentation lane is the complete
atlas inventory: **2,014 machine-readable research records**, not a small
topic sample. Every atlas record must appear in the social-augmentation
coverage manifest and end in one of three auditable states:

1. **augmented** — at least one traceable public discussion item is linked to
   the exact atlas record and research question;
2. **documented access/platform gap** — the required public searches or
   authorized Creator/API calls were attempted, with the query, date, platform,
   failure mode, and reason no item could be retained; or
3. **not socially applicable** — a documented decision explains why the record
   is not a meaningful target for public-discussion augmentation.

Topic-level social waves are useful calibration and synthesis layers, but they
do not close the record-level requirement. The 14 themes organize the work;
the 2,014 records are the corpus that must be accounted for.

## Why we are doing this

The cultural-mining atlas already contains papers, surveys, public records,
company evidence, and other research about what is changing in American life.
That tells us what was measured, but it does not always tell us how people
understand the change, how they experience it, or what new concerns are
forming before researchers measure them.

Public discussion helps fill that space. It can show lived experience, common
language, disagreement, fear, hope, status, trust, and practical trade-offs.
It cannot replace research or tell us how common a view is.

The atlas already contains a broad body of papers, surveys, administrative
records, public records, company evidence, infrastructure evidence, opinion
data, and geopolitical records. The social work must augment that full body of
research rather than replace it with a small set of online examples.

We therefore need two connected but distinct work lanes:

1. **Research augmentation:** add social discussion to topics already in the
   atlas.
2. **Independent discovery:** start with public discussion and search for new
   cultural and social trends before looking for research that confirms or
   rejects them.

Keeping these lanes separate protects us from only finding social evidence
that agrees with the papers we already chose.

## Lane 1: augment the existing atlas

For each selected topic, follow this chain:

```text
paper, survey, public record, or company evidence
  -> measured finding
  -> affected people, firms, places, or institutions
  -> possible cause or practical trade-off
  -> YouTube, Reddit, LinkedIn, and X discussion
  -> lived examples, public meaning, disagreement, and repeated language
  -> response by a firm, platform, institution, or community
  -> what the discussion supports, challenges, reframes, or misses
  -> next research test
```

The social discussion must stay visibly separate from the measured finding.
For example, a Reddit story can show how a worker experiences AI screening. It
cannot prove how many workers face that problem.

## Lane 2: discover new trends independently

Start with repeated public signals, without assuming that they are true:

```text
public discussion or new phrase
  -> repeated signal across people or platforms
  -> possible cultural or social trend
  -> cross-platform and time check
  -> search for papers, surveys, records, or market evidence
  -> confirm, qualify, or reject the trend
  -> add a tested finding or an open question to the atlas
```

An independent trend should not enter the atlas merely because it is popular
online. It needs a clear question, a bounded time window, a defined group or
place, and a research check. If no suitable research exists, store it as an
open signal rather than a fact.

## Long-term 14-theme scope

The social augmentation lane follows the complete atlas inventory:

1. household room and consumption;
2. time as a hidden price;
3. consumer power and recourse;
4. platforms, data, and attention;
5. work, control, and bargaining;
6. care, health, and social reproduction;
7. housing, place, and mobility;
8. unequal exposure and status;
9. trust, identity, and cultural meaning;
10. public systems and policy feedback;
11. political judgment and collective action;
12. firm, sector, and market power;
13. infrastructure, technology, and dependency; and
14. geopolitical and state consequences.

The [long-term coverage plan](analysis/social-discussions/long-term-coverage-plan.md)
sets the wave order, atlas entry points, and delivery rules. The existing
three-topic set is only the calibration wave. It must not be treated as the
scope of the program.

For every wave, connect public discussion to an existing research record,
source-led map, subtheme, or open arrow. Preserve the distinction between a
measured population result, a public account, a repeated phrase, a counterclaim,
and an inference across sources.

## Initial calibration topics

Begin with high-value topics that already have strong research anchors and
clear public discussion:

- AI, work, hiring, skills, and worker control;
- platform attention, social-media use, and the practical cost of leaving;
- AI companionship, emotional support, trust, privacy, and dependence;
- household pressure, consumer choice, trust, and adaptation;
- cultural meaning, belonging, identity, and political action.

After calibration, rotate through all remaining themes using the coverage plan;
do not wait for a single theme to become a complete explanation before
recording the next bounded wave.

## What every social record must preserve

Each item must record:

- platform and permanent URL;
- author, account, or a clear note that it was not exposed;
- date or an honest date range;
- country, language, and group when known;
- item type: creator claim, research relay, audience reaction, lived example,
  disagreement, repeated theme, or speculation;
- engagement numbers, clearly labeled as visibility signals rather than votes
  from the whole population;
- the atlas topic and exact research anchor;
- what the item says in short words;
- access, search, sampling, ranking, moderation, and missing-context limits;
- whether the item supports, challenges, reframes, amplifies, or leaves open
  the research finding.

Do not copy private, sensitive, or unnecessary personal information. Store only
what is needed to understand and reproduce the research signal.

## What each topic must produce

For every completed topic, publish:

1. a research-to-discussion bridge;
2. normalized records for all four platforms when usable material exists;
3. an acquisition log showing searches, dates, failures, and access limits;
4. a cross-platform comparison;
5. a finding written in everyday language;
6. counterexamples and disagreement;
7. a list of what the social material does not prove;
8. the next research or acquisition test;
9. links from the main atlas and reader layer.

## What the final system should answer

For any important topic, a reader should be able to ask:

- What changed?
- Who is affected?
- What does the research actually measure?
- How do people describe the change in ordinary life?
- Where do public accounts agree or disagree?
- What choices, costs, risks, or losses are visible?
- Which claims are measured, reported, inferred, or still guesses?
- What would prove the current interpretation wrong?
- What should we investigate next?

## Completion standard

This goal is complete when:

- the social-discussion subfolder has a documented schema and repeatable
  validator;
- selected atlas topics have research anchors and bounded four-platform
  discussion records;
- creator claims, audience reactions, lived examples, disagreement,
  repetition, and speculation are not mixed together;
- each record keeps its source, date, author/account, engagement, and limits;
- topic findings explain what public discussion adds without treating it as a
  representative survey;
- counterexamples and missing evidence are visible;
- an independent trend-discovery workflow is documented separately from the
  research-augmentation workflow;
- the main atlas links to both lanes;
- the repository validation checks pass; and
- the committed repository is synchronized with its remote.

For the long-term program, completion means the workflow remains repeatable:
each of the 14 themes has a dated social wave or a documented platform/access
gap, each wave is tied to the atlas evidence and open arrows, and independent
trend candidates remain visibly separate from atlas augmentation.

For the full-corpus lane, completion additionally requires a generated
record-level coverage manifest, stable atlas-record identifiers in every
retained social link, batch-level acquisition logs, a coverage audit showing
all 2,014 records in a terminal state, and a final validator that rejects
unaccounted records. No topic-wave count may be presented as completion of the
2,014-record requirement.

The result is not a popularity counter or a news feed. It is a disciplined way
to connect what is measured, what people say, and what society may be becoming.
