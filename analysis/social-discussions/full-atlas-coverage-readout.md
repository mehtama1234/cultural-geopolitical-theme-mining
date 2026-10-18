# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **51**
- Exact linked social items: **56**
- Record statuses: `{'augmented': 51, 'documented_access_gap': 74, 'queued': 1853}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 15 |
| `linkedin:documented_access_gap` | 110 |
| `linkedin:not_started` | 1,853 |
| `reddit:augmented` | 38 |
| `reddit:documented_access_gap` | 87 |
| `reddit:not_started` | 1,853 |
| `x:documented_access_gap` | 125 |
| `x:not_started` | 1,853 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 124 |
| `youtube:not_started` | 1,853 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
