# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **254**
- Exact linked social items: **259**
- Record statuses: `{'augmented': 254, 'documented_access_gap': 1096, 'queued': 628}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 216 |
| `linkedin:documented_access_gap` | 1,134 |
| `linkedin:not_started` | 628 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,310 |
| `reddit:not_started` | 628 |
| `x:documented_access_gap` | 1,350 |
| `x:not_started` | 628 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,349 |
| `youtube:not_started` | 628 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
