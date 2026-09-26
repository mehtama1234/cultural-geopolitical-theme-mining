# Finding 029: Insurance restitution can be paid while household recovery remains unknown

**Status:** bounded insurance-remedy and institutional-correction finding · **Checked:** 2026-09-19

## The bounded finding

The Virginia State Corporation Commission's public settlement summaries show
three different insurance failures followed by both reported restitution and
prospective correction:

| Matter | Reported exposure | Reported response | Still unknown |
|---|---|---|---|
| Esurance | Premium increases or rating points after accidents without required notice | About $2 million to 2,959 consumers plus a corrective plan | Individual receipt, corrected premium, coverage continuity, and trust |
| State Farm | Policies or premiums inconsistent with filed rate information | About $2.5 million to 91,696 consumers plus filing/rating controls | Person-level amount, receipt, renewal, and switching |
| Anthem/Carelon | Contracting, credentialing, network, demographic, and fee-schedule problems affecting claims/provider payments | About $346,000 to 1,680 consumers and 586 providers, $118,000 to Virginia, plus claims/vendor controls | Corrected claims, completed care, network restoration, patient cost, and provider retention |

The important distinction is between **reported payment** and **lived
recovery**. The regulator reports that restitution was paid, but the public
record does not identify individual receipt, adequacy, account or premium
correction, restored coverage/care, residual cost, trust, or switching.

## The chain

```text
rating, notice, network, or claims error
  -> consumer/provider financial or access burden
  -> regulator investigation and settlement
  -> reported restitution + corrective process
  -> individual receipt/correction [open]
  -> restored security, coverage, care, trust, or switching [open]
```

This strengthens the atlas's remedy-to-recovery lane because it contains more
than a complaint or an order: it contains regulator-reported aggregate payment
and a forward-looking system-control response. It still does not justify a
remedy-success rate or a claim that affected households recovered.

## Limits and next field

- The three matters are institution-level summaries, not a representative
  consumer sample.
- Aggregate restitution is not a recipient-level payment file.
- A corrective-action plan is not proof of a lower future error rate.
- The next decisive artifact is a lawful policy-, claim-, or recipient-level
  follow-up showing payment, correction, coverage/care continuity, remaining
  cost, recurrence, trust, or switching.

The [structured insurance-settlement ledger](../data/virginia-scc-insurance-settlement-remedy-event-ledger-v1.json)
preserves the three matters separately. The [Virginia SCC settlement summaries](https://www.scc.virginia.gov/about-the-scc/scc-facts/)
are the official source boundary.
