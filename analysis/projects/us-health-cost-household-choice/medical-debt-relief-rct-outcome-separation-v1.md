# Medical-debt relief RCT outcome separation v1

## Why this pass matters

The project has now measured care foregoing, household adaptation, credit
visibility, and institutional response in separate layers. This pass tests the
remedy itself with randomized evidence: when downstream medical debt is
forgiven, which currency actually changes?

## Evidence

Two randomized experiments conducted with RIP Medical Debt relieved $169
million in face-value debt for 83,401 people between 2018 and 2020. The debts
had been sent, or were about to be sent, to collections. One experiment
straddled an industry-wide pullback in medical-debt reporting, which permits a
credit-reporting contrast.

| Outcome | Estimated result |
|---|---:|
| Credit score in the reporting subexperiment | +3.4 points on average |
| Credit limits in that subexperiment | +$340 on average |
| Another unpaid bill sent to collections | +1.1 percentage points; 6.6% of the 16.2% control mean |
| Mental and physical health | No average effect detected |
| Health-care utilization | No average effect detected |
| Financial wellness | No average effect detected |

The result is not that relief “failed” in every sense. It improved a selected
credit-access surface when reporting was active. But the randomized evidence
does not support treating credit repair as automatic health recovery, care-use
recovery, or broad household financial recovery. The increase in unpaid bills
is a reminder that payment behavior can respond differently from credit access
and health; the study’s interpretation is consistent with lower repayment of
existing medical bills, not proof of intentional nonpayment or harm.

## End-to-end implication

```text
downstream medical debt / collection exposure
  -> randomized forgiveness
  -> modest credit-access change under reporting exposure
  -> no detected average health, care-use, or financial-wellness repair
```

This is the strongest causal remedy layer currently in the health-cost lane,
but it begins after the original care choice and does not observe trust or
political action. The next test must connect the original bill and care
decision to the remedy and then to a household and legitimacy outcome.

## Source

[Kluender, Mahoney, Wong, and Yin, “The Effects of Medical Debt Relief: Evidence from Two Randomized Experiments,” NBER Working Paper 32315](https://www.nber.org/papers/w32315), with the [published Quarterly Journal of Economics article](https://academic.oup.com/qje/article/140/2/1187/7933321).
