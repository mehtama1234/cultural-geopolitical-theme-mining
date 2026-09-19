# Remedy spectrum: from explanation to collective control

**Status:** provisional cross-domain synthesis  
**Checked:** 2026-09-18

## Research question

When an AI or algorithmic system changes access to work, income, identity, or
working conditions, which institutional route can produce a usable remedy?

The current evidence does not support a binary distinction between “regulated”
and “unregulated” systems. It supports a spectrum of control points:

```text
information -> review -> correction -> compensation -> prevention -> collective control
```

Each step requires a different actor, document, time horizon, and proof of
outcome. A right at one step must not be coded as achievement of the next.

## Comparative map

| Route | System and affected group | What is directly observed | Strongest missing link |
|---|---|---|---|
| Judicial disclosure | Uber/Ola decisions affecting London drivers | A court ordered information about factors and reasons behind automated decisions, making rectification more actionable | Public proof that a driver obtained correction, reinstatement, repayment, or protection from retaliation |
| Worker-reported appeal | Ugandan taxi and delivery platform workers | Survey respondents reported appeals and favorable resolutions | Administrative or platform records identifying what changed and whether the result was durable |
| Statutory review architecture | Malaysia gig workers; EU platform workers | Disclosure, non-automated review, hearing, conciliation, Tribunal, correction, compensation, and anti-retaliation rules are formally specified at different stages; Malaysia's first Tribunal hearing is reported | Primary case records, awards, resolution times, correction rates, compensation, and enforcement |
| Institutional mediation | Kenyan Ziada workers | Staff reportedly discuss low ratings with workers and clients rather than allowing automatic discipline to settle the matter | Authority to alter the rating or consequence, consistency across workers, and recurrence prevention |
| Regulatory contestability | UK jobseekers facing recruitment scoring/filtering | ICO review, recommendations, employer commitments, and expectations for meaningful human review | A named or aggregated candidate outcome showing review changed a hiring decision or produced compensation |
| Collective bargaining | SAG-AFTRA performers facing digital replicas | Advance notice, informed consent, bounded use, and compensation rules were negotiated before routine deployment | Compliance, refusal consequences, enforcement, and whether synthetic substitution shifts bargaining power |
| Workplace co-governance | German works-council and union cases | Negotiated limits on monitoring, human oversight, data use, training, and technology review are reported | Timely worker use of the controls and measured effects on work, pay, autonomy, or job security |
| Administrative back-pay completion | Apple PERM recruitment settlement affecting protected workers | DOJ reports that individualized lost-income review processed and exhausted an $18.25m back-pay fund in 2026, alongside prospective recruitment-channel controls and monitoring; the [structured event ledger](data/apple-perm-backpay-implementation-event-ledger-v1.json) keeps completion separate from restoration | Individual payment receipt, restored job consideration, post-monitoring compliance, and whether compensation restored household or status outcomes |
| Agency-reported individual remedy | DOJ IER employment-remedy follow-ups | Four agency summaries report individual back-pay or front/back-pay payments of $5,600, $16,730, $30,000, and $8,000; a fifth reports a $485,000 full-back-pay-and-benefits offer; the [structured ledger](data/ier-individual-employment-remedy-event-ledger-v1.json) keeps these separate from independent receipt | Payment instruments, receipt, restored employment or opportunity, employer identity, durable compliance, household recovery, trust, and exit |
| Agency-reported telephone intervention | DOJ IER employment-document cases | Four selected summaries report a worker barrier followed by IER contact and employer correction, including rehire, continued work, six days of back pay, $3,400, $264, or $2,615 plus a reinstatement offer; the [structured ledger](data/ier-telephone-intervention-remedy-event-ledger-v1.json) preserves the sequence without claiming worker-confirmed recovery | Worker confirmation, payment receipt, accepted restoration, alternatives, recurrence, household recovery, trust, and exit |
| Agency-reported rehire with status repair | DOJ IER California case | One official entry reports rehire, $1,650 in back pay, and restoration of the worker's seniority date for benefits after IER corrected a document misunderstanding; the [bounded case record](ier-california-rehire-seniority-backpay-record-v1.md) keeps access, money, and status restoration separate | Independent receipt, accepted/durable reemployment, actual benefit restoration, household recovery, trust, recurrence, and exit |
| Agency-reported bilateral remedy with wage and status restoration | DOJ IER DACA employment case | One official entry reports a lower-wage rehire followed by a signed bilateral agreement restoring the prior hourly wage, paying $4,712.50 in back pay, and restoring seniority; the [bounded case record](ier-daca-rehire-wage-seniority-record-v1.md) also records complaint withdrawal as an immediate action endpoint | Payment instrument/date, wage-gap duration, durable employment, actual benefit use, household recovery, trust, recurrence, and exit |
| Adjudicated alternative-employment remedy | Fair Work Commission site-clearance case | One public case reports termination after site-clearance revocation, new lower-paid work three weeks later with significant travel costs, and an $18,192 plus superannuation compensation order; the [structured ledger](data/fwc-site-clearance-alternative-employment-remedy-event-ledger-v1.json) keeps alternative employment, trade-off, order, and receipt separate | Payment receipt, duration/equivalence of alternative work, household recovery, trust, recurrence, action, and exit |
| Adjudicated unsuccessful alternative search | Fair Work Commission Greaves case | One primary decision records unsuccessful job search, eight weeks of assessed lost income, and an $8,025 plus superannuation compensation order with a payment deadline; the [structured ledger](data/fwc-no-alternative-employment-remedy-event-ledger-v1.json) keeps search effort, unemployment, order, and receipt separate | Payment receipt, later employment, household recovery, trust, recurrence, action, and exit |
| Adjudicated non-return after workplace mechanism dispute | Fair Work Commission customer-allocation case | One primary decision records 11 job applications, new employment, a stated refusal of reinstatement because of the customer-allocation mechanism, seven weeks and five days out of work, and a $4,312 compensation order; the [structured ledger](data/fwc-alternative-employment-nonreturn-remedy-event-ledger-v1.json) keeps non-return meaning/action distinct from standardized trust and receipt | Payment receipt, job duration, standardized trust, household recovery, recurrence, switching, and exit |
| Adjudicated post-dismissal client action | Fair Work Commission McGennan appeal | One primary appeal records alternative surf-shop earnings, client redirection to an aunt's salon, relationship breakdown, and a two-instalment $6,554.33 compensation order; the [structured ledger](data/fwc-alternative-work-client-redirection-remedy-event-ledger-v1.json) keeps action, alternative income, staged remedy, and receipt separate | Instalment receipt, later work, household recovery, standardized trust, recurrence, switching, and exit |
| Formal hearing-outcome benchmark | Fair Work Commission 2020–21 to 2024–25 unfair-dismissal hearings | The Commission reports five years of hearing outcomes; monetary-only remedies are the largest named category in four years, while reinstatement-only plus reinstatement-with-lost-remuneration ranges from 5 to 21 cases per year; the [bounded benchmark](fwc-unfair-dismissal-hearing-outcomes-2024-25-record-v1.md) keeps formal result separate from receipt and recovery | Worker-level denominator, payment, accepted/durable reinstatement, household recovery, trust, recurrence, and exit |
| Adjudicated alternative employment with compensation in lieu of reinstatement | Fair Work Commission Westrip case | One primary decision records dismissal of a mechanic, five weeks to alternative employment at slightly higher pay, no income during the assessed three-week notice-period loss, and a $3,744 compensation order; the [structured ledger](data/fwc-westrip-alternative-employment-compensation-event-ledger-v1.json) keeps alternative work, non-return, income gap, order, and receipt separate | Payment receipt, job duration, household recovery, durable trust, recurrence, switching, and exit |
| Adjudicated alternative employment affecting remedy calculation | Fair Work Commission McKerrow case example | Official FWC summary reports new employment at $1,882.69 gross per fortnight plus $169.44 superannuation, a 21-day order-to-receipt window, and deductions of $2,824 wages plus $254.16 superannuation from compensation; the [bounded case record](fwc-mckerrow-alternative-employment-compensation-record-v1.md) keeps calculation separate from receipt | Job equivalence/duration, payment receipt, residual loss, household recovery, durable trust, recurrence, switching, and exit |
| Adjudicated substitute earnings during platform deactivation | Fair Work Commission Mansoor case | One primary decision records $9,000 in Baysec earnings, an estimated $1,760 increase in Didi earnings, reactivation on prior terms, and a $6,073.23 gross lost-pay order; the [structured ledger](data/uber-mansoor-alternative-earnings-lost-pay-event-ledger-v1.json) keeps substitute-work equivalence, order, receipt, and access separate | Payment receipt, actual access, alternative equivalence, durable work, household recovery, trust, recurrence, switching, and exit |
| Enforced payment without reinstatement | Fair Work Commission Meadley case example | Official FWC follow-up reports that a $24,143 compensation award was paid but the worker was not reinstated; Federal Court enforcement produced further monetary relief and a penalty; the [structured ledger](data/fwc-meadley-enforced-payment-no-reinstatement-event-ledger-v1.json) keeps payment, restoration, and enforcement separate | Alternative/non-use, later employment, household recovery, durable trust, recurrence, and exit |
| Administrator-reported worker payment distribution | Amazon Flex drivers affected by alleged tip withholding | FTC reports more than $60.6m returned through earlier payment rounds and a current Zelle route for eligible drivers who did not cash checks | Complete eligible-driver denominator, individual receipt and remaining loss, continued work, alternatives, bargaining power, and exit |
| Adjudicated access and lost-pay remedy | Tanzeel Ur Rehman and Portier Pacific, Australia | Fair Work Commission records voluntary reactivation, a formal order restoring access, and A$7,096.96 gross lost remuneration ordered after deactivation | Payment receipt, net recovery, expenses, alternative work, durable access, recurrence protection, and practical exit |
| Multi-sided platform redress | Grubhub drivers, diners, and restaurants | FTC reports more than $23.8m in payments to 640,038 affected consumers, alongside requirements for honest driver-pay advertising, blocked-account disputes, and restaurant consent | Group-specific payment and correction, implementation, continued dependence, alternatives, trust, and exit |

