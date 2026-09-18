# Malaysia Act 872 official-route recheck v1

**Status:** official implementation surfaces rechecked; case-level outcome remains open  
**Checked:** 2026-09-18

## Result

The current official Ministry of Human Resources Act 872 portal and the
JTKSM enforcement page remain available and expose the Act, subsidiary
regulations, Tribunal information, and e-Aduan route. The official pages do
not expose a public register of Tribunal case numbers, pleadings, hearing
minutes, awards, settlements, payments, or enforcement outcomes for the
reported GrabCar proceeding.

The official Tribunal regulation confirms that the Registrar keeps proceeding
records in case files and that an agreed settlement can be recorded as an
award. The Act provides for an award and, where practicable, a 30-day period
from the last hearing. Those are procedural capabilities, not evidence that
the reported GrabCar matter reached an award or that a claimant received a
remedy.

## Route matrix

| Official surface | Current observation | Missing for the end-to-end case |
|---|---|---|
| Ministry Act 872 portal | Act, FAQ, information kit, Tribunal and e-Aduan links remain live | Case identifier, filed claim, hearing record, award |
| JTKSM enforcement page | Act and implementing materials; page states update date of 15 September 2026 | Complaint counts, case outcomes, enforcement actions, payment |
| Tribunal regulation | Hearing, settlement-award, reasons, and record-management rules are published | Actual case file or procedural order |
| e-Aduan route | Complaint/login route is exposed | Public complaint register, timing distribution, resolution, correction, payment |
| Ministry media/search surfaces | Institutional establishment and implementation communications are visible | GrabCar case number, merits reasoning, award, enforcement, worker outcome |

## Coding consequence

```text
official statutory route       observed_official
maintained implementation page observed_official
reported GrabCar hearing       observed_case_reported
public case identifier         not_observed
merits / award                 not_observed
payment / correction           not_observed
durability / anti-retaliation not_observed
```

This recheck does not downgrade the reported hearing. It separates a reported
institutional-use event from a primary adjudicative record and confirms that
the official route itself does not currently close the remedy arrow.

## Sources

- [Ministry Act 872 portal](https://www.mohr.gov.my/aktapekerjagig2025/)
- [Ministry Act 872 download and implementation page](https://www.mohr.gov.my/aktapekerjagig2025/download.html)
- [JTKSM enforcement page](https://jtksm.mohr.gov.my/ms/penguatkuasaan-akta-pekerja-gig-2025-jtksm)
- [Act 872](https://www.mohr.gov.my/aktapekerjagig2025/assets/documents/Act%20872.pdf)
- [Gig Workers Tribunal regulations](https://www.mohr.gov.my/aktapekerjagig2025/assets/documents/PUA144_2026%20-%20PERATURAN%20PEKERJA%20GIG%20%28TRIBUNAL%20PEKERJA%20GIG%29.pdf)
- [Machine-readable recheck](data/malaysia-act872-official-route-recheck-2026-09-18.json)

**Storage boundary:** only official public pages and regulations were reviewed;
no complaint, claimant, or Tribunal case file was downloaded or retained.
