# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **55**
- Exact linked social items: **60**
- Record statuses: `{'augmented': 55, 'documented_access_gap': 95, 'queued': 1828}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 18 |
| `linkedin:documented_access_gap` | 132 |
| `linkedin:not_started` | 1,828 |
| `reddit:augmented` | 39 |
| `reddit:documented_access_gap` | 111 |
| `reddit:not_started` | 1,828 |
| `x:documented_access_gap` | 150 |
| `x:not_started` | 1,828 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 149 |
| `youtube:not_started` | 1,828 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
