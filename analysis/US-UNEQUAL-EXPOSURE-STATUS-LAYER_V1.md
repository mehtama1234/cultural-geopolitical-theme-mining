# US unequal exposure and status layer v1

**Checked:** 2026-09-12  
**Purpose:** consolidate how status, resources, place, and alternatives shape
exposure and exit across the broad program  
**Status:** cross-source distributional synthesis; not one integrated sample

## The question

Who experiences a condition, who can avoid it, who can get a remedy, and who
has an alternative? Status is not only a demographic label. It changes cash,
time, access, treatment, social support, institutional voice, and ability to
leave.

```text
income, race, age, gender, disability, family, migration, tenure, place, or firm size
  -> exposure and available alternatives differ
  -> the same rule, price, service, or shock produces different effort or risk
  -> people adapt, appeal, borrow, stay, move, organize, or go without
  -> institutions and firms distribute remedy, cost, and control unevenly
```

The program must not treat a group average as a mechanism. Each dimension can
stand for several underlying conditions, and intersections can change both
exposure and the ability to respond.

## What the current layers show

| Dimension | Current evidence layer | What is visible | What remains open |
|---|---|---|---|
| Financial room | SHED price adaptation; SIPP resource and Fay-BRR resource layers | borrowing, reduced use, delayed purchases, savings, and emergency capacity vary with resources | same person’s price, sacrifice, health, and recovery sequence |
| Tenure and place | SIPP tenure × resource and region layers; NHTS | renters, owners, regions, and urban/rural settings have different measured room, food, utility, and mobility conditions | local price, housing quality, insurance, service access, and move/stay mechanism |
| Race, ethnicity, family, and poverty | USDA 2024 food-security layer | food insecurity is higher for households below poverty, single-parent households, Black and Hispanic households, and some city/rural settings; households with children can shield children from adult hardship | joint effects of income, family structure, place, work, assistance, and food access in the same records |
| Gender, age, education, employment, and care | ATUS 2024 time layer | paid work, household production, childcare, workplace location, and social time are distributed differently | who caused the schedule, what time displaced, and how cash and time constraints compound |
| Age, education, income, and civic identity | Pew news/civic-engagement layer | participation types differ, and younger adults, education, and income are unevenly represented across types | whether source environment or status changes interpretation and civic action over time |
| Product, state, and institutional access | CFPB complaint layer; safety-net access layer | complaint response varies by product; office access and administrative rules can change participation | who receives a remedy, what alternatives exist, and whether trust or exit changes |

These are compatible lenses, not a person-level join. They establish that
exposure and response are distributed; they do not identify one universal
status hierarchy or a single cause of unequal outcomes.

## The key societal pattern

The same nominal price, deadline, notice, work rule, or service failure can have
a different real cost because people have different reserves and alternatives.
One person pays with cash; another pays with time, food quality, family help,
credit, safety, or the ability to remain in a place. One person can switch or
appeal; another cannot afford the attempt.

This is the distributional core of the broad program. It links consumer,
household, work, care, public-system, cultural, and political themes without
claiming that any one status label determines behavior.

## What this adds to the 14-theme map

- **Unequal exposure and status:** status changes both treatment and exit
  options, so exposure, remedy, and recovery must be reported together.
- **Household room and consumption:** resources determine which need can be
  protected when choices conflict.
- **Time, work, and care:** schedule control and unpaid support can substitute
  for money, but not without cost.
- **Consumer and public power:** access to a human, appeal, benefit, repair,
  or alternative is itself unequally distributed.
- **Trust, identity, and politics:** unequal treatment may become meaning,
  blame, trust, or action, but those interpretations need direct measures.
- **Firm, infrastructure, and place power:** location and ownership determine
  who receives investment and who bears risk.

## Next valid intersectional test

Start with a small pre-registered set of intersections rather than dozens of
comparisons:

1. income-to-poverty ratio × tenure for housing, utility, food, and debt;
2. family structure × employment/care for time, food, work, and health;
3. race/ethnicity × income × place for food, assistance, and service access;
4. disability × channel/access route for public benefits and customer remedy;
5. age × source environment × civic participation for trust and action.

For each, specify the unit, universe, time window, weight, missingness, and
comparison before looking at outcomes. Use design-based uncertainty where the
source provides replicate weights. Keep the intersection as descriptive unless
a valid policy, place, or longitudinal design identifies a change.

## What would change the picture

The working picture would weaken if status differences disappeared after the
relevant resources, place, exposure, and alternatives were measured; if the
same rule produced equal practical costs across channels; or if apparent group
differences were entirely artifacts of incompatible universes or measurement.

The first intersectional diagnostic is now the [SIPP Fay-BRR race × resource
layer](projects/us-household-calendar-integration/sipp-fay-brr-race-resource-layer-v1.md),
followed by a [race × tenure × resource layer](projects/us-household-calendar-integration/sipp-fay-brr-race-tenure-resource-layer-v1.md).
The three-way passes have a defined person-month unit, replicate-weight
uncertainty, five distributional outcomes, and documented universe/status
filtering. The disability pass adds a work-limiting-condition intersection;
the tenure pass adds housing position; and the composition pass adds child
presence. All still lack household counting, direct care measurement, a
counterexample to a causal mechanism, and a downstream outcome in the same
design.

Related records: [US broad theme coverage matrix](US-BROAD-THEME-COVERAGE-MATRIX_V1.md),
[SIPP Fay-BRR intersectional layer](projects/us-household-calendar-integration/sipp-fay-brr-tenure-resource-estimates-v1.md),
[USDA food-security layer](projects/us-food-budget-security/usda-2024-food-security-layer-v1.md),
[ATUS time layer](projects/us-household-calendar-integration/atus-2024-time-hidden-price-layer-v1.md),
and [Pew civic-engagement layer](projects/us-digital-habits-attention/pew-2025-news-civic-engagement-layer-v1.md).
