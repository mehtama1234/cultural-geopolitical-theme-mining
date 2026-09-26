# Housing-assistance transition: next-test protocol v1

**Checked:** 2026-09-25  
**Status:** execution protocol; real public-file timing audit complete; no new estimate  
**Scope:** U.S. housing-assistance entry or exit, practical alternatives,
work/care trade-offs, and later housing security

## Why this is the next test

The HUD–LEHD study establishes a linked employment and earnings trajectory
around housing-assistance entry and exit. HUD HEARS adds a regional linked
comparison showing that positive, neutral, and negative exits have different
one-year housing, health, behavioral-health, and wage outcomes.

Together they close two important bridges:

```text
assistance transition -> same-linked-unit work/earnings trajectory
exit type -> same-linked-unit housing/health/wage outcome
```

They do not yet show whether the transition improved or worsened the person's
actual housing bargain, because assistance amount, rent burden, housing
quality, exit reason, available alternatives, and later recovery are not held
in one retained unit across the two studies.

## Bounded research question

For a person or household observed around housing-assistance entry or exit,
does the transition change practical room through rent, housing quality,
location, time/care constraints, work, health, and later housing stability—and
does the result differ by exit reason or available alternative?

This is a route for investigation, not a claim that assistance causes every
later outcome.

## Minimum episode stages

Promote a new end-to-end finding only if one lawful source or explicitly linked
design can retain, with denominators and missingness:

```text
need or eligibility
  -> assistance entry/continuation/exit and amount/timing
  -> rent burden, housing quality, location, and available alternative
  -> work, earnings, care, health, or time trade-off
  -> notice, appeal, landlord/agency response, or other institutional route
  -> move, continued housing, instability, or verified recovery
  -> later persistence, trust, action, switching, or exit
```

The minimum promotion gate is narrower than the full route: the record must
show both (1) an episode-level alternative, non-use, or exit reason and (2) a
later housing, work, health, or security outcome for the same retained unit.
Without both, publish an acquisition boundary or stage finding only.

## Candidate source routes

### 1. Authorized linked administrative route — highest value

Use the HUD–LEHD/linked housing records only if an authorized extract exposes
the necessary fields or a lawful analyst can run the requested tabulation.
Required checks are:

- unit identity and linkage quality;
- assistance program, entry/exit date, amount, and spell definition;
- rent burden, housing quality, location, and exit reason;
- employment, earnings, care/health, and observation windows;
- comparison group or documented noncausal design;
- missingness, disclosure rounding, and subgroup suppression; and
- whether later housing stability or recovery is actually measured.

The published HUD–LEHD paper is not itself a respondent-level extract. Its
aggregate slopes must not be expanded into a household recovery claim.

### 2. Public longitudinal survey route — only after field audit

The [SIPP housing-transition field audit](sipp-housing-transition-field-audit-v1.md)
confirmed that the 2025 public schema contains housing-assistance, rent
subsidy, voucher, move-reason, residence-spell, rent/mortgage, and
rent/mortgage-difficulty fields. The current local 35-field extraction omitted
them. The next low-cost action is therefore a smoke-test extraction with those
fields, not a new estimate.

Screen public SIPP or another authorized longitudinal survey for a compatible
housing-assistance spell, rent/housing-cost measure, employment, health/care,
and following-period housing-security fields. Before analysis, record the
survey universe, panel months, spell timing, weights, replicate weights,
missingness, and whether the housing-assistance field identifies entry/exit or
only current receipt.

This route can support a same-respondent descriptive bridge if the fields are
present and temporally aligned. It cannot be joined to HUD–LEHD or HEARS by
assumption, geography, or similar labels.

### 3. Public linked comparator — bounded regional outcome route

Retain HUD HEARS as the regional comparator for classified exit type and
one-year outcomes. It can test whether a proposed national interpretation is
consistent with or contradicted by a linked local case, but it cannot provide
national prevalence or causal effects.

The HUD USER national participation/transition study is useful for spell and
program-transition context. It does not supply adequacy, rent burden, health,
work, or recovery for the same household and must remain descriptive.

## Required counterexamples

Before strengthening the finding, test at least these alternatives:

- exit reflects rising income, homeownership, relocation, or family support;
- employment improvement began before assistance entry;
- negative exit reflects health, disability, eviction, or administrative loss
  rather than the assistance itself;
- rent burden changes because of local prices or household composition;
- stable employment coexists with unsafe or unaffordable housing; and
- a positive exit improves housing while reducing access to work, care, or
  social support.

## Stop conditions

Stop the pass and report an acquisition boundary if any of the following is
true:

- no same-unit alternative, non-use, or exit-reason field is available;
- assistance amount or timing cannot be aligned to the outcome window;
- rent burden or housing quality is only an aggregate contextual measure;
- the outcome is a different population, geography, or program with no valid
  linkage;
- the source is restricted and no authorized human/account-holder route is
  available; or
- the result would require treating entry, exit, or earnings as proof of
  housing security or recovery.

## Current decision

The field-level audit, synthetic extractor smoke test, and real public-file
missingness/timing report are complete. The real pass confirms that the public
file has a 12-month same-person backbone, but its main assistance and housing-
cost fields are reference-period or residence-spell variables rather than
dated monthly entry/exit measures. The current retained evidence therefore
still does not pass the minimum promotion gate. A future descriptive episode
ledger would require explicit SIPP universes, weights, replicate weights,
status/missingness treatment, and a predeclared transition window. Do not
download restricted respondent files by default, and do not add another
aggregate housing-assistance participation estimate as an end-to-end advance.

The follow-on [weighted monthly-assistance/work screen](sipp-housing-assistance-work-screen-v1.md)
uses `EOTHAS_MNYN` and reaches a bounded next-month housing-difficulty/work/
resource bridge with Fay–BRR uncertainty. It still does not pass the minimum
promotion gate because the exposure is combined “other” assistance rather than
HUD program identity or adequacy, and no institutional response, alternative,
verified recovery, trust, or political-action endpoint is retained.
The accompanying [tenure/resource counterexample audit](sipp-housing-assistance-work-stratified-v1.md)
shows the pooled housing-difficulty contrast is composition-sensitive and
reverses direction across renter resource bands; this is a required caution
against treating the pooled screen as an assistance effect.

## Existing evidence

- [HUD–LEHD bounded finding](findings/us-census-hud-lehd-assistance-employment-trajectories-2026-001.md)
- [HUD HEARS exit-type finding](../us-hud-hears-exit-type-outcomes/findings/us-hud-hears-exit-type-outcomes-2025-001.md)
- [Cross-source housing synthesis](../../US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md)
