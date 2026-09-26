# Platform remedy, restoration, and dependence

**Status:** provisional case-level synthesis  
**Checked:** 2026-09-18

## Research question

When a platform worker challenges an access restriction, what can the public
record actually show about restoration, lost-value recovery, continued use, or
exit?

The answer in the current case ledger is narrow but important: adjudication can
make restoration and lost remuneration visible, while the later relationship
between remedy and platform dependence remains mostly unobserved. A returned
account is not an exit, and an ordered payment is not evidence that the worker
received it.

## Ledger screen

The machine-readable ledger contains 27 case or comparative records. It is a
case inventory, not a representative sample or an effectiveness rate. A
manual screen of the stage fields gives the following descriptive map:

| Outcome surface | Records with the outcome visible | What that means |
|---|---:|---|
| Restoration or access resumption observed | 8 | An order or recorded resumption makes access visible in the case record; durability varies |
| Lost remuneration or earnings ordered / recognized | 3 | A formal monetary remedy is visible; receipt is not thereby established |
| Lost remuneration left open or directed for later calculation | 5 | The entitlement or issue is visible, but amount or payment remains unresolved |
| A merits-level refusal or dismissal observed | 4 | Review can produce a reasoned negative result; this is not proof the original system decision was accurate in general |
| Durable recurrence prevention observed | 0 | No record currently proves that the platform rule or process changed for future cases |
| Worker exit or platform switching after the event observed | 0 | No record currently links the remedy episode to leaving, switching, or independent recovery |

The counts overlap: a reactivation order can also carry a lost-pay order, and a
single case can have an open implementation field. The first four rows should
therefore never be summed into a single “success” total.

## What the Australian cases add

The Australian Fair Work Commission records provide the strongest visible
remedy chain in the ledger. They expose several distinct endpoints:

```text
challenge -> procedural finding -> reactivation or access resumption
                         -> lost remuneration order or open quantum
                         -> receipt / durable access / future rule change
                         -> later continued use, switching, or exit
```

The chain is complete only through selected middle stages. The records include
formal reactivation orders, recorded voluntary reactivation followed by more
than 150 trips, and orders or findings concerning lost remuneration. Other
records show the opposite boundary: a sufficient human-review process and
merits dismissal, an eligibility dismissal that never reaches fairness, or a
procedural defect without an unfairness remedy. These contrasts are useful
because they prevent “human review” from being treated as synonymous with
reversal.

The strongest individual records currently visible are:

- **PR-013 / Bandameeda:** reactivation on prior terms and a $12,126.31 lost-
  remuneration order are visible; payment receipt, durability, and
  anti-retaliation are not.
- **PR-018:** voluntary reactivation is recorded alongside a formal order and
  a $7,096.96 gross lost-remuneration order; downstream receipt and recurrence
  prevention remain open.
- **PR-019 / Hotak:** voluntary reactivation and more than 150 subsequent trips
  are recorded; that is evidence of continued platform use after restoration,
  not evidence that the worker lacked alternatives or freely chose dependence.
- **PR-020:** reactivation and a $6,073.23 gross lost-earnings order with a
  payment deadline are visible; actual receipt remains unobserved.
- **PR-022 / Waheed:** a 16 June 2026 appeal-stay order makes a $259.38-per-week
  interim payment obligation visible from 28 May 2026, but receipt, actual
  access, final quantum, and appeal outcome remain unobserved.
- **PR-021, PR-016, and PR-017:** reactivation or reactivation orders are
  visible while lost-pay quantum, payment, or implementation remains open.

### Structured end-to-end comparison

The two deepest same-case routes now have a shared event-ledger representation.
The table is a stage map, not a comparison of worker welfare or remedy
effectiveness:

| Case | Exposure / challenge | Access or work after challenge | Ordered money | Receipt / durable access | Meaning, action, exit |
|---|---|---|---|---|---|
| Hotak / Uber | Deactivation on 8 Apr 2025; worker challenged through the FWC route | Voluntary reactivation on 19 May; more than 150 trips recorded by 21 Jul; later formal reactivation order | Lost-remuneration quantum remains open; ordinary post-reactivation work payment is distinct from lost-pay recovery | Receipt, later access, recurrence prevention, and anti-retaliation not observed | Alternatives, reason for return, trust/action, persistence, and exit not observed |
| Rehman / Portier Pacific | Deactivation on 15 Dec 2025 over an alleged failed background check; application on 30 Dec | Voluntary reactivation on 20 Feb 2026; formal reactivation order on 20 Mar | A$7,096.96 gross lost remuneration ordered, payable within 14 days | Payment receipt, post-order work, durable access, and recurrence prevention not observed | Alternatives, reason for return, trust/action, persistence, and exit not observed |
| Mansoor / Uber | Complaint-based deactivation; substitute Baysec and Didi work documented | Reactivation ordered; substitute earnings visible during the interruption | A$6,073.23 gross lost-earnings order after substitute earnings were deducted | Receipt, practical restoration, and durable access not observed | Whether substitute work was equivalent or freely chosen, trust/action, and exit not observed |
| Bandameeda / Amazon Flex | Suspension and permanent deactivation after customer complaint | Reactivation on prior terms ordered | A$12,126.31 lost remuneration ordered | Receipt, continued access, recurrence prevention, and anti-retaliation not observed | Alternatives, reason for return, trust/action, persistence, and exit not observed |
| Waheed / Uber | Deactivation found unfair after inadequate notice/inquiry; appeal followed | Reactivation order stayed pending appeal | A$259.38 per week interim payment obligation from 28 May 2026; final quantum remains open | Receipt, actual access, appeal outcome, and durable protection not observed | Household recovery, trust/action, switching, and exit not observed |

