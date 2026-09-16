# Cultural, social, and geopolitical theme mining

This workspace studies what is changing underneath visible events, with a broad focus on US societal, cultural, consumer, financial, political, institutional, firm, infrastructure, and geopolitical life.

It starts with research from [Harvard Business School Working Knowledge](https://www.library.hbs.edu/working-knowledge) and the [National Bureau of Economic Research](https://www.nber.org/). It may add US public records, company filings, surveys, court records, financial data, consumer data, demographic data, and careful reporting when those sources help test a finding. International sources are comparison and context unless a project says otherwise.

The output is not a news feed and not a pile of summaries. Each project should move through this chain:

```text
source
  -> claim
  -> method and evidence
  -> mechanism
  -> who gains, loses, or changes behavior
  -> cultural and social meaning
  -> geopolitical or institutional effect
  -> company and sector exposure
  -> finding with limits and tests
```

The writing rule is simple: use ordinary words, show the causal steps, name the evidence, separate fact from inference, and say what would prove us wrong.

For a synchronized handoff check, run `python3 scripts/validate_long_term_publication_gate.py`.

## The broad program

The project is explicitly not a one-household study. It maps 14 program
themes across people, consumers, workers, households, firms, places,
institutions, infrastructure, and states. The [full broad-program reader map](site/us-broad-program-map.html)
is the simplest overview. The [end-to-end recovery brief](END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md)
is the restart document after a crash, and the [big-picture synthesis](analysis/us-big-picture-synthesis.md)
records the current cross-source interpretation.
The [current-status audit](analysis/US-BROAD-CURRENT-STATUS-AUDIT_V1.md)
records the 14-theme coverage, recent depth, open arrows, and next queue in one
place.
The [broad program focus brief](BROAD-PROGRAM-FOCUS_V1.md) is the short
restart document: it keeps societal, cultural, political, consumer, firm,
institutional, infrastructure, and geopolitical trend mining as the governing
goal, with household work treated as one evidence lane.
For a compact review of the writeups and active themes, use the [current themes
review packet](REVIEW-PACKET_CURRENT-THEMES_V1.md), then open the [trend
observations index](site/us-trend-observations.html) for the underlying records.
The [recurrent-source vintage watchlist](analysis/US-RECURRENT-SOURCE-VINTAGE-WATCHLIST_V1.md)
keeps release dates, refresh actions, revision boundaries, and account-gated
acquisition dependencies visible across research cycles.

The common question is:

```text
condition or decision
  -> available alternatives and money/time/access/control change
  -> people and organizations respond
  -> cost, risk, data, ownership, and power are redistributed
  -> cultural meaning, trust, political action, firm capacity, or state leverage changes
```

Household data are one measurement layer inside this chain. They must not
replace the firm, institutional, cultural, place, infrastructure, or
geopolitical layers.

## What this is for

We want to find slow forces before they become obvious:

- changes in work, status, trust, family life, health, and identity;
- shifts in who controls money, data, labor, land, energy, and infrastructure;
- new links between household behavior, company strategy, state power, and conflict;
- changes that look local but spread through markets, institutions, or culture;
- the hidden cost of policies and technologies that appear helpful on the surface.

## First sources

HBS Working Knowledge is used for accessible explanations of faculty research and topic discovery. Its current collections include managing the business, artificial intelligence, entrepreneurship, economics and global commerce, strategy and innovation, work, technology, and human behavior. NBER is used for working papers, research programs, paper metadata, public-use data, and later checks against the underlying study.

NBER working papers are early research circulated for discussion. They are useful evidence, but they are not treated as settled fact without checking the design, limits, later publication, and other evidence.

## Folder map

```text
raw/          saved source pages, paper metadata, files, and access notes
indexes/      source and topic indexes
analysis/     finding cards, evidence ledgers, theme maps, and project memos
manifests/    source, license, method, and coverage manifests
templates/    repeatable plain-language research forms
scripts/      collection, validation, and MD-to-HTML tools
site/         published HTML pages
```

Start with [START-HERE.md](START-HERE.md). The governing specification is [END_TO_END_GOAL_V1.md](END_TO_END_GOAL_V1.md). The working method is in [RESEARCH-METHOD.md](RESEARCH-METHOD.md), and the first topic queue is in [analysis/seed-topic-queue.md](analysis/seed-topic-queue.md).

To read the generated publication locally, run `python3 -m http.server 8000`
from the repository root and open `http://localhost:8000/site/index.html`.
Serve from the repository root (rather than using `--directory site`) so the
published pages can also link to their source Markdown, machine-readable
records, and audit documents under `analysis/`.
After rebuilding pages, run `python3 scripts/validate_published_site_links.py`
to check the published relative-link topology.
Run `python3 scripts/validate_trend_provenance.py` to verify that every trend
observation retains an HTTP(S) source URL and a structurally valid SHA-256
retrieval token.
Run `python3 scripts/audit_source_registry_coverage.py` to distinguish source
families that are merely registered from those referenced in the analysis
corpus; its report is `analysis/US-SOURCE-REGISTRY-COVERAGE-AUDIT_V1.md`.
