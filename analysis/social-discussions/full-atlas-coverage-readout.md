# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **229**
- Exact linked social items: **234**
- Record statuses: `{'augmented': 229, 'documented_access_gap': 921, 'queued': 828}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 191 |
| `linkedin:documented_access_gap` | 959 |
| `linkedin:not_started` | 828 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,110 |
| `reddit:not_started` | 828 |
| `x:documented_access_gap` | 1,150 |
| `x:not_started` | 828 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,149 |
| `youtube:not_started` | 828 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
