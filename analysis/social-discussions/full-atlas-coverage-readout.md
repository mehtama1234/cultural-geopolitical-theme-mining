# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,131**
- Atlas records with at least one exact linked social item: **375**
- Exact linked social items: **398**
- Record statuses: `{'augmented': 373, 'documented_access_gap': 1758}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 334 |
| `linkedin:documented_access_gap` | 1,797 |
| `reddit:augmented` | 52 |
| `reddit:documented_access_gap` | 2,079 |
| `x:documented_access_gap` | 2,131 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,128 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
