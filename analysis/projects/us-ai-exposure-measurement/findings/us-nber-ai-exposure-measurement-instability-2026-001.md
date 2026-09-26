# Finding 001: AI exposure estimates can change when the measuring model changes

**Status:** bounded measurement-quality counterexample · **Checked:** 2026-09-22

## The finding in plain language

Several recent studies use language models to judge how exposed different occupations are to AI. This NBER study asks whether those judgments stay the same when the model changes.

The researchers applied the same rubric to the same occupational tasks using three frontier language models. Mean exposure estimates differed by 3.6 times, and agreement fell as low as 57%. When the different exposure measures were used in later statistical exercises, individual-level coefficient sizes varied 2.4 times, and a county-level result changed from significantly negative to insignificantly positive.

```text
task description
  -> model-generated exposure score
  -> statistical estimate
  -> result can change with the model used to measure exposure
```

## What this adds to the broader atlas

This is an important brake on the AI-work findings. Exposure, adaptive capacity, and retraining outcomes can still be useful evidence, but they should not be treated as if “AI exposure” were one fixed natural fact. The measurement process itself can shape who appears exposed, how vulnerable a place looks, and how large an estimated effect becomes.

The broader societal point is that new technical systems can create not only new risks and opportunities, but also new disputes over what is being measured. Employers, workers, researchers, and policymakers may act on different exposure maps while believing they are discussing the same underlying condition. That is a cross-source interpretation, not a direct survey result from this paper.

## What the source does not show

- It studies LLM-generated exposure measures, not every AI-exposure measure.
- Model disagreement does not prove that all exposure concepts are meaningless.
- A changed downstream coefficient does not establish which estimate is correct.
- The study does not measure actual AI adoption, worker displacement, earnings, bargaining, or political response.
- Model instability may reflect ambiguous task descriptions, prompt design, model knowledge, or aggregation choices.

## Next decisive test

Before pooling AI exposure across findings, compare model-generated scores with worker reports, employer adoption records, non-LLM task measures, and realized job or earnings changes using the same occupations and period.

## Source

- [NBER working-paper page](https://www.nber.org/papers/w35110)
- [NBER DOI record](https://doi.org/10.3386/w35110)

**Evidence status:** the official NBER abstract reports substantial cross-model instability and downstream sensitivity; substantive labor-market outcomes remain separate evidence.
