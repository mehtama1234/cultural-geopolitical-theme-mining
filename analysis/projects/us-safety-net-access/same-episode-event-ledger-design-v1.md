# Same-episode public-system event ledger design v1

**Purpose:** make the public-system arrow measurable across many people,
places, channels, and program episodes. This is a population study design,
not a one-household narrative.

## The broad question

When people need public help, does the system convert eligibility into usable
security, or does the route to help redistribute time, work, food, debt, trust,
and political voice?

The unit is a dated program episode. The population is a stratified sample of
episodes, not a single case. Strata should include state, urban/rural place,
program, renewal versus new application, access channel, language or
disability accommodation, and eventual result.

## Sequence to capture

```text
need or rule exposure
  -> notice and route
  -> effort, delay, decision, and correction
  -> receipt, interruption, reduction, denial, or exit
  -> material and time outcomes
  -> interpretation, complaint, collective action, or silence
  -> agency or policy response
```

Every arrow gets a date, source type, denominator, missingness flag, and
confidence label. Administrative records establish the process and result;
respondent reports establish effort, meaning, and unrecorded alternatives;
follow-up measures establish recovery. Researcher interpretation remains a
separate field.

## Minimum linked records

| Layer | Record | Population-level question |
|---|---|---|
| Need | need category, onset, severity, competing expense | Which pressures bring people to the system? |
| Route | notice, language, channel, documents, attempts, hours, travel, childcare, accommodation | Who can complete which route, and at what cost? |
| Decision | eligibility, verification, denial/reduction, deadline, appeal, correction | Where does administration convert need into access or loss? |
| Material result | benefit amount/timing, gap days, food, work, debt, health, housing, transport | What does a successful or failed route protect or displace? |
| Meaning | comprehension, fairness, dignity, blame, trust, information source | How is the encounter interpreted? |
| Action | complaint, appeal, official contact, organizing, turnout, vote, no action | Which interpretations become public behavior? |
| Response | agency correction, rule change, office/channel change, outreach | Does the institution learn or reproduce the burden? |

## Comparison cells

The primary comparisons are:

1. similar need, different channel or language access;
2. similar eligibility, different notice or deadline;
3. approved without interruption versus delayed or denied;
4. exit with measured improvement versus exit without improvement;
5. eligible non-applicant versus applicant who received help;
6. same place and period before versus after an office or rule change.

Do not pool these into a single “take-up” rate. Report each cell’s universe,
weights, attrition, and unknown reasons. A person who never applies is not the
same as a person who applies and is denied.

## Estimands, in order

- route cost: time, money, and failed attempts by access route;
- process result: approval, delay, interruption, correction, and gap days;
- material displacement: change in food, work, debt, health, housing, or care;
- meaning: attribution and fairness conditional on the documented episode;
- action: complaint, appeal, organizing, turnout, vote, or no action;
- institutional response: whether a reported failure produces correction.

The later estimands are not inferred from the earlier ones. A benefit loss is
not automatically food insecurity; food insecurity is not automatically distrust;
and distrust is not automatically a vote.

## What would count as a real broad finding

A finding must replicate across a defined population or place comparison, show
the relevant arrow in time, retain a counterexample, and state what remains
unobserved. The strongest result would show that route or rule differences
change material security and that the same episode also changes attribution or
public action. Separate results—such as higher burden, more interruptions, or
lower trust—remain useful but must be named at their own stage.

## Immediate implementation

Build a consented, pseudonymous episode table with linked administrative,
survey, and follow-up records. Pilot across multiple states and channels,
pre-register the comparison cells, publish a missingness table, and release a
de-identified codebook before interpreting political consequences.

Related: [safety-net event ledger template](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md),
[public-system meaning/action gap](public-system-meaning-action-gap-v1.md), and
[public administration, take-up, security, and political feedback](public-administration-takeup-security-trust-action-layer-v1.md).
