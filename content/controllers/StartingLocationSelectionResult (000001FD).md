---
title: "StartingLocationSelectionResult (000001FD)"
displaytitle: "StartingLocationSelectionResult (000001FD)"
opcode: "000001FD"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# StartingLocationSelectionResult (000001FD)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client controller message sent during character creation confirming or rejecting the selected starting city location.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x000001FD (StartingLocationSelectionResult) |
| `LONG` | **NetworkId** | 64-bit Network ID of newly created character |
| `FLOAT` | **TickCount** | Creation session tick |
| `ASCII` | **LocationName** | Starting city / planetary location name string |
| `BYTE` | **ResultCode** | Status result code (0 = Accepted / Success, 1 = Error / Unavailable) |


## Variable Descriptions

- **Controller Opcode**: `000001FD (Hex) / 509 (Dec)`
- **Unpack Routine**: `0x011965b0`
- **Pack Routine**: `0x01196530`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x011965b0 deserializes std::string LocationName and uint8 ResultCode.



## Sample Packet

```text
// Verified payload structure for StartingLocationSelectionResult (000001FD)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 000001FD
```

## Related

- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

