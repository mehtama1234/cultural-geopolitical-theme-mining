# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **247**
- Exact linked social items: **252**
- Record statuses: `{'augmented': 247, 'documented_access_gap': 1053, 'queued': 678}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 209 |
| `linkedin:documented_access_gap` | 1,091 |
| `linkedin:not_started` | 678 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,260 |
| `reddit:not_started` | 678 |
| `x:documented_access_gap` | 1,300 |
| `x:not_started` | 678 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,299 |
| `youtube:not_started` | 678 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
