---
title: "QuestTaskCounterMessage (00000440)"
displaytitle: "QuestTaskCounterMessage (00000440)"
opcode: "00000440"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "S→C"
completion: "0%"
sample_status: "absent"
status: "stub"
---

# QuestTaskCounterMessage (00000440)

> [!CAUTION]
> **Documentation Pending / Reversal Needed**
> This packet was identified in SWG network specifications (Opcode: `00000440`), but requires packet captures to fully verify all payload offsets.

Server-to-client controller message updating task objective counters (kills, collections, deliveries) in the player Quest Journal.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `INT` | **Operand_Count** | 0x0000000B (ObjControllerMessage wrapper) |
| `INT` | **ControllerOpcode** | 0x00000440 |
| `LONG` | **PlayerId** | Network ID of target player creature object |
| `INT` | **TickCount** | Tick counter |
| `INT` | **QuestCrc** | CRC identifier of active quest |
| `INT` | **TaskId** | Identifier of specific quest task / step |
| `INT` | **CurrentCount** | Updated counter progress value |
| `INT` | **TotalRequired** | Target objective requirement count |


## Variable Descriptions

- **Controller Opcode**: `00000440 (Hex) / 1088 (Dec)`
- **Subsystem**: `Quest / Mission System`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Precedes QuestTaskTimerMessage (00000441) and QuestTaskTimerData (00000444) in the quest controller sequence.



## Sample Packet

```text
// Sample packet capture pending for opcode 00000440
```

## Related

- [QuestTaskTimerMessage (00000441)](../../controllers/QuestTaskTimerMessage (00000441).html)
- [QuestTaskTimerData (00000444)](../../controllers/QuestTaskTimerData (00000444).html)
- [RequestActivateQuest (000004B7)](../../controllers/RequestActivateQuest (000004B7).html)

