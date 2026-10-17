---
title: "ObjectMenuSelectMessage::MESSAGE_TYPE"
displaytitle: "ObjectMenuSelectMessage::MESSAGE_TYPE (7CA18726)"
opcode: "7CA18726"
section: "protocols"
category: "General & System Packets"
direction: "C→S"
completion: "0%"
sample_status: "absent"
status: "stub"
---

# ObjectMenuSelectMessage::MESSAGE_TYPE (7CA18726)

> [!CAUTION]
> **Documentation Pending / Reversal Needed**
> This packet was identified in SWG network specifications (Opcode: `7CA18726`), but requires packet captures to fully verify all payload offsets.

Client-to-server radial interaction message sent when a player selects a specific radial menu option on a world object or NPC.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Number of operands (header) |
| `INT` | **Opcode** | 0x7CA18726 |
| `LONG` | **TargetObjectId** | Network ID of target object being interacted with |
| `BYTE` | **SelectedMenuItem** | Radial menu option index / action identifier |
| `BYTE` | **SubMenuItem** | Sub-menu selection index if applicable |


## Variable Descriptions

- **Operand_Count**: `3`
- **Opcode**: `7CA18726 (Client Packet)`
- **Subsystem**: `Radial Object Menu Interaction`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Dispatched when the user clicks an entry on the radial menu (e.g. Open, Examine, Loot, Board Ship). Paired with ObjectMenuSelectResponseMessage from the server.



## Sample Packet

```text
// Sample packet capture pending for opcode 7CA18726
```

## Related

- [ObjectMenuSelectResponseMessage](../../protocols/ObjectMenuSelectResponseMessage.html)
- [ObjectAttributeManager (PacketTypeGroup)](../../protocols/ObjectAttributeManager (PacketTypeGroup).html)

