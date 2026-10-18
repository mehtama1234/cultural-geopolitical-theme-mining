# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **274**
- Exact linked social items: **279**
- Record statuses: `{'augmented': 274, 'documented_access_gap': 1326, 'queued': 378}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 236 |
| `linkedin:documented_access_gap` | 1,364 |
| `linkedin:not_started` | 378 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,560 |
| `reddit:not_started` | 378 |
| `x:documented_access_gap` | 1,600 |
| `x:not_started` | 378 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,599 |
| `youtube:not_started` | 378 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
