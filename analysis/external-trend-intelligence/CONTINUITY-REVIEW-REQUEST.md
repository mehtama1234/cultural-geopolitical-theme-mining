# Two-year continuity review request

This is the release-owner handoff for proving weekly observatory continuity.
The current evidence is a burst of refresh runs across one distinct weekly window;
that is not two-year coverage. This request records each weekly review without
turning a configured schedule into proof of future execution.

## Required weekly review fields

For every weekly window, record:

- scheduled window and actual run timestamp;
- full-refresh status and pipeline step count;
- source-family freshness and incomplete/recovery states;
- open-gate count and any newly opened or closed gate;
- missed-window or outage reason, if applicable;
- manual-dispatch recovery evidence, if used;
- release-owner review and next review date.

Acceptance requires 104 distinct weekly windows, each with a passed full
refresh and retained recovery evidence for any missed window. Repeated runs in
one week do not count as additional coverage.

## Current status

| Metric | Current value | Acceptance target | Review note |
| --- | ---: | ---: | --- |
| Distinct weekly windows | 1 | 104 | 103 windows remain |
| Passed refresh runs | see `refresh-continuity-audit.json` | one per observed week | Burst runs are not weekly coverage |
| Observed days | 2 | 104-week operating history | Future elapsed time is required |
| Scheduled cadence | weekly Monday 06:17 UTC | configured and monitored | Schedule configuration is not execution proof |
| Recovery path | manual dispatch | exercised and retained | Use only for missed/stale windows |

## Sign-off log

| Window | Run ID / artifact | Freshness decision | Recovery evidence | Release owner | Reviewed date |
| --- | --- | --- | --- | --- | --- |
| 2026-W44 | recorded in `refresh-history.json` | ready/hold: TBD | TBD | TBD | TBD |

The machine-readable coverage plan records the weekly-row schema, review
artifacts, and missed-window policy. The release owner should append one row per
weekly window and investigate any gap over 168 hours. Escalate unresolved continuity failures to
`release_owner` → `program_sponsor`. This handoff does not clear rights,
qualify trends, or authorize company data access.
