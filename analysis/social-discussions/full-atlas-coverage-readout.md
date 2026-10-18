# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **283**
- Exact linked social items: **288**
- Record statuses: `{'augmented': 283, 'documented_access_gap': 1417, 'queued': 278}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 245 |
| `linkedin:documented_access_gap` | 1,455 |
| `linkedin:not_started` | 278 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,660 |
| `reddit:not_started` | 278 |
| `x:documented_access_gap` | 1,700 |
| `x:not_started` | 278 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,699 |
| `youtube:not_started` | 278 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
