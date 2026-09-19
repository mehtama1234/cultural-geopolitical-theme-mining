# Remedy implementation is not the same as lived recovery v1

**Checked:** 2026-09-19  
**Status:** cross-domain synthesis of retained public case records; no pooled
recovery rate

## The finding

The strongest records in the atlas now travel beyond exposure and institutional
response. They show reported payment, restored work access, restored wage or
seniority, repeated post-restoration use, provider switching, or a worker's
decision not to return. Those endpoints are not interchangeable.

```text
harm or exclusion
  -> complaint / intervention / adjudication
  -> order, offer, correction, or reported payment
  -> access or money actually used
  -> durable security, trust, alternative choice, or exit
```

The portfolio is strongest in the middle of this chain and thins sharply at the
last step. A remedy can be implemented while recovery remains partial; access
can return while lost pay remains unresolved; payment can be reported while
receipt, adequacy, and later security remain unknown; and switching or
non-return can occur without proving that a viable alternative existed.

## What the cases establish

| Case surface | Strongest retained endpoint | What remains open |
|---|---|---|
| DOJ IER telephone interventions | Agency-reported return to work, back pay, alternate-location access, or a worker non-return decision; one case states the worker returned the next day and was paid about $420 | Independent receipt, wage adequacy, durable employment, household recovery, trust, recurrence, and exit |
| DOJ IER wage/seniority cases | Agency-reported rehire, back pay, prior-wage restoration, and seniority restoration in individual cases | Payment instrument and receipt, actual benefit use, tenure continuity, later security, and trust |
| Hotak platform case | Same worker's access was restored, ordinary post-restoration work payment was reported, and more than 150 later trips were recorded | Separate lost-remuneration payment, net recovery, later access, non-retaliation, alternatives, and exit |
| FTC Yellowstone refund | 3,759 small businesses receiving a third distribution had cashed a previous check | Whether the third check was cashed, account harm was corrected, business recovery, continued use, switching, and trust |
| SHED fraud route | Respondents reported provider contact, external reporting, and some provider switching after fraud | Account-level causation, completed switch, replacement quality, verified recovery, and restored trust |
| CCES job-loss panel | Same respondents show later Congress contact and local political action after a work-disruption screen | Dated separation, attribution, remedy, recovery, trust change, and whether lower action reflects constraint or choice |

These records answer different questions. “The institution acted,” “the
recipient reportedly received or used something,” “the person kept using the
service,” and “the person recovered or could leave” must remain separate fields.

## The deeper pattern

The cases suggest four practical currencies of remedy:

1. **Access:** the person can work, transact, receive a service, or return to
   an account.
2. **Money:** a payment, refund, back pay, or replacement amount is reported.
3. **Status and continuity:** seniority, prior wage, workplace location, or
   account terms are repaired.
4. **Choice:** the person can continue, switch, refuse return, use an
   alternative, or exit without carrying an unmeasured penalty.

The first three can improve while the fourth remains constrained. This is why
“remedy implemented” is not a household recovery measure and why “continued
use” is not proof of satisfaction. A worker may return because the job is
necessary; a customer may switch because the provider failed; a recipient may
cash a payment while still carrying residual loss; and a person may not return
because the original workplace is no longer acceptable, because another option
exists, or because the cost of returning is too high.

## Coding consequence for the atlas

The next evidence pass should not add another generic response count. It should
seek, for one already identified episode:

```text
reported remedy
  -> dated receipt or actual access
  -> amount / adequacy / continuity
  -> later recurrence or persistence
  -> trust, alternative use, switching, non-use, or exit
```

The minimum acceptable follow-up must preserve the same unit and distinguish:

- agency or firm report from recipient confirmation;
- ordinary post-restoration earnings from lost-pay recovery;
- a payment amount from money actually received and adequate;
- a switch attempt from completed replacement use;
- non-return or non-use from successful exit; and
- later political contact or action from remedy or recovery.

## Boundary

This synthesis is a structured interpretation of selected public records. The
cases are not representative, the units are not pooled, and the evidence does
not support a population recovery rate or a claim that remedies generally fail.
The defensible conclusion is narrower: public records document institutional
steps and selected implementation endpoints more readily than they document
whether the affected person regained durable security, trust, or practical
choice.

## Source records

- [IER telephone-intervention ledger](projects/ai-work-control/data/ier-telephone-intervention-remedy-event-ledger-v1.json)
- [Hotak platform-remedy ledger](projects/ai-work-control/data/uber-hotak-end-to-end-event-ledger-v1.json)
- [Yellowstone refund ledger](projects/us-customer-automation-recourse/data/ftc-yellowstone-refund-event-ledger-v1.json)
- [SHED fraud and switching ledger](projects/us-financial-intermediation/data/shed-fraud-recovery-switching-event-ledger-v1.json)
- [CCES job-loss political-action ledger](projects/us-cost-trust-politics/data/cces-job-loss-political-followup-event-ledger-v1.json)
