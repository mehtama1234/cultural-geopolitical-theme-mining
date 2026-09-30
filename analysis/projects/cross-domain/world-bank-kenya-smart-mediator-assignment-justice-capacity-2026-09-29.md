# When public capacity is scarce, algorithmic matching becomes a justice institution

## Finding

The World Bank's SMaRT paper studies an online allocation problem in the Kenyan Judiciary: incoming mediation cases must be assigned immediately to eligible mediators whose capacity and quality vary. The underlying administrative data cover 30,633 cases from 2016–2025, approximately 2,100 mediators, 87 court stations, and 13 case-type categories.

SMaRT (Selecting Mediators that are Right for the Task) combines quadratic-program assignment with multi-agent bandit-style learning. In the paper's stylized and Kenyan-data applications, it outperforms baseline approaches and makes explicit the tradeoff between strict capacity constraints and overall case-resolution rates. A randomized controlled trial is planned, so the current evidence is computational and retrospective rather than causal live-deployment evidence.

## Cross-domain interpretation

This adds a distinct allocation-to-legitimacy mechanism to the corpus. The social consequence is not merely that government uses AI. It is that a scarce public service is distributed through a rule system that learns from prior institutional performance:

`case arrival -> eligibility and capacity matching -> mediator exposure and workload -> resolution, delay, and backlog -> perceived access and institutional legitimacy`

The key cultural-social shift is from “fairness means equal assignment” toward a harder question: how should a public institution allocate unequal capacity and unequal observed quality without converting historical selection into a self-reinforcing hierarchy? The algorithm can make hidden administrative judgment inspectable, but it can also create a new authority that is difficult for litigants or mediators to contest.

## Political, cultural, and consumer-recourse significance

- Access to justice is partly an allocation problem: who receives scarce time, attention, and competent institutional assistance.
- Public-sector automation increasingly concerns matching and triage rather than only prediction or paperwork.
- “Fairness” becomes a live tradeoff among prompt service, workload equity, geographic eligibility, estimated quality, and resolution.
- Historical administrative data can turn unequal treatment into a quality signal, even when the original assignment process was itself unequal.
- The relevant consumer-recourse question is whether affected people can understand, challenge, or obtain a human override of an allocation decision.

## Boundary and next test

The paper does not yet establish that SMaRT improves litigant outcomes, equal access, satisfaction, or durable justice in live courts. Its administrative data are restricted, although the World Bank has released a computational reproducibility package. The next test is the planned RCT, expanded with measures of case mix, delay, mediator workload, litigant experience, appeal or override, and distributional effects across stations and case types.

Sources: [World Bank paper PDF](https://documents.worldbank.org/curated/en/099845009162639662/pdf/IDU-a2beaaf7-dbcc-4441-a911-92c4420f73e2.pdf), [World Bank research listing](https://www.worldbank.org/en/research/all?lang_exact=English&os=20&qterm=), [reproducibility package](https://reproducibility.worldbank.org/catalog/648), [bibliographic record](https://ideas.repec.org/p/wbk/wbrwps/11456.html).
