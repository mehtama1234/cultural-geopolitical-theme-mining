# Finding 003: Local change has multiple participation currencies—presence, trust, civic action, and safe use are not interchangeable

**Status:** provisional cross-source migration/place synthesis · **Checked:** 2026-09-17

## The bounded finding

The current migration/place evidence does not support a single “integration”
or “local reaction” measure. It separates four observable surfaces:

1. demographic context: population change and foreign-born share;
2. local capacity: health/social-assistance, retail, and food employment per
   resident;
3. political context: institution-specific trust, civic action, and reported
   voting by county-growth quartile; and
4. lived institutional behavior: immigrant-family avoidance of essential
   activities and public benefits when immigration concerns are present.

The surfaces point in different directions. In a 620-county context screen,
the highest-growth quartile had lower federal trust than the lowest-growth
quartile while civic action and reported voting were comparatively stable. In a
separate December 2025 WBNS subgroup, 23% of adults in immigrant families with
children reported avoiding at least one essential activity because of
immigration concerns. These are not the same people or units, so the result is
not a causal estimate. The contribution is a measurement rule: population
presence, political participation, and safe institutional use must be tracked
as distinct currencies.

```text
local demographic change
  -> demand, capacity, ownership, and distribution
  -> perceived fairness, control, belonging, and institutional trust
  -> civic action, voting, continued use, protective non-use, or exit
  -> [open] which actor responds, who recovers, and whether inclusion or power changes
```

## Evidence comparison without pooling

| Surface | Result | Unit and denominator | What it can and cannot say |
|---|---:|---|---|
| Growth context | Median population change ranged from -1.023% in Q1 to 6.749% in Q4 | 620 counties above 100,000 residents; 2020–2023 Census context | A place-change screen; growth is not migration and is not an individual exposure |
| Capacity by growth/nativity | In the high-growth/high-foreign-born cell, health/social-assistance employment was 436.23 per 10,000 residents versus 663.49 in the low-growth/high-foreign-born cell | 620-county joint quartile screen | Provider/employer presence per resident; not appointment reach, price, wait, language access, quality, or use |
| Federal trust by growth | 35.251% in the highest-growth quartile versus 41.927% in the lowest-growth quartile reported great deal/fair amount of federal trust | 2024 CES common-post respondents with county FIPS; weighted contextual comparison | A descriptive place context; not immigration-specific opinion or a causal effect of growth |
| State trust by growth | 57.406% in Q4 versus 54.174% in Q1 | Same CES contextual frame | State judgment is not monotonic with growth; institution-specific trust matters |
| Civic action by growth | 37.268% in Q4 versus 38.112% in Q1 reported at least one listed civic action | Same CES contextual frame; meeting, sign, campaign work, protest, official contact, donation | Action can remain stable while trust varies; the composite is not all organizing, turnout, or political withdrawal |
| Reported voting by growth | 97.070% in Q4 versus 96.714% in Q1 | Same CES contextual frame | A high reported-vote measure; not proof of inclusion, policy influence, or safe access |
| Essential-activity non-use | 23% avoided at least one of six essential activities | 1,036 adults in immigrant families with children under 19; prior-year retrospective WBNS measure | Directly reports perceived-risk-linked non-use, but not causal ordering, legal risk, alternatives, or remedy |
| Public-benefit non-use | Almost one in five went without public benefits because of immigration concerns; 12% cited information-sharing concern | Same WBNS subgroup and period | Perceived data/status risk can shape access behavior; actual agency sharing and eligibility are unverified |

The county and respondent surfaces are deliberately not combined into a
“migration trust index.” The county frame includes births, deaths, domestic
migration, and international migration. The CES contextual respondents are not
the WBNS families, and the WBNS estimates are not assigned to counties in this
pass.

## What the comparison establishes

### Trust and action can separate

The CES context screen shows lower federal trust in the fastest-growth county
quartile, but state trust is non-monotonic and civic action changes little. This
is a counterexample to both “growth causes political withdrawal” and “stable
action proves local acceptance.” People can judge a federal institution
differently while continuing to vote or perform one of the measured actions.

### Safe use is a different participation question

The WBNS layer shows a different boundary: a family may not use a clinic,
benefit, workplace, school or care activity, police, or community institution
because using it is perceived as risky. That behavior can be protective in the
short run and materially costly in the longer run. It may be invisible in
ordinary participation statistics because no application, complaint, or formal
exit is recorded.

