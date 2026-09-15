# FMS delivery, acceptance, and settlement can appear on different clocks

**Status:** comparative implementation-control finding · **Checked:** 2026-09-14

## The finding

The newer Polish Supreme Audit Office review adds an important timing rule to
the JASSM-ER case. NIK states that Foreign Military Sales schedules are
estimates, not fixed delivery dates. In one separate F-35 agreement, four
aircraft were delivered in December 2024 and January 2025 even though the
estimated contractual schedule placed delivery in the third quarter of 2024;
the related advance had not been settled by the end of 2024 because of delivery
dates and FMS accounting cycles, and the settlement forms arrived in 2025.

The evidence therefore separates three events that are often collapsed in
public narratives:

```text
estimated FMS schedule
  -> physical delivery                         [observed for comparator]
  -> acceptance / operational use               [not implied by delivery]
  -> accounting settlement and source form      [observed later for comparator]
```

This is not evidence that Poland’s 2024 JASSM-ER order has been delivered. It
is a cross-system control finding that explains why a schedule comparison,
public announcement, accounting record, and operational inventory search can
produce different timestamps.

## Evidence table

| Layer | NIK observation | Boundary |
|---|---|---|
| FMS schedule | Delivery months and costs in the FMS structure are estimates | A planned window is not a shipment or acceptance event |
| Physical realization | Four F-35 aircraft were delivered in December 2024 and January 2025 | This is the F-35 comparator, not JASSM-ER |
| Schedule variance | The estimated contractual schedule placed that delivery in Q3 2024 | NIK’s passage does not classify the difference as supplier delay or customer acceptance delay |
| Settlement visibility | The advance was not settled at 2024 year-end because of delivery dates and FMS cycles; forms arrived in 2025 | Accounting visibility lags physical delivery in this example |
| Broader FMS scale | NIK reports PLN 1,534,148.4 thousand of advances settled in 2024 through US DD Form 645 records covering Q4 2023 and Q1–Q3 2024 | Aggregate settlement value is not a missile or aircraft quantity |

## Why it matters for the end-to-end geopolitical question

The end-to-end atlas needs a realization clock, not one generic “delivery”
field. An aircraft or missile may be physically delivered, formally accepted,
integrated, trained on, placed into an inventory, and reflected in an accounting
settlement at different times. The FMS comparator makes this a measurable
design requirement for the JASSM-ER watchpoint: search separately for shipment,
acceptance, settlement, fielding, training, and operational-use evidence.

It also prevents a false negative. A missing settlement record cannot be used
to infer missing delivery, just as a delivered item cannot automatically be
treated as operationally usable or strategically consequential.

## Counterinterpretations kept visible

- The F-35 case may have contract-specific terms that do not generalize to
  JASSM-ER.
- “Delivered” in the audit passage does not establish acceptance, training,
  readiness, or operational employment.
- An estimated schedule can move for administrative, production, transport,
  or customer reasons; the cited passage does not identify the cause.
- Settlement-form arrival in 2025 does not mean the aircraft were delivered in
  2025; it is a documentation timestamp.
- This comparator does not close any realization arrow for Poland’s 2024
  JASSM-ER agreement.

## Next decisive acquisition

For JASSM-ER, locate a dated event for physical shipment or delivery, formal
acceptance, Polish unit receipt, training/integration, inventory, or FMS
settlement. Record the event type and date separately and preserve whether the
source is a schedule, delivery notice, acceptance document, accounting form, or
operational report.

## Sources and reproduction

- [NIK official 2024 audit PDF](https://www.nik.gov.pl/kontrole/wyniki-kontroli-nik/pobierz,kon~p_25_001_202502181310531739880653~id1~01,typ,kj.pdf) · pp. 12–14, especially the FMS schedule note and F-35 delivery/settlement passage
- Local extraction boundary note: [NIK FMS source note](../data/nik-2024-fms-realization-source-note.md)
- Related current-order finding: [Poland’s JASSM-ER order still has a schedule, not a public delivery record](ai-work-control-081.md)

**Evidence status:** FMS timing/accounting asynchrony is observed in the F-35
comparator; JASSM-ER shipment, acceptance, delivery, fielding, training,
settlement, and geopolitical response remain open.
