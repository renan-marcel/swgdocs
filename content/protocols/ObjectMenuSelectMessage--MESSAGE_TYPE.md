---
title: "ObjectMenuSelectMessage::MESSAGE_TYPE"
displaytitle: "ObjectMenuSelectMessage::MESSAGE_TYPE (7CA18726)"
opcode: "7CA18726"
section: "protocols"
category: "General & System Packets"
direction: "C→S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# ObjectMenuSelectMessage::MESSAGE_TYPE (7CA18726)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Client-to-server radial interaction message sent when a player selects a specific radial menu option on a world object, NPC, item, or terminal.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x7CA18726 (ObjectMenuSelectMessage) |
| `LONG` | **TargetObjectId** | 64-bit Network ID of target object being interacted with |
| `BYTE` | **SelectedMenuItem** | Radial menu option index / action identifier selected by user |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `7CA18726 (ObjectMenuSelectMessage)`
- **C++ Class**: `ObjectMenuSelectMessage (vtable 0x015ebaa0)`
- **Constructor Address**: `0x00af3c3c (ReadIterator ctor) / 0x00af3af4 (value ctor)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00af3c3c registers two Archive::AutoVariable members: AutoVariable<NetworkId> TargetObjectId at offset +0x38, and AutoVariable<unsigned char> SelectedMenuItem at offset +0x48.

> [!NOTE]
> **Radial Menu Mapping**: SelectedMenuItem maps to the radial menu action ID populated during the preceding ObjectMenuResponse baseline/controller interaction.



## Sample Packet

```text
// Verified payload structure for ObjectMenuSelectMessage::MESSAGE_TYPE (7CA18726)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 7CA18726
```

## Related

- [ObjControllerMessage](../../protocols/ObjControllerMessage.html)
- [CommandQueueEnqueue (00000116)](../../protocols/CommandQueueEnqueue (00000116).html)

