---
title: "SetupSwgSharedNetworkMessages (0000043C)"
displaytitle: "SetupSwgSharedNetworkMessages (0000043C)"
opcode: "0000043C"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "C↔S"
completion: "0%"
sample_status: "absent"
status: "stub"
---

# SetupSwgSharedNetworkMessages (0000043C)

> [!CAUTION]
> **Documentation Pending / Reversal Needed**
> This packet was identified in SWG network specifications (Opcode: `0000043C`), but requires packet captures to fully verify all payload offsets.

Jump to Lightspeed / Space flight controller message for ship component and flight state updates.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `INT` | **Operand_Count** | 0x0000000B (ObjControllerMessage wrapper) |
| `INT` | **ControllerOpcode** | 0x0000043C |
| `LONG` | **ShipId** | Network ID of ship object |
| `INT` | **TickCount** | Tick counter |
| `DATA` | **FlightData** | Flight subsystem parameters (pending capture) |


## Variable Descriptions

- **Controller Opcode**: `0000043C (Hex) / 1084 (Dec)`
- **Subsystem**: `Jump to Lightspeed (JTL) Space Flight`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Part of the 0x438-0x43F block handling ship launches, hyperspace transitions, and group space invitations.



## Sample Packet

```text
// Sample packet capture pending for opcode 0000043C
```

## Related

- [AskGroupMemberToLaunchIntoSpace (00000438)](../../controllers/AskGroupMemberToLaunchIntoSpace (00000438).html)
- [GroupMemberInvitationToLaunchIntoSpaceResponse (00000439)](../../controllers/GroupMemberInvitationToLaunchIntoSpaceResponse (00000439).html)

