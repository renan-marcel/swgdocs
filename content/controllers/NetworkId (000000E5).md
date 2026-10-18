---
title: "NetworkId (000000E5)"
displaytitle: "NetworkId (000000E5)"
opcode: "000000E5"
section: "controllers"
category: "Core Object Triggers (0x0C8 - 0x0F0)"
direction: "C↔S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# NetworkId (000000E5)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Standard single NetworkId controller message payload used for single-target object actions, targeting notifications, and entity state requests.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x000000E5 |
| `LONG` | **NetworkId** | 64-bit Network ID of source entity |
| `FLOAT` | **TickCount** | Tick counter |
| `LONG` | **TargetId** | 64-bit Network ID of target object or entity |


## Variable Descriptions

- **Controller Opcode**: `000000E5 (Hex) / 229 (Dec)`
- **Unpack Routine**: `0x00ade520`
- **Pack Routine**: `0x00ade500`
- **Payload Size**: `8 bytes (1 x 8-byte NetworkId)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Shared unpack routine 0x00ade520 reads a single 8-byte NetworkId for messages 0xE5, 0xE6, 0xE7, 0xE8, 0xE9, 0x114, 0x11C, 0x126, 0x127, 0x142, and 0x153.



## Sample Packet

```text
// Verified payload structure for NetworkId (000000E5)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 000000E5
```

## Related

- [NetworkIdPair (000000EB)](../../controllers/NetworkIdPair (000000EB).html)
- [NetworkIdAndTransform (0000012D)](../../controllers/NetworkIdAndTransform (0000012D).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

