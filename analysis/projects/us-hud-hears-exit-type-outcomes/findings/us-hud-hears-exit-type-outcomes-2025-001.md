# Finding 001: A housing-assistance exit is not one outcome

**Status:** bounded regional linked-administrative housing-exit finding · **Checked:** 2026-09-24

## The bounded finding

The HUD Health, Economic, and Residential Stability (HEARS) study linked exit
records from the Seattle Housing Authority and King County Housing Authority to
wage, Medicaid, behavioral-health, homelessness-service, and homeless-management
records. Among 8,266 heads of household with classified nondeath exits, 13.5%
were positive, 54.9% neutral, and 31.6% negative.

The one-year separation was substantial: a homelessness or unstable-housing
event occurred for 3.1% of people with positive exits, 14.5% with neutral exits,
and 25.4% with negative exits. Negative exits were also associated with roughly
double the odds of a behavioral-health crisis relative to neutral exits, while
positive exits were associated with lower emergency-department-use odds than
negative exits.

```text
assisted housing
  -> classified exit pathway
  -> housing stability + health + behavioral health + wages
  -> different residual-risk profiles
```

## What this adds to the atlas

It resolves a key interpretive problem in the national HUD–LEHD paper: the word
“exit” cannot be treated as either success or failure. The institutional question
is not merely whether someone left assistance, but whether the exit transferred
them into stable housing and greater autonomy or into homelessness, crisis, and
loss of support.

The study also shows the value of cross-sector administrative linkage: housing
records alone would not reveal the post-exit health and homelessness pathways.

## Limits and next test

- The evidence is observational and geographically bounded to two King County
  housing authorities.
- Exit categories are constructed from administrative reasons; health-related
  and moves-to-family exits can be ambiguous.
- Selection into positive, neutral, and negative exits may explain part of the
  outcome separation.
- The one-year window does not establish durable housing security, later trust,
  civic action, or practical ability to switch or exit other institutions.

The next decisive test is a broader linked panel that retains exit reason,
assistance amount and timing, rent burden, housing quality and location, health,
care burden, employment, and later housing stability for the same household.

## Source

- [HUD HEARS final report](https://www.huduser.gov/portal/portal/sites/default/files/pdf/HUD-HEARS-Study.pdf)
- [Machine-readable trend record](../../../records/us-hud-hears-exit-type-outcomes-2025.json)

**Evidence status:** same-linked-unit regional evidence distinguishes exit type and
shows divergent post-exit housing, health, behavioral-health, and wage outcomes;
it is not a national causal estimate.
