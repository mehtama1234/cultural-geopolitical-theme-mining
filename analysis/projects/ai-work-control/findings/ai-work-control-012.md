# Finding 012: AI access is not the same as AI capacity

**Status:** provisional  
**Last checked:** 2026-09-11  
**Project:** AI, work, and control

## Finding

An AI interface does not create equal capability. The result depends on the complements around it: capital, data, software, training, electricity, connectivity, institutions, and a way to change or challenge the system. Two firms or countries may have access to similar models and still receive different results because they do not control the same complements.

## What we directly know

- The World Bank's 2026 development report says AI gains depend on local complements and that a mismatch between where AI is developed and where it is deployed can weaken results. It names infrastructure, skills, and institutions as part of the conditions for adoption and links AI to jobs, public services, trade, energy costs, and political power. [World Development Report 2026](https://www.worldbank.org/en/publication/wdr2026)
- The BIS firm study reports that AI adoption gains are supported by complementary investment in software, data, and workforce training, and that the largest productivity benefits are concentrated in medium and large firms. [BIS Working Paper 1325](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms)
- The IEA reports that AI depends on physical data-centre and energy systems, including electricity generation, grids, critical minerals, and connection capacity. Its scenarios show that these needs are uneven across places and may affect affordability and energy security. [IEA Energy and AI](https://www.iea.org/reports/energy-and-ai)
- BEA's measurement work links AI use to production accounts, capital, R&D, labor, data assets, and digitally deliverable services, while warning that definitions and available data are still incomplete. [BEA Digital Economy](https://bea.gov/data/special-topics/digital-economy)
- The IMF model separates wage inequality from wealth inequality and shows how firm adoption choices and capital returns can distribute AI gains differently. [IMF: AI Adoption and Inequality](https://www.imf.org/en/publications/wp/issues/2025/04/04/ai-adoption-and-inequality-565729)

These sources measure different layers. They support a complements hypothesis; they do not prove a single global ranking of countries or firms.

## Causal chain under test

```text
model or tool access
  -> complements: capital, data, software, skills, power, connectivity, institutions
  -> actual use and system function
  -> output, task quality, worker opportunity, public service, or energy demand
  -> who captures value and who bears cost
  -> firm and state dependence
```

The first arrow is often visible. The later arrows need linked evidence.

## Minimum capacity test

| Complement | Question | Failure that can be hidden by an access headline |
|---|---|---|
| Capital | Who can pay for integration, testing, and change? | A free tool exists but only large firms can redesign work around it. |
| Data | Who owns, cleans, and can reuse the data? | A model is available but local data are missing, restricted, or poor. |
| Software and workflow | Can the tool enter the real process? | A pilot works while the old process remains in place. |
| Skills and training | Who can use, supervise, and correct it? | Use is shallow or responsibility shifts to workers without support. |
| Electricity and hardware | Can reliable power, chips, cooling, and connection be secured? | The service is imported while physical dependence grows elsewhere. |
| Institutions | Can people inspect, appeal, procure, and regulate it? | Adoption increases while accountability and public capacity lag. |
| Outside options | Can a worker, firm, or state refuse or switch? | Formal access exists but dependence removes practical choice. |

## Cultural and social meaning

The same technology can be experienced as opportunity in one place and dependence in another. A worker may gain a useful assistant but lose control if the firm owns the resulting profile and later uses it for evaluation. A country may celebrate local AI use while importing the model, cloud, chips, electricity, and rules that determine how the system works. The visible story is adoption; the lived story is who has room to choose.

This is an inference from the source set, not a direct finding about every deployment.

## Geopolitical meaning

Dependence becomes a geopolitical question when a critical complement is difficult to replace. The relevant map is not “which country uses AI?” It is:

```text
model owner -> cloud and chip suppliers -> data and energy systems
-> firms and public agencies -> workers and households
-> rules, bargaining, and exit options
```

Control at one layer does not prove control of the whole chain. The project must identify the contract, location, owner, substitute, and public authority at each step.

## Strongest challenge

Complementary inputs may simply measure better management. Larger firms may have higher productivity and wages for reasons that also make them more likely to adopt AI. Energy and infrastructure scenarios are not observed worker outcomes. The hypothesis must survive comparisons that handle firm size, prior capability, sector, country, and timing.

## What would change our mind

- Similar tools produce similar results across firms and countries after differences in complements are measured.
- Ownership and access to capital, data, power, skills, and institutions do not predict who captures gains.
- Small firms and lower-capacity countries catch up without new complementary investment.
- AI deployment changes worker, public-service, and state outcomes even where integration and institutional capacity remain weak.

## Next tests

1. Create a firm-country complement scorecard with sources and dates, not one synthetic ranking.
2. Compare large and small firms using the same system function and outcome measure.
3. Match AI use with software, data, training, electricity, and capital investment.
4. Track whether imported systems create local skills and bargaining power or deepen dependence.
5. Add a public-service case where procurement, local data, and appeal rights can be observed.
6. Add counterevidence from firms or countries that built capability without relying on dominant external providers.

## Sources

- [World Development Report 2026](https://www.worldbank.org/en/publication/wdr2026)
- [BIS Working Paper 1325](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms)
- [IEA Energy and AI](https://www.iea.org/reports/energy-and-ai)
- [BEA Digital Economy](https://bea.gov/data/special-topics/digital-economy)
- [IMF: AI Adoption and Inequality](https://www.imf.org/en/publications/wp/issues/2025/04/04/ai-adoption-and-inequality-565729)
- [Time-ordered adoption trace](../time-ordered-adoption-trace-v1.md)
- [Claims ledger](../claims-ledger-v1.md)
