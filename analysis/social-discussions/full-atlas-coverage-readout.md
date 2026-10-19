# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **342**
- Exact linked social items: **350**
- Record statuses: `{'augmented': 338, 'documented_access_gap': 1667, 'in_review': 9}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 304 |
| `linkedin:documented_access_gap` | 1,703 |
| `linkedin:not_started` | 7 |
| `reddit:augmented` | 41 |
| `reddit:documented_access_gap` | 1,964 |
| `reddit:not_started` | 9 |
| `x:documented_access_gap` | 2,005 |
| `x:not_started` | 9 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 2,004 |
| `youtube:not_started` | 9 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
