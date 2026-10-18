# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **215**
- Exact linked social items: **220**
- Record statuses: `{'augmented': 215, 'documented_access_gap': 835, 'queued': 928}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 177 |
| `linkedin:documented_access_gap` | 873 |
| `linkedin:not_started` | 928 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,010 |
| `reddit:not_started` | 928 |
| `x:documented_access_gap` | 1,050 |
| `x:not_started` | 928 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,049 |
| `youtube:not_started` | 928 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