## What the comparison changes

### 1. Remedy is a sequence, not a label

The records can be placed on a common chain without pretending they measure the
same outcome:

```text
system becomes visible
  -> affected person or representative can identify a problem
  -> an institution can require explanation or review
  -> someone has authority to change the decision or condition
  -> money, access, identity, or status is restored
  -> the system is changed so the harm is less likely to recur
  -> workers gain collective influence before the next deployment
```

Uber/Ola is strongest at the first institutional step. Malaysia and the EU
write later steps into formal architecture. Malaysia has now crossed into a
reported first hearing, but the primary case record and outcome are still being
acquired. SAG-AFTRA and the workplace cases move earlier in time:
they condition deployment itself through collective bargaining or co-governance.

The Apple PERM settlement adds a distinct administrative-completion clock. DOJ's
2026 implementation update reports that a defined back-pay fund was processed
after individualized claimant and lost-income review. That is stronger than a
reserved fund or a stated payment obligation, but it still does not establish
that a worker received the assessed amount, regained the missed opportunity,
or encountered durable compliance in later applications. The comparison makes
three remedy states explicit:

```text
prospective obligation or reserved fund
  -> payment ordered or claimant process defined
  -> fund processed / payment completed in the administrator's record
  -> worker receipt and lived opportunity restoration
  -> durable prevention and later household or collective outcome
```

