# Long-term goal and handoff

**Research lane:** cultural, social, geographical, technological and
geopolitical theme mining through language, Indigenous/minority-language
digitization, AI, public services, education, accessibility, cultural data and
community governance.

**Handoff status:** paused for transfer to another project, not complete.

**Last verified commit:** `d8fc87b7` — `Add Gazetteer machine-readable reuse evidence`

**Repository:** `cultural-geopolitical-theme-mining`

**Canonical packet:**
`analysis/ROTATION-BU-INDIGENOUS-MINORITY-LANGUAGE-AI-VITALITY-2026-10-29.md`

**Canonical ledger:**
`analysis/ROTATION-BU-INDIGENOUS-MINORITY-LANGUAGE-AI-VITALITY-2026-10-29.csv`

## Long-term objective

Continuously discover, verify, compare and synthesize cultural, social,
geographical, technological and geopolitical themes, with particular attention
to how language, identity, place, data, AI and institutions interact. Convert
signals into named evidence packets and machine-readable records. Preserve
uncertainty, counterexamples, source provenance, geographic variation, power
relationships and implementation gaps. Keep the work restartable so a later
researcher can extend it without treating a launch announcement, policy promise,
benchmark, funding award or vendor claim as proof of social impact.

This is an ongoing research program. It is intentionally not declared complete.
Each rotation must nevertheless have a finite acceptance test: a bounded set of
primary or authoritative sources, explicit observations, closed and open stages,
counterexamples, a synthesis update, a next-audit queue and a committed ledger
change.

## Working question for this lane

When language datasets, AI translation, speech tools, digital archives,
mother-tongue education, geographic naming and multilingual public services are
introduced, what converts technical representation into everyday language use,
intergenerational transmission, safe access, community control and cultural
vitality?

## Core conversion chain

```text
language exclusion / low-resource data / intergenerational decline
  -> documentation / corpus / tool / education / service intervention
  -> consent / authority / quality / access / usability / correction
  -> institutional workflow / repeated use / local content / learning
  -> service completion / participation / transmission / cultural vitality
  -> durable multilingual social and digital infrastructure
```

Do not collapse adjacent stages. A model can exist without a user; a user can
interact without completing a service; a service can complete without improving
transmission; and a population indicator can change without causal attribution
to a technology.

## What has been built

The current packet contains 53 ledger rows and 60 cited source entries. It covers
the following comparative cases:

- Māori: Te Hiku Media, TalkLink AAC voices, Waikato-Maniapoto voice work,
  Te Taura Whiri/Google Maps, Say It Tika, NZGB/LINZ orthography and audio,
  Gazetteer data infrastructure, and the University of Auckland pronunciation
  coach.
- Wales: Welsh Government technology and AI work, population and daily-use
  measurement, mapping, Helo Blod, post-16 training, and health/social-care
  indicator design.
- Sámi: Ábo speech service, clinical/cultural/evaluation workstreams and
  Indigenous-led governance.
- Basque: Euskorpus/Euskorpora funding, legal implementation, corpus/model
  phases, rights and talent signals.
- Ireland: public-service language plans, technical working group, active offer,
  language-choice portability and procurement.
- Africa/East Africa: AfriEval, EAC sovereignty and Kiswahili Trust Mark,
  AI4EAC, MORENA, Vambo, Jacaranda and low-bandwidth education evidence.
- India: BHASHINI national infrastructure, Kumbh cultural service and Indian
  Railways integration pathway.
- Ghana and South Africa: local-language speech-AI pathway, human-language
  technology funding mechanism and Rori education evidence.

## Strongest current synthesis

The evidence does not support the broad claim that “AI preserves minority
languages.” It supports a narrower conversion model with distinct gates:

1. community authority and consent;
2. usable and rights-cleared data;
3. language-, dialect- and task-specific quality;
4. deployable product or public resource;
5. institutional workflow and accessibility;
6. correction, escalation and accountability;
7. repeated user behavior and trust;
8. service, learning, health, cultural-production or economic outcomes;
9. intergenerational transmission and durable vitality.

The most important cross-case pattern is that different actors close different
gates. Community governance can exist without product quality. Public funding
can exist without deployment. A public demo can exist without completed service
transactions. A positive learning result can exist without local-language use.
An audio archive can exist without dialect coverage, metadata or reuse. A
population estimate can exist without causal attribution.

## Important counterexamples to preserve

- The 2017 Say It Tika campaign generated more than 67,000 corrections but did
  not initially produce the promised technical pronunciation fix.
- NZGB/LINZ later converted some of the signal into 629 standardized approvals
  and 24 corrigenda, while approximately 5,700 names were deferred. Spelling,
  official naming and pronunciation remain different stages.
