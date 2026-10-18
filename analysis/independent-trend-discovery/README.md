# Independent social-trend discovery

This is the second lane of the cultural-mining program. It starts with public
discussion and only later checks papers, surveys, records, or market data.

It must not begin with an existing atlas research claim. That separation helps
us notice new concerns instead of only collecting social proof for ideas we
already believe.

## Workflow

```text
public phrase, story, or concern
  -> repeated signal across items or platforms
  -> provisional trend candidate
  -> cross-platform and time check
  -> search for research and official evidence
  -> confirm, qualify, or reject
  -> publish a tested finding or keep an open question
```

## Discovery rules

- Start with the words and concerns people use, not a research topic.
- Keep a candidate separate from a proven trend.
- Require at least two platforms or two independent accounts before calling a
  signal repeated.
- Record both supporting and counter-signals.
- Do not use engagement as the number of people who believe something.
- Do not add a research anchor until the candidate has been frozen with a
  date, window, phrase, and source list.
- After the independent discovery pass, search for research that could confirm,
  qualify, or reject the candidate.

## Files

- `discovery-protocol.md` — the repeatable process and review gate.
- `candidate-queue.json` — provisional trends waiting for research checks.
- `research-check-log.md` — the later, independent evidence check.
- `research-check-summary.md` — plain-language results from the first checks.
- `counter-signals.md` — evidence that pushes against a candidate.
- `schema.json` — record contract.

Run the validator with:

```text
python3 scripts/validate_independent_trends.py
```

The initial candidates are deliberately qualified. The research checks support
parts of each pattern, but none proves that the candidate is widespread,
causal, or uniquely new.
