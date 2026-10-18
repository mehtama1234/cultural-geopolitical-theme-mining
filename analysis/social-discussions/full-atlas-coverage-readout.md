# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **118**
- Exact linked social items: **123**
- Record statuses: `{'augmented': 118, 'documented_access_gap': 457, 'queued': 1403}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 80 |
| `linkedin:documented_access_gap` | 495 |
| `linkedin:not_started` | 1,403 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 535 |
| `reddit:not_started` | 1,403 |
| `x:documented_access_gap` | 575 |
| `x:not_started` | 1,403 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 574 |
| `youtube:not_started` | 1,403 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
