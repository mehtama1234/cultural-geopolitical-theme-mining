# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **87**
- Exact linked social items: **92**
- Record statuses: `{'augmented': 87, 'documented_access_gap': 263, 'queued': 1628}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 49 |
| `linkedin:documented_access_gap` | 301 |
| `linkedin:not_started` | 1,628 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 310 |
| `reddit:not_started` | 1,628 |
| `x:documented_access_gap` | 350 |
| `x:not_started` | 1,628 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 349 |
| `youtube:not_started` | 1,628 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
