# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **370**
- Exact linked social items: **389**
- Record statuses: `{'augmented': 368, 'documented_access_gap': 1646}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 329 |
| `linkedin:documented_access_gap` | 1,685 |
| `reddit:augmented` | 49 |
| `reddit:documented_access_gap` | 1,965 |
| `x:documented_access_gap` | 2,014 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,011 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
