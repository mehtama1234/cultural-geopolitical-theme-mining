# Named workplace system stage ledger v1

**Status:** bounded stage comparison; no worker-welfare, household-security, or
exit estimate
**Checked:** 2026-09-17
**Machine record:** [named workplace system stage ledger](data/named-workplace-system-stage-ledger-v1.json)

## What this adds

The broad program asks whether a technological or organizational capability
changes not only productivity, but also control, security, meaning, action, and
power. The existing local AI/work records contain named governance and
deployment cases, but their stages were distributed across separate records.
This ledger puts those cases against one common sequence without treating them
as one workplace or one causal experiment.

```text
named system and owner
  -> dated rule or implementation
  -> worker exposure
  -> worker voice
  -> specific control or rule change
  -> enforcement / appeal
  -> worker outcome
  -> household outcome
  -> exit or collective action
```

## Stage comparison

| Named system | Highest supported stage | What remains open |
|---|---|---|
| IBM Germany AI framework | Anticipatory governance rules and representative architecture | Live exposure, intervention, enforcement, worker/household outcomes, exit |
| Microsoft Places | Company-reported product change: country targeting and default opt-out; current official docs specify consent, override, policy scope, and Inform/Ask/Off controls | Actual tenant mode, exposure, opt-out consequence, enforceability, privacy/work outcomes, household effects |
| Microsoft 365 Copilot | Company-reported controlled rollout and representative feedback loop | Specific feature change, review enforcement, worker outcomes, household security, exit |
| OpenAI/Statsig PERM recruitment | DOJ settlement with potential back-pay fund, electronic-application restoration, claimant process, reporting, and three-year oversight | Actual claimant eligibility/payment, restored consideration, implementation logs, household effects, and later behavior |
| Apple PERM recruitment | DOJ reports $18.25m back-pay fund processed and exhausted after individualized lost-income review; external/electronic recruitment controls and monitoring required | Individual payment distribution, restored consideration or hiring, post-monitoring compliance, household effects, and later behavior |

## Interpretation

The cases support a narrow institutional proposition: worker representation can
enter before or during deployment, and in one named product case the company
reports a design change tied to council concern. That is meaningful evidence of
a governance conversion point. It is not evidence that participation created a
veto, that the rule was enforced, or that workers became safer, more autonomous,
better paid, or more secure.

The missing middle is now explicit. We need an artifact that links a specific
concern to a dated rule or feature change and then observes who encountered it,
whether an override or appeal worked, what happened to pace, workload, pay,
health, schedule control, and bargaining, and whether the effect reached the
household or changed staying, switching, quitting, or organizing. A differently
governed workplace is required to avoid converting a named company account into
a general societal trend. The OpenAI/Statsig case adds a US access-and-remedy
route: a recruitment channel can impose unequal effort before a hiring
decision, and enforcement can specify both potential compensation and
technical access repair. The agreement still does not establish payment or
restored opportunity.

The Apple event adds a remedy-completion comparator to the named-system set: a
public implementation report can establish that a monetary fund was processed
and exhausted, while leaving lived opportunity restoration and durable worker
control unmeasured. The Microsoft Places technical-control note adds a limited
corroboration layer:
official product documentation makes user override, administrator geography,
consent, and historical-data boundaries inspectable. That moves the case beyond
a purely narrative claim about what the product can do. It does not show which
setting Microsoft Germany used, whether workers actually opted out, or whether
the controls changed lived privacy, schedule control, workload, or bargaining
power.

## Reproduction

```text
python3 scripts/validate_named_workplace_system_stage_ledger.py
```

The validator checks five committed local records plus the linked technical
source note and downloads nothing.
