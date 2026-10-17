---
title: "SetupSwgSharedNetworkMessages (000000E1)"
displaytitle: "SetupSwgSharedNetworkMessages (000000E1)"
opcode: "000000E1"
section: "controllers"
category: "Effects & Audio (0xA1 - 0x100)"
direction: "C↔S"
completion: "0%"
sample_status: "absent"
status: "stub"
---

# SetupSwgSharedNetworkMessages (000000E1)

> [!CAUTION]
> **Documentation Pending / Reversal Needed**
> This packet was identified in SWG network specifications (Opcode: `000000E1`), but requires packet captures to fully verify all payload offsets.

Shared network object controller message 0x000000E1 handling shared network synchronization in the SWG client/server object controller pipeline.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `INT` | **Operand_Count** | 0x0000000B (ObjControllerMessage wrapper) |
| `INT` | **ControllerOpcode** | 0x000000E1 |
| `LONG` | **NetworkId** | Target object network identifier |
| `INT` | **TickCount** | Client/Server synchronization tick counter |
| `DATA` | **SubsystemPayload** | Payload parameters (pending capture) |


## Variable Descriptions

- **Controller Opcode**: `000000E1 (Hex) / 225 (Dec)`
- **Operand Count**: `11 (Standard ObjController)`
- **Subsystem**: `Shared Network Subsystem`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Referenced in the master ObjControllerMessage table. Structure follows standard ObjControllerMessage envelope (NetworkId + TickCount) followed by subsystem data.



## Sample Packet

```text
// Sample packet capture pending for opcode 000000E1
```

## Related

- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

