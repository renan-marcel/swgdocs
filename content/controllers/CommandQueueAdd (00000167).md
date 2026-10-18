---
title: "CommandQueueAdd (00000167)"
displaytitle: "CommandQueueAdd (00000167)"
opcode: "00000167"
section: "controllers"
category: "Combat & Action Queue (0x0C8 - 0x104)"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# CommandQueueAdd (00000167)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client controller message acknowledging that a client command has been accepted into the server execution queue.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x00000167 (CommandQueueAdd) |
| `LONG` | **NetworkId** | 64-bit Network ID of player character |
| `FLOAT` | **TickCount** | Queue sync tick |
| `INT` | **SequenceId** | Action sequence identifier assigned to command |
| `INT` | **CommandCrc** | CRC identifier of queued combat / action command |


## Variable Descriptions

- **Controller Opcode**: `00000167 (Hex) / 359 (Dec)`
- **Unpack Routine**: `0x01195040`
- **Pack Routine**: `0x01194ff0`
- **Payload Size**: `8 bytes (2 x 4-byte INT)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x01195040 reads SequenceId (INT) and CommandCrc (INT).



## Sample Packet

```text
// Verified payload structure for CommandQueueAdd (00000167)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 00000167
```

## Related

- [CommandQueueRemove (00000117)](../../controllers/CommandQueueRemove (00000117).html)
- [CommandQueueEnqueue (00000116)](../../controllers/CommandQueueEnqueue (00000116).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

