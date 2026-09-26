# Finding 034: A remedy plan can formally recognize the reachability problem

**Status:** bounded official redress-design finding · **Checked:** 2026-09-19

## What the record shows

In a 2016 CFPB consent order, the required redress plan had to explain how the
company would locate affected consumers and follow up when redress payments
were returned as undeliverable or remained uncashed. The order also required a
process for deciding when the redress process was complete.

This is important because the institution itself treats mailing a payment as
an incomplete endpoint. The plan contains a second route for people who cannot
be reached through the first payment route.

## The end-to-end implication

```text
formal redress order
  -> locate affected consumer
  -> issue payment
  -> payment returned or remains uncashed
  -> follow-up / address correction / additional contact
  -> [open] cashing, account correction, adequate recovery, trust, or exit
```

The finding advances the remedy-reachability mechanism. It does not show how
many people were ultimately paid, whether the payment corrected the underlying
account, whether the amount was adequate, or whether consumers changed use,
trust, or switching behavior afterward.

## Why it belongs in the broad atlas

Across refunds, public benefits, disaster aid, worker remedies, and consumer
redress, the visible institutional endpoint is often earlier than the lived
endpoint. A formal plan may contain a follow-up mechanism, but that mechanism
is still not the same as a completed person-level recovery record.

The required episode fields are therefore separate:

- eligible or affected;
- payment issued;
- payment delivered and cashed;
- account or loss corrected;
- later financial security, trust, continued use, switching, or exit.

## Boundary

This is evidence about remedy design in one official consent order, not a
payment-completion rate and not evidence that the company failed to follow the
plan. It should be used to sharpen data requirements, not to infer an outcome
for affected consumers.

## Later formal-completion stage

The CFPB's case page says the order was terminated on December 20, 2022. The
termination document states that Wells Fargo had fulfilled its obligations,
including remediation to specified consumers, policies for accurate student-
loan furnishing, and redress of inaccurate furnishing. This closes a formal
institutional stage in the route:

```text
redress design and reachability obligations
  -> agency-reported fulfillment
  -> order termination
  -> [open] borrower-level receipt, account correction, adequacy, and recovery
```

The later status is important, but it is not a person-level payment file. It
does not tell us which borrowers were reached, whether payments were cashed,
whether every account was corrected, or whether financial security, trust,
switching, or exit changed.

Source: [CFPB Wells Fargo consent order](https://files.consumerfinance.gov/f/documents/2016-CFPB-0013Wells_Fargo_Bank_N.A.--_Consent_Order.pdf), §§74–75, pp. 22–23.
The later [CFPB termination order](https://files.consumerfinance.gov/f/documents/cfpb_wells-fargo-na-2016_consent-order-termination_2022-12.pdf)
states that the respondent fulfilled its obligations as of December 20, 2022.
