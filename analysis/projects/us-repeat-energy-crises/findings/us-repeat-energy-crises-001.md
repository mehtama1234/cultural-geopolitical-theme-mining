# Finding 001: Energy insecurity shows the gap between household sacrifice and public restoration

**Status:** provisional energy-burden and public-response synthesis · **Checked:** 2026-09-17

## The bounded finding

Three retained US evidence surfaces show different stages of the energy-
security chain. EIA records household consequences and threats: food or
medicine sacrifice, unhealthy temperatures, equipment failure, and disconnect
or delivery-stop notices. LIHEAP records public reach and reported restoration
instances. SIPP places utility difficulty before following food, housing, and
resource outcomes for selected person-month pairs. Together they show why
energy security cannot be represented by a price, a program reach count, or a
restoration count alone.

The safe conclusion is:

> Household energy pressure can be converted into sacrificed necessities and
> service threats, while public programs can reach millions and report
> restoration. The current public evidence does not show whether the affected
> household received help in time, stayed safe through the next bill, or
> recovered its food, health, work, and trust position.

## Chain under test

```text
bill, fuel, equipment, or utility-service pressure
  -> notice, threatened loss, service condition, or household sacrifice
  -> assistance contact, eligibility, payment, repair, or reconnection
  -> service continuity and protected food/medicine/health/work
  -> next bill, repeat crisis, recovery, trust, complaint, or political action
```

The three sources are complementary, not a household-level join. EIA is a
representative housing-unit consequence table; LIHEAP is a federal program
aggregate; SIPP is a person-month transition screen with field-timing and
repeated-reference limitations.

## Evidence comparison

| Stage | Observed record | Safe interpretation | Missing link |
|---|---|---|---|
| Household consequence | 43.56 million of 132.54 million primary-residence homes reported at least one listed energy-insecurity condition | Energy pressure is visible as more than a price: it includes sacrifice, temperature, equipment, and payment threat | Which condition came first, who paid, how long it lasted, and whether the same home received help |
| Protected/sacrificed need | 32.89 million homes reduced or forgone food or medicine to pay energy costs; 17.55 million reported unhealthy temperature | Households may preserve energy access by sacrificing another necessity | Item, duration, health effect, service continuity, and subsequent recovery |
| Threatened service | 16.19 million homes received a disconnect or delivery-stop notice; a notice is not a completed shutoff | Administrative threat is an important intermediate stage | Actual shutoff, reconnection, arrears, landlord/utility responsibility, and payment timing |
| Public reach | LIHEAP reported nearly 6 million individuals/families helped and about 5 million heating-assistance households in FY2024 | Program reach and need-response capacity are visible | Eligibility, amount, timing, take-up denominator, and whether assistance prevented loss |
| Public restoration | LIHEAP reported 279,000 home-energy restoration instances | Restoration is a distinct endpoint from reach and prevention | Duration, next bill, repeat crisis, equipment repair, food/medicine protection, and household recovery |
| Following household hardship | SIPP utility difficulty at one reference month is followed by food, housing, and income/resource movement screens in the next file month | Utility difficulty can be placed beside later household conditions for selected respondents | A dated bill or shutoff, assistance receipt, true event timing, and causal attribution |

The denominators are intentionally not pooled. EIA counts primary-residence
housing units; LIHEAP reports program aggregates without a household-level
restoration denominator; SIPP uses identified person-month pairs and separate
conditional universes. A public restoration instance cannot be divided into
the EIA count to create a restoration rate.

## What the comparison adds

### 1. A bill can become a food or medicine decision

The EIA table makes household allocation visible. Energy insecurity is not
only whether service was disconnected. A household can keep the lights or
heat on by reducing food or medicine, leaving home at an unhealthy temperature,
or living with unusable equipment. These are different routes and may overlap.
The result is a consequence map, not a severity scale.

### 2. Public response has multiple clocks

LIHEAP reach, prevention, restoration, and durable stability are separate
stages. A household can be counted as helped without the public record showing
the payment amount, date, next bill, equipment condition, or whether a prior
food/medicine sacrifice was reversed. A restoration instance can interrupt an
immediate loss while arrears, inefficient equipment, or a repeat crisis remain.

### 3. Following hardship is not verified recovery or causation

The SIPP transition screen is valuable because it places utility difficulty
before later food, housing, and resource outcomes for selected records. But
monthly survey fields can repeat reference-period information, and no public
field in this bridge supplies the exact bill, provider, assistance decision, or
reconnection event. The result strengthens temporal description without
becoming a utility-to-food causal estimate.

### 4. The political meaning is downstream, not assumed

Energy sacrifice and public restoration can affect trust, fairness judgments,
complaints, voting, or local organizing, but none of those responses should be
inferred from the household counts or program totals. A politically meaningful
route needs the responsible actor, notice or bill, effort, assistance outcome,
attribution, and later action for the same unit.

## Counterexamples and limits

- A disconnect notice is not a completed shutoff; some households may avoid
  loss through payment, assistance, borrowing, or informal help.
- Food/medicine sacrifice does not identify whether energy service was
  preserved, and the table does not establish medical harm.
- Program reach can reflect both substantial need and effective capacity; it is
  not a take-up rate or benefit-adequacy measure.
- Restoration can be timely and effective for some households while leaving
  other households unserved or facing repeat crisis.
- Utility difficulty followed by food insecurity does not identify a bill as
  the cause without event timing, alternatives, and a comparison design.
- EIA, LIHEAP, and SIPP do not share household identifiers and cannot be
  combined into a national recovery percentage.

## Next decisive energy episode

The smallest strong design is a privacy-preserving household event ledger:

```text
dated bill/fuel/equipment problem
  -> notice, contact, effort, payer, landlord/utility responsibility
  -> assistance application, amount, eligibility, payment, repair, reconnection
  -> service continuity, food/medicine tradeoff, health/work effect
  -> next bill, repeat crisis, recovery, complaint, trust, or action
```

The first promotion event should be one identified household or valid panel
unit with a dated bill or notice, a documented assistance or repair route, and a
following outcome. Preserve prevention, restoration, payment, and durable
stability as separate states.

## Provenance and storage boundary

This synthesis uses retained EIA, HHS/ACF LIHEAP, and SIPP records and local
source notes. No new EIA PDF, LIHEAP warehouse, utility account file, or SIPP
archive was downloaded.

- [EIA 2024 household energy-insecurity table](https://www.eia.gov/consumption/residential/data/2024/hc/pdf/HC11.1_2024.pdf)
- [LIHEAP FY2024 annual report](https://ocsannualreport.acf.hhs.gov/annual-report-fy24/priorities-and-fy24-spotlights)
- [SIPP 2025 data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [LIHEAP reach/restoration record](../../../records/us-liheap-reach-restoration-fy2024.json)

**Evidence status:** detailed non-pooled energy-security synthesis; no causal
price effect, assistance take-up rate, restoration rate, durable recovery,
health effect, trust change, or political-action estimate is made.
