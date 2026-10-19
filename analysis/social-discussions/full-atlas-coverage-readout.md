# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **349**
- Exact linked social items: **365**
- Record statuses: `{'augmented': 347, 'documented_access_gap': 1664, 'in_review': 3}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 310 |
| `linkedin:documented_access_gap` | 1,701 |
| `linkedin:not_started` | 3 |
| `reddit:augmented` | 45 |
| `reddit:documented_access_gap` | 1,966 |
| `reddit:not_started` | 3 |
| `x:documented_access_gap` | 2,011 |
| `x:not_started` | 3 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,008 |
| `youtube:not_started` | 3 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
