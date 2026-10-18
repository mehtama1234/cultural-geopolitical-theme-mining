# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **77**
- Exact linked social items: **82**
- Record statuses: `{'augmented': 77, 'documented_access_gap': 223, 'queued': 1678}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 39 |
| `linkedin:documented_access_gap` | 261 |
| `linkedin:not_started` | 1,678 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 260 |
| `reddit:not_started` | 1,678 |
| `x:documented_access_gap` | 300 |
| `x:not_started` | 1,678 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 299 |
| `youtube:not_started` | 1,678 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
