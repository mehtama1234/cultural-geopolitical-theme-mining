# Project: US cost of living, trust, and political response

## Question

How do ordinary costs—food, housing, health care, energy, and debt—turn into trust, blame, identity, and political demand?

## Short end-to-end goal

Follow a real household experience from the bill or lost benefit to what the person does next, then test whether that experience changes how people judge firms, government, parties, or the economy.

```text
price, income, benefit, or job change
  -> household adjustment or loss
  -> view of personal and national conditions
  -> trust, blame, identity, or political demand
  -> policy, firm, media, or voting response
```

Do not assume that a bad economic view comes from a bad personal outcome. Test personal experience, party identity, news, local conditions, and policy changes separately.

The next executable design is the [political-response measurement specification](political-response-measurement-spec-v1.md). It keeps exposure, adjustment, interpretation, expression, and political action separate and defines the valid respondent, place, and event-study alternatives.

The [ANES 2024 source record](anes-2024-political-path-source-record-v1.md) maps a current respondent-level pre/post political layer to that design. It records the official acquisition boundary and does not claim new estimates until the current microdata release is obtained.

The [ANES 2024 political judgment layer](anes-2024-political-judgment-layer-v1.md) now adds weighted, complex-design cross-tabs for financial worry against national economic judgment, federal-government trust, and reported presidential vote. It is a separate respondent-level layer beside SHED, not a join to SHED or a causal economic-voting result.

The [economic adaptation, perception, and public action layer](economic-adaptation-perception-action-layer-v1.md)
records the broader cross-source distinction: consumer adaptation,
economic judgment, institutional trust, cultural meaning, and civic/political
action are separate measured outcomes. It keeps the missing attribution and
longitudinal middle visible.

## First working idea

People may judge the economy through the loss of choices—what they delay, stop, borrow for, or ask family to cover—not only through income. A policy can therefore change public feeling even after the direct money effect fades. This is a working idea, not a conclusion.

## Scope

- US households, customers, workers, voters, firms, and public institutions;
- prices, benefits, wages, debt, housing, health care, and energy;
- personal experience versus views of the national economy;
- differences by income, race, age, party, family type, and place;
- policy changes and firm behavior only where the timing and path can be checked.

## Writing rule

Use simple words. Say what changed, who felt it, what they did, and who they blamed. Do not call something “polarization,” “populism,” or “loss of trust” unless the survey or behavior measure shows it.
