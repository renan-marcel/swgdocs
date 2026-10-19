---
title: "HyperspaceMessage"
displaytitle: "HyperspaceMessage (CBF88482)"
opcode: "CBF88482"
section: "protocols"
category: "Space & Ship Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# HyperspaceMessage (CBF88482)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client message indicating that a starship has engaged hyperspace engines, initiating the star-stretch acceleration visual effect and hyperspace transition sound.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0xCBF88482 (HyperspaceMessage) |
| `LONG` | **NetworkId** | Unique 64-bit Network ID of the ship jumping to hyperspace |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `CBF88482 (HyperspaceMessage)`
- **C++ Class**: `HyperspaceMessage (vtables 0x015eb020, 0x015eb018)`
- **Constructor Address**: `0x00ad5fba (ReadIterator ctor) / 0x00ad5f40 (value ctor)`
- **Getter Methods**: `getNetworkId() @ 0x00ad5ff0`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00ad5fba registers a single AutoVariable<NetworkId> at offset +0x2c.

> [!NOTE]
> **Space Engine Effect**: The client attaches the hyperspace warp shader effect to the specified ship mesh and plays the hyperspace entry audio event.



## Sample Packet

```text
02 00 82 84 f8 cb 40 e2 01 00 00 00 00 00
```

## Related

- [DestroyShipMessage](../../protocols/DestroyShipMessage.html)
- [ShipUpdateTransformCollisionMessage](../../protocols/ShipUpdateTransformCollisionMessage.html)
- [ShipUpdateTransformMessage](../../protocols/ShipUpdateTransformMessage.html)

