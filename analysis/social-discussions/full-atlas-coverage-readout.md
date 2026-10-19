# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **344**
- Exact linked social items: **357**
- Record statuses: `{'augmented': 342, 'documented_access_gap': 1663, 'in_review': 9}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 305 |
| `linkedin:documented_access_gap` | 1,700 |
| `linkedin:not_started` | 9 |
| `reddit:augmented` | 45 |
| `reddit:documented_access_gap` | 1,960 |
| `reddit:not_started` | 9 |
| `x:documented_access_gap` | 2,005 |
| `x:not_started` | 9 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,002 |
| `youtube:not_started` | 9 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
