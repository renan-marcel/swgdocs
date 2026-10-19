---
title: "SuiUpdatePageMessage"
displaytitle: "SuiUpdatePageMessage (5F3342F6)"
opcode: "5F3342F6"
section: "protocols"
category: "Scripted User Interface (SUI)"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# SuiUpdatePageMessage (5F3342F6)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client Scripted User Interface (SUI) update message that modifies properties and data in an active client dialog window without closing it.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x5F3342F6 (SuiUpdatePageMessage) |
| `INT` | **PageId** | Active SUI dialog window identifier |
| `INT` | **UpdateType** | SUI page update modifier type |
| `ASCII` | **PropertyPath** | UI widget path or property key being updated |
| `UNICODE` | **PropertyValue** | New localized string value or property data |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `5F3342F6 (SuiUpdatePageMessage)`
- **C++ Class**: `SuiUpdatePageMessage (vtables 0x015ebe60, 0x015ebe58)`
- **Constructor Address**: `0x00b002bf (ReadIterator ctor)`
- **Serialization Mechanism**: `AutoDeltaVariable<SuiPageData> containing delta property commands`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00b002bf unpacks PageId and the delta variable update payload for the active SUI page tree.

> [!NOTE]
> **Dynamic SUI Updates**: Allows dynamic UI dialogs (such as countdowns, auction bids, inventory pickers, and terminal lists) to refresh contents without flickering or closing the window.



## Sample Packet

```text
02 00 f6 42 33 5f 05 00 00 00 01 00 00 00 06 00 70 72 6f 6d 70 74 04 00 00 00 54 00 65 00 73 00 74 00
```

## Related

- [SuiCreatePageMessage](../../protocols/SuiCreatePageMessage.html)
- [SuiEventNotification](../../protocols/SuiEventNotification.html)

