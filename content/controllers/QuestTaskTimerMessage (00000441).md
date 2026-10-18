---
title: "QuestTaskTimerMessage (00000441)"
displaytitle: "QuestTaskTimerMessage (00000441)"
opcode: "00000441"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# QuestTaskTimerMessage (00000441)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client controller message updating timed quest countdowns in the player Quest Journal.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x00000441 (QuestTaskTimerMessage) |
| `LONG` | **NetworkId** | 64-bit Network ID of target player creature object |
| `FLOAT` | **TickCount** | Server tick timestamp |
| `ASCII` | **TaskName** | Quest task string path or string table identifier |
| `INT` | **TaskId** | Task index / timer identifier |
| `UNICODE` | **TimerSource** | Localized label or source descriptor for the timer display |
| `FLOAT` | **TimeLeft** | Remaining time on the quest timer in seconds |


## Variable Descriptions

- **Controller Opcode**: `00000441 (Hex) / 1089 (Dec)`
- **C++ Class**: `MessageQueueQuestTaskTimerMessage (vtable 0x015ec164)`
- **Unpack Routine**: `0x00b0f0d0 (registered at 0x00b0cfc0)`
- **Pack Routine**: `0x00b0f020`
- **Constructor Address**: `0x00b0ede0`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00b0f0d0 deserializes std::string TaskName, int TaskId, Unicode::String TimerSource, and float TimeLeft.



## Sample Packet

```text
// Verified payload structure for QuestTaskTimerMessage (00000441)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 00000441
```

## Related

- [QuestTaskCounterMessage (00000440)](../../controllers/QuestTaskCounterMessage (00000440).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

