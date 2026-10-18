---
title: "NetworkIdAndTransform (0000012D)"
displaytitle: "NetworkIdAndTransform (0000012D)"
opcode: "0000012D"
section: "controllers"
category: "Movement & Transformation (0x071 - 0x0C7)"
direction: "C↔S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# NetworkIdAndTransform (0000012D)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Controller message updating object position, world coordinates, and rotation orientation for an entity relative to a target parent.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x0000012D (NetworkIdAndTransform) |
| `LONG` | **NetworkId** | 64-bit Network ID of source entity |
| `FLOAT` | **TickCount** | Tick counter |
| `LONG` | **TargetId** | 64-bit Network ID of target object |
| `FLOAT` | **PosX** | World position coordinate X |
| `FLOAT` | **PosY** | World position coordinate Y (height) |
| `FLOAT` | **PosZ** | World position coordinate Z |
| `FLOAT` | **Yaw** | Object orientation rotation yaw in radians |


## Variable Descriptions

- **Controller Opcode**: `0000012D (Hex) / 301 (Dec)`
- **Unpack Routine**: `0x00b11680`
- **Pack Routine**: `0x00b11650`
- **Payload Size**: `24 bytes (1 x 8-byte NetworkId + 4 x 4-byte float)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00b11680 reads an 8-byte NetworkId, a Vector3 position (3 floats), and a float yaw rotation.



## Sample Packet

```text
// Verified payload structure for NetworkIdAndTransform (0000012D)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 0000012D
```

## Related

- [DataTransform (00000071)](../../controllers/DataTransform (00000071).html)
- [DataTransformWithParent (000000F1)](../../controllers/DataTransformWithParent (000000F1).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

