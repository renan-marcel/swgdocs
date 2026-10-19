---
title: "ShipUpdateTransformCollisionMessage"
displaytitle: "ShipUpdateTransformCollisionMessage (763648D0)"
opcode: "763648D0"
section: "protocols"
category: "Space & Ship Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# ShipUpdateTransformCollisionMessage (763648D0)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client physics synchronization message updating a ship position, orientation matrix, linear velocity vector, and collision sequence timestamp.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x763648D0 (ShipUpdateTransformCollisionMessage) |
| `LONG` | **ShipId** | 64-bit Network ID of the colliding starship |
| `FLOAT[12]` | **Transform** | Position & orientation matrix (3x3 rotation + translation vector) |
| `FLOAT[3]` | **Velocity** | Linear velocity vector (Vx, Vy, Vz) |
| `INT` | **SyncStamp** | Movement sequence / synchronization timestamp |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `763648D0 (ShipUpdateTransformCollisionMessage)`
- **C++ Class**: `ShipUpdateTransformCollisionMessage (vtables 0x015eb03c, 0x015eb034)`
- **Constructor Address**: `0x00ad611c (ReadIterator ctor)`
- **AutoVariables**: `AutoVariable<NetworkId> (+0x2c), AutoVariable<Transform> (+0x3c), AutoVariable<Vector> (+0x74), AutoVariable<unsigned long> (+0x8c)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00ad611c registers 4 AutoVariables: ShipId, Transform (48 bytes), Velocity Vector (12 bytes), and SyncStamp (4 bytes).

> [!NOTE]
> **Collision Handling**: Used when a ship collides with another ship, terrain, asteroid, or space station to correct ship trajectory client-side and synchronize physical bounce velocity.



## Sample Packet

```text
02 00 d0 48 36 76 40 e2 01 00 00 00 00 00 00 00 80 3f 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3f 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3f 00 00 00 00 00 00 00 00 00 00 00 00 00 00 20 41 00 00 00 00 00 00 00 00 01 00 00 00
```

## Related

- [ShipUpdateTransformMessage](../../protocols/ShipUpdateTransformMessage.html)
- [DestroyShipMessage](../../protocols/DestroyShipMessage.html)
- [DestroyShipComponentMessage](../../protocols/DestroyShipComponentMessage.html)