The public record can therefore advance from institutional promise to
administrative completion without closing the lived-recovery arrow. This is a
cross-domain comparison, not a pooled remedy rate: the Apple record concerns
employment-channel discrimination and back pay, while the platform cases
concern access restoration, lost remuneration, and continued use.

The IER follow-ups add a narrower but important stage: an agency can report a
payment tied to an individual charging party without exposing the payment
instrument, independent receipt, restored job opportunity, or later household
outcome. These records therefore sit between an aggregate fund-completion
claim and a verified lived-remedy episode. The four reported payments and the
separate $485,000 offer must not be pooled into a worker recovery rate or
joined to the Apple fund without a shared episode key.

The telephone-intervention records add a different kind of strength. They
retain a short chronology from employment-document barrier, to worker or
advocate contact, to IER explanation, to an employer decision. Several records
also report rehire, continued work, or back pay. That makes the institutional
intervention arrow more concrete than a prospective policy statement, but the
public summaries still end before worker confirmation, accepted restoration,
household recovery, trust, or exit. They are therefore useful remedy-stage
comparators, not evidence of durable individual recovery or prevalence.

The California January 2023 example adds a status-restoration endpoint within
that same intervention family. The official account reports rehire, $1,650 in
back pay, and restoration of the worker's seniority date for benefits. Seniority
is not just another payment: it is a continuity and future-benefit position.
The case therefore separates three immediate remedy currencies—access, money,
and status—while still leaving receipt, actual benefit use, durability,
household recovery, trust, and exit open.

