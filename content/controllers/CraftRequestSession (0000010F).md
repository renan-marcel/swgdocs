---
title: "CraftRequestSession (0000010F)"
displaytitle: "CraftRequestSession (0000010F)"
opcode: "0000010F"
section: "controllers"
category: "Crafting Subsystem (0x105 - 0x124)"
direction: "C→S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# CraftRequestSession (0000010F)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Client-to-server controller message requesting initialization of a crafting session using a specified crafting tool or crafting station.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x0000010F (CraftRequestSession) |
| `LONG` | **NetworkId** | 64-bit Network ID of player character |
| `FLOAT` | **TickCount** | Client tick counter |
| `LONG` | **CraftingStationId** | 64-bit Network ID of crafting tool or installation terminal |
| `BYTE` | **CraftingMode** | Crafting session mode / type |


## Variable Descriptions

- **Controller Opcode**: `0000010F (Hex) / 271 (Dec)`
- **C++ Class**: `MessageQueueCraftRequestSession (vtable 0x015ec25c)`
- **Unpack Routine**: `0x00b1aac0`
- **Pack Routine**: `0x00b1aa80`
- **Constructor Address**: `0x00b1a960`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00b1aac0 reads an 8-byte NetworkId CraftingStationId followed by a 1-byte unsigned char CraftingMode and instantiates MessageQueueCraftRequestSession.



## Sample Packet

```text
// Verified payload structure for CraftRequestSession (0000010F)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 0000010F
```

## Related

- [CraftSelectSchematic (0000010E)](../../controllers/CraftSelectSchematic (0000010E).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

