---
title: "PlayClientEventLocMessage"
displaytitle: "PlayClientEventLocMessage (0A4E222C)"
opcode: "0A4E222C"
section: "protocols"
category: "General & System Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# PlayClientEventLocMessage (0A4E222C)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client message triggering a client event or particle effect at an explicit world coordinate, scene, and interior cell.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x0A4E222C (PlayClientEventLocMessage) |
| `ASCII` | **EventName** | Asset path or event string identifier |
| `ASCII` | **SceneName** | Planetary terrain scene name (e.g. tatooine, naboo, corellia) |
| `FLOAT` | **X** | World coordinate X |
| `FLOAT` | **Y** | World coordinate Y (altitude) |
| `FLOAT` | **Z** | World coordinate Z |
| `LONG` | **CellId** | 64-bit interior cell object ID (0 for terrain surface) |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `0A4E222C (PlayClientEventLocMessage)`
- **C++ Class**: `PlayClientEventLocMessage (vtables 0x015eb394, 0x015eb38c)`
- **Constructor Address**: `0x00adde0bd (ReadIterator ctor)`
- **Getter Methods**: `getEventName() @ 0x00ade140, getSceneId() @ 0x00ade150, getLocation() @ 0x00ade160, getCell() @ 0x00ade170`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Constructor registers AutoVariable<std::string> EventName (+0x2c), AutoVariable<std::string> SceneName (+0x48), AutoVariable<Vector> Location (+0x64), and AutoVariable<NetworkId> CellId (+0x7c).



## Sample Packet

```text
02 00 2c 22 4e 0a 0b 00 65 76 65 6e 74 2e 63 65 66 08 00 74 61 74 6f 6f 69 6e 65 00 00 c8 42 00 00 34 42 00 00 70 42 00 00 00 00 00 00 00 00
```

## Related

- [PlayClientEventObjectMessage](../../protocols/PlayClientEventObjectMessage.html)
- [PlayClientEffectObjectTransformMessage](../../protocols/PlayClientEffectObjectTransformMessage.html)

