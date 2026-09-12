# Claims ledger: US household energy burden

**Check date:** 2026-09-11  
**Scope:** US homes, energy bills, housing, utility insecurity, and public help

| ID | Claim | Evidence type | What supports it | Limit |
|---|---|---|---|---|
| C-001 | Energy burden is higher for low-income households. | DOE data tool | DOE reports an average burden of about 6% for low-income households versus about 2% for other households. | These are modeled and survey-linked averages, not each home's bill. |
| C-002 | Energy insecurity can mean a direct tradeoff with food or medicine. | 2024 EIA household survey | EIA reports 32.89 million primary homes where someone reduced or went without food or medicine to pay energy costs. | Respondents may report more than one insecurity; the table does not show the full sequence. |
| C-003 | A notice, an unsafe temperature, and a shutoff are different events. | EIA survey definitions | The 2024 table separates disconnect notices, unhealthy temperatures, and inability to use heating or cooling equipment. | It does not show whether a notice became a shutoff or how long the condition lasted. |
| C-004 | Renters may pay the energy bill without controlling the building improvement. | DOE housing and energy data | DOE estimates that 52% of low-income households are renters and describes this split between who pays and who can improve the building. | The estimate does not show which landlord makes which investment. |
| C-005 | A utility allowance can change whether assisted housing remains affordable. | GAO analysis | GAO estimated that 56% of voucher households were rent-burdened when actual utility expenses were included, versus 32% under its baseline assumption. | The estimates use different utility assumptions and do not follow later household choices. |
| C-006 | Energy help can reduce a bill without proving that food, health, work, or housing outcomes improved. | Inference from C-001 through C-005 | The records show burden and possible relief points, but not one household's complete before-and-after path. | Linked administrative and household outcome data remain needed. |

## Mechanism under test

```text
home, fuel, and utility condition
  -> energy bill or insecurity
  -> food, medicine, rent, debt, work, or comfort tradeoff
  -> aid, shutoff, weatherization, or landlord response
  -> health, housing, work, and public trust
```

## Next test

Join energy insecurity with rent or ownership, building condition, income, utility payment responsibility, assistance, and later health or housing outcomes. Mark whether each record is a bill, a missed service, a coping action, or a measured result.
