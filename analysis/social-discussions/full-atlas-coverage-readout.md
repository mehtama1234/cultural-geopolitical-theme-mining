# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **289**
- Exact linked social items: **294**
- Record statuses: `{'augmented': 289, 'documented_access_gap': 1461, 'queued': 228}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 251 |
| `linkedin:documented_access_gap` | 1,499 |
| `linkedin:not_started` | 228 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,710 |
| `reddit:not_started` | 228 |
| `x:documented_access_gap` | 1,750 |
| `x:not_started` | 228 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,749 |
| `youtube:not_started` | 228 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
