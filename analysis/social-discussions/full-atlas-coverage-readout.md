# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **271**
- Exact linked social items: **276**
- Record statuses: `{'augmented': 271, 'documented_access_gap': 1279, 'queued': 428}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 233 |
| `linkedin:documented_access_gap` | 1,317 |
| `linkedin:not_started` | 428 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,510 |
| `reddit:not_started` | 428 |
| `x:documented_access_gap` | 1,550 |
| `x:not_started` | 428 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,549 |
| `youtube:not_started` | 428 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
