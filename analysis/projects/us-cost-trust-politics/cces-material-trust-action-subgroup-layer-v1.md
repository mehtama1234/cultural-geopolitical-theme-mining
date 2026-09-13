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
The machine-readable output was produced at `/tmp/cces-material-trust-action-subgroups.json`.

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
retains counts and weighted numerators for audit.

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
vote, consumer exit, and later material security.
