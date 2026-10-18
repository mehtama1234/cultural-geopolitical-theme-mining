# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **205**
- Exact linked social items: **210**
- Record statuses: `{'augmented': 201, 'documented_access_gap': 799, 'in_review': 25, 'queued': 953}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 167 |
| `linkedin:documented_access_gap` | 837 |
| `linkedin:not_started` | 974 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 960 |
| `reddit:not_started` | 978 |
| `x:documented_access_gap` | 1,000 |
| `x:not_started` | 978 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 999 |
| `youtube:not_started` | 978 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
