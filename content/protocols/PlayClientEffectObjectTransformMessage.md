---
title: "PlayClientEffectObjectTransformMessage"
displaytitle: "PlayClientEffectObjectTransformMessage (4F5E09B6)"
opcode: "4F5E09B6"
section: "protocols"
category: "General & System Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# PlayClientEffectObjectTransformMessage (4F5E09B6)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client message triggering a client-side particle/audio effect (.cef) attached to a specific world object with a relative transform matrix.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x4F5E09B6 (PlayClientEffectObjectTransformMessage) |
| `ASCII` | **EffectName** | Asset path to the client effect file (.cef) |
| `LONG` | **NetworkId** | 64-bit Network ID of target object anchor |
| `FLOAT[12]` | **Transform** | Relative transform matrix (3x3 rotation matrix + 3D position vector) |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `4F5E09B6 (PlayClientEffectObjectTransformMessage)`
- **C++ Class**: `PlayClientEffectObjectTransformMessage (vtables 0x015eb324, 0x015eb31c)`
- **Constructor Address**: `0x00adce74 (ReadIterator ctor)`
- **Serialization Members**: `AutoVariable<std::string> (+0x2c), AutoVariable<NetworkId> (+0x48), AutoVariable<Transform> (+0x58)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine registers AutoVariable<std::string> (EffectName), AutoVariable<NetworkId> (TargetId), and AutoVariable<Transform> (LocalTransform).

> [!NOTE]
> **Transform Serialization**: Transform serializes a 3x3 rotation matrix followed by a 3-element translation vector (12 floats total, 48 bytes).



## Sample Packet

```text
02 00 b6 09 5e 4f 0e 00 63 6c 69 65 6e 74 65 66 66 65 63 74 2e 63 65 66 40 e2 01 00 00 00 00 00 00 00 80 3f 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3f 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3f 00 00 00 00 00 00 00 00 00 00 00 00
```

## Related

- [PlayClientEventLocMessage](../../protocols/PlayClientEventLocMessage.html)
- [PlayClientEventObjectMessage](../../protocols/PlayClientEventObjectMessage.html)

