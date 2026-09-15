# AI task adoption and sector mobility must not be mistaken for worker control

**Status:** provisional NBER–BLS work-control synthesis · **Checked:** 2026-09-14

## The bounded finding

Two current evidence layers locate different parts of the work transition:

1. NBER Working Paper 35677 reports generative-AI use for detailed work
   activities from pooled Real-Time Population Survey waves, with 682 rated
   detailed activities, 256 rated intermediate activities, and 9 broad
   activities. At the broad level, reported use is highest for reasoning and
   decision-making activities (30.0%) and lowest for physical/manual work
   (9.6%). Within similar work, adoption is still uneven rather than being
   determined by occupational exposure alone.
2. NBER Working Paper 33795 supplies a worker-level randomized field
   experiment: across 66 firms and 7,137 knowledge workers, 80% of treated
   users used the tool in the second half of the six-month experiment and those
   users spent about two fewer hours per week on email while outside-hours work
   decreased. The experiment found no detectable change in task quantity or
   composition. This populates an exposure-to-time endpoint, not worker control.
3. BLS 2025 sector context shows quits rates of 1.39% in manufacturing, 2.34%
   in professional/business services, 1.93% in education/health services, and
   3.93% in leisure/hospitality. These are establishment rates, not AI-exposed
   worker outcomes.

The defensible synthesis is: **task-level AI use and sector-level mobility
identify different exposure surfaces; neither measures whether workers gained
discretion, lost control, received training, or could appeal a decision.**

## Why the units cannot be pooled

| Evidence | Unit | Direct result | What it cannot establish |
|---|---|---|---|
| NBER W35677 | Worker-task observations and survey-weighted activity indexes | AI use varies across work activities and within similar work | Sector quits, workplace rules, pay, autonomy, or household effects |
| BLS JOLTS | Establishment-month rates | Sector mobility differs materially | Unique worker transitions, AI exposure, reasons, or worker power |
| BLS CPS/union context | Industry worker population | Formal membership varies by sector | The represented worker's actual tool, grievance, or schedule experience |
| BLS CES | Establishment average earnings | Average pay differs by sector | Worker pay trajectory, hours, benefits, or control |
| NBER W33795 | 66-firm randomized field experiment; 7,137 knowledge workers | Tool access changed email time and outside-hours work for treated users without detectable task-quantity/composition change | Whether saved time remained with workers, changed workload, pay, health, discretion, or bargaining |

The NBER indexes come from pooled survey waves and suppress task cells below
the stated observation threshold; the BLS series summarize separate annual or
monthly programs. A high-use task can exist in a low-quits sector, and a
high-quits sector can contain both low- and high-adoption tasks. The current
files do not supply the common worker, workplace, occupation, or place key
needed to test that intersection.

## Mechanism under test

```text
task fit and access
  -> worker adoption or non-adoption
  -> tool-mediated pace, evaluation, correction, and discretion
  -> pay, health, schedule, bargaining, and exit
  -> household security, trust, collective action, or political judgment
```

The NBER layer measures the first transition in a task-use sense. The BLS
layer provides surrounding labor-market and representation context. The
remaining worker, workplace, household, and meaning/action stages are open.
W33795 adds a stronger within-work event for time use, but its conditional user
effect still does not identify who controlled the saved time or whether the
change reached household security.

## Counterexamples kept visible

- High adoption in reasoning or information tasks does not prove productivity,
  promotion, or autonomy; the tool may be employer-directed or used without
  training or review rights.
- Low adoption in physical/manual work does not mean low algorithmic control;
  scheduling, monitoring, routing, or evaluation may occur outside the task
  index.
- High quits can reflect opportunity, churn, poor conditions, or composition;
  low quits can reflect satisfaction, weak alternatives, or delayed exits.
- Sector pay and union membership do not reveal whether a worker can inspect,
  correct, refuse, or bargain over a tool.
- A reduction in email time can be a worker benefit, employer capacity gain, or
  reallocation into other work; without workload, schedule, and appropriation
  measures it is not a control result.
- Similar occupational exposure can coexist with different access, employer
  permission, privacy rules, learning time, and responsibility for errors.

## Next end-to-end test

The decisive next dataset must supply a compatible worker or workplace key and
measure, in time order:

1. task-level tool use and employer permission;
2. training, monitoring, evaluation, and human review;
3. schedule, pace, discretion, pay, health, and correction/appeal;
4. representation, grievance, switching, retention, or exit; and
5. household time/security and later trust or collective action.

The comparison should stratify by sector and representation while retaining
high-adoption/low-mobility and low-adoption/high-mobility countercells. Until
that evidence exists, this synthesis is a measurement map, not a claim that
AI caused sector mobility or changed worker power.

## Reproduction and sources

- [NBER task-level adoption record](../../../records/us-nber-task-level-genai-adoption-2026.json)
- [NBER public index acquisition audit](../nber-w35677-index-acquisition-v1.md)
- [BLS JOLTS/union/earnings context record](../../../records/us-bls-jolts-union-earnings-industry-context-2025.json)
- [BLS sector context finding](ai-work-control-034.md)
- [NBER Working Paper 35677](https://www.nber.org/papers/w35677)
- [NBER Working Paper 33795](https://www.nber.org/papers/w33795)
- [BLS JOLTS API](https://api.bls.gov/publicAPI/v2/timeseries/data/)

**Evidence status:** cross-source task/sector measurement synthesis; no pooled
worker-level estimate, causal AI effect, household consequence, political
meaning, or geopolitical claim is made.