The Hotak and Rehman ledgers preserve the full observed event sequence and its
open arrows in machine-readable form: [Hotak event ledger](data/uber-hotak-end-to-end-event-ledger-v1.json)
and [Rehman event ledger](data/uber-rehman-end-to-end-event-ledger-v1.json).
Their common boundary is important: formal access restoration and a monetary
order can be observed without observing payment receipt, durable protection,
the worker's alternatives, or the later relationship to the platform.
The Waheed stay adds a sharper intermediate stage: a conditional legal payment
obligation can exist while receipt and actual work access remain unknown.

These are not pooled estimates. They are a deliberately small set of public
case records whose unit is a proceeding or named worker, with uneven follow-up
windows and different procedural postures.

The [Azwar regular-work and time-control record](uber-azwar-regular-work-time-control-record-v1.md)
adds an upstream eligibility and time-control boundary rather than another
remedy outcome. The FWC treated logged-on standby availability as distinct
from paid trip time for the hourly threshold, but accepted a recurring
three-days-per-week paid-work pattern as sufficient for protection from unfair
deactivation. This makes a hidden cost of access visible—time can be committed
without being paid—while leaving income recovery, alternatives, and exit
unobserved.

## The key mechanism distinction

The evidence now supports four separate propositions:

1. **External review can change access.** Some Commission records show an
   adjudicated reactivation order or a recorded return to the platform.
2. **A remedy can price the interruption without restoring the relationship.**
   Lost remuneration orders make the value of exclusion legible, but do not
   establish payment or future access.
3. **Review can validate a refusal.** Other records find notice, response
   consideration, and a rating rule sufficient, or dismiss on eligibility or
   merits grounds. A human reviewer can therefore be present without the
   decision being reversed.
4. **Restoration may increase observed dependence rather than demonstrate
   autonomy.** A worker who returns and completes later trips has regained an
   income route, but the record does not identify alternatives, bargaining
   power, switching costs, or whether return was voluntary under household
  constraints.

5. **Legal access to review does not measure the full cost of availability.**
   Azwar shows that a worker can satisfy a patterned legal-work gate while the
   time spent waiting for paid tasks remains outside the paid-hours measure.
   Eligibility, paid time, opportunity cost, and household security must remain
   separate variables.

This yields a sharper theme than “platforms are contestable”:

> **Contestability can restore access without making exit observable.**

That is a provisional cultural and institutional theme. It describes what the
remedy architecture makes legible and what it leaves outside the record; it
does not claim that restoration causes dependence or that any worker was
unable to leave.

## Acquisition required to close the arrow

The next evidence pass should follow the same proceeding beyond the order or
judgment and preserve a defined observation window:

1. order date, compliance date, and actual account status;
2. payment due, payment made, and payment receipt evidence;
3. post-remedy trips, hours, earnings, or non-return, with the source and
   observation window identified;
4. alternative platform use, occupational transition, or documented exit;
5. repeat deactivation, retaliation, or recurrence prevention;
6. worker-reported reason for return, switch, or exit where available.

Until those fields are acquired, the atlas should use “restoration observed,”
“continued use observed,” “payment ordered,” and “exit not observed” as separate
labels. It should not infer autonomy, dependence, or remedy effectiveness from
any one of them.

## Linked evidence

- [Platform-work remedy case ledger](platform-remedy-case-ledger-v1.md)
- [Remedy spectrum synthesis](remedy-spectrum-cross-domain-synthesis-v1.md)
- [Amazon Flex / Bandameeda remedy record](amazon-bandameeda-deactivation-remedy-record-v1.md)
- [Uber / Hotak reactivation and lost-pay record](uber-hotak-access-restoration-followup-record-v1.md)
- [Uber / Hotak structured event ledger](data/uber-hotak-end-to-end-event-ledger-v1.json)
- [Uber / Rehman structured event ledger](data/uber-rehman-end-to-end-event-ledger-v1.json)
- [Uber / Khan reactivation and lost-pay record](uber-khan-reactivation-lost-pay-record-v1.md)
- [Uber / Waheed merits remedy record](uber-waheed-merits-remedy-record-v1.md)
- [Uber / Azwar regular-work and time-control record](uber-azwar-regular-work-time-control-record-v1.md)

## Boundary

This memo reports a bounded public-record screen. The ledger has no common
denominator, no control group, no uniform follow-up period, and no verified
exit series. It therefore cannot estimate the probability of restoration,
payment, continued dependence, switching, or exit.
