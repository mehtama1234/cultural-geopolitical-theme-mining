# Finding 027: SNAP restrictions can change consumption while increasing the felt stigma of receiving aid

**Status:** bounded safety-net, consumer-behavior, health-policy, and cultural-meaning finding · **Checked:** 2026-10-18

## The bounded finding

An NBER study of the first ten states to restrict SNAP purchases of sugary
drinks found that average SNAP-household retail purchases of excluded drinks
fell 12.4% in the first half of 2026. Where states excluded only some drinks,
households partly shifted toward drinks that remained eligible.

The study also surveyed SNAP recipients before and after implementation. Three
measures of perceived stigma increased by 0.10 to 0.17 standard deviations.
The authors' modeled national scenario estimates about $1.1 billion in annual
benefits if all sugary drinks were excluded, with about 70% coming from
modeled health-care savings—but the model does not fully value stigma.

A related NBER study, Working Paper 35739, reports a roughly 11% reduction in
restricted SNAP spending across the first statewide restrictions on sweetened
beverages and candy. Its summary also reports lower purchased calories and
sugar, while shelf prices changed little. This is a useful consumer-price
refinement, not a replacement for the first study: the spending, purchase,
calorie, sugar, price, and stigma measures use different units and do not yet
show total household consumption, health, or food security.

As a design counterexample, NBER Working Paper 35835 finds that P-EBT
disbursement was associated with a **16% increase in weekly sugary-item
spending** among SNAP-eligible households with school-aged children. The study
uses state-level payment timing and NielsenIQ Consumer Panel data, with no
change in placebo years or among households unlikely to receive P-EBT. This
does not mean P-EBT caused worse health; it shows that adding food purchasing
capacity and restricting eligible products can move the same consumer measure
in opposite directions.

The route is:

```text
SNAP purchase rule
  -> eligible/ineligible product boundary
  -> purchase substitution or reduced purchase
  -> health and household-budget possibility
  -> felt stigma, respect, or loss of choice
  -> [open] long-run health, food security, and political response
```

## Counterexample: a formal price wedge may not reach health

The paired [NBER Navajo Nation study](https://www.nber.org/papers/w35662)
examines the Healthy Diné Nation Act, which exempted healthier foods and
beverages from sales tax while increasing tax on unhealthy items. The policy
created a reported **7–8% price wedge**, but difference-in-differences and event
studies using maternal and newborn birth-certificate outcomes found no
detectable improvement in the studied diet- and weight-related health measures.
The public abstract identifies incomplete retailer implementation and
cross-border shopping as possible explanations, not isolated causal mechanisms.

This is a useful disconfirmation check. The first-wave SNAP study shows that a
purchase rule can change retail behavior while also increasing perceived stigma;
the Navajo study shows that a formal price signal can coexist with a health
null when implementation and shopping routes do not carry the policy through.
Neither result establishes that all nutrition restrictions fail or that no
other health, budget, or cultural outcome changed.

## Bounded public discussion

The [SNAP measurement discussion](../../../social-discussions/records/social-snap-current-context-linkedin-001.json)
warns that participation counts cannot identify underlying need or food
insecurity when administrative responsibility and measurement conditions change.
It is not a direct evaluation of the sugary-drink rule, but it helps preserve a
parallel boundary: visible program scale, visible purchase change, and actual
household security are different denominators. The post is selected LinkedIn
commentary, not population evidence.

## What this adds to the broad atlas

This is a clear example of policy effectiveness and social meaning moving in
opposite directions:

> A rule can produce the intended consumer behavior while making recipients
> feel more judged, controlled, or disrespected.

It also shows why “welfare” cannot be read from consumption alone. The health
case, household budget, public spending, autonomy, and stigma are separate
currencies. Mental accounting may make the restriction more effective than a
simple “people will just pay cash” story predicts, but it may also make the
boundary more socially visible.

## Limits and next test

- The source is a preliminary working paper, and the public abstract does not
  disclose complete sample counts or all state-level estimates.
- Grocery purchases are not the same as total consumption, household food
  intake, or health change.
- The 12.4% excluded-drink estimate and the roughly 11% restricted-spending
  estimate come from related but distinct summaries and should not be averaged
  into one effect.
- The 16% P-EBT sugary-item result is a different program, period, household
  group, and identification design. It is a mechanism counterexample, not a
  direct estimate of the 2026 restriction's effect or of health harm.
- The national $1.1 billion figure is modeled, not observed, and does not
  fully price stigma or every substitution route.
- The study does not establish whether stigma persists, changes participation,
  affects food security, or produces political action.
- A place-specific price-policy null may reflect implementation, retailer
  participation, product availability, or cross-border shopping rather than a
  universal absence of consumer response.

The next decisive artifact is a protected household-and-retailer panel linking
SNAP policy exposure, EBT and cash purchases, total sugary-drink consumption,
food security, medical outcomes, perceived respect, benefit participation, and
later policy judgment. Until then, the safe claim is that the restriction
changed short-run purchases and recipient perceptions at the same time, while a
separate place-specific price policy did not produce a detectable measured
health improvement.

## Sources

- [NBER Working Paper 35659](https://www.nber.org/papers/w35659)
- [NBER Working Paper 35739](https://www.nber.org/papers/w35739)
- [NBER Working Paper 35835](https://www.nber.org/papers/w35835)
- [University of Chicago research brief](https://bfi.uchicago.edu/insights/the-effects-of-snap-sugary-drink-restrictions-on-consumption-and-welfare/)
- [NBER Healthy Diné Nation Act study](https://www.nber.org/papers/w35662)
- [Bounded SNAP measurement discussion](../../../social-discussions/records/social-snap-current-context-linkedin-001.json)

**Evidence status:** quasi-experimental purchase evidence and pre/post stigma
surveys show distinct behavioral and meaning effects; long-run health,
household, and political outcomes remain open.
