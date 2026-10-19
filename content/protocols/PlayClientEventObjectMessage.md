---
title: "PlayClientEventObjectMessage"
displaytitle: "PlayClientEventObjectMessage (AF83C3F2)"
opcode: "AF83C3F2"
section: "protocols"
category: "General & System Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# PlayClientEventObjectMessage (AF83C3F2)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client message triggering a client event or particle effect attached directly to a mesh hardpoint on a target world object.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0xAF83C3F2 (PlayClientEventObjectMessage) |
| `ASCII` | **EventName** | Asset path or event string identifier |
| `ASCII` | **HardpointName** | Hardpoint attachment point name on target mesh (e.g. muzzle, head, chest) |
| `LONG` | **TargetId** | 64-bit Network ID of target object |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `AF83C3F2 (PlayClientEventObjectMessage)`
- **C++ Class**: `PlayClientEventObjectMessage (vtables 0x015eb35c, 0x015eb354)`
- **Constructor Address**: `0x00add830 (ReadIterator ctor)`
- **Getter Methods**: `getTargetId() @ 0x00add880, getEventName() @ 0x00add890, getHardpointName() @ 0x00add8a0`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Constructor registers AutoVariable<std::string> EventName (+0x2c), AutoVariable<std::string> HardpointName (+0x48), and AutoVariable<NetworkId> TargetId (+0x64).



## Sample Packet

```text
02 00 f2 c3 83 af 0b 00 65 76 65 6e 74 2e 63 65 66 06 00 6d 75 7a 7a 6c 65 40 e2 01 00 00 00 00 00
```

## Related

- [PlayClientEventLocMessage](../../protocols/PlayClientEventLocMessage.html)
- [PlayClientEffectObjectTransformMessage](../../protocols/PlayClientEffectObjectTransformMessage.html)

