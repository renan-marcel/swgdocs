---
title: "ImageDesignStartMessage (0000022A)"
displaytitle: "ImageDesignStartMessage (0000022A)"
opcode: "0000022A"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "C↔S"
completion: "100%"
sample_status: "present"
status: "verified"
---

# ImageDesignStartMessage (0000022A)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Controller message initializing an Image Design customization session between an image designer and a client character.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | 0x0005 (ObjControllerMessage wrapper) |
| `INT` | **Opcode** | 0x80CE5E46 (ObjControllerMessage) |
| `INT` | **Flags** | Delivery reliability flags |
| `INT` | **MessageId** | 0x0000022A (ImageDesignStartMessage) |
| `LONG` | **NetworkId** | 64-bit Network ID of image designer or client |
| `FLOAT` | **TickCount** | Session tick counter |
| `INT` | **SessionType** | Image design session type / configuration identifier |


## Variable Descriptions

- **Controller Opcode**: `0000022A (Hex) / 554 (Dec)`
- **C++ Class**: `MessageQueueImageDesign (vtable 0x015eab98)`
- **Unpack Routine**: `0x00ac80c0`
- **Pack Routine**: `0x00ac80a0`
- **Payload Size**: `4 bytes (1 x 4-byte INT)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Unpack routine 0x00ac80c0 reads 4 bytes into SessionType and constructs MessageQueueImageDesign.



## Sample Packet

```text
// Verified payload structure for ImageDesignStartMessage (0000022A)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: 0000022A
```

## Related

- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

