---
title: "CraftSelectSchematic (0000010E)"
displaytitle: "CraftSelectSchematic (0000010E)"
opcode: "0000010E"
section: "controllers"
category: "Crafting & Command Queue (0x101 - 0x150)"
direction: "C→S"
completion: "0%"
sample_status: "absent"
status: "stub"
---

# CraftSelectSchematic (0000010E)

> [!CAUTION]
> **Documentation Pending / Reversal Needed**
> This packet was identified in SWG network specifications (Opcode: `0000010E`), but requires packet captures to fully verify all payload offsets.

Client crafting controller message sent when a player chooses a schematic draft from a crafting tool to initiate an item assembly session.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `INT` | **Operand_Count** | 0x0000000B (ObjControllerMessage wrapper) |
| `INT` | **ControllerOpcode** | 0x0000010E |
| `LONG` | **CraftingToolId** | Object ID of crafting station or tool in use |
| `INT` | **TickCount** | Client tick counter |
| `INT` | **SchematicCrc** | CRC32 identifier of the selected draft schematic |


## Variable Descriptions

- **Controller Opcode**: `0000010E (Hex) / 270 (Dec)`
- **Subsystem**: `Crafting System`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Transmitted when the user double-clicks or selects a schematic from the crafting tool dialog to proceed to the ingredient assembly stage.



## Sample Packet

```text
// Sample packet capture pending for opcode 0000010E
```

## Related

- [CraftIngredients (00000105)](../../controllers/CraftIngredients (00000105).html)
- [CraftRequestSession (0000010E)](../../controllers/CraftRequestSession (0000010E).html)
- [NextCraftingStage (00000109)](../../controllers/NextCraftingStage (00000109).html)