### Capacity is neither inclusion nor exclusion by itself

The capacity screen finds non-monotonic relationships across population growth
and foreign-born share. A place can have more residents and lower per-resident
provider employment without proving a shortage, and a place can have higher
capacity without proving that newcomers or existing residents can safely use it.
Likewise, a local attitude difference cannot be attributed to capacity without
respondent-level exposure, alternatives, attribution, and timing.

## What this adds to the broad atlas

This synthesis turns “belonging” into an executable measurement stack rather
than a single cultural label:

- **presence:** who lives in a place and how the place changes;
- **capacity:** what firms and institutions are physically or administratively
  available;
- **usable access:** whether people can safely and practically use the route;
- **judgment:** which institution is trusted, blamed, or seen as fair;
- **action:** vote, contact, complaint, organizing, protest, switching, or
  non-use;
- **power:** whether residents can influence rules, ownership, data, prices, or
  public response.

The broad societal question is therefore not simply whether immigration is
popular or whether a county is growing. It is whether demographic change is
converted into usable opportunity and recognized belonging, or into constrained
access, protective withdrawal, contested responsibility, and different forms of
political demand.

## Counterexamples and limits

- Fast growth is not the same as immigration; foreign-born share is a stock,
  not an arrival event.
- High growth with lower federal trust does not establish that growth caused
  distrust or that residents were less politically active.
- Stable civic action does not prove belonging, fair treatment, or safe access.
- Non-use can be protective, costly, strategic, temporary, or all four; it is
  not automatically apathy or generalized distrust.
- Employer and provider presence does not measure price, wait, travel,
  language, acceptance, quality, or unmet need.
- The WBNS family-status comparison does not isolate composition from income,
  language, geography, hardship, or prior institutional experience.
- No source here observes the same family from a dated policy/enforcement
  encounter through remedy, recovery, trust, and political action.

## Coding rule

```text
population change      != immigration exposure
foreign-born share     != arrival flow
capacity presence      != usable access
voting                 != belonging
civic action           != trust
trust                  != safe service use
non-use                != apathy
county context         != respondent experience
cross-source contrast  != pooled causal estimate
```

Code this as **cross-source evidence that local demographic context, capacity,
institution-specific judgment, civic action, and perceived-risk-linked non-use
can diverge; a same-unit causal path from migration or policy exposure to
belonging, remedy, trust, and political action remains open**.

## Next decisive test

The smallest stronger design is a place-linked repeated respondent or family
panel with a dated encounter and a common alternative/response ledger:

```text
arrival, policy, enforcement, workplace, school, health, or benefit event
  -> perceived risk, information source, and blamed actor
  -> attempted use, safe substitute, delay, or non-use
  -> price, time, travel, income, health, child, or belonging outcome
  -> agency/employer response and verified remedy
  -> later trust, complaint, organizing, turnout, vote, continued use, or exit
```

Stratify by family composition, nativity, language, income, race/ethnicity,
tenure, disability, geography, prior use, and capacity context. Include
high-capacity/high-pressure and low-capacity/low-pressure places as
countercells. The design should measure both protection and sacrifice so that
“safe non-use” is not automatically coded as harm or freedom.

## Sources and storage boundary

- [Local capacity and immigration meaning finding](us-immigration-local-demand-001.md)
- [Immigration concern and essential-activity non-use finding](us-immigration-local-demand-002.md)
- [CES local trust/action context by growth](../migration-place-local-trust-action-context-v1.md)
- [Joint growth, nativity, and capacity layer](../migration-growth-nativity-joint-capacity-layer-v1.md)
- [Urban Institute WBNS project](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey)
- [Urban Institute WBNS 2025 analysis](https://www.urban.org/research/publication/immigration-concerns-disrupted-families-essential-activities-and-caused)
- [CES Common Content 2024 dataset](https://doi.org/10.7910/DVN/X11EP6)
- [American Community Survey](https://www.census.gov/programs-surveys/acs)

This synthesis uses existing local county summaries and compact WBNS metadata;
no respondent microdata or bulk file was downloaded.

**Evidence status:** separate place-context, political-context, capacity, and
respondent non-use surfaces compared with preserved units and boundaries. No
individual-level migration-to-belonging or policy-to-action effect is claimed.
