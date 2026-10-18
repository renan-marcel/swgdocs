---
title: "UpdateShipOnCollision (000003FD)"
displaytitle: "UpdateShipOnCollision (000003FD)"
opcode: "000003FD"
section: "controllers"
category: "Space & Vehicle Systems (0x3E8+)"
direction: "C↔S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# UpdateShipOnCollision (000003FD)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Controller message synchronizing starship collision dynamics, surface rebound normals, and reflection velocities when colliding with asteroids or space stations.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x000003FD (UpdateShipOnCollision) |
| `LONG` | **NetworkId** | 64-bit Network ID of colliding starship object |
| `FLOAT` | **TickCount** | Physics tick counter |
| `FLOAT` | **NormalX** | Collision obstacle surface normal vector X |
| `FLOAT` | **NormalY** | Collision obstacle surface normal vector Y |
| `FLOAT` | **NormalZ** | Collision obstacle surface normal vector Z |
| `FLOAT` | **VelocityX** | Ship reflection velocity vector X |
| `FLOAT` | **VelocityY** | Ship reflection velocity vector Y |
| `FLOAT` | **VelocityZ** | Ship reflection velocity vector Z |
| `FLOAT` | **Severity** | Collision impact speed / severity magnitude |


## Variable Descriptions

- **Controller Opcode**: `000003FD (Hex) / 1021 (Dec)`
- **C++ Class**: `MessageQueueUpdateShipOnCollision (vtable 0x015ec1bc)`
- **Unpack Routine**: `0x00b10c10`
- **Pack Routine**: `0x00b10b60`
- **Payload Size**: `28 bytes (7 x 4-byte float fields)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00b10c10 reads two Vector3s (surface normal and velocity) and a float severity before instantiating MessageQueueUpdateShipOnCollision.



## Sample Packet

```text
// Verified payload structure for UpdateShipOnCollision (000003FD)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 000003FD
```

## Related

- [ShipHit (00000432)](../../controllers/ShipHit (00000432).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

