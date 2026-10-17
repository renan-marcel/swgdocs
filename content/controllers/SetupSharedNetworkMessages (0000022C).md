---
title: "SetupSharedNetworkMessages (0000022C)"
displaytitle: "SetupSharedNetworkMessages (0000022C)"
opcode: "0000022C"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "C↔S"
completion: "0%"
sample_status: "absent"
status: "stub"
---

# SetupSharedNetworkMessages (0000022C)

> [!CAUTION]
> **Documentation Pending / Reversal Needed**
> This packet was identified in SWG network specifications (Opcode: `0000022C`), but requires packet captures to fully verify all payload offsets.

Shared network controller message 0x0000022C for advanced subsystem triggers and image design / player interaction synchronization.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `INT` | **Operand_Count** | 0x0000000B (ObjControllerMessage wrapper) |
| `INT` | **ControllerOpcode** | 0x0000022C |
| `LONG` | **NetworkId** | Target object network identifier |
| `INT` | **TickCount** | Tick counter |
| `DATA` | **SubsystemPayload** | Payload parameters (pending capture) |


## Variable Descriptions

- **Controller Opcode**: `0000022C (Hex) / 556 (Dec)`
- **Subsystem**: `Shared Network Subsystem`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Coexists alongside ImageDesignStartMessage (0000022C) in the 0x22C opcode space.



## Sample Packet

```text
// Sample packet capture pending for opcode 0000022C
```

## Related

- [ImageDesignStartMessage (0000022C)](../../controllers/ImageDesignStartMessage (0000022C).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

