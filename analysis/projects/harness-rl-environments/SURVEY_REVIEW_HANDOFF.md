# Survey review handoff

## Remote survey reviewed

`mehtama1234/harnessresearchsurvey` at commit `0c43a1a57e3fe3d96950ebd2d528a9c624cd5aca`.

The repository's README says the canonical narrative survey moved to the
`system-designs` repository. The remaining executable finance harness is still
valuable as a concrete environment contract.

## What it contributes

- deterministic environment reset, observation, typed proposal, hard-gated
  verification, and replay;
- immutable fixtures and evidence digests;
- held-out evaluation separated from training cases;
- trajectory safety gates that cannot be compensated by aggregate reward;
- bounded recursive improvement with lineage and regression checks;
- canary, review, rollback, and proposal-mode release boundaries;
- an offline RL lane that cannot access providers, credentials, or production
  state.

## What the six-month literature adds

The newer papers move the harness itself into the research variable: external
state, context policies, trajectory capture, environment redesign, and
self-evolution are treated as objects that can change agent outcomes. The
survey's safety and replay discipline is therefore a useful control baseline,
not a substitute for cross-model transfer evidence.

## Next review actions

- resolve the canonical `system-designs` survey files against the seven ArXiv
  candidates;
- compare the finance benchmark's hard gates with each paper's verifier and
  reward design;
- record whether each reported gain survives held-out tasks, cost accounting,
  and failure/recovery tests;
- publish a single crosswalk in the research-signals run folder.
