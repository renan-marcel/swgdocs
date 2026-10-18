---
title: "QuestTaskCounterMessage (00000440)"
displaytitle: "QuestTaskCounterMessage (00000440)"
opcode: "00000440"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# QuestTaskCounterMessage (00000440)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client controller message updating task objective counters (kills, collections, crafting steps, deliveries) in the player Quest Journal.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags (e.g. 0x00000004) |
| `INT` | **MessageId** | 0x00000440 (QuestTaskCounterMessage) |
| `LONG` | **NetworkId** | 64-bit Network ID of target player creature object |
| `FLOAT` | **TickCount** | Server tick timestamp |
| `ASCII` | **TaskName** | Quest task string path or string table identifier |
| `INT` | **TaskId** | Task index / counter identifier |
| `UNICODE` | **CounterSource** | Localized label or source descriptor for the counter display |
| `INT` | **Count** | Current counter progress value achieved by the player |
| `INT` | **MaxCount** | Target / threshold counter value required for task completion |


## Variable Descriptions

- **Controller Opcode**: `00000440 (Hex) / 1088 (Dec)`
- **C++ Class**: `MessageQueueQuestTaskCounterMessage (vtable 0x015ec16c)`
- **Unpack Routine**: `0x00b0f6f0 (registered at 0x00b0cdd1)`
- **Pack Routine**: `0x00b0f630`
- **Constructor Address**: `0x00b0f3f0`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. ControllerMessageFactory handler at 0x00b0f6f0 unpacks std::string TaskName, int TaskId, Unicode::String CounterSource, int Count, and int MaxCount before instantiating MessageQueueQuestTaskCounterMessage.

> [!NOTE]
> **Quest Journal Integration**: The client PlayerQuestManager updates the UI progress bar and objective text when Count reaches or exceeds MaxCount.



## Sample Packet

```text
// Verified payload structure for QuestTaskCounterMessage (00000440)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 00000440
```

## Related

- [QuestTaskTimerMessage (00000441)](../../controllers/QuestTaskTimerMessage (00000441).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

