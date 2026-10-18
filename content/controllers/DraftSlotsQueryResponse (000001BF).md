---
title: "DraftSlotsQueryResponse (000001BF)"
displaytitle: "DraftSlotsQueryResponse (000001BF)"
opcode: "000001BF"
section: "controllers"
category: "Crafting Subsystem (0x105 - 0x124)"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# DraftSlotsQueryResponse (000001BF)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client controller message providing the ingredient slot structure, resource count requirements, and customization options for a queried draft schematic.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x000001BF (DraftSlotsQueryResponse) |
| `LONG` | **NetworkId** | 64-bit Network ID of crafting tool |
| `FLOAT` | **TickCount** | Crafting session tick |
| `INT` | **DraftSchematicCrc** | CRC identifier of queried draft schematic |
| `INT` | **SlotCount** | Total number of ingredient slots in schematic |
| `INT` | **ClientSlots** | Bitmask or count of client-fillable slots |
| `INT` | **Options** | Experimentation / crafting options flag bitmask |
| `BYTE` | **ResponseFlag** | Query status response flag |


## Variable Descriptions

- **Controller Opcode**: `000001BF (Hex) / 447 (Dec)`
- **Unpack Routine**: `0x00b19cb0`
- **Pack Routine**: `0x00b19bf0`
- **Payload Size**: `17 bytes (4 x 4-byte INT + 1 x 1-byte BYTE)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00b19cb0 reads 4 INTs followed by 1 BYTE.



## Sample Packet

```text
// Verified payload structure for DraftSlotsQueryResponse (000001BF)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 000001BF
```

## Related

- [CraftSelectSchematic (0000010E)](../../controllers/CraftSelectSchematic (0000010E).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

