# Finding 001: A better-looking survey question is not automatically a better coverage measure

**Status:** bounded health-insurance measurement and administrative-legibility finding · **Checked:** 2026-09-23

## The finding in plain language

The Census has historically counted fewer people as having Medicaid in the ACS
than appear in CMS enrollment records. The 2022 ACS Content Test compared a
redesigned health-insurance question with the old version, changing the format,
some response wording, and the order of response options.

Against linked CMS enrollment records, the two versions performed equally well
at measuring Medicaid. The proposed redesign therefore did not, by itself,
resolve the survey-administrative gap.

The practical chain is:

```text
question wording and response interface
  -> respondent understanding and recall
  -> reported Medicaid coverage
  -> comparison with CMS enrollment
  -> active coverage, care, affordability, and continuity [separate open stages]
```

The simple social insight is that improving the interface is useful only if it
changes what can be measured. And even a better measure of enrollment is not the
same thing as better coverage or better care.

## What this adds to the atlas

This strengthens the measurement counterexample across the atlas: a formal
correction can be well designed and still fail to improve the benchmarked result.
It also separates survey voice from administrative truth without assuming that
either source is the complete lived experience.

## Limits and counterexamples

- This is a Census SEHSD working paper and measurement evaluation, not a final
  Census publication or universal survey judgment.
- Equal performance in the test does not prove equal accuracy for every subgroup,
  state, mode, enrollment type, or year.
- Survey responses and CMS enrollment can differ in timing, coding, recall, and
  linkage; neither measures all care use or affordability.
- Enrollment is not active treatment, continuity, health, or household security.
- A null question-design result does not mean wording, order, language, or mode
  never matter in other contexts.

The next decisive artifact is a protected respondent-month panel linking question
version, response, CMS enrollment, churn, managed-care status, care use, claims,
out-of-pocket cost, correction, and later continuity.

## Sources

- [Census SEHSD working-paper page](https://www.census.gov/library/working-papers/2026/demo/sehsd-wp2026-18.html)
- [Full Census paper](https://www2.census.gov/library/working-papers/2026/demo/sehsd-wp2026-18.pdf)

**Evidence status:** the official evaluation reports equal test performance of
the redesigned and control Medicaid questions against CMS records; coverage,
care, affordability, and continuity remain separate.
