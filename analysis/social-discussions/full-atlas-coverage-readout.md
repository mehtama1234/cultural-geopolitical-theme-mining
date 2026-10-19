# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **352**
- Exact linked social items: **370**
- Record statuses: `{'augmented': 350, 'documented_access_gap': 1664}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 313 |
| `linkedin:documented_access_gap` | 1,701 |
| `reddit:augmented` | 46 |
| `reddit:documented_access_gap` | 1,968 |
| `x:documented_access_gap` | 2,014 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,011 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
