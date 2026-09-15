# SIPP utility-to-work time-field gate

**Checked:** 2026-09-14 · **Status:** acquisition and measurement boundary

The utility-to-work following-month record uses `TPEARN` and `TMWKHRS`
because they are numeric monthly fields with a valid person-month transition
surface in the extracted 2025 SIPP file. The next desired arrow is material
pressure → time displacement, but the currently selected time-related fields
do not support the same clean interpretation without a separate universe audit.

| Field | Current use | Why it is not promoted as a following-month time outcome |
|---|---|---|
| `ETIMELOST` | Selected in the SIPP calendar slice | The full 379,215-row slice has 1,128 nonblank values, but the official universe is `EWORKMORE=1`: a reference parent who reported that child-care arrangements prevented working or working more during the fall of the reference year. It is not a monthly utility-response field. |
| `ATIMELOST` | Used in child-care/work-prevention layers | It is conditional on a reported work-prevention route and therefore is not a general monthly time-loss measure. |
| `EWORKMORE` | Used in child-care/care-work layers | It describes a reference-period child-care/work constraint, not a dated utility event or general next-month response. |
| `EPAY` / `EPAYHELP` | Used in care and assistance layers | They describe child-care payment/help universes and do not measure time displacement after utility difficulty. |

The full-file audit and official dictionary resolve the immediate uncertainty:
`ETIMELOST` is a child-care time-loss amount, measured for a typical week of
the fall reference year, with values from 1 to 99 and a separate hours/days/
weeks type field. It is useful for a care/work layer, but it cannot be promoted
as a following-month utility outcome. The next program step should therefore
seek an event-compatible time diary or administrative schedule source rather
than calling this annual conditional care field a monthly utility response.

This gate preserves the current finding's boundary: utility status can be
placed beside next-month earnings and hours movement, but no utility-to-time-
displacement arrow is yet measured. The 1,128 nonblank rows belong to a
different, annual child-care universe and do not close that arrow.

## Sources and audit trail

- [SIPP smoke check](sipp-smoke-check-v1.md)
- [SIPP broad bridge crosswalk](sipp-broad-bridge-crosswalk-v1.md)
- [Utility-to-work following-month finding](findings/us-household-calendar-integration-028.md)
- [2025 SIPP public-use data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
