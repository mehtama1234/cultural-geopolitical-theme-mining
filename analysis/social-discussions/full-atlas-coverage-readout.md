# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **115**
- Exact linked social items: **120**
- Record statuses: `{'augmented': 115, 'documented_access_gap': 435, 'queued': 1428}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 77 |
| `linkedin:documented_access_gap` | 473 |
| `linkedin:not_started` | 1,428 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 510 |
| `reddit:not_started` | 1,428 |
| `x:documented_access_gap` | 550 |
| `x:not_started` | 1,428 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 549 |
| `youtube:not_started` | 1,428 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
