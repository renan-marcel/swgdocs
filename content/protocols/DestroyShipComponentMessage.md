---
title: "DestroyShipComponentMessage"
displaytitle: "DestroyShipComponentMessage (3871D784)"
opcode: "3871D784"
section: "protocols"
category: "Space & Ship Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# DestroyShipComponentMessage (3871D784)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client notification sent when an individual subsystem or component of a starship (e.g. engine, shield generator, weapon capacitor, reactor) is completely destroyed in space combat.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x3871D784 (DestroyShipComponentMessage) |
| `LONG` | **NetworkId** | Unique 64-bit Network ID of the affected ship object |
| `INT` | **ComponentIndex** | Ship component slot index destroyed (0-indexed chassis slot) |
| `FLOAT` | **Severity** | Destruction / explosion severity multiplier |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `3871D784 (DestroyShipComponentMessage)`
- **C++ Class**: `DestroyShipComponentMessage (vtables 0x015eaed0, 0x015eaec8)`
- **Constructor Address**: `0x00ad2bd5 (ReadIterator ctor) / 0x00ad2b30 (value ctor)`
- **Getter Methods**: `getNetworkId() @ 0x00ad2c20, getComponentIndex() @ 0x00ad2c30, getSeverity() @ 0x00ad2c40`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00ad2bd5 registers three Archive::AutoVariable members in exact sequence: AutoVariable<NetworkId> at +0x2c, AutoVariable<int> at +0x3c, and AutoVariable<float> at +0x4c.

> [!NOTE]
> **Space Combat Component System**: ComponentIndex maps to the ship component slot definition in the client ship datatable (chassis component index). When received, the client triggers component destruction audio-visual effects and updates ship component health in the ship status MFD.



## Sample Packet

```text
02 00 84 d7 71 38 40 e2 01 00 00 00 00 00 02 00 00 00 00 00 80 3f
```

## Related

- [DestroyShipMessage](../../protocols/DestroyShipMessage.html)
- [ShipUpdateTransformCollisionMessage](../../protocols/ShipUpdateTransformCollisionMessage.html)
- [UpdateMissileMessage](../../protocols/UpdateMissileMessage.html)