The Fair Work Commission site-clearance case adds the missing-choice stage in a
bounded way. The public summary records that the worker obtained alternative
employment three weeks after dismissal, but at lower remuneration and with
significant travel costs. That is stronger than an inferred alternative: it is
a same-case reported transition and trade-off. It still does not establish
that the alternative was freely chosen among viable options, that the ordered
compensation was paid, or that the worker or household recovered.

The Greaves decision supplies the counterexample. The worker sought alternative
employment but had not secured work by the hearing, and the Commission assessed
an eight-week loss before ordering compensation. Together, the two cases show
that “adaptation” must distinguish obtained replacement work from unsuccessful
search effort and continued unemployment; neither outcome establishes receipt
of the legal remedy or later recovery.

The customer-allocation case adds a bounded meaning/action signal. The worker
applied for 11 jobs, obtained a new role, and stated that she did not want
reinstatement because of the employer's customer-allocation mechanism. This is
stronger than inferring distrust from a complaint alone, but it remains a
case-level attribution rather than a standardized trust measure; the order's
payment and the later trajectory remain open.

The McGennan appeal adds a second action comparator: after dismissal, the
worker earned roughly $2,000 at a surf shop and referred former clients to her
aunt rather than working from home. The appeal records relationship breakdown
and a staged compensation schedule, but no instalment receipt or later
trajectory. This distinguishes immediate post-dismissal action from durable
exit or recovery.

The McKerrow example adds a narrower remedy-calculation mechanism. The worker
had already started new employment, and the Commission deducted expected wages
and superannuation during the 21-day order-to-receipt interval. This shows that
alternative work can reduce the formal award while the public record remains
silent on job equivalence, search cost, payment receipt, and household
recovery. It is therefore a calculation-stage comparator, not evidence that
the worker was made whole.

The Commission's five-year hearing table supplies a broader denominator for
the institutional stage: monetary-only outcomes are the largest named
category in four of the five years, while any reinstatement outcome ranges
from 5 to 21 cases per year. This does not mean money is the wrong remedy or
that reinstatement would have worked. It does mean the case-level atlas should
keep compensation, access restoration, and durable workplace correction as
separate remedy currencies rather than calling all of them “resolution.”

The Meadley case closes a different remedy clock. The official FWC account
reports payment of the compensation award but failure to reinstate the worker;
court enforcement then produced further monetary relief and a penalty. This is
the clearest retained counterexample to treating payment as restored opportunity.

Amazon Flex adds a fourth observable point on the same spectrum: distribution
has occurred and the administrator is still addressing uncashed payments. That
is a stronger implementation record than an order alone, but it remains a
program-level endpoint. Without the eligible-driver denominator and a
driver-level follow-up, the record cannot tell us who received what, whether
the remaining loss was resolved, or whether the payment changed work choices,
trust, or collective power.

The Rehman case adds a distinct adjudicated comparator between an order and
lived recovery. The worker regained access voluntarily before the Commission's
formal decision, yet the Commission still issued a concurrent reactivation
order and ordered A$7,096.96 gross lost remuneration. Access restoration and
financial restoration are therefore separate remedy outputs even within one
case. The amount is not payment receipt or net household recovery; the decision
also records no expense evidence and the public record does not establish
alternative work, durable protection, or later exit. This makes the case useful
for stage coding, not for estimating platform-wide fairness or worker welfare.

### 2. Timing changes the power balance

An appeal after a deactivation or rejection asks a person to recover a lost
opportunity. Consent, bargaining, or technology review before deployment can
change the rule before the loss occurs. That does not make pre-deployment voice
automatically effective: refusal may carry a hiring cost, and a written
agreement may lack enforcement. It does mean that “remedy” should record when
the intervention occurs, not only whether a formal right exists.

### 3. Human presence is not human control

