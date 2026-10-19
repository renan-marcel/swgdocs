---
title: "UpdateMissileMessage"
displaytitle: "UpdateMissileMessage (1228CD01)"
opcode: "1228CD01"
section: "protocols"
category: "Space & Ship Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# UpdateMissileMessage (1228CD01)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client missile tracking message updating projectile target component, firing weapon index, and in-flight tracking status.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x1228CD01 (UpdateMissileMessage) |
| `LONG` | **NetworkId** | 64-bit Network ID of missile projectile object |
| `INT` | **WeaponIndex** | Launcher weapon slot index on attacking ship |
| `INT` | **TargetComponent** | Target subsystem index being locked/homed onto |
| `INT` | **Status** | Missile state flag (tracking, lost lock, detonated) |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `1228CD01 (UpdateMissileMessage)`
- **C++ Class**: `UpdateMissileMessage (vtables 0x015eb0a0, 0x015eb098)`
- **Constructor Address**: `0x00ad6e6e (ReadIterator ctor)`
- **AutoVariables**: `AutoVariable<NetworkId> (+0x2c), AutoVariable<int> (+0x3c), AutoVariable<int> (+0x4c), AutoVariable<int> (+0x5c)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine registers AutoVariable<NetworkId> NetworkId, followed by three AutoVariable<int> fields for WeaponIndex, TargetComponent, and Status.



## Sample Packet

```text
02 00 01 cd 28 12 40 e2 01 00 00 00 00 00 00 00 00 00 03 00 00 00 01 00 00 00
```

## Related

- [CreateMissileMessage](../../protocols/CreateMissileMessage.html)
- [DestroyShipComponentMessage](../../protocols/DestroyShipComponentMessage.html)

