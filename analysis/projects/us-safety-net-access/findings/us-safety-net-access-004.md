# The SNAP route can change receipt before it changes security

## The end-to-end finding

The public system is not experienced as a simple transfer. It is a sequence of notices, deadlines, interviews, documents, offices, software, eligibility decisions, benefit issuance, and renewal. The evidence now supports a bounded end-to-end conclusion:

**Route design can change whether people receive or retain SNAP, while receipt and exit remain separate from material security. The recipient-side experience includes time, notice, paperwork, and interview failures that state processing metrics cannot see. Trust, blame, appeal, and political action remain unmeasured rather than inferred.**

This conclusion comes from four evidence layers that are intentionally not pooled.

## Four layers, four units

| Layer | Unit and design | Main evidence | Boundary |
|---|---|---|---|
| USDA/FNA timeliness | State aggregates; FY2025 quality-control measures | APT ranges 61.24–97.22%; RPT ranges 25.23–99.87% across 51 states/DC; participation–APT correlation is 0.033 | Does not observe household effort, notice comprehension, benefit gap, or remedy |
| Urban WBNS | Working-age adults in SNAP families; retrospective weighted survey | 24% reported involuntary interruption; 13% cited inability to recertify on time; among n=182, 40% lacked enough time after notice and 32% did not receive notice | Does not link respondent to a case file or verify dates, amount, agency fault, or correction |
| NBER studies | Study-specific applicants, administrative cases, and place/policy settings | Flexible interviews increased approvals and longer-term participation; office closures reduced participation; work requirements produced exits without the intended employment response in studied populations | Effects are design- and setting-specific; downstream security and political meaning are not measured |
| Census SIPP | Person-month transitions with Fay-BRR weights | Following-month rent hardship: 16.40% after no→yes, 11.53% after yes→no, 11.98% after yes→yes; utility hardship: 20.80%, 20.83%, 18.61% | Descriptive transitions; no same-episode notice, amount, remedy, trust, or action |

The denominator differences are not a nuisance. They are the reason the synthesis can be honest.

## What the state metrics cannot see

The USDA/FNA state layer shows that population participation is not a route-quality score. Across the 51 state/DC aggregates, FY2025 participation has almost no unweighted association with APT (`r = 0.033`) and only a small association with RPT (`r = 0.211`). That does not mean administrative performance is irrelevant. It means that high participation may coexist with poor handling, and low participation may coexist with strong handling.

The WBNS explains what a route failure can look like to a person. Among those reporting an interruption because they could not recertify on time, the barriers include:

- not enough time after receiving a notice: 40%;
- no notice about the need to recertify: 32%;
- paperwork too difficult to understand or complete: 22%;
- inability to participate in a required interview: 16%; and
- an office losing paperwork or documentation: 15%.

These are multiple-response reports, not a decomposition of agency responsibility. But they show why “processed on time” and “had a usable opportunity to retain benefits” are related rather than identical concepts.

## What the intervention studies add

The NBER evidence supplies stronger leverage on route mechanisms than a cross-sectional comparison. The Los Angeles flexible-interview field experiment found that allowing applicant-initiated flexible interviews increased approvals by about 6 percentage points, doubled early approvals, and increased longer-term participation by more than 2 percentage points. A separate office-access study found that closing an enrollment office reduced tract SNAP participation by 7–9% over two years. Work-requirement studies found large participation exits without the intended employment response in the studied populations.

Together these results support a narrow causal claim: **the route can alter observed participation.** They do not support the larger claim that any exit is wrongful, that any processing delay causes food insecurity, or that a changed route necessarily changes political trust.

## What the SIPP outcome layer prevents us from saying

The SIPP transition comparison blocks two common shortcuts. First, exit is not automatically recovery: following-month rent hardship remains 11.53% after yes→no transitions and utility hardship 20.83%. Second, continued receipt is not complete security: the yes→yes group reports 11.98% rent hardship and 18.61% utility hardship in the following record.

Entry is also a marker of pressure rather than proof that SNAP caused hardship: the no→yes group has 16.40% rent hardship and 20.80% utility hardship in the following month, but entry cases are selected by need, eligibility, household composition, and other shocks.

## The surviving mechanism chain

```text
need / eligibility / rule exposure
  → notice, office, interview, paperwork, deadline
  → approval, procedural denial, interruption, churn, or continued receipt
  → benefit timing and amount
  → food, housing, utility, work, health, and time security
  → fairness, trust, complaint, appeal, organizing, or vote
```

The first four stages now have distinct evidence. The final stage remains open. Meaning cannot be inferred from a denial, and political action cannot be inferred from a benefit transition.

## Falsification and next gate

This synthesis should be revised if linked evidence shows that notice and paperwork barriers do not predict interruptions, route changes affect only ineligible cases, work-requirement exits are consistently followed by improved security, or exits are generally followed by reduced hardship after amount and remedy are observed.

The next acquisition is a de-identified, linked or matched episode table with:

`notice → route attempts → documents/interview → decision → expected/received amount → gap days → correction/appeal → material outcome → fairness/trust → action → recovery/reentry`

Until that exists, the atlas should preserve this as a strong triangulated mechanism map—not a closed causal story.

## Sources and reproducibility

- [Cross-source triangulation layer](../public-system-route-to-security-triangulation-v1.md)
- [Machine-readable synthesis record](../../../records/us-public-system-route-security-triangulation-2026.json)
- [USDA/FNA state route-performance finding](us-safety-net-access-002.md)
- [Urban WBNS lived-route finding](us-safety-net-access-003.md)
- [WBNS public-use route acquisition audit](../wbns-public-use-route-acquisition-audit-v1.md)
- [SNAP administrative-burden paper scan](../snap-administrative-burden-paper-scan-v1.md)
- [SIPP transition × following hardship](../sipp-snap-transition-outcome-fay-brr-layer-v1.md)
