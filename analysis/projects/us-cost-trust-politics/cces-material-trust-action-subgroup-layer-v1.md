# CCES material-proxy, trust, action, and subgroup layer v1

**Checked:** 2026-09-13  
**Status:** weighted descriptive subgroup comparison; not a causal or complex-survey estimate

## Why this pass exists

The existing CCES layer showed that gig work and student-loan responsibility
do not map monotonically onto trust or civic action when pooled across
respondents. This pass asks whether that broad non-monotonic pattern is hiding
different relationships across income and race groups.

The unit remains the **2024 CCES post-election respondent**. The analysis uses
the common post-election weight and retains respondents with valid values for
both material/work proxies, federal and state trust, and all six selected
civic-action fields. It reads 60,000 rows and retains 21,560 valid subgroup
records in 48 cells.

## Variables and limits

- `gigwork`: earned money through a website or mobile app in the prior year.
- `edloan`: currently responsible for paying a student loan.
- Federal/state trust: “a great deal” or “a fair amount” treated as positive.
- Civic action: at least one positive response among six selected past-year
  action fields.
- `faminc_new`: ordered income codes grouped as 1–4, 5–9, and 10–16. Codes
  97/other are excluded; the grouped labels are code bands, not dollar values
  in this artifact.
- Race: codes 1, 2, and 3 retained as White, Black, and Hispanic; codes 4–8
  combined as `other_or_multiracial` to avoid presenting very small cells as
  stable subgroup estimates.

The script is [analyze_cces_material_trust_action_subgroups.py](../../../scripts/analyze_cces_material_trust_action_subgroups.py).
The full machine-readable output was regenerated from the official public CSV
on 2026-09-25 (60,000 rows; 21,560 valid records; 48 cells). The compact
committed [reproduction audit](data/cces-material-trust-action-subgroups-2024-v9-audit.json)
retains the Dataverse file identifier, MD5, generated-output hash, valid
universe, and all extrema reported below; the full 48-cell output remains a
temporary derived artifact rather than a committed raw-data copy.

## What the screen shows

Among cells with at least 100 unweighted respondents, the observed ranges are:

| Outcome | Lowest cell | Highest cell | Reading |
|---|---|---|---|
| Federal trust | 34.0%: higher-income-code White respondents, no gig work, student debt yes (n=729) | 68.3%: lower-income-code Hispanic respondents, no gig work, student debt no (n=325) | Trust varies across subgroup and proxy combinations; income alone is not a sufficient interpretation. |
| State trust | 52.2%: lower-income-code Black respondents, gig work yes, student debt no (n=136) | 75.7%: higher-income-code Hispanic respondents, no gig work, student debt no (n=193) | Federal and state trust need not move together. |
| Any civic action | 18.5%: lower-income-code Hispanic respondents, no gig work, student debt no (n=325) | 51.7%: higher-income-code White respondents, no gig work, student debt yes (n=729) | Action is not a simple inverse of hardship proxy or trust. |

The range is a deliberately compact screen, not a ranking of groups. Several
gig-work/student-debt/race intersections are smaller than 100 respondents and
should not carry a strong substantive interpretation. The full 48-cell output
retains counts and weighted numerators for audit, while the committed audit
artifact preserves the range screen and its exact source/output hashes.

## Vote is a separate outcome and a separate valid universe

The same official CSV contains `CC24_401`, where code 5 is the self-reported
answer “I definitely voted.” A separate audit retains valid codes 1–5 and
recomputes the 48 material/work/race cells with `commonpostweight`. It reads
60,000 rows and retains 26,231 valid vote answers, versus 21,560 valid records
in the trust/action screen. Among cells with at least 100 unweighted records,
the reported definite-vote share ranges from 82.29% in the lower-income-code
Black, gig-work, no-student-debt cell to 99.96% in the higher-income-code
Black, no-gig-work, student-debt cell.

The [separate vote audit](data/cces-material-vote-audit-2024-v9.json) is kept
apart for three reasons: the valid denominator differs, self-reported voting
is not the same as validated turnout, and voting is not interchangeable with
the six selected civic-action items or with trust. The comparison is therefore
useful mainly as a denominator and outcome-boundary check, not as evidence that
the material proxies caused turnout or vote choice.

## Broad interpretation

Material position, work form, debt responsibility, race, trust, and civic
action intersect without producing one universal response pattern. That is
consistent with the program's larger claim that material conditions become
political through identity, information, institutional experience, and
available alternatives—not through a single automatic pipeline.

This is evidence about **distribution and heterogeneity**, not proof that
income, race, gig work, or student debt caused trust or action. The post-election
cross-section lacks event timing, prior identity history, attribution, and a
design-based variance estimate in this pass. `CC24_401` vote is intentionally
not used here because the selected valid universe and missingness differ from
the trust/action screen.

## What this changes in the broad program

It strengthens themes 8, 9, and 11 by adding an explicit subgroup check to the
material → trust/action bridge. It also supplies a counterexample to any
summary that treats either lower income, gig work, or student debt as a
uniform predictor of distrust or withdrawal.

The next stronger test is a repeated or event-based design with timing,
attribution, prior political identity, source environment, and a valid variance
procedure. The required outcomes remain separate: trust, civic action, turnout,
vote, consumer exit, and later material security. The vote audit makes the
separation operational in the current CCES release.
