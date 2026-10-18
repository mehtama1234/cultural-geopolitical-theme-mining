# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **73**
- Exact linked social items: **78**
- Record statuses: `{'augmented': 73, 'documented_access_gap': 202, 'queued': 1703}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 35 |
| `linkedin:documented_access_gap` | 240 |
| `linkedin:not_started` | 1,703 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 235 |
| `reddit:not_started` | 1,703 |
| `x:documented_access_gap` | 275 |
| `x:not_started` | 1,703 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 274 |
| `youtube:not_started` | 1,703 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