- The current Google Maps voice is an English voice for Māori place names, not a
  full te reo Māori Maps experience; dialect variation is explicitly outside the
  release.
- LINZ audio production has grown substantially, but selection, metadata,
  dialect coverage, external reuse and user outcomes remain under-audited.
- Welsh technology outputs and population indicators do not by themselves prove
  higher-intensity institutional use or intergenerational transmission.
- Rori provides a measured low-bandwidth learning signal, but the evidence does
  not prove that local-language interaction caused the result.
- Vendor-reported customer, API-volume and engagement claims must remain
  separate from independently measured customer impact.

## Exact next-audit queue

### Priority 1 — Māori Gazetteer crosswalk

Construct a small, reproducible sample—not a national scrape—using stable
Gazetteer name IDs. For each sampled name, record:

- Gazetteer name and official/unofficial status;
- Māori name/macron form and English or dual-name form;
- history/origin and NZGB authority fields;
- whether audio exists and the audio URL or stable identifier;
- recording/version metadata if exposed;
- whether the same name appears in Google Maps and how it is pronounced;
- any correction or amendment history;
- dialect/standard-pronunciation treatment;
- license and permitted downstream reuse;
- evidence of education, navigation or public-service use.

The output should be a new small crosswalk ledger, not an assertion that the
whole system has been audited. If the audio index is not publicly enumerable,
record that as an observability limitation and preserve the exact query paths
attempted.

### Priority 2 — University of Auckland pronunciation coach

Find evidence of release, university-system integration, learner evaluation,
teacher workload change, repeated use, pronunciation improvement and acceptable-
range governance. Separate the $1 million grant and one-million-user ambition
from observed adoption or learning outcomes.

### Priority 3 — Māori AAC deployment

Obtain the TalkLink phase-two cohort, device compatibility, repeated daily use,
communication success and cultural-participation outcomes. Keep named-user
examples separate from cohort-level evidence.

### Priority 4 — Rotate geography

After the Māori audit, select one under-covered language or region outside the
current cases. Prefer a case with a public service, education, health,
geographic-data or accessibility deployment and at least one counterexample.
Do not keep expanding the Māori packet indefinitely without rotation.

## Required evidence record for every new case

Every new row in the CSV must contain:

1. stable `source_id`;
2. source title;
3. unit or geographic scope;
4. stage;
5. direct observation, with claims attributed;
6. stage closed;
7. stage still missing or unproven;
8. evidence status (`high`, `medium`, `low` or equivalent with explanation);
9. next test.

Use direct observations rather than conclusions. Record denominators, dates,
geography, dialect, sample selection, data rights, correction route, user
eligibility, implementation support and independent corroboration whenever
available. Use `medium` or `low` when the source is provider-reported,
aspirational, undated, incomplete or not independently evaluated.

## Source hierarchy

Prefer, in order:

1. official datasets, gazettes, APIs and administrative records;
2. peer-reviewed or clearly identified research with methods and limitations;
3. community or Indigenous institutions with named governance and artifact
   details;
4. government plans, procurement and implementation records;
5. organizational impact reports with denominators and methods;
6. vendor pages, investor claims, press coverage and social posts as leads or
   self-reported evidence only.

Use secondary reporting when it documents a counterexample or historical failure,
but identify it as secondary and seek the underlying institutional record.

## Restart procedure

From the repository root:

```bash
cd /home/mehta/git-repo/cultural-geopolitical-theme-mining
git status --short
git log -5 --oneline -- analysis/ROTATION-BU-INDIGENOUS-MINORITY-LANGUAGE-AI-VITALITY-2026-10-29.md
python3 - <<'PY'
import csv
p = 'analysis/ROTATION-BU-INDIGENOUS-MINORITY-LANGUAGE-AI-VITALITY-2026-10-29.csv'
with open(p, newline='') as f:
    rows = list(csv.reader(f))
assert all(len(row) == 9 for row in rows)
print(len(rows)-1, 'data rows;', len(rows[0]), 'columns')
PY
```

Read this handoff, then the end of the narrative packet—especially
`Cross-case synthesis` and `Next-audit queue`. Inspect current external sources
before relying on prior claims because this is a refreshable research program.

Use explicit paths with `git add --sparse`; unrelated parallel changes are
present in the worktree and belong to other research lanes. Never stage the
whole repository for this lane.

## Handoff acceptance test

The lane is safely handed off when:

- the two canonical packet files are present and validated;
- this handoff identifies the objective, method, current state and next tests;
- the current commit is pushed to the remote;
- unrelated worktree changes remain unstaged;
- no completion claim is made for the long-term objective.

This acceptance test is satisfied for the handoff commit that adds this folder.
