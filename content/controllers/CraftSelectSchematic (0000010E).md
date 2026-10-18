---
title: "CraftSelectSchematic (0000010E)"
displaytitle: "CraftSelectSchematic (0000010E)"
opcode: "0000010E"
section: "controllers"
category: "Crafting Subsystem (0x105 - 0x124)"
direction: "C→S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# CraftSelectSchematic (0000010E)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Client-to-server controller message sent when a player selects a draft schematic from the crafting tool or station schematic browser.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x0000010E (CraftSelectSchematic) |
| `LONG` | **NetworkId** | 64-bit Network ID of crafting tool or station |
| `FLOAT` | **TickCount** | Client tick counter |
| `INT` | **SchematicIndex** | Selected draft schematic index / CRC identifier in manufacturing schematic table |


## Variable Descriptions

- **Controller Opcode**: `0000010E (Hex) / 270 (Dec)`
- **C++ Class**: `MessageQueueCraftSelectSchematic (vtable 0x015ec254)`
- **Unpack Routine**: `0x00b1a7f0`
- **Pack Routine**: `0x00b1a7d0`
- **Constructor Address**: `0x00b1a700`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00b1a7f0 reads a 4-byte INT SchematicIndex and constructs MessageQueueCraftSelectSchematic.

> [!NOTE]
> **Disambiguation Note**: Previous wiki extractions conflated 0x0000010E with CraftRequestSession. Binary analysis proves 0x0000010E is MessageQueueCraftSelectSchematic, whereas 0x0000010F is MessageQueueCraftRequestSession.



## Sample Packet

```text
// Verified payload structure for CraftSelectSchematic (0000010E)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 0000010E
```

## Related

- [CraftRequestSession (0000010F)](../../controllers/CraftRequestSession (0000010F).html)
- [DraftSlotsQueryResponse (000001BF)](../../controllers/DraftSlotsQueryResponse (000001BF).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

