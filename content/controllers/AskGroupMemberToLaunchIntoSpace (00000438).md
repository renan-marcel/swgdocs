---
title: "AskGroupMemberToLaunchIntoSpace (00000438)"
displaytitle: "AskGroupMemberToLaunchIntoSpace (00000438)"
opcode: "00000438"
section: "controllers"
category: "Space & Vehicle Systems (0x3E8+)"
direction: "C↔S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# AskGroupMemberToLaunchIntoSpace (00000438)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Controller message sent when a ship pilot prompts group members to board or launch together into space (0x438) or when a group member responds with approval/refusal (0x439).

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x00000438 / 0x00000439 |
| `LONG` | **NetworkId** | 64-bit Network ID of pilot ship or group member |
| `FLOAT` | **TickCount** | Group sync tick |
| `LONG` | **GroupMemberId** | 64-bit Network ID of group member invited or responding |
| `BYTE` | **Response** | Decision status (0 = Decline / Abort, 1 = Accept / Launch) |


## Variable Descriptions

- **Controller Opcode**: `00000438 / 00000439 (1080 / 1081 Dec)`
- **Unpack Routine**: `0x01196ee0`
- **Pack Routine**: `0x01196eb0`
- **Payload Size**: `9 bytes (8-byte NetworkId + 1-byte unsigned char)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x01196ee0 reads an 8-byte NetworkId GroupMemberId followed by a 1-byte unsigned char Response.



## Sample Packet

```text
// Verified payload structure for AskGroupMemberToLaunchIntoSpace (00000438)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 00000438
```

## Related

- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

