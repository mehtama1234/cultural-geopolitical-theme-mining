# The material-to-institutional-judgment path is not uniform across groups

**Status:** provisional same-respondent subgroup cross-lag · **Checked:** 2026-09-14

## The bounded finding

The April–June 2025 HTOPS linkage allows a more demanding question than a
single cross-sectional association: among the same retained respondents, does
April household-expense difficulty sit beside June confidence in Congress in
the same way across income and race/ethnicity groups?

The answer is descriptive and uneven. In the linked sample, high June
confidence among respondents with April expense difficulty was 27.1% in the
under-$25,000 income group versus 26.1% among under-$25,000 respondents who
reported no difficulty. In the $75,000–$99,999 group the corresponding values
were 13.5% and 20.8%. Among White-alone respondents the values were 12.8% and
15.9%; among Black-alone respondents they were 19.9% and 12.6%. Hispanic- and
Asian-alone difficult-expense cells were 26.7% and 35.5%, respectively.

These contrasts are useful because they resist a single “hardship lowers
trust” story. They are not causal effects, population transition rates, or
evidence that expense difficulty produced political action.

## Selected estimates

| Baseline subgroup | April no difficulty | April any difficulty | Reading boundary |
|---|---:|---:|---|
| Under $25,000 | 26.1% (SE 2.17) | 27.1% (SE 1.99) | 257 and 429 unweighted valid records |
| $75,000–$99,999 | 20.8% (SE 1.96) | 13.5% (SE 1.67) | 520 and 348 unweighted valid records |
| White alone | 15.9% (SE 0.65) | 12.8% (SE 0.72) | 2,895 and 1,643 unweighted valid records |
| Black alone | 12.6% (SE 1.70) | 19.9% (SE 1.90) | 287 and 278 unweighted valid records |
| Hispanic | 21.9% (SE 2.56) | 26.7% (SE 2.35) | 186 and 249 unweighted valid records |
| Asian alone | 26.2% (SE 2.08) | 35.5% (SE 3.07) | 357 and 175 unweighted valid records |

The percentages are weighted conditional shares within the selected linked
subgroup cells. “High confidence” means reporting a great deal or quite a lot
of confidence in Congress in June. “Any difficulty” combines a little,
somewhat, and very difficult responses to the April question about usual
household expenses.

## What this adds to the end-to-end program

This pass closes part of the measurement gap between material condition and
institutional judgment:

```text
April household-expense condition
  -> same retained respondent
  -> June institutional-confidence measure
  -> open attribution, action, remedy, and recovery
```

The subgroup variation is substantively important. It suggests that the
meaning of a material condition may be conditioned by income position, race and
ethnicity, prior trust, institutional experience, political identity, and
available alternatives. The current data cannot identify which of those
mechanisms is responsible, but they make a pooled interpretation less
credible.

The Black-alone and Asian-alone difficult-expense cells are not evidence of a
generalized group effect: they are descriptive cells with different sample
sizes, selection, weighting, and unmeasured composition. The under-$25,000
result also shows why income should not be treated as a complete proxy for
liquid room or meaning.

## Design and uncertainty boundary

- April and June public-use records are linked by `SCRAMID`; 6,564 IDs are
  retained from the two files.
- April `PWEIGHT0` and 80 replicate weights provide conditional precision for
  the retained linked sample. They are not documented here as an
  attrition-adjusted longitudinal weight.
- The exposure is a broad self-reported two-month expense-difficulty item, not
  a dated bill, price, job loss, care event, or objective expenditure.
- June confidence in Congress is an institutional-judgment outcome, not
  attribution, legitimacy, vote, turnout, complaint, appeal, or collective
  action.
- The subgroup comparisons were not specified as a causal model and should
  not be read as a set of independently confirmed significance tests.

## Counterexamples kept visible

- Low-income respondents with and without reported expense difficulty have
  similar high-confidence shares in this selected panel, so hardship is not a
  sufficient explanation of institutional judgment.
- The $75,000–$99,999 contrast runs in the opposite direction from the
  under-$25,000 contrast, showing why a pooled hardship/trust rule is unsafe.
- A respondent can retain confidence while remaining materially pressured, or
  lose confidence without a reported expense transition; both routes remain
  possible.
- The observed judgment does not tell us whether the respondent blamed
  Congress, the administration, firms, prices, employers, health costs, or no
  actor at all.

## Next test

The next high-value extension is to add baseline and follow-up food, energy,
job, health, care, and source-environment fields to the subgroup design, then
measure an actual action endpoint where available. The action endpoint should
remain separate by type: vote, registration, contact, complaint, appeal,
switching, exit, or silence. A same-person causal interpretation still
requires dated exposure, prior judgment, alternatives, attribution, and an
appropriate attrition strategy.

## Reproduction

The [machine-readable subgroup record](../../../records/us-htops-material-trust-subgroups-2025.json)
and [full audit output](../data/htops-2025-material-trust-subgroups.json)
preserve the subgroup estimates, valid counts, replicate-weight standard
errors, and input hashes. The calculation is implemented in
[`analyze_htops_2025_material_trust_subgroups.py`](../../../../scripts/analyze_htops_2025_material_trust_subgroups.py).

**Evidence status:** same-respondent subgroup descriptive cross-lags in a
selected linked HTOPS panel; no causal, attrition-adjusted, attribution, or
political-action claim.
