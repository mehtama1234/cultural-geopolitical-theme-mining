# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **34**
- Exact linked social items: **37**
- Record statuses: `{'augmented': 34, 'documented_access_gap': 16, 'queued': 1928}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 3 |
| `linkedin:documented_access_gap` | 47 |
| `linkedin:not_started` | 1,928 |
| `reddit:augmented` | 32 |
| `reddit:documented_access_gap` | 18 |
| `reddit:not_started` | 1,928 |
| `x:documented_access_gap` | 50 |
| `x:not_started` | 1,928 |
| `youtube:documented_access_gap` | 50 |
| `youtube:not_started` | 1,928 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
