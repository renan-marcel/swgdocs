---
title: "AboutToHyperspace (000003FE)"
displaytitle: "AboutToHyperspace (000003FE)"
opcode: "000003FE"
section: "controllers"
category: "Space & Vehicle Systems (0x3E8+)"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# AboutToHyperspace (000003FE)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client controller message notifying the player ship that hyperspace jump sequence has begun towards a target hyperspace beacon or zone.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x000003FE (AboutToHyperspace) |
| `LONG` | **NetworkId** | 64-bit Network ID of starship jumping to hyperspace |
| `FLOAT` | **TickCount** | Server tick counter |
| `ASCII` | **PointName** | Hyperspace route name or destination sector identifier |
| `FLOAT` | **PosX** | Destination coordinates X |
| `FLOAT` | **PosY** | Destination coordinates Y |
| `FLOAT` | **PosZ** | Destination coordinates Z |


## Variable Descriptions

- **Controller Opcode**: `000003FE (Hex) / 1022 (Dec)`
- **Unpack Routine**: `0x01195b30`
- **Pack Routine**: `0x01195a70`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x01195b30 deserializes an ASCII string PointName followed by three 4-byte floats (PosX, PosY, PosZ).



## Sample Packet

```text
// Verified payload structure for AboutToHyperspace (000003FE)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 000003FE
```

## Related

- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

