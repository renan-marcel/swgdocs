---
title: "NetworkIdPair (000000EB)"
displaytitle: "NetworkIdPair (000000EB)"
opcode: "000000EB"
section: "controllers"
category: "Core Object Triggers (0x0C8 - 0x0F0)"
direction: "C↔S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# NetworkIdPair (000000EB)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Controller message payload transmitting a pair of Network IDs for container transfers, parent/child relationships, or mutual interactions.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x000000EB / 0x000000EC |
| `LONG` | **NetworkId** | 64-bit Network ID of source entity |
| `FLOAT` | **TickCount** | Tick counter |
| `LONG` | **FirstId** | First 64-bit Network ID (e.g. source container or item) |
| `LONG` | **SecondId** | Second 64-bit Network ID (e.g. destination container or target) |


## Variable Descriptions

- **Controller Opcode**: `000000EB / 000000EC (235 / 236 Dec)`
- **Unpack Routine**: `0x00b153b0`
- **Pack Routine**: `0x00b15380`
- **Payload Size**: `16 bytes (2 x 8-byte NetworkId)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00b153b0 reads two consecutive 8-byte NetworkIds.



## Sample Packet

```text
// Verified payload structure for NetworkIdPair (000000EB)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 000000EB
```

## Related

- [NetworkId (000000E5)](../../controllers/NetworkId (000000E5).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

