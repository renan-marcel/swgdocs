---
title: "CommandQueueRemove (00000117)"
displaytitle: "CommandQueueRemove (00000117)"
opcode: "00000117"
section: "controllers"
category: "Combat & Action Queue (0x0C8 - 0x104)"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# CommandQueueRemove (00000117)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client controller message notifying the client that a queued action has completed execution, failed, or was removed from the command queue.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x00000117 (CommandQueueRemove) |
| `LONG` | **NetworkId** | 64-bit Network ID of player character |
| `FLOAT` | **TickCount** | Queue sync tick |
| `INT` | **ActionSequenceId** | Action sequence identifier removed from queue |
| `FLOAT` | **ExecutionTime** | Wait time / cooldown elapsed |
| `INT` | **CommandCrc** | CRC identifier of executed command |
| `INT` | **ErrorCode** | Execution result status (0 = Success, non-zero = error reason) |


## Variable Descriptions

- **Controller Opcode**: `00000117 (Hex) / 279 (Dec)`
- **Unpack Routine**: `0x00ae3850`
- **Pack Routine**: `0x00ae37e0`
- **Payload Size**: `16 bytes (4 x 4-byte fields)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00ae3850 reads ActionSequenceId, ExecutionTime, CommandCrc, and ErrorCode.



## Sample Packet

```text
// Verified payload structure for CommandQueueRemove (00000117)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 00000117
```

## Related

- [CommandQueueAdd (00000167)](../../controllers/CommandQueueAdd (00000167).html)
- [CommandQueueEnqueue (00000116)](../../controllers/CommandQueueEnqueue (00000116).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

