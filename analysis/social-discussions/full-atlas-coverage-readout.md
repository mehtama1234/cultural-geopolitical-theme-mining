# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **341**
- Exact linked social items: **349**
- Record statuses: `{'augmented': 337, 'documented_access_gap': 1667, 'in_review': 10}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 303 |
| `linkedin:documented_access_gap` | 1,703 |
| `linkedin:not_started` | 8 |
| `reddit:augmented` | 41 |
| `reddit:documented_access_gap` | 1,963 |
| `reddit:not_started` | 10 |
| `x:documented_access_gap` | 2,004 |
| `x:not_started` | 10 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 2,003 |
| `youtube:not_started` | 10 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
