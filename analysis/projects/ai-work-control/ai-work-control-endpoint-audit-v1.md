# AI/work-control endpoint audit v1

**Status:** coverage audit only; no pooled adoption, productivity, or worker-power estimate  
**Checked:** 2026-09-17
**Machine record:** [AI/work-control endpoint audit](data/ai-work-control-endpoint-audit-v1.json)

## Result

The existing local evidence covers a meaningful sequence but not a complete
worker-control outcome:

```text
AI capability or management tool
  -> adoption or organizational implementation
  -> worker voice, consultation, or bargaining
  -> rule/feature change and enforcement
  -> workload, pace, pay, schedule, health, security, and bargaining outcome
```

| Source layer | Exposure/implementation | Voice/control | Realized outcome boundary |
|---|---|---|---|
| NBER worker/task evidence | Adoption and field-experiment productivity/time measures | Not directly observed | Worker-level control, pay, security, and bargaining open |
| OECD/employer + executive + union comparison | Employer tools, monitoring, AI use, expectations, representation | Governance measures and formal representation reported | No same-workplace worker outcome |
| JRC/ILO comparative evidence | Worker AI use and algorithmic-management practices | Consultation, bargaining, data access, legal/public challenge | Case-specific rule changes observed; US generalization and durability open |
| Microsoft Germany implementation | Named Copilot/Places rollout, controls, training, dashboards | Company-reported works-council feedback and product changes | No independent worker-level welfare or enforcement outcome |
| NYC AEDT regime | Bias-audit, public-summary, and employee/candidate-notice requirements | Complaint route; discrimination claims referred to NYC Commission on Human Rights | No named employer implementation, worker decision change, appeal, compensation, or defined complaint outcome |
| DOL WHD federal guidance | FLSA guidance addresses AI/automated workplace surveillance, targeting, and analytics | Existing labor-standard and anti-retaliation obligations provide an enforcement route | No named implementation, worker exposure, enforcement disposition, correction, or compensation outcome |

## Broad-program interpretation

The strongest current conclusion is not that AI inevitably improves or harms
work. It is that adoption and organizational capacity can become visible before
workers' control over task order, monitoring, performance evaluation, data,
pace, and job change is measured. Consultation is a conversion point: in the
comparative cases it can surface objections and modify rules, but participation
does not automatically equal veto power, enforcement, or improved welfare.

The targeted NYC AEDT recheck adds a US public-rule and contestability surface:
the city specifies pre-use audit, disclosure, notice, and complaint
requirements, but the public pages checked do not identify a named employer,
worker decision, correction, or remedy. This is an institutional access route,
not evidence of compliance or lived control.

The next decisive test is one named workplace system followed through actual
worker exposure and a defined rule or feature change, with notice, override or
appeal, workload/pace, pay, schedule control, health, bargaining, and household
outcomes. A comparable workplace or implementation path is required to avoid
turning a company case into a population claim.

## Reproduction

```text
python3 scripts/validate_ai_work_control_endpoint_audit.py
```

The validator checks the four local source rows and downloads nothing.
