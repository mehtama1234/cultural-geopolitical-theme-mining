# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **273**
- Exact linked social items: **278**
- Record statuses: `{'augmented': 273, 'documented_access_gap': 1302, 'queued': 403}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 235 |
| `linkedin:documented_access_gap` | 1,340 |
| `linkedin:not_started` | 403 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,535 |
| `reddit:not_started` | 403 |
| `x:documented_access_gap` | 1,575 |
| `x:not_started` | 403 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,574 |
| `youtube:not_started` | 403 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
