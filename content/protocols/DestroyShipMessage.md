---
title: "DestroyShipMessage"
displaytitle: "DestroyShipMessage (5C680884)"
opcode: "5C680884"
section: "protocols"
category: "Space & Ship Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# DestroyShipMessage (5C680884)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client message informing the client that a starship has been catastrophically destroyed, triggering the primary explosion effect, debris generation, and target removal.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x5C680884 (DestroyShipMessage) |
| `LONG` | **NetworkId** | Unique 64-bit Network ID of the destroyed ship |
| `FLOAT` | **Severity** | Destruction severity multiplier (determines blast radius and debris scale) |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `5C680884 (DestroyShipMessage)`
- **C++ Class**: `DestroyShipMessage (vtables 0x015eaeb0, 0x015eaea8)`
- **Constructor Address**: `0x00ad291c (ReadIterator ctor) / 0x00ad2880 (value ctor)`
- **Getter Methods**: `getNetworkId() @ 0x00ad2950, getSeverity() @ 0x00ad2960`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00ad291c registers two Archive::AutoVariable members: AutoVariable<NetworkId> at +0x2c and AutoVariable<float> at +0x3c.

> [!NOTE]
> **Client Hull Destruction**: Triggers the catastrophic hull breach sequence. If the destroyed ship is the player ship, initiates ejection sequence and death recovery flow.



## Sample Packet

```text
02 00 84 08 68 5c 40 e2 01 00 00 00 00 00 00 00 80 3f
```

## Related

- [DestroyShipComponentMessage](../../protocols/DestroyShipComponentMessage.html)
- [HyperspaceMessage](../../protocols/HyperspaceMessage.html)
- [ShipUpdateTransformCollisionMessage](../../protocols/ShipUpdateTransformCollisionMessage.html)