The Kenya and UK records make a useful distinction. A person may discuss a
rating or inspect an automated recommendation without having authority to
change the score, reverse the outcome, or prevent future penalty. The minimum
meaningful-review test therefore has three fields:

```text
reviewer sees the actual decision
reviewer can disagree with the system
reviewer can change the consequence
```

If any field is unknown, the evidence should remain at “human involvement” or
“review expectation,” not “effective human oversight.”

### 4. Collective control reaches different objects

The records do not all contest the same thing. Courts contest information;
statutes specify procedures; regulators specify compliance expectations;
mediators handle a live rating dispute; and unions negotiate identity, consent,
pay, workload, or deployment conditions. The atlas should therefore code the
object of control separately:

```text
information | decision | consequence | payment | data/identity | workflow | deployment
```

This prevents a contract over digital replicas from being treated as proof that
an employment platform can correct a deactivation, while still recognizing
both as evidence about who can govern work systems.

Malaysia's first Tribunal hearing adds an access-to-justice test to the remedy
chain. The Act's no-lawyer design may make a low-value dispute affordable, but
the absence of lawyers does not prove parity between an individual worker and a
platform employee with access to organizational records. Future case records
should code representation, data access, preparation support, and technical
assistance alongside the formal right to appear.

## Provisional theme

The emerging cultural and geopolitical theme is **proceduralization without
yet-proven recovery**. Across jurisdictions, institutions are translating
opaque technical functions into notices, review rights, consent clauses,
consultation duties, and dispute routes. The unresolved power question is
whether those procedures move control over the underlying opportunity, income,
identity, or workflow—or merely make an adverse system easier to describe.

This is a theme, not a causal conclusion. The current evidence is deliberately
heterogeneous: court records, legislation, regulator materials, surveys,
institutional case studies, and collective agreements. It supports a mechanism
map and a disciplined acquisition plan, not a ranking of countries or a pooled
remedy rate.

## Next evidence needed

For each route, acquire one artifact that crosses the missing link:

1. a post-order Uber/Ola record showing correction or restoration;
2. a Ugandan platform or worker-organization record itemizing a favorable appeal;
3. the primary record or award for Malaysia's reported first GrabCar Tribunal
   hearing, or an EU case showing a review, correction, payment, or sanction;
4. a Kenya Ziada case documenting authority to alter the rating or consequence;
5. an ICO follow-up outcome with a defined candidate or organization denominator;
6. a SAG-AFTRA enforcement or use record showing consent, payment, or refusal effects;
7. a workplace agreement implementation record showing worker use and outcome.
8. for an administratively completed fund, a claimant-level or audited
   implementation artifact showing payment receipt, timing, deductions, and
   whether the original opportunity or a comparable alternative was restored.
9. for an adjudicated access-and-lost-pay order, a compliance or worker-side
   follow-up showing payment receipt, net expenses, continued access, and
   alternative work or exit.

The acquisition schema should preserve the intervention date, decision object,
actor, reviewer authority, changed consequence, money or access restored,
recurrence prevention, and retaliation evidence.

## Linked evidence

- [Global platform-work remedy comparison](global-platform-remedy-comparison-v1.md)
- [Platform-work remedy case ledger](platform-remedy-case-ledger-v1.md)
- [UK ICO recruitment remedy record](uk-ico-automated-recruitment-remedy-record-v1.md)
- [UK ICO follow-up acquisition audit](uk-ico-recruitment-follow-up-acquisition-audit-2026-09-15.md)
- [SAG-AFTRA digital-replica source record](sag-aftra-digital-replica-source-record-v1.md)
- [IBM Germany works-council AI framework governance record](ibm-germany-works-council-ai-framework-governance-record-v1.md)
- [Microsoft Germany works-council Copilot deployment record](microsoft-germany-works-council-copilot-deployment-record-v1.md)
- [ILO social-dialogue case table](ilo-social-dialogue-case-table-v1.md)
- [Rehman adjudicated platform-remedy record](uber-rehman-remedy-record-v1.md)
- [Rehman canonical trend record](../../records/au-rehman-platform-remedy-2026.json)

## Boundary

This synthesis does not claim that any route is effective in general. It
distinguishes observed rules and practices from verified worker outcomes and
keeps public non-observation separate from proof of absence.
